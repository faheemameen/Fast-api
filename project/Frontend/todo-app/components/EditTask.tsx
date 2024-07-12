"use client";
import { Todo } from "../../types";
import { useFormState } from "react-dom";
import SubmitButton from "./SubmitButton";
import { useEffect, useState } from "react";
import toast from "react-hot-toast";
import { edit_todo } from "@/action/action";

export default function EditTask({ task }: { task: Todo }) {
  const [value, setValue] = useState(task.content);
  const [state, formAction] = useFormState(edit_todo, {
    status: "",
    message: "",
  });
  const { status, message } = state;

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
  };

  const handleSubmit = (formData: FormData) => {
    const id: number = task.id;
    const content: string = formData.get("edit_task") as string;
    const is_Completed: boolean = task.is_Completed;
    formAction({ id, content, is_Completed });
  };
  useEffect(() => {
    if (status == "success") {
      toast.success(message);
    } else if (status == "error") {
      toast.error(message);
    }
  }, [state]);
  return (
    <form
      action={handleSubmit}
      className="flex flex-col justify-between items-center gap-x-4 w-full"
    >
      <input
        onChange={handleChange}
        type="text"
        minLength={3}
        maxLength={54}
        required
        name="edit_task"
        value={value}
        className="w-full px-2 py-1 border border-gray-100 rounded-md"
      />
      <SubmitButton />
    </form>
  );
}
