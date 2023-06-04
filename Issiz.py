class Issiz:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        self.__statu = statu
        self.__statu_tecrubesi = {"mavi yaka": 0, "beyaz yaka": 0, "yonetici": 0}

    def get_tc_no(self):
        return self.__tc_no

    def set_tc_no(self, tc_no):
        self.__tc_no = tc_no

    def get_ad(self):
        return self.__ad

    def set_ad(self, ad):
        self.__ad = ad

    def get_soyad(self):
        return self.__soyad

    def set_soyad(self, soyad):
        self.__soyad = soyad

    def get_yas(self):
        return self.__yas

    def set_yas(self, yas):
        self.__yas = yas

    def get_cinsiyet(self):
        return self.__cinsiyet

    def set_cinsiyet(self, cinsiyet):
        self.__cinsiyet = cinsiyet

    def get_uyruk(self):
        return self.__uyruk

    def set_uyruk(self, uyruk):
        self.__uyruk = uyruk

    def get_statu(self):
        return self.__statu

    def set_statu(self, statu):
        self.__statu = statu

    def get_statu_tecrubesi(self):
        return self.__statu_tecrubesi

    def set_statu_tecrubesi(self, statu_tecrubesi):
        self.__statu_tecrubesi = statu_tecrubesi

    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0
            beyaz_yaka_etkisi = 0
            yonetici_etkisi = 0
            
            for statu, yil in self.__statu_tecrubesi.items():
                if statu == "mavi yaka":
                    mavi_yaka_etkisi += yil * 0.2
                elif statu == "beyaz yaka":
                    beyaz_yaka_etkisi += yil * 0.35
                elif statu == "yonetici":
                    yonetici_etkisi += yil * 0.45
            
            if mavi_yaka_etkisi > beyaz_yaka_etkisi and mavi_yaka_etkisi > yonetici_etkisi:
                return "mavi yaka"
            elif beyaz_yaka_etkisi > mavi_yaka_etkisi and beyaz_yaka_etkisi > yonetici_etkisi:
                return "beyaz yaka"
            else:
                return "yonetici"
            
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata Olustu.", Hata) #hata mesajı

    def __str__(self):
        return "Tc No: {}\nAd: {}\nSoyad: {}\nYaş: {}\nCinsiyet: {}\nUyruk: {}\nKişiye Uygun Statü: {}\n".format(self.__tc_no, self.__ad, self.__soyad, self.__yas, self.__cinsiyet, self.__uyruk, self.__statu)
    