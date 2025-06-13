def nhap_thong_tin_sinh_vien(n):
    """Nhập thông tin của n sinh viên và trả về dictionary."""
    danh_sach_sinh_vien = {}
    for _ in range(n):
        ma_sinh_vien = input("Nhập mã sinh viên: ")
        try:
            so_luong_tin_chi = int(input("Nhập số lượng tín chỉ đã học: "))
            danh_sach_sinh_vien[ma_sinh_vien] = so_luong_tin_chi
        except ValueError:
            print("Số lượng tín chỉ phải là số nguyên.")
    return danh_sach_sinh_vien

def khoi_tao_thong_tin_hoc_phan():
    """Khởi tạo dictionary thông tin học phần và in ra màn hình."""
    thong_tin_hoc_phan = {
        "CS101": "Nhập môn Lập trình",
        "MA201": "Giải tích 1",
        "PH102": "Vật lý đại cương",
        "LA101": "Triết học Mác - Lênin",
        "EN201": "Tiếng Anh cơ bản"
    }
    print("\n--- Thông tin học phần ---")
    for ma_hp, ten_lop in thong_tin_hoc_phan.items():
        print(f"Mã học phần: {ma_hp}, Tên lớp: {ten_lop}")
    return thong_tin_hoc_phan

def cap_nhat_thong_tin_sinh_vien(danh_sach_sinh_vien):
    """Kiểm tra và cập nhật thông tin sinh viên '2024123456'."""
    ma_sv_can_tim = "2024123456"
    if ma_sv_can_tim in danh_sach_sinh_vien:
        danh_sach_sinh_vien[ma_sv_can_tim] = 100
        print(f"\nĐã cập nhật số tín chỉ của sinh viên {ma_sv_can_tim} thành 100.")
    else:
        try:
            so_luong_tin_chi_moi = int(input(f"Không tìm thấy sinh viên {ma_sv_can_tim}. Nhập số lượng tín chỉ cho sinh viên này: "))
            danh_sach_sinh_vien[ma_sv_can_tim] = so_luong_tin_chi_moi
            print(f"\nĐã thêm sinh viên {ma_sv_can_tim} với số tín chỉ là {so_luong_tin_chi_moi}.")
        except ValueError:
            print("Số lượng tín chỉ phải là số nguyên.")

def xoa_sinh_vien_no_tin_chi(danh_sach_sinh_vien):
    """Xóa các sinh viên có số tín chỉ bằng 0."""
    sinh_vien_can_xoa = [sv for sv, so_tc in danh_sach_sinh_vien.items() if so_tc == 0]
    for sv in sinh_vien_can_xoa:
        del danh_sach_sinh_vien[sv]
    if sinh_vien_can_xoa:
        print("\nĐã xóa các sinh viên có số tín chỉ bằng 0.")
    else:
        print("\nKhông có sinh viên nào có số tín chỉ bằng 0.")

def chuyen_du_lieu_sang_list(danh_sach_sinh_vien):
    """Chuyển dữ liệu từ dictionary sang hai list."""
    list_ma_sinh_vien = list(danh_sach_sinh_vien.keys())
    list_so_luong_tin_chi = list(danh_sach_sinh_vien.values())
    return list_ma_sinh_vien, list_so_luong_tin_chi

def in_ba_phan_tu_dau_va_cuoi(list1, list2):
    """In 3 phần tử đầu của list 1 và 3 phần tử cuối của list 2."""
    print("\n--- Danh sách mã sinh viên (3 phần tử đầu) ---")
    print(list1[:3])
    print("\n--- Danh sách số lượng tín chỉ (3 phần tử cuối) ---")
    print(list2[-3:])

def main():
    """Hàm chính để chạy chương trình."""
    try:
        n = int(input("Nhập số lượng sinh viên: "))
        danh_sach_sv = nhap_thong_tin_sinh_vien(n)

        thong_tin_hp = khoi_tao_thong_tin_hoc_phan()

        cap_nhat_thong_tin_sinh_vien(danh_sach_sv)

        xoa_sinh_vien_no_tin_chi(danh_sach_sv)

        list_msv, list_sltc = chuyen_du_lieu_sang_list(danh_sach_sv)

        in_ba_phan_tu_dau_va_cuoi(list_msv, list_sltc)

    except ValueError:
        print("Số lượng sinh viên phải là số nguyên.")

if __name__ == "__main__":
    main()  