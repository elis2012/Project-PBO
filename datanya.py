import sqlite3
import register as rg
dataUser = "data.db"
data = sqlite3.connect(dataUser)
data.execute(
    "create table if not exists dataUser (email text primary key, password text, nama text, alamat text)"
)
data.execute(
    "create table if not exists login (email text primary key, password text)"
)
data.execute(
    "create table if not exists pemesanan (id_order int primary key, alamat TEXT, jmlBarang int, namaBrg TEXT, ongkirBrg int, hargaBrg int, TotalPembayaran int)"
)
data.execute(
    "create table if not exists pembayaran (id_bayar int primary key, jumlah int, jmlBayar int, noTransaksi int, diskon int, viaPembayaran int, tglBayar datetime)"
)
data.execute(
    "create table if not exists status (id_status int primary key, status text)"
)

user1Reg = [
    rg.Register(input('masukkan email anda :'),input('masukkan password :'),input('masukkan nama :'), input('masukkan alamat :'))
]
user1Lg = [
    rg.Login(input('masukkan email anda :'),input('masukkan password :'))
]

pesan = [
    rg.Pemesanan(input('masukkan id order :'),input('masukkan alamat lengkap :'), input('masukkan jumlah barang : '), input('masukkan nama barang :'), input('masukkan ongkir : '), input('masukkan harga : '),'')
]

status = [
    rg.Status(input('masukkan id status :'),input('masukkan status :'))
]
#bayar = [
#    rg.Pembayaran(input('masukkan id order'),input('masukkan jumlah harga :'), input('masukkan jumlah pembayaran : '), input('masukkan no transaksi :'), input('masukkan diskon : '), input('masukkan tgl pembayaran : '), input('masukkan via pembayaran : '))
#]

for user in user1Reg:
    res = data.execute('select * from dataUser where email = ?', (user.get_email(),))
    if res.fetchone() is None:
        data.execute("insert into dataUser values (?,?,?,?)", (user.get_email(), user.get_pass(), user.get_username(), user.get_alamat()))
        data.commit()

for login in user1Lg:
    lg = data.execute('select * from login where email = ?', (login.get_email(),))
    if lg.fetchone() is None:
        data.execute("insert into login values (?,?)", (login.get_email(), login.get_pass()))
        data.commit()

for pemesanan in pesan:
    psn = data.execute('select * from pemesanan where id_order = ?', (pemesanan.get_idOrder(),))
    if psn.fetchone() is None:
        data.execute("insert into pemesanan values (?,?,?,?,?,?,?)", (pemesanan.get_idOrder(), pemesanan.get_alamatLengkap(), pemesanan.get_jmlBarang(), pemesanan.get_namaBrg(), pemesanan.get_ongkirBrg(), pemesanan.get_hargaBrg(), pemesanan.get_totalPemabyaran()))
        data.commit()

#for pembayaran in bayar:
 #   byr = data.execute('select * from pembayaran where id_bayar = ?', (pembayaran.get_idPembayaran(),))
  #  if byr.fetchone() is None:
   #     data.execute("insert into pembayaran values (?,?,?,?,?,?,?)", (pembayaran.get_idPembayaran(), pembayaran.get_jml(), pembayaran.jmlBayar(), pembayaran.get_noTransaksi(), pembayaran.get_diskon(), pembayaran.get_tglBayar(), pembayaran.get_viaPembayaran()))
    #    data.commit()

for status in status:
    sts = data.execute('select * from status where id_status = ?', (status.get_idStatus(),))
    if sts.fetchone() is None:
        data.execute("insert into status values (?,?)", (status.get_idStatus(), status.get_Status()))
        data.commit()


cursor = data.cursor().execute("select * from dataUser")
for row in cursor:
    print('Register :')
    print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}')
    print('_'*50)

cursor = data.cursor().execute("select * from login")
for row in cursor:
    print('Login :')
    print(f'{row[0]}, {row[1]}')
    print('_'*50)

cursor = data.cursor().execute("select * from pemesanan")
for row in cursor:
    print('pesanan :')
    print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')
    print('_'*50)

#cursor = data.cursor().execute("select * from pembayaran")
#for row in cursor:
  #  print('pembayaran :')
   # print(f'{row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}, {row[5]}, {row[6]}')
    #print('_'*50)

cursor = data.cursor().execute("select * from status")
for row in cursor:
    print('status :')
    print(f'{row[0]}, {row[1]}')
    print('_'*50)
data.close()