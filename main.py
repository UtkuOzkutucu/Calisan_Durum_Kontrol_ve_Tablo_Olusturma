from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka


def main():
    try:

        insan1 = Insan("12345678910", "Ali", "Veli", 18, "Erkek", "Türk")
        insan2 = Insan("12345678911", "John", "Clark", 34, "Kadın", "Amerikalı")
        print(insan1)
        print(insan2)

        issiz1 = Issiz("12345678912", "Ahmet", "Mehmet", 40, "Erkek", "Türk", {"mavi_yaka": 62, "beyaz_yaka": 30, "yonetici": 10})
        issiz2= Issiz("12345678913", "Zehra", "Tosun", 52, "Kadın", "Türk", {"mavi_yaka": 180, "beyaz_yaka": 20, "yonetici": 80})
        issiz3 = Issiz("12345678914", "Aylin", "Özdemir", 44, "Kadın", "Türk", {"mavi_yaka": 90, "beyaz_yaka": 50, "yonetici": 500})

        print(issiz1)
        print(issiz2)
        print(issiz3)

        calisan1 = Calisan("12345678915", "Zeynep", "Kaya", 33, "Kadın", "Türk", "Muhasebe", 15, 9000)
        calisan2 = Calisan("12345678916", "Emre", "Demir", 51, "Erkek", "Türk", "İnşaat", 32, 15000)
        calisan3 = Calisan("12345678917", "Murat", "Öztürk", 30, "Erkek", "Türk", "Teknoloji", 60, 30000)

        print(calisan1)
        print(calisan2)
        print(calisan3)

        mavi_yaka1 = MaviYaka("12345678918", "Cemre", "Aksoy", 51, "Erkek", "Türk", "E-Ticaret", 60, 10000, 0.4)
        mavi_yaka2 = MaviYaka("12345678919", "Cem", "Özdemir", 62, "Erkek", "Türk", "Diğer", 120, 10000, 0.8)
        mavi_yaka3 = MaviYaka("12345678920", "Cankat", "Parlat", 35, "Erkek", "Türk", "Teknoloji", 30, 10000, 0.1)

        print(mavi_yaka1)
        print(mavi_yaka2)
        print(mavi_yaka3)

        beyaz_yaka1 = BeyazYaka("12345678920", "Furkan", "Türk", 40, "Erkek", "Türk", "Teknoloji", 60, 23000, 5000)
        beyaz_yaka2 = BeyazYaka("12345678921", "Volkan", "Kılıç", 38, "Erkek", "Türk", "Muhasebe", 20, 19000, 500)
        beyaz_yaka3 = BeyazYaka("12345678922", "Ceren", "Aydın", 45, "Kadın", "Türk", "Ticaret", 30, 19000, 2500)

        print(beyaz_yaka1)
        print(beyaz_yaka2)
        print(beyaz_yaka3)
    except Exception as Hata:
        print("Hata: ", Hata)

main()