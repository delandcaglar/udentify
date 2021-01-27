import os
import shutil
import time


#0 incisi ve birincisi deger almali

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)



#yeni_liste =[["Under Armour","Under Armour Zorlu Center",239,ilk_tarih,son_tarih,160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]],["Under Armour","Under Armour Akasya",240,ilk_tarih,son_tarih,161,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]],["Under Armour","Under Armour Istinye Park",228,ilk_tarih,son_tarih,149,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]]]


# gereken_dosya = "Under Armour"
# gereken_dosya_ismi = "under_armour_akasya.docx"

# magaza_adi_listesi =[["Under Armour","Under Armour Zorlu Center",239,"01/12/2020","25/12/2020",160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Zorlu Center"],
#                      ["Under Armour","Under Armour Akasya",240,"01/12/2020","25/12/2020",161,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Akasya"],
#                      ["Under Armour","Under Armour Istinye Park",228,"01/12/2020","25/12/2020",149,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Istinye Park"],
#                     ["Suwen","Suwen Viaport",307,"01/12/2020","25/12/2020",189,[["TAYT","ÇORAP"],["ATLET","ERKEK REYONU"]],"Viaport"]
#                      ]

def dosya_yaratici(magaza,BASE_DIR):

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #print(BASE_DIR)



    gereken_dosya = magaza[0]
    #print ( gereken_dosya )
    gereken_dosya_ismi = magaza[1] ## 2 ler 1 oldu
    #print(gereken_dosya_ismi)
    dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify/firms/{gereken_dosya}" )
    print("hata sebebi")
    print(magaza)
    print ( dosya_yolu )

    # if os.path.exists ( dosya_yolu ):  # firma ismi dosyasi yaratmak icin calisiyor
    #     print(dosya_yolu)
    #     print ( "dosya_kotrol1" )
    #     shutil.rmtree ( dosya_yolu )  # temizleme kodu

    if not os.path.exists ( dosya_yolu ): # firma ismi dosyasi yaratmak icin calisiyor
        print ( dosya_yolu )
        print ( "yaratildi1" )
        os.makedirs ( dosya_yolu )
        print("bak_yaratmismi")


    dosya_statik_resimler_yolu = os.path.join ( BASE_DIR, f"bot_udentify/firms/{gereken_dosya}/Statik {gereken_dosya_ismi}" )

    if os.path.exists ( dosya_statik_resimler_yolu ):  # firma ismi dosyasi yaratmak icin calisiyor
        print ( dosya_statik_resimler_yolu )
        print ( "dosya_kotrol2" )
        shutil.rmtree ( dosya_statik_resimler_yolu )  # temizleme kodu
    if not os.path.exists ( dosya_statik_resimler_yolu ): # firma ismi dosyasi yaratmak icin calisiyor
        print ( "yaratildi2" )
        print ( dosya_statik_resimler_yolu )
        os.makedirs ( dosya_statik_resimler_yolu )
    else:
        print ( "yaratilamadi_statik_dosya" )
        print ( dosya_statik_resimler_yolu )


    dosya_word_yolu = f"{dosya_yolu}/{gereken_dosya_ismi}.docx"
    #print(dosya_word_yolu)

    if os.path.exists ( dosya_word_yolu ):  # firma ismi dosyasi yaratmak icin calisiyor
        print ( dosya_word_yolu )
        print ( "dosya_kotrol3" )
        os.remove ( dosya_word_yolu )  # temizleme kodu
    if not os.path.exists ( dosya_word_yolu ):
        print ( "yaratildi3" )
        print ( dosya_word_yolu )
        file = open ( dosya_word_yolu, 'w+' )
    else:
        print ( "yaratilamadi_word_dosyasu" )
        print ( dosya_word_yolu )


    src_dir = f"{BASE_DIR}/bot_udentify/statik_resimler"  ### burayi statik yapmalisin
    dst_dir = os.path.join ( BASE_DIR, f"bot_udentify/firms/{magaza[0]}/Statik {magaza[1]}")

    ########!!!!!!!!!!______burraya magaza logolarini ekle imagenamees kismina f string koy o string urun basina degissin
    imageNames = (os.listdir ( src_dir ))

    # imageNames = ['en_cok_ziyaret.png', 'giren_m_1.png', 'giren_m_1_c.png', 'gunluk_kisi_sure_grafigi.png','gunluk_toplam_kisi_ve_sure.png',
    #               'isi1.png', 'isi1_deneme.png', 'isi2.png', 'isi3.png', 'kisi_sure-1.png', 'kisi_sure_grafigi.png',
    #               'magaza_ici_dagilimi.png', 'musteri_sayisi.png','performans_tablosu.png', 'saatlik_kisi_sure.png',
    #               'tablo-1.png', 'tablo-2.png', 'tablo-3.png', 'tablo-4.png','tablo-5.png', 'tablo-6.png',
    #               'ters_ucgen.png', 'top5.png', 'toplam_kisi_sure.png', 'Under Armour_logo.png', 'under_armour_logo1.png',
    #               'uzuntablo.png', 'yogunlu_m2.png', 'yogunluk.png',
    #               'yogunluk_haritasi.png', 'yogunluk_yogunluk_ortalamasi.png', 'korelasyonlar.png','Suwen_logo.png','udentify.png']
    for imageName in imageNames:

        try:
            shutil.copy ( os.path.join ( src_dir, imageName ), dst_dir )
        except shutil.SameFileError:
            print("duplicate")
            pass


# magaza_adi_listesi =[["under armour","under armour zorlu center",239,"01/12/2020","25/12/2020",160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Zorlu Center"],
#                      ["under armour","under armour akasya",240,"01/12/2020","25/12/2020",161,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Akasya"],
#                      ["under armour","under armour istinye Park",228,"01/12/2020","25/12/2020",149,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],"Istinye Park"],
#                      ["suwen","Suwen Viaport",307,"01/12/2020","25/12/2020",189,[["TAYT","ÇORAP"],["ATLET","ERKEK REYONU"]],"Viaport"]
#                   ]
#
#
# print(magaza_adi_listesi)
# magaza = magaza_adi_listesi[0]
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     #print(BASE_DIR)
#
#
#
# gereken_dosya = magaza[0]
# #print ( gereken_dosya )
# gereken_dosya_ismi = magaza[1] ## 2 ler 1 oldu
# #print(gereken_dosya_ismi)
# dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify/firms/{gereken_dosya}" )
# print("hata sebebi")
# print(magaza)
#
# #dosya_yolu1 = os.path.join ( BASE_DIR, f"bot_udentify/firms/Ebebek" )
#
# # if os.path.exists ( dosya_yolu ):  # firma ismi dosyasi yaratmak icin calisiyor
# #     print("lololo")
# #     shutil.rmtree ( dosya_yolu ) # temizleme kodu
#
# if not os.path.exists ( dosya_yolu ):  # firma ismi dosyasi yaratmak icin calisiyor
#     os.makedirs ( dosya_yolu )
#
# src_dir = f"{BASE_DIR}/bot_udentify/statik_resimler"  ### burayi statik yapmalisin
# print(src_dir)
# imageNames = (os.listdir(src_dir))




##burradaki kod dosya duzeninde sikintiya yol aciyor bbir sonuc bul







#dosya_yaratici(magaza_adi_listesi)
