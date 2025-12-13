import GlassForm from "../components/GlassForm";
import ProductTable from "../components/ProductTable";

export default async function Home() {
    return (
      <main>
      <ProductTable />
      <GlassForm />
      </main>
    );
}
