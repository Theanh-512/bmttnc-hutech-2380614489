from QuanLySinhVien import QuanLySinhVien

def main():
    manager = QuanLySinhVien()

    while True:
        print("\n--- MENU QUẢN LÝ SINH VIÊN ---")
        print("1. Thêm sinh viên")
        print("2. Cập nhật thông tin sinh viên theo ID")
        print("3. Xóa sinh viên theo ID")
        print("4. Tìm kiếm sinh viên qua tên")
        print("5. Sắp xếp danh sách sinh viên theo điểm trung bình")
        print("6. Sắp xếp danh sách sinh viên theo tên chuyên ngành")
        print("7. Hiển thị danh sách sinh viên")
        print("8. Thoát")
        choice = input("Vui lòng chọn một tùy chọn: ")

        if choice == "1":
            name = input("Nhập tên sinh viên: ")
            gender = input("Nhập giới tính: ")
            major = input("Nhập chuyên ngành: ")
            try:
                avg_score = float(input("Nhập điểm trung bình (hệ 10): "))
                manager.add_student(name, gender, major, avg_score)
            except ValueError:
                print("Điểm trung bình phải là một số hợp lệ.")

        elif choice == "2":
            try:
                student_id = int(input("Nhập ID sinh viên cần cập nhật: "))
                name = input("Nhập tên mới (nhấn Enter để bỏ qua): ")
                gender = input("Nhập giới tính mới (nhấn Enter để bỏ qua): ")
                major = input("Nhập chuyên ngành mới (nhấn Enter để bỏ qua): ")
                avg_score_input = input("Nhập điểm trung bình mới (nhấn Enter để bỏ qua): ")
                avg_score = float(avg_score_input) if avg_score_input else None
                manager.update_student(student_id, name, gender, major, avg_score)
            except ValueError:
                print("ID hoặc điểm trung bình không hợp lệ.")

        elif choice == "3":
            try:
                student_id = int(input("Nhập ID sinh viên cần xóa: "))
                manager.delete_student(student_id)
            except ValueError:
                print("ID không hợp lệ.")

        elif choice == "4":
            name = input("Nhập tên sinh viên cần tìm: ")
            manager.search_student_by_name(name)

        elif choice == "5":
            manager.sort_students_by_score()
            manager.display_students()

        elif choice == "6":
            manager.sort_students_by_major()
            manager.display_students()

        elif choice == "7":
            manager.display_students()

        elif choice == "8":
            print("Thoát chương trình. Tạm biệt!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
            
if __name__ == "__main__":
    main()