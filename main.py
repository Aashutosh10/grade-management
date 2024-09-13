import tkinter as tk
from tkinter import messagebox

class GradeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grades Management")
        self.root.configure(bg="#f0f0f0")  # Set the background color

        self.student_grades = {}

        self.create_widgets()

    def create_widgets(self):
        self.add_grade_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.add_grade_frame.pack(pady=10)

        self.name_label = tk.Label(self.add_grade_frame, text="Student Name:", bg="#f0f0f0")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.add_grade_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.subject_label = tk.Label(self.add_grade_frame, text="Subject:", bg="#f0f0f0")
        self.subject_label.grid(row=1, column=0, padx=5, pady=5)
        self.subject_var = tk.StringVar(self.root)
        self.subject_var.set("Math")  # default value
        self.subject_menu = tk.OptionMenu(self.add_grade_frame, self.subject_var, "Math", "Science", "English", "History")
        self.subject_menu.grid(row=1, column=1, padx=5, pady=5)

        self.grade_label = tk.Label(self.add_grade_frame, text="Grade:", bg="#f0f0f0")
        self.grade_label.grid(row=2, column=0, padx=5, pady=5)
        self.grade_entry = tk.Entry(self.add_grade_frame)
        self.grade_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.add_grade_frame, text="Add Grade", command=self.add_student_grade, bg="#4CAF50", fg="white")
        self.add_button.grid(row=3, columnspan=2, pady=10)

        self.view_button = tk.Button(self.root, text="View All Student Grades", command=self.view_all_student_grades, bg="#2196F3", fg="white")
        self.view_button.pack(pady=5)

        self.compute_button = tk.Button(self.root, text="Compute Average Grade", command=self.compute_average_grades, bg="#FF9800", fg="white")
        self.compute_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit, bg="#f44336", fg="white")
        self.exit_button.pack(pady=5)

    def add_student_grade(self):
        student_name = self.name_entry.get().strip()
        subject = self.subject_var.get()
        grade_input = self.grade_entry.get().strip()

        if not grade_input.replace('.', '', 1).isdigit():
            messagebox.showerror("Invalid Input", "Grade must be a numeric value.")
            return

        grade = float(grade_input)
        if student_name in self.student_grades:
            if subject in self.student_grades[student_name]:
                self.student_grades[student_name][subject].append(grade)
            else:
                self.student_grades[student_name][subject] = [grade]
        else:
            self.student_grades[student_name] = {subject: [grade]}

        self.name_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Grade {grade} added for student {student_name} in subject {subject}.")

    def view_all_student_grades(self):
        if not self.student_grades:
            messagebox.showinfo("No Data", "No student grades available.")
            return

        all_grades = ""
        for student_name, subjects in self.student_grades.items():
            all_grades += f"Student: {student_name}\n"
            for subject, grades in subjects.items():
                all_grades += f"  Subject: {subject}, Grades: {grades}\n"

        messagebox.showinfo("All Student Grades", all_grades)

    def compute_average_grades(self):
        if not self.student_grades:
            messagebox.showinfo("No Data", "No student grades available.")
            return

        averages = ""
        for student_name, subjects in self.student_grades.items():
            total_grades = []
            for grades in subjects.values():
                total_grades.extend(grades)
            if total_grades:
                average_grade = sum(total_grades) / len(total_grades)
                averages += f"Student: {student_name}, Average Grade: {average_grade:.2f}\n"
            else:
                averages += f"Student: {student_name} has no grades.\n"

        messagebox.showinfo("Average Grades", averages)

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeManager(root)
    root.mainloop()
