class User:
    def __init__(self, email, password):
        self.__email = email
        self.__pas = password

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_pass(self, password):
        self.__pas = password
    def get_pass(self):
        return self.__pas

class Register(User):
    def __init__(self, username, email, password, alamat):
        super().__init__(email, password)
        self.nama = username
        self.alamat = alamat

    def set_username(self, username):
        self.nama = username
    def get_username(self):
        return self.nama

    def set_alamat(self, alamat):
        self.alamat = alamat
    def get_alamat(self):
        return self.alamat

class Login(User):
    def __init__(self,email, password):
        super().__init__(email, password)

class Pemesanan:
    def __init__(self, idOrder, alamatLengkap, jmlBarang, namaBrg, ongkirBrg, hargaBrg, totalpembayaran):
        self.alamatLengkap = alamatLengkap
        self.idOrder = idOrder
        self.jmlBarang = jmlBarang
        self.namaBrg = namaBrg
        self.ongkirBrg = ongkirBrg
        self.hargaBrg = hargaBrg
        self.totalpembayaran = totalpembayaran

    def set_alamatLengkap(self, alamatLengkap):
        self.alamatLengkap = alamatLengkap
    def get_alamatLengkap(self) : #mengambil data dari set alamat lenhkaap
        return self.alamatLengkap # mengembalikan nilai alamat lengkap

    def set_idOrder(self, idOrder):
        self.idOrder = idOrder
    def get_idOrder(self) : 
        return self.idOrder 

    def set_jmlBarang(self, jmlBarang):
        self.jmlBarang = jmlBarang
    def get_jmlBarang(self) : 
        return self.jmlBarang

    def set_namaBrg(self, namaBrg):
        self.namaBrg = namaBrg
    def get_namaBrg(self) : 
        return self.namaBrg

    def set_ongkirBrg(self, ongkirBrg):
        self.ongkirBrg = ongkirBrg
    def get_ongkirBrg(self) : 
        return self.ongkirBrg

    def set_hargaBrg(self, hargaBrg):
        self.hargaBrg = hargaBrg
    def get_hargaBrg(self) : 
        return self.hargaBrg

    def set_totalPembayaran(self, totalpembayaran):
        self.totalpembayaran = totalpembayaran
    def get_totalPemabyaran(self) : 
        return self.totalpembayaran

class Status:
    def __init__(self, id_status, status):
        self.idstatus = id_status
        self.status = status
    def set_idStatus(self, id_status):
        self.idstatus = id_status
    def get_idStatus(self):
        return self.idstatus

    def set_Status(self, status):
        self.status = status
    def get_Status(self):
        return self.status

class Pembayaran() :
    def __init__(self, idPembayaran, jml, jmlBayar, noTransaksi, diskon, tanggalPembayaran, viaPembayaran):
        self.idPembayaran = idPembayaran
        self.jml = jml
        self.jmlBayar = jmlBayar
        self.noTransaksi = noTransaksi
        self.diskon =diskon
        self.tanggalPembayaran = tanggalPembayaran
        self.viaPembayarn = viaPembayaran

    def set_idPembayaran(self, idPembayaran):
        self.idPembayaran = idPembayaran
    def get_idPembayaran(self) : 
        return self.idPembayaran 

    def set_jml(self, jml):
        self.jml = jml
    def get_jml(self) : 
        return self.jml

    def set_jmlBrg(self, jmlBayar):
        self.jmlBayar = jmlBayar
    def get_jmlBrg(self) : 
        return self.jmlBayar

    def set_noTransaksi(self, noTransaksi):
        self.noTransaksi = noTransaksi
    def get_noTransaksi(self) : 
        return self.noTransaksi

    def set_diskon(self, diskon):
        self.diskon = diskon
    def get_diskon(self) : 
        return self.diskon

    def set_tglBayar(self, tanggalPembayaran):
        self.tglBayar = tanggalPembayaran
    def get_tglBayar(self) : 
        return self.tglBayar
    
    def set_viaPembayaran(self, viaPembayaran):
        self.viapembayaran = viaPembayaran
    def get_viaPembayaran(self) : 
        return self.viaPembayaran




