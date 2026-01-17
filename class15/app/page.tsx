import BlogCard from "./components/BlogCard";
import blogs from "./data/blogs.json";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 via-white to-violet-50">
      {/* Header */}
      <header className="pt-16 pb-12 px-6">
        <div className="max-w-6xl mx-auto text-center">
          <h1 className="text-5xl font-bold text-gray-800 mb-4">
            My <span className="text-transparent bg-clip-text bg-gradient-to-r from-violet-600 to-purple-600">Blog</span>
          </h1>
          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Discover insights, tutorials, and stories from our team of passionate developers and designers.
          </p>
        </div>
      </header>

      {/* Blog Grid */}
      <main className="px-6 pb-20">
        <div className="max-w-6xl mx-auto grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {blogs.map((blog) => (
            <BlogCard key={blog.id} blog={blog} />
          ))}
        </div>
      </main>

      {/* Footer */}
      <footer className="py-8 border-t border-gray-100 bg-white/50">
        <p className="text-center text-gray-500 text-sm">
          Made with Next.js & Tailwind CSS
        </p>
      </footer>
    </div>
  );
}
