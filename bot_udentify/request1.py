import requests
import json
import time
from decimal import *
import logging
from logging.handlers import RotatingFileHandler
import os
import datetime
import time
import calendar
from scipy.stats.stats import pearsonr
import math

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
dosya_yolu =( BASE_DIR + f"/bot_udentify/test.log" )
print(dosya_yolu)



log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')
logFile = dosya_yolu
my_handler = RotatingFileHandler(logFile,mode='a',maxBytes=5*1024*1024,backupCount=2,encoding=None,delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)
app_log = logging.getLogger('root')
app_log.setLevel(logging.INFO)
app_log.addHandler(my_handler)




APIURL = "https://api.udentify.co"
APIUSER = "delandcaglar@hotmail.com"
APIPASS = "caglar2020"
APITOKEN = ""



magaza_id = 240
# tarih_ilk = "16/11/2020"
# tarih_son = "02/12/2020"
tarih_ilk = "16/10/2020"
tarih_son = "30/10/2020"


url1 = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=180"
url_yogunluk = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=180"
ure_yogunluk_g = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=180"

saatlik_kisi_sure_grafigi = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset=180"
yogunluk_haritasi = "{}/Sketch/{}/Rectangles?sdate=29/10/2020&edate=12/11/2020&stime=10:00&etime=22:00&tzoffset=180&layer=1" ##hatali
performas_tablosu = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1" ##  180 i 0 yaptin duzelt

deneme_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=180&layer=1"
deneme2_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}0&stime=10:00&etime=22:00&tzoffset=180&layer=1"

devam = "{}/Rect/9954/CountandSpenttime?sdate=15/11/2020&edate=26/11/2020&stime=10:00&etime=22:00&filter=1&tzoffset=180"

gunluk_kisi_sure_grafigi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=180"


yogunluk_haritasi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=180"
saatlik_kisi_sure_grafigi_2_8 = "{}/SketchRect/{}/CountandSpenttime?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset=180"


edinme_hunisi_url = "{}/Rect/{}/Funnel?sdate={}&edate={}&stime=10:00&etime=22:00&funnelthresholds=3,10,15&tzoffset=180"  # 3, 10 , 15 sabit



#https://api.udentify.co/Store/240/AreaCount?sdate=15/10/2020&edate=30/10/2020&stime=10:00&etime=22:00&tzoffset=0

def get_token():
    url = "{}/token".format ( APIURL )
    payload = (("grant_type", "password"), ("username", APIUSER), ("password", APIPASS))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    return requests.post ( url, data=payload, headers=headers ).json ()["access_token"]


def get_performancetable(url1,storeId, start, end):
    global APITOKEN
    if APITOKEN == "":
        APITOKEN = get_token ()
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + APITOKEN,
    }

    #url = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1".format ( APIURL,storeId,start,end )
    url = url1.format ( APIURL,storeId,start,end )
    r = requests.get ( url, headers=headers )
    return r.json ()


def main(url1):
    data = get_performancetable (url1,240, '15/10/2020', '30/10/2020' ) ##240 akasyaya baktigimiz icin
    #print ( data )

    #list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print(headersiz_data)
    print("________________________________")
    #print(headersiz_data[0]["Name"]) # Labels tarih
    #print ( headersiz_data[0]["Serial"] )
    #print ( headersiz_data[1]["Name"] ) #Customer
    #print ( headersiz_data[1]["Serial"] )
    #print ( headersiz_data[3]["Name"] ) ##eime
    #print ( headersiz_data[3]["Serial"] )


    #list_data = json.loads ( headersiz_data )

    #print(list_data['fruits'])


def main1_1_tarih (magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( url1 , magaza_id, tarih_ilk, tarih_son ) ##240 akasyaya baktigimiz icin
    #print ( data )

    #list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print(headersiz_data)
    print("________________________________")
    #print(headersiz_data[0]["Name"]) # Labels tarih
    #print ( headersiz_data[0]["Serial"] )
    #print ( headersiz_data[1]["Name"] ) #Customer
    #print ( headersiz_data[1]["Serial"] )
    #print ( headersiz_data[3]["Name"] ) ##eime
    #print ( headersiz_data[3]["Serial"] )

    return  ( headersiz_data[0]["Serial"] )

def main1_1_musteri_sayisi (magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( url1, magaza_id, tarih_ilk, tarih_son ) ##240 akasyaya baktigimiz icin
    #print ( data )

    #list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print(headersiz_data)
    print("________________________________")
    #print(headersiz_data[0]["Name"]) # Labels tarih
    #print ( headersiz_data[0]["Serial"] )
    #print ( headersiz_data[1]["Name"] ) #Customer
    #print ( headersiz_data[1]["Serial"] )
    #print ( headersiz_data[3]["Name"] ) ##eime
    #print ( headersiz_data[3]["Serial"] )

    return  ( headersiz_data[1]["Serial"] )

def main1_1_musteri_suresi (magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( url1,magaza_id, tarih_ilk, tarih_son ) ##240 akasyaya baktigimiz icin
    #print ( data )

    #list_data = json.loads ( data )

    headersiz_data = ((data["Data"]))
    print(headersiz_data)
    print("________________________________")
    #print(headersiz_data[0]["Name"]) # Labels tarih
    #print ( headersiz_data[0]["Serial"] )
    #print ( headersiz_data[1]["Name"] ) #Customer
    #print ( headersiz_data[1]["Serial"] )
    #print ( headersiz_data[3]["Name"] ) ##eime
    #print ( headersiz_data[3]["Serial"] )

    return  ( headersiz_data[3]["Serial"] )


def main_1_1_yogunluk_listesi_tarihler(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( url_yogunluk,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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


def main_1_1_yogunluk_listesi(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( url_yogunluk,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print(headersiz_data)
    # print("________________________________")
    # print(headersiz_data[0]["Name"]) # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )

    return headersiz_data[4]["Serial"]  # yogunluk_listesi =


def list_to_string(s):
    # initialize an empty string
    str1 = " "

    elma = [x for y in (s[i:i+1] + [','] * (i < len(s) - 1) for i in range(0, len(s), 1)) for x in y]
    #print(elma)
    # return string
    return (str1.join (elma))





def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num / len(num)
    return avg
def cal_total(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t

    avg = sum_num
    return avg


def cal_average_density(num): ##sadece degeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    for t in num:
        if t != 0:
            sum_num = sum_num + t
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar

    avg = sum_num / (len(num) - cikarilacak_sayilar)
    return avg


def cal_average_density_buyuk_olanlar(num): ##sadece deegeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    for t in num:
        if t != 0:
            sum_num = sum_num + t
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar

    avg = sum_num / (len(num) - cikarilacak_sayilar)
    return avg

def cal_average_density_arrray(num): ##sadece deegeri verilen sayilari topluyor
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
    print("cozumm")
    print(num)
    print ( sum_num )
    print ( no_zero )
    avg = sum_num / (no_zero - cikarilacak_sayilar)
    return avg

def bigger_than_average_arrray(num): ##sadece deegeri verilen sayilari topluyor
    sum_num = 0
    cikarilacak_sayilar = 0
    buyuk_olanlar_listesi = []

    for t in num:
        if t[1] != 0:
            sum_num = sum_num + t[1]
        else:
            cikarilacak_sayilar = 1 + cikarilacak_sayilar
    no_zero = len(num)
    if no_zero == 0:
        no_zero =1
    avg = sum_num / (no_zero - cikarilacak_sayilar)
    for t in num:
        if t[1] >= avg:
            buyuk_olanlar_listesi.append(t[0])

    return buyuk_olanlar_listesi


def main_2_1_saatler(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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

def main_2_1_kisi_sure_saatlik(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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

def cal_average_array(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t[1]

    avg1 = sum_num / len(num) #yuvarlanmamis hali
    avg = float(("{:.2f}".format(round(avg1, 2)))) ##
    return avg

def ikincisi_dogru_ise_liste_devam_etsin(num):
    list_more_than_1 = []
    for t in num:
        if t[1] == True:
            list_more_than_1.append(t[0])
    return list_more_than_1



def ikincisi_dogru_ise_liste_devam_etmesin(num):
    list_more_than_1 = []
    for t in num:
        if t[1] == False:
            list_more_than_1.append(t[0])
    return list_more_than_1


def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a

    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c

    return largest

def sabah_ogle_aksam(sabah_ortalmasi,oglen_ortalmasi,aksam_ortalmasi):
    if maximum(sabah_ortalmasi,oglen_ortalmasi,aksam_ortalmasi) == sabah_ortalmasi:
        return 'sabah'
    elif maximum(sabah_ortalmasi,oglen_ortalmasi,aksam_ortalmasi) == oglen_ortalmasi:
        return 'öglen'
    else:
        return 'aksam'

def max_number_array(num):
    max_sayi = float(0)
    max_sayi_zaman = ""
    for t in num:
        if max_sayi <= t[1]:
            max_sayi = t[1]
            max_sayi_zaman = t[0]
    return max_sayi_zaman


yogunluk_toplam_deger = float(0)

def yogunluk_haritasi_hesaplama_degerleri_top_5(data): ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1,2,3,4,5]
    bottom_5_area = [1,2,3,4,5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print("Ss")
        print(area)
        yogunluk_listesi.append(data[sayi]["DensityRatio"])
        sayi = sayi + 1
        print(sayi)
    print(yogunluk_listesi)
    yogunluk_toplam_deger = (cal_total(yogunluk_listesi))
    yogunluk_toplam_deger_sirali = (sorted(yogunluk_listesi,reverse=True))
    print('_________')
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse= False ))  #reverse

    print(yogunluk_toplam_deger_sirali)
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5] #en kucukten en buyuge yap
    print(top_5_liste)
    print(bottom_5_liste)
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    def sayilar_listesi(siralama_sayisi,data,top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            if top_5_liste[siralama_sayisi] ==(data[sayi1]["DensityRatio"]):
                en_buyuk = (data[sayi1]["Name"])
            sayi1 = sayi1 + 1
        return(en_buyuk)
    top_5_liste_adlar.append(sayilar_listesi(0,data,top_5_liste))
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data,top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data ,top_5_liste) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data ,top_5_liste) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data,top_5_liste ) )
    print(top_5_liste_adlar)
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data,bottom_5_liste ) )
    print ( bottom_5_liste_adlar )
    return top_5_liste_adlar

def yogunluk_haritasi_hesaplama_degerleri_bottom_5(data): ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1,2,3,4,5]
    bottom_5_area = [1,2,3,4,5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print("Ss")
        print(area)
        yogunluk_listesi.append(data[sayi]["DensityRatio"])
        sayi = sayi + 1
        print(sayi)
    print(yogunluk_listesi)
    yogunluk_toplam_deger = (cal_total(yogunluk_listesi))
    yogunluk_toplam_deger_sirali = (sorted(yogunluk_listesi,reverse=True))
    print('_________')
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse= False ))  #reverse

    print(yogunluk_toplam_deger_sirali)
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5] #en kucukten en buyuge yap
    print(top_5_liste)
    print(bottom_5_liste)
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    def sayilar_listesi(siralama_sayisi,data,top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            if top_5_liste[siralama_sayisi] ==(data[sayi1]["DensityRatio"]):
                en_buyuk = (data[sayi1]["Name"])
            sayi1 = sayi1 + 1
        return(en_buyuk)
    top_5_liste_adlar.append(sayilar_listesi(0,data,top_5_liste))
    top_5_liste_adlar.append ( sayilar_listesi ( 1, data,top_5_liste ) )
    top_5_liste_adlar.append ( sayilar_listesi ( 2, data ,top_5_liste) )
    top_5_liste_adlar.append ( sayilar_listesi ( 3, data ,top_5_liste) )
    top_5_liste_adlar.append ( sayilar_listesi ( 4, data,top_5_liste ) )
    print(top_5_liste_adlar)
    bottom_5_liste_adlar.append ( sayilar_listesi ( 0, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 1, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 2, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 3, data,bottom_5_liste ) )
    bottom_5_liste_adlar.append ( sayilar_listesi ( 4, data,bottom_5_liste ) )
    print ( bottom_5_liste_adlar )
    return bottom_5_liste_adlar




def main_2_3_yogunluk_haritasi_top_5(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])

    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

def main_2_3_yogunluk_haritasi_bottom_5(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5(headersiz_data)


def main_2_3_yogunluk_haritasi_orani_bottom_5(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5(headersiz_data)


def yogunluk_haritasi_hesaplama_degerleri_bottom_5_orani(data): ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1,2,3,4,5]
    bottom_5_area = [1,2,3,4,5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print("Ss")
        print(area)
        yogunluk_listesi.append(data[sayi]["DensityRatio"])
        sayi = sayi + 1
        print(sayi)
    print(yogunluk_listesi)
    yogunluk_toplam_deger = (cal_total(yogunluk_listesi))
    yogunluk_toplam_deger_sirali = (sorted(yogunluk_listesi,reverse=True))
    print('_________')
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse= False ))  #reverse

    print(yogunluk_toplam_deger_sirali)
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5] #en kucukten en buyuge yap
    print(top_5_liste)
    print(bottom_5_liste)
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    top_5_liste_adlar_tf = []
    bottom_5_liste_adlar_tf = []
    def sayilar_listesi(siralama_sayisi,data,top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            if top_5_liste[siralama_sayisi] ==(data[sayi1]["DensityRatio"]):
                en_buyuk = (data[sayi1]["Name"])
            sayi1 = sayi1 + 1
        return(en_buyuk)
    def sayilar_listesi_orani_1_den_buyuk_mu(siralama_sayisi,data,top_5_liste):
        sayi1 = 0
        buyuk_mu = False
        for area in data:
            if top_5_liste[siralama_sayisi] ==(data[sayi1]["DensityRatio"]) and  (((data[sayi1]["DensityRatio"])/(yogunluk_toplam_deger)) >= 0.01):
                buyuk_mu = True
            sayi1 = sayi1 + 1
        return(buyuk_mu)

    print("yogunluk_toplam")
    print(yogunluk_toplam_deger)

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


    top_5_liste_adlar_tf.append(sayilar_listesi_orani_1_den_buyuk_mu( 1, data,top_5_liste ))
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,top_5_liste ) )
    top_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,top_5_liste ) )
    print(top_5_liste_adlar_tf)
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,bottom_5_liste ) )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,bottom_5_liste )  )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,bottom_5_liste )  )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,bottom_5_liste )  )
    bottom_5_liste_adlar_tf.append ( sayilar_listesi_orani_1_den_buyuk_mu( 1, data,bottom_5_liste )  )
    print ( bottom_5_liste_adlar_tf )

    array = list ( zip ( bottom_5_liste_adlar, bottom_5_liste_adlar_tf ) )
    print('aaa')
    print(array)
    liste = ikincisi_dogru_ise_liste_devam_etmesin(array)
    print("listee")
    print(liste)

    return liste

def yogunluk_haritasi_hesaplama_degerleri_top_5_orani(data): ##ayni sayi olursa nasil siraliyoruz platformda diye sor
    global yogunluk_toplam_deger
    top_5_area = [1,2,3,4,5]
    bottom_5_area = [1,2,3,4,5]
    yogunluk_listesi = []
    sayi = 0
    for area in data:
        print("Ss")
        print(area)
        yogunluk_listesi.append(data[sayi]["DensityRatio"])
        sayi = sayi + 1
        print(sayi)
    print(yogunluk_listesi)
    yogunluk_toplam_deger = (cal_total(yogunluk_listesi))
    yogunluk_toplam_deger_sirali = (sorted(yogunluk_listesi,reverse=True))
    print('_________')
    yogunluk_toplam_deger_sirali_reverse = (sorted ( yogunluk_listesi, reverse= False ))  #reverse

    print(yogunluk_toplam_deger_sirali)
    top_5_liste = yogunluk_toplam_deger_sirali[:5]
    bottom_5_liste = yogunluk_toplam_deger_sirali_reverse[:5] #en kucukten en buyuge yap
    print(top_5_liste)
    print(bottom_5_liste)
    top_5_liste_adlar = []
    bottom_5_liste_adlar = []
    top_5_liste_adlar_tf = []
    bottom_5_liste_adlar_tf = []

    def sayilar_listesi(siralama_sayisi, data, top_5_liste):
        en_buyuk = "s"
        sayi1 = 0
        for area in data:
            if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]):
                en_buyuk = (data[sayi1]["Name"])
            sayi1 = sayi1 + 1
        return (en_buyuk)

    def sayilar_listesi_orani_1_den_buyuk_mu(siralama_sayisi, data, top_5_liste):
        sayi1 = 0
        buyuk_mu = False
        for area in data:
            if top_5_liste[siralama_sayisi] == (data[sayi1]["DensityRatio"]) and (
                    ((data[sayi1]["DensityRatio"]) / (yogunluk_toplam_deger)) >= 0.01):
                buyuk_mu = True
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

    liste = ikincisi_dogru_ise_liste_devam_etsin(array)


    return liste






def main_2_5_yogunluk_haritasi_orani_bottom_5_orani(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_bottom_5_orani(headersiz_data)


def main_2_5_yogunluk_haritasi_orani_top_5_orani(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return yogunluk_haritasi_hesaplama_degerleri_top_5_orani(headersiz_data)

def main_2_7_performans_tablosu_alansal(magaza_id, tarih_ilk , tarih_son,bakilan_alan): #ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin

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
    print("tarih_kontrolu")
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
    print(len(headersiz_data)) # kac tane alan var
    meterSquareTotal = float(0)
    densityTotal = float(0)
    densityPrevTotal = float(0)
    saleQuantityTotal = float(0)
    prevsaleQuantityTotal = float(0)
    prevsaleAmountTotal = float(0)
    saleAmountTotal = float(0)

    for headers in headersiz_data:
        #print(headersiz_data[n])
        #print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        #print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float(headersiz_data[n]["Metersquare"])
        print(headersiz_data[n]["Name"])
        densityTotal = ( densityTotal + float(("{:.2f}".format(float (( headersiz_data[n]["Density"])), 2))))
        print("guncellendi")
        densityPrevTotal = densityPrevTotal +  float(("{:.2f}".format(float (( headersiz_data1[n]["Density"])), 2)))
        try:
            saleQuantityTotal = saleQuantityTotal + float ( headersiz_data[n]["AvgSaleQuantity"] ) #eksik data bunu sor
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)

        # try:
        #     densityPrevTotal = densityPrevTotal + float ( headersiz_data1[n]["Density"] ) #AvgSaleAmount
        # except Exception as e:
        #     log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
        #     app_log.info(log_info)
        #     print ( "nassiya" )



        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float (headersiz_data1[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            print ( "nassiya1" )

        try:
            saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            print ( "nassiya1" )


        n += 1


    print(meterSquareTotal)
    print(densityTotal)
    print(densityPrevTotal)
    print(saleQuantityTotal)
    print(prevsaleQuantityTotal)
    print(prevsaleAmountTotal)
    print(saleAmountTotal)

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float(0)
    info_all = []

    n = 0
    for headers in headersiz_data:
        print ( headersiz_data[n]["Name"] )
        print ( headersiz_data[n]["Id"] )
        print(headersiz_data[n])
        print("__previousData__")
        #print ( headersiz_data1[n] )
        print("header uzunlugu")
        #print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar

        print("department rectangles")
        #print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print("bakilan_alan")
        # TotalCount_final = float(headersiz_data[n][bakilan_alan])
        # print(TotalCount_final)

        def searching_function(bakilan_alan):
            if bakilan_alan == "PrevCount":
                a1 = float ( headersiz_data[n]["Count"] )
                a2 = float ( headersiz_data1[n]["Count"] )
                return  float(math.ceil ( ((a1 - a2) / a2) * 100 ))
            if bakilan_alan == "PrevDwell" :
                a1 = float ( headersiz_data[n]["Dwell"] )
                a2 = float ( headersiz_data1[n]["Dwell"] )
                return float(math.ceil ( ((a1 - a2) / a2) * 100 ))
            if bakilan_alan == "_15s_Enterance" :
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                return float ( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
            if bakilan_alan == "n_15s_Enterance" :
                _15s_Enterance = (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"]) * 100
                try :
                    return   1/float( ("{:.2f}".format ( float ( (_15s_Enterance) ), 2 )) )
                except:
                    return 1/10000
            if bakilan_alan == "Dwell":
                Dwell = float ( headersiz_data[n]["Dwell"] )
                return float ( ("{:.2f}".format ( float ( (Dwell) ), 2 )) )
            if bakilan_alan == "Count":
                return  float ( headersiz_data[n]["Count"] )

        TotalCount_final = searching_function(bakilan_alan)

        print(TotalCount_final)
        print(En_cok_ziyaret_edilen_sayi)

        if En_cok_ziyaret_edilen_sayi < TotalCount_final :
            print("son_denemeeeee")

            En_cok_ziyaret_edilen_sayi = TotalCount_final
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print (En_cok_ziyaret_edilen_id1)
                En_cok_ziyaret_edilen_id2= headersiz_data[n]["DepartmentRectangles"][1]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )

            #  x = float ( ("{:.2f}".format ( float ( (    ) ), 2 )) )

            print("En_cok_ziyaret_edilen_ad11")
            print(En_cok_ziyaret_edilen_ad)

            # yogunluk ile alakadar degisim
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data[n]["Dwell"] )
            a3 = float ( headersiz_data1[n]["Count"] )
            a4 = float ( headersiz_data1[n]["Dwell"] )

            DensityChange = math.ceil(float ( (a1 * a2 - a3 * a4) / (a3 * a4) ) * 100)
            DensityChange = float ( ("{:.2f}".format ( float ( (DensityChange) ), 2 )) )

            print ( "PrevDwell" )
            a1 = float ( headersiz_data[n]["Dwell"] )
            a2 = float ( headersiz_data1[n]["Dwell"] )
            PrevDwell = math.ceil ( ((a1 - a2) / a2) * 100 )
            print ( PrevDwell )

            print ( "Density111" )  # ! burayi duzelt
            print(DensityChange)
            print(headersiz_data[n]["Density"])
            print(densityTotal)
            Density = float ( ( (float(headersiz_data[n]["Density"])  ) * (100)) / (densityTotal) ) # ! duzelt math.ceil
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
            PrevCount = math.ceil(((a1-a2) / a2)*100)

            print ( "PrevCount111" )
            print(a1)
            print ( a2 )




            # ilgi orani
            _15s_Enterance =  (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"] ) * 100
            _15s_Enterance = float ( ("{:.2f}".format ( float ( ( _15s_Enterance   ) ), 2 )) )
            a1= float ( headersiz_data[n]["CountOver15Sec"] )
            a2= float ( headersiz_data[n]["Count"] )
            a3=float (headersiz_data1[n]["CountOver15Sec"] )
            a4=float ( headersiz_data1[n]["Count"] )
            EntranceChange = (a1/a2 - a3/a4)/(a3/a4)*100
            EntranceChange = float ( ("{:.2f}".format ( float ( (  EntranceChange  ) ), 2 )) )



            ## Ortalama sure
            Dwell = float ( headersiz_data[n]["Dwell"] )
            Dwell = float ( ("{:.2f}".format ( float ( (  Dwell  ) ), 2 )) )



            # print("DensityChange")
            # DensityChange = (((float(headersiz_data[n]["Count"]) * float(headersiz_data[n]["Dwell"])) - (float(headersiz_data1[n]["Dwell"]) * float(headersiz_data1[n]["Count"]))) / (float(headersiz_data1[n]["Count"]) * float(headersiz_data1[n]["Dwell"]))) * 100
            # DensityChange = float ( ("{:.2f}".format ( float ( ( DensityChange  ) ), 2 )) )
            # print(DensityChange)

            #_______________ m2

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )
            a3 = float ( headersiz_data1[n]["SketchMetersquare"] )

            SketchMetersquare = ((a1 /a2 ) * a3)
            SketchMetersquare = float ( ("{:.2f}".format ( float ( (SketchMetersquare) ), 2 )) )

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )


            Metersquare = ((a1 * 100) / a2)
            Metersquare = float ( ("{:.2f}".format ( float ( (Metersquare) ), 2 )) )





            print("SaleAmount")
            #SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            #print(SaleAmount)
            print("ConversionRate")
            #ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            #print(ConversionRate) # key error veriyor bunu hallet
            print("ConversionChange") #emin olamadim bak
            print("Enterance_15s")
            Enterance_15s = (float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"]))*100
            print(Enterance_15s)
            print("EntranceChange") #try except koydur hepsinde yok
            #EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            #print(EntranceChange)


        n += 1
        print("/n 1")

    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)


    #print(headersiz_data)
    #return headersiz_data
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
    print('TotalCount _kisi_sayisi_toplam') # kisi_sayisi == toplam
    print(TotalCount)
    print("PrevCount kisi _sayisi_degisim")
    print(PrevCount)

    # print ( "DensityChange" )
    # print ( DensityChange )

    print ( "\n______ ortalma_sure" )
    print ( "Dwell __ ortalama_sure_saniye" )
    print ( Dwell )
    print ( "PrevDwell _ortalama_sure_degisim" )
    print ( PrevDwell )



    print("\n______ ilgi_orani")
    print("_15s_Enterance  ilgi_orani _15s/giren")
    print(_15s_Enterance)
    print("EntranceChange ilgi_orani_degisim")
    print(EntranceChange)
    print ( "bitti" )


    print("\n______ m2_orani")

    print("SketchMetersquare __ metrekare")
    print(SketchMetersquare)
    print("Metersquare  __metrekare orani")
    print(Metersquare)



    try:
        info_all = [[En_cok_ziyaret_edilen_ad,En_cok_ziyaret_edilen_id,En_cok_ziyaret_edilen_sayi,En_cok_ziyaret_edilen_id1,En_cok_ziyaret_edilen_id2],[Density,DensityStoreChange,DensityChange,Count,TotalCount,PrevCount,Dwell,PrevDwell,_15s_Enterance,EntranceChange,SketchMetersquare,Metersquare]]
    except:
        info_all = [[En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi,En_cok_ziyaret_edilen_id1],[Density,DensityStoreChange,DensityChange,Count,TotalCount,PrevCount,Dwell,PrevDwell,_15s_Enterance,EntranceChange,SketchMetersquare,Metersquare]]


    return info_all





def main_2_7_performans_tablosu_double_isim(magaza_id, tarih_ilk , tarih_son,alan_ismi): #ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin

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
    print("tarih_kontrolu")
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
    print(len(headersiz_data)) # kac tane alan var
    meterSquareTotal = float(0)
    densityTotal = float(0)
    densityPrevTotal = float(0)
    saleQuantityTotal = float(0)
    prevsaleQuantityTotal = float(0)
    prevsaleAmountTotal = float(0)
    saleAmountTotal = float(0)

    for headers in headersiz_data:
        #print(headersiz_data[n])
        #print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        #print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float(headersiz_data[n]["Metersquare"])
        print(headersiz_data[n]["Name"])
        densityTotal = ( densityTotal + float(("{:.2f}".format(float (( headersiz_data[n]["Density"])), 2))))
        print("guncellendi")
        densityPrevTotal = densityPrevTotal +  float(("{:.2f}".format(float (( headersiz_data1[n]["Density"])), 2)))
        try:
            saleQuantityTotal = saleQuantityTotal + float ( headersiz_data[n]["AvgSaleQuantity"] ) #eksik data bunu sor
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)

        # try:
        #     densityPrevTotal = densityPrevTotal + float ( headersiz_data1[n]["Density"] ) #AvgSaleAmount
        # except Exception as e:
        #     log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
        #     app_log.info(log_info)
        #     print ( "nassiya" )



        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float (headersiz_data1[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            print ( "nassiya1" )

        try:
            saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            print ( "nassiya1" )


        n += 1


    print(meterSquareTotal)
    print(densityTotal)
    print(densityPrevTotal)
    print(saleQuantityTotal)
    print(prevsaleQuantityTotal)
    print(prevsaleAmountTotal)
    print(saleAmountTotal)

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float(0)
    info_all = []

    n = 0
    for headers in headersiz_data:
        print ( headersiz_data[n]["Name"] )
        print ( headersiz_data[n]["Id"] )
        print(headersiz_data[n])
        print("__previousData__")
        #print ( headersiz_data1[n] )
        print("header uzunlugu")
        #print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar

        print("department rectangles")
        #print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print("TotalCount")
        TotalCount_final = float(headersiz_data[n]["TotalCount"])
        print(TotalCount_final)

        if headersiz_data[n]["Name"] == alan_ismi :
            print("son_denemeeeee")

            En_cok_ziyaret_edilen_sayi = TotalCount_final
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print (En_cok_ziyaret_edilen_id1)
                En_cok_ziyaret_edilen_id2= headersiz_data[n]["DepartmentRectangles"][1]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )

            #  x = float ( ("{:.2f}".format ( float ( (    ) ), 2 )) )

            print("En_cok_ziyaret_edilen_ad11")
            print(En_cok_ziyaret_edilen_ad)

            # yogunluk ile alakadar degisim
            a1 = float ( headersiz_data[n]["Count"] )
            a2 = float ( headersiz_data[n]["Dwell"] )
            a3 = float ( headersiz_data1[n]["Count"] )
            a4 = float ( headersiz_data1[n]["Dwell"] )

            DensityChange = math.ceil(float ( (a1 * a2 - a3 * a4) / (a3 * a4) ) * 100)
            DensityChange = float ( ("{:.2f}".format ( float ( (DensityChange) ), 2 )) )

            print ( "PrevDwell" )
            a1 = float ( headersiz_data[n]["Dwell"] )
            a2 = float ( headersiz_data1[n]["Dwell"] )
            PrevDwell = math.ceil ( ((a1 - a2) / a2) * 100 )
            print ( PrevDwell )

            print ( "Density111" )  # ! burayi duzelt
            print(DensityChange)
            print(headersiz_data[n]["Density"])
            print(densityTotal)
            Density = float ( ( (float(headersiz_data[n]["Density"])  ) * (100)) / (densityTotal) ) # ! duzelt math.ceil
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
            PrevCount = math.ceil(((a1-a2) / a2)*100)

            print ( "PrevCount111" )
            print(a1)
            print ( a2 )




            # ilgi orani
            _15s_Enterance =  (headersiz_data[n]["CountOver15Sec"]) / (headersiz_data[n]["Count"] ) * 100
            _15s_Enterance = float ( ("{:.2f}".format ( float ( ( _15s_Enterance   ) ), 2 )) )
            a1= float ( headersiz_data[n]["CountOver15Sec"] )
            a2= float ( headersiz_data[n]["Count"] )
            a3=float (headersiz_data1[n]["CountOver15Sec"] )
            a4=float ( headersiz_data1[n]["Count"] )
            EntranceChange = (a1/a2 - a3/a4)/(a3/a4)*100
            EntranceChange = float ( ("{:.2f}".format ( float ( (  EntranceChange  ) ), 2 )) )



            ## Ortalama sure
            Dwell = float ( headersiz_data[n]["Dwell"] )
            Dwell = float ( ("{:.2f}".format ( float ( (  Dwell  ) ), 2 )) )



            # print("DensityChange")
            # DensityChange = (((float(headersiz_data[n]["Count"]) * float(headersiz_data[n]["Dwell"])) - (float(headersiz_data1[n]["Dwell"]) * float(headersiz_data1[n]["Count"]))) / (float(headersiz_data1[n]["Count"]) * float(headersiz_data1[n]["Dwell"]))) * 100
            # DensityChange = float ( ("{:.2f}".format ( float ( ( DensityChange  ) ), 2 )) )
            # print(DensityChange)

            #_______________ m2

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )
            a3 = float ( headersiz_data1[n]["SketchMetersquare"] )

            SketchMetersquare = ((a1 /a2 ) * a3)
            SketchMetersquare = float ( ("{:.2f}".format ( float ( (SketchMetersquare) ), 2 )) )

            a1 = float ( headersiz_data[n]["Metersquare"] )
            a2 = float ( meterSquareTotal )


            Metersquare = ((a1 * 100) / a2)
            Metersquare = float ( ("{:.2f}".format ( float ( (Metersquare) ), 2 )) )





            print("SaleAmount")
            #SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            #print(SaleAmount)
            print("ConversionRate")
            #ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            #print(ConversionRate) # key error veriyor bunu hallet
            print("ConversionChange") #emin olamadim bak
            print("Enterance_15s")
            Enterance_15s = (float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"]))*100
            print(Enterance_15s)
            print("EntranceChange") #try except koydur hepsinde yok
            #EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            #print(EntranceChange)


        n += 1
        print("/n 1")

    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)


    #print(headersiz_data)
    #return headersiz_data
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
    print('TotalCount _kisi_sayisi_toplam') # kisi_sayisi == toplam
    print(TotalCount)
    print("PrevCount kisi _sayisi_degisim")
    print(PrevCount)

    # print ( "DensityChange" )
    # print ( DensityChange )

    print ( "\n______ ortalma_sure" )
    print ( "Dwell __ ortalama_sure_saniye" )
    print ( Dwell )
    print ( "PrevDwell _ortalama_sure_degisim" )
    print ( PrevDwell )



    print("\n______ ilgi_orani")
    print("_15s_Enterance  ilgi_orani _15s/giren")
    print(_15s_Enterance)
    print("EntranceChange ilgi_orani_degisim")
    print(EntranceChange)
    print ( "bitti" )


    print("\n______ m2_orani")

    print("SketchMetersquare __ metrekare")
    print(SketchMetersquare)
    print("Metersquare  __metrekare orani")
    print(Metersquare)



    try:
        info_all = [[En_cok_ziyaret_edilen_ad,En_cok_ziyaret_edilen_id,En_cok_ziyaret_edilen_sayi,En_cok_ziyaret_edilen_id1,En_cok_ziyaret_edilen_id2],[Density,DensityStoreChange,DensityChange,Count,TotalCount,PrevCount,Dwell,PrevDwell,_15s_Enterance,EntranceChange,SketchMetersquare,Metersquare]]
    except:
        info_all = [[En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi],[Density,DensityStoreChange,DensityChange,Count,TotalCount,PrevCount,Dwell,PrevDwell,_15s_Enterance,EntranceChange,SketchMetersquare,Metersquare]]


    return info_all




















def main_2_7_performans_tablosu(magaza_id, tarih_ilk , tarih_son): #ceil gordugun yere round fonksiyonu at
    data = get_performancetable ( performas_tablosu,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )
    n = 0
    print(len(headersiz_data)) # kac tane alan var
    meterSquareTotal = float(0)
    densityTotal = float(0)
    densityPrevTotal = float(0)
    saleQuantityTotal = float(0)
    prevsaleQuantityTotal = float(0)
    prevsaleAmountTotal = float(0)
    saleAmountTotal = float(0)

    for headers in headersiz_data:
        #print(headersiz_data[n])
        #print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        #print(headersiz_data[n]["Id"])
        meterSquareTotal = meterSquareTotal + float(headersiz_data[n]["Metersquare"])
        densityTotal = densityTotal + float ( headersiz_data[n]["Density"])
        densityPrevTotal = densityPrevTotal + float ( headersiz_data[n]["DepartmentRectangles"][0]["Density"] )
        try:
            saleQuantityTotal = saleQuantityTotal + float ( headersiz_data[n]["AvgSaleQuantity"] ) #eksik data bunu sor
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            continue

        try:
            densityPrevTotal = densityPrevTotal + float ( headersiz_data[n]["DepartmentRectangles"][0]["Density"] ) ## hatali
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            continue
        print("nassiya")

        try:
            prevsaleAmountTotal = prevsaleAmountTotal + float (headersiz_data[n]["DepartmentRectangles"][0]["AvgSaleAmount"] )
        except Exception as e:
            log_info = str(f"{e}_ buyuk olasilikla eksik data var burada")
            app_log.info(log_info)
            continue
        print("nassiya1")



        saleAmountTotal = saleAmountTotal + float ( headersiz_data[n]["AvgSaleAmount"] )




        n += 1


    print(meterSquareTotal)
    print(densityTotal)
    print(densityPrevTotal)
    print(saleQuantityTotal)
    print(prevsaleQuantityTotal)
    print(prevsaleAmountTotal)
    print(saleAmountTotal)

    En_cok_ziyaret_edilen_ad = ""
    En_cok_ziyaret_edilen_id = ""
    En_cok_ziyaret_edilen_sayi = float(0)
    info_all = []

    n = 0
    for headers in headersiz_data:
        print(headersiz_data[n])
        print("header uzunlugu")
        print(len(headersiz_data[n])) # alanlarin uzunlugu ne kadar
        print ( headersiz_data[n]["Name"] )
        print(headersiz_data[n]["Id"])
        print("department rectangles")
        #print ( headersiz_data[n]["DepartmentRectangles"][0]["Density"])

        print("TotalCount")
        TotalCount = float(headersiz_data[n]["TotalCount"])
        print(TotalCount)
        if En_cok_ziyaret_edilen_sayi < TotalCount :
            print("son_denemeeeee")

            En_cok_ziyaret_edilen_sayi = TotalCount
            En_cok_ziyaret_edilen_ad = headersiz_data[n]["Name"]
            En_cok_ziyaret_edilen_id = headersiz_data[n]["Id"]
            print ( En_cok_ziyaret_edilen_sayi )
            print ( En_cok_ziyaret_edilen_ad )
            print ( En_cok_ziyaret_edilen_id )
            try:
                En_cok_ziyaret_edilen_id1 = headersiz_data[n]["DepartmentRectangles"][0]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print (En_cok_ziyaret_edilen_id1)
                En_cok_ziyaret_edilen_id2= headersiz_data[n]["DepartmentRectangles"][1]["Id"]  #HUNI iD BUNLARI GUNCELLE
                print ( En_cok_ziyaret_edilen_id2 )

            except Exception as e:
                log_info = str ( f"{e}_ buyuk olasilikla eksik data var burada" )
                app_log.info ( log_info )
                continue


            print("En_cok_ziyaret_edilen_ad11")
            print(En_cok_ziyaret_edilen_ad)

            print("Density")
            Density = float((((headersiz_data[n]["Density"]))*(100))/(densityTotal))
            print(Density)
            print("DensityStoreChange") #duzelttin
            DensityStoreChange = Density - (float((((headersiz_data[n]["DepartmentRectangles"][0]["Density"]))*(100))/(densityPrevTotal)))
            print(DensityStoreChange)
            print("DensityChange")
            DensityChange = (((float(headersiz_data[n]["Count"]) * float(headersiz_data[n]["Dwell"])) - (float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]) * float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))) / (float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]) * float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))) * 100
            print(DensityChange)

            print("PrevCount")
            PrevCount = ((float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))*100
            print(PrevCount)
            print("PrevDwell")
            PrevDwell = ((float(headersiz_data[n]["Dwell"])-float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"])) / float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"])) * 100
            print(PrevDwell)
            print("SaleAmount")
            #SaleAmount = float(headersiz_data[n]["AvgSaleAmount"]) # key error veriyor bunu hallet
            #print(SaleAmount)
            print("ConversionRate")
            #ConversionRate = (float(headersiz_data[n]["AvgSaleAmount"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Dwell"]))/(float(headersiz_data[n]["AvgSaleAmount"]))*100
            #print(ConversionRate) # key error veriyor bunu hallet
            print("ConversionChange") #emin olamadim bak
            print("Enterance_15s")
            Enterance_15s = (float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"]))*100
            print(Enterance_15s)
            print("EntranceChange") #try except koydur hepsinde yok
            #EntranceChange = ((float(headersiz_data[n]["CountOver15Sec"])/float(headersiz_data[n]["Count"])-float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"]))/(float(headersiz_data[n]["DepartmentRectangles"][0]["CountOver15Sec"])/float(headersiz_data[n]["DepartmentRectangles"][0]["Count"])))
            #print(EntranceChange)

        n += 1
        print("/n 1")

    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    try:
        info_all = [En_cok_ziyaret_edilen_ad,En_cok_ziyaret_edilen_id,En_cok_ziyaret_edilen_sayi,En_cok_ziyaret_edilen_id1,En_cok_ziyaret_edilen_id2]
    except:
        info_all = [En_cok_ziyaret_edilen_ad, En_cok_ziyaret_edilen_id, En_cok_ziyaret_edilen_sayi]


    #print(headersiz_data)
    #return headersiz_data
    return info_all






def main_2_8_ozel_alan(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return headersiz_data




def main_2_8_saatler_gunluk(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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

def main_2_8_kisi_miktari(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )
    headersiz_data = (data["Data"])
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[1]["Serial"]

def main_2_8_kisi_sure(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( gunluk_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )
    print("_________main_2_8_kisi_miktari")
    headersiz_data = (data["Data"])
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return (headersiz_data[3]["Serial"])



def findDay(date):
    born = datetime.datetime.strptime(date, "%d/%m/%Y").weekday()
    return (calendar.day_name[born])

def gunleri_classifiye_et(gunler):
    hafta_sonu_degerleri = []
    hafta_ici_degerleri = []
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
    return hafta_ici_degerleri,hafta_sonu_degerleri

def hafta_ici_hafta_sonu_ortalamalar(hafta_ici_degerleri,hafta_sonu_degerleri,gunler_ve_musteri):
    hafta_ici_ortalama_listesi = []
    hafta_sonu_ortalama_listesi = []
    for hafta_ici_degerler in hafta_ici_degerleri:
         #print(gunler_ve_musteri[hafta_ici_degerler])
         hafta_ici_ortalama_listesi.append(gunler_ve_musteri[hafta_ici_degerler])

    hafta_ici_ortalama = cal_average(hafta_ici_ortalama_listesi)
    #print(hafta_ici_ortalama)
    for hafta_sonu_degerler in hafta_sonu_degerleri:
        #print ( gunler_ve_musteri[hafta_sonu_degerler] )
        hafta_sonu_ortalama_listesi.append ( gunler_ve_musteri[hafta_sonu_degerler]  )
    hafta_sonu_ortalama = cal_average ( hafta_sonu_ortalama_listesi )
    #print ( hafta_sonu_ortalama )
    return(hafta_ici_ortalama,hafta_sonu_ortalama)


def hafta_ici_hafta_sonu_oran_karsilastirmasi(hafta_ici_ortalama,hafta_sonu_ortalama):
    #print(hafta_sonu_ortalama / hafta_ici_ortalama)
    return ("{:.2f}".format(round((hafta_sonu_ortalama / hafta_ici_ortalama), 2))) # en yakin ikinci basamaga yuvarliyor

def hafta_ici_hafta_sonu_buyukluk_karsilastirmasi(hafta_ici_ortalama,hafta_sonu_ortalama):

    if hafta_sonu_ortalama > hafta_ici_ortalama:
        return "artmaktadır."
    elif hafta_sonu_ortalama < hafta_ici_ortalama:
        return "azalmaktadır."
    elif hafta_sonu_ortalama > hafta_ici_ortalama:
        return "hafta içi ile ortalamada günlük olarak aynı kalmaktadır."

def gunluk_ortalama_sure_2_8(gunler_ve_sure): ##tum gunluk sureleri topla gunluk sure sayisina bol
    global gunluk_ortalama_sure #sundan bir emin ol
    toplam_deger = float(0)
    for gunler in gunler_ve_sure:
        toplam_deger = toplam_deger + gunler
    return ("{:.2f}".format(round(toplam_deger/(len(gunler_ve_sure)), 2)))

# gunler = main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son)
# gunler_ve_musteri = main_2_8_kisi_miktari(4777,tarih_ilk , tarih_son)
# gunler_ve_sure = main_2_8_kisi_sure(4777,tarih_ilk , tarih_son)
# print(gunluk_ortalama_sure_2_8(gunler_ve_sure))
# print("bababa")
# print(gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son)))
# print(hafta_ici_hafta_sonu_ortalamalar(gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son))[0],gunleri_classifiye_et(main_2_8_saatler_gunluk(4777,tarih_ilk , tarih_son))[1],main_2_8_kisi_miktari(4777,tarih_ilk , tarih_son)))
# print(hafta_ici_hafta_sonu_oran_karsilastirmasi(1760.6923076923076, 1796.25))
# print(hafta_ici_hafta_sonu_buyukluk_karsilastirmasi(1760.6923076923076,1796.25))

def saatler_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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

def toplam_kisi_sure_saatlik_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    #print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[2]["Serial"]

def saat_sure_saatlik_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    #print ( headersiz_data )
    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return headersiz_data[3]["Serial"]

def kisi_sure_saatlik_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( saatlik_kisi_sure_grafigi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print("bakbakbak")
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
            return("pozitif güçlü korelasyon")
        if 0.5 <= r_degeri <= 0.85:
            return("pozitif orta korelasyon")
        if 0.1 <= r_degeri <= 0.5:
            return("pozitif zayıf korelasyon")
        if  0 <= r_degeri <= 0.1:
            return("pozitif çok zayıf korelasyon")
    else:
        if -0.85 >= r_degeri >= -1:
            return("negatif güçlü korelasyon")
        if -0.5 >= r_degeri >= -0.85:
            return("negatif orta korelasyon")
        if -0.1 >= r_degeri >= -0.5:
            return("negatif zayıf korelasyon")
        if -0 >= r_degeri >= -0.1:
            return("negatif çok zayıf korelasyon")

#print(korelasyon_orani(r_degeri[0]))

#main_2_8_ozel_alan(4777,tarih_ilk , tarih_son)

def yogunluk_listesi_tarihler_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
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


def yogunluk_listesi_2_8_(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( yogunluk_haritasi_2_8,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    #print(headersiz_data)
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
    if len(hafta_ici) == len(hafta_sonu):
        return(f"Yoğunluğu ortalamanın üstünde olan günler hafta içinde ve hafta sonunda aynıdır. Miktarları {len(hafta_sonu)} olarak ortaya çıkmıştır.")
    if len(hafta_ici) > len(hafta_sonu):
        return ( f"Yoğunluğu ortalamanın üstünde olan günler hafta içinde daha fazladır miktarları sırasıyla {len(hafta_sonu)} ve {len(hafta_ici)} olarak ortaya çıkmıştır." )
    if len ( hafta_sonu ) > len ( hafta_ici ):
        return ( f"Yoğunluğu ortalamanın üstünde olan günler hafta sonunda daha fazladır ve miktarları sırasıyla {len(hafta_sonu)} ve {len(hafta_ici)} olarak ortaya çıkmıştır." )

# hafta_ici_hafta_sonu_oranlari(yogunlugu_fazla_olan_tarihler_2_8[0],yogunlugu_fazla_olan_tarihler_2_8[1])
def main_2_8_edinme_hunisi(huni_id, tarih_ilk , tarih_son): #degeerleri 3s 10s 15s
    data = get_performancetable ( edinme_hunisi_url,huni_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )


    #list_data = json.loads ( data )
    print("_________ edinme hunisii")
    headersiz_data = (data["Data"])
    saniye_3 = headersiz_data[0]
    saniye_10 = headersiz_data[1]
    saniye_15 = headersiz_data[2]

    saniye_3_yuzde = float(100)
    saniye_10_yuzde = round(float(headersiz_data[1])/float(headersiz_data[0])*100)
    saniye_15_yuzde = round(float(headersiz_data[2])/float(headersiz_data[0])*100)

    saniye_liste = [saniye_3,saniye_10,saniye_15]
    print(saniye_liste)
    yuzde_liste = [saniye_3_yuzde,saniye_10_yuzde,saniye_15_yuzde]
    print ( yuzde_liste )
    array = list ( zip ( saniye_liste, yuzde_liste ) )

    # print ( "________________________________" )
    # print ( headersiz_data[0]["Name"] )  # Labels tarih
    # print ( headersiz_data[0]["Serial"] )
    # print ( headersiz_data[4]["Name"] )  # Labels tarih
    # print ( headersiz_data[4]["Serial"] )
    return array


if __name__ == "__main__":

    #main ()
    print("s")
    tarih_ilk = "01/12/2020"
    tarih_son = "25/12/2020"
    #print(main_2_7_performans_tablosu(240, tarih_ilk , tarih_son))
    #boys = (main_2_7_performans_tablosu_double_isim(240, tarih_ilk , tarih_son,"WOMEN'S RUN"))
    #girls = ( main_2_7_performans_tablosu_double_isim ( 240, tarih_ilk, tarih_son, "MEN'S RUN" ) )

    #print(boys)
    # print(girls)
    #
    #print(boys[1][10]) #metrekare
    #print ( boys[1][11] ) #metrekareorani
    # print(boys[1][3])
    # print ( boys[1][6] )
    # print ( girls[1][3] )
    # print ( girls[1][6] )

    ###print(main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "PrevCount" ))

    ## 5 INCISI KISI SAYISI DEGISIMI
    ###print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "PrevDwell" ) )
    ## 7 INCISI ortalama sure degisimi

    ###print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI

    #print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "n_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI # EN AZ OLAN

    #print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "n_15s_Enterance" ) )
    ## 8 INCISI ILGI ORANNI # EN AZ OLAN


    #print ( main_2_7_performans_tablosu_alansal ( magaza_id, tarih_ilk, tarih_son, "Count" ) )

    #3 kisi sayisi

    #6 ortalama sure



    #print(main_2_8_edinme_hunisi ( 11162, tarih_ilk, tarih_son ))#5599 #11162  #9943 #11162 #5605 == > #11151












#############______________1.1_sayfa_yogunluk
#liste = main_1_1_yogunluk_listesi(239, '29/10/2020', '12/11/2020' )
#print(liste)
#liste1 = main_1_1_yogunluk_listesi_tarihler(239, '29/10/2020', '12/11/2020' )
#print(liste1)
#dictionary = dict ( zip ( liste, liste1 ) )### gereksiz
#print(dictionary)### gereksiz
#array = list(zip(liste1,liste))
#print(array)
#print(cal_average_density_arrray(array))
#print(bigger_than_average_arrray(array))

#############______________2.1_saaatlik degerler

#main(saatlik_kisi_sure_grafigi)
#liste = main_2_1_saatler ( 240, '29/10/2020', '12/11/2020' )
#print(liste)
#liste1 = main_2_1_kisi_sure_saatlik ( 240, '29/10/2020', '12/11/2020' )
#print ( liste1 )
#array = list ( zip ( liste, liste1 ) )
#print(array)
#sabah_listesi = array[0:3]
#sabah_ortalmasi = (cal_average_array(sabah_listesi))
#oglen_listesi = array[3:7]
#oglen_ortalmasi = (cal_average_array(oglen_listesi))
#aksam_listesi = array[7:12]
#aksam_ortalmasi = (cal_average_array ( aksam_listesi ))
#print(sabah_ogle_aksam ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ))
#print(max_number_array(array))


##______
#main ( saatlik_kisi_sure_grafigi )
#liste = main_2_1_saatler ( 240, '29/10/2020', '12/11/2020' )
#print ( liste )
#liste1 = main_2_1_kisi_sure_saatlik ( 240, '29/10/2020', '12/11/2020' )
#print ( liste1 )
#array = list ( zip ( liste, liste1 ) )
#print ( array )
#sabah_listesi = array[0:3]
#sabah_ortalmasi = (cal_average_array ( sabah_listesi ))
#oglen_listesi = array[3:7]
#oglen_ortalmasi = (cal_average_array ( oglen_listesi ))
#aksam_listesi = array[7:12]
#aksam_ortalmasi = (cal_average_array ( aksam_listesi ))
#print ( sabah_ogle_aksam ( sabah_ortalmasi, oglen_ortalmasi, aksam_ortalmasi ) )
#print ( max_number_array ( array ) )



# Korelasyon mantigi == https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.pearsonr.html
# Korelasyon aciklamasi == https://www.ck12.org/c/statistics/linear-correlation-and-regression/lesson/Linear-Correlation-Coefficient-PST/#:~:text=Linear%20correlation%20is%20a%20measure,strength%20of%20the%20linear%20relationship.