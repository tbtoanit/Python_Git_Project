#viết function truyền vào 1 argument là chuỗi, return => True/False
#True => nếu là số nguyên
#False => nếu không phải là số nguyên

def kiem_tra_chu_so(s):
    if s.isdigit() == True:
        return True
    else:
        return False

k = kiem_tra_chu_so("a1")
print(k)

def kt_snt(a):
    nguyen_to = True
    for i in range(2,a):
        if a % i ==0: #i: 2,3,4...9
            nguyen_to=False
            break #khi đã có 1 số chia hết, không còn số nguyên tố=> hệ thống ngừng=> thoát khỏi vòng lặp=>tiết kiệm Ram cho máy tính
    return nguyen_to
