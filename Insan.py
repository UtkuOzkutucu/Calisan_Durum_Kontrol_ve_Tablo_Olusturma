class Insan: #Insan sınıfı oluşturuluyor
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk): #init metodu oluşturuluyor
        self.__tc_no = tc_no
        self.__ad = ad
        self.__soyad = soyad
        self.__yas = yas
        self.__cinsiyet = cinsiyet
        self.__uyruk = uyruk

 #Insan sınıfının get ve set fonksiyonları oluşturuluyor
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
        
 #Insan sınıfının str fonksiyonu oluşturuluyor
    def __str__(self):
        return "Tc No: {}\nAd: {}\nSoyad: {}\nYaş: {}\nCinsiyet: {}\nUyruk: {}\n".format(self.__tc_no, self.__ad, self.__soyad, self.__yas, self.__cinsiyet, self.__uyruk)