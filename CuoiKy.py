# --- Hàm 1: Khởi tạo từ điển môn học ---
def khoi_tao_mon_hoc():
    while True:
        try:
            # Xử lý nhập liệu, đảm bảo n là số nguyên và >= 5
            n = int(input("Nhập số lượng môn học (n >= 5): "))
            if n >= 5:
                break
            else:
                print("Số lượng môn học phải lớn hơn hoặc bằng 5. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    ds_mon = {} # Khởi tạo một từ điển rỗng
    print("-" * 20)
    for i in range(n):
        print(f"Nhập thông tin cho môn học thứ {i + 1}:")
        ma_mon = input(" - Mã môn học: ")
        ten_mon = input(" - Tên môn học: ")
        so_tin_chi = int(input(" - Số tín chỉ: "))
        hoc_ky = input(" - Học kỳ: ")
        giang_vien = input(" - Giảng viên: ")
        
        # Thêm một cặp key-value mới vào từ điển
        ds_mon[ma_mon] = [ten_mon, so_tin_chi, hoc_ky, giang_vien]
        print("-" * 10)
        
    return ds_mon

# --- Hàm 2: Nhập số lượng đăng ký ---
def nhap_so_dang_ky(ma_mon, ds_mon):
    if ma_mon in ds_mon:
        so_luong = int(input(f"Nhập số lượng sinh viên đăng ký môn '{ma_mon}': "))
        # Thêm số lượng vào cuối danh sách của môn học tương ứng
        ds_mon[ma_mon].append(so_luong)
        print("Cập nhật thành công!")
    else:
        print(f"Lỗi: Không tìm thấy môn học có mã '{ma_mon}'.")

# --- Hàm 3: Kiểm tra môn học đã có số lượng đăng ký chưa ---
def kiem_tra_dang_ky(ma_mon, ds_mon):
    if ma_mon in ds_mon:
        # Nếu danh sách có 5 phần tử, nghĩa là đã nhập số lượng
        if len(ds_mon[ma_mon]) == 5:
            print(f"Môn học '{ma_mon}' ĐÃ CÓ thông tin đăng ký.")
            return True
        else:
            print(f"Môn học '{ma_mon}' CHƯA CÓ thông tin đăng ký.")
            return False
    else:
        print(f"Lỗi: Không tìm thấy môn học có mã '{ma_mon}'.")
        return False

# --- Khối lệnh chính để thực thi ---
if __name__ == "__main__":
    # 1. Xây dựng danh sách môn học
    danh_sach_mon_hoc = khoi_tao_mon_hoc()
    print("\nDANH SÁCH MÔN HỌC ĐÃ TẠO:")
    print(danh_sach_mon_hoc)
    
    # 2. Bổ sung thông tin đăng ký (ví dụ cho một môn)
    ma_can_nhap = input("\nNhập mã môn bạn muốn bổ sung số lượng đăng ký: ")
    nhap_so_dang_ky(ma_can_nhap, danh_sach_mon_hoc)
    
    # 3. Kiểm tra lại môn vừa nhập
    kiem_tra_dang_ky(ma_can_nhap, danh_sach_mon_hoc)

    # 4. Tính và in tổng số lượt đăng ký
    tong_so_luot_dang_ky = 0
    # Duyệt qua các giá trị (là các list) trong từ điển
    for mon_hoc_info in danh_sach_mon_hoc.values():
        # Nếu môn học đã có thông tin đăng ký (danh sách có 5 phần tử)
        if len(mon_hoc_info) == 5:
            # Cộng dồn số lượng đăng ký (phần tử thứ 5, chỉ số 4)
            tong_so_luot_dang_ky += mon_hoc_info[4]
            
    print(f"\nTổng số lượt đăng ký của tất cả các môn là: {tong_so_luot_dang_ky}")
    # Câu 2 -------------------------------------

# --- Lớp cha: Nguoi ---
class Nguoi:
    # Hàm khởi tạo của lớp Nguoi
    def __init__(self, ho_ten, ngay_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.dia_chi = dia_chi
        
    # Phương thức để hiển thị thông tin, giúp in ra đẹp hơn
    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Ngày sinh: {self.ngay_sinh}, Địa chỉ: {self.dia_chi}"

# --- Lớp con: GiaoVien, kế thừa từ Nguoi ---
class GiaoVien(Nguoi):
    # Hàm khởi tạo của lớp GiaoVien
    def __init__(self, ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_cong_tac):
        # Gọi hàm khởi tạo của lớp cha (Nguoi) để không phải viết lại code
        super().__init__(ho_ten, ngay_sinh, dia_chi)
        # Thêm các thuộc tính riêng của GiaoVien
        self.mon_day = mon_day
        self.trinh_do = trinh_do
        self.so_nam_cong_tac = so_nam_cong_tac

    # Nạp chồng phương thức __str__ để thêm thông tin của GiaoVien
    def __str__(self):
        # Lấy chuỗi thông tin cơ bản từ lớp cha
        thong_tin_cha = super().__str__()
        # Nối thêm thông tin riêng
        thong_tin_con = f", Môn dạy: {self.mon_day}, Trình độ: {self.trinh_do}, Số năm công tác: {self.so_nam_cong_tac}"
        return thong_tin_cha + thong_tin_con
        
    # --- Nạp chồng toán tử so sánh '<' (less than) ---
    # Python sẽ dùng phương thức này khi so sánh hai đối tượng GiaoVien
    def __lt__(self, other):
        # So sánh dựa trên số năm công tác
        return self.so_nam_cong_tac < other.so_nam_cong_tac

# --- Khối lệnh chính để thực thi ---
if __name__ == "__main__":
    danh_sach_giao_vien = []
    
    while True:
        try:
            n = int(input("Nhập số lượng giáo viên (n > 3): "))
            if n > 3:
                break
            else:
                print("Số lượng giáo viên phải lớn hơn 3. Vui lòng nhập lại.")
        except ValueError:
            print("Vui lòng nhập một số nguyên.")

    print("-" * 20)
    for i in range(n):
        print(f"Nhập thông tin cho giáo viên thứ {i + 1}:")
        ho_ten = input(" - Họ tên: ")
        ngay_sinh = input(" - Ngày sinh: ")
        dia_chi = input(" - Địa chỉ: ")
        mon_day = input(" - Môn dạy: ")
        trinh_do = input(" - Trình độ: ")
        so_nam_cong_tac = int(input(" - Số năm công tác: "))
        
        # Tạo một đối tượng (instance) của lớp GiaoVien
        giao_vien = GiaoVien(ho_ten, ngay_sinh, dia_chi, mon_day, trinh_do, so_nam_cong_tac)
        
        # Thêm đối tượng vừa tạo vào danh sách
        danh_sach_giao_vien.append(giao_vien)
        print("-" * 10)
        
    # Sắp xếp danh sách giáo viên.
    # Python sẽ tự động dùng phương thức __lt__ ta đã định nghĩa để biết cách sắp xếp
    danh_sach_giao_vien.sort()
    
    print("\n--- DANH SÁCH GIÁO VIÊN SAU KHI SẮP XẾP TĂNG DẦN THEO SỐ NĂM CÔNG TÁC ---")
    # In ra màn hình
    for gv in danh_sach_giao_vien:
        print(gv) # Tự động gọi phương thức __str__
        
    # Ghi kết quả vào file GIAOVIEN.TXT
    try:
        with open("GIAOVIEN.TXT", "w", encoding="utf-8") as f:
            f.write("DANH SÁCH GIÁO VIÊN SAU KHI SẮP XẾP\n")
            f.write("-" * 30 + "\n")
            for gv in danh_sach_giao_vien:
                # Ghi chuỗi trả về từ __str__ vào file, cộng thêm dấu xuống dòng
                f.write(str(gv) + "\n")
        print("\nĐã ghi thành công kết quả vào file GIAOVIEN.TXT")
    except IOError:
        print("\nLỗi: Không thể ghi file.")