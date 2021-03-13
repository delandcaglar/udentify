import requests
import logging
from logging.handlers import RotatingFileHandler
import os
import datetime
import time
import calendar
import math

from pytz import timezone
from dateutil.relativedelta import relativedelta

utcnow = timezone('utc').localize(datetime.datetime.utcnow()) # generic time
here = utcnow.astimezone(timezone('Turkey')).replace(tzinfo=None)
real_location = (utcnow.astimezone().replace(tzinfo=None))
offset = relativedelta(here, real_location)
offser_ayari = (offset.hours)* 60
print("offset")
print(offser_ayari)
# offser_ayari = 0



BASE_DIR = os.path.dirname ( os.path.dirname ( os.path.abspath ( __file__ ) ) )
print ( BASE_DIR )

dosya_yolu = (BASE_DIR + f"/bot_udentify/test.log")
print ( dosya_yolu )

log_formatter = logging.Formatter ( '%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s' )
logFile = dosya_yolu
my_handler = RotatingFileHandler ( logFile, mode='a', maxBytes=5 * 1024 * 1024, backupCount=2, encoding=None, delay=0 )
my_handler.setFormatter ( log_formatter )
my_handler.setLevel ( logging.INFO )
app_log = logging.getLogger ( 'root' )
app_log.setLevel ( logging.INFO )
app_log.addHandler ( my_handler )

APIURL = "https://api.udentify.co"
APIUSER = "delandcaglar@hotmail.com"
APIPASS = "caglar2020"
APITOKEN = ""

# tarih_ilk = "16/11/2020"
# tarih_son = "02/12/2020"
tarih_ilk = "05/02/2021"
tarih_son = "19/02/2021"

url1 = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"
url_yogunluk = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"
ure_yogunluk_g = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"

saatlik_kisi_sure_grafigi = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset={}"
yogunluk_haritasi = "{}/Sketch/{}/Rectangles?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset={}&layer=1"  ##hatali

performas_tablosu = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset={}&layer=1"  ##  180 i 0 yaptin duzelt

deneme_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset={}&layer=1"
deneme2_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}0&stime=10:00&etime=22:00&tzoffset={}&layer=1"

devam = "{}/Rect/9954/CountandSpenttime?sdate=15/11/2020&edate=26/11/2020&stime=10:00&etime=22:00&filter=1&tzoffset={}"

gunluk_kisi_sure_grafigi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"
gunluk_kisi_sure_grafigi_2_8_updated = "{}/Store/{}/LineEntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"
gunluk_kisi_sure_grafigi_2_8_updated_saatlik = "{}/Store/{}/LineEntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset={}"

yogunluk_haritasi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"
saatlik_kisi_sure_grafigi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset={}"

edinme_hunisi_url = "{}/Rect/{}/Funnel?sdate={}&edate={}&stime=10:00&etime=22:00&funnelthresholds=3,10,15&tzoffset={}"  # 3, 10 , 15 sabit

store_sure_api = "{}/Store/{}/CheckoutSummary?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset={}"

store_sure_api_saatlik = "{}/Store/{}/CheckoutSummary?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset={}"



# https://api.udentify.co/Store/240/AreaCount?sdate=15/10/2020&edate=30/10/2020&stime=10:00&etime=22:00&tzoffset=0

def get_token():
    url = "{}/token".format ( APIURL )
    payload = (("grant_type", "password"), ("username", APIUSER), ("password", APIPASS))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return requests.post ( url, data=payload, headers=headers ).json ()["access_token"]


def get_performancetable(url1, storeId, start, end):
    global APITOKEN
    global offser_ayari
    if APITOKEN == "":
        APITOKEN = get_token ()
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + APITOKEN,
    }
    print("offset_ayari")
    print(offser_ayari)
    # url = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1".format ( APIURL,storeId,start,end )
    url = url1.format ( APIURL, storeId, start, end ,offser_ayari) # ofset ayarini koy buraya
    r = requests.get ( url, headers=headers )
    return r.json ()


def main(url1):
    data = get_performancetable ( url1, 240, '15/10/2020', '30/10/2020' )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print ( headersiz_data )
    print ( "________________________________" )
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[1]["Name"] ) #Customer
    # print ( headersiz_data[1]["Serial"] )
    # print ( headersiz_data[3]["Name"] ) ##eime
    # print ( headersiz_data[3]["Serial"] )

    # list_data = json.loads ( headersiz_data )

    # print(list_data['fruits'])



### Udentify Onemli Fonksiyonlar




def list_to_string(s):
    # Output Ornegi: 5 UHD-LCD TV PALET , 131 YER BAKIM URUNLERI , 142 CAMASIR MAKINELERI, Kasa
    # initialize an empty string
    str1 = " "

    elma = [x for y in (s[i:i + 1] + [','] * (i < len ( s ) - 1) for i in range ( 0, len ( s ), 1 )) for x in y]
    # print(elma)
    # return string
    return (str1.join ( elma ))

def list_to_string_ve_ile(s):
    # Output Ornegi: 5 UHD-LCD TV PALET , 131 YER BAKIM URUNLERI , 142 CAMASIR MAKINELERI ve Kasa
    # initialize an empty string
    son_part = s[-1:]
    s = s[:-1]
    str1 = " "
    str2 = " "
    ilk_liste = [x for y in (s[i:i + 1] + [','] * (i < len ( s ) - 1) for i in range ( 0, len ( s ), 1 )) for x in y]
    ikici_liste = [x for y in (son_part[i:i + 1] + [','] * (i < len ( son_part ) - 1) for i in range ( 0, len ( son_part ), 1 )) for x in y]
    final_form2 = (str2.join ( ikici_liste ))
    final_form = (str1.join ( ilk_liste ))
    final_form1 = f"{final_form} ve {(final_form2)}"
    if final_form == "":
        final_form1 = f"{(final_form2)}"

    return final_form1

def cakisan_liste_elemanlar(list_1, list_2):
    cakisan_elemanlar_listesi = []
    for element in range(0, len(list_1)):
        if list_1[element] in list_2:
            cakisan_elemanlar_listesi.append(list_1[element])
    return cakisan_elemanlar_listesi

def cakisan_liste_elemanlar_ilk_3(list_1, list_2):
    cakisan_elemanlar_listesi = []
    for element in range(0, 3):
        print(element)
        if list_1[element] in list_2[0:3]:
            cakisan_elemanlar_listesi.append(list_1[element])
    return cakisan_elemanlar_listesi

def listeleri_oranla(liste1,liste2):
    liste3=[]
    for element in range(0,len(liste2)):
        print(element)
        print(liste2[element])
        artis = float(liste2[element])/float(liste1[element])
        son_kisim = artis -1

        liste3.append(float (("{:.2f}".format ( float ( son_kisim )*100, 2 )) ))
    return liste3



def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len ( num )
    return avg

def cal_average_bosluklu_data(num):
    sum_num = 0
    cikarilacak_sayi = 0
    for t in num:
        if t == 0:
            cikarilacak_sayi +=1
        sum_num = sum_num + t

    avg = sum_num / (len ( num ) - cikarilacak_sayi)
    return avg


def cal_total(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num
    return avg


def cal_average_density(num):  ##sadece degeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    for t in num:
        if t != 0:
            sum_num = sum_num + t
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar

    avg = sum_num / (len ( num ) - cikarilacak_sayilar)
    return avg


def cal_average_density_buyuk_olanlar(num):  ##sadece deegeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    for t in num:
        if t != 0:
            sum_num = sum_num + t
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar

    avg = sum_num / (len ( num ) - cikarilacak_sayilar)
    return avg


def cal_average_density_arrray(num):  ##sadece deegeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    for t in num:
        if t[1] != 0:
            sum_num = sum_num + t[1]
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar
    no_zero = len ( num )
    if no_zero == 0:
        no_zero = 1
    print ( "cozumm" )
    print ( num )
    print ( sum_num )
    print ( no_zero )
    avg = sum_num / (no_zero - cikarilacak_sayilar)
    return avg


def bigger_than_average_arrray(num):  ##sadece deegeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    buyuk_olanlar_listesi = []

    for t in num:
        if t[1] != 0:
            sum_num = sum_num + t[1]
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar
    no_zero = len ( num )
    if no_zero == 0:
        no_zero = 1
    avg = sum_num / (no_zero - cikarilacak_sayilar)
    for t in num:
        if t[1] >= avg:
            buyuk_olanlar_listesi.append ( t[0] )

    return buyuk_olanlar_listesi
def BubleSort(sub_li):
    l = len ( sub_li )
    for i in range ( 0, l ):
        for j in range ( 0, l - i - 1 ):
            if (sub_li[j][2] > sub_li[j + 1][2]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li
def negatifse(liste):
    numbers = [2,1,0]
    print('deneme')
    for element in numbers:
        print(element)
        if liste[element][2] < 0:
            liste_hali = liste[0:(element+1)]
            for element in range(len(liste_hali)):
                print(liste_hali)
                print(element)
                print(liste_hali[element])
                liste_hali[element][2] = f"%{-1*liste_hali[element][2]}"
                listea=[]
                listeb=[]
                listec=[]
                for elements in range(len(liste_hali)):
                    print ( 'deneme11' )
                    print(liste_hali)
                    listea.append(liste_hali[elements][0])
                    listeb.append(liste_hali[elements][1])
                    listec.append(liste_hali[elements][2])
            return [listea,listeb,listec]
def pozitifse(liste):
    numbers = [-3, -2, -1]
    print ( 'denem2e2' )
    for element in numbers:
        print ( element )
        if liste[element][2] > 0:
            liste_hali = liste[element:]
            for element in range ( len ( liste_hali ) ):
                print ( liste_hali )
                print ( element )
                print ( liste_hali[element] )
                liste_hali[element][2] = f"%{ liste_hali[element][2]}"

                listea = []
                listeb = []
                listec = []
                for elements in range ( len ( liste_hali ) ):
                    print ( 'deneme11' )
                    print ( liste_hali )
                    listea.append ( liste_hali[elements][0] )
                    listeb.append ( liste_hali[elements][1] )
                    listec.append ( liste_hali[elements][2] )
            return [listea,listeb,listec]
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


def main1_1_tarih(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( url1, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print ( headersiz_data )
    print ( "________________________________" )
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[1]["Name"] ) #Customer
    # print ( headersiz_data[1]["Serial"] )
    # print ( headersiz_data[3]["Name"] ) ##eime
    # print ( headersiz_data[3]["Serial"] )

    return (headersiz_data[0]["Serial"])
def main1_1_musteri_sayisi(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( url1, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print ( headersiz_data )
    print ( "________________________________" )
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[1]["Name"] ) #Customer
    # print ( headersiz_data[1]["Serial"] )
    # print ( headersiz_data[3]["Name"] ) ##eime
    # print ( headersiz_data[3]["Serial"] )

    return (headersiz_data[1]["Serial"])
def main1_1_musteri_suresi(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( url1, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print ( headersiz_data )
    print ( "________________________________" )
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[1]["Name"] ) #Customer
    # print ( headersiz_data[1]["Serial"] )
    # print ( headersiz_data[3]["Name"] ) ##eime
    # print ( headersiz_data[3]["Serial"] )

    return (headersiz_data[3]["Serial"])
def main_1_1_yogunluk_listesi_tarihler(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( url_yogunluk, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[0]["Serial"]
def main_1_1_yogunluk_listesi(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( url_yogunluk, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )
    # print("________________________________")
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )

    return headersiz_data[4]["Serial"]  # yogunluk_listesi =
def main_2_1_saatler(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[0]["Serial"]
def main_2_1_kisi_sure_saatlik(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[2]["Serial"]
def cal_average_array(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t[1]

    avg1 = sum_num / len ( num )  # yuvarlanmamis hali
    avg = float ( ("{:.2f}".format ( round ( avg1, 2 ) )) )  ##
    return avg


def ikincisi_dogru_ise_liste_devam_etsin(num):
    list_more_than_1 = []
    for t in num:
        if t[1] == True:
            list_more_than_1.append ( t[0] )
    return list_more_than_1


def ikincisi_dogru_ise_liste_devam_etmesin(num):
    list_more_than_1 = []
    for t in num:
        if t[1] == False:
            list_more_than_1.append ( t[0] )
    return list_more_than_1


def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest


def sabah_ogle_aksam(sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi):
    if maximum ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ) == sabah_ortalmasi:
        return 'sabah'
    elif maximum ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ) == oglen_ortalmasi:
        return 'öglen'
    else:
        return 'aksam'


def max_number_array(num):
    max_sayi = float ( 0 )
    max_sayi_zaman = ""
    for t in num:
        if max_sayi <= t[1]:
            max_sayi = t[1]
            max_sayi_zaman = t[0]
    return max_sayi_zaman


yogunluk_toplam_deger = float ( 0 )

def json_isimden_listeye_5(tarih1, tarih2,magaza_no, isim, reverse=True ):
    json33 = get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
    edited_json = ((json33["Data"]))
    edited_json1 = sorted ( edited_json, key=lambda k: k.get ( isim, 0 ), reverse=reverse )
    print('kotu siralama')
    print ( edited_json1 )
    id_listesi = []
    isim_listesi = []
    degerler_listesi = []
    sayi = 0
    for area in range ( 0, 5 ):
        try:
            print('before')
            print(edited_json1[sayi][isim])
            istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json1[sayi][isim]) )*100, 2 )) )
            print ( 'After' )
            print(istenen_sayi)

            degerler_listesi.append ( istenen_sayi )
            isim_listesi.append ( edited_json1[sayi]["Name"] )
            id_listesi.append(edited_json1[sayi]['Id'])
        except Exception as e:
            print(e)
            log_info = str ( f'eksik data, {edited_json1[sayi]["Name"]}, {e}' )
            print ( log_info )
            degerler_listesi.append ( 0 )
            isim_listesi.append ( edited_json1[sayi]["Name"] )
            id_listesi.append ( edited_json1[sayi]['Id'] )

        sayi += 1
    print('output')
    return  id_listesi,isim_listesi,degerler_listesi

def yogunluk_haritasi_hesaplama_degerleri_top_5(data):  ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    print("api_datasi")
    print(data)

    top_5_area = [1, 2, 3, 4, 5]
    bottom_5_area = [1, 2, 3, 4, 5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print ( "Ss" )
        print ( area )
        try:
            yogunluk_listesi.append ( data[sayi]["DensityRatio"] )
        except Exception as e:
            log_info = str ( f'eksik data, {data[sayi]["Name"]}, {e}' )
            app_log.info ( log_info )

        sayi = sayi + 1
        print ( sayi )
    print ( yogunluk_listesi )
    yogunluk_toplam_deger = (cal_total ( yogunluk_listesi ))
    yogunluk_toplam_deger_sirali = (sorted ( yogunluk_listesi, reverse=True ))
    print ( '_________' )
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse=False ))  # reverse

    print ( yogunluk_toplam_deger_sirali )
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5]  # en kucukten en buyuge yap
    print ( top_5_liste )
    print ( bottom_5_liste )
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []

    def sayilar_listesi(siralama_sayisi, data, top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]):
                    en_buyuk = (data[sayi1]["Name"])
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )
            sayi1 = sayi1 + 1
        return (en_buyuk)

    top_5_liste_adlar.append ( sayilar_listesi ( 0, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data, top_5_liste ) )
    print ( top_5_liste_adlar )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar )
    return top_5_liste_adlar

def yogunluk_haritasi_isimine_gore_yuzde_top_5( magaza_id, tarih_ilk, tarih_son,isim,boolean ):  ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    print ( "hata017" )
    print ( data )


    # list_data = json.loads ( data )

    data = (data["Data"])
    count_ratio = float ( 0 )
    print("api_datasi")
    print(data)

    liste =  json_isimden_listeye_5(data,isim,boolean)

    return liste


def yogunluk_haritasi_hesaplama_degerleri_bottom_5(data):  ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1, 2, 3, 4, 5]
    bottom_5_area = [1, 2, 3, 4, 5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print ( "Ss" )
        print ( area)

        try:
            yogunluk_listesi.append ( data[sayi]["DensityRatio"] )
        except Exception as e:
            log_info = str ( f'eksik data, {data[sayi]["Name"]}, {e}' )
            app_log.info ( log_info )

        sayi = sayi + 1
        print ( sayi )
    print ( yogunluk_listesi )
    yogunluk_toplam_deger = (cal_total ( yogunluk_listesi ))
    yogunluk_toplam_deger_sirali = (sorted ( yogunluk_listesi, reverse=True ))
    print ( '_________' )
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse=False ))  # reverse

    print ( yogunluk_toplam_deger_sirali )
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5]  # en kucukten en buyuge yap
    print ( top_5_liste )
    print ( bottom_5_liste )
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []

    def sayilar_listesi(siralama_sayisi, data, top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:

            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]):
                    en_buyuk = (data[sayi1]["Name"])
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )
            sayi1 = sayi1 + 1
        return (en_buyuk)

    top_5_liste_adlar.append ( sayilar_listesi ( 0, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data, top_5_liste ) )
    print ( top_5_liste_adlar )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar )
    return bottom_5_liste_adlar


def main_2_3_yogunluk_haritasi_top_5(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    print("hata01")
    print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])

    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_top_5 ( headersiz_data )


def main_2_3_yogunluk_haritasi_bottom_5(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5 ( headersiz_data )


def main_2_3_yogunluk_haritasi_orani_bottom_5(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5 ( headersiz_data )


def yogunluk_haritasi_hesaplama_degerleri_bottom_5_orani(
        data):  ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1, 2, 3, 4, 5]
    bottom_5_area = [1, 2, 3, 4, 5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print ( "Ss" )
        print ( area )
        try:
            yogunluk_listesi.append ( data[sayi]["DensityRatio"] )
        except Exception as e:
            log_info = str ( f'eksik data, {data[sayi]["Name"]}, {e}' )
            app_log.info ( log_info )
        sayi = sayi + 1
        print ( sayi )
    print ( yogunluk_listesi )
    yogunluk_toplam_deger = (cal_total ( yogunluk_listesi ))
    yogunluk_toplam_deger_sirali = (sorted ( yogunluk_listesi, reverse=True ))
    print ( '_________' )
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse=False ))  # reverse

    print ( yogunluk_toplam_deger_sirali )
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5]  # en kucukten en buyuge yap
    print ( top_5_liste )
    print ( bottom_5_liste )
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    top_5_liste_adlar_tf = []
    bottom_5_liste_adlar_tf = []

    def sayilar_listesi(siralama_sayisi, data, top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]):
                    en_buyuk = (data[sayi1]["Name"])
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )

            sayi1 = sayi1 + 1
        return (en_buyuk)

    def sayilar_listesi_orani_1_den_buyuk_mu(siralama_sayisi, data, top_5_liste):
        sayi1 = 0
        buyuk_mu = False
        for area in data:

            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]) and (
                        ((data[sayi1]["DensityRatio"]) / (yogunluk_toplam_deger)) >= 0.01):
                    buyuk_mu = True
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )
            sayi1 = sayi1 + 1
        return (buyuk_mu)

    print ( "yogunluk_toplam" )
    print ( yogunluk_toplam_deger )

    top_5_liste_adlar.append ( sayilar_listesi ( 0, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data, top_5_liste ) )
    print ( top_5_liste_adlar )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar )

    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    print ( top_5_liste_adlar_tf )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar_tf )

    array = list ( zip ( bottom_5_liste_adlar, bottom_5_liste_adlar_tf ) )
    print ( 'aaa' )
    print ( array )
    liste = ikincisi_dogru_ise_liste_devam_etmesin ( array )
    print ( "listee" )
    print ( liste )

    return liste


def yogunluk_haritasi_hesaplama_degerleri_top_5_orani(data):  ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1, 2, 3, 4, 5]
    bottom_5_area = [1, 2, 3, 4, 5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print ( "Ss" )
        print ( area )
        try:
            yogunluk_listesi.append ( data[sayi]["DensityRatio"] )
        except Exception as e:
            log_info = str ( f'eksik data, {data[sayi]["Name"]}, {e}' )
            app_log.info ( log_info )
        sayi = sayi + 1
        print ( sayi )
    print ( yogunluk_listesi )
    yogunluk_toplam_deger = (cal_total ( yogunluk_listesi ))
    yogunluk_toplam_deger_sirali = (sorted ( yogunluk_listesi, reverse=True ))
    print ( '_________' )
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse=False ))  # reverse

    print ( yogunluk_toplam_deger_sirali )
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5]  # en kucukten en buyuge yap
    print ( top_5_liste )
    print ( bottom_5_liste )
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    top_5_liste_adlar_tf = []
    bottom_5_liste_adlar_tf = []

    def sayilar_listesi(siralama_sayisi, data, top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]):
                    en_buyuk = (data[sayi1]["Name"])
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )

            sayi1 = sayi1 + 1
        return (en_buyuk)

    def sayilar_listesi_orani_1_den_buyuk_mu(siralama_sayisi, data, top_5_liste):
        sayi1 = 0
        buyuk_mu = False
        for area in data:
            try:
                if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]) and (
                        ((data[sayi1]["DensityRatio"]) / (yogunluk_toplam_deger)) >= 0.01):
                    buyuk_mu = True
            except Exception as e:
                log_info = str ( f'eksik data, {data[sayi1]["Name"]}, {e}' )
                app_log.info ( log_info )
            sayi1 = sayi1 + 1
        return (buyuk_mu)

    print ( "yogunluk_toplam" )
    print ( yogunluk_toplam_deger )

    top_5_liste_adlar.append ( sayilar_listesi ( 0, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data, top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data, top_5_liste ) )
    print ( top_5_liste_adlar )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data, bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar )

    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, top_5_liste ) )
    print ( top_5_liste_adlar_tf )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu ( 1, data, bottom_5_liste ) )
    print ( bottom_5_liste_adlar_tf )

    array = list ( zip ( top_5_liste_adlar, top_5_liste_adlar_tf ) )

    liste = ikincisi_dogru_ise_liste_devam_etsin ( array )

    return liste


def main_2_5_yogunluk_haritasi_orani_bottom_5_orani(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5_orani ( headersiz_data )


def main_2_5_yogunluk_haritasi_orani_top_5_orani(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_top_5_orani ( headersiz_data )


def main_2_7_performans_tablosu_alansal(magaza_id, tarih_ilk, tarih_son,
                                        bakilan_alan):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin

    print ( "son_data_hali" )
    print ( data )

    def numOfDays(date1, date2):
        return (date2 - date1).days

    gun1 = int ( str ( tarih_ilk )[0:2] )
    ay1 = int ( str ( tarih_ilk )[3:5] )
    yil1 = int ( str ( tarih_ilk )[6:10] )
    gun2 = int ( str ( tarih_son )[0:2] )
    ay2 = int ( str ( tarih_son )[3:5] )
    yil2 = int ( str ( tarih_son )[6:10] )
    date1 = datetime.datetime ( yil1, ay1, gun1 )
    date2 = datetime.datetime ( yil2, ay2, gun2 )
    elma = (numOfDays ( date1, date2 ), "days")[0] + 1
    cikarilacak_gun = (numOfDays ( date1, date2 ), "days")[0]
    onceki_ay_son_tarih = date2 - datetime.timedelta ( days=elma )
    onceki_ay_ilk_tarih = date1 - datetime.timedelta ( days=elma )
    print ( "tarih_kontrolu" )
    print ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    print ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_son1 = str ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_ilk1 = str ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )

    data1 = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk1, tarih_son1 )
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    headersiz_data1 = (data1["Data"])
    print ( headersiz_data )
    n = 0
    print ( len ( headersiz_data ) )  # kac tane alan var
    meterSquareTotal = float ( 0 )
    densityTotal = float ( 0 )
    densityPrevTotal = float ( 0 )
    saleQuantityTotal = float ( 0 )
    prevsaleQuantityTotal = float ( 0 )
    prevsaleAmountTotal = float ( 0 )
    saleAmountTotal = float ( 0 )


    for headers in headersiz_data:
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])

        print ( headersiz_data[n]["Name"] )
        meterSquareTotal = meterSquareTotal + float ( headersiz_data[n]["Metersquare"] )
        try:
            densityTotal = (densityTotal + float ( ("{:.2f}".format ( float ( (headersiz_data[n]["Density"]) ), 2 )) ))
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        print ( "guncellendi" )
        print ( headersiz_data[n]["Name"] )

        print ( "guncellendi" )
        print ( "guncellendi" )
        print ( headersiz_data[n]["Name"] )
        try:
            densityPrevTotal = densityPrevTotal + float (
                ("{:.2f}".format ( float ( (headersiz_data1[n]["Density"]) ), 2 )) )
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        print ( "guncellendi" )



        try:
            saleQuantityTotal = saleQuantityTotal + float (
                headersiz_data[n]["AvgSaleQuantity"] )  # eksik data bunu sor
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )

        # try:
        #     densityPrevTotal = densityPrevTotal + float ( headersiz_data1[n]["Density"] ) #AvgSaleAmount
        # except Exception as e:
        #     log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
        #     app_log.info(log_info)
        #     print ( "nassiya" )

        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float ( headersiz_data1[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        try:
            saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        n += 1

    print ( meterSquareTotal )
    print ( densityTotal )
    print ( densityPrevTotal )
    print ( saleQuantityTotal )
    print ( prevsaleQuantityTotal )
    print ( prevsaleAmountTotal )
    print ( saleAmountTotal )

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float ( 0 )
    info_all = []

    n = 0

    def searching_function(bakilan_alan):
        if bakilan_alan == "PrevCount":
            print ( headersiz_data[n]["Name"] )
            try:
                a1 = float ( headersiz_data[n]["Count"] )
                a2 = float ( headersiz_data1[n]["Count"] )
                return float ( math.ceil ( ((a1 - a2) / a2) * 100 ) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                return 0

        if bakilan_alan == "PrevDwell":
            print ( "PrevDwell_degeri" )
            print ( headersiz_data[n]["Name"] )
            try:
                a1 = float ( headersiz_data[n]["Dwell"] )
                a2 = float ( headersiz_data1[n]["Dwell"] )
                print ( "PrevDwell_degeri" )
                print ( float ( math.ceil ( ((a1 - a2) / a2) * 100 ) ) )
                return float ( math.ceil ( ((a1 - a2) / a2) * 100 ) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                return 0


        if bakilan_alan == "_15s_Enterance":
            print ( "_15s_Enterance" )
            print ( headersiz_data[n]["Name"] )
            try:
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                return float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                return 0




        if bakilan_alan == "n_15s_Enterance":
            print ( "n_15s_Enterance" )
            print ( headersiz_data[n]["Name"] )
            try:
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                return 1 / float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            except:
                return 1 / 10000
        if bakilan_alan == "Dwell":
            print ( "Dwell" )
            print ( headersiz_data[n]["Name"] )
            try:
                Dwell = float ( headersiz_data[n]["Dwell"] )
                return float ( ("{:.2f}".format ( float ( (Dwell) ), 2 )) )
            except:
                return 0

        if bakilan_alan == "Count":
            try:
                return float ( headersiz_data[n]["Count"] )
            except:
                return 0
                #bosluk var datada



    TotalCount_final = searching_function ( bakilan_alan )
    if bakilan_alan == "PrevDwell":

        ( En_cok_ziyaret_edilen_sayi ) = float(-999)

    for headers in headersiz_data:
        print ( headersiz_data[n]["Name"] )
        print ( headersiz_data[n]["Id"] )
        print ( headersiz_data[n] )
        print ( "__previousData__" )
        # print ( headersiz_data1[n] )
        print ( "header uzunlugu" )
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar

        print ( "department rectangles" )
        # print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print ( "bakilan_alan" )

        # TotalCount_final = float(headersiz_data[n][bakilan_alan])
        # print(TotalCount_final)



        TotalCount_final = searching_function ( bakilan_alan )

        print ( TotalCount_final )
        print ( En_cok_ziyaret_edilen_sayi )

        if En_cok_ziyaret_edilen_sayi < TotalCount_final:
            print ( "son_denemeeeee" )

            En_cok_ziyaret_edilen_sayi = TotalCount_final
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id1 )
                En_cok_ziyaret_edilen_id2 = headersiz_data[n]["DepartmentRectangles"][1][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )

            #  x = float ( ("{:.2f}".format ( float ( (    ) ), 2 )) )

            print ( "En_cok_ziyaret_edilen_ad11" )
            print ( En_cok_ziyaret_edilen_ad )

            # yogunluk ile alakadar degisim
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data[n]["Dwell"] )
            a3 = float ( headersiz_data1[n]["Count"] )
            a4 = float ( headersiz_data1[n]["Dwell"] )

            DensityChange = math.ceil ( float ( (a1 * a2 - a3 * a4) / (a3 * a4) ) * 100 )
            DensityChange = float ( ("{:.2f}".format ( float ( (DensityChange) ), 2 )) )

            print ( "PrevDwell" )
            a1 = float ( headersiz_data[n]["Dwell"] )
            a2 = float ( headersiz_data1[n]["Dwell"] )
            PrevDwell = math.ceil ( ((a1 - a2) / a2) * 100 )
            print ( PrevDwell )

            print ( "Density111" )  # ! burayi duzelt
            print ( DensityChange )
            print ( headersiz_data[n]["Density"] )
            print ( densityTotal )
            Density = float (((float ( headersiz_data[n]["Density"] )) * (100)) / (densityTotal) )  # ! duzelt math.ceil
            print ( Density )
            print ( "DensityStoreChange" )  # duzelttin
            DensityStoreChange = Density - (float ( (((headersiz_data1[n]["Density"])) * (100)) / (densityPrevTotal) ))  # magaza ici degisimi
            DensityStoreChange = float (("{:.2f}".format ( float ( (DensityStoreChange) ), 2 )) )  # magaza ici degisimi
            print ( DensityStoreChange )

            # kisi sayisi ile alakadar degisim
            TotalCount = float ( headersiz_data[n]["TotalCount"] )
            print ( TotalCount )
            print ( 'Count' )
            Count = float ( headersiz_data[n]["Count"] )
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data1[n]["Count"] )
            PrevCount = math.ceil ( ((a1 - a2) / a2) * 100 )

            print ( "PrevCount111" )
            print ( a1 )
            print ( a2 )

            # ilgi orani
            _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
            _15s_Enterance = float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            print ( "hatali_kisim-1" )
            a1 = float ( headersiz_data[n]["CountOver15Sec"] )
            a2 = float ( headersiz_data[n]["Count"] )
            a3 = float ( headersiz_data1[n]["CountOver15Sec"] )
            a4 = float ( headersiz_data1[n]["Count"] )
            print(headersiz_data[n]["Name"])
            print("hatali_kisim")
            print(a1)
            print(a2)
            print(a3)
            print(a4)
            try:
                EntranceChange = (a1 / a2 - a3 / a4) / (a3 / a4) * 100
                EntranceChange = float ( ("{:.2f}".format ( float ( (EntranceChange) ), 2 )) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                EntranceChange = 0


            ## Ortalama sure

            try:
                Dwell = float ( headersiz_data[n]["Dwell"] )
                Dwell = float ( ("{:.2f}".format ( float ( (Dwell) ), 2 )) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                Dwell = 0


            # print("DensityChange")
            # DensityChange = (((float(headersiz_data[n]["Count"]) * float(headersiz_data[n]["Dwell"])) - (float(headersiz_data1[n]["Dwell"]) * float(headersiz_data1[n]["Count"]))) / (float(headersiz_data1[n]["Count"]) * float(headersiz_data1[n]["Dwell"]))) * 100
            # DensityChange = float ( ("{:.2f}".format ( float ( ( DensityChange  ) ), 2 )) )
            # print(DensityChange)

            # _______________ m2



            try:
                a1 = float ( headersiz_data[n]["Metersquare"] )
                a2 = float ( meterSquareTotal )
                a3 = float ( headersiz_data1[n]["SketchMetersquare"] )
                SketchMetersquare = ((a1 / a2) * a3)
                SketchMetersquare = float ( ("{:.2f}".format ( float ( (SketchMetersquare) ), 2 )) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                SketchMetersquare = 0

            try:
                a1 = float ( headersiz_data[n]["Metersquare"] )
                a2 = float ( meterSquareTotal )
                Metersquare = ((a1 * 100) / a2)
                Metersquare = float ( ("{:.2f}".format ( float ( (Metersquare) ), 2 )) )
            except Exception as e:
                log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                Metersquare = 0



            print ( "SaleAmount" )
            # SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            # print(SaleAmount)
            print ( "ConversionRate" )
            # ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            # print(ConversionRate) # key error veriyor bunu hallet
            print ( "ConversionChange" )  # emin olamadim bak
            print ( "Enterance_15s" )
            Enterance_15s = (float ( headersiz_data[n]["CountOver15Sec"] ) / float ( headersiz_data[n]["Count"] )) * 100
            print ( Enterance_15s )
            print ( "EntranceChange" )  # try except koydur hepsinde yok
            # EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            # print(EntranceChange)

        n += 1
        print ( "/n 1" )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    # print(headersiz_data)
    # return headersiz_data
    print ( "\n______ Yogunluk" )
    # print("densityTotal _toplam yogunluk")
    # print(densityTotal)
    # print ( "densityPrevTotal _toplam_yogunluk_pre" )
    # print(densityPrevTotal)

    print ( "Density __ magaza_ici_degisim" )
    print ( Density )

    print ( "DensityStoreChange _magaza_ici_degisim" )
    print ( DensityStoreChange )  # Magaza ici degisim

    print ( "DensityChange  kisi_sure_degisimi" )
    print ( DensityChange )

    print ( "\n______ kisi sayisi" )
    print ( 'Count_ kisi _sayisi_gunluk_ortalama' )
    print ( Count )
    print ( 'TotalCount _kisi_sayisi_toplam' )  # kisi_sayisi == toplam
    print ( TotalCount )
    print ( "PrevCount kisi _sayisi_degisim" )
    print ( PrevCount )

    # print ( "DensityChange" )
    # print ( DensityChange )

    print ( "\n______ ortalma_sure" )
    print ( "Dwell __ ortalama_sure_saniye" )
    print ( Dwell )
    print ( "PrevDwell _ortalama_sure_degisim" )
    print ( PrevDwell )

    print ( "\n______ ilgi_orani" )
    print ( "_15s_Enterance  ilgi_orani _15s/giren" )
    print ( _15s_Enterance )
    print ( "EntranceChange ilgi_orani_degisim" )
    print ( EntranceChange )
    print ( "bitti" )

    print ( "\n______ m2_orani" )

    print ( "SketchMetersquare __ metrekare" )
    print ( SketchMetersquare )
    print ( "Metersquare  __metrekare orani" )
    print ( Metersquare )

    try:
        info_all = [
            [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi, En_cok_ziyaret_edilen_id1,
             En_cok_ziyaret_edilen_id2],
            [Density, DensityStoreChange, DensityChange, Count, TotalCount, PrevCount, Dwell, PrevDwell, _15s_Enterance,
             EntranceChange, SketchMetersquare, Metersquare]]
    except:
        info_all = [
            [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi, En_cok_ziyaret_edilen_id1],
            [Density, DensityStoreChange, DensityChange, Count, TotalCount, PrevCount, Dwell, PrevDwell, _15s_Enterance,
             EntranceChange, SketchMetersquare, Metersquare]]

    return info_all


def main_2_7_performans_tablosu_isimsel(magaza_id, tarih_ilk, tarih_son,isim):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin

    def numOfDays(date1, date2):
        return (date2 - date1).days

    gun1 = int ( str ( tarih_ilk )[0:2] )
    ay1 = int ( str ( tarih_ilk )[3:5] )
    yil1 = int ( str ( tarih_ilk )[6:10] )
    gun2 = int ( str ( tarih_son )[0:2] )
    ay2 = int ( str ( tarih_son )[3:5] )
    yil2 = int ( str ( tarih_son )[6:10] )
    date1 = datetime.datetime ( yil1, ay1, gun1 )
    date2 = datetime.datetime ( yil2, ay2, gun2 )
    elma = (numOfDays ( date1, date2 ), "days")[0] + 1
    onceki_ay_son_tarih = date2 - datetime.timedelta ( days=elma )
    onceki_ay_ilk_tarih = date1 - datetime.timedelta ( days=elma )
    print ( "tarih_kontrolu" )
    print ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    print ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_son1 = str ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_ilk1 = str ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )

    data1 = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk1, tarih_son1 )
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    headersiz_data1 = (data1["Data"])
    print ( headersiz_data )
    n = 0
    print ( len ( headersiz_data ) )  # kac tane alan var
    meterSquareTotal = float ( 0 )
    densityTotal = float ( 0 )
    densityPrevTotal = float ( 0 )
    saleQuantityTotal = float ( 0 )
    prevsaleQuantityTotal = float ( 0 )
    prevsaleAmountTotal = float ( 0 )
    saleAmountTotal = float ( 0 )
    kategori_sirasi = int ( 1 )

    for headers in headersiz_data:
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float ( headersiz_data[n]["Metersquare"] )
        print ( headersiz_data[n]["Name"] )
        try:
            densityTotal = (densityTotal + float ( ("{:.2f}".format ( float ( (headersiz_data[n]["Density"]) ), 2 )) ))
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        print ( "guncellendi" )
        print ( headersiz_data[n]["Name"] )
        try:
            densityPrevTotal = densityPrevTotal + float (
                ("{:.2f}".format ( float ( (headersiz_data1[n]["Density"]) ), 2 )) )
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        print ( "guncellendi" )
        try:
            saleQuantityTotal = saleQuantityTotal + float (
                headersiz_data[n]["AvgSaleQuantity"] )  # eksik data bunu sor
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )

        # try:
        #     densityPrevTotal = densityPrevTotal + float ( headersiz_data1[n]["Density"] ) #AvgSaleAmount
        # except Exception as e:
        #     log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
        #     app_log.info(log_info)
        #     print ( "nassiya" )

        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float ( headersiz_data1[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        try:
            saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        n += 1

    print ( meterSquareTotal )
    print ( densityTotal )
    print ( densityPrevTotal )
    print ( saleQuantityTotal )
    print ( prevsaleQuantityTotal )
    print ( prevsaleAmountTotal )
    print ( saleAmountTotal )

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float ( 0 )
    info_all = []

    n = 0
    for headers in headersiz_data:

        def searching_function(bakilan_alan, n):
            if bakilan_alan == "PrevCount":
                a1 = float ( headersiz_data[n]["Count"] )
                a2 = float ( headersiz_data1[n]["Count"] )
                return float ( math.ceil ( ((a1 - a2) / a2) * 100 ) )
            if bakilan_alan == "PrevDwell":
                a1 = float ( headersiz_data[n]["Dwell"] )
                a2 = float ( headersiz_data1[n]["Dwell"] )
                return float ( math.ceil ( ((a1 - a2) / a2) * 100 ) )
            if bakilan_alan == "_15s_Enterance":
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                return float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            if bakilan_alan == "n_15s_Enterance":
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                try:
                    return 1 / float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
                except:
                    return 1 / 10000
            if bakilan_alan == "Dwell":
                Dwell = float ( headersiz_data[n]["Dwell"] )
                return float ( ("{:.2f}".format ( float ( (Dwell) ), 2 )) )
            if bakilan_alan == "Count":
                return float ( headersiz_data[n]["Count"] )
            if bakilan_alan == "Density":
                try:
                    return float ( ((float ( headersiz_data[n]["Density"] )) * (100)) / (densityTotal) )
                except:
                    return 0

        if headersiz_data[n]["Name"] == isim:
            print ( "yojooo" )
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]

            TotalCount_final = searching_function ( "Density", n )
            print ( "geriplik" )
            print ( TotalCount_final )
            hesap = 0
            for headers in headersiz_data:
                if searching_function ( "Density", hesap ) > TotalCount_final:
                    print("buyuk olan deger")
                    print(searching_function ( "Density", hesap ))
                    kategori_sirasi += 1
                hesap += 1
        final_kategori_sirasi1 = kategori_sirasi

        n += 1
        print ( "/n 1" )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    try:
        info_all = [En_cok_ziyaret_edilen_ad, final_kategori_sirasi1]
    except:
        info_all = [En_cok_ziyaret_edilen_ad, final_kategori_sirasi1]

    return info_all


def main_2_7_performans_tablosu_double_isim(magaza_id, tarih_ilk, tarih_son,
                                            alan_ismi):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin

    def numOfDays(date1, date2):
        return (date2 - date1).days

    gun1 = int ( str ( tarih_ilk )[0:2] )
    ay1 = int ( str ( tarih_ilk )[3:5] )
    yil1 = int ( str ( tarih_ilk )[6:10] )
    gun2 = int ( str ( tarih_son )[0:2] )
    ay2 = int ( str ( tarih_son )[3:5] )
    yil2 = int ( str ( tarih_son )[6:10] )
    date1 = datetime.datetime ( yil1, ay1, gun1 )
    date2 = datetime.datetime ( yil2, ay2, gun2 )
    elma = (numOfDays ( date1, date2 ), "days")[0] + 1
    onceki_ay_son_tarih = date2 - datetime.timedelta ( days=elma )
    onceki_ay_ilk_tarih = date1 - datetime.timedelta ( days=elma )
    print ( "tarih_kontrolu" )
    print ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    print ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_son1 = str ( onceki_ay_son_tarih.strftime ( '%d/%m/%Y' ) )
    tarih_ilk1 = str ( onceki_ay_ilk_tarih.strftime ( '%d/%m/%Y' ) )
    print("diger_tarihler")
    print(tarih_ilk1)
    print(tarih_son1)

    data1 = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk1, tarih_son1 )
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    headersiz_data1 = (data1["Data"])
    print ( headersiz_data )
    n = 0
    print ( len ( headersiz_data ) )  # kac tane alan var
    meterSquareTotal = float ( 0 )
    densityTotal = float ( 0 )
    densityPrevTotal = float ( 0 )
    saleQuantityTotal = float ( 0 )
    prevsaleQuantityTotal = float ( 0 )
    prevsaleAmountTotal = float ( 0 )
    saleAmountTotal = float ( 0 )

    for headers in headersiz_data:
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float ( headersiz_data[n]["Metersquare"] )
        print ( headersiz_data[n]["Name"] )



        try:
            densityTotal = (densityTotal + float ( ("{:.2f}".format ( float ( (headersiz_data[n]["Density"]) ), 2 )) ))
            print ( "guncellendi" )
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        try:
            densityPrevTotal = densityPrevTotal + float (
                ("{:.2f}".format ( float ( (headersiz_data1[n]["Density"]) ), 2 )) )
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )

        try:
            saleQuantityTotal = saleQuantityTotal + float (
                headersiz_data[n]["AvgSaleQuantity"] )  # eksik data bunu sor
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        # try:
        #     densityPrevTotal = densityPrevTotal + float ( headersiz_data1[n]["Density"] ) #AvgSaleAmount
        # except Exception as e:
        #     log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
        #     app_log.info(log_info)
        #     print ( "nassiya" )

        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float ( headersiz_data1[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        try:
            saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
            print ( "nassiya1" )

        n += 1

    print ( meterSquareTotal )
    print ( densityTotal )
    print ( densityPrevTotal )
    print ( saleQuantityTotal )
    print ( prevsaleQuantityTotal )
    print ( prevsaleAmountTotal )
    print ( saleAmountTotal )

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float ( 0 )
    info_all = []

    n = 0
    for headers in headersiz_data:
        print ( headersiz_data[n]["Name"] )
        print ( headersiz_data[n]["Id"] )
        print ( headersiz_data[n] )
        print ( "__previousData__" )
        # print ( headersiz_data1[n] )
        print ( "header uzunlugu" )
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar

        print ( "department rectangles" )
        # print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print ( "TotalCount" )
        try:
            TotalCount_final = float ( headersiz_data[n]["TotalCount"] )
            print ( TotalCount_final )
        except Exception as e:
            log_info = str ( f'eksik data, {headersiz_data[n]["Name"]}, {e}' )
            app_log.info ( log_info )

        print("niye_erro")
        print(headersiz_data[n]["Name"])
        print(alan_ismi)
        if headersiz_data[n]["Name"] == alan_ismi:
            print ( "son_denemeeeee12133" )
            print(headersiz_data[n])

            En_cok_ziyaret_edilen_sayi = TotalCount_final
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id1 )
                En_cok_ziyaret_edilen_id2 = headersiz_data[n]["DepartmentRectangles"][1][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )

            #  x = float ( ("{:.2f}".format ( float ( (    ) ), 2 )) )

            print ( "En_cok_ziyaret_edilen_ad11" )
            print ( En_cok_ziyaret_edilen_ad )

            # yogunluk ile alakadar degisim
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data[n]["Dwell"] )
            a3 = float ( headersiz_data1[n]["Count"] )
            a4 = float ( headersiz_data1[n]["Dwell"] )

            DensityChange = math.ceil ( float ( (a1 * a2 - a3 * a4) / (a3 * a4) ) * 100 )
            DensityChange = float ( ("{:.2f}".format ( float ( (DensityChange) ), 2 )) )

            print ( "PrevDwell" )
            a1 = float ( headersiz_data[n]["Dwell"] )
            a2 = float ( headersiz_data1[n]["Dwell"] )
            PrevDwell = math.ceil ( ((a1 - a2) / a2) * 100 )
            print ( PrevDwell )

            print ( "Density111" )  # ! burayi duzelt
            print ( DensityChange )
            print ( headersiz_data[n]["Density"] )
            print ( densityTotal )
            Density = float (((float ( headersiz_data[n]["Density"] )) * (100)) / (densityTotal) )  # ! duzelt math.ceil
            Density = float ( ("{:.2f}".format ( float ( (Density) ), 2 )) )
            print ( Density )
            print ( "DensityStoreChange" )  # duzelttin
            DensityStoreChange = Density - (
                float ( (((headersiz_data1[n]["Density"])) * (100)) / (densityPrevTotal) ))  # magaza ici degisimi
            DensityStoreChange = float (
                ("{:.2f}".format ( float ( (DensityStoreChange) ), 2 )) )  # magaza ici degisimi
            print ( DensityStoreChange )

            # kisi sayisi ile alakadar degisim
            TotalCount = float ( headersiz_data[n]["TotalCount"] )
            print ( TotalCount )
            print ( 'Count' )
            Count = float ( headersiz_data[n]["Count"] )
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data1[n]["Count"] )
            PrevCount = math.ceil ( ((a1 - a2) / a2) * 100 )

            print ( "PrevCount111" )
            print ( a1 )
            print ( a2 )

            # ilgi orani
            _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
            _15s_Enterance = float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            a1 = float ( headersiz_data[n]["CountOver15Sec"] )
            a2 = float ( headersiz_data[n]["Count"] )
            a3 = float ( headersiz_data1[n]["CountOver15Sec"] )
            a4 = float ( headersiz_data1[n]["Count"] )
            EntranceChange = (a1 / a2 - a3 / a4) / (a3 / a4) * 100
            EntranceChange = float ( ("{:.2f}".format ( float ( (EntranceChange) ), 2 )) )

            ## Ortalama sure
            Dwell = float ( headersiz_data[n]["Dwell"] )
            Dwell = float ( ("{:.2f}".format ( float ( (Dwell) ), 2 )) )

            # print("DensityChange")
            # DensityChange = (((float(headersiz_data[n]["Count"]) * float(headersiz_data[n]["Dwell"])) - (float(headersiz_data1[n]["Dwell"]) * float(headersiz_data1[n]["Count"]))) / (float(headersiz_data1[n]["Count"]) * float(headersiz_data1[n]["Dwell"]))) * 100
            # DensityChange = float ( ("{:.2f}".format ( float ( ( DensityChange  ) ), 2 )) )
            # print(DensityChange)

            # _______________ m2

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )
            try:
                a3 = float ( headersiz_data1[n]["SketchMetersquare"] )
            except Exception as e:
                log_info = str ( f'eksik SketchMetersquare data, {headersiz_data[n]["Name"]}, {e}' )
                app_log.info ( log_info )
                a3 = 1


            SketchMetersquare = ((a1 / a2) * a3)
            SketchMetersquare = float ( ("{:.2f}".format ( float ( (SketchMetersquare) ), 2 )) )

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )

            Metersquare = ((a1 * 100) / a2)
            Metersquare = float ( ("{:.2f}".format ( float ( (Metersquare) ), 2 )) )

            print ( "SaleAmount" )
            # SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            # print(SaleAmount)
            print ( "ConversionRate" )
            # ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            # print(ConversionRate) # key error veriyor bunu hallet
            print ( "ConversionChange" )  # emin olamadim bak
            print ( "Enterance_15s" )
            Enterance_15s = (float ( headersiz_data[n]["CountOver15Sec"] ) / float ( headersiz_data[n]["Count"] )) * 100
            print ( Enterance_15s )
            print ( "EntranceChange" )  # try except koydur hepsinde yok
            # EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            # print(EntranceChange)

        n += 1
        print ( "/n 1" )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    # print(headersiz_data)
    # return headersiz_data
    print ( "\n______ Yogunluk" )
    # print("densityTotal _toplam yogunluk")
    # print(densityTotal)
    # print ( "densityPrevTotal _toplam_yogunluk_pre" )
    # print(densityPrevTotal)

    print ( "Density __ magaza_ici_degisim" )
    print ( Density )

    print ( "DensityStoreChange _magaza_ici_degisim" )
    print ( DensityStoreChange )  # Magaza ici degisim

    print ( "DensityChange  kisi_sure_degisimi" )
    print ( DensityChange )

    print ( "\n______ kisi sayisi" )
    print ( 'Count_ kisi _sayisi_gunluk_ortalama' )
    print ( Count )
    print ( 'TotalCount _kisi_sayisi_toplam' )  # kisi_sayisi == toplam
    print ( TotalCount )
    print ( "PrevCount kisi _sayisi_degisim" )
    print ( PrevCount )

    # print ( "DensityChange" )
    # print ( DensityChange )

    print ( "\n______ ortalma_sure" )
    print ( "Dwell __ ortalama_sure_saniye" )
    print ( Dwell )
    print ( "PrevDwell _ortalama_sure_degisim" )
    print ( PrevDwell )

    print ( "\n______ ilgi_orani" )
    print ( "_15s_Enterance  ilgi_orani _15s/giren" )
    print ( _15s_Enterance )
    print ( "EntranceChange ilgi_orani_degisim" )
    print ( EntranceChange )
    print ( "bitti" )

    print ( "\n______ m2_orani" )

    print ( "SketchMetersquare __ metrekare" )
    print ( SketchMetersquare )
    print ( "Metersquare  __metrekare orani" )
    print ( Metersquare )

    try:
        info_all = [
            [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi, En_cok_ziyaret_edilen_id1,
             En_cok_ziyaret_edilen_id2],
            [Density, DensityStoreChange, DensityChange, Count, TotalCount, PrevCount, Dwell, PrevDwell, _15s_Enterance,
             EntranceChange, SketchMetersquare, Metersquare]]
    except:
        info_all = [[En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi],
                    [Density, DensityStoreChange, DensityChange, Count, TotalCount, PrevCount, Dwell, PrevDwell,
                     _15s_Enterance, EntranceChange, SketchMetersquare, Metersquare]]

    return info_all


def main_2_7_performans_tablosu(magaza_id, tarih_ilk, tarih_son):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )
    n = 0
    print ( len ( headersiz_data ) )  # kac tane alan var
    meterSquareTotal = float ( 0 )
    densityTotal = float ( 0 )
    densityPrevTotal = float ( 0 )
    saleQuantityTotal = float ( 0 )
    prevsaleQuantityTotal = float ( 0 )
    prevsaleAmountTotal = float ( 0 )
    saleAmountTotal = float ( 0 )

    for headers in headersiz_data:
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float ( headersiz_data[n]["Metersquare"] )
        densityTotal = densityTotal + float ( headersiz_data[n]["Density"] )
        densityPrevTotal = densityPrevTotal + float ( headersiz_data[n]["DepartmentRectangles"][0]["Density"] )
        try:
            saleQuantityTotal = saleQuantityTotal + float (
                headersiz_data[n]["AvgSaleQuantity"] )  # eksik data bunu sor
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )


        try:
            densityPrevTotal = densityPrevTotal + float (
                headersiz_data[n]["DepartmentRectangles"][0]["Density"] )  ## hatali
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
        print ( "nassiya" )

        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float (
                headersiz_data[n]["DepartmentRectangles"][0]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
            app_log.info ( log_info )
        print ( "nassiya1" )

        saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )

        n += 1

    print ( meterSquareTotal )
    print ( densityTotal )
    print ( densityPrevTotal )
    print ( saleQuantityTotal )
    print ( prevsaleQuantityTotal )
    print ( prevsaleAmountTotal )
    print ( saleAmountTotal )

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float ( 0 )
    info_all = []

    n = 0
    for headers in headersiz_data:
        print ( headersiz_data[n] )
        print ( "header uzunlugu" )
        print ( len ( headersiz_data[n] ) )  # alanlarin uzunlugu ne kadar
        print ( headersiz_data[n]["Name"] )
        print ( headersiz_data[n]["Id"] )
        print ( "department rectangles" )
        # print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print ( "TotalCount" )
        TotalCount = float ( headersiz_data[n]["TotalCount"] )
        print ( TotalCount )
        if En_cok_ziyaret_edilen_sayi < TotalCount:
            print ( "son_denemeeeee" )

            En_cok_ziyaret_edilen_sayi = TotalCount
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id1 )
                En_cok_ziyaret_edilen_id2 = headersiz_data[n]["DepartmentRectangles"][1][
                    "Id"]  # HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )


            print ( "En_cok_ziyaret_edilen_ad11" )
            print ( En_cok_ziyaret_edilen_ad )

            print ( "Density" )
            Density = float ( (((headersiz_data[n]["Density"])) * (100)) / (densityTotal) )
            print ( Density )
            print ( "DensityStoreChange" )  # duzelttin
            DensityStoreChange = Density - (
                float ( (((headersiz_data[n]["DepartmentRectangles"][0]["Density"])) * (100)) / (densityPrevTotal) ))
            print ( DensityStoreChange )
            print ( "DensityChange" )
            DensityChange = (((float ( headersiz_data[n]["Count"] ) * float ( headersiz_data[n]["Dwell"] )) - (
                        float ( headersiz_data[n]["DepartmentRectangles"][0]["Dwell"] ) * float (
                    headersiz_data[n]["DepartmentRectangles"][0]["Count"] ))) / (
                                         float ( headersiz_data[n]["DepartmentRectangles"][0]["Count"] ) * float (
                                     headersiz_data[n]["DepartmentRectangles"][0]["Dwell"] ))) * 100
            print ( DensityChange )

            print ( "PrevCount" )
            PrevCount = ((float ( headersiz_data[n]["Count"] ) - float (
                headersiz_data[n]["DepartmentRectangles"][0]["Count"] )) / float (
                headersiz_data[n]["DepartmentRectangles"][0]["Count"] )) * 100
            print ( PrevCount )
            print ( "PrevDwell" )
            PrevDwell = ((float ( headersiz_data[n]["Dwell"] ) - float (
                headersiz_data[n]["DepartmentRectangles"][0]["Dwell"] )) / float (
                headersiz_data[n]["DepartmentRectangles"][0]["Dwell"] )) * 100
            print ( PrevDwell )
            print ( "SaleAmount" )
            # SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            # print(SaleAmount)
            print ( "ConversionRate" )
            # ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            # print(ConversionRate) # key error veriyor bunu hallet
            print ( "ConversionChange" )  # emin olamadim bak
            print ( "Enterance_15s" )
            Enterance_15s = (float ( headersiz_data[n]["CountOver15Sec"] ) / float ( headersiz_data[n]["Count"] )) * 100
            print ( Enterance_15s )
            print ( "EntranceChange" )  # try except koydur hepsinde yok
            # EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            # print(EntranceChange)

        n += 1
        print ( "/n 1" )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    try:
        info_all = [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi,
                    En_cok_ziyaret_edilen_id1, En_cok_ziyaret_edilen_id2]
    except:
        info_all = [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi]

    # print(headersiz_data)
    # return headersiz_data
    return info_all


def main_2_8_ozel_alan(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )

    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return headersiz_data

def giren_kisi_sayisi_hepsi(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8_updated_saatlik, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )
    print("satis_miktari_data")

    # list_data = json.loads ( data )
    headersiz_data = (data["Data"])
    print ( headersiz_data )
    print ( "satis_miktari_data" )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data


def main_2_8_satis_miktari(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8_updated, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )
    print("satis_miktari_data")

    # list_data = json.loads ( data )
    headersiz_data = (data["Data"])
    print ( headersiz_data )
    print ( "satis_miktari_data" )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[4]["Serial"]


def main_2_8_saatler_gunluk(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[0]["Serial"]


def main_2_8_kisi_miktari(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )
    headersiz_data = (data["Data"])
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[1]["Serial"]


def main_2_8_kisi_sure(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )
    print ( "_________main_2_8_kisi_miktari" )
    headersiz_data = (data["Data"])
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return (headersiz_data[3]["Serial"])


def findDay(date):
    born = datetime.datetime.strptime ( date, "%d/%m/%Y" ).weekday ()
    return (calendar.day_name[born])


def gunleri_classifiye_et(gunler):
    hafta_sonu_degerleri = []
    hafta_ici_degerleri = []
    for gun in gunler:
        if (findDay ( gun ) == "Sunday") or (findDay ( gun ) == "Saturday"):
            # print(gun)
            index = gunler.index ( gun )  # sifirdan basliyor
            # print ( 'The index of e:', index )
            # print("bugun sunday")
            hafta_sonu_degerleri.append ( index )
        else:
            # print(gun)
            index = gunler.index ( gun )  # sifirdan basliyor
            # print ( 'The index of e:', index )
            hafta_ici_degerleri.append ( index )
    return hafta_ici_degerleri, hafta_sonu_degerleri


def hafta_ici_hafta_sonu_ortalamalar(hafta_ici_degerleri, hafta_sonu_degerleri, gunler_ve_musteri):
    hafta_ici_ortalama_listesi = []
    hafta_sonu_ortalama_listesi = []
    for hafta_ici_degerler in hafta_ici_degerleri:
        # print(gunler_ve_musteri[hafta_ici_degerler])
        hafta_ici_ortalama_listesi.append ( gunler_ve_musteri[hafta_ici_degerler] )

    hafta_ici_ortalama = cal_average ( hafta_ici_ortalama_listesi )
    # print(hafta_ici_ortalama)
    for hafta_sonu_degerler in hafta_sonu_degerleri:
        # print ( gunler_ve_musteri[hafta_sonu_degerler] )
        hafta_sonu_ortalama_listesi.append ( gunler_ve_musteri[hafta_sonu_degerler] )
    hafta_sonu_ortalama = cal_average ( hafta_sonu_ortalama_listesi )
    # print ( hafta_sonu_ortalama )
    return (hafta_ici_ortalama, hafta_sonu_ortalama)


def hafta_ici_hafta_sonu_oran_karsilastirmasi(hafta_ici_ortalama, hafta_sonu_ortalama):
    # print(hafta_sonu_ortalama / hafta_ici_ortalama)
    try:
        return ("{:.2f}".format (
            round ( (hafta_sonu_ortalama / hafta_ici_ortalama), 2 ) ))  # en yakin ikinci basamaga yuvarliyor
    except:
        return 0


def hafta_ici_hafta_sonu_buyukluk_karsilastirmasi(hafta_ici_ortalama, hafta_sonu_ortalama):
    if hafta_sonu_ortalama > hafta_ici_ortalama:
        return "artmaktadır."
    elif hafta_sonu_ortalama < hafta_ici_ortalama:
        return "azalmaktadır."
    elif hafta_sonu_ortalama > hafta_ici_ortalama:
        return "hafta içi ile ortalamada günlük olarak aynı kalmaktadır."


def gunluk_ortalama_sure_2_8(gunler_ve_sure):  ##tum gunluk sureleri topla gunluk sure sayisina bol
    global gunluk_ortalama_sure  # sundan bir emin ol
    toplam_deger = float ( 0 )
    for gunler in gunler_ve_sure:
        toplam_deger = toplam_deger + gunler
    return ("{:.2f}".format ( round ( toplam_deger / (len ( gunler_ve_sure )), 2 ) ))


# gunler = main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son)
# gunler_ve_musteri = main_2_8_kisi_miktari(4777,tarih_ilk , tarih_son)
# gunler_ve_sure = main_2_8_kisi_sure(4777,tarih_ilk , tarih_son)
# print(gunluk_ortalama_sure_2_8(gunler_ve_sure))
# print("bababa")
# print(gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son)))
# print(hafta_ici_hafta_sonu_ortalamalar(gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son))[0],gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son))[1],main_2_8_kisi_miktari(4777,tarih_ilk , tarih_son)))
# print(hafta_ici_hafta_sonu_oran_karsilastirmasi(1760.6923076923076, 1796.25))
# print(hafta_ici_hafta_sonu_buyukluk_karsilastirmasi(1760.6923076923076,1796.25))

def saatler_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[0]["Serial"]


def toplam_kisi_sure_saatlik_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[2]["Serial"]


def saat_sure_saatlik_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[3]["Serial"]


def kisi_sure_saatlik_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( "bakbakbak" )
    print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[1]["Serial"]


# kisi_sure_saatlik_liste_2_8_ = (kisi_sure_saatlik_2_8_(4777,tarih_ilk , tarih_son))
# #lilil = (saatler_2_8_(4777,tarih_ilk , tarih_son))
# #lilil1 = (toplam_kisi_sure_saatlik_2_8_(4777,tarih_ilk , tarih_son))
# saat_sure_2_8 = saat_sure_saatlik_2_8_(4777,tarih_ilk , tarih_son)
#
# #sure corrolated olabilir #sure sabit kalabilir #sure corralated olmayabilir
#
# print(cal_average(saat_sure_2_8))
# print("sss")
# print(saat_sure_2_8) #sure
# # print(lilil)
# # print(lilil1)
# # array = list ( zip ( lilil, lilil1 ) )
# # elma = max_number_array ( array )
# print("ornekk")
#
#
# r_degeri = (pearsonr(kisi_sure_saatlik_liste_2_8_,saat_sure_2_8))

def korelasyon_orani(r_degeri):
    if r_degeri >= 0:
        if 0.85 <= r_degeri <= 1:
            return ("pozitif güçlü korelasyon")
        if 0.5 <= r_degeri <= 0.85:
            return ("pozitif orta korelasyon")
        if 0.1 <= r_degeri <= 0.5:
            return ("pozitif zayıf korelasyon")
        if 0 <= r_degeri <= 0.1:
            return ("pozitif çok zayıf korelasyon")
    else:
        if -0.85 >= r_degeri >= -1:
            return ("negatif güçlü korelasyon")
        if -0.5 >= r_degeri >= -0.85:
            return ("negatif orta korelasyon")
        if -0.1 >= r_degeri >= -0.5:
            return ("negatif zayıf korelasyon")
        if -0 >= r_degeri >= -0.1:
            return ("negatif çok zayıf korelasyon")


# print(korelasyon_orani(r_degeri[0]))

# main_2_8_ozel_alan(4777,tarih_ilk , tarih_son)

def yogunluk_listesi_tarihler_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[0]["Serial"]


def yogunluk_listesi_2_8_(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( yogunluk_haritasi_2_8, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    # print(headersiz_data)
    # print("________________________________")
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )

    return headersiz_data[4]["Serial"]  # yogunluk_listesi =


# yogunluk_tarihleri_2_8 = (yogunluk_listesi_tarihler_2_8_(4777,tarih_ilk , tarih_son))
# yougunluk_miktarlari_2_8 = (yogunluk_listesi_2_8_(4777,tarih_ilk , tarih_son))
# array_yogunluk_2_8 = list ( zip ( yogunluk_tarihleri_2_8, yougunluk_miktarlari_2_8 ) )
# print ( array_yogunluk_2_8 )
# print ( cal_average_density_arrray ( array_yogunluk_2_8 ) )
# print ( bigger_than_average_arrray ( array_yogunluk_2_8 ) )
# ortalamanin_ustundeki_yogunluklar_2_8 = bigger_than_average_arrray ( array_yogunluk_2_8 )
# print("bak____")
# print(ortalamanin_ustundeki_yogunluklar_2_8)
# yogunlugu_fazla_olan_tarihler_2_8 = (gunleri_classifiye_et(ortalamanin_ustundeki_yogunluklar_2_8))

def hafta_ici_hafta_sonu_oranlari(hafta_ici, hafta_sonu):
    if len ( hafta_ici ) == len ( hafta_sonu ):
        return (
            f"Yoğunluğu ortalamanın üstünde olan günler hafta içinde ve hafta sonunda aynıdır. Miktarları {len ( hafta_sonu )} olarak ortaya çıkmıştır.")
    if len ( hafta_ici ) > len ( hafta_sonu ):
        return (
            f"Yoğunluğu ortalamanın üstünde olan günler hafta içinde daha fazladır miktarları sırasıyla {len ( hafta_sonu )} ve {len ( hafta_ici )} olarak ortaya çıkmıştır.")
    if len ( hafta_sonu ) > len ( hafta_ici ):
        return (
            f"Yoğunluğu ortalamanın üstünde olan günler hafta sonunda daha fazladır ve miktarları sırasıyla {len ( hafta_sonu )} ve {len ( hafta_ici )} olarak ortaya çıkmıştır.")


# hafta_ici_hafta_sonu_oranlari(yogunlugu_fazla_olan_tarihler_2_8[0],yogunlugu_fazla_olan_tarihler_2_8[1])
def main_2_8_edinme_hunisi(huni_id, tarih_ilk, tarih_son):  # degeerleri 3s 10s 15s
    data = get_performancetable ( edinme_hunisi_url, huni_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )
    print ( "_________ edinme hunisii" )
    headersiz_data = (data["Data"])
    saniye_3 = headersiz_data[0]
    saniye_10 = headersiz_data[1]
    saniye_15 = headersiz_data[2]

    saniye_3_yuzde = float ( 100 )
    saniye_10_yuzde = round ( float ( headersiz_data[1] ) / float ( headersiz_data[0] ) * 100 )
    saniye_15_yuzde = round ( float ( headersiz_data[2] ) / float ( headersiz_data[0] ) * 100 )

    saniye_liste = [saniye_3, saniye_10, saniye_15]
    print ( saniye_liste )
    yuzde_liste = [saniye_3_yuzde, saniye_10_yuzde, saniye_15_yuzde]
    print ( yuzde_liste )
    array = list ( zip ( saniye_liste, yuzde_liste ) )

    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return array

def store_sure_2_2(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( store_sure_api, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin

    try:
        print ( data )

        # list_data = json.loads ( data )

        headersiz_data = (data["Data"])
        # print(headersiz_data)
        # print("________________________________")
        # print(headersiz_data[0]["Name"]) # Labels tarih
        # print ( headersiz_data[0]["Serial"] )
        # print ( headersiz_data[4]["Name"] )  # Labels tarih
        print("tarihler")
        print ( headersiz_data[1]["Serial"] )
        print ( "Over15SecCount-15 saniyeyi asan" )
        print ( headersiz_data[2]["Serial"] )
        print ( "Over15SecDwell- 15 sn üzeri geçiren ortalama süre" )
        print ( headersiz_data[3]["Serial"] )
        print ( "Over90SecCount- 3 dk aşan kişi" )
        print ( headersiz_data[4]["Serial"] )
        print ( "TotalCount" )
        print ( headersiz_data[5]["Serial"] )
        print ( "AvgDwell - Ortalama bekleme süresi(sn)" )
        print ( headersiz_data[6]["Serial"] )
        final_list = []
        for element in range(len(headersiz_data[1]["Serial"])):
            print(element)
            eklenecek_element = []
            eklenecek_element.append ( headersiz_data[1]["Serial"][element] )
            eklenecek_element.append ( str(headersiz_data[2]["Serial"][element]) )
            eklenecek_element.append ( str(headersiz_data[3]["Serial"][element]) )
            eklenecek_element.append ( str(headersiz_data[4]["Serial"][element]) )
            eklenecek_element.append ( str(headersiz_data[6]["Serial"][element]) )
            final_list.append(eklenecek_element)
        print("final_list_bu")
        print(final_list)



        return final_list  # yogunluk_listesi =
    except:
        data = [
            [1, 'hatali',"hatali","hatali","hatali"],
            [2, 'Geek 2', "ahha", "lolo", "ortalama"],
            [2, 'Geek 2', "ahha", "lolo", "ortalama"]
        ]

        return data

def store_sure_2_2_saatlik(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( store_sure_api_saatlik, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin

    print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print("saatlik_data")
    print(headersiz_data)



    return headersiz_data  # yogunluk_listesi =




def main_2_8_kisi_miktari(magaza_id, tarih_ilk, tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8_updated, magaza_id, tarih_ilk,
                                  tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )
    print("satis_miktari_data")

    # list_data = json.loads ( data )
    headersiz_data = (data["Data"])
    print ( headersiz_data )
    print ( "satis_miktari_data" )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[1]["Serial"]

def json_id_den_degisim_oranina(tarih1,tarih2,tarih3,tarih4,magaza_no, veri_adi, reverse=True):
    json33 = get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
    edited_json = ((json33["Data"]))
    edited_json1 = sorted ( edited_json, key=lambda k: k.get ( veri_adi, 0 ), reverse=reverse )
    print('kotu siralama11')
    print ( edited_json1 )
    id_listesi = 0
    isim_listesi = 0
    degerler_listesi = 0
    sayi = 0
    toplam_degerler = []
    final_list = []

    json33 = get_performancetable ( yogunluk_haritasi, magaza_no, tarih3, tarih4 )
    edited_json_2 = ((json33["Data"]))

    edited_json2 = sorted ( edited_json_2, key=lambda k: k.get ( veri_adi, 0 ), reverse=reverse )
    print ( 'kotu siralama11' )
    print ( edited_json2 )
    id_listesi2 = 0
    isim_listesi2 = 0
    degerler_listesi2 = 0

    edited_json3 = edited_json1 + edited_json2
    uzunluk_degerleri = len ( edited_json3 )
    print("editeddure11")
    print(edited_json3)

    for area in range ( len(edited_json3) ):
        try:

            print('before11')
            print( edited_json3[sayi][veri_adi] )
            print ( edited_json3[sayi]["Name"] )
            istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json3[sayi][veri_adi]) ) * 100, 2 )) )
            print ( 'After' )
            print(istenen_sayi)
            toplam_degerler.append( istenen_sayi )
        except Exception as e:
            uzunluk_degerleri -= 1
            print("error")
            print(e)
            log_info = str ( f'eksik data1, {edited_json3[sayi]["Name"]}, {e}' )
            print ( log_info )
            toplam_degerler.append( 0 )
        sayi += 1
    sayi = 0

    for area in range ( len(edited_json1) ):
        try:
            id_no =edited_json1[sayi]['Id']
            print('before')
            print( edited_json1[sayi][veri_adi] )
            istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json1[sayi][veri_adi]) ) * 100, 2 )) )
            print ( 'After' )
            print(istenen_sayi)

            degerler_listesi = ( istenen_sayi )
            isim_listesi = ( edited_json1[sayi]["Name"] )
            id_listesi = (edited_json1[sayi]['Id'])

            sayi_2 = 0
            for area in range ( len ( edited_json2 ) ):
                try:
                    if edited_json2[sayi_2]['Id'] == id_no:
                        print ( 'before' )
                        print ( edited_json2[sayi_2][veri_adi] )
                        istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json2[sayi_2][veri_adi]) ) * 100, 2 )) )
                        print ( 'After' )
                        print ( istenen_sayi )

                        degerler_listesi2 = (istenen_sayi)
                        isim_listesi2 = (edited_json2[sayi_2]["Name"])
                        id_listesi2 = (edited_json2[sayi_2]['Id'])

                        print('bunu_buna_bod')
                        print(edited_json2[sayi_2][veri_adi])
                        print(id_listesi2)
                        print(isim_listesi2)
                        print(degerler_listesi2)
                        print(degerler_listesi)



                        final_list.append([id_listesi,isim_listesi, float ( ("{:.2f}".format ( float ( degerler_listesi2/degerler_listesi -1 ) * 100, 2 )) )])
                except ZeroDivisionError as e:
                    print ( "error_zero_division" )
                    print ( e )
                    print(degerler_listesi2,degerler_listesi)
                    log_info = str ( f'eksik data1, {edited_json2[sayi_2]["Name"]}, {e}' )
                    print ( log_info )
                    # degerler_listesi2 = (0)
                    isim_listesi2 = (edited_json2[sayi_2]["Name"])
                    id_listesi2 = (edited_json2[sayi_2]['Id'])
                    final_list.append ( [id_listesi, isim_listesi, float (
                        ("{:.2f}".format ( float ( degerler_listesi2 / 1 ) * 100, 2 )) )] )

                except Exception as e:
                    print ( "error1" )
                    print ( e )
                    log_info = str ( f'eksik data1, {edited_json2[sayi_2]["Name"]}, {e}' )
                    print ( log_info )
                    degerler_listesi2 = (0)
                    isim_listesi2 = (edited_json2[sayi_2]["Name"])
                    id_listesi2 = (edited_json2[sayi_2]['Id'])
                    final_list.append([id_listesi,isim_listesi, float ( ("{:.2f}".format ( float ( degerler_listesi2/degerler_listesi ) * 100, 2 )) )])

                sayi_2 += 1



        except Exception as e:
            print("error")
            print(e)
            log_info = str ( f'eksik data1, {edited_json1[sayi]["Name"]}, {e}' )
            print ( log_info )
            degerler_listesi = ( 0 )
            isim_listesi = ( edited_json1[sayi]["Name"] )
            id_listesi = ( edited_json1[sayi]['Id'] )

        sayi += 1

    print('output')
    print(toplam_degerler)
    print ( 'yogunluk_ortalamasi' )
    yogunluk_ortalamasi = (sum(toplam_degerler)/uzunluk_degerleri)
    print(yogunluk_ortalamasi)
    print(id_listesi,id_listesi2,isim_listesi,isim_listesi2,degerler_listesi,degerler_listesi2)
    return  final_list



def main_2_7_performans_tablosu_hesapla(magaza_id, tarih1,tarih2,tarih3,tarih4,istenen_alan):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih1, tarih2 )  ##240 akasyaya baktigimiz icin
    transfored_alan = "Dwell"
    if istenen_alan == "Dwell":
        transfored_alan = "Dwell"
    elif istenen_alan == "Count":
        transfored_alan = "Count"
    elif istenen_alan == "Density":
        transfored_alan = "Density"

    data1 = get_performancetable ( performas_tablosu, magaza_id, tarih3, tarih4 )
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    headersiz_data1 = (data1["Data"])

    edited_json1 = sorted ( headersiz_data, key=lambda k: k.get ( "Density", 0 ), reverse=True )
    edited_json2 = sorted ( headersiz_data1, key=lambda k: k.get ( "Density", 0 ), reverse=True )

    edited_json3 = edited_json1 + edited_json2


    n = 0
    print ( len ( edited_json3 ) )  # kac tane alan var
    ici_dolu_data = len ( edited_json3 )
    meterSquareTotal = float ( 0 )
    densityTotal = float ( 0 )
    print('bakalimmm')
    print(ici_dolu_data)
    print ( edited_json3 )


    for n in range(len(edited_json3)):
        print("ahhaah")
        print(n)
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])

        print ( edited_json3[n]["Name"] )

        try:
            densityTotal = (densityTotal + float ( ("{:.2f}".format ( float ( (edited_json3[n][transfored_alan]) ), 2 )) ))
            print ( "guncellendi" )
        except Exception as e:

            log_info = str ( f'eksik data, {edited_json3[n]["Name"]}, {e}' )
            app_log.info ( log_info )
            ici_dolu_data -=1


    # yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    # print(headersiz_data)
    # return headersiz_data
    print ( "\n______ Yogunluk" )
    # print("densityTotal _toplam yogunluk")
    # print(densityTotal)
    # print ( "densityPrevTotal _toplam_yogunluk_pre" )
    # print(densityPrevTotal)

    print ( "Density __ total" )
    print ( densityTotal )
    print(ici_dolu_data)
    print(densityTotal/ici_dolu_data)
    son_yuvarlama = float ( ("{:.2f}".format ( float ( (densityTotal/ici_dolu_data) ), 2 )) )

    if transfored_alan == "Density":
        son_yuvarlama = float ( ("{:.2f}".format ( float ( (200/ici_dolu_data) ), 2 )) )

    return son_yuvarlama


def main_2_7_performans_tablosu_satis_sira(magaza_id, tarih1,tarih2):  # ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu, magaza_id, tarih1, tarih2 )  ##240 akasyaya baktigimiz icin


    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])


    edited_json1 = sorted ( headersiz_data, key=lambda k: k.get ( "SaleAmount", 0 ), reverse=False )
    print("hahageld")
    print(edited_json1)




    final_list = []

    kucukden_buyuge_sira = -1
    for n in range(len(edited_json1)):
        print("ahhaah")
        print(n)
        # print(headersiz_data[n])
        # print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        # print(headersiz_data[n]["Id"])

        print ( edited_json1[n]["Name"] )

        try:
            SaleAmount1 = ( float ( ("{:.2f}".format ( float ( (edited_json1[n]["SaleAmount"]) ), 2 )) ))

            print ( "guncellendi" )
        except Exception as e:
            SaleAmount1 = 0

            log_info = str ( f'eksik data, {edited_json1[n]["Name"]}, {e}' )
            app_log.info ( log_info )
        kucukden_buyuge_sira += 1
        print("miktari bu kadar")
        print(SaleAmount1)
        if SaleAmount1 > 0:
            break


    return kucukden_buyuge_sira







if __name__ == "__main__":
    # main ()
    # print(main_2_8_kisi_miktari ( 240, tarih_ilk , tarih_son ))
    # print(main_2_7_performans_tablosu(240, tarih_ilk , tarih_son))
    # boys = (main_2_7_performans_tablosu_double_isim(228, tarih_ilk , tarih_son,"BOYS"))
    # girls = ( main_2_7_performans_tablosu_double_isim ( 240, tarih_ilk, tarih_son, "MEN'S RUN" ) )

    tarih_ilk = "01/02/2021"
    tarih_son = "12/02/2021"

    tarih_1 = tarih_ilk
    tarih_4 = tarih_son
    tarig_limitleri = ilk_tarih_end_son_tarih_baslangic ( tarih_1, tarih_4 )
    tarih_2 = tarig_limitleri[0]
    tarih_3 = tarig_limitleri[1]

    # json33 = get_performancetable ( performas_tablosu, 240, tarih_1, tarih_2 )
    # edited_json = ((json33["Data"]))

    # birlesik_liste = (
    #     json_id_den_degisim_oranina ( tarih_1, tarih_2, tarih_3, tarih_4, 234, "DensityRatio",
    #                                   reverse=True ))
    print(main_2_7_performans_tablosu_satis_sira(240, tarih_1,tarih_2))





    # print ( birlesik_liste )
    #
    # sorted_list = (BubleSort ( birlesik_liste ))
    # print("listeye_bakalim")
    # print(sorted_list)
    # negatif_liste = negatifse ( sorted_list )
    # pozitif_liste = pozitifse ( sorted_list )
    # print ( negatif_liste )
    # print ( pozitif_liste )
    # isimler_listesi_negatif = list_to_string_ve_ile ( negatif_liste[1] )
    # print ( isimler_listesi_negatif )
    # oranlari_listesi_negatif = list_to_string_ve_ile ( negatif_liste[2] )
    # print ( oranlari_listesi_negatif )
    # isimler_listesi_pozitif = list_to_string_ve_ile ( pozitif_liste[1] )
    # print ( isimler_listesi_pozitif  )
    # oranlari_listesi_pozitif  = list_to_string_ve_ile ( pozitif_liste[2] )
    # print ( oranlari_listesi_pozitif  )
    #
    #
    #
    # json33 = get_performancetable ( yogunluk_haritasi, 234, tarih_1, tarih_2 )
    # edited_json = ((json33["Data"]))
    # edited_json1 = sorted ( edited_json, key=lambda k: k.get ( "DensityRatio", 0 ), reverse=True )
    #
    # id_listesi = 0
    # isim_listesi = 0
    # degerler_listesi = 0
    # sayi = 0
    # toplam_degerler = []
    # final_list = []
    #
    # json33 = get_performancetable ( yogunluk_haritasi, 234, tarih_3, tarih_4 )
    # edited_json_2 = ((json33["Data"]))
    #
    # edited_json2 = sorted ( edited_json_2, key=lambda k: k.get ( "DensityRatio", 0 ), reverse=True )
    # id_listesi2 = 0
    # isim_listesi2 = 0
    # degerler_listesi2 = 0





















    #store_sure_2_2 ( 240, tarih_ilk, tarih_son)
    # main_2_3_yogunluk_haritasi_top_5 ( 234, tarih_ilk, tarih_son )
    # print("son____")
    # # print(boys) # CountRatio
    # ilk_liste =(yogunluk_haritasi_isimine_gore_yuzde_top_5( 234, tarih_ilk, tarih_son,"CountRatio",True ))
    #
    # tarih_ilk = "22/02/2021"
    # tarih_son = "26/02/2021"
    #
    # ikinci_liste = ( yogunluk_haritasi_isimine_gore_yuzde_top_5 ( 234, tarih_ilk, tarih_son, "CountRatio", True ) )
    #
    # print(ilk_liste)
    # print(ikinci_liste)
    # cakisanlar = (cakisan_liste_elemanlar_ilk_3(ilk_liste[0],ikinci_liste[0]))
    # print(list_to_string_ve_ile(cakisanlar))
    #
    # tarih_ilk = "15/02/2021"
    # tarih_son = "19/02/2021"

    # print ( main_2_7_performans_tablosu_double_isim ( 240, tarih_ilk, tarih_son, "BOYS" ) )

    #
    # print(boys[1][10]) #metrekare
    # print ( boys[1][11] ) #metrekareorani
    # print(boys[1][3])
    # print ( boys[1][6] )
    # print ( girls[1][3] )
    # print ( girls[1][6] )

    #print(main_2_7_performans_tablosu_alansal ( 308, tarih_ilk, tarih_son, "PrevCount" ))

    ## 5 INCISI KISI SAYISI DEGISIMI
    ###print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "PrevDwell" ) )
    ## 7 INCISI ortalama sure degisimi

    ###print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI

    # print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "n_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI # EN AZ OLAN

    # print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "n_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI # EN AZ OLAN

    # print ( "s" )
    # magaza_id = 307
    # tarih_ilk = "18/01/2021"  # tariha hatasini coz
    # tarih_son = "27/01/2021"
    #print(main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son,"PrevDwell" ))
    # boys = (main_2_7_performans_tablosu_double_isim(228, tarih_ilk , tarih_son,"BOYS"))
    # print(boys)

    # # #main_2_1_kisi_sure_saatlik ( magaza_id, tarih_ilk, tarih_son )
    # #
    # print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "Count" ) )





    #main_2_7_performans_tablosu_alansal ( 308,tarih_ilk, tarih_son, "Count" )

    # 3 kisi sayisi

    # 6 ortalama sure
    #
    # print(main_2_8_edinme_hunisi ( 10324, tarih_ilk, tarih_son ))#5599 #11162  #9943 #11162 #5605 == > #11151
    # print("lalla")
#############______________1.1_sayfa_yogunluk
# liste = main_1_1_yogunluk_listesi(239, '29/10/2020', '12/11/2020' )
# print(liste)
# liste1 = main_1_1_yogunluk_listesi_tarihler(239, '29/10/2020', '12/11/2020' )
# print(liste1)
# dictionary = dict ( zip ( liste, liste1 ) )### gereksiz
# print(dictionary)### gereksiz
# array = list(zip(liste1,liste))
# print(array)
# print(cal_average_density_arrray(array))
# print(bigger_than_average_arrray(array))

#############______________2.1_saaatlik degerler

# main(saatlik_kisi_sure_grafigi)
# liste = main_2_1_saatler ( 240, '29/10/2020', '12/11/2020' )
# print(liste)
# liste1 = main_2_1_kisi_sure_saatlik ( 240, '29/10/2020', '12/11/2020' )
# print ( liste1 )
# array = list ( zip ( liste, liste1 ) )
# print(array)
# sabah_listesi = array[0:3]
# sabah_ortalmasi = (cal_average_array(sabah_listesi))
# oglen_listesi = array[3:7]
# oglen_ortalmasi = (cal_average_array(oglen_listesi))
# aksam_listesi = array[7:12]
# aksam_ortalmasi = (cal_average_array ( aksam_listesi ))
# print(sabah_ogle_aksam ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ))
# print(max_number_array(array))


##______
# main ( saatlik_kisi_sure_grafigi )
# liste = main_2_1_saatler ( 240, '29/10/2020', '12/11/2020' )
# print ( liste )
# liste1 = main_2_1_kisi_sure_saatlik ( 240, '29/10/2020', '12/11/2020' )
# print ( liste1 )
# array = list ( zip ( liste, liste1 ) )
# print ( array )
# sabah_listesi = array[0:3]
# sabah_ortalmasi = (cal_average_array ( sabah_listesi ))
# oglen_listesi = array[3:7]
# oglen_ortalmasi = (cal_average_array ( oglen_listesi ))
# aksam_listesi = array[7:12]
# aksam_ortalmasi = (cal_average_array ( aksam_listesi ))
# print ( sabah_ogle_aksam ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ) )
# print ( max_number_array ( array ) )
