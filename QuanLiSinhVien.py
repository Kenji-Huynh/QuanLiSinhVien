import tkinter as tk
from tkinter import ttk

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản Lý Sinh Viên")

# Tạo frame cho phần nhập liệu
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Label và Entry cho Tên sinh viên
label_name = tk.Label(input_frame, text="Tên sinh viên:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(input_frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Label và Entry cho Tuổi sinh viên
label_age = tk.Label(input_frame, text="Tuổi:")
label_age.grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(input_frame)
entry_age.grid(row=1, column=1, padx=10, pady=5)

# Label và Entry cho Lớp sinh viên
label_class = tk.Label(input_frame, text="Lớp:")
label_class.grid(row=2, column=0, padx=10, pady=5)
entry_class = tk.Entry(input_frame)
entry_class.grid(row=2, column=1, padx=10, pady=5)

# Tạo bảng Treeview để hiển thị danh sách sinh viên
tree_frame = tk.Frame(root)
tree_frame.pack(pady=20)

tree = ttk.Treeview(tree_frame, columns=("Tên", "Tuổi", "Lớp"), show='headings', height=8)
tree.pack()

# Đặt tiêu đề cho các cột
tree.heading("Tên", text="Tên")
tree.heading("Tuổi", text="Tuổi")
tree.heading("Lớp", text="Lớp")

# Định dạng kích thước cột
tree.column("Tên", width=150)
tree.column("Tuổi", width=50)
tree.column("Lớp", width=100)

# Hàm thêm sinh viên vào bảng
def add_student():
    name = entry_name.get()
    age = entry_age.get()
    student_class = entry_class.get()

    if name and age and student_class:
        # Thêm dữ liệu vào bảng Treeview
        tree.insert("", tk.END, values=(name, age, student_class))

        # Xóa nội dung trong các ô nhập liệu sau khi thêm
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_class.delete(0, tk.END)

# Tạo nút "Thêm sinh viên"
add_button = tk.Button(root, text="Thêm Sinh Viên", command=add_student)
add_button.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
