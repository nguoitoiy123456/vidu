tongtien = int(input("Số điền đã có: "))
songuoidonggop = 0
while tongtien <= 100000:
    donggop = int(input("Mời bạn góp tiền uống cafe: "))
    tongtien += donggop
    songuoidonggop += 1
else:
    print("Bạn đã đủ tiền uống cafe, quyên góp để chi! ")
print("Đã quyên góp được {} từ {} người!".format(tongtien, songuoidonggop))    
