"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

export default function GlassForm() {
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [description, setDescription] = useState("");
  const [inStock, setInStock] = useState(true);
  const [submitted, setSubmitted] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    setSubmitted(false);
    setLoading(true);
    try {
      const res = await fetch("http://localhost:8000/products", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name,
          description,
          price: price ? Number(price) : undefined,
          in_stock: inStock,
        }),
      });

      if (!res.ok) {
        let details = "";
        try {
          const payload = await res.json();
          details = typeof payload?.detail === "string" ? payload.detail : JSON.stringify(payload?.detail ?? payload);
        } catch (_) {}
        setError(details || `Request failed (${res.status})`);
        return;
      }

      setSubmitted(true);
      setName("");
      setPrice("");
      setDescription("");
      setInStock(true);
      router.refresh();
    } catch (err: any) {
      setError(err?.message || "Network error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-[#fffb00] to-black p-8">
      <div className="w-full max-w-xl p-8 rounded-3xl bg-white/20 backdrop-blur-xl border border-white/30 shadow-xl text-white">
        <h2 className="mb-4 text-2xl font-bold">Add Product</h2>
        <p className="-mt-2 mb-6 text-white/80">A clean glassmorphism form that’s easy on eyes.</p>
        <form onSubmit={handleSubmit}>
          <div className="grid gap-4">
            <label className="grid gap-2">
              <span className="text-sm opacity-90">Name</span>
              <input
                value={name}
                onChange={(e) => setName(e.target.value)}
                placeholder="Product name"
                className="px-4 py-3 rounded-xl border border-white/40 bg-white/30 text-slate-900 outline-none placeholder-slate-600 focus:ring-2 focus:ring-[#00ffff] focus:border-white/60"
              />
            </label>
            <label className="grid gap-2">
              <span className="text-sm opacity-90">Price</span>
              <input
                value={price}
                onChange={(e) => setPrice(e.target.value)}
                placeholder="0.00"
                type="number"
                step="0.01"
                className="px-4 py-3 rounded-xl border border-white/40 bg-white/30 text-slate-900 outline-none placeholder-slate-600 focus:ring-2 focus:ring-[#00ffff] focus:border-white/60"
              />
            </label>
            <label className="grid gap-2">
              <span className="text-sm opacity-90">Description</span>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Short details"
                rows={4}
                className="px-4 py-3 rounded-xl border border-white/40 bg-white/30 text-slate-900 outline-none placeholder-slate-600 resize-y focus:ring-2 focus:ring-[#00ffff] focus:border-white/60"
              />
            </label>
            <label className="flex items-center gap-2">
              <input
                type="checkbox"
                checked={inStock}
                onChange={(e) => setInStock(e.target.checked)}
                className="accent-[#00ffff]"
              />
              <span className="text-sm opacity-90">In Stock</span>
            </label>
          </div>
          <div className="flex items-center gap-3 mt-6">
            <button
              type="submit"
              className="px-5 py-3 rounded-xl border border-white/40 bg-gradient-to-br from-white/70 to-white/40 text-slate-900 font-semibold cursor-pointer hover:from-white/80 hover:to-white/50 disabled:opacity-50"
              disabled={loading}
            >
              {loading ? "Saving…" : "Save"}
            </button>
            {submitted && (
              <span className="text-white">Submitted!</span>
            )}
            {error && (
              <span className="text-white">Error: {error}</span>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}
