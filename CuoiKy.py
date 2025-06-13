# ===================================================================
# PHẦN ĐỊNH NGHĨA CÁC LỚP (Sử dụng cho Câu 2)
# ===================================================================

class Nguoi:
    """Lớp cha chứa các thông tin cơ bản về một người."""
    def __init__(self, ho_ten, ngay_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi
        
    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Địa chỉ: {self.dia_chi}"

class GiaoVien(Nguoi):
    """Lớp con GiaoVien kế thừa từ Nguoi, có thêm thông tin chuyên môn."""
    def __init__(self, ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_cong_tac):
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        self.mon_day = mon_day
        self.trinh_do = trinh_do
        self.so_nam_cong_tac = so_nam_cong_tac

    def __str__(self):
        thong_tin_cha = super().__str__()
        thong_tin_con = f", Môn dạy: {self.mon_day}, Trình độ: {self.trinh_do}, Số năm công tác: {self.so_nam_cong_tac}"
        return thong_tin_cha + thong_tin_con
        
    def __lt__(self, other):
        """Nạp chồng toán tử '<' để sắp xếp GiaoVien theo số năm công tác."""
        return self.so_nam_cong_tac < other.so_nam_cong_tac

# ===================================================================
# PHẦN ĐỊNH NGHĨA CÁC HÀM (Sử dụng cho Câu 1)
# ===================================================================

def khoi_tao_mon_hoc():
    """Hàm khởi tạo từ điển chứa thông tin các môn học."""
    while True:
        try:
            n = int(input("Nhập số lượng môn học (n >= 5): "))
            if n >= 5: break
            else: print("Số lượng môn học phải lớn hơn hoặc bằng 5.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    ds_mon = {}
    print("-" * 20)
    for i in range(n):
        print(f"Nhập thông tin cho môn học thứ {i + 1}:")
        ma_mon = input(" - Mã môn học: ")
        ten_mon = input(" - Tên môn học: ")
        so_tin_chi = int(input(" - Số tín chỉ: "))
        hoc_ky = input(" - Học kỳ: ")
        giang_vien = input(" - Giảng viên: ")
        ds_mon[ma_mon] = [ten_mon, so_tin_chi, hoc_ky, giang_vien]
        print("-" * 10)
    return ds_mon

def nhap_so_dang_ky(ma_mon, ds_mon):
    """Hàm nhập số lượng sinh viên đăng ký cho một môn học."""
    if ma_mon in ds_mon:
        so_luong = int(input(f"Nhập số lượng SV đăng ký môn '{ma_mon}': "))
        if len(ds_mon[ma_mon]) == 4: # Chỉ thêm nếu chưa có
            ds_mon[ma_mon].append(so_luong)
            print("Cập nhật thành công!")
        else:
            print("Môn này đã có thông tin đăng ký.")
    else:
        print(f"Lỗi: Không tìm thấy môn học có mã '{ma_mon}'.")

def kiem_tra_dang_ky(ma_mon, ds_mon):
    """Hàm kiểm tra một môn học đã có dữ liệu đăng ký hay chưa."""
    if ma_mon in ds_mon and len(ds_mon[ma_mon]) == 5:
        print(f"Môn học '{ma_mon}' ĐÃ CÓ thông tin đăng ký.")
        return True
    else:
        print(f"Môn học '{ma_mon}' CHƯA CÓ thông tin đăng ký.")
        return False

# ===================================================================
# KHỐI LỆNH CHÍNH (MAIN)
# ===================================================================

if __name__ == "__main__":
    
    # --- Bắt đầu thực thi yêu cầu Câu 1 ---
    print("="*15, "PHẦN 1: QUẢN LÝ MÔN HỌC (CÂU 1)", "="*15)
    
    danh_sach_mon_hoc = khoi_tao_mon_hoc()
    print("\nDANH SÁCH MÔN HỌC BAN ĐẦU:")
    print(danh_sach_mon_hoc)
    
    ma_can_nhap = input("\nNhập mã môn bạn muốn bổ sung số lượng đăng ký: ")
    nhap_so_dang_ky(ma_can_nhap, danh_sach_mon_hoc)
    
    tong_so_luot_dang_ky = sum(mon[4] for mon in danh_sach_mon_hoc.values() if len(mon) == 5)
    print(f"\nTổng số lượt đăng ký của tất cả các môn là: {tong_so_luot_dang_ky}")
    
    # --- Bắt đầu thực thi yêu cầu Câu 2 ---
    print("\n\n" + "="*15, "PHẦN 2: QUẢN LÝ GIÁO VIÊN (CÂU 2)", "="*15)
    
    danh_sach_giao_vien = []
    while True:
        try:
            n_gv = int(input("Nhập số lượng giáo viên (n > 3): "))
            if n_gv > 3: break
            else: print("Số lượng giáo viên phải lớn hơn 3.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    print("-" * 20)
    for i in range(n_gv):
        print(f"Nhập thông tin cho giáo viên thứ {i + 1}:")
        gv = GiaoVien(ho_ten=input(" - Họ tên: "),
                      ngay_sinh=input(" - Ngày sinh: "),
                      dia_chi=input(" - Địa chỉ: "),
                      mon_day=input(" - Môn dạy: "),
                      trinh_do=input(" - Trình độ: "),
                      so_nam_cong_tac=int(input(" - Số năm công tác: ")))
        danh_sach_giao_vien.append(gv)
        print("-" * 10)
        
    danh_sach_giao_vien.sort()
    
    print("\n--- DANH SÁCH GIÁO VIÊN SAU KHI SẮP XẾP ---")
    for gv in danh_sach_giao_vien:
        print(gv)
        
    try:
        with open("GIAOVIEN.TXT", "w", encoding="utf-8") as f:
            f.write("DANH SÁCH GIÁO VIÊN SẮP XẾP THEO SỐ NĂM CÔNG TÁC\n")
            f.write("-" * 30 + "\n")
            for gv in danh_sach_giao_vien:
                f.write(str(gv) + "\n")
        print("\nĐã ghi thành công kết quả vào file GIAOVIEN.TXT")
    except IOError:
        print("\nLỗi: Không thể ghi file.")