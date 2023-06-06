import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

def main():


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

    beyaz_yaka1 = BeyazYaka("12345678921", "Furkan", "Türk", 40, "Erkek", "Türk", "Teknoloji", 60, 23000, 5000)
    beyaz_yaka2 = BeyazYaka("12345678922", "Volkan", "Kılıç", 38, "Erkek", "Türk", "Muhasebe", 20, 19000, 500)
    beyaz_yaka3 = BeyazYaka("12345678923", "Ceren", "Aydın", 45, "Kadın", "Türk", "Ticaret", 30, 19000, 2500)

    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
    
    
    data = {"Tür": ["Çalışan", "Çalışan", "Çalışan", "mavi_yaka", "mavi_yaka", "mavi_yaka", "beyaz_yaka", "beyaz_yaka", "beyaz_yaka"],
            "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(), beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
            "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(), beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
            "soyad": [calisan1.get_soyad(),calisan2.get_soyad(), calisan3.get_soyad(), mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(), beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
            "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(), beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
            "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(), beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
            "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(), beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
            "sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), mavi_yaka1.get_sektor(), mavi_yaka2.get_sektor(), mavi_yaka3.get_sektor(), beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
            "tecrübe": [calisan1.get_tecrube()/12, calisan2.get_tecrube()/12, calisan3.get_tecrube()/12, mavi_yaka1.get_tecrube()/12, mavi_yaka2.get_tecrube()/12, mavi_yaka3.get_tecrube()/12, beyaz_yaka1.get_tecrube()/12, beyaz_yaka2.get_tecrube()/12, beyaz_yaka3.get_tecrube()/12 ],
            "maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(), beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
            "yıpranma_payı": [0, 0, 0, mavi_yaka1.get_yipranma_payi(), mavi_yaka2.get_yipranma_payi(), mavi_yaka3.get_yipranma_payi(), 0, 0,0],
            "teşvik_primi": [0, 0, 0, 0, 0, 0, beyaz_yaka1.get_teşvik_primi(), beyaz_yaka2.get_teşvik_primi(), beyaz_yaka3.get_teşvik_primi()],
            "yeni_maaş": [calisan1.Son_maas(), calisan2.Son_maas(), calisan3.Son_maas(), mavi_yaka1.Son_maas(), mavi_yaka2.Son_maas(), mavi_yaka3.Son_maas(), beyaz_yaka1.Son_maas(), beyaz_yaka2.Son_maas(), beyaz_yaka3.Son_maas() ]}
    df = pd.DataFrame(data)
    print(df)
    
    
    print(df.groupby("Tür")[["tecrübe", "yeni_maaş"]].mean())
    
    print("Maaşı 15000 üzerinde olanların sayısı:", df[df["maaş"] > 15000]["maaş"].count())
    
    print(df.sort_values("yeni_maaş"))
    
    print(df[(df["tecrübe"] > 3) & (df["Tür"] == "beyaz_yaka")])
    
    print(df[df["yeni_maaş"] > 10000].iloc[1:5, [1,12]])
    
    df2 = df[["ad", "soyad", "sektör", "yeni_maaş"]]
    print(df2)
    print("Bu Branch'te değişiklik yapıldı.")


main()

    