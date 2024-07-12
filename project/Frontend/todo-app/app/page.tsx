import TodoTable from "@/components/TodoTable";
import { Modal } from "@/components/ui/Modal";
import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <main className="max-w-5xl mx-auto mt-8">
      <section>
        <Modal title="Add new Task" Adding={true}>
          <Button
            variant="default"
            className="w-full bg-teal-600 px-2 py-1 text-white uppercase text-lg"
          >
            Add Task
          </Button>
        </Modal>
      </section>
      <section className="mt-4">
        <TodoTable />
      </section>
    </main>
  );
}
