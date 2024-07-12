"use server";

import { revalidatePath } from "next/cache";

// Add Todo
export async function add_todo(
  state: { status: string; message: string },
  formData: FormData
) {
  const new_todo = formData.get("add_task") as string;

  try {
    const response = await fetch("http://127.0.0.1:8000/todos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: new_todo }),
    });
    revalidatePath("/todos");
    const data = await response.json();
    if (data.content) {
      revalidatePath("/todos/");
      return { status: "success", message: "Todo added successfully" };
    } else {
      return { status: "error", message: "Something went wrong" };
    }
  } catch (error) {
    return { status: "error", message: "something went wrong" };
  }
}

// Edit Todo
export async function edit_todo(
  state: { status: string; message: string },
  {
    id,
    content,
    is_Completed,
  }: { id: number; content: string; is_Completed: boolean }
) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        id: id,
        content: content,
        is_Completed: is_Completed,
      }),
    });
    revalidatePath("/todos");
    return { status: "success", message: "todo edited successfully" };
  } catch (error) {
    return { status: "error", message: "something went wrong" };
  }
}

// Status Change todo
export async function status_change(
  id: number,
  content: string,
  is_Completed: boolean
) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        content: content,
        is_Completed: is_Completed,
      }),
    });
    const res = await response.json();
    revalidatePath("/todos");
    return { status: "success", message: "status changed successfully" };
  } catch (error) {
    return { status: "error", message: "something went wrong" };
  }
}

// Delete Todo
export async function delete_todo(id: number) {
  try {
    const response = await fetch(`http://127.0.0.1:8000/todos/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });
    revalidatePath("/todos");
    return { status: "success", message: "Task deleted successfully" };
  } catch (error) {
    return { status: "error", message: "Something went wrong" };
  }
}
