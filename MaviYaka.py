class MaviYaka():
    def __init__(self, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yipranma_payi = yipranma_payi

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

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.__tecrube < 24:
                return self.__maas+ (self.__maas * (self.__yipranma_payi*10))
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return self.__maas + (self.__maas * (self.__maas % self.__tecrube))
            elif self.__tecrube > 48 and self.__maas < 25000:
                return self.__maas + (self.__maas * (self.__maas % self.__tecrube / 2))
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)

    def __str__(self):
        return "Ad: " + self.__ad + "\nSoyad: " + self.__soyad + "\nTecrübe: " + str(self.__tecrube) + "\nYeni Maaş: " + str(self.zam_hakki())
    

