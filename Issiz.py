import Insan
class Issiz(Insan):
    def __init__(self, tecrube):
        self._statu = self.statu_bul()
        self.__tecrube = tecrube
        self.__statu_dict = {"Mavi Yaka": 0.2, "Beyaz Yaka": 0.35, "Yönetici": 0.45}
    
    
    def get_tecrube(self):
        return self.__tecrube
    
    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube
    
    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0
            beyaz_yaka_etkisi = 0
            yonetici_etkisi = 0
            
            for statu, yil in self.__statu_dict.keys(), self.__tecrube:
                if statu == "Mavi yaka":
                    mavi_yaka_etkisi += yil * self.__statu_dict["Mavi Yaka"]
                elif statu == "Beyaz yaka":
                    beyaz_yaka_etkisi += yil * self.__statu_dict["Beyaz Yaka"]
                elif statu == "Yonetici":
                    yonetici_etkisi += yil * self.__statu_dict["Yonetici"]
            
            if mavi_yaka_etkisi > beyaz_yaka_etkisi and mavi_yaka_etkisi > yonetici_etkisi:
                return "mavi yaka"
            elif beyaz_yaka_etkisi > mavi_yaka_etkisi and beyaz_yaka_etkisi > yonetici_etkisi:
                return "beyaz yaka"
            else:
                return "yonetici"
        except Exception as Hata:
            print("Hata: ", Hata)
    
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nStatü: {}\nTecrübe: {}\n".format(self.get_ad(), self.get_soyad(), self.get_statu(), self.statu_bul())