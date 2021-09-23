

#while(True):
    #print("0: Thoát")
    # print("2: Sắp xếm sinh viên theo điểm")
    #print("3: Tìm kiếm sinh viên")
    #print("4: Hiển thị bảng điểm sinh viên")
    #chon = int(input("Mời bạn chọn: "))
    #if chon == 0: break


dayso = []
for i in range(2000, 3201):
    if ( i % 7 == 0) and ( i % 5!= 0):
        dayso.append(str(i))

print(', '.join(dayso))


