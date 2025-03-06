class SinhVien:
    id_counter = 1  # Biến tĩnh để tự động tăng mã sinh viên

    def __init__(self, name, gender, major, avg_score):
        self.id = SinhVien.id_counter
        SinhVien.id_counter += 1
        self.name = name
        self.gender = gender
        self.major = major
        self.avg_score = avg_score

    def get_academic_performance(self):
        if self.avg_score >= 8:
            return "Giỏi"
        elif self.avg_score >= 6.5:
            return "Khá"
        elif self.avg_score >= 5:
            return "Trung bình"
        else:
            return "Yếu"

    def __str__(self):
        return (f"ID: {self.id}, Tên: {self.name}, Giới tính: {self.gender}, "
                f"Chuyên ngành: {self.major}, Điểm trung bình: {self.avg_score}, "
                f"Học lực: {self.get_academic_performance()}")
        
    def __str__(self):
        return (f"{self.id:<10}{self.name:<15}{self.gender:<10}{self.major:<15}"
                f"{self.avg_score:<10}{self.get_academic_performance()}")