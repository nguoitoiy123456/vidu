for x in range(5):
    print(x)
else:
    print("Vòng lặp kết thúc tại x = {}".format(x))


danhsachsv = ["Linh", "Huyền", "Huế", "Phượng", "Vy"]
for sv in danhsachsv:
    print(sv)

for char in danhsachsv[1]:
    print(char)

tong = 0
for i in range(11):
    tong = tong + i

print("Tổng từ 0-10 là: {tong}")