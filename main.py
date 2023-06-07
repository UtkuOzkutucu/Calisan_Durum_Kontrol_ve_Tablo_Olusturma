import pandas as pd             # pandas kütüphanesini pd olarak import ediyoruz
from Insan import Insan         # Insan sınıfını import ediyoruz
from Issiz import Issiz         # Issiz sınıfını import ediyoruz
from Calisan import Calisan     # Calisan sınıfını import ediyoruz
from MaviYaka import MaviYaka   # MaviYaka sınıfını import ediyoruz
from BeyazYaka import BeyazYaka # BeyazYaka sınıfını import ediyoruz

def main():                     # main fonksiyonu


    insan1 = Insan("12345678910", "Ali", "Veli", 18, "Erkek", "Türk")           #insan1 nesnesi oluşturuluyor
    insan2 = Insan("12345678911", "John", "Clark", 34, "Kadın", "Amerikalı")    #insan2 nesnesi oluşturuluyor
    
    print(insan1)       #insan1 nesnesi yazdırılıyor
    print(insan2)       #insan2 nesnesi yazdırılıyor

    issiz1 = Issiz("12345678912", "Ahmet", "Mehmet", 40, "Erkek", "Türk", {"mavi_yaka": 62, "beyaz_yaka": 30, "yonetici": 10})      #issiz1 nesnesi oluşturuluyor
    issiz2= Issiz("12345678913", "Zehra", "Tosun", 52, "Kadın", "Türk", {"mavi_yaka": 180, "beyaz_yaka": 20, "yonetici": 80})       #issiz2 nesnesi oluşturuluyor
    issiz3 = Issiz("12345678914", "Aylin", "Özdemir", 44, "Kadın", "Türk", {"mavi_yaka": 90, "beyaz_yaka": 50, "yonetici": 500})    #issiz3 nesnesi oluşturuluyor

    print(issiz1)       #issiz1 nesnesi yazdırılıyor
    print(issiz2)       #issiz2 nesnesi yazdırılıyor
    print(issiz3)       #issiz3 nesnesi yazdırılıyor

    calisan1 = Calisan("12345678915", "Zeynep", "Kaya", 33, "Kadın", "Türk", "Muhasebe", 15, 9000)      #calisan1 nesnesi oluşturuluyor
    calisan2 = Calisan("12345678916", "Emre", "Demir", 51, "Erkek", "Türk", "İnşaat", 32, 15000)        #calisan2 nesnesi oluşturuluyor
    calisan3 = Calisan("12345678917", "Murat", "Öztürk", 30, "Erkek", "Türk", "Teknoloji", 60, 30000)   #calisan3 nesnesi oluşturuluyor

    print(calisan1)     #calisan1 nesnesi yazdırılıyor
    print(calisan2)     #calisan2 nesnesi yazdırılıyor
    print(calisan3)     #calisan3 nesnesi yazdırılıyor

    mavi_yaka1 = MaviYaka("12345678918", "Cemre", "Aksoy", 51, "Erkek", "Türk", "E-Ticaret", 60, 10000, 0.4)    #mavi_yaka1 nesnesi oluşturuluyor
    mavi_yaka2 = MaviYaka("12345678919", "Cem", "Özdemir", 62, "Erkek", "Türk", "Diğer", 120, 10000, 0.8)       #mavi_yaka2 nesnesi oluşturuluyor 
    mavi_yaka3 = MaviYaka("12345678920", "Cankat", "Parlat", 35, "Erkek", "Türk", "Teknoloji", 30, 10000, 0.1)  #mavi_yaka3 nesnesi oluşturuluyor

    print(mavi_yaka1)   #mavi_yaka1 nesnesi yazdırılıyor
    print(mavi_yaka2)   #mavi_yaka2 nesnesi yazdırılıyor
    print(mavi_yaka3)   #mavi_yaka3 nesnesi yazdırılıyor

    beyaz_yaka1 = BeyazYaka("12345678921", "Furkan", "Türk", 40, "Erkek", "Türk", "Teknoloji", 60, 23000, 5000) #beyaz_yaka1 nesnesi oluşturuluyor
    beyaz_yaka2 = BeyazYaka("12345678922", "Volkan", "Kılıç", 38, "Erkek", "Türk", "Muhasebe", 20, 19000, 500)  #beyaz_yaka2 nesnesi oluşturuluyor
    beyaz_yaka3 = BeyazYaka("12345678923", "Ceren", "Aydın", 45, "Kadın", "Türk", "Ticaret", 30, 19000, 2500)   #beyaz_yaka3 nesnesi oluşturuluyor

    print(beyaz_yaka1)  #beyaz_yaka1 nesnesi yazdırılıyor
    print(beyaz_yaka2)  #beyaz_yaka2 nesnesi yazdırılıyor
    print(beyaz_yaka3)  #beyaz_yaka3 nesnesi yazdırılıyor
    
    
    data = {"Tür": ["Çalışan", "Çalışan", "Çalışan", "mavi_yaka", "mavi_yaka", "mavi_yaka", "beyaz_yaka", "beyaz_yaka", "beyaz_yaka"], #data adında bir sözlük oluşturuluyor
            "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()], #data sözlüğüne get_tc_no fonksiyonları ile tc_no bilgileri ekleniyor
            "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],                               #data sözlüğüne get_ad fonksiyonları ile ad bilgileri ekleniyor
            "soyad": [calisan1.get_soyad(),calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],  #data sözlüğüne get_soyad fonksiyonları ile soyad bilgileri ekleniyor
            "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],                     #data sözlüğüne get_yas fonksiyonları ile yas bilgileri ekleniyor
            "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],   #data sözlüğüne get_cinsiyet fonksiyonları ile cinsiyet bilgileri ekleniyor
            "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()], #data sözlüğüne get_uyruk fonksiyonları ile uyruk bilgileri ekleniyor
            "sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],                       #data sözlüğüne get_sektor fonksiyonları ile sektor bilgileri ekleniyor
            "tecrübe": [calisan1.get_tecrube()/12, calisan2.get_tecrube()/12, calisan3.get_tecrube()/12, mavi_yaka1.get_tecrube()/12, mavi_yaka2.get_tecrube()/12, mavi_yaka3.get_tecrube()/12, beyaz_yaka1.get_tecrube()/12, beyaz_yaka2.get_tecrube()/12, beyaz_yaka3.get_tecrube()/12 ], #data sözlüğüne get_tecrube fonksiyonları ile tecrube bilgileri ekleniyor
            "maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],           #data sözlüğüne get_maas fonksiyonları ile maas bilgileri ekleniyor
            "yıpranma_payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0,0], #data sözlüğüne get_yipranma_payi fonksiyonları ile yipranma_payi bilgileri ekleniyor
            "teşvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_teşvik_primi(), beyaz_yaka2.get_teşvik_primi(), beyaz_yaka3.get_teşvik_primi()], #data sözlüğüne get_teşvik_primi fonksiyonları ile teşvik_primi bilgileri ekleniyor
            "yeni_maaş": [calisan1.Son_maas(), calisan2.Son_maas(), calisan3.Son_maas(), mavi_yaka1.Son_maas(), mavi_yaka2.Son_maas(), mavi_yaka3.Son_maas(), beyaz_yaka1.Son_maas(), beyaz_yaka2.Son_maas(), beyaz_yaka3.Son_maas() ]} #data sözlüğüne Son_maas fonksiyonları ile yeni_maaş bilgileri ekleniyor
    df = pd.DataFrame(data) #data sözlüğü dataframe'e dönüştürülüyor
    print(df)               #dataframe yazdırılıyor
    
    
    print(df.groupby("Tür")[["tecrübe", "yeni_maaş"]].mean()) #Çalışan, mavi yaka ve beyaz yaka için gruplandırma yapılıyor ve gruplanan değerlerin ortalama değerleri alınıyor
    
    print("Maaşı 15000 üzerinde olanların sayısı:", df[df["maaş"] > 15000]["maaş"].count()) #maaşı 15000 üzerinde kaç kişi olduğu yazdırılıyor
    
    print(df.sort_values("yeni_maaş")) #yeni maaşa göre Dataframe'i küçükten büyüğe sıralama yapılıyor
    
    print(df[(df["tecrübe"] > 3) & (df["Tür"] == "beyaz_yaka")]) #tecrübesi 3 yıldan fazla olan beyaz yaka çalışanlar yazdırılıyor
    
    print(df[df["yeni_maaş"] > 10000].iloc[1:5, [1,12]]) #yeni maaşı 10000 üzerinde olan çalışanların 2. ve 5. satırları arasındaki ad ve yeni maaş bilgileri yazdırılıyor
    
    df2 = df[["ad", "soyad", "sektör", "yeni_maaş"]] #ad, soyad, sektör ve yeni maaş bilgileri df2 dataframe'ine aktarılıyor
    print(df2) #df2 yazdırılıyor

main() #main fonksiyonu çağırılıyor

    