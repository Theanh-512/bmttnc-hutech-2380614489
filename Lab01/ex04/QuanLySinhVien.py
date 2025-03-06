from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.students = []

    def add_student(self, name, gender, major, avg_score):
        student = SinhVien(name, gender, major, avg_score)
        self.students.append(student)
        print("Đã thêm sinh viên: {student}")

    def update_student(self, student_id, name=None, gender=None, major=None, avg_score=None):
        for student in self.students:
            if student.id == student_id:
                if name:
                    student.name = name
                if gender:
                    student.gender = gender
                if major:
                    student.major = major
                if avg_score is not None:
                    student.avg_score = avg_score
                print(f"Đã cập nhật thông tin sinh viên: {student}")
                return
        print("Không tìm thấy sinh viên với ID này.")

    def delete_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                self.students.remove(student)
                print(f"Đã xóa sinh viên với ID: {student_id}")
                return
        print("Không tìm thấy sinh viên với ID này.")

    def search_student_by_name(self, name):
        results = [student for student in self.students if name.lower() in student.name.lower()]
        if results:
            print("Kết quả tìm kiếm:")
            for student in results:
                print(student)
        else:
            print("Không tìm thấy sinh viên nào với tên này.")

    def sort_students_by_score(self):
        self.students.sort(key=lambda student: student.avg_score, reverse=True)
        print("Danh sách sinh viên đã được sắp xếp theo điểm trung bình.")

    def sort_students_by_major(self):
        self.students.sort(key=lambda student: student.major)
        print("Danh sách sinh viên đã được sắp xếp theo chuyên ngành.")

    def display_students(self):
        if not self.students:
            print("Danh sách sinh viên trống.")
        else:
            print("Danh sách sinh viên:")
            for student in self.students:
                print(student)