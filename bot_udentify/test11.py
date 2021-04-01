import request1

def BubleSort(sub_li):
    l = len ( sub_li )
    for i in range ( 0, l ):
        for j in range ( 0, l - i - 1 ):
            if (sub_li[j][2] > sub_li[j + 1][2]):
                tempo = sub_li[j]
                sub_li[j] = sub_li[j + 1]
                sub_li[j + 1] = tempo
    return sub_li


# Driver Code
# sub_li = [['rishav', 10], ['akash', 5], ['ram', 20], ['gaurav', 15]]
#
#
# print ( Sort ( sub_li ) )

liste2 = [[5987, '131 YER BAKIM URUNLERI', -28.08], [5975, '108 AKILLI TELEFONLAR', -13.1], [5893, '5 UHD-LCD TV PALET', 23.87], [5959, '86 NOTEBOOK AKSESUARLARI', -68.62], [5977, '108 SAMSUNG', 4.95], [5885, 'Kasa', 2.22], [5935, '142 CAMASIR MAKINELERI', -13.28], [5965, '75 DIZUSTU BILGISAYARLAR', 34.22], [5923, '124 EV ALETLERI', 16.57], [5979, 'INNOVATION', -22.73], [5936, 'YUVAKURAN', -28.13], [5938, '108 APPLE WHITE', 20.0], [5967, 'SMARTBAR', 8.55], [5962, '71 MASAUSTU BILGISAYARLAR', -15.33], [5922, '128 KISISEL BAKIM', 46.7], [5933, '36 LG', -71.84], [5981, '117 KULAKLIKLAR', -1.16], [5892, '5 SAMSUNG TV', 4.29], [5949, '79 BILGISAYAR OYUN AKSESUARLARI', -2.47], [5928, '134 SOGUTUCU VE BUZDOLAPLARI', -7.69], [5891, '36 BOSCH', -16.18], [5887, '5 UHD-LCD TV DUVAR B', 16.28], [5983, '108 HUAWEI', 10.48], [5978, '108 OPPO', 23.14], [5982, '47 DIGER FOTOGRAF DONANIMLARI', -5.0], [5918, '125 MUTFAK ALETLERI', 23.01], [5931, '134 SOGUTUCU VE BUZDOLAPLARI', -64.86], [5905, 'SNAKEZONE', -22.68], [5921, '125 MUTFAK ALETLERI', 2.15], [5966, 'ACTION AREA', 171.91], [5914, '35 HIFI MIKRO SISTEMLER', 15.91], [5958, '70 MONITOR (TFT)', 8.75], [5943, '94 BILGISAYAR BILESENLERI', 50.63], [5952, '82 KLAVYE VE SETLERI', 97.44], [5968, '104 AKSESUAR GSM', -4.05], [5969, '404 GIYILEBILIR TEKNOLOJI', -12.16], [5926, '123 SEZONLUK URUNLER', 20.9], [5946, '163 KONSOL AKSESUARLARI SONY', -15.15], [5974, '76 TABLET', 30.77], [5973, '108 XIAOMI', 38.46], [5927, '172 ANKASTRE PISIRICILER', 9.38], [5920, '126 KAHVE', 15.25], [5980, '5 UHD-LCD TV ALAN', 79.31], [5912, '5 LG TV', -10.34], [5888, '5 UHD-LCD TV DUVAR A', 17.86], [5915, '127 PISIRME GERECLERI', 66.67], [5925, '118 DIGER AKSESUARLAR', 5.66], [5919, '125 MUTFAK ALETLERI', 32.56], [5909, '12 TASINABILIR SES URUNLERI', 28.57], [5964, '75 LENOVO', 7.32], [5984, '401 KILIF & KORUMA', 2.56], [5913, '6 TV AKSESUARLARI VE MOBILYALARI', 20.51], [5956, '80 DEPOLAMA', 31.58], [5883, '5 PHILIPS TV', 15.79], [5890, '5 VESTEL TV', 18.92], [5989, '403 DEPOLAMA', -8.11], [5971, '108 AKILLI TELEFONLAR', 0.0], [5886, '5 UHD-LCD TV DUVAR C', 59.38], [5954, '90 PC / BILGISAYAR SES', 10.0], [5972, '108 TCL', 7.69], [5970, '75 CASPER', 196.15], [5932, '36 ALTUS', -42.31], [5953, '72 YAZICILAR', 56.0], [5916, '126 KAHVE', 29.17], [5960, '72 YAZICILAR PALET', 4.17], [5985, '104 AKSESUAR GSM', 0.0], [5889, '5 PHILIPS TV', 34.78], [5941, '197 KABLO (IT)', 13.64], [5908, '192 AYDINLATMA', 13.64], [5934, '36 SAMSUNG', -40.0], [5944, '157 KONSOL DONANIM NINTENDO', -15.0], [5942, 'GAMEZONE', 18.75], [5907, '114 PILLER', 14.29], [5906, '118 DIGER AKSESUARLAR', -21.43], [5961, '71 MASAUSTU BILGISAYARLAR PALET', 42.86], [5945, '156 KONSOL DONANIM MICROSOFT', 36.36], [5957, '93 TONER, KARTUS VE KAGIT', 9.09], [5948, 'VR', 50.0], [5955, '89 DIGER BILGISAYAR AKSESUARLARI', 33.33], [5951, '85 NETWORK / AG URUNLERI', 50.0], [5940, '89 DIGER BILGISAYAR AKSESUARLARI', -12.5], [5917, '141 MIKRODALGA FIRINLAR', 25.0], [5947, '89 DIGER BILGISAYAR AKSESUARLARI', 50.0], [5950, '89 DIGER BILGISAYAR AKSESUARLARI', 75.0]]

sorted_list =  (BubleSort ( liste2 ))

print(sorted_list)

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



negatif_liste = negatifse(sorted_list)
pozitif_liste = pozitifse(sorted_list)

print(negatif_liste)
print(pozitif_liste)

son = request1.list_to_string_ve_ile(negatif_liste[2])
print(son)

son = request1.list_to_string_ve_ile(negatif_liste[1])
print(son)