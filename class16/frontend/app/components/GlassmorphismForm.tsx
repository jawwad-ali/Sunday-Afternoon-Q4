'use client';

import { FormEvent, useState, useEffect } from 'react';

interface Blog {
  id: string;
  title: string;
  description: string;
  createdAt?: string;
}

export default function GlassmorphismForm() {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [validationErrors, setValidationErrors] = useState<{ [key: string]: string }>({});
  const [blogs, setBlogs] = useState<Blog[]>([]);
  const [loadingBlogs, setLoadingBlogs] = useState(false);

  // Fetch blogs on component mount
  useEffect(() => {
    fetchBlogs();
  }, []);

  const fetchBlogs = async () => {
    setLoadingBlogs(true);
    try {
      const response = await fetch('http://localhost:8000/api/blogs');
      if (!response.ok) {
        throw new Error('Failed to fetch blogs');
      }
      const data = await response.json();
      setBlogs(Array.isArray(data) ? data : data.blogs || []);
    } catch (err) {
      console.error('Error fetching blogs:', err);
      setBlogs([]);
    } finally {
      setLoadingBlogs(false);
    }
  };

  const validateForm = () => {
    const errors: { [key: string]: string } = {};

    if (!formData.title.trim()) {
      errors.title = 'Title is required';
    }
    if (!formData.description.trim()) {
      errors.description = 'Description is required';
    }

    setValidationErrors(errors);
    return Object.keys(errors).length === 0;
  };

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
    // Clear validation error for this field
    if (validationErrors[name]) {
      setValidationErrors((prev) => {
        const newErrors = { ...prev };
        delete newErrors[name];
        return newErrors;
      });
    }
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setError('');
    setSuccess('');

    // Validate form
    if (!validateForm()) {
      return;
    }

    setLoading(true);

    try {
      const response = await fetch('http://localhost:8000/api/blogs', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title: formData.title,
          description: formData.description,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.message || 'Failed to create blog');
      }

      const newBlog = await response.json();

      // Show success message
      setSuccess('Blog created successfully!');

      // Clear form
      setFormData({ title: '', description: '' });

      // Refresh blogs list
      await fetchBlogs();

      // Clear success message after 3 seconds
      setTimeout(() => setSuccess(''), 3000);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'An error occurred';
      setError(errorMessage);
      console.error('Error creating blog:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="relative min-h-screen w-full overflow-hidden bg-black flex flex-col items-center justify-center p-4">
      {/* Animated background elements */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute -top-40 -right-40 w-80 h-80 bg-white/15 rounded-full blur-3xl animate-pulse"></div>
        <div className="absolute -bottom-40 -left-40 w-80 h-80 bg-white/10 rounded-full blur-3xl animate-pulse" style={{ animationDelay: '1s' }}></div>
      </div>

      {/* Form Container */}
      <div className="relative z-10 w-full max-w-4xl">
        {/* 45 Degree Line */}
        <div className="flex justify-center mb-12">
          <div className="w-48 h-1.5 bg-white transform -rotate-45 shadow-lg"></div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
          {/* Form Section */}
          <div className="glassmorphism-form rounded-2xl border border-white/40 bg-white/20 p-8 shadow-2xl backdrop-blur-xl">
            {/* Header */}
            <div className="mb-8 text-center">
              <h1 className="text-3xl font-bold text-white mb-2">
                Create Blog
              </h1>
              <p className="text-white/80 text-sm">
                Share your thoughts with the world
              </p>
            </div>

            {/* Error Message */}
            {error && (
              <div className="mb-4 p-4 rounded-lg bg-red-500/20 border border-red-500/50 text-red-200 text-sm">
                {error}
              </div>
            )}

            {/* Success Message */}
            {success && (
              <div className="mb-4 p-4 rounded-lg bg-green-500/20 border border-green-500/50 text-green-200 text-sm">
                {success}
              </div>
            )}

            {/* Form */}
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Title Input */}
              <div className="relative">
                <label htmlFor="title" className="block text-sm font-medium text-white mb-2">
                  Title
                </label>
                <input
                  type="text"
                  id="title"
                  name="title"
                  value={formData.title}
                  onChange={handleChange}
                  placeholder="Enter blog title..."
                  disabled={loading}
                  className={`w-full px-4 py-3 rounded-lg bg-white/20 border text-white placeholder-white/50 focus:outline-none focus:bg-white/30 transition-all duration-300 backdrop-blur-sm disabled:opacity-50 disabled:cursor-not-allowed ${
                    validationErrors.title
                      ? 'border-red-500/70 focus:border-red-500'
                      : 'border-white/40 focus:border-white/60'
                  }`}
                />
                {validationErrors.title && (
                  <p className="mt-1 text-sm text-red-300">{validationErrors.title}</p>
                )}
              </div>

              {/* Description Textarea */}
              <div className="relative">
                <label htmlFor="description" className="block text-sm font-medium text-white mb-2">
                  Description
                </label>
                <textarea
                  id="description"
                  name="description"
                  value={formData.description}
                  onChange={handleChange}
                  placeholder="Enter blog description..."
                  disabled={loading}
                  rows={5}
                  className={`w-full px-4 py-3 rounded-lg bg-white/20 border text-white placeholder-white/50 focus:outline-none focus:bg-white/30 transition-all duration-300 backdrop-blur-sm resize-none disabled:opacity-50 disabled:cursor-not-allowed ${
                    validationErrors.description
                      ? 'border-red-500/70 focus:border-red-500'
                      : 'border-white/40 focus:border-white/60'
                  }`}
                />
                {validationErrors.description && (
                  <p className="mt-1 text-sm text-red-300">{validationErrors.description}</p>
                )}
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={loading}
                className="w-full mt-8 px-6 py-3 rounded-lg font-semibold text-white bg-white/30 border border-white/50 hover:bg-white/40 hover:border-white/70 hover:shadow-2xl transition-all duration-300 backdrop-blur-sm transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100"
              >
                {loading ? 'Creating Blog...' : 'Create Blog'}
              </button>
            </form>
          </div>

          {/* Blogs List Section */}
          <div className="glassmorphism-form rounded-2xl border border-white/40 bg-white/20 p-8 shadow-2xl backdrop-blur-xl">
            <div className="mb-8 text-center">
              <h2 className="text-3xl font-bold text-white mb-2">
                Recent Blogs
              </h2>
              <p className="text-white/80 text-sm">
                ({blogs.length} blog{blogs.length !== 1 ? 's' : ''})
              </p>
            </div>

            {loadingBlogs ? (
              <div className="flex items-center justify-center py-12">
                <div className="animate-spin rounded-full h-8 w-8 border border-white/30 border-t-white"></div>
              </div>
            ) : blogs.length === 0 ? (
              <div className="text-center py-12">
                <p className="text-white/60">No blogs yet. Create one to get started!</p>
              </div>
            ) : (
              <div className="space-y-4 max-h-96 overflow-y-auto">
                {blogs.map((blog) => (
                  <div
                    key={blog.id}
                    className="rounded-lg border border-white/30 bg-white/10 p-4 hover:bg-white/15 transition-all duration-300"
                  >
                    <h3 className="font-semibold text-white text-lg mb-2 break-words">
                      {blog.title}
                    </h3>
                    <p className="text-white/70 text-sm line-clamp-2 break-words">
                      {blog.description}
                    </p>
                    {blog.createdAt && (
                      <p className="text-white/50 text-xs mt-2">
                        {new Date(blog.createdAt).toLocaleDateString()}
                      </p>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
