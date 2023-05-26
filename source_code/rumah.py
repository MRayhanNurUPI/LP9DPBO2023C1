from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, luasBangunan, foto):
        super().__init__("Rumah", jml_penghuni, jml_kamar, foto)
        self.nama_pemilik = nama_pemilik
        self.luasBangunan = luasBangunan

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
   
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nLuas Bangunan : " + str(self.luasBangunan) + " m^2\n"
    
    def get_luas_bangunan(self):
        return self.luasBangunan