j = []
# duyệt qua số từ 2000 đến 3200, ktra chia hết cho 7 , không phải bội số của 5
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        j.append(str(i))
print (','.join(j))