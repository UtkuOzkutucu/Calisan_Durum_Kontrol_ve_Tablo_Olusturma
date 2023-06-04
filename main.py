import Insan
import Issiz
import Calisan
import MaviYaka


def main():
    try:
        insan1 = Insan("12345678910", "Ali", "Veli", 25, "Erkek", "Türk")
        print(insan1)
        
        issiz1 = Issiz("Mavi Yaka", 5)
        print(issiz1)
        
        calisan1 = Calisan.Calisan("Bilgisayar", 25, 15000)
        print(calisan1)
        
        mavi_yaka1 = MaviYaka.MaviYaka(5)
        print(mavi_yaka1)
        
        
    except Exception as Hata:
        print("Hata: ", Hata)
