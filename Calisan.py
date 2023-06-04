class Calisan:
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

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

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakli_para(self):
        try:
            if self.__tecrube < 24:
                return self.__maas 
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return self.__maas + (self.__maas * (self.__maas % self.__tecrube)) 
            elif self.__tecrube > 48 and self.__maas < 25000:
                return self.__maas + (self.__maas * (self.__maas % self.__tecrube / 2))
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)

    

        def __str__(self):
            return "Ad: {}\nSoyad: {}\nTecrübe: {}\nYeni Maaş: {}\n".format(self.__ad, self.__soyad, self.__tecrube, self.__zam_hakli_para)