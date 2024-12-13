import datetime
from collections import defaultdict

class NguoiDung:
    def __init__(self, id_nguoidung, ten, lienlac):
        self.id_nguoidung = id_nguoidung
        self.ten = ten
        self.lienlac = lienlac

class BenhNhan(NguoiDung):
    def __init__(self, id_nguoidung, ten, lienlac, dieutri=None, trangthai="Khach"):
        super().__init__(id_nguoidung, ten, lienlac)
        self.dieutri = dieutri
        self.trangthai = trangthai
        self.lichhen = []  # Danh sach (datetime, id_bacsi)

    def __str__(self):
        return (f"ID: {self.id_nguoidung}, Ten: {self.ten}, Lien lac: {self.lienlac}, "
                f"Trang thai: {self.trangthai}, So lich hen: {len(self.lichhen)}")

class BacSi(NguoiDung):
    def __init__(self, id_nguoidung, ten, lienlac):
        super().__init__(id_nguoidung, ten, lienlac)
        self.lichlamviec = defaultdict(list)  # Key: ngay, Value: danh sach gio hen
        self.benhnhan = []  # Danh sach ID BenhNhan

    def __str__(self):
        return f"ID: {self.id_nguoidung}, Ten: {self.ten}, Lien lac: {self.lienlac}, So benh nhan: {len(self.benhnhan)}"

class PhongKham:
    def __init__(self):
        self.benhnhan = {}
        self.bacsi = {}
        self.lichhen = defaultdict(list)  # Key: ngay, Value: danh sach lich hen

    def them_benhnhan(self):
        print("\n--- Them Benh Nhan Moi ---")
        id_benhnhan = input("Nhap ID Benh Nhan: ")
        if id_benhnhan in self.benhnhan:
            print("Benh nhan da ton tai.")
            return
        ten = input("Nhap Ten Benh Nhan: ")
        lienlac = input("Nhap So Dien Thoai: ")
        benhnhan_moi = BenhNhan(id_benhnhan, ten, lienlac)
        self.benhnhan[id_benhnhan] = benhnhan_moi
        print("Them benh nhan thanh cong!\n")

    def them_bacsi(self):
        print("\n--- Them Bac Si Moi ---")
        id_bacsi = input("Nhap ID Bac Si: ")
        if id_bacsi in self.bacsi:
            print("Bac si da ton tai.")
            return
        ten = input("Nhap Ten Bac Si: ")
        lienlac = input("Nhap So Dien Thoai: ")
        bacsi_moi = BacSi(id_bacsi, ten, lienlac)
        self.bacsi[id_bacsi] = bacsi_moi
        print("Them bac si thanh cong!\n")

    def xem_benhnhan(self):
        print("\n--- Danh Sach Benh Nhan ---")
        if not self.benhnhan:
            print("Khong co benh nhan nao.")
            return
        for benhnhan in self.benhnhan.values():
            print(benhnhan)

    def xem_bacsi(self):
        print("\n--- Danh Sach Bac Si ---")
        if not self.bacsi:
            print("Khong co bac si nao.")
            return
        for bacsi in self.bacsi.values():
            print(bacsi)

    def dat_lich_hen(self):
        print("\n--- Dat Lich Hen ---")
        id_benhnhan = input("Nhap ID Benh Nhan: ")
        if id_benhnhan not in self.benhnhan:
            print("Khong tim thay benh nhan. Vui long them benh nhan truoc.")
            return
        id_bacsi = input("Nhap ID Bac Si: ")
        if id_bacsi not in self.bacsi:
            print("Khong tim thay bac si.")
            return
        ngay = input("Nhap Ngay Hen (YYYY-MM-DD): ")
        gio = input("Nhap Gio Hen (HH:MM): ")
        try:
            ngay_gio_hen = datetime.datetime.strptime(f"{ngay} {gio}", "%Y-%m-%d %H:%M")
        except ValueError:
            print("Ngay hoac gio khong hop le.")
            return

        if len(self.bacsi[id_bacsi].lichlamviec[ngay_gio_hen.date()]) >= 3:
            print("Bac si da day lich cho khung gio nay.")
            return

        self.benhnhan[id_benhnhan].lichhen.append((ngay_gio_hen, id_bacsi))
        self.bacsi[id_bacsi].lichlamviec[ngay_gio_hen.date()].append(ngay_gio_hen.time())
        print("Dat lich hen thanh cong!\n")

    def menu_chinh(self):
        while True:
            print("\n--- He Thong Quan Ly Phong Kham ---")
            print("1. Them Benh Nhan")
            print("2. Them Bac Si")
            print("3. Xem Danh Sach Benh Nhan")
            print("4. Xem Danh Sach Bac Si")
            print("5. Dat Lich Hen")
            print("6. Thoat")
            
            lua_chon = input("Nhap lua chon cua ban: ")
            if lua_chon == '1':
                self.them_benhnhan()
            elif lua_chon == '2':
                self.them_bacsi()
            elif lua_chon == '3':
                self.xem_benhnhan()
            elif lua_chon == '4':
                self.xem_bacsi()
            elif lua_chon == '5':
                self.dat_lich_hen()
            elif lua_chon == '6':
                print("Dang thoat he thong. Tam biet!")
                break
            else:
                print("Lua chon khong hop le. Vui long thu lai.")

if __name__ == "__main__":
    phong_kham = PhongKham()
    phong_kham.menu_chinh()
