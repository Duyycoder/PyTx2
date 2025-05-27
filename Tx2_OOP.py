# --- Dữ liệu ban đầu ---
du_lieu_bang_dau_goc = {
    'Mã': ['ENG', 'IRN', 'USA', 'WAL'],
    'Quốc gia': ['Anh', 'Iran', 'Mỹ', 'Wales'],
    'Liên đoàn': ['UEFA', 'AFC', 'CONCACAF', 'UEFA'],
    'Số lần tham dự': [16, 6, 11, 2],
    'Thành tích tốt nhất': ['Vô địch', 'Vòng bảng', 'Hạng ba', 'Tứ kết']
}

# --- Định nghĩa Lớp (OOP) ---
class DoiBong:
    def __init__(self, ma, quoc_gia, lien_doan, so_lan, thanh_tich):
        self.ma = ma
        self.quoc_gia = quoc_gia
        self.lien_doan = lien_doan
        self.so_lan = so_lan
        self.thanh_tich = thanh_tich

    def __str__(self):
        # Điều chỉnh khoảng cách tab cho đẹp hơn
        return f"{self.ma:<5}\t{self.quoc_gia:<10}\t{self.lien_doan:<10}\t{self.so_lan:<16}\t{self.thanh_tich}"

    def la_vo_dich_wc(self):
        return self.thanh_tich == 'Vô địch'

    def cap_nhat_thong_tin(self, thuoc_tinh, gia_tri_moi):
        if hasattr(self, thuoc_tinh):
            if thuoc_tinh == 'so_lan':
                try:
                    setattr(self, thuoc_tinh, int(gia_tri_moi))
                except ValueError:
                    print("Lỗi: Số lần tham dự phải là một số nguyên.")
                    return False
            else:
                setattr(self, thuoc_tinh, gia_tri_moi)
            return True
        print(f"Lỗi: Thuộc tính '{thuoc_tinh}' không tồn tại để cập nhật.")
        return False

class BangDau:
    def __init__(self, ten_giai, bang, ngay_khai_mac, chu_nha, cac_doi_data):
        self.ten_giai = ten_giai
        self.bang = bang
        self.ngay_khai_mac = ngay_khai_mac
        self.chu_nha = chu_nha
        self.cac_doi = []
        # Tạo danh sách các đối tượng DoiBong từ dữ liệu đầu vào
        for i in range(len(cac_doi_data['Mã'])):
            doi = DoiBong(
                cac_doi_data['Mã'][i],
                cac_doi_data['Quốc gia'][i],
                cac_doi_data['Liên đoàn'][i],
                cac_doi_data['Số lần tham dự'][i],
                cac_doi_data['Thành tích tốt nhất'][i]
            )
            self.cac_doi.append(doi)

    def hien_thi_thong_tin(self, tieu_de=""):
        if tieu_de:
            print(f"\n--- {tieu_de} ---")
        print(f"Giải đấu: {self.ten_giai}")
        print(f"BẢNG {self.bang}")
        print(f"Ngày khai mạc: {self.ngay_khai_mac}")
        print(f"Chủ nhà: {self.chu_nha}")
        print("--------------------------------------------------------------------------")
        print(f"{'Mã':<5}\t{'Quốc gia':<10}\t{'Liên đoàn':<10}\t{'Số lần tham dự':<16}\tThành tích tốt nhất")
        print("--------------------------------------------------------------------------")
        for doi in self.cac_doi:
            print(doi)
        print("--------------------------------------------------------------------------\n")

    def sua_chu_nha_tuong_tac(self):
        ten_moi = input(f"Nhập tên nước chủ nhà mới (hiện tại: {self.chu_nha}): ").strip()
        if ten_moi: # Chỉ cập nhật nếu người dùng nhập gì đó
            self.chu_nha = ten_moi
            print(f"Đã cập nhật nước chủ nhà thành: {self.chu_nha}")
        else:
            print("Không có thay đổi nào được thực hiện cho nước chủ nhà.")
        self.hien_thi_thong_tin("Bảng sau khi thử sửa chủ nhà")

    def sua_chu_nha_truc_tiep(self, ten_moi):
        self.chu_nha = ten_moi
        print(f"Đã cập nhật nước chủ nhà (trực tiếp) thành: {self.chu_nha}")


    def tim_doi_theo_ma(self, ma_doi):
        for doi in self.cac_doi:
            if doi.ma.lower() == ma_doi.lower():
                return doi
        return None
    def tim_doi_vo_dich(self):
        print("\n--- Các đội từng vô địch World Cup trong bảng ---")
        tim_thay = False
        cac_doi_vo_dich = []
        for doi in self.cac_doi:
            if doi.la_vo_dich_wc():
                cac_doi_vo_dich.append(str(doi)) # Thêm dạng string để in
                tim_thay = True
        
        if tim_thay:
            print(f"{'Mã':<5}\t{'Quốc gia':<10}\t{'Liên đoàn':<10}\t{'Số lần tham dự':<16}\tThành tích tốt nhất")
            print("--------------------------------------------------------------------------")
            for thong_tin_doi in cac_doi_vo_dich:
                print(thong_tin_doi)
            print("--------------------------------------------------------------------------")
        else:
            print("Không có đội nào trong bảng từng vô địch World Cup.")
        print("\n")

    def sap_xep_theo_so_lan(self):
        self.cac_doi.sort(key=lambda x: x.so_lan, reverse=True)
        self.hien_thi_thong_tin("Bảng sau khi sắp xếp theo số lần tham dự (giảm dần)")

    def luu_file_txt(self, ten_file="BANGA_WORLD_CUP.TXT"):
        try:
            with open(ten_file, 'w', encoding='utf-8') as f:
                f.write(f"Giải đấu: {self.ten_giai}\n")
                f.write(f"BẢNG {self.bang}\n")
                f.write(f"Ngày khai mạc: {self.ngay_khai_mac}\n")
                f.write(f"Chủ nhà: {self.chu_nha}\n")
                f.write("--------------------------------------------------------------------------\n")
                f.write(f"{'Mã':<5}\t{'Quốc gia':<10}\t{'Liên đoàn':<10}\t{'Số lần tham dự':<16}\tThành tích tốt nhất\n")
                f.write("--------------------------------------------------------------------------\n")
                for doi in self.cac_doi:
                    # Sử dụng định dạng của __str__ cho nhất quán
                    f.write(f"{doi.ma:<5}\t{doi.quoc_gia:<10}\t{doi.lien_doan:<10}\t{doi.so_lan:<16}\t{doi.thanh_tich}\n")
                f.write("--------------------------------------------------------------------------\n")
            print(f"Đã ghi dữ liệu bảng đấu vào file '{ten_file}'\n")
        except IOError:
            print(f"Lỗi: Không thể ghi vào file '{ten_file}'. Vui lòng kiểm tra quyền ghi.")


# --- Chương trình chính ---
def quan_ly_bang_dau_tuong_tac():
    # Tạo bản sao dữ liệu gốc để mỗi lần chạy đều bắt đầu từ dữ liệu gốc
    du_lieu_hien_tai = {key: list(value) for key, value in du_lieu_bang_dau_goc.items()}
    
    # (3d) Xác định các lớp, các thuộc tính, phương thức cần thiết và cài đặt chương trình
    bang_b = BangDau(
        ten_giai="FIFA World Cup 2022",
        bang="B",
        ngay_khai_mac="20/11/2022",
        chu_nha="Pháp", # Chủ nhà ban đầu theo đề bài
        cac_doi_data=du_lieu_hien_tai
    )

    # (1d) Sửa lại thông tin nước chủ nhà của giải đấu thành “Qatar” (thực hiện một lần theo yêu cầu)
    print("--- THỰC HIỆN YÊU CẦU BAN ĐẦU CỦA ĐỀ BÀI ---")
    bang_b.hien_thi_thong_tin("Bảng đấu ban đầu")
    bang_b.sua_chu_nha_truc_tiep("Qatar") # Sửa trực tiếp thành Qatar
    bang_b.hien_thi_thong_tin("Bảng sau khi sửa chủ nhà thành Qatar")
    print("----------------------------------------------\n")

    while True:
        print("\n--- MENU QUẢN LÝ BẢNG ĐẤU WORLD CUP (OOP) ---")
        print("Trạng thái hiện tại của Bảng:")
        bang_b.hien_thi_thong_tin() # Hiển thị bảng hiện tại ở đầu menu
        print("Các lựa chọn:")
        print("1. Sửa thông tin nước chủ nhà (tương tác)")
        print("2. Tìm các đội từng vô địch World Cup trong bảng")
        print("3. Sắp xếp danh sách đội theo số lần tham dự (giảm dần)")
        print("4. Ghi dữ liệu bảng đấu hiện tại vào file BANGA_WORLD_CUP.TXT")
        print("0. Thoát chương trình")

        lua_chon = input("Nhập lựa chọn của bạn: ").strip()

        if lua_chon == '1':
            bang_b.sua_chu_nha_tuong_tac()
        elif lua_chon == '2':
            bang_b.tim_doi_vo_dich()
        elif lua_chon == '3':
            bang_b.sap_xep_theo_so_lan()
        elif lua_chon == '4':
            bang_b.luu_file_txt()
        elif lua_chon == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    quan_ly_bang_dau_tuong_tac()