import pandas as pd

# Dữ liệu ban đầu
data = {
    'TÊN': ['Python', 'Java', 'C++', 'Ruby', 'JavaScript'],
    'NĂM': [1991, 1995, 1985, 1995, 1995],
    'NGƯỜI SÁNG TẠO': ['Guido van Rossum', 'James Gosling', 'Bjarne Stroustrup', 'Yukihiro Matsumoto', 'Brendan Eich'],
    'KIỂU LẬP TRÌNH': ['Hướng đối tượng', 'Hướng đối tượng', 'Thủ tục', 'Hướng đối tượng', 'Hướng sự kiện']
}
df = pd.DataFrame(data)

def hien_thi_dataframe(dataframe_hien_thi):
    """Hàm hiển thị DataFrame."""
    if dataframe_hien_thi.empty:
        print("DataFrame hiện đang rỗng.")
    else:
        print(dataframe_hien_thi.to_string()) # .to_string() để hiển thị đầy đủ

def them_ngon_ngu(dataframe):
    """Thêm một ngôn ngữ lập trình mới do người dùng nhập."""
    print("\n--- Thêm ngôn ngữ lập trình mới ---")
    ten = input("Nhập tên ngôn ngữ: ")
    while True:
        try:
            nam = int(input("Nhập năm ra đời: "))
            break
        except ValueError:
            print("Năm phải là một số nguyên. Vui lòng nhập lại.")
    nguoi_sang_tao = input("Nhập người sáng tạo: ")
    kieu_lap_trinh = input("Nhập kiểu lập trình: ")

    new_language = pd.DataFrame({
        'TÊN': [ten],
        'NĂM': [nam],
        'NGƯỜI SÁNG TẠO': [nguoi_sang_tao],
        'KIỂU LẬP TRÌNH': [kieu_lap_trinh]
    })
    dataframe = pd.concat([dataframe, new_language], ignore_index=True)
    print("Đã thêm ngôn ngữ mới.")
    return dataframe

def sua_kieu_lap_trinh(dataframe):
    """Sửa đổi kiểu lập trình của một ngôn ngữ."""
    print("\n--- Sửa đổi kiểu lập trình ---")
    ten_can_sua = input("Nhập tên ngôn ngữ cần sửa kiểu lập trình: ")

    if ten_can_sua not in dataframe['TÊN'].values:
        print(f"Không tìm thấy ngôn ngữ có tên '{ten_can_sua}'.")
        return dataframe

    kieu_moi = input(f"Nhập kiểu lập trình mới cho {ten_can_sua} (ví dụ: Chức năng, Hướng sự kiện): ")
    dataframe.loc[dataframe['TÊN'] == ten_can_sua, 'KIỂU LẬP TRÌNH'] = kieu_moi
    print(f"Đã cập nhật kiểu lập trình cho {ten_can_sua}.")
    return dataframe

def xoa_ngon_ngu(dataframe):
    """Xoá một ngôn ngữ lập trình."""
    print("\n--- Xoá ngôn ngữ lập trình ---")
    ten_can_xoa = input("Nhập tên ngôn ngữ cần xoá: ")

    if ten_can_xoa not in dataframe['TÊN'].values:
        print(f"Không tìm thấy ngôn ngữ có tên '{ten_can_xoa}'.")
        return dataframe

    dataframe = dataframe[dataframe['TÊN'] != ten_can_xoa].reset_index(drop=True)
    print(f"Đã xoá ngôn ngữ '{ten_can_xoa}'.")
    return dataframe

def loc_ngon_ngu_theo_nam(dataframe):
    """Lọc và in ra các ngôn ngữ lập trình ra đời sau một năm nhất định."""
    print("\n--- Lọc ngôn ngữ theo năm ra đời ---")
    while True:
        try:
            nam_moc = int(input("Nhập năm để lọc (hiển thị các ngôn ngữ ra đời SAU năm này): "))
            break
        except ValueError:
            print("Năm phải là một số nguyên. Vui lòng nhập lại.")

    df_filtered = dataframe[dataframe['NĂM'] > nam_moc]
    if df_filtered.empty:
        print(f"Không có ngôn ngữ nào được tạo sau năm {nam_moc}.")
    else:
        print(f"Các ngôn ngữ lập trình ra đời sau năm {nam_moc}:")
        hien_thi_dataframe(df_filtered)

def dem_ngon_ngu(dataframe):
    """Đếm số lượng ngôn ngữ lập trình theo năm và kiểu lập trình."""
    print("\n--- Đếm ngôn ngữ theo năm và kiểu lập trình ---")
    while True:
        try:
            nam_dem = int(input("Nhập năm ra đời cần đếm: "))
            break
        except ValueError:
            print("Năm phải là một số nguyên. Vui lòng nhập lại.")

    kieu_dem = input("Nhập kiểu lập trình cần đếm (ví dụ: Hướng đối tượng, Thủ tục, Hướng sự kiện, Chức năng): ")

    count = dataframe[
        (dataframe['NĂM'] == nam_dem) &
        (dataframe['KIỂU LẬP TRÌNH'].str.contains(kieu_dem, case=False, na=False))
    ].shape[0]
    print(f"Số lượng ngôn ngữ lập trình ra đời năm {nam_dem} và có kiểu '{kieu_dem}': {count}")

def sap_xep_theo_nam(dataframe):
    """Sắp xếp các bản ghi theo thứ tự tăng dần của Năm."""
    print("\n--- DataFrame sau khi sắp xếp theo Năm tăng dần ---")
    df_sorted = dataframe.sort_values(by='NĂM')
    hien_thi_dataframe(df_sorted)
    return df_sorted # Trả về DataFrame đã sắp xếp nếu muốn lưu trạng thái này

def luu_file_csv(dataframe):
    """Ghi dữ liệu cuối cùng vào file CSV."""
    ten_file = input("Nhập tên file CSV để lưu (ví dụ: NNLT_custom.csv): ")
    if not ten_file.endswith('.csv'):
        ten_file += '.csv'
    try:
        dataframe.to_csv(ten_file, index=False, encoding='utf-8-sig')
        print(f"Đã ghi DataFrame vào file '{ten_file}'.")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def main_menu():
    """Hiển thị menu chính và xử lý lựa chọn của người dùng."""
    global df # Sử dụng biến df toàn cục

    while True:
        print("\nMENU CHỨC NĂNG:")
        print("-----------------------------------------------------------------")
        print("1. Hiển thị danh sách ngôn ngữ lập trình hiện tại")
        print("2. Thêm một ngôn ngữ lập trình mới")
        print("3. Sửa đổi kiểu lập trình của một ngôn ngữ")
        print("4. Xoá một ngôn ngữ lập trình")
        print("5. Lọc và hiển thị ngôn ngữ lập trình ra đời sau một năm nhất định")
        print("6. Đếm số lượng ngôn ngữ theo năm và kiểu lập trình")
        print("7. Sắp xếp danh sách theo năm ra đời (tăng dần)")
        print("8. Lưu danh sách hiện tại ra file CSV")
        print("0. Thoát chương trình")
        print("-----------------------------------------------------------------")

        lua_chon = input("Nhập lựa chọn của bạn: ")

        if lua_chon == '1':
            print("\n--- Danh sách ngôn ngữ lập trình hiện tại ---")
            hien_thi_dataframe(df)
        elif lua_chon == '2':
            # Ví dụ để thực hiện yêu cầu (2đ) của đề bài gốc:
            # Người dùng sẽ chọn 2, sau đó nhập:
            # Tên: Go
            # Năm: 2009
            # Người sáng tạo: Robert Griesemer
            # Kiểu lập trình: Thủ tục
            df = them_ngon_ngu(df)
            hien_thi_dataframe(df)
        elif lua_chon == '3':
            # Ví dụ để thực hiện yêu cầu (1đ) sửa JavaScript:
            # Người dùng sẽ chọn 3, sau đó nhập:
            # Tên ngôn ngữ cần sửa: JavaScript
            # Kiểu lập trình mới: Chức năng, Hướng sự kiện
            df = sua_kieu_lap_trinh(df)
            hien_thi_dataframe(df)
        elif lua_chon == '4':
            # Ví dụ để thực hiện yêu cầu (1đ) xóa Ruby:
            # Người dùng sẽ chọn 4, sau đó nhập:
            # Tên ngôn ngữ cần xóa: Ruby
            df = xoa_ngon_ngu(df)
            hien_thi_dataframe(df)
        elif lua_chon == '5':
            # Ví dụ để thực hiện yêu cầu (1đ) lọc sau năm 1990:
            # Người dùng sẽ chọn 5, sau đó nhập:
            # Năm để lọc: 1990
            loc_ngon_ngu_theo_nam(df)
        elif lua_chon == '6':
            # Ví dụ để thực hiện yêu cầu (1đ) đếm ngôn ngữ năm 1995, Hướng đối tượng:
            # Người dùng sẽ chọn 6, sau đó nhập:
            # Năm ra đời cần đếm: 1995
            # Kiểu lập trình cần đếm: Hướng đối tượng
            dem_ngon_ngu(df)
        elif lua_chon == '7':
            df_da_sap_xep = sap_xep_theo_nam(df)
            # Nếu muốn DataFrame chính được cập nhật thành phiên bản đã sắp xếp:
            # df = df_da_sap_xep
        elif lua_chon == '8':
            luu_file_csv(df)
        elif lua_chon == '0':
            print("Đã thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")

if __name__ == "__main__":
    print("--- Chương trình quản lý danh sách ngôn ngữ lập trình ---")
    print("DataFrame ban đầu:")
    hien_thi_dataframe(df)
    main_menu()