import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("800x600")

        self.students = {}
        self.student_id = 1

        # Style Configuration
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        # Title Label
        title_label = ttk.Label(self.root, text="Student Management System", font=("Arial", 18))
        title_label.pack(pady=10)

        # Entry Fields
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.course_var = tk.StringVar()

        ttk.Label(self.root, text="Name").pack(pady=5)
        self.name_entry = ttk.Entry(self.root, textvariable=self.name_var)
        self.name_entry.pack(pady=5)

        ttk.Label(self.root, text="Age").pack(pady=5)
        self.age_entry = ttk.Entry(self.root, textvariable=self.age_var)
        self.age_entry.pack(pady=5)

        ttk.Label(self.root, text="Course").pack(pady=5)
        self.course_entry = ttk.Entry(self.root, textvariable=self.course_var)
        self.course_entry.pack(pady=5)

        # Buttons
        add_button = ttk.Button(self.root, text="Add Student", command=self.add_student)
        add_button.pack(pady=10)

        view_button = ttk.Button(self.root, text="View Students", command=self.view_students)
        view_button.pack(pady=10)

        update_button = ttk.Button(self.root, text="Update Student", command=self.update_student)
        update_button.pack(pady=10)

        delete_button = ttk.Button(self.root, text="Delete Student", command=self.delete_student)
        delete_button.pack(pady=10)

    def add_student(self):
        name = self.name_var.get()
        age = self.age_var.get()
        course = self.course_var.get()

        if name and age and course:
            self.students[self.student_id] = {"Name": name, "Age": age, "Course": course}
            self.student_id += 1
            messagebox.showinfo("Success", "Student added successfully!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_students(self):
        if self.students:
            students_info = "\n".join([f"ID: {sid}, Name: {info['Name']}, Age: {info['Age']}, Course: {info['Course']}"
                                       for sid, info in self.students.items()])
            messagebox.showinfo("Student List", students_info)
        else:
            messagebox.showinfo("No Data", "No students found.")

    def update_student(self):
        update_window = tk.Toplevel(self.root)
        update_window.title("Update Student")
        update_window.geometry("300x400")

        ttk.Label(update_window, text="Student ID").pack(pady=5)
        id_var = tk.StringVar()
        id_entry = ttk.Entry(update_window, textvariable=id_var)
        id_entry.pack(pady=5)

        ttk.Label(update_window, text="New Name").pack(pady=5)
        new_name_var = tk.StringVar()
        new_name_entry = ttk.Entry(update_window, textvariable=new_name_var)
        new_name_entry.pack(pady=5)

        ttk.Label(update_window, text="New Age").pack(pady=5)
        new_age_var = tk.StringVar()
        new_age_entry = ttk.Entry(update_window, textvariable=new_age_var)
        new_age_entry.pack(pady=5)

        ttk.Label(update_window, text="New Course").pack(pady=5)
        new_course_var = tk.StringVar()
        new_course_entry = ttk.Entry(update_window, textvariable=new_course_var)
        new_course_entry.pack(pady=5)

        def update():
            sid = int(id_var.get())
            if sid in self.students:
                self.students[sid]["Name"] = new_name_var.get()
                self.students[sid]["Age"] = new_age_var.get()
                self.students[sid]["Course"] = new_course_var.get()
                messagebox.showinfo("Success", "Student updated successfully!")
                update_window.destroy()
            else:
                messagebox.showerror("Error", "Student ID not found.")

        ttk.Button(update_window, text="Update", command=update).pack(pady=10)

    def delete_student(self):
        delete_window = tk.Toplevel(self.root)
        delete_window.title("Delete Student")
        delete_window.geometry("300x200")

        ttk.Label(delete_window, text="Student ID").pack(pady=5)
        id_var = tk.StringVar()
        id_entry = ttk.Entry(delete_window, textvariable=id_var)
        id_entry.pack(pady=5)

        def delete():
            sid = int(id_var.get())
            if sid in self.students:
                del self.students[sid]
                messagebox.showinfo("Success", "Student deleted successfully!")
                delete_window.destroy()
            else:
                messagebox.showerror("Error", "Student ID not found.")

        ttk.Button(delete_window, text="Delete", command=delete).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementSystem(root)
    root.mainloop()
