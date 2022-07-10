# i = 0
# while True: #True/False
#     print(i)
#     i = i+1
#     if i >= 10:
#         break

#Viết chương trình cho nhập vào 1 số nguyên, nếu giá trị được nhập vào không phải
# là số nguyên thì sẽ bắt người dùng nhập lại cho đến khi nhập đúng số nguyên.
def kiem_tra_so_nguyen():
    count = 0
    while True:
        s = input('Vui long nhap so: ') # s = "6.5"
        if s.isdigit(): #sẽ là True nếu chuỗi không chứa gì khác ngoài số
            print("Số nguyên")
            break
        else:
            print("Nhập lại đi!")
            count += 1
            if count == 3:
                print("Bị khóa")
                break
            else:
                print("Không bị khoá !")

kiem_tra_so_nguyen()
print("Chức năng của toan tran")
print("Thêm chức năng thứ 2 của toàn trần")

# thêm dòng code mới
print("Thêm dòng code mới !")

print('code cua Thai')
