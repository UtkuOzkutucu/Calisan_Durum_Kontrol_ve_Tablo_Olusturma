from Insan import Insan
class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu = ""
        self.__tecrube = tecrube
    
    def get_gecmis_tecrube(self):
        return self.__tecrube
    
    def set_gecmis_tecrube(self, gecmis_tecrube):
        self.__tecrube = gecmis_tecrube
    
    def statu_bul(self):
        try:
            mavi_etki= self.__tecrube["mavi_yaka"] * 0.2
            beyaz_etki = self.__tecrube["beyaz_yaka"] * 0.35
            yonetici_etki = self.__tecrube["yonetici"] * 0.45
            if mavi_etki > beyaz_etki and mavi_etki > yonetici_etki:
                self.__statu = "Mavi yaka"
            elif beyaz_etki > mavi_etki and beyaz_etki > yonetici_etki:
                self.__statu = "Beyaz yaka"
            elif yonetici_etki > mavi_etki and yonetici_etki > beyaz_etki:
                self.__statu = "Yönetici"
            else:
                print("Geçersiz statü")
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)
    
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nOnerilen Statü: {}\n".format(self.get_ad(), self.get_soyad(), self.statu_bul())

