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
            if self.__tecrube < 24:
                return self.__yipranma_payi*10
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return (self.__maas % self.__tecrube)/2 + self.__yipranma_payi * 10
            elif self.__tecrube > 48 and self.__maas < 25000:
                return (self.__maas % self.__tecrube / 3) + self.__yipranma_payi * 10
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)
        
    def Son_maas(self):
            return self.__maas + self.__maas * 0.01 * self.zam_hakki()
        
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nTecrübe: {}\nYeni Maaş: {}\n".format(self.__ad, self.__soyad, self.__tecrube, self.Son_maas())