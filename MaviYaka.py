from Calisan import Calisan
class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = yipranma_payi
        
    def get_yipranma_payi(self):
        return self.__yipranma_payi
    
    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi
        
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return self.__yipranma_payi*10
            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube())/2 + self.__yipranma_payi * 10
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube() / 3) + self.__yipranma_payi * 10
            else:
                return 0
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)
        
    def Son_maas(self):
            return self.get_maas() + self.get_maas() * 0.01 * self.zam_hakki()
        
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nTecrübe: {}\nYeni Maaş: {}\n".format(self.get_ad(), self.get_soyad(), self.get_tecrube(), self.Son_maas())