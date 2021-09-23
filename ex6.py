sanpham = {
    "thuonghieu": "Apple",
    "sacnhanh": True,
    "namsx" : 2021,
    "mausac" : ["Xanh", "Hồng", "Đen"]
}

print(sanpham)

print(sanpham["thuonghieu"])
print(sanpham.keys())

sanpham.update({"thuonghieu":"SamSung"})
sanpham.update({"trongluong":"0.5 kg"})
print(sanpham)