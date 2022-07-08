from fb_func import xac_thuc_email, luu_thong_tin_nguoi_dung


def tinh_toan(a, b, c='+'):  # a,b argument, parameter
    if c == '+':
        ket_qua = a + b
    elif c == '-':
        ket_qua = a - b
    elif c == '*':
        ket_qua = a * b
    elif c == '/':
        ket_qua = a / b

    return ket_qua


if __name__ == "__main__":  # đoạn code này chỉ được thực thi khi developer run trực tiếp từ file này
    # tạo tài khoản facebook
    # 1: Gửi email xác thực vào email đã đăng ký trên tk facebook
    # 2: lưu thông tin các bạn vào cở sở dữ
    print("Cod chay trong file function demo")
    xac_thuc_email()
    luu_thong_tin_nguoi_dung()

kq = tinh_toan(c='/', a=10, b=5)  # tham số keyword
print(kq)

print('toi', 'ten', 'ton', sep='-')  # separate #tham số keyword


def tinh(*numbers, formular):
    sum = numbers[0]
    for i in range(1, len(numbers)):
        if formular == '-':
            sum -= numbers[i]
        elif formular == '+':
            sum += numbers[i]
    return sum


kq = tinh(1, 2, 3, formular='-')  # sử dụng tham số tùy biến và tham số keyword
print(kq)

cong_hai_so = lambda a, b: print(a + b)  # sử dụng lambda


def cong_2_so(a, b):  # sử dụng function truyền thống
    print(a + b)


cong_hai_so(1, 2)
