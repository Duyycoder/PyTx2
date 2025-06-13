# Định nghĩa Lớp (Class) NhanVien
class NhanVien:
    # Đây là hàm khởi tạo (constructor), được gọi khi một đối tượng mới được tạo ra
    # `self` đại diện cho chính đối tượng sẽ được tạo ra
    def __init__(self, ten, chuc_vu, luong):
        # Đây là các thuộc tính (attributes) của đối tượng
        self.ten = ten
        self.chuc_vu = chuc_vu
        self.luong = luong
        self.email = ten.lower().replace(" ", "") + "@congty.com"

    # Đây là một phương thức (method) của đối tượng
    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ten}")
        print(f"Chức vụ: {self.chuc_vu}")
        print(f"Lương: {self.luong}")
        print(f"Email: {self.email}")

# Tạo ra các Đối tượng (Object) từ lớp NhanVien
nv1 = NhanVien("Nguyễn Văn A", "Lập trình viên", 15000000)
nv2 = NhanVien("Trần Thị B", "Quản lý dự án", 25000000)

# Gọi phương thức từ đối tượng
print("--- Thông tin nhân viên 1 ---")
nv1.hien_thi_thong_tin()

print("\n--- Thông tin nhân viên 2 ---")
nv2.hien_thi_thong_tin()
#-----------------------------------------------------------------------------------------------

class TaiKhoanNganHang:
    def __init__(self, chu_tai_khoan, so_du):
        self.chu_tai_khoan = chu_tai_khoan
        self.__so_du = so_du # Dùng '__' để che giấu thuộc tính này

    def xem_so_du(self):
        # Cung cấp một phương thức công khai để xem số dư
        print(f"Số dư tài khoản của {self.chu_tai_khoan} là: {self.__so_du}")

    def nap_tien(self, so_tien):
        if so_tien > 0:
            self.__so_du += so_tien
            print(f"Nạp thành công {so_tien}. Số dư mới: {self.__so_du}")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

tk = TaiKhoanNganHang("Lê C", 50000)

# Cố gắng truy cập trực tiếp (sẽ gây lỗi)
# print(tk.__so_du) # AttributeError: 'TaiKhoanNganHang' object has no attribute '__so_du'

# Truy cập thông qua phương thức công khai
tk.xem_so_du() # Hoạt động bình thường

tk.nap_tien(20000)
tk.xem_so_du()

#-------------------------------------------------------------------------------------------------

# Lớp cha (đã định nghĩa ở trên)
class NhanVien:
    def __init__(self, ten, chuc_vu, luong):
        self.ten = ten
        self.chuc_vu = chuc_vu
        self.luong = luong

    def hien_thi_thong_tin(self):
        print(f"Tên: {self.ten}, Chức vụ: {self.chuc_vu}, Lương: {self.luong}")

# Lớp con QuanLy kế thừa từ NhanVien
class QuanLy(NhanVien):
    def __init__(self, ten, chuc_vu, luong, nhan_vien_cap_duoi=None):
        # Gọi hàm khởi tạo của lớp cha (NhanVien) để khởi tạo các thuộc tính chung
        super().__init__(ten, chuc_vu, luong)
        # Thêm thuộc tính mới cho lớp QuanLy
        if nhan_vien_cap_duoi is None:
            self.nhan_vien_cap_duoi = []
        else:
            self.nhan_vien_cap_duoi = nhan_vien_cap_duoi

    def them_nhan_vien(self, nhan_vien):
        if nhan_vien not in self.nhan_vien_cap_duoi:
            self.nhan_vien_cap_duoi.append(nhan_vien)

    # Ghi đè (override) phương thức của lớp cha
    def hien_thi_thong_tin(self):
        super().hien_thi_thong_tin() # Gọi lại phương thức của lớp cha
        print(f"Số lượng nhân viên quản lý: {len(self.nhan_vien_cap_duoi)}")


# Tạo đối tượng
nv_a = NhanVien("Nguyễn Văn A", "Lập trình viên", 15000000)
ql_b = QuanLy("Trần Thị B", "Quản lý dự án", 25000000)

ql_b.them_nhan_vien(nv_a)

print("--- Thông tin nhân viên ---")
nv_a.hien_thi_thong_tin()

print("\n--- Thông tin quản lý ---")
ql_b.hien_thi_thong_tin()
#------------------------------------------------------------------------------------------------

class ThongBaoEmail:
    def gui(self, nguoi_nhan, noi_dung):
        print(f"Đang gửi EMAIL tới {nguoi_nhan}: '{noi_dung}'")

class ThongBaoSMS:
    def gui(self, nguoi_nhan, noi_dung):
        print(f"Đang gửi SMS tới {nguoi_nhan}: '{noi_dung}'")

# Tạo các đối tượng
tb_email = ThongBaoEmail()
tb_sms = ThongBaoSMS()

# Cả hai đối tượng đều có thể gọi phương thức `gui`
# nhưng hành động thực tế là khác nhau.
# Đây chính là tính đa hình.
def gui_thong_bao_chung(phuong_thuc_thong_bao, nguoi_nhan, noi_dung):
    phuong_thuc_thong_bao.gui(nguoi_nhan, noi_dung)


gui_thong_bao_chung(tb_email, "a@example.com", "Chào mừng bạn!")
gui_thong_bao_chung(tb_sms, "0987654321", "Mã xác thực của bạn là 123456.")