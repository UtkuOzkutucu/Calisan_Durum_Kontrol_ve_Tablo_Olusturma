from Insan import Insan # Insan sınıfını import ediyoruz
class Issiz(Insan): #Issiz sınıfı Insan sınıfından kalıtılıyor
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, tecrube): #init metodu oluşturuluyor
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu = ""
        self.__tecrube = tecrube 
        self.statu_bul() 
        
 #Issiz sınıfının get ve set fonksiyonları oluşturuluyor
    def get_gecmis_tecrube(self):
        return self.__tecrube
    
    def set_gecmis_tecrube(self, tecrube):
        self.__tecrube = tecrube

    #Issiz sınıfının statu_bul fonksiyonu oluşturuluyor
    def statu_bul(self):
        try:
            mavi_etki= self.__tecrube["mavi_yaka"] * 0.2 #mavi_yaka etkisi hesaplanıyor
            beyaz_etki = self.__tecrube["beyaz_yaka"] * 0.35 #beyaz_yaka etkisi hesaplanıyor
            yonetici_etki = self.__tecrube["yonetici"] * 0.45   #yonetici etkisi hesaplanıyor
            if mavi_etki > beyaz_etki and mavi_etki > yonetici_etki: #mavi_yaka etkisi beyaz_yaka ve yonetici etkisinden büyükse
                self.__statu = "Mavi yaka" #statu mavi_yaka olarak atanıyor
            elif beyaz_etki > mavi_etki and beyaz_etki > yonetici_etki: #beyaz_yaka etkisi mavi_yaka ve yonetici etkisinden büyükse
                self.__statu = "Beyaz yaka" #statu beyaz_yaka olarak atanıyor
            elif yonetici_etki > mavi_etki and yonetici_etki > beyaz_etki: #yonetici etkisi mavi_yaka ve beyaz_yaka etkisinden büyükse
                self.__statu = "Yönetici" #statu yonetici olarak atanıyor
            else: #yukarıdaki koşullar sağlanmıyorsa
                self.__statu = "İşsiz" #statu issiz olarak atanıyor
        except Exception as Hata:
            print("Hata: ", Hata)
            
    #Issiz sınıfının get_statu fonksiyonu oluşturuluyor
    def get_statu(self):
        return self.__statu
    
    #Issiz sınıfının str fonksiyonu oluşturuluyor
    def __str__(self):
        return "Ad: {}\nSoyad: {}\nOnerilen Statü: {}\n".format(self.get_ad(), self.get_soyad(), self.get_statu())

