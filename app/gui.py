# app/gui.py

import tkinter as tk
from tkinter import messagebox
from app.logic import TaskManager

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_manager = TaskManager()

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_manager.add_task(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            self.task_manager.remove_task(selected_task_index[0])
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "You must select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.task_manager.tasks:
            self.task_listbox.insert(tk.END, task)
