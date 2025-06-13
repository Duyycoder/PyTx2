def nhap_danh_sach_hang_hoa():
    """Nhập danh sách hàng hóa từ người dùng."""
    danh_sach = []
    while True:
        ma_hang = input("Nhập mã hàng (hoặc 'q' để kết thúc): ")
        if ma_hang.lower() == 'q':
            break
        ten_mat_hang = input("Nhập tên mặt hàng: ")
        try:
            so_luong = int(input("Nhập số lượng: "))
            gia_tien = float(input("Nhập giá tiền: "))
            danh_sach.append({
                "ma_hang": ma_hang,
                "ten_mat_hang": ten_mat_hang,
                "so_luong": so_luong,
                "gia_tien": gia_tien
            })
        except ValueError:
            print("Số lượng và giá tiền phải là số.")
    return danh_sach

def hien_thi_danh_sach(danh_sach):
    """Hiển thị danh sách hàng hóa đã nhập."""
    print("\n--- Danh sách hàng hóa ---")
    print("Mã hàng | Tên mặt hàng | Số lượng | Giá tiền | Tổng tiền")
    for hang_hoa in danh_sach:
        tong_tien = hang_hoa["so_luong"] * hang_hoa["gia_tien"]
        print(f"{hang_hoa['ma_hang']:<8} | {hang_hoa['ten_mat_hang']:<15} | {hang_hoa['so_luong']:<8} | {hang_hoa['gia_tien']:<9} | {tong_tien:<10,.0f}")

def tim_mat_hang_gia_tri_lon_nhat(danh_sach):
    """Tìm mặt hàng có tổng giá trị lớn nhất."""
    if not danh_sach:
        return None
    mat_hang_max = danh_sach[0]
    tong_tien_max = mat_hang_max["so_luong"] * mat_hang_max["gia_tien"]
    for hang_hoa in danh_sach[1:]:
        tong_tien = hang_hoa["so_luong"] * hang_hoa["gia_tien"]
        if tong_tien > tong_tien_max:
            tong_tien_max = tong_tien
            mat_hang_max = hang_hoa
    return mat_hang_max

def dem_so_luong_mat_hang_du_dieu_kien(danh_sach):
    """Đếm số lượng mặt hàng có số lượng > 5 và tổng tiền < 1,000,000 VND."""
    count = 0
    for hang_hoa in danh_sach:
        tong_tien = hang_hoa["so_luong"] * hang_hoa["gia_tien"]
        if hang_hoa["so_luong"] > 5 and tong_tien < 1000000:
            count += 1
    return count

def main():
    """Hàm chính để chạy chương trình."""
    danh_sach_hang = nhap_danh_sach_hang_hoa()
    if danh_sach_hang:
        hien_thi_danh_sach(danh_sach_hang)

        mat_hang_gia_tri_nhat = tim_mat_hang_gia_tri_lon_nhat(danh_sach_hang)
        if mat_hang_gia_tri_nhat:
            tong_tien_max = mat_hang_gia_tri_nhat["so_luong"] * mat_hang_gia_tri_nhat["gia_tien"]
            print("\n--- Mặt hàng có tổng giá trị lớn nhất ---")
            print(f"Mã hàng: {mat_hang_gia_tri_nhat['ma_hang']}")
            print(f"Tên mặt hàng: {mat_hang_gia_tri_nhat['ten_mat_hang']}")
            print(f"Tổng giá trị: {tong_tien_max:,.0f} VND")

        so_luong_du_dk = dem_so_luong_mat_hang_du_dieu_kien(danh_sach_hang)
        print(f"\nSố lượng mặt hàng có số lượng > 5 và tổng tiền < 1,000,000 VND: {so_luong_du_dk}")
    else:
        print("Không có mặt hàng nào được nhập.")

if __name__ == "__main__":
    main()