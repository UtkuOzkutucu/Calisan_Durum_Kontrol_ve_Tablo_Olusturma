from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, teşvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__teşvik_primi = teşvik_primi
        
    def get_teşvik_primi(self):
        return self.__teşvik_primi
    
    def set_teşvik_primi(self, teşvik_primi):
        self.__teşvik_primi = teşvik_primi
        
    def zam_hakki(self):
        try:
            if self.get_tecrube() < 24:
                return 0
            elif self.get_tecrube() >= 24 and self.get_tecrube() <= 48 and self.get_maas() < 15000:
                return (self.get_maas() % self.get_tecrube())*5 
            elif self.get_tecrube() > 48 and self.get_maas() < 25000:
                return (self.get_maas() % self.get_tecrube())*4 
            else:
                return 0
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata) 
        
    def Son_maas(self):
            return self.get_maas() + (self.get_maas() * 0.01 * self.zam_hakki()) + self.__teşvik_primi
        
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nTecrübe: {}\nYeni Maaş: {}\n".format(self.get_ad(), self.get_soyad(), self.get_tecrube(), self.Son_maas())