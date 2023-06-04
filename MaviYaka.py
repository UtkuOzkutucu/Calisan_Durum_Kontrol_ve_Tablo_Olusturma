import Calisan
class MaviYaka(Calisan):
    def __init__(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self):
        try:
            if self.__tecrube < 24:
                return (self.__yipranma_payi*10)
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return (self.__maas % self.__tecrube)/2 + (self.__yipranma_payi*10)
            elif self.__tecrube > 48 and self.__maas < 25000:
                return ((self.__maas %self.__tecrube)/3 + (self.__yipranma_payi*10))
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)

    def Son_maas(self):
        try:
            if self.__tecrube < 24:
                return self.__maas+ (self.__maas * (self.__yipranma_payi*10))
            elif self.__tecrube >= 24 and self.__tecrube <= 48 and self.__maas < 15000:
                return self.__maas + (self.__maas * (self.__maas % self.__tecrube)/2 + (self.__yipranma_payi*10))
            elif self.__tecrube > 48 and self.__maas < 25000:
                return self.__maas + (self.__maas * (self.__maas %self.__tecrube)/3 + (self.__yipranma_payi*10))
            else:
                return self.__maas
        except Exception as Hata: #hatanın ne hatası olduğunu gösterme
            print("Hata: ", Hata)

    def __str__(self):
        return "Ad: " + self.__ad + "\nSoyad: " + self.__soyad + "\nTecrübe: " + str(self.__tecrube) + "\nYeni Maaş: " + str(self.Son_maas()) 
    

