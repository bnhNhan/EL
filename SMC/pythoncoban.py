
'''
https://www.niemvuilaptrinh.com/article/30-Visual-Studio-Code-Extension-Tot-Nhat-Cho-Phat-Trien-Web2020
https://codelearn.io/sharing/tuy-bien-visual-studio-code-toi-uu-hieu-qua-cong-viec
1. Các Phép toán số học
    + Chia a/b
    + Cộng a+b
    + Nhân a*b
    + Chia a/b
    + Lũy thừa a**b
'''
# chia lấy phần nguyên //
# print(10//3) #3
# chia lấy phânf dư %
# print(10%3) #1
'''
2. Các phép toán so sánh trả về true or false
    + Bằng: a==b
    + a nhỏ hơn b: a<=b
    + a>=b
    + a!=b
3. Phép gán
    + a=b
    + a*=b : a = a*b
'''
'''
4. Phép toán logic and (&&), or (||), not (!, ~)
print(not(True)) # false

'''
'''
5. Thư viện số học
    + max(a)
    + min(a)
    + abs(a): giá trị tuyêt đối
    + round(a): làm tròn
    + sqrt(a); căn bậc 2
6. Hàm ramdom:
from random import randrange
    + random()
    + randrange(a,b): số thưc
    + unifrom(a,b): số nguyên
'''
# 7. Câu lệnh rẽ nhánh
'''
a = int(input('nhập số a')) ; b = int(input('Nhập số b '))

if a <= b:
    print(f'{a} bé hơn {b}')
elif a >= b:
    print(f'{a} lơn hơn {b}')
else:
    print('a khac b')    
'''
# 8. Vòng lặp for
'''
n = int(input('Nhập số n : '))
m = int(input('Nhập số m : '))
c = int(input('Nhập số c : '))
for i in range(m, n+1, c): # m vị trí bắt đầu, n ví trí kết thúc, c bước nhảy
    print(f'số i {i}', end = ' ')
print('', end = '\n')
print('Hiếu Nhân')

for i in a:
    print('số', a)
'''

# 9. Vòng lặp while

'''
a = [3, 5, 7, 9]
h = len(a)
i = 0
while i <= h:
    print(i) 
    i += 1
'''

# 10. Chuỗi String (str)

'''
data = 'hieunhan'
lengdata = len(data)
findata = data[:]
findhieunhan = findata.find('hieunhan') # phân biệt hoa thường tìm thấy trả về vị trí không tìm thấy trả về -1
#indexhieunhan = findata.index('hieunhan') # phân biệt hoa thường tìm thấy trả về vị trí không tìm thấy trả về lỗi

isanfla = data.isalnum() # trả về True or Flase
isNumber = data.isdecimal() # check number return True or Flase

replacedate = data.replace('5', 'cc') # repace 5 become cc

lowerdate = data.lower() # change upper become lower
upperdate = data.upper() # change lower become upper

splitdate = data.split() # chuyển đổi chuỗi thành [] list

print(replacedate)
print(lowerdate)

'''
# 11. Kiểu dữ liệt list []
concu = 222

listnek = [1.2, 2, 5, 8, 'hieunhan']

listone = ['3', '5']

listnek[2] = 'cho'
c = list(listnek)  # ép kiểu dữ liệu
t = 2
if t in listnek:  # kiểm tra t có trong a hay không
    print('co')
if t not in listnek:
    print('có')

del listnek[-1]  # xóa phần tử cưa list

listnek.remove(2)  # xóa phần tử đầu tiên gặp đc trong list không có báo lỗi

listnek.append(listone)  # thêm phần tử vào list địa chỉ id khôn thai đổi

listnek.extend(listone)  # gop 2 mảng listnek + listone nhưng không thai đổi id

# chèm vào vị trí thứ 2 hihi nếu ko có vị trí chèn vào vị trí cuối cùng
listnek.insert(10, 'hihi')
print(listnek)

# list list[]


'''
develop = 'hieunhanhieu'


# thai thế 'nhan' trong chuỗi nếu tìm thấy bằng 1 , số lần thai thế
a = develop.replace('kkk', '1', 1)

print(develop, a)

developer = 'Jessica Wilkins'
print(developer.translate({ord('i'): ''}))  # kq: Jessca Wlkns
print(ord('t'))  # mã unicode
'''
