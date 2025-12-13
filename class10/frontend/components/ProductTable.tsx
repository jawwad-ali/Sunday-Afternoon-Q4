export default async function ProductTable() {
  const data = await fetch("http://localhost:8000/products", { cache: "no-store" });
  const result = await data.json();

  return (
    <section className="p-4">
      <div className="overflow-x-auto">
        <table className="min-w-full table-auto border-collapse">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-4 py-3 text-left text-sm font-semibold text-gray-700">Name</th>
              <th className="px-4 py-3 text-left text-sm font-semibold text-gray-700">Description</th>
              <th className="px-4 py-3 text-right text-sm font-semibold text-gray-700">Price</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {result?.map((product: any, idx: number) => (
              <tr key={product?.id ?? idx} className="odd:bg-white even:bg-gray-50">
                <td className="px-4 py-3 font-semibold text-gray-900">{product?.name}</td>
                <td className="px-4 py-3 text-gray-600">{product?.description}</td>
                <td className="px-4 py-3 text-right text-gray-900">${product?.price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}
