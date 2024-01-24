# -*- coding: utf-8 -*-

class mydata:
    """
    Class dùng để lưu dữ liệu của các thành phần liên quan tới tử vi
    """
    def __init__(self, id, ten:str, viettat:str, so=None, sinhxuat=None, khacxuat=None):
      """
      Khởi tạo một đối tượng

      :param id: The unique identifier.
      :param ten: Tên của dữ liệu, lưu tiếng việt đầy đủ
      :param viet: Tên viết tắt của dữ liệu
      :param so: mảng các số liên quan tới dữ liệu này
      :param sinhxuat: mảng các id mà dữ liệu này tạo sinh, kiểu như Thổ sinh Kim thì Thổ có id của Kim trong list này, Thổ bị tổn hao
      :param khacxuat: mảng các id mà dữ liệu này khắc chế, kiểu như Kim khắc Mộc thì Kim được lợi, còn Thổ bị thiệt thòi, Kim sẽ có id của Mộc ở đây
      :return: không trả về vì đây là hàm init

      """
      self.id = id
      self.ten = ten
      self.viettat = viettat
      self.so = so if so is not None else []
      self.sinhxuat = sinhxuat if sinhxuat is not None else []
      self.khacxuat = khacxuat if khacxuat is not None else []

    def them_so(self, conso):
      self.so.append(conso)

    def __str__(self):
      return f"ID: {self.id}, Name: {self.ten}, Numbers: {self.so}"


class vt:
  """
  Dùng để dùng các từ khóa dễ dùng
  """
  def __init__(self):
    # loại đặc biệt
    self.none = -32000

    # âm dương
    self.am = mydata(-100, "Âm", "-", [0])
    self.duong = mydata(100, "Dương", "+", [1])

    # ngũ hành
    self.tho = mydata(0,"Thổ","O",[0],[6],[1])
    self.kim = mydata(6, "Kim","K", [6],[1],[3])
    self.moc = mydata(3, "Mộc","M", [3],[9],[0])
    self.thuy = mydata(1, "Thủy","T", [1],[3],[9])
    self.hoa = mydata(9,"Hỏa","H", [9],[0],[6])

    # các loại sao tốt
    self.chinhtinh = 101
    self.phutinh = 102
    self.quytinh = 103
    self.quyentinh = 104
    self.phuctinh = 105
    self.vantin = 106
    self.daicactinh = 107
    self.daohoatinh = 108
    # các loại sao xấu
    self.sattinh = 1
    self.baitinh = 1
    self.amtinh = 13
    self.damtinh = 1
    self.hinhtinh = 1
    # 3 loại phương vị
    self.detinh = 1
    self.bacdautinh = 1
    self.namdautinh = 1
    # 3 loại vòng
    self.truongsinh = 1
    self.thaitue = 1
    self.locton = 1
    self.tuongtinh = 1
    # độ sáng
    self.vuong = 1
    self.mieu = 1
    self.dac = 1
    self.binh = 1
    self.ham = 1

  def lay_ten(self, id):
    s = "khong biet"
    for key, value in self.__dict__.items():
      if not callable(value):
        if type(value)!= int:
          if value.id == id:
            s = value.ten
    
    return s

class sao:
  def __init__(self, id, Ten, NguHanh, Loai, PhuongVi, AmDuong):
    self.id = id
    self.Ten = Ten
    self.NguHanh = NguHanh
    self.Loai = Loai
    self.PhuongVi = PhuongVi
    self.AmDuong = AmDuong

  def __str__(self) -> str:
      return self.Ten

class thienban:
  def __init__(self):
    avt = vt()
    # Tử vi
    self.tuvi = sao(          1,  "Tử Vi",        avt.tho,  avt.chinhtinh,  avt.detinh,       avt.duong)
    self.liemtrinh = sao(     2,  "Liêm Trinh",   avt.hoa,  avt.chinhtinh,  avt.bacdautinh,   avt.duong) 
    self.thiendong = sao(     3,  "Thiên Đồng",   avt.thuy, avt.chinhtinh,  avt.bacdautinh,   avt.duong)
    self.vukhuc = sao(        4,  "Vũ Khúc",      avt.kim,  avt.chinhtinh,  avt.bacdautinh,   avt.am)
    self.thaiduong = sao(     5,  "Thái Dương",   avt.hoa,  avt.chinhtinh,  avt.namdautinh,   avt.duong)
    self.thienco = sao(       6,  "Thiên Cơ",     avt.moc,  avt.chinhtinh,  avt.namdautinh,   avt.am)

    # Thiên phủ
    self.thienphu = sao(      7,  "Thiên Phủ",    avt.tho,  avt.chinhtinh,  avt.namdautinh,   avt.duong)
    self.thaiam = sao(        8,  "Thái Âm",      avt.thuy, avt.chinhtinh,  avt.bacdautinh,   avt.am)
    self.thamlang = sao(      9,  "Tham Lang",    avt.thuy, avt.chinhtinh,  avt.bacdautinh,   avt.am)
    self.cumon = sao(        10,  "Cự Môn",       avt.thuy, avt.chinhtinh,  avt.bacdautinh,   avt.am)
    self.thientuong = sao(   11,  "Thiên Tướng",  avt.thuy, avt.chinhtinh,  avt.namdautinh,   avt.duong)
    self.thienluong = sao(   12,  "Thiên Lương",  avt.moc,  avt.chinhtinh,  avt.namdautinh,   avt.am)
    self.thatsat = sao(      13,  "Thát Sát",     avt.kim,  avt.chinhtinh,  avt.namdautinh,   avt.duong)
    self.phaquan = sao(      14,  "Phá Quân",     avt.thuy, avt.chinhtinh,  avt.bacdautinh,   avt.am)

  
"""
# Tử vi tinh hệ

    
saoTuVi = Sao(1, "Tử vi", "O", 1, "Đế tinh", 1, 0)
saoLiemTrinh = Sao(2, "Liêm trinh", "H", 1, "Bắc đẩu tinh", 1, 0)
saoThienDong = Sao(3, "Thiên đồng", "T", 1, "Bắc đẩu tinh", 1, 0)
saoVuKhuc = Sao(4, "Vũ khúc", "K", 1, "Bắc đẩu tinh", -1, 0)
saoThaiDuong = Sao(5, "Thái Dương", "H", 1, "Nam đẩu tinh", 1, 0)
saoThienCo = Sao(6, "Thiên cơ", "M", 1, "Nam đẩu tinh", -1, 0)

# Thiên phủ tinh hệ
saoThienPhu = Sao(7, "Thiên phủ", "O", 1, "Nam đẩu tinh", 1, 0)
saoThaiAm = Sao(8, "Thái âm", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThamLang = Sao(9, "Tham lang", "T", 1, "Bắc đẩu tinh", -1, 0)
saoCuMon = Sao(10, "Cự môn", "T", 1, "Bắc đẩu tinh", -1, 0)
saoThienTuong = Sao(11, "Thiên tướng", "T", 1, "Nam đẩu tinh", 1, 0)
saoThienLuong = Sao(12, "Thiên lương", "M", 1, "Nam đẩu tinh", -1, 0)
saoThatSat = Sao(13, "Thất sát", "K", 1, "Nam đẩu tinh", 1, 0)
saoPhaQuan = Sao(14, "Phá quân", "T", 1, "Bắc đẩu tinh", -1, 0)

# Vòng Địa chi - Thái tuế
saoThaiTue = Sao(15, "Thái tuế", "H", 15, "", 0)
saoThieuDuong = Sao(16, "Thiếu dương", "H", 5)
saoTangMon = Sao(17, "Tang môn", "M", 12)
saoThieuAm = Sao(18, "Thiếu âm", "T", 5)
saoQuanPhu3 = Sao(19, "Quan phù", "H", 12)
saoTuPhu = Sao(20, "Tử phù", "K", 12)
saoTuePha = Sao(21, "Tuế phá", "H", 12)
saoLongDuc = Sao(22, "Long đức", "T", 5)
saoBachHo = Sao(23, "Bạch hổ", "K", 12)
saoPhucDuc = Sao(24, "Phúc đức", "O", 5)
saoDieuKhach = Sao(25, "Điếu khách", "H", 12)
saoTrucPhu = Sao(26, "Trực phù", "K", 16)

#  Vòng Thiên can - Lộc tồn
saoLocTon = Sao(27, "Lộc tồn", "O", 3, "Bắc đẩu tinh")
saoBacSy = Sao(109, "Bác sỹ", "T", 5, )
saoLucSi = Sao(28, "Lực sĩ", "H", 2)
saoThanhLong = Sao(29, "Thanh long", "T", 5)
saoTieuHao = Sao(30, "Tiểu hao", "H", 12)
saoTuongQuan = Sao(31, "Tướng quân", "M", 4)
saoTauThu = Sao(32, "Tấu thư", "K", 3)
saoPhiLiem = Sao(33, "Phi liêm", "H", 2)
saoHyThan = Sao(34, "Hỷ thần", "H", 5)
saoBenhPhu = Sao(35, "Bệnh phù", "O", 12)
saoDaiHao = Sao(36, "Đại hao", "H", 12)
saoPhucBinh = Sao(37, "Phục binh", "H", 13)
saoQuanPhu2 = Sao(38, "Quan phù", "H", 12)

# Vòng Tràng sinh
saoTrangSinh = Sao(39, "Tràng sinh", "T", 5, vongTrangSinh=1)
saoMocDuc = Sao(40, "Mộc dục", "T", 14, vongTrangSinh=1)
saoQuanDoi = Sao(41, "Quan đới", "K", 4, vongTrangSinh=1)
saoLamQuan = Sao(42, "Lâm quan", "K", 7, vongTrangSinh=1)
saoDeVuong = Sao(43, "Đế vượng", "K", 5, vongTrangSinh=1)
saoSuy = Sao(44, "Suy", "T", 12, vongTrangSinh=1)
saoBenh = Sao(45, "Bệnh", "H", 12, vongTrangSinh=1)
saoTu = Sao(46, "Tử", "H", 12, vongTrangSinh=1)
saoMo = Sao(47, "Mộ", "O", vongTrangSinh=1)
saoTuyet = Sao(48, "Tuyệt", "O", 12, vongTrangSinh=1)
saoThai = Sao(49, "Thai", "O", 14, vongTrangSinh=1)
saoDuong = Sao(50, "Dưỡng", "M", 2, vongTrangSinh=1)

# Lục sát
#    Kình dương đà la
saoDaLa = Sao(51, "Đà la", "K", 11)
saoKinhDuong = Sao(52, "Kình dương", "K", 11)

#    Địa không - Địa kiếp
saoDiaKhong = Sao(53, "Địa không", "H", 11)
saoDiaKiep = Sao(54, "Địa kiếp", "H", 11)

#    Hỏa tinh - Linh tinh
saoLinhTinh = Sao(55, "Linh tinh", "H", 11)
saoHoaTinh = Sao(56, "Hỏa tinh", "H", 11)

# Sao Âm Dương
#    Văn xương - Văn khúc
saoVanXuong = Sao(57, "Văn xương", "K", 6)
saoVanKhuc = Sao(58, "Văn Khúc", "T", 6)

#    Thiên khôi - Thiên Việt
saoThienKhoi = Sao(59, "Thiên khôi", "H", 6)
saoThienViet = Sao(60, "Thiên việt", "H", 6)

#    Tả phù - Hữu bật
saoTaPhu = Sao(61, "Tả phù", "O", 2)
saoHuuBat = Sao(62, "Hữu bật", "O", 2)

#    Long trì - Phượng các
saoLongTri = Sao(63, "Long trì", "T", 3)
saoPhuongCac = Sao(64, "Phượng các", "O", 3)

#    Tam thai - Bát tọa
saoTamThai = Sao(65, "Tam thai", "M", 7)
saoBatToa = Sao(66, "Bát tọa", "T", 7)

#    Ân quang - Thiên quý
saoAnQuang = Sao(67, "Ân quang", "M", 3)
saoThienQuy = Sao(68, "Thiên quý", "O", 3)

# Sao đôi khác
saoThienKhoc = Sao(69, "Thiên khốc", "T", 12)
saoThienHu = Sao(70, "Thiên hư", "T", 12)
saoThienDuc = Sao(71, "Thiên đức", "H", 5)
saoNguyetDuc = Sao(72, "Nguyệt đức", "H", 5)
saoThienHinh = Sao(73, "Thiên hình", "H", 15)
saoThienRieu = Sao(74, "Thiên riêu", "T", 13)
saoThienY = Sao(75, "Thiên y", "T", 5)
saoQuocAn = Sao(76, "Quốc ấn", "O", 6)
saoDuongPhu = Sao(77, "Đường phù", "M", 4)
saoDaoHoa = Sao(78, "Đào hoa", "M", 8)
saoHongLoan = Sao(79, "Hồng loan", "T", 8)
saoThienHy = Sao(80, "Thiên hỷ", "T", 5)
saoThienGiai = Sao(81, "Thiên giải", "H", 5)
saoDiaGiai = Sao(82, "Địa giải", "O", 5)
saoGiaiThan = Sao(83, "Giải thần", "M", 5)
saoThaiPhu = Sao(84, "Thai phụ", "K", 6)
saoPhongCao = Sao(85, "Phong cáo", "O", 4)
saoThienTai = Sao(86, "Thiên tài", "O", 2)
saoThienTho = Sao(87, "Thiên thọ", "O", 5)
saoThienThuong = Sao(88, "Thiên thương", "O", 12)
saoThienSu = Sao(89, "Thiên sứ", "T", 12)
saoThienLa = Sao(90, "Thiên la", "O", 12)
saoDiaVong = Sao(91, "Địa võng", "O", 12)
saoHoaKhoa = Sao(92, "Hóa khoa", "T", 5)
saoHoaQuyen = Sao(93, "Hóa quyền", "T", 4)
saoHoaLoc = Sao(94, "Hóa lộc", "M", 3)
saoHoaKy = Sao(95, "Hóa kỵ", "T", 13)
saoCoThan = Sao(96, "Cô thần", "O", 13)
saoQuaTu = Sao(97, "Quả tú", "O", 13)
saoThienMa = Sao(98, "Thiên mã", "H", 3)
saoPhaToai = Sao(99, "Phá toái", "H", 12)
saoThienQuan = Sao(100, "Thiên quan", "H", 5)
saoThienPhuc = Sao(101, "Thiên phúc", "H", 5)
saoLuuHa = Sao(102, "Lưu hà", "T", 12)
saoThienTru = Sao(103, "Thiên trù", "O", 5)
saoKiepSat = Sao(104, "Kiếp sát", "H", 11)
saoHoaCai = Sao(105, "Hoa cái", "K", 14)
saoVanTinh = Sao(106, "Văn tinh", "H", 6)
saoDauQuan = Sao(107, "Đẩu quân", "H", 5)
saoThienKhong = Sao(108, "Thiên không", "T", 11)
"""