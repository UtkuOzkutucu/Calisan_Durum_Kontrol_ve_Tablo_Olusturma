from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

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

    def zam_hakki(self):
        try:
            if self.__tecrube < 24:
                return 0
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return (self.__maas % self.__tecrube)
            elif self.__tecrube > 48 and self.__maas < 25000:
                return (self.__maas % self.__tecrube / 2)
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)

    def Son_maas(self):
            return self.__maas + self.__maas * 0.01 * self.zam_hakki()
        

    def __str__(self):
        return "Ad: {}\nSoyad: {}\nTecrübe: {}\nYeni Maaş: {}\n".format(self.__ad, self.__soyad, self.__tecrube, self.Son_maas())