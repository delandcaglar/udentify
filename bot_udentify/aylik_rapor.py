from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement, ns
import os
import heatmap
import datetime
import calendar
import request1
from scipy.stats.stats import pearsonr
import math
import matplotlib.pyplot as plt
import io
from PIL import Image




global_test =  True






#Genel_variabler
"""
Tüm_hafta_uzunlugu = son tarih - ilk tarih

"""
##pdf e cevirirken access vermen gerekli pythona dosyalar icin
firma = "Under Armour"
magza_statik_dosya_location_ismi = "Under Armour Akasya"
gereken_dosya_ismi = "Under Armour Akasya"
magaza_id_no = 240
magaza_adi = "Kad'ikoy"

ilk_tarih = "01/12/2020"
son_tarih = "25/12/2020"
tarih = ""

if global_test == True:
    print("global version")
    BASE_DIR = os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) )
    print ( BASE_DIR )
    magza_statik_dosya_location = os.path.join ( BASE_DIR, f"bot_udentify/firms/{firma}/Statik {magza_statik_dosya_location_ismi}" )
    print ( magza_statik_dosya_location )
    dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify/firms/{firma}" )
    magaza_dosyasi_ismi = f"{dosya_yolu}/{magza_statik_dosya_location_ismi}.docx"  ##bunu sona baglayacan

else:

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(BASE_DIR)
    magza_statik_dosya_location = os.path.join(BASE_DIR, 'bot_udentify/demo_resimler')
    print(magza_statik_dosya_location)
    dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify" )
    magaza_dosyasi_ismi = (f"{dosya_yolu}/demo.docx")



##global liste fonksiyonlari

def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg




#1.1 için fonksiyon______________________


#1.1 global variables



""" 1-)Hangi günün pazartesi olduğunu bul 
2-)pazartesiden  sonra haftalara böl 4 parçada bak 5 günün ortalamasını al sonra kalan 2 günün ortalamasını al
3-)kişi sayısı 2 tanesinde fazla isi artmaktadır de 4 taneesi uzerinden
4-)ortalama süreeyi çek veye listelerin ortalamasını al ve yazdır 
5-)yukarıda yaptığun hafta içi hafta sonu değerlerini oranla 
6-)Yogunlik ortalamasi al toplam sureye bol


Kullanılacak varıabler *****
Magza_adi =
Magza_tarihi =
baslik_adlari = [] ## bunu dinamik liste yap"""




###1.11   tarih gerekli

def tarihi_bul(ilk_tarih1, son_tarih1):
    global tarih
    global ilk_tarih
    global son_tarih
    tarih = f"{ilk_tarih1} - {son_tarih1}" ##gloabal variable unutma

def magaza_adi_(magaza_adi1):
    global magaza_adi
    magaza_adi = magaza_adi1

tarihi_bul(ilk_tarih, son_tarih)
magaza_adi_(magza_statik_dosya_location_ismi)









#2.1 için fonksiyon______________________
""" 1-)Hangi günün pazartesi olduğunu bul 
2-)pazartesiden  sonra haftalara böl 4 parçada bak 5 günün ortalamasını al sonra kalan 2 günün ortalamasını al
3-)kişi sayısı 2 tanesinde fazla isi artmaktadır de 4 taneesi uzerinden
4-)ortalama süreeyi çek veye listelerin ortalamasını al ve yazdır 
5-)yukarıda yaptığun hafta içi hafta sonu değerlerini oranla 
6-)Yogunlik ortalamasi al toplam sureye bol

Gereken Variablelar ****
ortama_hafta_icleri = [a,b,c,d]
ortalama_hafta_sonlari = [a1,b1,c1,d1]
ortalama_sure = [a+b+c+d+a1+b1+c1+d1/8]  ##haftaya ölçeklendirilmiş veya tüm stringleri böl
ziyaretci_sayi_orani = [a+b+c+d /  a1+b1+c1+d1]
yogunluk_ortalamasi = yogunluk tablosunu al hepsini bol
yogunluk_grafiği_turevi = turevi fazla olan tarihi yaz

Kullanılacak varıabler *****
Tüm_hafta_uzunlugu ="""






gunler = request1.main1_1_tarih(240, ilk_tarih , son_tarih)
print("ilki success")
gunler_ve_musteri = request1.main1_1_musteri_sayisi(240, ilk_tarih , son_tarih)
gunler_ve_sure = request1.main1_1_musteri_suresi(240, ilk_tarih , son_tarih)
hafta_sonu_degerleri = []
hafta_ici_degerleri = []
hafta_ici_ortalama = float()
hafta_sonu_ortalama = float()
gunluk_ortalama_sure =float()



def findDay(date):
    born = datetime.datetime.strptime(date, "%d/%m/%Y").weekday()
    return (calendar.day_name[born])


def gunleri_classifiye_et():
    global hafta_sonu_degerleri
    global hafta_ici_degerleri
    global gunler
    for gun in gunler:
        if (findDay(gun) == "Sunday") or (findDay(gun) == "Saturday"):
            #print(gun)
            index = gunler.index ( gun )  # sifirdan basliyor
            #print ( 'The index of e:', index )
            #print("bugun sunday")
            hafta_sonu_degerleri.append ( index )
        else:
            #print(gun)
            index = gunler.index ( gun )  # sifirdan basliyor
            #print ( 'The index of e:', index )
            hafta_ici_degerleri.append(index)

#print(hafta_ici_degerleri)
#print(hafta_sonu_degerleri)


def hafta_ici_hafta_sonu_karsilastirma():
    global hafta_sonu_ortalama
    global hafta_ici_ortalama
    sabit = float ( 0 )
    print("hafta ici ve hafta sonu ortalamasi______")
    hafta_ici_ortalama_listesi = []
    hafta_sonu_ortalama_listesi = []
    for hafta_ici_degerler in hafta_ici_degerleri:
         #print(gunler_ve_musteri[hafta_ici_degerler])
         hafta_ici_ortalama_listesi.append(gunler_ve_musteri[hafta_ici_degerler])

    hafta_ici_ortalama = cal_average(hafta_ici_ortalama_listesi)
    print(hafta_ici_ortalama)
    for hafta_sonu_degerler in hafta_sonu_degerleri:
        #print ( gunler_ve_musteri[hafta_sonu_degerler] )
        hafta_sonu_ortalama_listesi.append ( gunler_ve_musteri[hafta_sonu_degerler]  )
    hafta_sonu_ortalama = cal_average ( hafta_sonu_ortalama_listesi )
    print ( hafta_sonu_ortalama )

def hafta_ici_hafta_sonu_oran_karsilastirmasi():
    global hafta_sonu_ortalama
    global hafta_ici_ortalama
    return (hafta_sonu_ortalama / hafta_ici_ortalama)


def hafta_ici_hafta_sonu_buyukluk_karsilastirmasi():
    global hafta_sonu_ortalama
    global hafta_ici_ortalama
    if hafta_sonu_ortalama > hafta_ici_ortalama:
        return "artmaktadır."
    elif hafta_sonu_ortalama < hafta_ici_ortalama:
        return "azalmaktadır."
    elif hafta_sonu_ortalama > hafta_ici_ortalama:
        return "hafta içi ile ortalamada günlük olarak aynı kalmaktadır."


## bbunlarin hepsinni fonksiyon icine koy calistir global degerlerini koynayi unnutma




gunleri_classifiye_et()
hafta_ici_hafta_sonu_karsilastirma() #ilk calismasi gereken fonksiyon !!!!!!!!! bbu part icin
hafta_ici_hafta_sonu_musteri_orani = ("{:.2f}".format(round(hafta_ici_hafta_sonu_oran_karsilastirmasi(), 2)))
hafta_ici_hafta_sonu_buyukluk_karsilastirma = hafta_ici_hafta_sonu_buyukluk_karsilastirmasi()





















def gunluk_ortalama_sure_(): ##tum gunluk sureleri topla gunluk sure sayisina bol
    global gunluk_ortalama_sure #sundan bir emin ol
    toplam_deger = float(0)
    for gunler in gunler_ve_sure:
        toplam_deger = toplam_deger + gunler
    return toplam_deger/(len(gunler_ve_sure))

print(gunluk_ortalama_sure_())
gunluk_ortalama_sure = ("{:.2f}".format(round(gunluk_ortalama_sure_(), 2))) ##


## density

density_tarihler = []
density_ortalama = []
density_degerler = []







#2.2 için fonksiyon______________________
""" 1-) en yuksek deger ile saatlik_sure degerini eslestir
2-) saatleri sabah 10-12  oglen 13-17  aksam 17-22  degerleerine bak son deger ortalamanin uzerinde ise
artislar kismina ekle 

Gereken Variablelar ****
sabah_degerleri = [a,b,c,]
oglen_degerleri = [a1,b1,c1,d1]
aksam_degerleri = [a1,b1,c1,d1,e1]

ortalama_hafta_sonlari = [a1,b1,c1,d1]
ortalama_sure = [a+b+c+d+a1+b1+c1+d1/8]  ##haftaya ölçeklendirilmiş veya tüm stringleri böl
ziyaretci_sayi_orani = [a+b+c+d /  a1+b1+c1+d1]
yogunluk_ortalamasi = yogunluk tablosunu al hepsini bol
yogunluk_grafiği_turevi = turevi fazla olan tarihi yaz

Kullanılacak varıabler *****
Tüm_hafta_uzunlugu ="""



sabah_degerleri = True
oglen_degerleri = True
aksam_degerleri = True

musteri_artisi_degeri = f""
def musteri_artisi():
    global musteri_artisi_degeri
    if sabah_degerleri == True:
        if oglen_degerleri == True:
            if aksam_degerleri == True :
                musteri_artisi_degeri =("sabah, öğlen ve akşam")
            else:
                musteri_artisi_degeri = ("sabah ve öğlen")
        else:
            if aksam_degerleri == True :
                musteri_artisi_degeri =("sabah ve akşam")
            else:
                musteri_artisi_degeri = ("sabah")
    else:
        if oglen_degerleri == True:
            if aksam_degerleri == True :
                musteri_artisi_degeri =("öğlen ve akşam")
            else:
                musteri_artisi_degeri = ("öğlen")
        else:
            if aksam_degerleri == True :
                musteri_artisi_degeri =("akşam")
            else:
                musteri_artisi_degeri = (" error atris yoktur") ##kontrol ett





#2.3 için fonksiyon______________________

""" tum alanlari 3 li list halinde siniflandir isim, yon, yogunluk degeri, (2.5 icin gerekli)
1-) Tum alanlara bak en yogun 3 unu sec
2-) Tum alanlara bak en yogun 4 unu sec
3-) tum alanlarin yukarisi, asagisi , solu, sagi diye siniflandir grafigin 
4-) yonlerden el fazlasina sahip olanini sec

Gereken Variablelar ****
yukari_degerleri = [a,b,c,]
sol_degerleri = [a1,b1,c1,d1]
sag_degerleri = [a1,b1,c1,d1,e1]
asagi_degerleri = [a1,b1,c1,d1,e1]
en_yogun_3_lu_degerler = [a9,b9,c9]
en_az_yogun_4_lu_degerler = [a0,b0,c0,d0]"""


yogunluk_haritasi_listesi =  [["FTW","sol alt",5  ],["Recover","sol alt",9 ],["Golf","sag alt",7 ]]

isim_listesi = []
konum_listesi = []
density_listesi = []
density_listesi_sorted = []

for elements in yogunluk_haritasi_listesi:
    isim_listesi.append(elements[0])
    konum_listesi.append(elements[1])
    density_listesi.append ( elements[2] )

density_listesi_sorted = density_listesi

density_listesi_sorted.sort()
print(density_listesi)


print(isim_listesi)

#2.4 için fonksiyon______________________
""" Buna bir geerekmiyor"""


#2.5 için fonksiyon______________________
""" 1-) tum alanlari 3 li list halinde siniflandir isim, yon, yogunluk degeri, 
 
 1-) Tum alanlara bak yogunlugu 1 in altindakileri sirala
2-) Tum alanlara bak yogunlugu 1 in ustundekiler sirala
3-) tum alanlarin yukarisi, asagisi , solu, sagi diye siniflandir grafigin 
4-) yonlerden el fazlasina sahip olanini sec

Gereken Listeler ****

Gereken_list_ler = [ [elma,1.8, yukari],[elma2,1.9, asagi] ]

Gereken Variablelar ****
yogunlugu_1_in_altindakiler = []
yogunlugu_1_in_ustundekiler = []


not: alani veya alanlarini ayarla cumle sonunda duzgun dursun"""

yogunlugu_1_in_altindakiler = [1]
yogunlugu_1_in_ustundekiler = []





#2.6 için fonksiyon______________________

""" 1-) Buraya bir open CV Atilabilinir veya elle yazilabilinir 
2-) yukari yonununde, asagi yonunde, sol yonunde, sag yonunde


not: alani veya alanlarini ayarla cumle sonunda duzgun dursun"""





#2.7 için fonksiyon______________________
""" 1-) listeleri_al = 3 uncu degeri yani degisimi en fazla olani koy(degisim)
2-)listeleri_al = 7 uncu degeri yani saniye en fazla olani koy(gecirilen sure)
3-)listeleri_al = 7 uncu degeri yani 15s giren en fazla olani koy(15s giren)

boyle gotur zaten tek fonksiyon

Gereken Listeler ****

Gereken_list_ler = [ [elma,1.8, yukari],[elma2,1.9, asagi] ]

Gereken Variablelar ****
yogunlugu_1_in_altindakiler = []
yogunlugu_1_in_ustundekiler = []


Kullanılacak varıabler *****
listeleri_al =
tarih =

not: alani veya alanlarini ayarla cumle sonunda duzgun dursun"""



#2.8 için fonksiyon______________________
"""1-)Hangi günün pazartesi olduğunu bul 
2-)pazartesiden  sonra haftalara böl 4 parçada bak 5 günün ortalamasını al sonra kalan 2 günün ortalamasını al
3-)kişi sayısı 2 tanesinde fazla isi artmaktadır de 4 taneesi uzerinden
4-)ortalama süreeyi çek veye listelerin ortalamasını al ve yazdır 
5-)yukarıda yaptığun hafta içi hafta sonu değerlerini oranla 
6-)Yogunlik ortalamasi al toplam sureye bol


Kullanılacak varıabler *****
Magza_alani =
Magza_tarihi ="""



#2.9 için fonksiyon______________________




#3.1 için fonksiyon______________________



##degerlerı refreshlemek ıcın gereklı scrıpt

def refresh():
    print('refresh baslatildi')







def start_writing_on_docx(firma,magza_statik_dosya_location_ismi,magaza_id_no,ilk_tarih,son_tarih,magaza_id_yogunluk,karsilastirilacak_isim_listesi,isi_tablosu_liste):
    global global_test

    def ilk_tarih_end_son_tarih_baslangic(tarih_ilk, tarih_son):
        def numOfDays(date1, date2):
            return (date2 - date1).days

        gun1 = int ( str ( tarih_ilk )[0:2] )
        ay1 = int ( str ( tarih_ilk )[3:5] )
        yil1 = int ( str ( tarih_ilk )[6:10] )
        gun2 = int ( str ( tarih_son )[0:2] )
        ay2 = int ( str ( tarih_son )[3:5] )
        yil2 = int ( str ( tarih_son )[6:10] )
        ilk_tarih_updated = datetime.datetime ( yil1, ay1, gun1 )
        son_tarih_updated = datetime.datetime ( yil2, ay2, gun2 )
        # gun_farki = (numOfDays ( ilk_tarih_updated, son_tarih_updated ), "days")[0] + 1
        gun_farki = 4
        print ( gun_farki )
        cikarilacak_gun = (numOfDays ( ilk_tarih_updated, son_tarih_updated ), "days")[0]
        onceki_ay_ilk_tarih = ilk_tarih_updated + datetime.timedelta ( days=gun_farki )
        onceki_ay_son_tarih = son_tarih_updated - datetime.timedelta ( days=gun_farki )
        print ( "tarih_kontrolu" )
        tarih_son_baslangic = str ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
        tarih_ilk_bitis = str ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )
        print ( tarih_ilk_bitis )
        print ( tarih_son_baslangic )
        return [tarih_ilk_bitis, tarih_son_baslangic]

    tarih_1 = ilk_tarih
    tarih_4 = son_tarih
    tarig_limitleri = ilk_tarih_end_son_tarih_baslangic(tarih_1,tarih_4)
    tarih_2 = tarig_limitleri[0]
    tarih_3 = tarig_limitleri[1]


    ##starting function
    if global_test == True:
        print ( "global version" )
        BASE_DIR = os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) )
        print ( BASE_DIR )
        magza_statik_dosya_location = os.path.join ( BASE_DIR,f"bot_udentify/firms/{firma}/Statik {magza_statik_dosya_location_ismi}" )
        print ( magza_statik_dosya_location )
        dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify/firms/{firma}" )
        magaza_dosyasi_ismi = f"{dosya_yolu}/{magza_statik_dosya_location_ismi}.docx"  ##bunu sona baglayacan
    else:

        BASE_DIR = os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) )
        print ( BASE_DIR )
        magza_statik_dosya_location = os.path.join ( BASE_DIR, 'bot_udentify/demo_resimler' )
        print ( magza_statik_dosya_location )
        dosya_yolu = os.path.join ( BASE_DIR, f"bot_udentify" )
        magaza_dosyasi_ismi = (f"{dosya_yolu}/demo.docx")


    #global variabllari kullanmayi unutma
    global tarih
    global magaza_adi


    tarihi_bul(ilk_tarih,son_tarih)
    magaza_adi_(magza_statik_dosya_location_ismi)

    print(magaza_id_no) ##burayi api ya bagladigin fonksiyonlari calistirmak icin kullanacaksin
    print(ilk_tarih)  ##bunlari norma diger tarihler icin kullanacaksin
    print(son_tarih)

    ##########___________________1.1 fonksiyonnlar

    global hafta_sonu_degerleri
    global hafta_ici_degerleri
    global hafta_sonu_ortalama
    global hafta_ici_ortalama
    global gunler
    global gunler_ve_musteri
    global gunler_ve_sure
    global hafta_ici_hafta_sonu_musteri_orani
    global hafta_ici_hafta_sonu_buyukluk_karsilastirma
    global gunluk_ortalama_sure

    gunler = request1.main1_1_tarih ( magaza_id_no, ilk_tarih, son_tarih )
    # burasi asil hata
    print ( 'gunlerr___' )
    print ( gunler )
    gunler_ve_musteri = request1.main1_1_musteri_sayisi ( magaza_id_no, ilk_tarih, son_tarih )
    print ( gunler_ve_musteri )
    gunler_ve_satis_adedi = request1.main1_1_musteri_suresi ( magaza_id_no, ilk_tarih, son_tarih )
    print ( gunler_ve_satis_adedi )
    gunler_ve_satis_miktari = request1.main_2_8_satis_miktari ( magaza_id_no, ilk_tarih, son_tarih )
    gunler_ve_musteri_1_1 = request1.main_2_8_kisi_miktari ( magaza_id_no, ilk_tarih, son_tarih )
    satis_ortalama = ("{:.2f}".format ( round ( request1.cal_average ( gunler_ve_satis_miktari ), 2 ) ))

    hafta_ici_degerler_1_1, haftasonu_degerleri_1_1 = request1.gunleri_classifiye_et ( gunler )[0], \
                                                      request1.gunleri_classifiye_et ( gunler )[1]

    hafta_ici_ortalama_2_8, haftasonu_ortalama_2_8 = \
        request1.hafta_ici_hafta_sonu_ortalamalar ( hafta_ici_degerler_1_1, haftasonu_degerleri_1_1,
                                                    gunler_ve_musteri_1_1 )[0], \
        request1.hafta_ici_hafta_sonu_ortalamalar ( hafta_ici_degerler_1_1, haftasonu_degerleri_1_1,
                                                    gunler_ve_musteri_1_1 )[1]

    hafta_ici_hafta_sonu_musteri_orani = request1.hafta_ici_hafta_sonu_oran_karsilastirmasi ( hafta_ici_ortalama_2_8,
                                                                                     haftasonu_ortalama_2_8 )



    ##sayfa-2.2
    liste = request1.main_2_1_saatler ( magaza_id_no, ilk_tarih, son_tarih )
    print ( liste )
    liste1 = request1.main_2_1_kisi_sure_saatlik ( magaza_id_no, ilk_tarih, son_tarih )
    print ( liste1 )
    array = list ( zip ( liste, liste1 ) )
    print ( array )
    sabah_listesi = array[0:3]
    sabah_ortalmasi = (request1.cal_average_array ( sabah_listesi ))
    oglen_listesi = array[3:7]
    oglen_ortalmasi = (request1.cal_average_array ( oglen_listesi ))
    aksam_listesi = array[7:12]
    aksam_ortalmasi = (request1.cal_average_array ( aksam_listesi ))
    en_yogun_zaman = ( request1.sabah_ogle_aksam ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ) )
    max_saat_araligi = ( request1.max_number_array ( array ) )

    #sayfa-2.3
    liste_yogunluk_top_5 = request1.main_2_3_yogunluk_haritasi_top_5(magaza_id_yogunluk,ilk_tarih, son_tarih )
    print("lolall")
    print(liste_yogunluk_top_5)

    liste_yogunluk_bottom_5 =request1.main_2_3_yogunluk_haritasi_bottom_5 ( magaza_id_yogunluk, ilk_tarih, son_tarih )
    print ( liste_yogunluk_bottom_5 )

    # sayfa-2.5
    yogunlugu_1_in_ustundekiler = request1.main_2_5_yogunluk_haritasi_orani_top_5_orani ( magaza_id_yogunluk, ilk_tarih, son_tarih )
    print ( "top_5" )
    print ( yogunlugu_1_in_ustundekiler )
    yogunlugu_1_in_altindakiler = request1.main_2_5_yogunluk_haritasi_orani_bottom_5_orani ( magaza_id_yogunluk, ilk_tarih, son_tarih )
    print ( "bot_5" )
    print ( yogunlugu_1_in_altindakiler )

    # sayfa-2.7
    print("burada_error_olabbilir")
    elma111 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih, "Count" )
    print ( "burada_error_olabbilir1" )

    performans_tablosu_listesi = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih, "Count" )
    print ( "performans_tablosu_listesi" )
    print ( performans_tablosu_listesi )
    magaza_bolumu_id = (performans_tablosu_listesi[0][1])

    ##________

    kisi_sayisi2_7 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih, "PrevCount" )
    kisi_sayisi2_7_isim = kisi_sayisi2_7[0][0].title ()
    kisi_sayisi2_7_deger = kisi_sayisi2_7[1][5]

    gecirilen_sure_2_7 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih,
                                                                        "PrevDwell" )
    gecirilen_sure_2_7_isim = gecirilen_sure_2_7[0][0].title ()
    gecirilen_sure_2_7_deger = gecirilen_sure_2_7[1][7]

    ilgi_oranı_2_7 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih,
                                                                    "_15s_Enterance" )
    ilgi_oranı_2_7_isim = ilgi_oranı_2_7[0][0].title ()
    ilgi_oranı_2_7_deger = ilgi_oranı_2_7[1][8]

    ilgi_oranı_n2_7 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih,
                                                                     "n_15s_Enterance" )
    ilgi_oranı_n2_7_isim = ilgi_oranı_n2_7[0][0].title ()
    ilgi_oranı_n2_7_deger = ilgi_oranı_n2_7[1][8]

    en_cok_zaman_2_7 = request1.main_2_7_performans_tablosu_alansal ( magaza_id_no, ilk_tarih, son_tarih, "Dwell" )
    en_cok_zaman_2_7_isim = en_cok_zaman_2_7[0][0].title ()
    en_cok_zaman_2_7_deger = en_cok_zaman_2_7[1][6]

    # sayfa-2.7







    gunler_2_8 = request1.main_2_8_saatler_gunluk(magaza_bolumu_id, ilk_tarih, son_tarih)

    gunler_ve_musteri_2_8 = request1.main_2_8_kisi_miktari(magaza_bolumu_id, ilk_tarih, son_tarih)

    gunler_ve_sure_2_8 = request1.main_2_8_kisi_sure(magaza_bolumu_id, ilk_tarih, son_tarih)

    hafta_ici_degerler_2_8 , haftasonu_degerleri_2_8 = request1.gunleri_classifiye_et(gunler_2_8)[0],request1.gunleri_classifiye_et(gunler_2_8)[1]

    print("ilk_deneme")
    print(hafta_ici_degerler_2_8)
    print(haftasonu_degerleri_2_8)

    hafta_ici_ortalama_2_8, haftasonu_ortalama_2_8 = request1.hafta_ici_hafta_sonu_ortalamalar(hafta_ici_degerler_2_8,haftasonu_degerleri_2_8,gunler_ve_musteri_2_8)[0],request1.hafta_ici_hafta_sonu_ortalamalar(hafta_ici_degerler_2_8,haftasonu_degerleri_2_8,gunler_ve_musteri_2_8)[1]

    print(hafta_ici_ortalama_2_8)
    print(haftasonu_ortalama_2_8)

    katsayi_2_8 = request1.hafta_ici_hafta_sonu_oran_karsilastirmasi(hafta_ici_ortalama_2_8,haftasonu_ortalama_2_8)
    print(katsayi_2_8)

    artis_2_8 = request1.hafta_ici_hafta_sonu_buyukluk_karsilastirmasi(hafta_ici_ortalama_2_8,haftasonu_ortalama_2_8)

    ortalama_sure_2_8 = request1.gunluk_ortalama_sure_2_8(gunler_ve_sure_2_8)

    #### saatlik kisi sure grafigi

    saatler_listes_2_8_ = (request1.saatler_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih ))
    kisi_sure_saatlik_listes_2_8_ = (request1.toplam_kisi_sure_saatlik_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih ))

    array = list ( zip ( saatler_listes_2_8_, kisi_sure_saatlik_listes_2_8_ ) )
    artisin_oldugu_sure_2_8 = request1.max_number_array ( array )
    print ( artisin_oldugu_sure_2_8 )

    kisi_sure_saatlik_liste_2_8_ = (request1.kisi_sure_saatlik_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih ))

    saat_sure_2_8 = request1.saat_sure_saatlik_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih )

    r_degeri = (pearsonr ( kisi_sure_saatlik_liste_2_8_, saat_sure_2_8 ))

    korelasyon_degeri_2_8= float("{:.2f}".format(round(r_degeri[0], 3)))

    print("korelasyon_degeero")
    print(korelasyon_degeri_2_8)
    korelasyon_turu = request1.korelasyon_orani(korelasyon_degeri_2_8)

    #2_8 yogunluk
    yogunluk_tarihleri_2_8 = (request1.yogunluk_listesi_tarihler_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih ))
    yougunluk_miktarlari_2_8 = (request1.yogunluk_listesi_2_8_ ( magaza_bolumu_id, ilk_tarih, son_tarih ))
    array_yogunluk_2_8 = list ( zip ( yogunluk_tarihleri_2_8, yougunluk_miktarlari_2_8 ) )
    print ( array_yogunluk_2_8 )
    print ( request1.cal_average_density_arrray ( array_yogunluk_2_8 ) )
    print ( request1.bigger_than_average_arrray ( array_yogunluk_2_8 ) )
    ortalamanin_ustundeki_yogunluklar_2_8 = request1.bigger_than_average_arrray ( array_yogunluk_2_8 )
    print ( "bak____" )
    print ( ortalamanin_ustundeki_yogunluklar_2_8 )

    yogunlugu_fazla_olan_tarihler_2_8 = (request1.gunleri_classifiye_et ( ortalamanin_ustundeki_yogunluklar_2_8 ))



    hafta_ici_hafta_sonu_oranlari_2_8 = request1.hafta_ici_hafta_sonu_oranlari(yogunlugu_fazla_olan_tarihler_2_8[0],yogunlugu_fazla_olan_tarihler_2_8[1])

    print ( "deneme11111122" )
    print ( performans_tablosu_listesi )
    edinme_hunisi_yuzde = request1.main_2_8_edinme_hunisi(performans_tablosu_listesi[0][3],ilk_tarih, son_tarih) # burayı a veya b ye goree ayarlayabılıyoruz
    print("deneme1111111") # ! burayi degistirdin 4 u yukarida 3 yaprin
    print(performans_tablosu_listesi)
    print(performans_tablosu_listesi[0][3])













    document = Document()


    #Header ekleme kodu
    header = document.sections[0].header
    htable=header.add_table(1, 2, Inches(13))
    htab_cells=htable.rows[0].cells
    ht0=htab_cells[1].add_paragraph()
    kh=ht0.add_run()
    kh.add_picture(f"{magza_statik_dosya_location}/udentify.png", width=Inches(1))
    #ht1=htab_cells[1].add_paragraph('put your header text here')
    ht0.alignment = WD_ALIGN_PARAGRAPH.RIGHT

    ##syafa ekleme kodu
    def create_element(name):
        return OxmlElement(name)


    def create_attribute(element, name, value):
        element.set(ns.qn(name), value)


    def add_page_number(paragraph):
        paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT

        page_run = paragraph.add_run()
        t1 = create_element('w:t')
        create_attribute(t1, 'xml:space', 'preserve')
        t1.text = 'Sayfa '
        page_run._r.append(t1)

        page_num_run = paragraph.add_run()

        fldChar1 = create_element('w:fldChar')
        create_attribute(fldChar1, 'w:fldCharType', 'begin')

        instrText = create_element('w:instrText')
        create_attribute(instrText, 'xml:space', 'preserve')
        instrText.text = "PAGE"

        fldChar2 = create_element('w:fldChar')
        create_attribute(fldChar2, 'w:fldCharType', 'end')

        page_num_run._r.append(fldChar1)
        page_num_run._r.append(instrText)
        page_num_run._r.append(fldChar2)

        of_run = paragraph.add_run()
        t2 = create_element('w:t')
        create_attribute(t2, 'xml:space', 'preserve')
        t2.text = ' / '
        of_run._r.append(t2)

        fldChar3 = create_element('w:fldChar')
        create_attribute(fldChar3, 'w:fldCharType', 'begin')

        instrText2 = create_element('w:instrText')
        create_attribute(instrText2, 'xml:space', 'preserve')
        instrText2.text = "NUMPAGES"

        fldChar4 = create_element('w:fldChar')
        create_attribute(fldChar4, 'w:fldCharType', 'end')

        num_pages_run = paragraph.add_run()
        num_pages_run._r.append(fldChar3)
        num_pages_run._r.append(instrText2)
        num_pages_run._r.append(fldChar4)

    add_page_number(document.sections[0].footer.paragraphs[0])


    #sayfe-giris


    p = document.add_paragraph(f"")
    p = document.add_paragraph(f"")
    p = document.add_paragraph(f"")
    p = document.add_paragraph(f"")
    p = document.add_paragraph(f"")
    p = document.add_paragraph(f"")



    ##docx_svg._SvgParser.monkey ()



    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/{firma}_logo.png"), width=Inches(2.5) , height=Inches(2.5))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"")
    p.add_run(f"({magaza_adi.title()})").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER



    #sayfa-icindekiler_____________________________

    document.add_page_break()

    document.add_heading("İçindekiler", level=0)

    p = document.add_paragraph(f"")
    p.add_run(f"1.0 Giriş").bold = True
    p = document.add_paragraph(f"       1.1 Raporun Amacı")

    p = document.add_paragraph(f"")
    p.add_run(f"2.0 Undentify Performans Raporu").bold = True
    p = document.add_paragraph(f"       2.1 Satış Tutarı")
    p = document.add_paragraph(f"       2.2 Kasadaki Müşteri Sayısı & Geçirilen süre")
    p = document.add_paragraph(f"       2.3 Isı Haritası")
    p = document.add_paragraph(f"       2.4 Yoğunluk, Temas ve Süre Değişimi")

    p = document.add_paragraph ( f"" )
    p.add_run ( f"3.0 Kategori Karşılaştırması" ).bold = True
    p = document.add_paragraph ( f"       3.1 Kategoriler" )
    p = document.add_paragraph(f"")

    p.add_run(f"4.0 Sonuç").bold = True
    p = document.add_paragraph(f"       4.1 Analizin sonucu")



    #sayfa-1.1_____________________________________________________

    document.add_page_break()
    document.add_heading('1.0 Giriş', 0)

    document.add_heading('1.1 Raporun Amacı', level=1)

    baslik_adlari = f"günlük kişi süre grafiği, saatlik kişi süre grafiği, yoğunluk haritası, mağaza içi yoğunluk dağılımı, metre kare başına düşen yoğunluk haritası, ısı haritası ,performans kıyaslaması, {performans_tablosu_listesi[0][0].title()}, kategori karşılaştırması"

    p = document.add_paragraph(f'Bu raporun amacı {magaza_adi} ({tarih_1}-{tarih_4}) tarih aralığındaki mağazanın genel performansı, yoğunluk haritası, kategorilerin performans değişimi, seçili kategorilerin performans analizi üzerinde yapılan analizler sonucu elde edilen bilgileri özet halinde sağlamaktır')

    p = document.add_paragraph (
        f'' )
    p = document.add_paragraph (
        f'Detaylı bilgi için app.udentify.co/ sitesini ziyaret edebilirsiniz.' )

    #magzalarinin



    #sayfa-2.1_____________________________________________________

    document.add_page_break()
    document.add_heading('2.0 Mağaza Özeti', 0)
    document.add_paragraph (
        f'Hafta sonu gerçekleşen sokağa çıkma yasağı nedeniyle ({tarih_1}-{tarih_2}) ve ({tarih_3}-{tarih_4}) tarihleri kendi aralarında karşılaştırılmıştır.'
    )
    document.add_heading ( '2.1 Satış Tutarı', level=1 )

    gunler_ve_satis_miktari = request1.main_2_8_satis_miktari ( magaza_id_no, tarih_1, tarih_2 )
    satis_ortalama_1 = ("{:.2f}".format (  request1.cal_total ( gunler_ve_satis_miktari ) ))

    gunler_ve_satis_miktari = request1.main_2_8_satis_miktari ( magaza_id_no, tarih_3, tarih_4 )
    satis_ortalama_2 = ("{:.2f}".format ( request1.cal_total ( gunler_ve_satis_miktari ) ))

    try:
        degisim_miktari = ("{:.2f}".format ( 100 - ( float(satis_ortalama_1 )/float(satis_ortalama_2 ) *100) ))
    except:
        degisim_miktari = 0


    gunler_ve_satis_miktari = request1.main_2_8_satis_miktari ( magaza_id_no, tarih_1, tarih_4 )
    try:
        satis_ortalama_3 = ("{:.2f}".format (  request1.cal_average_bosluklu_data ( gunler_ve_satis_miktari ) ))
    except:
        satis_ortalama_3 = 0

    p = document.add_paragraph (
        f"({tarih_1}-{tarih_2}) tarihli süreçte toplam satış tutarı ({satis_ortalama_1} TL) bir önceki hafta olan({tarih_3}-{tarih_4}) tarihli satış tutarına ({satis_ortalama_2} TL) göre %{degisim_miktari} fark ortaya çıkmıştır. Mağaza içi ortalama satış tutarı bir kategori için {satis_ortalama_3} TL’dir."
    )
    p = document.add_paragraph (
        f""
    )
    p = document.add_paragraph (
        f"Toplam satış tutarına göre büyükten küçüğe kategoriler aşağıdaki tabloda gösterilmiştir."
    )

    document.add_paragraph (
        f'Kategori incelendiğinde ‘ACC.’ kategorisi hariç her kategoride temas açısından bir önceki haftaya göre artış yaşanmıştır',
        style='List Bullet'
    )
    document.add_paragraph (
        f'Genel satış tutarı tablosuna bakıldığında ise 9 kategoride bir önceki haftaya göre artış yaşanmışken 10 kategoride düşüş gözlemlenmiştir.',
        style='List Bullet'
    )
    document.add_paragraph (
        f'‘ACC’ kategorisinde yoğunluk, süre, temas ve satış tutarında düşüş gözlemlenmiştir. Mağaza müdürü ile iletişim halinde olunmalıdır.',
        style='List Bullet'
    )

    document.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/performans_tablosu_fiyat_buyukten.png" ),
        width=Inches ( 6 ), height=Inches ( 2.72 )
    )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph ( f"(Büyükten Küçüğe Satış Tutarı Tablosu)" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph (
        f"Toplam satış tutarı değişimine göre son 10 kategori aşağıdaki tabloda gösterilmiştir."
    )

    document.add_paragraph (
        f"Aşağıdaki tabloda yer alan ‘ACC.’ ve WOMEN' S RECOVERY - CHARGED COTTON kategorilerinde satış düşüşüne ek olarak aynı zamanda yoğunluk, temas ve süre düşüşü de yaşandığı gözlemlenmiştir. Nedenleri ve çözümleri için mağaza müdürü ile iletişim halinde olunmalıdır.",
        style='List Bullet'
    )

    document.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/performans_tablosu_fiyat_kucukten.png" ),
        width=Inches ( 6 ), height=Inches ( 2.72 )
    )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph ( f"(Küçükten Büyüğe Satış Tutarı Tablosu)" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_page_break ()
    document.add_heading ( '2.2 Kasadaki Müşteri Sayısı & Geçirilen süre', level=1 )

    data = request1.main_2_8_kisi_miktari ( magaza_id_no, ilk_tarih, son_tarih )
    toplam_kisi_sayisi = request1.cal_total(data)
    document.add_paragraph (
        f' ({tarih_1}-{tarih_4}) tarih aralığında kasa alanına uğrayan toplam ziyaretçi sayısı {toplam_kisi_sayisi}’dir. Kasa alanında 15 saniye, 180 saniye vakit geçiren ziyaretçiler aşağıdaki tabloda gösterilmiştir.'
    )
    document.add_heading ( 'Vakit Tablosu', 0 )

    # Table data in a form of list
    # data = [
    #     [1, 'Geek 1',"ahha","lolo","ortalama"],
    #     [2, 'Geek 2',"ahha","lolo","ortalama"],
    #     [3, 'Geek 3',"ahha","lolo","ortalama"],
    #     [3, 'Geek 3',"ahha","lolo","ortalama"],
    #     [3, 'Geek 3',"ahha","lolo","ortalama"]
    # ]
    data = request1.store_sure_2_2 ( magaza_id_no, ilk_tarih, son_tarih )

    # Creating a table object
    table = document.add_table ( rows=1, cols=5 )
    table.style = 'TableGrid'
    # Adding heading in the 1st row of the table
    row = table.rows[0].cells
    row[0].text = 'Tarih'
    row[1].text = '15 sn aşan kişi'
    row[2].text = '15 sn üzeri geçiren ortalama süre'
    row[3].text = '180 sn yi aşan kişi'
    row[4].text = 'Ortalama bekleme süresi(sn)'

    # Adding data from the list to the table
    for a, b, c, d, e in data:
        # Adding a row and then adding data in it.
        row = table.add_row ().cells
        # Converting id to string as table can only take string input
        row[0].text = str ( a )
        row[1].text = b
        row[2].text = c
        row[3].text = d
        row[4].text = e

    p = document.add_paragraph ( f"" )

    document.add_paragraph (
        f'Kasada bekleme süresi arttıkça müşterinin ürünü almama ihtimali artmaktadır, bu nedenle 180 saniye üzeri bekleme yapan müşteri sayısı ile fiş sayısı kıyaslandığında kaç kişilik kayıp olduğu anlaşılır ve mağaza sepet ortalamasına bakılarak satış kaybı miktarı belirlenebilir.'
    )

    document.add_paragraph ( f"Kasada bekleme süresi arttıkça müşterinin ürünü almama ihtimali artmaktadır, bu nedenle 120 saniye üzeri bekleme yapan müşteri sayısı ile fiş sayısı kıyaslandığında kaç kişilik kayıp olduğu anlaşılır ve mağaza sepet ortalamasına bakılarak satış kaybı miktarı belirlenebilir." )


    liste1 = request1.giren_kisi_sayisi_hepsi ( magaza_id_no, ilk_tarih, son_tarih )
    print ( liste1 )

    liste_saat = liste1[0]["Serial"]
    print ( liste_saat )
    for element in range ( 0, len ( liste_saat ) ):
        liste_saat[element] = str ( liste_saat[element] )[-5:]

    liste_kisi = liste1[1]["Serial"]
    print ( liste_kisi )

    plt.figure ()
    # x axis values
    x = liste_saat
    # corresponding y axis values
    y = liste_kisi
    # plotting the points
    plt.plot ( x, y )  # ,color='red', lw=2
    # plt.fill_between(x,y, 0, alpha=0.30)
    # naming the x axis
    # naming the y axis

    # giving a title to my graph
    # plt.title ( 'My first graph!' )
    plt.gca ().axes.get_yaxis ().set_visible ( False )
    # function to show the plot
    buf = io.BytesIO ()
    plt.savefig ( buf, format='png' )
    buf.seek ( 0 )
    # im = Image.open ( buf )
    document.add_picture ( buf, width=Inches ( 4.5 ),
                           height=Inches ( 3.37 ) )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph ( f"(Kasa Saatlik Yoğunluk)" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # im.show ()
    #
    buf.close ()

    plt.figure ()

    liste_ikinci = request1.store_sure_2_2_saatlik ( magaza_id_no, ilk_tarih, son_tarih )
    saatlik_liste = liste_ikinci[1]["Serial"]
    sure_liste = liste_ikinci[2]["Serial"]
    x = saatlik_liste
    # corresponding y axis values
    y = sure_liste
    print ( " x y " )
    print ( x )
    print ( y )
    plt.plot ( x, y )  # ,color='red', lw=2
    plt.fill_between ( x, y, 0, alpha=0.30 )
    # naming the x axis

    # naming the y axis

    # # giving a title to my graph
    # #plt.title ( 'My first graph!' )
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.gca().axes.get_xaxis().set_visible(False)
    # # function to show the plot
    # elma = plt.show ()
    # print(plt)
    # figure = io.BytesIO(elma)
    # print(figure)
    buf = io.BytesIO ()
    plt.savefig ( buf, format='png' )
    buf.seek ( 0 )
    # im = Image.open(buf)
    # im.show()
    document.add_picture ( buf, width=Inches ( 4.5 ),
                           height=Inches ( 3.37 ) )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph ( f"(Kasa Saatlik Giren Temas)" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    buf.close ()


    p = document.add_paragraph ( f"Kasa alanının saatlik yoğunluğu ve giren temas sayısı incelendiğinde saat 15-16 ve 17-18 aralıklarında temasta ve yoğunlukta en yüksek değerlere ulaşılmıştır. Saat 16-17 aralığından itibaren temas düşme eğilimine girmişken yoğunluk aynı seviyede azalmamıştır. Yoğunluğun nedeni süredir. Bu nedenle, bekleme süresini azaltmak ve müşteri memnuniyetini en üst seviyede tutabilmek için belirtilen saat aralıklarında kasaya personel eklenmelidir." )





    # yogunluk_temas_sure
    document.add_page_break ()
    document.add_heading ( '2.3 Isı Haritası', level=1 )

    p = document.add_paragraph ( f"Kırmızı: Çok yoğun Sarı: Orta yoğun Yeşil: Az yoğun" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_paragraph (
        'Isı haritaları incelendiğinde, mağaza içerisinde yoğunluğu daha az ve daha fazla olan alanlar görülmektedir.',
        style='List Bullet'
    )











    # ['Ana Giriş', 'Cam 7', 'Cam 8', 'Run', 'Youth', 'Giriş', 'Train', 'Train Ön']
    def isi_haritalarini_yarat(sayi, kamera_adi_isimi, table):
        sifirdan_baslat = sayi - 1
        if sifirdan_baslat % 2 == 0:
            ikincisi = 0
        else:
            ikincisi = 1
        birincisi = (round ( (sifirdan_baslat + 1.01) / 2 ) - 1)  # math.ceil kullanmamak icin 0.51 yaptim
        print ( "birincisi_bak" )
        print ( birincisi )
        print ( ikincisi )
        row_cells1 = table.cell ( birincisi, ikincisi )
        paragraph = row_cells1.paragraphs[0]
        run = paragraph.add_run ()
        run.add_picture ( f'{magza_statik_dosya_location}/isi_haritasi{sayi}.png', width=Inches ( 2.66 ),
                          height=Inches ( 2.24 ) )  ### 2.25 1.9 normalde

        # last_paragraph = paragraph.paragraphs[-1]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

        # document.add_picture(os.path.join(BASE_DIR, f'{magza_statik_dosya_location}/isi_haritasi{sayi}.png'), width=Inches(2.25) , height=Inches(1.9))
        # last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
        # last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        # document.add_paragraph (
        #     f"{kamera_adi_isimi} kamerasının....",
        #     style='List Bullet'
        # )

    tablo_satir_sayisi = (
                math.ceil ( (len ( isi_tablosu_liste ) + 1.001) / 2 ) - 1)  # math.ceil kullanmamak icin 0.51 yaptim




    table = document.add_table ( rows=tablo_satir_sayisi, cols=2 )
    # table.columns[0].width = Inches ( 5 )
    # table.rows[0].cells[0].height = Inches ( 5 )
    for row in table.rows:
        row.height = Inches ( 2.25 )
        row.width = Inches ( 1.9 )
    table.style = 'TableGrid'

    sayi = 1
    for kamera in isi_tablosu_liste:
        isi_haritalarini_yarat( sayi, kamera, table )
        sayi += 1


    document.add_page_break ()
    document.add_heading ( '2.4 Yoğunluk, Temas ve Süre Değişimi', level=1 )

    # Trendler_birinci_kisim
    document.add_paragraph (
        f'({tarih_1}-{tarih_4}) tarih aralığında mağaza yoğunluk, temas ve süre oranı metriklerine göre incelenmiştir. En yüksek ve en düşük orana sahip 5 kategori belirtilen metriklere göre aşağıdaki tabloda gösterilmiştir. Referans noktası belirtilen tarih olmak üzere hafta içi, hafta sonu ve bir önceki hafta değerli ile karşılaştırılmıştır. Yoğunluk, temas ve süre oran verileri belirtildikten sonra bölüm sonunda analiz kısmı yer almaktadır.'
    )

    # trendler yogunluk
    p = document.add_paragraph ( f"" )
    p.add_run ( f"A. Yoğunluk" ).bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    magaza_ici_oran = request1.main_2_7_performans_tablosu_hesapla(magaza_id_no,tarih_1,tarih_2,tarih_3,tarih_4,"Density")

    document.add_paragraph (
        f'Mağaza içi ortalama yoğunluk oranı bir kategori için %{magaza_ici_oran} olarak ortaya çıkmıştır.'
    )

    table = document.add_table ( rows=1, cols=2 )
    # table.columns[0].width = Inches ( 5 )
    # table.rows[0].cells[0].height = Inches ( 5 )
    for row in table.rows:
        row.height = Inches ( 2.25 )
        row.width = Inches ( 1.9 )

    row_cells1 = table.cell ( 0, 0 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_yogunluk0_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    row_cells1 = table.cell ( 0, 1 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_yogunluk1_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    #degistirilecek
    liste_yogunluk_top_5_ilk_hafta = request1.main_2_3_yogunluk_haritasi_top_5 ( magaza_id_yogunluk, tarih_1, tarih_2 )
    liste_yogunluk_top_5_ikinci_hafta = request1.main_2_3_yogunluk_haritasi_top_5 ( magaza_id_yogunluk, tarih_3, tarih_4 )
    print ( "lolall_basladik_____" )
    print ( liste_yogunluk_top_5_ilk_hafta )
    print(liste_yogunluk_top_5_ikinci_hafta)

    ilk_5_de_yenini_koruyanlar = request1.cakisan_liste_elemanlar(liste_yogunluk_top_5_ilk_hafta,liste_yogunluk_top_5_ikinci_hafta)






    liste_yogunluk_bottom_5 = request1.main_2_3_yogunluk_haritasi_bottom_5 ( magaza_id_yogunluk, tarih_1, tarih_2 )
    print ( liste_yogunluk_bottom_5 )

    # sayfa-2.5
    yogunlugu_1_in_ustundekiler = request1.main_2_5_yogunluk_haritasi_orani_top_5_orani ( magaza_id_yogunluk, tarih_1, tarih_2 )
    print ( "top_5" )
    print ( yogunlugu_1_in_ustundekiler )
    yogunlugu_1_in_altindakiler = request1.main_2_5_yogunluk_haritasi_orani_bottom_5_orani ( magaza_id_yogunluk,
                                                                                             tarih_1, tarih_2 )
    print ( "bot_5" )
    print ( yogunlugu_1_in_altindakiler )


    # onemlı unutma
    # document.add_paragraph (
    #     f'Yukarıdaki yoğunluk haritası incelendiğinde, mağazanın en yoğun alanlarının {liste_yogunluk_top_5[0].title ()}, {liste_yogunluk_top_5[1].title ()} ve {liste_yogunluk_top_5[2].title ()} alanları olduğu görülür.',
    #     style='List Bullet'
    # )
    #
    # document.add_paragraph (
    #     f'Yoğunluğun en az olduğu alanlar ise; {liste_yogunluk_bottom_5[0].title ()}, {liste_yogunluk_bottom_5[1].title ()}, {liste_yogunluk_bottom_5[2].title ()}, {liste_yogunluk_bottom_5[3].title ()}, ve {liste_yogunluk_bottom_5[4].title ()} alanlarıdır.',
    #     style='List Bullet'
    # )

    birlesik_liste = (
        request1.json_id_den_degisim_oranina ( tarih_1, tarih_2, tarih_3, tarih_4, magaza_id_yogunluk, "DensityRatio",
                                      reverse=True ))

    print ( birlesik_liste )

    sorted_list = (request1.BubleSort ( birlesik_liste ))
    negatif_liste = request1.negatifse ( sorted_list )
    pozitif_liste = request1.pozitifse ( sorted_list )
    print ( negatif_liste )
    print ( pozitif_liste )
    isimler_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[1] )
    print ( isimler_listesi_negatif )
    oranlari_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[2] )
    print ( oranlari_listesi_negatif )
    isimler_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[1] )
    print ( isimler_listesi_pozitif )
    oranlari_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[2] )
    print ( oranlari_listesi_pozitif )

    document.add_paragraph (
        f"({tarih_3}-{tarih_4}) bir önceki hafta içi olan ({tarih_1}-{tarih_2}) tarih aralığıyla karşılaştırıldığında {isimler_listesi_negatif} kategorilerinde sırasıyla yoğunluk değişiminde {oranlari_listesi_negatif} oranlarında düşüş gözlemlenirken {isimler_listesi_pozitif} kategorilerinde ise sırasıyla {oranlari_listesi_pozitif} oranlarında bir artış mevcuttur."
    )

    ilk_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_1, tarih_2, magaza_id_yogunluk, "DwellRatio", True ))
    ikinci_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_3, tarih_4, magaza_id_yogunluk, "DwellRatio", True ))
    print ( ilk_hafta_top_5 )
    print ( ikinci_hafta_top_5 )
    eslesen_isimler_listesi = (request1.cakisan_liste_elemanlar_ilk_3 ( ilk_hafta_top_5[1], ikinci_hafta_top_5[1] ))
    print ( eslesen_isimler_listesi )
    eslesen_isimler_listesi_str = request1.list_to_string_ve_ile ( eslesen_isimler_listesi )
    ek_kelime = "kategorileri"
    if eslesen_isimler_listesi ==0:
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} kategori belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumamıştır."
        )
    elif len(eslesen_isimler_listesi)>1:
        ek_kelime = "kategorileri"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )
    else:
        ek_kelime = "kategorisi"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )


    # Trendler_Temas
    document.add_page_break ()
    p = document.add_paragraph ( f"" )
    p.add_run ( f"A. Temas" ).bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    magaza_ici_oran = request1.main_2_7_performans_tablosu_hesapla ( magaza_id_no, tarih_1, tarih_2, tarih_3, tarih_4,
                                                                     "Count" )

    document.add_paragraph (
        f'Mağaza içi ortalama temas sayısı bir kategori için {magaza_ici_oran} olarak ortaya çıkmıştır.'
    )

    table = document.add_table ( rows=1, cols=2 )
    # table.columns[0].width = Inches ( 5 )
    # table.rows[0].cells[0].height = Inches ( 5 )
    for row in table.rows:
        row.height = Inches ( 2.25 )
        row.width = Inches ( 1.9 )

    row_cells1 = table.cell ( 0, 0 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_kisi0_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    row_cells1 = table.cell ( 0, 1 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_kisi1_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    birlesik_liste = (
        request1.json_id_den_degisim_oranina ( tarih_1, tarih_2, tarih_3, tarih_4, magaza_id_yogunluk, "CountRatio",
                                               reverse=True ))

    print ( birlesik_liste )

    sorted_list = (request1.BubleSort ( birlesik_liste ))
    negatif_liste = request1.negatifse ( sorted_list )
    pozitif_liste = request1.pozitifse ( sorted_list )
    print ( negatif_liste )
    print ( pozitif_liste )
    isimler_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[1] )
    print ( isimler_listesi_negatif )
    oranlari_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[2] )
    print ( oranlari_listesi_negatif )
    isimler_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[1] )
    print ( isimler_listesi_pozitif )
    oranlari_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[2] )
    print ( oranlari_listesi_pozitif )

    document.add_paragraph (
        f"({tarih_3}-{tarih_4}) bir önceki hafta içi olan ({tarih_1}-{tarih_2}) tarih aralığıyla karşılaştırıldığında {isimler_listesi_negatif} kategorilerinde sırasıyla yoğunluk değişiminde {oranlari_listesi_negatif} oranlarında düşüş gözlemlenirken {isimler_listesi_pozitif} kategorilerinde ise sırasıyla {oranlari_listesi_pozitif} oranlarında bir artış mevcuttur."
    )
    ilk_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_1, tarih_2, magaza_id_yogunluk, "CountRatio", True ))
    ikinci_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_3, tarih_4, magaza_id_yogunluk, "CountRatio", True ))
    print ( ilk_hafta_top_5 )
    print ( ikinci_hafta_top_5 )
    eslesen_isimler_listesi = (request1.cakisan_liste_elemanlar_ilk_3 ( ilk_hafta_top_5[1], ikinci_hafta_top_5[1] ))
    print ( eslesen_isimler_listesi )
    eslesen_isimler_listesi_str = request1.list_to_string_ve_ile ( eslesen_isimler_listesi )
    ek_kelime = "kategorileri"
    if eslesen_isimler_listesi == 0:
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} kategori belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumamıştır."
        )
    elif len ( eslesen_isimler_listesi ) > 1:
        ek_kelime = "kategorileri"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )
    else:
        ek_kelime = "kategorisi"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )

    # Trendler_Sure

    document.add_page_break ()
    p = document.add_paragraph ( f"" )
    p.add_run ( f"A. Süre" ).bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    magaza_ici_oran = request1.main_2_7_performans_tablosu_hesapla(magaza_id_no,tarih_1,tarih_2,tarih_3,tarih_4,"Dwell")

    document.add_paragraph (
        f'Mağaza içi ortalama süre bir kategori için {magaza_ici_oran} olarak ortaya çıkmıştır.'
    )

    table = document.add_table ( rows=1, cols=2 )
    # table.columns[0].width = Inches ( 5 )
    # table.rows[0].cells[0].height = Inches ( 5 )
    for row in table.rows:
        row.height = Inches ( 2.25 )
        row.width = Inches ( 1.9 )

    row_cells1 = table.cell ( 0, 0 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_sure0_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    row_cells1 = table.cell ( 0, 1 )
    paragraph = row_cells1.paragraphs[0]
    run = paragraph.add_run ()
    run.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/_sure1_yogunluk_haritasi_birincisi.png" ),
        width=Inches ( 2.2 ), height=Inches ( 4.25 ) )
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    birlesik_liste = (
        request1.json_id_den_degisim_oranina ( tarih_1, tarih_2, tarih_3, tarih_4, magaza_id_yogunluk, "DwellRatio",
                                               reverse=True ))

    print ( birlesik_liste )

    sorted_list = (request1.BubleSort ( birlesik_liste ))
    negatif_liste = request1.negatifse ( sorted_list )
    pozitif_liste = request1.pozitifse ( sorted_list )
    print ( negatif_liste )
    print ( pozitif_liste )
    isimler_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[1] )
    print ( isimler_listesi_negatif )
    oranlari_listesi_negatif = request1.list_to_string_ve_ile ( negatif_liste[2] )
    print ( oranlari_listesi_negatif )
    isimler_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[1] )
    print ( isimler_listesi_pozitif )
    oranlari_listesi_pozitif = request1.list_to_string_ve_ile ( pozitif_liste[2] )
    print ( oranlari_listesi_pozitif )

    document.add_paragraph (
        f"({tarih_3}-{tarih_4}) bir önceki hafta içi olan ({tarih_1}-{tarih_2}) tarih aralığıyla karşılaştırıldığında {isimler_listesi_negatif} kategorilerinde sırasıyla yoğunluk değişiminde {oranlari_listesi_negatif} oranlarında düşüş gözlemlenirken {isimler_listesi_pozitif} kategorilerinde ise sırasıyla {oranlari_listesi_pozitif} oranlarında bir artış mevcuttur."
    )
    ilk_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_1, tarih_2, magaza_id_yogunluk, "DwellRatio", True ))
    ikinci_hafta_top_5 = (request1.json_isimden_listeye_5 ( tarih_3, tarih_4, magaza_id_yogunluk, "DwellRatio", True ))
    print ( ilk_hafta_top_5 )
    print ( ikinci_hafta_top_5 )
    eslesen_isimler_listesi = (request1.cakisan_liste_elemanlar_ilk_3 ( ilk_hafta_top_5[1], ikinci_hafta_top_5[1] ))
    print ( eslesen_isimler_listesi )
    eslesen_isimler_listesi_str = request1.list_to_string_ve_ile ( eslesen_isimler_listesi )
    ek_kelime = "kategorileri"
    if eslesen_isimler_listesi == 0:
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} kategori belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumamıştır."
        )
    elif len ( eslesen_isimler_listesi ) > 1:
        ek_kelime = "kategorileri"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )
    else:
        ek_kelime = "kategorisi"
        print ( eslesen_isimler_listesi_str )
        document.add_paragraph (
            f"{eslesen_isimler_listesi_str} {ek_kelime} belirtilen tüm tarih aralıklarında yoğunluk oranı açısından ilk üç sıradaki yerlerini korumuştur."
        )

    document.add_page_break ()
    document.add_heading ( '2.5 Trendler', level=1 )

    # Trendler_birinci_kisim
    document.add_paragraph (
        'Trendler bölümünde süreklilik gösteren kategori ve alanlar incelenmiştir. Günlük, haftalık ve aylık olarak veriler incelenebilir. Bu bilgiler Trendler paneli aracılığıyla hem grafik modunda hem de harita modunda incelenebilirken aynı zamanda Excel dosyası şeklinde indirerek tablo halinde de incelenebilir.'
    )

    p = document.add_paragraph ( f"" )
    p.add_run ( f"A. Yoğunluk" ).bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    document.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/trends_density_haftalik.png" ),
        width=Inches ( 1.5 ), height=Inches ( 4.35 ) )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph (
        f"3 Haftadır Yoğunluğu Artan Kategoriler: ‘MEN'S RUN’, ‘MAN' S UNSTOPPABLE’, ‘MAN' S THE ROCK’, ‘MEN' S VANISH & RUSH’, ‘MEN' S RECOVERY’, ‘BASKETBALL’, ‘MEN'S RIVAL FLEECE PLUS’, ‘APOLLO’, ‘WOMEN'S RIVAL FLEECE’, ‘WOMEN' S THE ROCK’, ‘WOMEN' S ARMOUR HG’" )
    p = document.add_paragraph (
        f"2 Haftadır Yoğunluğu Azalan Kategoriler: ‘WOMEN' S VANISH & RUSH’, ‘WOMEN' S UNSTOPPABLE’, ‘WOMEN' S RECOVERY - CHARGED COTTON’" )

    # Trendler_ikinci_kisim
    document.add_page_break ()

    p = document.add_paragraph ( f"" )
    p.add_run ( f"B. İlgi" ).bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT

    document.add_picture (
        os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/trends_interest_haftalik.png" ),
        width=Inches ( 1.5 ), height=Inches ( 4.35 ) )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    p = document.add_paragraph (
        f"3 Haftadır Yoğunluğu Artan Kategoriler: ‘MEN'S RUN’, ‘MAN' S UNSTOPPABLE’, ‘MAN' S THE ROCK’, ‘MEN' S VANISH & RUSH’, ‘MEN' S RECOVERY’, ‘BASKETBALL’, ‘MEN'S RIVAL FLEECE PLUS’, ‘APOLLO’, ‘WOMEN'S RIVAL FLEECE’, ‘WOMEN' S THE ROCK’, ‘WOMEN' S ARMOUR HG’" )
    p = document.add_paragraph (
        f"2 Haftadır Yoğunluğu Azalan Kategoriler: ‘WOMEN' S VANISH & RUSH’, ‘WOMEN' S UNSTOPPABLE’, ‘WOMEN' S RECOVERY - CHARGED COTTON’" )

    # document.add_picture('monty-truth.png', width=Inches(1.25))
    document.add_page_break ()
    document.add_heading ( '4.0 Kategori Karşılaştırması', 0 )
    document.add_heading ( '3.1 Kategoriler', level=1 )

    def populate_karsilastirma(kategori_karsilasmasi_1, kategori_karsilasmasi_2, magaza_id_no, siralamasi,
                               ikiser_siralamasi):

        p = document.add_paragraph ( f"" )
        p.add_run ( f"{kategori_karsilasmasi_1} & {kategori_karsilasmasi_2}" ).bold = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        kategori_1 = request1.main_2_7_performans_tablosu_double_isim ( magaza_id_no, ilk_tarih, son_tarih,
                                                                        kategori_karsilasmasi_1 )
        kategori_2 = request1.main_2_7_performans_tablosu_double_isim ( magaza_id_no, ilk_tarih, son_tarih,
                                                                        kategori_karsilasmasi_2 )

        kategori_1_magaza_ici_yogunluk = kategori_1[1][0]
        kategori_1_magaza_ici_m2_orani = kategori_1[1][11]
        kategori_2_magaza_ici_yogunluk = kategori_2[1][0]
        kategori_2_magaza_ici_m2_orani = kategori_2[1][11]

        def yogunlu_b_m2_karsilastirma(kategori_1_magaza_ici_yogunluk, kategori_1_magaza_ici_m2_orani,
                                       kategori_2_magaza_ici_yogunluk, kategori_2_magaza_ici_m2_orani):

            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) and float (
                    kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 1:
                return f'Metre kare başına düşen yoğunluklar incelendiğinde, {kategori_karsilasmasi_1.title ()} alanının metre kare başına düşen yoğunluğu, {kategori_karsilasmasi_2.title ()}’dan daha büyüktür ve bu oran 1’in üzerindedir.'
            elif float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) <= float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) and float (
                kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 1:
                return f'Metre kare başına düşen yoğunluklar incelendiğinde, {kategori_karsilasmasi_2.title ()} alanının metre kare başına düşen yoğunluğu, {kategori_karsilasmasi_1.title ()}’dan daha büyüktür ve bu oran 1’in üzerindedir.'
            elif float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) and float (
                    kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) <= 1:
                return f'Metre kare başına düşen yoğunluklar incelendiğinde, {kategori_karsilasmasi_1.title ()} alanının metre kare başına düşen yoğunluğu, {kategori_karsilasmasi_2.title ()}’dan daha büyüktür ve fakat oranlar 1’in altındadır.'
            elif float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) <= float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) and float (
                kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) <= 1:
                return f'Metre kare başına düşen yoğunluklar incelendiğinde, {kategori_karsilasmasi_2.title ()} alanının metre kare başına düşen yoğunluğu, {kategori_karsilasmasi_1.title ()}’dan daha büyüktür ve fakat oranlar 1’in altındadır.'

        print ( "errorlere_bakkk" )
        print ( kategori_1 )
        print ( kategori_2 )
        print ( kategori_1_magaza_ici_yogunluk )
        print ( kategori_1_magaza_ici_m2_orani )
        print ( kategori_2_magaza_ici_yogunluk )
        print ( kategori_2_magaza_ici_m2_orani )
        yogunlu_b_m2_karsilastirma_yazi = yogunlu_b_m2_karsilastirma ( kategori_1_magaza_ici_yogunluk,
                                                                       kategori_1_magaza_ici_m2_orani,
                                                                       kategori_2_magaza_ici_yogunluk,
                                                                       kategori_2_magaza_ici_m2_orani )

        def yogunlu_b_m2_verim_karsilastirma(kategori_1_magaza_ici_yogunluk, kategori_1_magaza_ici_m2_orani,
                                             kategori_2_magaza_ici_yogunluk, kategori_2_magaza_ici_m2_orani):

            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 1 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 1:
                return f'Birim metrekareye düşen yoğunluğa bakıldığında {kategori_karsilasmasi_1.title ()} ve {kategori_karsilasmasi_2.title ()} alanı verimli kullanılmıştır, verimleri sırasıyla 1 birim metre kareye {("{:.2f}".format ( round ( float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ), 2 ) ))} ve {("{:.2f}".format ( round ( float ( kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ), 2 ) ))} olarak ortaya çıkmıştır.'
            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 1 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 0:
                return f'Birim metrekareye düşen yoğunluğa bakıldığında {kategori_karsilasmasi_1.title ()} verimli, {kategori_karsilasmasi_2.title ()} alanı verimsiz kullanılmıştır, verimleri sırasıyla 1 birim metre kareye {("{:.2f}".format ( round ( float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ), 2 ) ))} ve {("{:.2f}".format ( round ( float ( kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ), 2 ) ))} olarak ortaya çıkmıştır.'
            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 0 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 1:
                return f'Birim metrekareye düşen yoğunluğa bakıldığında {kategori_karsilasmasi_2.title ()} verimli, {kategori_karsilasmasi_1.title ()} alanı verimsiz kullanılmıştır, verimleri sırasıyla 1 birim metre kareye {("{:.2f}".format ( round ( float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ), 2 ) ))} ve {("{:.2f}".format ( round ( float ( kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ), 2 ) ))} olarak ortaya çıkmıştır.'
            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 0 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 0:
                return f'Birim metrekareye düşen yoğunluğa bakıldığında {kategori_karsilasmasi_1.title ()} ve {kategori_karsilasmasi_2.title ()} alanı verimsiz kullanılmıştır, verimleri sırasıyla 1 birim metre kareye {("{:.2f}".format ( round ( float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ), 2 ) ))} ve {("{:.2f}".format ( round ( float ( kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ), 2 ) ))} olarak ortaya çıkmıştır.'

        yogunlu_b_m2_verim_karsilastirma_yazi = yogunlu_b_m2_verim_karsilastirma ( kategori_1_magaza_ici_yogunluk,
                                                                                   kategori_1_magaza_ici_m2_orani,
                                                                                   kategori_2_magaza_ici_yogunluk,
                                                                                   kategori_2_magaza_ici_m2_orani )

        def yogunlu_b_m2_verim_karsilastirma_aksiyon(kategori_1_magaza_ici_yogunluk, kategori_1_magaza_ici_m2_orani,
                                                     kategori_2_magaza_ici_yogunluk, kategori_2_magaza_ici_m2_orani):

            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 1 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 1:
                return f"Her iki alanda da yoğunluğu ve dolayısıyla satışları arttırmak için alana gelen kişi sayısını ve geçirilen süreyi arttırmak için aksiyon alınmasina gerek yoktur. Aynı verimin mağazanın farklı bir konumunda elde edilip edilemeyeceği, bunun neticesinde diğer alanların verimliliğinin arttırılıp arttırrılamayacağı denenebilir."

            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 1 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 0:
                return f'Alana gelen kişi sayısını ve geçirilen süreyi arttırmak için {kategori_karsilasmasi_1.title ()} alanında bir aksiyona gerek yoktur, fakat {kategori_karsilasmasi_2.title ()} alanına bir aksiyon gereklidir. Bu alan, yoğunluk bazında verimli kullanılamamıştır. Alana ayrılan metre karenin büyük geldiği düşünülüyorsa alan kademeli olarak küçültülmeli, metre kare küçülürken satış azalmıyorsa alan küçültülmelidir.'
            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 0 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 1:
                return f'Alana gelen kişi sayısını ve geçirilen süreyi arttırmak için {kategori_karsilasmasi_2.title ()} alanında bir aksiyona gerek yoktur, fakat {kategori_karsilasmasi_1.title ()} alanına bir aksiyon gereklidir. Bu alan, yoğunluk bazında verimli kullanılamamıştır. Alana ayrılan metre karenin büyük geldiği düşünülüyorsa alan kademeli olarak küçültülmeli, metre kare küçülürken satış azalmıyorsa alan küçültülmelidir.'
            if float ( kategori_1_magaza_ici_yogunluk ) / float ( kategori_1_magaza_ici_m2_orani ) >= 0 and float (
                    kategori_2_magaza_ici_yogunluk ) / float ( kategori_2_magaza_ici_m2_orani ) >= 0:
                return f"Her iki alanda da yoğunluğu ve dolayısıyla satışları arttırmak için alana gelen kişi sayısını ve geçirilen süreyi arttırmak için aksiyon alınmalıdır.Çünkü bu alanlar, yoğunluk bazında verimli kullanılamamıştır. Alanlara ayrılan metre karenin büyük geldiği düşünülüyorsa alanlar kademeli olarak küçültülmeli, metre kare küçülürken satış azalmıyorsa alanlar küçültülmelidir.'"

        yogunlu_b_m2_verim_karsilastirma_aksiyon_yazi = yogunlu_b_m2_verim_karsilastirma_aksiyon (
            kategori_1_magaza_ici_yogunluk, kategori_1_magaza_ici_m2_orani, kategori_2_magaza_ici_yogunluk,
            kategori_2_magaza_ici_m2_orani )

        kategori_1_kisi_sayisi = kategori_1[1][3]  # kisi sayisi
        kategori_1_sure = kategori_1[1][6]  # sure
        kategori_1_m2 = kategori_1[1][10]  # sure
        kategori_1_m2_orani = kategori_1[1][11]  # sure
        kategori_1_yogunluk = kategori_1[1][0]
        kategori_1_m2_bolu_yogunluk = float ( kategori_1_m2 ) / float ( kategori_1_yogunluk )

        kategori_2_kisi_sayisi = kategori_2[1][3]  # kisi sayisi
        kategori_2_sure = kategori_2[1][6]  # sure
        kategori_2_m2 = kategori_2[1][10]  # sure
        kategori_2_m2_orani = kategori_2[1][11]  # sure
        kategori_2_yogunluk = kategori_2[1][0]
        kategori_2_m2_bolu_yogunluk = float ( kategori_2_m2 ) / float ( kategori_2_yogunluk )

        print ( "su sayilara bakk" )
        print ( kategori_1_m2_bolu_yogunluk )
        print ( kategori_2_m2_bolu_yogunluk )

        def yazilar(kategori_karsilasmasi_1, kategori_1_kisi_sayisi, kategori_1_sure, kategori_karsilasmasi_2,
                    kategori_2_kisi_sayisi, kategori_2_sure):
            if kategori_1_kisi_sayisi > kategori_2_kisi_sayisi:
                print ( "süre ağırlıklı" )
                if kategori_1_sure > kategori_2_sure:
                    return f'{kategori_karsilasmasi_1.title ()} alanında yoğunluğu oluşturan asıl parametre kişi sayısı ve ortalama geçirilen süredir. {kategori_karsilasmasi_2} alanına daha çok odaklanılmalıdır. Bu alanda geçirilen ortalama süre sadece {kategori_1_sure} saniye, ortalama kişi sayısı {kategori_1_kisi_sayisi} kişidir.'
                else:
                    return f'{kategori_karsilasmasi_1.title ()} alanında yoğunluğu oluşturan asıl parametre kişi sayısıdır. Bu alanda yoğunluğu arttırmak için süreyi arttırmaya odaklanmak gerekir. Bu alanda geçirilen ortalama süre sadece {kategori_1_sure} saniyedir.'

            elif kategori_1_sure > kategori_2_sure:
                return f'{kategori_karsilasmasi_1.title ()} alanında yoğunluğu oluşturan asıl parametre süre ağırlıklıdır. Bu alanda yoğunluğu arttırmak için kişi sayısını arttırmaya odaklanmak gerekir. Bu alandaki ortalama kişi sayısı {kategori_1_sure} saniyedir.'
            else:
                return f'{kategori_karsilasmasi_2.title ()} alanına göre kişi veya süre ağırlıklı değildir. Bu alanda yoğunluğu arttırmak için kişi sayısını ve süreyi arttırmaya odaklanmak gerekir.'

        ilk_part = yazilar ( kategori_karsilasmasi_1, kategori_1_kisi_sayisi, kategori_1_sure, kategori_karsilasmasi_2,
                             kategori_2_kisi_sayisi, kategori_2_sure )
        ikici_part = yazilar ( kategori_karsilasmasi_2, kategori_2_kisi_sayisi, kategori_2_sure,
                               kategori_karsilasmasi_1, kategori_1_kisi_sayisi, kategori_1_sure )

        def m2_karsilastirma(kategori_karsilasmasi_1, kategori_1_m2, kategori_karsilasmasi_2, kategori_2_m2):
            if kategori_1_m2 > kategori_2_m2:
                return (
                    f'Mağaza içerisinde {kategori_karsilasmasi_1.title ()} alanının m2 orani büyüktür, fark {("{:.2f}".format ( round ( kategori_1_m2 - kategori_2_m2, 2 ) ))} kadardır.')  # {("{:.2f}".format(round(kategori_1_m2-kategori_2_m2, 2)))}
            elif kategori_2_m2 > kategori_1_m2:
                return (
                    f'Mağaza içerisinde {kategori_karsilasmasi_2.title ()} alanının m2 orani küçüktür,fark {("{:.2f}".format ( round ( kategori_2_m2 - kategori_1_m2, 2 ) ))} kadardır.')
            elif kategori_1_m2 + 2 > kategori_2_m2 or kategori_1_m2 - 2 > kategori_2_m2:
                return (f"Mağaza içerisinde her iki alana ayrılan metre kareler yaklaşık olarak eşittir.")

        m2_karsilartirma_1 = m2_karsilastirma ( kategori_karsilasmasi_1, kategori_1_m2, kategori_karsilasmasi_2,
                                                kategori_2_m2 )

        def yogunluk_karsilastirma(kategori_karsilasmasi_1, kategori_1_yogunluk, kategori_karsilasmasi_2,
                                   kategori_2_yogunluk):
            if kategori_1_yogunluk > kategori_2_yogunluk:
                return (
                    f'{kategori_karsilasmasi_1.title ()} alanı, {kategori_karsilasmasi_2.title ()} alanının yaklaşık olarak {("{:.2f}".format ( round ( kategori_1_yogunluk / kategori_2_yogunluk, 2 ) ))} katı yoğunluğa sahiptir.')
            else:
                return (
                    f'{kategori_karsilasmasi_2.title ()} alanı, {kategori_karsilasmasi_1.title ()} alanının yaklaşık olarak {("{:.2f}".format ( round ( kategori_2_yogunluk / kategori_1_yogunluk, 2 ) ))} katı yoğunluğa sahiptir.')

        yogunluk_karsilastirma_1 = yogunluk_karsilastirma ( kategori_karsilasmasi_1, kategori_1_yogunluk,
                                                            kategori_karsilasmasi_2, kategori_2_yogunluk )

        document.add_picture (
            os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/kategori_karsilastirmasi{siralamasi}.png" ),
            width=Inches ( 6 ), height=Inches ( 3.83 ) )
        last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = document.add_paragraph (
            f"({kategori_karsilasmasi_1.title ()} ve {kategori_karsilasmasi_2.title ()} Alanlarının Yoğunlukları)" )
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p = document.add_paragraph ( f"" )
        p.add_run (
            f'Mağaza içerisindeki {kategori_karsilasmasi_1.title ()} ve {kategori_karsilasmasi_1.title ()} alanlarının yoğunlukları, metre kareleri ve metre kare başına düşen yoğunluk yüzdeleri kıyaslanmıştır.' ).italic = True

        document.add_paragraph (
            f'{m2_karsilartirma_1}', style='List Bullet'
        )
        document.add_paragraph (
            f'{yogunluk_karsilastirma_1}', style='List Bullet'
        )
        document.add_paragraph (
            'Yoğunluk paylarının, satış paylarına paralel olması beklenir.', style='List Bullet'  # burayi gelistir
        )
        document.add_paragraph (
            f'{yogunlu_b_m2_karsilastirma_yazi}', style='List Bullet'
        )  # ! duzelt
        document.add_paragraph (
            f'{yogunlu_b_m2_verim_karsilastirma_yazi}', style='List Bullet'
        )
        document.add_paragraph (
            f'{yogunlu_b_m2_verim_karsilastirma_aksiyon_yazi}',
            style='List Bullet'
        )
        # document.add_paragraph(
        #     f'Alanlarda yoğunluk/metre kare oranı 1 in aldtında kaldığı şartlar altında; Alana ayrılan metre karenin büyük geldiği düşünülüyorsa alan kademeli olarak küçültülmeli, metre kare küçülürken satış azalmıyorsa alan küçültülmelidir.', style='List Bullet'
        # )
        # document.add_paragraph(
        #     f'Yoğunluktaki artışın satışı da arttırması beklenir.', style='List Bullet'
        # )

        document.add_picture (
            os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/karsilastitilacak_{ikiser_siralamasi}.png" ),
            width=Inches ( 6 ), height=Inches ( 0.35 ) )
        last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        document.add_picture (
            os.path.join ( BASE_DIR, f"{magza_statik_dosya_location}/karsilastitilacak_{ikiser_siralamasi + 1}.png" ),
            width=Inches ( 6 ), height=Inches ( 0.35 ) )
        last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
        last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p = document.add_paragraph (
            f"({kategori_karsilasmasi_1.title ()} ve {kategori_karsilasmasi_2.title ()} Tablosu)" )
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

        p = document.add_paragraph ( f"Detaya inildiğinde;" )
        document.add_paragraph (
            f'{ilk_part}', style='List Bullet'
        )

        document.add_paragraph (
            f'{ikici_part}', style='List Bullet'
        )
        # document.add_page_break ()

    ikiser_siralamasi = 0
    siralamasi = 1
    for karsilastirilacak in karsilastirilacak_isim_listesi:
        populate_karsilastirma ( karsilastirilacak[0], karsilastirilacak[1], magaza_id_no, siralamasi,
                                 ikiser_siralamasi )
        siralamasi += 1
        ikiser_siralamasi += 2

    document.add_page_break ()
    document.add_heading ( '4.0 Sonuç', 0 )

    document.add_heading ( '4.1 Analizin Sonucu', level=1 )

    p = document.add_paragraph (
        f"Bu raporda {magaza_adi} mağazası detaylı olarak incelenmiştir. Alınacak muhtemel aksiyonlar da gösterilmiştir.\nBu aksiyonların uygulanıp uygulanmadığını Udentify tarafına bildirdiğinizde detaylı olarak analizlerle değişimlerin başarısını ölçümleyip size raporlamak isteriz." )

    """p = document.add_paragraph(f"")
    p.add_run(f"Günlük Kişi Süre Grafiği").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""

    document.add_heading('2.1 Günlük Kişi Süre Grafiği', level=1)


    ee = os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/giren_m_1.png")
    ee_o = os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/Giren_Kişi_Sayısı_gunluk.png")# toplam_kisi_sure.png di degisitii !

    #deneme = image_corpingv1.image_corp_edit_infile(ee,ee_o,1008,286) #kullanmamis oldugundan emin old !!!!!!!!!!!!!___________________




    document.add_picture(ee_o, width=Inches(6) , height=Inches(2)) #kesme fonksiyonlari cok iyi degil
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Toplam Kişi & Ortalama Geçirilen Süre Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER





    document.add_paragraph(
        f"Kişi-süre grafiği incelendiğinde {tarih} tarihleri arasında mağazaya gelen ziyaretçi sayısında ve geçirdikleri süredeki değişiklikler görülmektedir.", style='List Bullet'
    )

    document.add_paragraph(
        f"Hafta sonları ortalama kişi sayısı {haftasonu_ortalama_2_8}", style='List Bullet'
    )

    document.add_paragraph(
        f"Mağazaya gelen ziyaretçilere ortalma satış miktarı {satis_ortalama} TL dir.", style='List Bullet'
    )

    document.add_paragraph(
        f"Hafta sonu mağazaya gelen ortalama ziyaretçi sayısı, hafta içinin {hafta_ici_hafta_sonu_musteri_orani} katıdır.", style='List Bullet'
    )

    ##########___________________2.1 fonksiyonnlar   ## silindiii yogunluk kismi

    # yougunluk_miktarlari = request1.main_1_1_yogunluk_listesi ( magaza_id_no, ilk_tarih, son_tarih )
    # print ( yougunluk_miktarlari )
    # yogunluk_tarihleri = request1.main_1_1_yogunluk_listesi_tarihler ( magaza_id_no, ilk_tarih, son_tarih )
    # print ( yogunluk_tarihleri )
    # # dictionary = dict ( zip ( liste, liste1 ) )
    # # print(dictionary)
    # array_yogunluk = list ( zip ( yogunluk_tarihleri, yougunluk_miktarlari ) )
    # print ( array_yogunluk )
    # print ( request1.cal_average_density_arrray ( array_yogunluk ) )
    # print ( request1.bigger_than_average_arrray ( array_yogunluk ) )
    # ortalamanin_ustundeki_yogunluklar = request1.bigger_than_average_arrray ( array_yogunluk )
    # print ( "bak____" )
    # print ( ortalamanin_ustundeki_yogunluklar )
    #
    #
    # document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/yogunluk_yogunluk_ortalamasi.png"), width=Inches(6) , height=Inches(2))
    # last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    # last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    # p = document.add_paragraph(f"(Yoğunluk Trendi Tablosu)")
    # p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    #
    #
    # document.add_paragraph(
    #     'Yoğunluk grafiği incelendiğinde, yoğunluğun ortalamanın üstüne çıktığı tarihler görülmektedir.', style='List Bullet'
    # )
    #
    # document.add_paragraph(
    #     f'{ortalamanin_ustundeki_yogunluklar[0].title()} tarihi yoğunluğun en çok arttığı tarihlerden biridir. Yoğunluktaki artışın sebebi, kişi sayısındaki artıştır.', style='List Bullet'
    # )
    #
    # document.add_paragraph(
    #     f'Yoğunluğun en çok artış gösterdiği diğer bir tarih {ortalamanin_ustundeki_yogunluklar[0].title()}’dir. O gün yoğunluğun artmasının sebebi, mağaza içerisinde geçirilen sürenin artış göstermesidir.', style='List Bullet'
    # )




    #sayfa-2.2_____________________________________________________
    #document.add_page_break()

    """p = document.add_paragraph(f"")
    p.add_run(f"Saatlik Kişi Süre Grafiği").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""

    document.add_heading('2.2 Saatlik Kişi Süre Grafiği', level=1)


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/Giren_Kişi_Sayısı_saatlik.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Toplam Kişi - Ortama Geçirilen Saatlik Süre Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_paragraph(
        f'Mağazaya en çok sayıda ziyaretçinin geldiği saat aralığı {max_saat_araligi} saatleri arasıdır', style='List Bullet'
    )

    document.add_paragraph(
        f'Mağaza içerisinde geçirilen {en_yogun_zaman} saatlerinde artmaktadır. ', style='List Bullet'
    )

    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/En_Çok_Vakit_Geçirilen_Alanlar_kişi_sn_saatlik.png"), width=Inches(4.5) , height=Inches(2.95))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(En Çok Ziyaret Edilenler Tablosu(saatlik))")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_picture ( os.path.join ( BASE_DIR,
                                          f"{magza_statik_dosya_location}/En_Çok_Ziyaret_Edilen_Alanlar_kişi_adet_saatlik.png" ),width=Inches(4.5) , height=Inches(2.95)
                            )
    last_paragraph = document.paragraphs[-1]  # resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph ( f"(En Çok Ziyaret Edilenler Tablosu(saatlik))" )
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER



    #sayfa-2.3_____________________________________________________
    document.add_page_break()

    """p = document.add_paragraph(f"")
    p.add_run(f"Yoğunluk Haritası").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""

    document.add_heading('2.3 Yoğunluk Haritası', level=1)


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/yogunluk_haritasiyogunluk.png"), width=Inches(6) , height=Inches(3.43))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Yoğunluk Haritaları Ve Tabloları)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/top5.png"), width=Inches(2) , height=Inches(2))
    # last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    # last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        f'Yukarıdaki yoğunluk haritası incelendiğinde, mağazanın en yoğun alanlarının {liste_yogunluk_top_5[0].title()}, {liste_yogunluk_top_5[1].title()} ve {liste_yogunluk_top_5[2].title()} alanları olduğu görülür.', style='List Bullet'
    )

    document.add_paragraph(
        f'Yoğunluğun en az olduğu alanlar ise; {liste_yogunluk_bottom_5[0].title()}, {liste_yogunluk_bottom_5[1].title()}, {liste_yogunluk_bottom_5[2].title()}, {liste_yogunluk_bottom_5[3].title()}, ve {liste_yogunluk_bottom_5[4].title()} alanlarıdır.', style='List Bullet'
    )











    #sayfa-2.4_____________________________________________________

    document.add_page_break()


    """p = document.add_paragraph(f"")
    p.add_run(f"Mağaza İçi Yoğunluk Dağılımı").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""

    document.add_heading('2.4 Mağaza İçi Yoğunluk Dağılımı', level=1)


    p = document.add_paragraph(f"")
    p.add_run('Mağaza içerisindeki alanlar, yoğunluğu en büyük olandan en küçük olana doğru sıralanmıştır.').italic = True


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/magaza_ici_dagilimi.png"), width=Inches(6) , height=Inches(7))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Yoğunluk Alan Tablosu)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER




    #sayfa-2.5_____________________________________________________
    document.add_page_break()


    """p = document.add_paragraph(f"")
    p.add_run(f"Metre Kare Başına Düşen Yoğunluk Haritası").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""

    document.add_heading('2.5 Metre Kare Başına Düşen Yoğunluk Haritası', level=1)


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/yogunluk_haritasiYoğunluk_m2.png"), width=Inches(6) , height=Inches(3.34))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Yoğunluk Haritası Ve Tablosu)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        f"Metre kare başına düşen yoğunluklar incelendiğinde, bazı alanlarda bu oranın 1’den küçük olduğu görülür. Bu, birim metre kare başına birim yoğunluktan daha az yoğunluk düştüğünü gösterir.  Birçok alanda metre kare başına düşen yoğunluk 1’in altında kalmıştır. Örneğin; {yogunlugu_1_in_ustundekiler[0].title()}, {yogunlugu_1_in_ustundekiler[1].title()}, {yogunlugu_1_in_ustundekiler[2].title()} alanları en düşük metre kare başına düşen yoğunluk oranına sahiptir.", style='List Bullet'
    )

    document.add_paragraph(
        'Bu alanlarda, metre karenin küçültülmesi düşünülebilir. Buna karar vermek için metre kare kademeli olarak küçültülüp bunun satışa etkisi incelenmelidir. Alan küçülürken satış azalmıyorsa alan küçültülmelidir.', style='List Bullet'
    )
    try:
        listeyy = f"{yogunlugu_1_in_altindakiler[0].title ()}, {yogunlugu_1_in_altindakiler[1].title ()}, {yogunlugu_1_in_altindakiler[2].title ()}"
    except:
        try:
            listeyy = f"{yogunlugu_1_in_altindakiler[0].title ()}, {yogunlugu_1_in_altindakiler[1].title ()}"
        except:
            try:
                listeyy = f"{yogunlugu_1_in_altindakiler[0].title ()}"
            except:
                listeyy = f"hepsi cok iyi"


    document.add_paragraph(
        f"Bazı alanlarda ise bu oran 1’in üstündedir. Yani, birim metre kare başına birim yoğunluktan daha fazlası düşmüştür. Örneğin; {listeyy} alanları.", style='List Bullet'
    )

    document.add_paragraph(
        'Aynı mantıkla, küçültülen alanlardan kalan payın bu alana verilerek bu alanın genişletilmesi düşünülebilir. ', style='List Bullet'
    )


    #sayfa-2.6_____________________________________________________
    document.add_page_break()

    """p = document.add_paragraph(f"")
    p.add_run(f"Isı Haritası").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""





    #sayfa-2.7_____________________________________________________
    document.add_page_break()


    """p = document.add_paragraph(f"")
    p.add_run(f"Performans Kıyaslaması").bold = True"""


    document.add_heading('2.7 Performans Kıyaslaması', level=1)


    p = document.add_paragraph(f"")
    p.add_run(f'{tarih_1}-{tarih_4} tarih aralığı, 01/01/2020-14/01/2020 aralığı ile kıyaslanmıştır.').italic = True


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/performans_tablosu_final.png"), width=Inches(6) , height=Inches(5))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"(Performans Tablosu)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER







    p = document.add_paragraph(f"")
    p.add_run('*Performans tablosu, mağaza içerisindeki yoğunluk payı en fazla olan bölgeden en az olan bölgeye doğru sıralanmıştır.').italic = True


    p = document.add_paragraph(f"Performans tablosu incelendiğinde;")

    document.add_paragraph(
        f'Kişi sayısı en çok artan alan %{kisi_sayisi2_7_deger} artış ile {kisi_sayisi2_7_isim} alanı,', style='List Bullet'
    )

    document.add_paragraph(
        f'Geçirilen süresi en çok artan alan %{gecirilen_sure_2_7_deger} artış ile {gecirilen_sure_2_7_isim} alanı,', style='List Bullet'
    )
    document.add_paragraph(
        f'İlgi oranı en yüksek olan alan %{ilgi_oranı_2_7_deger} ile {ilgi_oranı_2_7_isim} alanı,', style='List Bullet'
    )

    document.add_paragraph(
        f'İlgi oranı en az olan alan %{ilgi_oranı_n2_7_deger} ile {ilgi_oranı_n2_7_isim} alanı,', style='List Bullet'
    )
    document.add_paragraph(
        f'En çok zaman geçirilen alan ortalama {en_cok_zaman_2_7_deger} saniye ile {en_cok_zaman_2_7_isim} alanı,', style='List Bullet'
    )
    document.add_paragraph(
        f'En çok ziyaret edilen alan günde ortalama {performans_tablosu_listesi[1][3]} kişi ile {performans_tablosu_listesi[0][0].title()} alanı olmuştur.', style='List Bullet'
    )






    #sayfa-2.8_____________________________________________________
    #document.add_page_break()


    document.add_heading(f'2.8 {performans_tablosu_listesi[0][0].title()}', level=1)


    p = document.add_paragraph(f"Mağaza içerisindeki en yoğun alan olan {performans_tablosu_listesi[0][0].title()} alanının detayına inildiğinde;")

    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/Alana_Giriş_Sayısı_&_Ortalama_Geçirilen_Süre_gunluk.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Alanı Toplam Kişi Ve Günlük Süre Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        f'Günlük kişi süre grafiği incelendiğinde, hafta sonu mağazaya gelen ortalama kişi sayısı hafta sonuna göre {artis_2_8} Bu oran {katsayi_2_8} katıdır.', style='List Bullet'
    )

    document.add_paragraph(
        f'Bu alana gelen bir kişinin alanda geçirdiği ortalama süre {ortalama_sure_2_8} saniyedir.', style='List Bullet'
    )


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/Alana_Giriş_Sayısı_&_Ortalama_Geçirilen_Süre_saatlik.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Alanı Toplam Kişi Ve Saatlik Süre Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        f'Saatlik kişi süre grafiği incelendiğinde mağazaya en çok sayıda ziyaretçinin geldiği zaman aralığının {artisin_oldugu_sure_2_8} saatleri arası olduğu görülür.', style='List Bullet'
    )

    document.add_paragraph (
        'Geçirilen sürenin arttığı saatlerde müşteri ilgisi artmaktadır.', style='List Bullet'
    )

    document.add_paragraph(
        f'Kişi sayısı ile süre korelasyonu {korelasyon_degeri_2_8} dir, yani {korelasyon_turu} vardır.', style='List Bullet'
    )


    document.add_paragraph(
        'Bu saatlerde, artan yoğunluk potansiyelini satışa dönüştürmek için personel ilgisine ekstra dikkat etmek gerekir.', style='List Bullet'
    )


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/Alana_Giriş_Sayısı_&_Ortalama_Geçirilen_Süre_yogunluk_gunluk.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Alanı Yoğunluk Ve Yoğunluk Ortalaması Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        f'Yoğunluk grafiğinde, yoğunluğun ortalamanın üstünde ve altında kaldığı günler görülmektedir. Yoğuluğun arttığı tarihler {request1.list_to_string(ortalamanin_ustundeki_yogunluklar_2_8)} olarak gözükmektedir. Yoğunluğun arttığı günlerde, satışın da artması beklenir.', style='List Bullet'
    )

    document.add_paragraph(
        f'{hafta_ici_hafta_sonu_oranlari_2_8}', style='List Bullet'
    )

    ##-_____________________________________________________


    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/korelasyonlar.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Alanı Korelasyon Tablosu)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER


    document.add_paragraph(
        'Korelasyonlar incelendiğinde, bu alana gelen ziyaretçilerin büyük çoğunluğunun bu alandan sonra men’s sportstyle alanına yöneldiği görülür.', style='List Bullet'
    )

    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/ters_ucgen.png"), width=Inches(6) , height=Inches(2))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Edinme Hunisi)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    document.add_paragraph(
        'Edinme hunisi incelendiğinde, alana gelen kişilerin', style='List Bullet'
    )
    p = document.add_paragraph(f"o 15 saniye ve üzeri alanında {edinme_hunisi_yuzde[2][1]}%.")
    p = document.add_paragraph(f"o 10 saniye ve üzeri alanında {edinme_hunisi_yuzde[1][1]}%.")
    p = document.add_paragraph(f"o 3 saniye ve üzeri alanında {edinme_hunisi_yuzde[0][1]}% zaman geçirilmektedir.")



    p = document.add_paragraph(f"{performans_tablosu_listesi[0][0].title()} alanının performans değişimi incelendiğinde;")

    document.add_picture(os.path.join(BASE_DIR, f"{magza_statik_dosya_location}/performans_tek0.png"), width=Inches(6) , height=Inches(0.35))
    last_paragraph = document.paragraphs[-1]#resimleri ortalamak icin
    last_paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = document.add_paragraph(f"({performans_tablosu_listesi[0][0].title()} Alanı Yüzdelik Performans Değişimi Grafiği)")
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER









    print("simdi son")

    degerler = performans_tablosu_listesi[1][3]



    ilgi_orani_artisi_2_8 = performans_tablosu_listesi[1][9]

    def ilgi_orani_durumu():
        if ilgi_orani_artisi_2_8> 0:
            return "artmıştır."
        else:
            return "azalmıştır."
    def ilgi_orani_hali():
        if ilgi_orani_artisi_2_8> 0:
            return "artarken"
        else:
            return "azalirken"


    ilgi_orani_durumu_2_8 = ilgi_orani_durumu()

    kişi_sayisi_artisi_2_8 = performans_tablosu_listesi[1][5]
    gecirilen_sure_artisi_2_8 = performans_tablosu_listesi[1][7]
    yogunluk_artisi_2_8 = performans_tablosu_listesi[1][7]

    def ilk_kisim2_8_(kişi_sayisi_artisi_2_8,gecirilen_sure_artisi_2_8,yogunluk_artisi_2_8):

        if kişi_sayisi_artisi_2_8>0:
            if gecirilen_sure_artisi_2_8 > 0:
                if yogunluk_artisi_2_8 > 0:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre hem kişi sayısının hem de geçirilen sürenin sırasıyla {kişi_sayisi_artisi_2_8}% ve {gecirilen_sure_artisi_2_8}% artmasına bağlı olarak yoğunluk {yogunluk_artisi_2_8}% artmıştır.',1]
                else:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre hem kişi sayısının hem de geçirilen sürenin sırasıyla {kişi_sayisi_artisi_2_8}% ve {gecirilen_sure_artisi_2_8}% artmasına bağlı olarak yoğunluk {yogunluk_artisi_2_8}% azalmıştır.',0]
            else:
                if yogunluk_artisi_2_8 > 0:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% artmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile azalmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% artmıştır.',1]
                else:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% artmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile azalmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% azalmıştır.',0]

        else:
            if gecirilen_sure_artisi_2_8 > 0:
                if yogunluk_artisi_2_8 > 0:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% ile azalmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile artmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% artmıştır.',1]
                else:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% ile azalmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile artmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% azalmıştır.',0]

            else:
                if yogunluk_artisi_2_8 > 0:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% ile azalmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile azalmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% artmıştır.',1]
                else:
                    return [f'İlgili alanda, bir önceki tarih aralığına göre kişi sayısı {kişi_sayisi_artisi_2_8}% ile azalmıştır, geçirilen süre  {gecirilen_sure_artisi_2_8}% ile azalmıştır bunların etkisiyle; yoğunluk {yogunluk_artisi_2_8}% azalmıştır.',0]

    ilk_kisim2_8_yazi = ilk_kisim2_8_(kişi_sayisi_artisi_2_8,gecirilen_sure_artisi_2_8,yogunluk_artisi_2_8)

    if ilk_kisim2_8_yazi[1]== True:
        paragraf_2 = 'Yoğunluktaki genel artışın satışı da buna yakın bir yüzdeyle arttırması beklenir.'
    else:
        paragraf_2 = 'Yoğunluktaki genel azalışın satışı buna yakın bir yüzdeyle azaltması beklenir.'

    if ilk_kisim2_8_yazi[1]== True:
        paragraf_3 = 'artarken'
    else:
        paragraf_3 = 'azalırken'

    ilgi_hali_2_8 = ilgi_orani_hali()

    def yogunluk_orani_hali():
        if ilk_kisim2_8_yazi[1] == 1:
            return "artarken"
        else:
            return "azalirken"

    yogunluk_hali_2_8 = yogunluk_orani_hali()


    document.add_paragraph(
        f'{ilk_kisim2_8_yazi[0]}', style='List Bullet'
    )
    document.add_paragraph(
        f'{paragraf_2}', style='List Bullet'
    )

    p = document.add_paragraph(f"Satışlar arttıysa;")

    p = document.add_paragraph(f"o Yoğunluk {paragraf_3} satışın da artması, alandaki potansiyelin yükselmekte olduğunu gösterir.")
    p = document.add_paragraph(f"o Satış hedefini daha da yükseltmeye yönelik aksiyon alınmalıdır.")
    p = document.add_paragraph(f"o Önceki tarih aralığına göre ilgi oranı da {ilgi_orani_artisi_2_8}% {ilgi_orani_durumu_2_8}. ")
    p = document.add_paragraph(f"o Bu alanda ilgi oranı {ilgi_hali_2_8} ve yoğunluk {yogunluk_hali_2_8} satış da arttığına göre bu alanda geçirilen sürenin satışa olan etkisi incelenmelidir.")
    p = document.add_paragraph(f"o Satışı daha da arttırmak için ziyaretçilerin alanda daha fazla zaman geçirmesi sağlanabilir.")
    p = document.add_paragraph(f"o Bunun için; personel ilgisi, ürün fiyat dengesi, ürün çeşitliliği gözden geçirilebilinir ")





    ##-sayfa-2.9_____________________________________________________

    """p = document.add_paragraph(f"")
    p.add_run(f"Kategori Karşılaştırması").bold = True
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER"""




    ###-11_______________________________________________





    #sayfa-3.1




    print("basarili_")#________Bitti

    document.add_page_break()

    document.save(f"{magaza_dosyasi_ismi}")



#refresh() # burayi degistirdin



#start_writing_on_docx(magza_statik_dosya_location,magaza_dosyasi_ismi,200,ilk_tarih,son_tarih,gereken_dosya_ismi)


#start_writing_on_docx("Under Armour","under atmour akasyya")


#burasi test kismi

#magaza_adi_listesi = [["Under Armour","Akasya",240,"Under Armour Akasya",240],["Under Armour","Zorlu Center",239,"Under Armour Zorlu Center",240],["Under Armour","İstinye Park",228,"Under Armour Istinye Park",240]]
#
# start_writing_on_docx(firma,magza_statik_dosya_location_ismi,240,ilk_tarih,son_tarih,161,240,[["a","b"],["c","d"]])  ##birincisi firma adi ile dosya konumunu bulmaya yariyor   ,ikincisi statik dosya locationlarini bulmaya yariyor
#
#global_test =  True
#

if __name__ == "__main__":
    #Calismayan
    ilk_tarih = "01/02/2021"
    son_tarih = "12/02/2021"

    #Calisan
    # ilk_tarih = "05/01/2021"
    # son_tarih = "19/01/2021"
    #

    # yeni_liste =[["Under Armour","Under Armour Zorlu Center",239,ilk_tarih,son_tarih,160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]],["Under Armour","Under Armour Akasya",240,ilk_tarih,son_tarih,161,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]],["Under Armour","Under Armour Istinye Park",228,ilk_tarih,son_tarih,149,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]]]]
    #
    # for liste in yeni_liste:
    #     start_writing_on_docx ( liste[0], liste[1], liste[2], liste[3], liste[4], liste[5],
    #                             liste[6] )


    #start_writing_on_docx("under armour","under armour zorlu center",239,ilk_tarih,son_tarih,160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],['Kasa', 'Cam 2', 'Train', 'Cam 4', 'Giriş'])
    #start_writing_on_docx("under armour","under armour akasya",240,ilk_tarih,son_tarih,161,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],['Ana Giriş', 'Cam 7', 'Cam 8', 'Run', 'Youth', 'Giriş', 'Train', 'Train Ön' ])
    # start_writing_on_docx("under armour","under armour istinye park",228,ilk_tarih,son_tarih,149,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]])
    # start_writing_on_docx("suwen","suwen viaport",307,"01/01/2021","19/01/2021",189,[["TAYT","ÇORAP"],["ATLET","ERKEK REYONU"]],['Ön', 'Arka', 'Giriş', 'Cam 4'])
    #start_writing_on_docx("suwen","suwen mall of istanbul",306,"20/01/2021","27/01/2021",189,[["LOHUSA","ÇORAP"],["KORSE","TRENDY"]],['Giriş', 'Sol', 'Sağ', 'Cam 4'])

    # suwen	suwen viaport	307	01/02/2021	12/02/2021	189	[["TAYT","ÇORAP"],["ATLET","ERKEK REYONU"]]	Viaport
    #


    #start_writing_on_docx("Suwen","Suwen Viaport",307,ilk_tarih,son_tarih,189,[["TAYT","ÇORAP"],["ATLET","ERKEK REYONU"]]) #density kisimlari error veriyo cikarmadinn daha



    # start_writing_on_docx("arçelik","arçelik ada",133,"01/02/2021","12/02/2021",99,[["TELEVIZYON","FIRIN"],["SÜPÜRGE","ÜTÜ"]],['KASA','MUTFAK GERECLERI', 'GİRİŞ SAĞ', 'GİRİŞ SOL', 'TELEVIZYON', 'KLIMA', 'DONDURUCU', 'ÇAMAŞIR MAKINESI', 'ÇAMASIR KURUTMA MAKINESI', 'PISIRICI CIHAZLAR'])


    start_writing_on_docx("bizim toptan","bizim toptan Alibeyköy",308,"01/02/2021","12/02/2021",89,[["Kahvaltılık","Çikolata"],["Çay","Cips"]],['Promo Alan','Bakliyat', 'Temel Gıda', 'Atıştırmalık', 'İçecek', 'Gıda dışı', 'Camlı Soğuk Oda', 'Kasa', 'Cam 9', 'Kişisel Bakım', 'Giriş', 'Temizlik', 'Soğuk Dolap'])

    # start_writing_on_docx("mediamarkt","mediamarkt ankara forum",318,"01/02/2021","12/02/2021",234,[["5 LG TV","5 SAMSUNG TV"],["5 VESTEL TV","36 BOSCH"]],['Cam 1', 'Cam 2', 'Cam 3', 'Cam 4', 'Cam 5', 'Cam 6', 'Cam 7', 'Cam 8', 'Cam 9', 'Cam 10', 'Cam 11', 'Cam 12', 'Cam 13', 'Cam 14', 'Cam 15', 'Cam 16', 'Cam 17', 'Cam 18', 'Cam 19', 'Cam 20', 'Cam 21', 'Cam 22', 'Cam 23', 'Cam 24', 'Cam 25', 'Cam 26', 'Cam 27', 'Cam 28', 'Cam 29', 'Cam 30', 'Cam 31', 'Cam 32', 'Cam 33', 'Cam 34'])
    #
    #











