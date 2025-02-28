def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:  # Kiểm tra chia hết cho i
            return False  # Nếu chia hết, n không phải số nguyên tố
    return True  # Nếu không tìm thấy ước số nào, n là số nguyên tố


number = int(input("Nhập vào số cần kiểm tra: "))
if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải số nguyên tố.")
