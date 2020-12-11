import requests
import json
import time


APIURL = "https://api.udentify.co"
APIUSER = "delandcaglar@hotmail.com"
APIPASS = "caglar2020"
APITOKEN = ""



magaza_id = 240
tarih_ilk = '15/10/2020'
tarih_son = '30/10/2020'


url1 = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=0"
url_yogunluk = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=0"
ure_yogunluk_g = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=1&tzoffset=0"

saatlik_kisi_sure_grafigi = "{}/Store/{}/EntranceCount?sdate={}&edate={}&stime=10:00&etime=22:00&filter=0&tzoffset=0"
yogunluk_haritasi = "{}/Sketch/{}/Rectangles?sdate=29/10/2020&edate=12/11/2020&stime=10:00&etime=22:00&tzoffset=0&layer=1" ##hatali
performas_tablosu = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1"

deneme_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset=0&layer=1"
deneme2_performans = "{}/Store/{}/AreaTable?sdate={}&edate={}0&stime=10:00&etime=22:00&tzoffset=0&layer=1"

devam = "{}/Rect/9954/CountandSpenttime?sdate=15/11/2020&edate=26/11/2020&stime=10:00&etime=22:00&filter=1&tzoffset=0"



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

    avg = sum_num / (len(num) - cikarilacak_sayilar)
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

    avg = sum_num / (len(num) - cikarilacak_sayilar)
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






def main_2_7_performans_tablosu(magaza_id, tarih_ilk , tarih_son):
    data = get_performancetable ( performas_tablosu,magaza_id, tarih_ilk, tarih_son )  ##240 akasyaya baktigimiz icin
    # print ( data )

    # list_data = json.loads ( data )

    headersiz_data = (data["Data"])
    print ( headersiz_data )


    #yogunluk_haritasi_hesaplama_degerleri_top_5(headersiz_data)

    return (headersiz_data)






print(main_2_7_performans_tablosu(240, tarih_ilk , tarih_son))



if __name__ == "__main__":
    #main ()
    print("s")












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