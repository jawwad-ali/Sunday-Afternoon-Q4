interface Blog {
  id: number;
  title: string;
  slug: string;
  content: string;
  author: string;
  date: string;
}

interface BlogCardProps {
  blog: Blog;
}

const gradients = [
  "from-violet-500 to-purple-600",
  "from-pink-500 to-rose-500",
  "from-cyan-500 to-blue-500",
  "from-emerald-500 to-teal-500",
  "from-orange-500 to-amber-500",
];

export default function BlogCard({ blog }: BlogCardProps) {
  const gradient = gradients[(blog.id - 1) % gradients.length];

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString("en-US", {
      month: "short",
      day: "numeric",
      year: "numeric",
    });
  };

  return (
    <article className="group relative overflow-hidden rounded-2xl bg-white shadow-lg transition-all duration-300 hover:shadow-2xl hover:-translate-y-2">
      {/* Gradient Header */}
      <div className={`h-32 bg-gradient-to-r ${gradient} relative overflow-hidden`}>
        <div className="absolute inset-0 bg-black/10"></div>
        <div className="absolute -bottom-6 -right-6 h-24 w-24 rounded-full bg-white/20 blur-xl"></div>
        <div className="absolute -top-6 -left-6 h-20 w-20 rounded-full bg-white/10 blur-lg"></div>
      </div>

      {/* Content */}
      <div className="p-6">
        {/* Date Badge */}
        <div className="mb-4 -mt-10 relative z-10">
          <span className="inline-block rounded-full bg-white px-4 py-2 text-sm font-medium text-gray-600 shadow-md">
            {formatDate(blog.date)}
          </span>
        </div>

        {/* Title */}
        <h2 className="mb-3 text-xl font-semibold text-gray-800 line-clamp-2 group-hover:text-violet-600 transition-colors">
          {blog.title}
        </h2>

        {/* Content Preview */}
        <p className="mb-4 text-gray-600 text-sm leading-relaxed line-clamp-3">
          {blog.content}
        </p>

        {/* Footer */}
        <div className="flex items-center justify-between pt-4 border-t border-gray-100">
          {/* Author */}
          <div className="flex items-center gap-3">
            <div className={`h-10 w-10 rounded-full bg-gradient-to-r ${gradient} flex items-center justify-center text-white font-semibold text-sm`}>
              {blog.author.split(" ").map(n => n[0]).join("")}
            </div>
            <span className="text-sm font-medium text-gray-700">{blog.author}</span>
          </div>

          {/* Read More */}
          <button className="flex items-center gap-1 text-sm font-medium text-violet-600 hover:text-violet-700 transition-colors">
            Read More
            <svg
              className="h-4 w-4 transition-transform group-hover:translate-x-1"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
            </svg>
          </button>
        </div>
      </div>
    </article>
  );
}
