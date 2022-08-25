from itertools import combinations
import itertools
import time
start = time.time()
mo = open("C:/Users/admin/Desktop/in.inp.txt","r")
# lấy dữ liệu số người hướng dẫn viên và số địa điểm
dulieu = mo.readline().split()
# tạo biến để lưu số khách chưa đc hd ít nhất
luu = "check"
# tạo 1 mảng để lưu các địa điểm
mang = []
# số khác chưa được hướng dẫn
sokhach = 0
# cho các dữ liệu của địa điểm vào mảng
for i in range(int(dulieu[1])) :
    mang.append(mo.readline().split())
# số khách lúc đầu
for i in mang :
    sokhach += int(i[0])
# hoán vị các địa điểm rồi kiểm tra từng hoán vị đó 
mang = list(itertools.permutations(mang))
# duyệt qua từng hoán vị 
for i in mang :
    huongdan = int(dulieu[0])
    save = sokhach
    for j in i :
        tong = 0
        while tong < int(j[0]) :
            if huongdan == 0 :
                if luu == "check" :
                    luu = save
                elif save < luu :
                    luu = save
                break 
            if (int(j[0]) - tong) < int(j[1]) :
                save -= (int(j[0]) - int(j[1]))
            else :
                save -= int(j[1])
            tong += int(j[1])
            huongdan -= 1
        if huongdan ==0 :
            if save < luu :
                luu = save
            break
print(luu)
end = time.time()
print(end-start)


        