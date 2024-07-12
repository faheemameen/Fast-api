"use client";
import { add_todo } from "@/action/action";
import { useFormState } from "react-dom";
import { useRef, useEffect } from "react";
import toast from "react-hot-toast";
import SubmitButton from "./SubmitButton";

export default function AddTask() {
  const ref = useRef<HTMLFormElement>(null);
  const [state, formAction] = useFormState(add_todo, {
    status: "",
    message: "",
  });
  const { status, message } = state;

  useEffect(() => {
    if (status == "success") {
      ref.current?.reset();
      toast.success(message);
    } else if (status == "error") {
      toast.error(message);
    }
  }, [state]);
  return (
    <form
      ref={ref}
      action={formAction}
      className="flex flex-col justify-between items-center gap-x-3 w-full"
    >
      <input
        type="text"
        placeholder="add task here"
        minLength={3}
        maxLength={54}
        required
        name="add_task"
        className="w-full px-2 py-1 border border-gray-100 rounded-md"
      />
      <SubmitButton />
    </form>
  );
}
