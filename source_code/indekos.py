from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, no_kamar, foto):
        super().__init__("Indekos", 1, 1, foto)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.no_kamar = no_kamar

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni

    def get_nomor_kamar(self):
        return self.no_kamar

    def get_detail(self):
        return "Pemilik Kos : " + self.nama_pemilik + "\nNama Penghuni : " + self.nama_penghuni + "\nNomor Kamar : " + self.no_kamar + "\n"