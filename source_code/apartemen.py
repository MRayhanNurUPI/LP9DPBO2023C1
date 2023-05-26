from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, tower, foto):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, foto)
        self.nama_pemilik = nama_pemilik
        self.tower = tower

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nNama Tower : " + self.tower + "\n"
    
    def get_tower(self):
        return self.tower