import matplotlib.pyplot as plt
import request1
import io
from PIL import Image

# magaza_id_no= 118
# ilk_tarih = "01/02/2021"
# son_tarih = "12/02/2021"
#
#
# liste1 = request1.giren_kisi_sayisi_hepsi ( magaza_id_no, ilk_tarih, son_tarih )
# print ( liste1 )
#
# liste_saat = liste1[0]["Serial"]
# print ( liste_saat )
# for element in range ( 0, len ( liste_saat ) ):
#     liste_saat[element] = str ( liste_saat[element] )[-5:]
#
# liste_kisi = liste1[1]["Serial"]
# print ( liste_kisi )
#
#
#
# plt.figure()
# # x axis values
# x = liste_saat
# # corresponding y axis values
# y = liste_kisi
# # plotting the points
# plt.plot ( x, y )  # ,color='red', lw=2
# # plt.fill_between(x,y, 0, alpha=0.30)
# # naming the x axis
# plt.xlabel ( 'Saatler' )
# # naming the y axis
# plt.ylabel ( 'Giren Kişi Sayısı' )
# # giving a title to my graph
# # plt.title ( 'My first graph!' )
# plt.gca ().axes.get_yaxis ().set_visible ( False )
# # function to show the plot
# buf = io.BytesIO ()
# plt.savefig ( buf, format='png' )
# buf.seek ( 0 )
# #im = Image.open ( buf )
#
#
# # im.show ()
# #
# buf.close ()
#
#
#
# plt.figure()
#
# liste_ikinci = request1.store_sure_2_2_saatlik ( magaza_id_no, ilk_tarih, son_tarih )
# saatlik_liste = liste_ikinci[1]["Serial"]
# sure_liste = liste_ikinci[2]["Serial"]
# x = saatlik_liste
# # corresponding y axis values
# y = sure_liste
# print(" x y ")
# print(x)
# print(y)
# plt.plot ( x, y) # ,color='red', lw=2
# plt.fill_between(x,y, 0, alpha=0.30)
# # naming the x axis
# # plt.xlabel ( 'Saatler' )
# # naming the y axis
# plt.ylabel ( 'Giren Kişi Sayısı' )
# # # giving a title to my graph
# # #plt.title ( 'My first graph!' )
# plt.gca().axes.get_yaxis().set_visible(False)
# plt.gca().axes.get_xaxis().set_visible(False)
# # # function to show the plot
# elma = plt.show ()
# # print(plt)
# # figure = io.BytesIO(elma)
# # print(figure)
#
#
#
# #
# # buf = io.BytesIO()
# # plt.savefig(buf, format='png')
# # buf.seek(0)
# # im = Image.open(buf)
# # im.show()
# #
# #
# # buf.close()


liste_1 =['5 UHD-LCD TV PALET', '131 YER BAKIM URUNLERI', '142 CAMASIR MAKINELERI', 'Kasa', '108 APPLE WHITE']
liste_2 = ['131 YER BAKIM URUNLERI', '5 UHD-LCD TV PALET', 'Kasa', '142 CAMASIR MAKINELERI', '125 MUTFAK ALETLERI']

def cakisan_liste_elemanlar(list_1, list_2):
    cakisan_elemanlar_listesi = []
    for element in range(0, len(list_1)):
        if list_1[element] in list_2:
            cakisan_elemanlar_listesi.append(list_1[element])
    return cakisan_elemanlar_listesi

def list_to_string_ve_ile(s):
    # initialize an empty string
    son_part = s[-1:]
    s = s[:-1]

    str1 = " "
    str2 = " "
    elma = [x for y in (s[i:i + 1] + [','] * (i < len ( s ) - 1) for i in range ( 0, len ( s ), 1 )) for x in y]
    elma2 = [x for y in (son_part[i:i + 1] + [','] * (i < len ( son_part ) - 1) for i in range ( 0, len ( son_part ), 1 )) for x in y]
    # return string
    final_form2 = (str2.join ( elma2 ))
    final_form = (str1.join ( elma ))
    final_form = f"{final_form} ve {(final_form2)}"
    return final_form



x = (cakisan_liste_elemanlar(liste_1, liste_2))
print(x) #['5 UHD-LCD TV PALET', '131 YER BAKIM URUNLERI', '142 CAMASIR MAKINELERI', 'Kasa']

elma =list_to_string_ve_ile(x)
print("cakisan_listeler")
print(elma)


yogunluk_haritasi = "{}/Sketch/{}/Rectangles?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset={}&layer=1"  ##hatali
json =  request1.get_performancetable ( yogunluk_haritasi, 234, '22/02/2021', '26/02/2021' )

json = json["Data"]


# json =  [{'Id': 5883, 'Name': '5 PHILIPS TV', 'Corners': '[{"x":133.29,"y":183.94},{"x":188.29,"y":184.94},{"x":189.29,"y":233.94},{"x":133.29,"y":233.94}]', 'Area': 2747.0, 'DataStatus': 4, 'InterestScore': 28050, 'CountRatio': 0.006130618826050871, 'DwellRatio': 0.009092491272042296, 'Over15SecRatio': 0.0038650288647829978, 'DensityRatio': 0.004119419392645139, 'M2Ratio': 0.006415689502114935, 'SketchRectDepartments': [{'Id': 11596, 'Name': '5 PHILIPS TV', 'CameraId': 1513, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5885, 'Name': 'Kasa', 'Corners': '[{"x":138.3,"y":479.57},{"x":167.29,"y":480.39},{"x":168.29,"y":627.39},{"x":138.3,"y":633.57}]', 'Area': 4439.58, 'DataStatus': 4, 'InterestScore': 259892, 'CountRatio': 0.0144104206654346, 'DwellRatio': 0.03584001298086605, 'Over15SecRatio': 0.03433286454696551, 'DensityRatio': 0.038167490743468466, 'M2Ratio': 0.010368753840480315, 'SketchRectDepartments': [{'Id': 11590, 'Name': 'Kasa', 'CameraId': 1500, 'Archived': False, 'DataStatus': 4}]}, {'Id': 5886, 'Name': '5 UHD-LCD TV DUVAR C', 'Corners': '[{"x":257.29,"y":2.94},{"x":354.29,"y":3.94},{"x":355.29,"y":60.94},{"x":257.29,"y":59.94}]', 'Area': 5557.0, 'DataStatus': 4, 'InterestScore': 23097, 'CountRatio': 0.004583603219218648, 'DwellRatio': 0.010014018913573139, 'Over15SecRatio': 0.0034913110610635223, 'DensityRatio': 0.003392065387940608, 'M2Ratio': 0.012978517132600181, 'SketchRectDepartments': [{'Id': 11602, 'Name': '5 UHD-LCD TV DUVAR C', 'CameraId': 1528, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5887, 'Name': '5 UHD-LCD TV DUVAR B', 'Corners': '[{"x":133.29,"y":114.76},{"x":188.29,"y":115.76},{"x":188.29,"y":61.76},{"x":257.29,"y":61.76},{"x":256.84,"y":5.4},{"x":134.29,"y":4.76}]', 'Area': 9903.31, 'DataStatus': 4, 'InterestScore': 94346, 'CountRatio': 0.007576612927187264, 'DwellRatio': 0.024745754077496237, 'Over15SecRatio': 0.01533226463154375, 'DensityRatio': 0.01385557574585742, 'M2Ratio': 0.023129436477317022, 'SketchRectDepartments': [{'Id': 11601, 'Name': '5 UHD-LCD TV DUVAR B', 'CameraId': 1527, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5888, 'Name': '5 UHD-LCD TV DUVAR A', 'Corners': '[{"x":134.29,"y":182.76},{"x":187.29,"y":182.76},{"x":188.29,"y":115.76},{"x":135.29,"y":113.76}]', 'Area': 3605.0, 'DataStatus': 4, 'InterestScore': 42278, 'CountRatio': 0.0050332479602569515, 'DwellRatio': 0.016692546323303234, 'Over15SecRatio': 0.007139976986851034, 'DensityRatio': 0.006208972228091631, 'M2Ratio': 0.008419570678967725, 'SketchRectDepartments': [{'Id': 11600, 'Name': '5 UHD-LCD TV DUVAR A', 'CameraId': 1526, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5889, 'Name': '5 PHILIPS TV', 'Corners': '[{"x":188.29,"y":99.94},{"x":280.29,"y":98.76},{"x":280.29,"y":60.39},{"x":188.29,"y":60.94}]', 'Area': 3559.02, 'DataStatus': 4, 'InterestScore': 17243, 'CountRatio': 0.003953704418997589, 'DwellRatio': 0.008667211723629976, 'Over15SecRatio': 0.002665198021262576, 'DensityRatio': 0.0025324005827719923, 'M2Ratio': 0.00831218320051587, 'SketchRectDepartments': [{'Id': 11603, 'Name': '5 PHILIPS TV', 'CameraId': 1527, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5890, 'Name': '5 VESTEL TV', 'Corners': '[{"x":188.29,"y":149.57},{"x":266.97,"y":146.91},{"x":264.94,"y":99.29},{"x":189.29,"y":99.57}]', 'Area': 3767.18, 'DataStatus': 4, 'InterestScore': 26350, 'CountRatio': 0.004510313107243242, 'DwellRatio': 0.011609865611094864, 'Over15SecRatio': 0.004022383729506988, 'DensityRatio': 0.003869747998708825, 'M2Ratio': 0.008798346260858151, 'SketchRectDepartments': [{'Id': 11604, 'Name': '5 VESTEL TV', 'CameraId': 1527, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11598, 'Name': '5 VESTEL TV', 'CameraId': 1526, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5891, 'Name': '36 BOSCH', 'Corners': '[{"x":846.29,"y":222.39},{"x":988.29,"y":222.39},{"x":988.29,"y":356.39},{"x":860.29,"y":355.39},{"x":846.29,"y":355.39}]', 'Area': 18950.0, 'DataStatus': 4, 'InterestScore': 92054, 'CountRatio': 0.00892950877797652, 'DwellRatio': 0.020486421449261515, 'Over15SecRatio': 0.01674845841405966, 'DensityRatio': 0.013518934680206195, 'M2Ratio': 0.04425821480345032, 'SketchRectDepartments': [{'Id': 11592, 'Name': '36 BOSCH', 'CameraId': 1519, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5892, 'Name': '5 SAMSUNG TV', 'Corners': '[{"x":282.67,"y":304.12},{"x":280.29,"y":147.76},{"x":188.29,"y":148.39},{"x":189.97,"y":233.7},{"x":226.44,"y":233.7},{"x":226.44,"y":305.3}]', 'Area': 11817.2, 'DataStatus': 4, 'InterestScore': 107522, 'CountRatio': 0.023147790501205325, 'DwellRatio': 0.009230788588766456, 'Over15SecRatio': 0.01667961566074291, 'DensityRatio': 0.015790546671897634, 'M2Ratio': 0.027599376040914676, 'SketchRectDepartments': [{'Id': 11599, 'Name': '5 SAMSUNG TV', 'CameraId': 1526, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11606, 'Name': '5 SAMSUNG TV', 'CameraId': 1513, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5893, 'Name': '5 UHD-LCD TV PALET', 'Corners': '[{"x":280.29,"y":96.76},{"x":407.29,"y":97.66},{"x":406.29,"y":303.66},{"x":283.9,"y":304.12}]', 'Area': 25771.67, 'DataStatus': 4, 'InterestScore': 327874, 'CountRatio': 0.046305485071596514, 'DwellRatio': 0.014071044187369146, 'Over15SecRatio': 0.04878000806443682, 'DensityRatio': 0.048151250721319955, 'M2Ratio': 0.060190401409162875, 'SketchRectDepartments': [{'Id': 11607, 'Name': '5 UHD-LCD TV PALET', 'CameraId': 1525, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11608, 'Name': '5 UHD-LCD TV PALET', 'CameraId': 1524, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11609, 'Name': '5 UHD-LCD TV PALET', 'CameraId': 1514, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11610, 'Name': '5 UHD-LCD TV PALET', 'CameraId': 1524, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5905, 'Name': 'SNAKEZONE', 'Corners': '[{"x":182.29,"y":457.39},{"x":208.29,"y":456.39},{"x":230.29,"y":457.39},{"x":233.29,"y":620.85},{"x":203.29,"y":621.85},{"x":186.29,"y":623.39},{"x":182.45,"y":504}]', 'Area': 7918.46, 'DataStatus': 4, 'InterestScore': 56783, 'CountRatio': 0.011985904528734676, 'DwellRatio': 0.009414520862906674, 'Over15SecRatio': 0.009480630599620381, 'DensityRatio': 0.008339074195684701, 'M2Ratio': 0.018493767999605764, 'SketchRectDepartments': [{'Id': 11661, 'Name': 'SNAKEZONE', 'CameraId': 1500, 'DepartmentId': 2368, 'DepartmentName': 'SNAKEZONE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5906, 'Name': '118 DIGER AKSESUARLAR', 'Corners': '[{"x":167.93,"y":527.01},{"x":182.53,"y":528.47},{"x":186.29,"y":623.39},{"x":167.93,"y":627.74}]', 'Area': 1614.87, 'DataStatus': 4, 'InterestScore': 9975, 'CountRatio': 0.00171538478299194, 'DwellRatio': 0.011556998615069501, 'Over15SecRatio': 0.0015342099310588998, 'DensityRatio': 0.0014650600731699256, 'M2Ratio': 0.003771570624783526, 'SketchRectDepartments': [{'Id': 11663, 'Name': '118 DIGER AKSESUARLAR', 'CameraId': 1500, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5907, 'Name': '114 PILLER', 'Corners': '[{"x":166.47,"y":478.83},{"x":182.53,"y":478.83},{"x":181.07,"y":528.47},{"x":166.47,"y":527.01}]', 'Area': 750.32, 'DataStatus': 4, 'InterestScore': 10045, 'SaleQuantity': 152, 'SaleTotalAmount': 1959.2, 'CountRatio': 0.001756981873572576, 'DwellRatio': 0.01136253462967068, 'Over15SecRatio': 0.0014850365358326531, 'DensityRatio': 0.0014753372390372162, 'SaleQuantityRatio': 0.145038173, 'SaleTotalAmountRatio': 0.00166421779, 'M2Ratio': 0.0017523917536319178, 'SketchRectDepartments': [{'Id': 11662, 'Name': '114 PILLER', 'CameraId': 1500, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5908, 'Name': '192 AYDINLATMA', 'Corners': '[{"x":156.25,"y":478.83},{"x":156.25,"y":467.15},{"x":182.53,"y":467.15},{"x":182.53,"y":478.83}]', 'Area': 306.95, 'DataStatus': 4, 'InterestScore': 15494, 'SaleQuantity': 40, 'SaleTotalAmount': 2279.59985, 'CountRatio': 0.008497691361472775, 'DwellRatio': 0.0036234228052564213, 'Over15SecRatio': 0.0015243752520136505, 'DensityRatio': 0.002275458218814393, 'SaleQuantityRatio': 0.03816794, 'SaleTotalAmountRatio': 0.00193637749, 'M2Ratio': 0.0007168896587820093, 'SketchRectDepartments': [{'Id': 11660, 'Name': '192 AYDINLATMA', 'CameraId': 1502, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5909, 'Name': '12 TASINABILIR SES URUNLERI', 'Corners': '[{"x":182.29,"y":416.39},{"x":183.29,"y":456.39},{"x":231.29,"y":457.39},{"x":231.29,"y":416.39}]', 'Area': 1964.0, 'DataStatus': 4, 'InterestScore': 29518, 'CountRatio': 0.011708590591530435, 'DwellRatio': 0.005010015680287215, 'Over15SecRatio': 0.0038551941857377483, 'DensityRatio': 0.004335034273797448, 'M2Ratio': 0.004586972763798229, 'SketchRectDepartments': [{'Id': 11659, 'Name': '12 TASINABILIR SES URUNLERI', 'CameraId': 1502, 'DepartmentId': 2360, 'DepartmentName': '6 TASINABILIR SES', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5912, 'Name': '5 LG TV', 'Corners': '[{"x":135.26,"y":307.33},{"x":226.44,"y":305.3},{"x":227.46,"y":234.38},{"x":135.26,"y":234.38}]', 'Area': 6595.2, 'DataStatus': 4, 'InterestScore': 40560, 'CountRatio': 0.008061912317294685, 'DwellRatio': 0.00999815159140187, 'Over15SecRatio': 0.006530226886045574, 'DensityRatio': 0.00595671171677549, 'M2Ratio': 0.015403260067108999, 'SketchRectDepartments': [{'Id': 11605, 'Name': '5 LG TV', 'CameraId': 1513, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5913, 'Name': '6 TV AKSESUARLARI VE MOBILYALARI', 'Corners': '[{"x":265.96,"y":148.94},{"x":265.96,"y":97.26},{"x":279.13,"y":97.26},{"x":282.17,"y":146.91}]', 'Area': 745.81, 'DataStatus': 4, 'InterestScore': 25395, 'CountRatio': 0.010650836002479978, 'DwellRatio': 0.004738368047700461, 'Over15SecRatio': 0.0028225528859865657, 'DensityRatio': 0.0037295920110393854, 'M2Ratio': 0.0017418585320612813, 'SketchRectDepartments': [{'Id': 11667, 'Name': '6 TV AKSESUARLARI VE MOBILYALARI', 'CameraId': 1525, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}, {'Id': 11668, 'Name': '6 TV AKSESUARLARI VE MOBILYALARI', 'CameraId': 1526, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5914, 'Name': '35 HIFI MIKRO SISTEMLER', 'Corners': '[{"x":407.8,"y":63.15},{"x":280.14,"y":60.79},{"x":280.14,"y":98.62},{"x":407.8,"y":96.59}]', 'Area': 4549.16, 'DataStatus': 4, 'InterestScore': 60001, 'CountRatio': 0.011060864466774819, 'DwellRatio': 0.010780174009285552, 'Over15SecRatio': 0.009854348403339857, 'DensityRatio': 0.008811779767995609, 'M2Ratio': 0.010624680762810769, 'SketchRectDepartments': [{'Id': 11669, 'Name': '35 HIFI MIKRO SISTEMLER', 'CameraId': 1525, 'DepartmentId': 2337, 'DepartmentName': '18 HIFI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5915, 'Name': '127 PISIRME GERECLERI', 'Corners': '[{"x":446.29,"y":63.66},{"x":406.29,"y":63.66},{"x":407.29,"y":169.94},{"x":446.29,"y":169.94}]', 'Area': 4198.06, 'DataStatus': 4, 'InterestScore': 38182, 'CountRatio': 0.00824216637647744, 'DwellRatio': 0.009205993389761467, 'Over15SecRatio': 0.006510557527955075, 'DensityRatio': 0.005607390878318008, 'M2Ratio': 0.009804677637877185, 'SketchRectDepartments': [{'Id': 11622, 'Name': '127 PISIRME GERECLERI', 'CameraId': 1529, 'DepartmentId': 2348, 'DepartmentName': '32 PISIRME GERECLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5916, 'Name': '126 KAHVE', 'Corners': '[{"x":465.29,"y":169.94},{"x":463.29,"y":62.94},{"x":444.29,"y":62.85},{"x":447.29,"y":169.94}]', 'Area': 1980.22, 'DataStatus': 4, 'InterestScore': 17696, 'CountRatio': 0.00295141261738798, 'DwellRatio': 0.011915398845202659, 'Over15SecRatio': 0.003402798949656278, 'DensityRatio': 0.0025988864148874503, 'M2Ratio': 0.004624854993038966, 'SketchRectDepartments': [{'Id': 11613, 'Name': '126 KAHVE', 'CameraId': 1529, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5917, 'Name': '141 MIKRODALGA FIRINLAR', 'Corners': '[{"x":482.29,"y":169.94},{"x":479.29,"y":62.94},{"x":464.29,"y":63.57},{"x":467.29,"y":169.94}]', 'Area': 1601.22, 'DataStatus': 4, 'InterestScore': 3007, 'CountRatio': 0.0019015812836862154, 'DwellRatio': 0.0031431865015823486, 'Over15SecRatio': 0.0003147097294479795, 'DensityRatio': 0.0004417066558881059, 'M2Ratio': 0.0037396906969699587, 'SketchRectDepartments': [{'Id': 11614, 'Name': '141 MIKRODALGA FIRINLAR', 'CameraId': 1529, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5918, 'Name': '125 MUTFAK ALETLERI', 'Corners': '[{"x":407.29,"y":62.39},{"x":405.29,"y":-0.61},{"x":557.29,"y":-6.06},{"x":558.29,"y":60.94},{"x":500.29,"y":61.48},{"x":500.29,"y":168.48},{"x":483.29,"y":168.39},{"x":478.29,"y":63.48}]', 'Area': 12002.89, 'DataStatus': 4, 'InterestScore': 78254, 'CountRatio': 0.016264462417028662, 'DwellRatio': 0.009561427024569608, 'Over15SecRatio': 0.01365053451480611, 'DensityRatio': 0.01149241356225386, 'M2Ratio': 0.028033059835471545, 'SketchRectDepartments': [{'Id': 11618, 'Name': '125 MUTFAK ALETLERI', 'CameraId': 1529, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}, {'Id': 11612, 'Name': '125 MUTFAK ALETLERI', 'CameraId': 1529, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5919, 'Name': '125 MUTFAK ALETLERI', 'Corners': '[{"x":407.29,"y":302.39},{"x":440.29,"y":303.39},{"x":439.29,"y":170.39},{"x":407.29,"y":169.39}]', 'Area': 4322.0, 'DataStatus': 4, 'InterestScore': 29212, 'CountRatio': 0.008256032073337652, 'DwellRatio': 0.007031610441614152, 'Over15SecRatio': 0.004809158053126936, 'DensityRatio': 0.004290174841304985, 'M2Ratio': 0.01009414271137268, 'SketchRectDepartments': [{'Id': 11615, 'Name': '125 MUTFAK ALETLERI', 'CameraId': 1524, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5920, 'Name': '126 KAHVE', 'Corners': '[{"x":465.29,"y":304.48},{"x":462.29,"y":171.48},{"x":439.29,"y":170.94},{"x":441.29,"y":301.48}]', 'Area': 3092.17, 'DataStatus': 4, 'InterestScore': 40073, 'CountRatio': 0.007606325134744862, 'DwellRatio': 0.010469778046892217, 'Over15SecRatio': 0.007395678642027517, 'DensityRatio': 0.005885198914273673, 'M2Ratio': 0.007221842958774933, 'SketchRectDepartments': [{'Id': 11670, 'Name': '126 KAHVE', 'CameraId': 1524, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5921, 'Name': '125 MUTFAK ALETLERI', 'Corners': '[{"x":501.29,"y":300.48},{"x":499.29,"y":169.48},{"x":463.29,"y":170.48},{"x":465.29,"y":301.39}]', 'Area': 4716.29, 'DataStatus': 4, 'InterestScore': 59219, 'CountRatio': 0.013695346870215097, 'DwellRatio': 0.008592921434885515, 'Over15SecRatio': 0.009372449130122638, 'DensityRatio': 0.008696864370460654, 'M2Ratio': 0.011015017197644576, 'SketchRectDepartments': [{'Id': 11617, 'Name': '125 MUTFAK ALETLERI', 'CameraId': 1524, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5922, 'Name': '128 KISISEL BAKIM', 'Corners': '[{"x":590.29,"y":59.94},{"x":500.29,"y":62.48},{"x":501.29,"y":168.48},{"x":591.29,"y":168.94}]', 'Area': 9676.04, 'DataStatus': 4, 'InterestScore': 113868, 'CountRatio': 0.01886923261291134, 'DwellRatio': 0.011992179187919621, 'Over15SecRatio': 0.02005291057326344, 'DensityRatio': 0.01672249822446833, 'M2Ratio': 0.02259864151803575, 'SketchRectDepartments': [{'Id': 11619, 'Name': '128 KISISEL BAKIM', 'CameraId': 1530, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5923, 'Name': '124 EV ALETLERI', 'Corners': '[{"x":501.29,"y":299.48},{"x":591.29,"y":299.94},{"x":591.29,"y":167.94},{"x":501.29,"y":169.48}]', 'Area': 11790.0, 'DataStatus': 4, 'InterestScore': 215196, 'CountRatio': 0.025483170015232457, 'DwellRatio': 0.016781546189543594, 'Over15SecRatio': 0.0352081509819927, 'DensityRatio': 0.031603429070527995, 'M2Ratio': 0.027535849737872257, 'SketchRectDepartments': [{'Id': 11620, 'Name': '124 EV ALETLERI', 'CameraId': 1523, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5925, 'Name': '118 DIGER AKSESUARLAR', 'Corners': '[{"x":183.29,"y":422.85},{"x":138.29,"y":422.85},{"x":138.29,"y":478.85},{"x":156.29,"y":478.85},{"x":156.29,"y":469.85},{"x":182.29,"y":468.85}]', 'Area': 2240.0, 'DataStatus': 4, 'InterestScore': 37825, 'CountRatio': 0.010205152889116022, 'DwellRatio': 0.007365753212036945, 'Over15SecRatio': 0.005635271092927882, 'DensityRatio': 0.005555018159089755, 'M2Ratio': 0.005231577897611014, 'SketchRectDepartments': [{'Id': 11664, 'Name': '118 DIGER AKSESUARLAR', 'CameraId': 1502, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5926, 'Name': '123 SEZONLUK URUNLER', 'Corners': '[{"x":643.29,"y":59.94},{"x":645.29,"y":-1.06},{"x":558.29,"y":-0.06},{"x":558.29,"y":59.94}]', 'Area': 5202.5, 'DataStatus': 4, 'InterestScore': 43230, 'CountRatio': 0.01091032261514966, 'DwellRatio': 0.007874095423059784, 'Over15SecRatio': 0.0057041138462446276, 'DensityRatio': 0.00634873316608712, 'M2Ratio': 0.012150573219786295, 'SketchRectDepartments': [{'Id': 11674, 'Name': '123 SEZONLUK URUNLER', 'CameraId': 1530, 'DepartmentId': 2349, 'DepartmentName': '33 KUCUK EV ESYALARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5927, 'Name': '172 ANKASTRE PISIRICILER', 'Corners': '[{"x":743.29,"y":-0.06},{"x":744.29,"y":60.94},{"x":643.29,"y":60.94},{"x":643.29,"y":-2.06}]', 'Area': 6230.5, 'DataStatus': 4, 'InterestScore': 44347, 'CountRatio': 0.0102289226551621, 'DwellRatio': 0.008615656972002693, 'Over15SecRatio': 0.006510557527955075, 'DensityRatio': 0.0065127903933236, 'M2Ratio': 0.014551493790654206, 'SketchRectDepartments': [{'Id': 11675, 'Name': '172 ANKASTRE PISIRICILER', 'CameraId': 1630, 'DepartmentId': 2352, 'DepartmentName': '39 ANKASTRE URUNLER', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5928, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'Corners': '[{"x":945.29,"y":221.76},{"x":944.29,"y":53.94},{"x":761.29,"y":53.94},{"x":762.29,"y":170.39},{"x":720.29,"y":169.94},{"x":719.29,"y":60.94},{"x":744.29,"y":58.94},{"x":747.29,"y":19.94},{"x":986.29,"y":18.94},{"x":991.29,"y":221.94}]', 'Area': 20498.99, 'DataStatus': 4, 'InterestScore': 97729, 'CountRatio': 0.015509772345065693, 'DwellRatio': 0.012521908574843262, 'Over15SecRatio': 0.018194156233711314, 'DensityRatio': 0.01435240725141609, 'M2Ratio': 0.04787592098542375, 'SketchRectDepartments': [{'Id': 11677, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'CameraId': 1631, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11593, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'CameraId': 1520, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11594, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'CameraId': 1632, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5931, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'Corners': '[{"x":881.29,"y":84.94},{"x":881.29,"y":104.94},{"x":851.29,"y":103.94},{"x":847.29,"y":83.94}]', 'Area': 638.0, 'DataStatus': 4, 'InterestScore': 75832, 'CountRatio': 0.00470443286328621, 'DwellRatio': 0.032032922109146385, 'Over15SecRatio': 0.003048750504027301, 'DensityRatio': 0.011136600104433805, 'M2Ratio': 0.00149006549048028, 'SketchRectDepartments': [{'Id': 11679, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'CameraId': 1632, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11680, 'Name': '134 SOGUTUCU VE BUZDOLAPLARI', 'CameraId': 1631, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5932, 'Name': '36 ALTUS', 'Corners': '[{"x":882.29,"y":94.57},{"x":944.29,"y":94.57},{"x":943.29,"y":53.57},{"x":848.29,"y":52.57},{"x":847.29,"y":83.57},{"x":881.29,"y":84.57}]', 'Area': 3627.5, 'DataStatus': 4, 'InterestScore': 17005, 'CountRatio': 0.002190780103913494, 'DwellRatio': 0.015425915460241788, 'Over15SecRatio': 0.00291106499739381, 'DensityRatio': 0.002497459981126583, 'M2Ratio': 0.00847212001052855, 'SketchRectDepartments': [{'Id': 11678, 'Name': '36 ALTUS', 'CameraId': 1632, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5933, 'Name': '36 LG', 'Corners': '[{"x":943.29,"y":134.94},{"x":846.29,"y":134.94},{"x":846.29,"y":103.94},{"x":883.29,"y":102.94},{"x":881.29,"y":93.94},{"x":946.29,"y":92.94}]', 'Area': 3727.0, 'DataStatus': 4, 'InterestScore': 141057, 'CountRatio': 0.004205267776318578, 'DwellRatio': 0.0666579241895002, 'Over15SecRatio': 0.006313863947050088, 'DensityRatio': 0.020715442978003575, 'M2Ratio': 0.008704504832319755, 'SketchRectDepartments': [{'Id': 11681, 'Name': '36 LG', 'CameraId': 1632, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5934, 'Name': '36 SAMSUNG', 'Corners': '[{"x":846.29,"y":175.94},{"x":944.29,"y":175.94},{"x":943.29,"y":134.94},{"x":845.29,"y":134.94}]', 'Area': 4018.0, 'DataStatus': 4, 'InterestScore': 12637, 'CountRatio': 0.0027572928613450124, 'DwellRatio': 0.00910820208800095, 'Over15SecRatio': 0.002252141501362103, 'DensityRatio': 0.0018559418996303108, 'M2Ratio': 0.009384142853839756, 'SketchRectDepartments': [{'Id': 11682, 'Name': '36 SAMSUNG', 'CameraId': 1520, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5935, 'Name': '142 CAMASIR MAKINELERI', 'Corners': '[{"x":720.29,"y":299.39},{"x":846.29,"y":299.39},{"x":844.29,"y":160.39},{"x":799.29,"y":159.39},{"x":800.29,"y":115.39},{"x":847.29,"y":115.39},{"x":845.29,"y":53.39},{"x":761.29,"y":53.39},{"x":762.29,"y":170.39},{"x":721.29,"y":170.39}]', 'Area': 23866.5, 'DataStatus': 4, 'InterestScore': 224719, 'CountRatio': 0.03248138530196516, 'DwellRatio': 0.013748535045417395, 'Over15SecRatio': 0.03858144589451323, 'DensityRatio': 0.03300196365975645, 'M2Ratio': 0.05574082763095235, 'SketchRectDepartments': [{'Id': 11683, 'Name': '142 CAMASIR MAKINELERI', 'CameraId': 1522, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11684, 'Name': '142 CAMASIR MAKINELERI', 'CameraId': 1521, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11676, 'Name': '142 CAMASIR MAKINELERI', 'CameraId': 1631, 'DepartmentId': 2351, 'DepartmentName': '36 BUYUK ELEKTRIKLI EV ALETLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5936, 'Name': 'YUVAKURAN', 'Corners': '[{"x":847.29,"y":114.94},{"x":799.29,"y":116.39},{"x":800.29,"y":159.94},{"x":846.29,"y":159.94}]', 'Area': 2080.92, 'DataStatus': 4, 'InterestScore': 226288, 'CountRatio': 0.021911762666809286, 'DwellRatio': 0.02052275396522209, 'Over15SecRatio': 0.03235609405887039, 'DensityRatio': 0.033232403918077996, 'M2Ratio': 0.004860042445846746, 'SketchRectDepartments': [{'Id': 11685, 'Name': 'YUVAKURAN', 'CameraId': 1521, 'DepartmentId': 2367, 'DepartmentName': 'HİZMET ALANI', 'Archived': False, 'DataStatus': 4}, {'Id': 11686, 'Name': 'YUVAKURAN', 'CameraId': 1631, 'DepartmentId': 2367, 'DepartmentName': 'HİZMET ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5938, 'Name': '108 APPLE WHITE', 'Corners': '[{"x":478.29,"y":360.39},{"x":519.29,"y":359.94},{"x":520.29,"y":480.94},{"x":478.29,"y":480.94}]', 'Area': 5012.27, 'DataStatus': 4, 'InterestScore': 212161, 'CountRatio': 0.02938339246062637, 'DwellRatio': 0.014348766468144255, 'Over15SecRatio': 0.03667351815973486, 'DensityRatio': 0.031157692614248368, 'M2Ratio': 0.011706286137883373, 'SketchRectDepartments': [{'Id': 11698, 'Name': '108 APPLE WHITE', 'CameraId': 1510, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}, {'Id': 11699, 'Name': '108 APPLE WHITE', 'CameraId': 1509, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5940, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'Corners': '[{"x":826.32,"y":299.27},{"x":826.32,"y":391.24},{"x":845.3,"y":391.24},{"x":845.3,"y":299.27}]', 'Area': 1745.59, 'DataStatus': 4, 'InterestScore': 6731, 'CountRatio': 0.0018916772145003496, 'DwellRatio': 0.007071479396032854, 'Over15SecRatio': 0.0011899961644751724, 'DensityRatio': 0.0009885670171820042, 'M2Ratio': 0.004076870563522683, 'SketchRectDepartments': [{'Id': 11690, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5941, 'Name': '197 KABLO (IT)', 'Corners': '[{"x":808.8,"y":299.27},{"x":807.34,"y":391.24},{"x":826.32,"y":391.24},{"x":824.86,"y":299.27}]', 'Area': 1611.31, 'DataStatus': 4, 'InterestScore': 15798, 'CountRatio': 0.0026899451908811256, 'DwellRatio': 0.011671616341176031, 'Over15SecRatio': 0.0027340407745793218, 'DensityRatio': 0.0023201884157257866, 'M2Ratio': 0.00376325615276768, 'SketchRectDepartments': [{'Id': 11689, 'Name': '197 KABLO (IT)', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5942, 'Name': 'GAMEZONE', 'Corners': '[{"x":765.01,"y":299.27},{"x":765.01,"y":369.34},{"x":807.34,"y":369.34},{"x":807.34,"y":300.73}]', 'Area': 2935.16, 'DataStatus': 4, 'InterestScore': 10979, 'CountRatio': 0.00428846195747985, 'DwellRatio': 0.00508800392992718, 'Over15SecRatio': 0.0014948712148779024, 'DensityRatio': 0.0016124929052052446, 'M2Ratio': 0.006855142045514261, 'SketchRectDepartments': [{'Id': 11687, 'Name': 'GAMEZONE', 'CameraId': 1518, 'DepartmentId': 2366, 'DepartmentName': 'MÜŞTERİ ALANI', 'Archived': False, 'DataStatus': 4}, {'Id': 11688, 'Name': 'GAMEZONE', 'CameraId': 1507, 'DepartmentId': 2366, 'DepartmentName': 'MÜŞTERİ ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5943, 'Name': '94 BILGISAYAR BILESENLERI', 'Corners': '[{"x":734.35,"y":451.82},{"x":805.89,"y":451.09},{"x":807.34,"y":369.34},{"x":732.89,"y":368.61}]', 'Area': 6020.62, 'DataStatus': 4, 'InterestScore': 52693, 'CountRatio': 0.0105755650766674, 'DwellRatio': 0.009901504992132337, 'Over15SecRatio': 0.00797592470569723, 'DensityRatio': 0.007738443021149166, 'M2Ratio': 0.014061313625854832, 'SketchRectDepartments': [{'Id': 11705, 'Name': '94 BILGISAYAR BILESENLERI', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5944, 'Name': '157 KONSOL DONANIM NINTENDO', 'Corners': '[{"x":873.04,"y":401.46},{"x":846.76,"y":401.46},{"x":845.3,"y":356.2},{"x":874.5,"y":357.66}]', 'Area': 1235.26, 'DataStatus': 4, 'InterestScore': 15668, 'CountRatio': 0.0021828568485648013, 'DwellRatio': 0.014264704573560886, 'Over15SecRatio': 0.0026750327003078255, 'DensityRatio': 0.0023011070758981638, 'M2Ratio': 0.002884981657947759, 'SketchRectDepartments': [{'Id': 11691, 'Name': '157 KONSOL DONANIM NINTENDO', 'CameraId': 1507, 'DepartmentId': 2357, 'DepartmentName': '53 KONSOL DONANIM', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5945, 'Name': '156 KONSOL DONANIM MICROSOFT', 'Corners': '[{"x":846.76,"y":400},{"x":846.76,"y":437.96},{"x":871.58,"y":435.04},{"x":871.58,"y":400}]', 'Area': 905.93, 'DataStatus': 4, 'InterestScore': 7496, 'CountRatio': 0.0019867562786846605, 'DwellRatio': 0.007498340058490565, 'Over15SecRatio': 0.0014260284615611569, 'DensityRatio': 0.0011009270748185474, 'M2Ratio': 0.002115822930706583, 'SketchRectDepartments': [{'Id': 11693, 'Name': '156 KONSOL DONANIM MICROSOFT', 'CameraId': 1507, 'DepartmentId': 2357, 'DepartmentName': '53 KONSOL DONANIM', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5946, 'Name': '163 KONSOL AKSESUARLARI SONY', 'Corners': '[{"x":873.04,"y":472.99},{"x":846.76,"y":455.47},{"x":846.76,"y":436.5},{"x":874.5,"y":435.04}]', 'Area': 774.56, 'DataStatus': 4, 'InterestScore': 56676, 'CountRatio': 0.005894901979427268, 'DwellRatio': 0.019106483098001715, 'Over15SecRatio': 0.0067269204669505615, 'DensityRatio': 0.008323502776752024, 'M2Ratio': 0.00180900490016678, 'SketchRectDepartments': [{'Id': 11694, 'Name': '163 KONSOL AKSESUARLARI SONY', 'CameraId': 1507, 'DepartmentId': 2358, 'DepartmentName': '55 KONSOL AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5947, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'Corners': '[{"x":805.89,"y":404.38},{"x":846.76,"y":404.38},{"x":846.76,"y":391.24},{"x":807.34,"y":391.24}]', 'Area': 527.5, 'DataStatus': 4, 'InterestScore': 2857, 'CountRatio': 0.0012895098079997148, 'DwellRatio': 0.004403088600746304, 'Over15SecRatio': 0.00034421376658372755, 'DensityRatio': 0.00041959562283610163, 'M2Ratio': 0.0012319898843704507, 'SketchRectDepartments': [{'Id': 11692, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5948, 'Name': 'VR', 'Corners': '[{"x":845.3,"y":451.09},{"x":805.89,"y":451.09},{"x":805.89,"y":404.38},{"x":845.3,"y":404.38}]', 'Area': 1840.84, 'DataStatus': 4, 'InterestScore': 6187, 'CountRatio': 0.00216304871019307, 'DwellRatio': 0.005684521339839293, 'Over15SecRatio': 0.0007080968912579538, 'DensityRatio': 0.0009086759307029239, 'M2Ratio': 0.004299329400463509, 'SketchRectDepartments': [{'Id': 11695, 'Name': 'VR', 'CameraId': 1507, 'DepartmentId': 2366, 'DepartmentName': 'MÜŞTERİ ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5949, 'Name': '79 BILGISAYAR OYUN AKSESUARLARI', 'Corners': '[{"x":697.86,"y":509.49},{"x":678.88,"y":471.53},{"x":735.81,"y":451.82},{"x":848.22,"y":451.09},{"x":849.68,"y":458.39},{"x":878.88,"y":478.83},{"x":805.89,"y":478.83}]', 'Area': 6265.23, 'DataStatus': 4, 'InterestScore': 120760, 'CountRatio': 0.019841812206963353, 'DwellRatio': 0.01209471583830622, 'Over15SecRatio': 0.016728789055969157, 'DensityRatio': 0.017734779970776517, 'M2Ratio': 0.01463260660332565, 'SketchRectDepartments': [{'Id': 11706, 'Name': '79 BILGISAYAR OYUN AKSESUARLARI', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}, {'Id': 11707, 'Name': '79 BILGISAYAR OYUN AKSESUARLARI', 'CameraId': 1506, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5950, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'Corners': '[{"x":744.57,"y":348.18},{"x":743.11,"y":371.53},{"x":765.01,"y":370.07},{"x":765.01,"y":348.18}]', 'Area': 478.33, 'DataStatus': 4, 'InterestScore': 2949, 'CountRatio': 0.0014222243350903152, 'DwellRatio': 0.004121491787964023, 'Over15SecRatio': 0.0003737178037194756, 'DensityRatio': 0.00043318298188213934, 'M2Ratio': 0.0011171520784661949, 'SketchRectDepartments': [{'Id': 11708, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'CameraId': 1507, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5951, 'Name': '85 NETWORK / AG URUNLERI', 'Corners': '[{"x":711.75,"y":396.83},{"x":734.04,"y":396.83},{"x":735.06,"y":300.24},{"x":712.77,"y":300.24}]', 'Area': 2152.99, 'DataStatus': 4, 'InterestScore': 6285, 'CountRatio': 0.0022541661467030344, 'DwellRatio': 0.005541437541445993, 'Over15SecRatio': 0.0009736332254796865, 'DensityRatio': 0.0009231180068873958, 'M2Ratio': 0.005028363793650686, 'SketchRectDepartments': [{'Id': 11711, 'Name': '85 NETWORK / AG URUNLERI', 'CameraId': 1508, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5952, 'Name': '82 KLAVYE VE SETLERI', 'Corners': '[{"x":676.29,"y":418.39},{"x":712.29,"y":418.39},{"x":711.75,"y":300.24},{"x":676.29,"y":300.24}]', 'Area': 4221.49, 'DataStatus': 4, 'InterestScore': 55163, 'CountRatio': 0.006314834512907973, 'DwellRatio': 0.017359548713854367, 'Over15SecRatio': 0.009421622525348885, 'DensityRatio': 0.008101197017107091, 'M2Ratio': 0.009859399008475857, 'SketchRectDepartments': [{'Id': 11709, 'Name': '82 KLAVYE VE SETLERI', 'CameraId': 1508, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5953, 'Name': '72 YAZICILAR', 'Corners': '[{"x":634.75,"y":414.72},{"x":651.98,"y":414.72},{"x":651.98,"y":301.25},{"x":632.73,"y":300.57}]', 'Area': 2075.55, 'DataStatus': 4, 'InterestScore': 18737, 'CountRatio': 0.005366024684902039, 'DwellRatio': 0.006939081159630335, 'Over15SecRatio': 0.0030585851830725506, 'DensityRatio': 0.002751714832432404, 'M2Ratio': 0.004847500672047563, 'SketchRectDepartments': [{'Id': 11712, 'Name': '72 YAZICILAR', 'CameraId': 1508, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5954, 'Name': '90 PC / BILGISAYAR SES', 'Corners': '[{"x":651.98,"y":433.98},{"x":676.29,"y":432.96},{"x":676.29,"y":301.25},{"x":651.98,"y":299.22}]', 'Area': 3238.94, 'DataStatus': 4, 'InterestScore': 18766, 'CountRatio': 0.0036427166465614062, 'DwellRatio': 0.010237794706753824, 'Over15SecRatio': 0.0035601538143802676, 'DensityRatio': 0.0027560089783306547, 'M2Ratio': 0.007564628087360812, 'SketchRectDepartments': [{'Id': 11713, 'Name': '90 PC / BILGISAYAR SES', 'CameraId': 1508, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5955, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'Corners': '[{"x":713.29,"y":459.94},{"x":734.29,"y":450.94},{"x":733.29,"y":395.94},{"x":713.29,"y":395.94}]', 'Area': 1222.0, 'DataStatus': 4, 'InterestScore': 5966, 'CountRatio': 0.0034802899119132087, 'DwellRatio': 0.0034071091480336216, 'Over15SecRatio': 0.0005212379893982159, 'DensityRatio': 0.0008762950747143718, 'M2Ratio': 0.00285401258521458, 'SketchRectDepartments': [{'Id': 11717, 'Name': '89 DIGER BILGISAYAR AKSESUARLARI', 'CameraId': 1506, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5956, 'Name': '80 DEPOLAMA', 'Corners': '[{"x":653.29,"y":436.39},{"x":677.29,"y":433.39},{"x":676.29,"y":418.39},{"x":712.29,"y":418.39},{"x":712.29,"y":459.39},{"x":651.29,"y":482.39},{"x":644.29,"y":483.39},{"x":646.29,"y":466.39},{"x":651.29,"y":466.39}]', 'Area': 2846.5, 'DataStatus': 4, 'InterestScore': 26032, 'CountRatio': 0.005381871195599424, 'DwellRatio': 0.009612570445766301, 'Over15SecRatio': 0.004228911989457224, 'DensityRatio': 0.00382315269738882, 'M2Ratio': 0.006648074323906139, 'SketchRectDepartments': [{'Id': 11716, 'Name': '80 DEPOLAMA', 'CameraId': 1506, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5957, 'Name': '93 TONER, KARTUS VE KAGIT', 'Corners': '[{"x":628.29,"y":415.39},{"x":650.29,"y":414.39},{"x":650.29,"y":466.39},{"x":643.29,"y":465.39},{"x":643.29,"y":481.39},{"x":628.29,"y":481.39}]', 'Area': 1354.5, 'DataStatus': 4, 'InterestScore': 7347, 'CountRatio': 0.0019213894220579467, 'DwellRatio': 0.007599197276826412, 'Over15SecRatio': 0.0010424759787964319, 'DensityRatio': 0.0010790260495857804, 'M2Ratio': 0.00316346975996166, 'SketchRectDepartments': [{'Id': 11718, 'Name': '93 TONER, KARTUS VE KAGIT', 'CameraId': 1506, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5958, 'Name': '70 MONITOR (TFT)', 'Corners': '[{"x":629.29,"y":531.39},{"x":611.29,"y":486.39},{"x":629.29,"y":480.39},{"x":650.29,"y":482.39},{"x":677.29,"y":471.39},{"x":698.29,"y":509.39},{"x":655.29,"y":522.39}]', 'Area': 3058.0, 'DataStatus': 4, 'InterestScore': 55147, 'CountRatio': 0.009527714556802808, 'DwellRatio': 0.01150246522917777, 'Over15SecRatio': 0.008487328016050196, 'DensityRatio': 0.008098945674541422, 'M2Ratio': 0.007142038040577893, 'SketchRectDepartments': [{'Id': 11715, 'Name': '70 MONITOR (TFT)', 'CameraId': 1506, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5959, 'Name': '86 NOTEBOOK AKSESUARLARI', 'Corners': '[{"x":526.29,"y":569.39},{"x":503.29,"y":515.39},{"x":612.29,"y":488.39},{"x":628.29,"y":532.39},{"x":593.29,"y":544.39}]', 'Area': 5758.0, 'DataStatus': 4, 'InterestScore': 300638, 'CountRatio': 0.02588725603801578, 'DwellRatio': 0.02307856261841106, 'Over15SecRatio': 0.034873771894454224, 'DensityRatio': 0.044151308154787045, 'M2Ratio': 0.013447957827876883, 'SketchRectDepartments': [{'Id': 11720, 'Name': '86 NOTEBOOK AKSESUARLARI', 'CameraId': 1509, 'DepartmentId': 2342, 'DepartmentName': '26 BILGISAYAR AKSESUARLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5960, 'Name': '72 YAZICILAR PALET', 'Corners': '[{"x":601.29,"y":300.39},{"x":600.29,"y":385.39},{"x":632.29,"y":385.39},{"x":631.29,"y":300.39}]', 'Area': 2635.0, 'DataStatus': 4, 'InterestScore': 15902, 'CountRatio': 0.0070081193559185725, 'DwellRatio': 0.004509333244477934, 'Over15SecRatio': 0.0017210688329186378, 'DensityRatio': 0.002335407373982822, 'M2Ratio': 0.006154110607234385, 'SketchRectDepartments': [{'Id': 11721, 'Name': '72 YAZICILAR PALET', 'CameraId': 1517, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}, {'Id': 11722, 'Name': '72 YAZICILAR PALET', 'CameraId': 1509, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5961, 'Name': '71 MASAUSTU BILGISAYARLAR PALET', 'Corners': '[{"x":607.29,"y":414.94},{"x":628.29,"y":413.94},{"x":628.29,"y":480.94},{"x":611.29,"y":486.94}]', 'Area': 1327.5, 'DataStatus': 4, 'InterestScore': 8179, 'CountRatio': 0.0037536422214431023, 'DwellRatio': 0.0043304968057066955, 'Over15SecRatio': 0.000904790472162941, 'DensityRatio': 0.0012012667548295156, 'M2Ratio': 0.00310041056208867, 'SketchRectDepartments': [{'Id': 11725, 'Name': '71 MASAUSTU BILGISAYARLAR PALET', 'CameraId': 1509, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5962, 'Name': '71 MASAUSTU BILGISAYARLAR', 'Corners': '[{"x":569.29,"y":405.39},{"x":569.29,"y":498.94},{"x":611.29,"y":487.94},{"x":607.29,"y":405.39}]', 'Area': 3533.0, 'DataStatus': 4, 'InterestScore': 159283, 'CountRatio': 0.017072634462595302, 'DwellRatio': 0.018540488412529324, 'Over15SecRatio': 0.026337270483177782, 'DensityRatio': 0.023392170333106782, 'M2Ratio': 0.008251412817973086, 'SketchRectDepartments': [{'Id': 11724, 'Name': '71 MASAUSTU BILGISAYARLAR', 'CameraId': 1509, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5964, 'Name': '75 LENOVO', 'Corners': '[{"x":566.29,"y":300.94},{"x":601.29,"y":299.94},{"x":600.29,"y":386.39},{"x":568.29,"y":386.94}]', 'Area': 2888.92, 'DataStatus': 4, 'InterestScore': 29862, 'CountRatio': 0.009192957018320546, 'DwellRatio': 0.006455274307169745, 'Over15SecRatio': 0.004219077310411975, 'DensityRatio': 0.004385496362446486, 'M2Ratio': 0.006747147330342148, 'SketchRectDepartments': [{'Id': 11697, 'Name': '75 LENOVO', 'CameraId': 1516, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5965, 'Name': '75 DIZUSTU BILGISAYARLAR', 'Corners': '[{"x":521.29,"y":300.39},{"x":518.29,"y":512.39},{"x":569.29,"y":498.39},{"x":568.29,"y":406.39},{"x":607.29,"y":406.39},{"x":606.29,"y":387.39},{"x":568.29,"y":387.39},{"x":565.29,"y":300.39}]', 'Area': 10586.0, 'DataStatus': 4, 'InterestScore': 242322, 'CountRatio': 0.033919456147752866, 'DwellRatio': 0.014196938386743572, 'Over15SecRatio': 0.04159085768235954, 'DensityRatio': 0.03558708061091545, 'M2Ratio': 0.024723876617906336, 'SketchRectDepartments': [{'Id': 11726, 'Name': '75 DIZUSTU BILGISAYARLAR', 'CameraId': 1516, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}, {'Id': 11723, 'Name': '75 DIZUSTU BILGISAYARLAR', 'CameraId': 1509, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5966, 'Name': 'ACTION AREA', 'Corners': '[{"x":230.29,"y":466.39},{"x":277.29,"y":466.39},{"x":277.29,"y":549.85},{"x":360.29,"y":548.85},{"x":361.29,"y":595.39},{"x":233.29,"y":594.39}]', 'Area': 9648.59, 'DataStatus': 4, 'InterestScore': 62373, 'CountRatio': 0.020826276684038404, 'DwellRatio': 0.005951700519406899, 'Over15SecRatio': 0.007523529469615759, 'DensityRatio': 0.009160126933836627, 'M2Ratio': 0.022534531333531543, 'SketchRectDepartments': [{'Id': 11696, 'Name': 'ACTION AREA', 'CameraId': 1501, 'DepartmentId': 2366, 'DepartmentName': 'MÜŞTERİ ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5967, 'Name': 'SMARTBAR', 'Corners': '[{"x":398.29,"y":386.39},{"x":399.29,"y":456.39},{"x":478.29,"y":456.39},{"x":477.29,"y":385.39}]', 'Area': 5570.0, 'DataStatus': 4, 'InterestScore': 187374, 'CountRatio': 0.023538010827128433, 'DwellRatio': 0.015819431270207945, 'Over15SecRatio': 0.027812472339965186, 'DensityRatio': 0.027517528688136506, 'M2Ratio': 0.013008878968613101, 'SketchRectDepartments': [{'Id': 11700, 'Name': 'SMARTBAR', 'CameraId': 1510, 'DepartmentId': 2367, 'DepartmentName': 'HİZMET ALANI', 'Archived': False, 'DataStatus': 4}, {'Id': 11703, 'Name': 'SMARTBAR', 'CameraId': 1515, 'DepartmentId': 2367, 'DepartmentName': 'HİZMET ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5968, 'Name': '104 AKSESUAR GSM', 'Corners': '[{"x":361.29,"y":597.39},{"x":375.29,"y":631.39},{"x":526.29,"y":570.39},{"x":502.29,"y":514.39},{"x":361.29,"y":566.39}]', 'Area': 10123.5, 'DataStatus': 4, 'InterestScore': 50110, 'CountRatio': 0.007420128634050586, 'DwellRatio': 0.013420538153574597, 'Over15SecRatio': 0.00813327957042122, 'DensityRatio': 0.007359192396985, 'M2Ratio': 0.02364369591360049, 'SketchRectDepartments': [{'Id': 11730, 'Name': '104 AKSESUAR GSM', 'CameraId': 1504, 'DepartmentId': 2345, 'DepartmentName': '29 TELEKOM AKSESUAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5969, 'Name': '404 GIYILEBILIR TEKNOLOJI', 'Corners': '[{"x":418.29,"y":509.39},{"x":418.29,"y":546.39},{"x":485.29,"y":522.39},{"x":483.29,"y":507.39}]', 'Area': 1729.0, 'DataStatus': 4, 'InterestScore': 60924, 'CountRatio': 0.013017908537901883, 'DwellRatio': 0.009300399743051711, 'Over15SecRatio': 0.005684444488154129, 'DensityRatio': 0.008947292086263452, 'M2Ratio': 0.004038124189718501, 'SketchRectDepartments': [{'Id': 11728, 'Name': '404 GIYILEBILIR TEKNOLOJI', 'CameraId': 1504, 'DepartmentId': 2345, 'DepartmentName': '29 TELEKOM AKSESUAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5970, 'Name': '75 CASPER', 'Corners': '[{"x":479.29,"y":482.39},{"x":519.29,"y":481.39},{"x":520.29,"y":508.39},{"x":480.29,"y":524.39}]', 'Area': 1388.5, 'DataStatus': 4, 'InterestScore': 17658, 'CountRatio': 0.00797673732229624, 'DwellRatio': 0.0043991699259612145, 'Over15SecRatio': 0.002035778562366617, 'DensityRatio': 0.002593252918421756, 'M2Ratio': 0.0032428776387646843, 'SketchRectDepartments': [{'Id': 11732, 'Name': '75 CASPER', 'CameraId': 1510, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5971, 'Name': '108 AKILLI TELEFONLAR', 'Corners': '[{"x":419.29,"y":486.39},{"x":420.29,"y":509.39},{"x":450.29,"y":508.39},{"x":448.29,"y":486.39}]', 'Area': 664.5, 'DataStatus': 4, 'InterestScore': 24675, 'CountRatio': 0.009757488961914893, 'DwellRatio': 0.005025448597393982, 'Over15SecRatio': 0.0030585851830725506, 'DensityRatio': 0.0036237789104529112, 'M2Ratio': 0.001551956925429696, 'SketchRectDepartments': [{'Id': 11733, 'Name': '108 AKILLI TELEFONLAR', 'CameraId': 1504, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5972, 'Name': '108 TCL', 'Corners': '[{"x":450.29,"y":486.39},{"x":478.29,"y":487.39},{"x":477.29,"y":507.39},{"x":451.29,"y":507.39}]', 'Area': 553.5, 'DataStatus': 4, 'InterestScore': 19663, 'CountRatio': 0.007138853069172, 'DwellRatio': 0.005473780708328518, 'Over15SecRatio': 0.0025471818727195836, 'DensityRatio': 0.002887783744850533, 'M2Ratio': 0.001292713556396293, 'SketchRectDepartments': [{'Id': 11729, 'Name': '108 TCL', 'CameraId': 1504, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5973, 'Name': '108 XIAOMI', 'Corners': '[{"x":418.29,"y":456.39},{"x":417.29,"y":488.39},{"x":480.29,"y":489.39},{"x":477.29,"y":456.39}]', 'Area': 1982.0, 'DataStatus': 4, 'InterestScore': 45771, 'CountRatio': 0.011803669655714747, 'DwellRatio': 0.007705956585218757, 'Over15SecRatio': 0.006913779368810299, 'DensityRatio': 0.006721905312182593, 'M2Ratio': 0.004629012229046888, 'SketchRectDepartments': [{'Id': 11731, 'Name': '108 XIAOMI', 'CameraId': 1510, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5974, 'Name': '76 TABLET', 'Corners': '[{"x":478.29,"y":300.39},{"x":478.29,"y":361.39},{"x":521.29,"y":360.39},{"x":521.29,"y":300.39}]', 'Area': 2601.5, 'DataStatus': 4, 'InterestScore': 47902, 'CountRatio': 0.0117997080280404, 'DwellRatio': 0.008067424738417147, 'Over15SecRatio': 0.007317001209665523, 'DensityRatio': 0.0070348522089137165, 'M2Ratio': 0.006075870491354934, 'SketchRectDepartments': [{'Id': 11727, 'Name': '76 TABLET', 'CameraId': 1505, 'DepartmentId': 2340, 'DepartmentName': '24 BILGISAYAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5975, 'Name': '108 AKILLI TELEFONLAR', 'Corners': '[{"x":277.29,"y":503.39},{"x":419.29,"y":502.39},{"x":418.29,"y":548.85},{"x":277.29,"y":548.85}]', 'Area': 6503.09, 'DataStatus': 4, 'InterestScore': 350678, 'SaleQuantity': 40, 'SaleTotalAmount': 65592.08, 'CountRatio': 0.03341831024694806, 'DwellRatio': 0.020853302108979503, 'Over15SecRatio': 0.06559730923181321, 'DensityRatio': 0.05150010443042673, 'SaleQuantityRatio': 0.03816794, 'SaleTotalAmountRatio': 0.0557163656, 'M2Ratio': 0.015188134781328218, 'SketchRectDepartments': [{'Id': 11734, 'Name': '108 AKILLI TELEFONLAR', 'CameraId': 1501, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5977, 'Name': '108 SAMSUNG', 'Corners': '[{"x":300.29,"y":502.3},{"x":298.29,"y":434.3},{"x":398.29,"y":434.3},{"x":399.29,"y":501.3}]', 'Area': 6717.0, 'DataStatus': 4, 'InterestScore': 260604, 'SaleQuantity': 256, 'SaleTotalAmount': 679817.938, 'CountRatio': 0.027707623954377897, 'DwellRatio': 0.018691009265756692, 'Over15SecRatio': 0.04415770891316962, 'DensityRatio': 0.038271971836418235, 'SaleQuantityRatio': 0.24427481, 'SaleTotalAmountRatio': 0.5774628, 'M2Ratio': 0.015687727115291598, 'SketchRectDepartments': [{'Id': 11735, 'Name': '108 SAMSUNG', 'CameraId': 1503, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5978, 'Name': '108 OPPO', 'Corners': '[{"x":299.29,"y":390.94},{"x":398.29,"y":392.94},{"x":398.29,"y":434.94},{"x":299.29,"y":433.94}]', 'Area': 4207.5, 'DataStatus': 4, 'InterestScore': 85827, 'SaleQuantity': 176, 'SaleTotalAmount': 360200.469, 'CountRatio': 0.015618717106110217, 'DwellRatio': 0.010920217975472293, 'Over15SecRatio': 0.015194579124910259, 'DensityRatio': 0.012604496017456508, 'SaleQuantityRatio': 0.167938933, 'SaleTotalAmountRatio': 0.305967748, 'M2Ratio': 0.009826725001874259, 'SketchRectDepartments': [{'Id': 11736, 'Name': '108 OPPO', 'CameraId': 1503, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5979, 'Name': 'INNOVATION', 'Corners': '[{"x":181.86,"y":371.83},{"x":281.16,"y":371.83},{"x":281.16,"y":417.43},{"x":180.85,"y":416.41}]', 'Area': 4500.46, 'DataStatus': 4, 'InterestScore': 237246, 'CountRatio': 0.018195755908272472, 'DwellRatio': 0.025910787327446772, 'Over15SecRatio': 0.022491910976485282, 'DensityRatio': 0.03484171292851326, 'M2Ratio': 0.010510940654054671, 'SketchRectDepartments': [{'Id': 11737, 'Name': 'INNOVATION', 'CameraId': 1502, 'DepartmentId': 2366, 'DepartmentName': 'MÜŞTERİ ALANI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5980, 'Name': '5 UHD-LCD TV ALAN', 'Corners': '[{"x":181.86,"y":340.09},{"x":281.29,"y":340.85},{"x":283.18,"y":304.63},{"x":179.84,"y":306.65}]', 'Area': 3531.28, 'DataStatus': 4, 'InterestScore': 39930, 'CountRatio': 0.012619764956630081, 'DwellRatio': 0.006287853792714823, 'Over15SecRatio': 0.0059696501804663606, 'DensityRatio': 0.005864115891525627, 'M2Ratio': 0.008247395713515992, 'SketchRectDepartments': [{'Id': 11738, 'Name': '5 UHD-LCD TV ALAN', 'CameraId': 1512, 'DepartmentId': 2346, 'DepartmentName': '3 TV', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5981, 'Name': '117 KULAKLIKLAR', 'Corners': '[{"x":139.29,"y":421.85},{"x":181.29,"y":422.85},{"x":181.29,"y":370.85},{"x":281.29,"y":371.85},{"x":280.29,"y":339.85},{"x":181.29,"y":340.85},{"x":181.29,"y":305.85},{"x":136.29,"y":306.39}]', 'Area': 8140.16, 'DataStatus': 4, 'InterestScore': 123939, 'SaleQuantity': 384, 'SaleTotalAmount': 67400.48, 'CountRatio': 0.02200288010331925, 'DwellRatio': 0.011193850026575407, 'Over15SecRatio': 0.019836547634267957, 'DensityRatio': 0.018201527489082908, 'SaleQuantityRatio': 0.366412222, 'SaleTotalAmountRatio': 0.05725249, 'M2Ratio': 0.019011554079918426, 'SketchRectDepartments': [{'Id': 11739, 'Name': '117 KULAKLIKLAR', 'CameraId': 1512, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}, {'Id': 11665, 'Name': '117 KULAKLIKLAR', 'CameraId': 1502, 'DepartmentId': 2347, 'DepartmentName': '30 AKSESUAR CE', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5982, 'Name': '47 DIGER FOTOGRAF DONANIMLARI', 'Corners': '[{"x":399.29,"y":345.85},{"x":398.29,"y":384.85},{"x":477.29,"y":386.85},{"x":477.29,"y":345.85}]', 'Area': 3140.5, 'DataStatus': 4, 'InterestScore': 83977, 'CountRatio': 0.013273433522897218, 'DwellRatio': 0.012572761055003684, 'Over15SecRatio': 0.013984913602344587, 'DensityRatio': 0.012332829608773922, 'M2Ratio': 0.007334718922967585, 'SketchRectDepartments': [{'Id': 11704, 'Name': '47 DIGER FOTOGRAF DONANIMLARI', 'CameraId': 1515, 'DepartmentId': 2338, 'DepartmentName': '21 FOTO', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5983, 'Name': '108 HUAWEI', 'Corners': '[{"x":300.29,"y":344.85},{"x":299.29,"y":390.85},{"x":397.29,"y":391.85},{"x":398.29,"y":344.85}]', 'Area': 4557.5, 'DataStatus': 4, 'InterestScore': 90945, 'CountRatio': 0.015737565936340604, 'DwellRatio': 0.011484072739460657, 'Over15SecRatio': 0.015224083162046006, 'DensityRatio': 0.013356181557469593, 'M2Ratio': 0.01064415904837598, 'SketchRectDepartments': [{'Id': 11740, 'Name': '108 HUAWEI', 'CameraId': 1515, 'DepartmentId': 2344, 'DepartmentName': '28 CEP TELEFONLARI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5984, 'Name': '401 KILIF & KORUMA', 'Corners': '[{"x":323.29,"y":325.39},{"x":322.29,"y":344.39},{"x":454.29,"y":345.39},{"x":452.29,"y":325.39}]', 'Area': 2544.5, 'DataStatus': 4, 'InterestScore': 27644, 'CountRatio': 0.006546589731857231, 'DwellRatio': 0.00839170460771034, 'Over15SecRatio': 0.00399287969237124, 'DensityRatio': 0.004059888784529036, 'M2Ratio': 0.005942745518067511, 'SketchRectDepartments': [{'Id': 11741, 'Name': '401 KILIF & KORUMA', 'CameraId': 1515, 'DepartmentId': 2345, 'DepartmentName': '29 TELEKOM AKSESUAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5985, 'Name': '104 AKSESUAR GSM', 'Corners': '[{"x":395.29,"y":325.39},{"x":394.29,"y":303.39},{"x":453.29,"y":302.39},{"x":454.29,"y":325.39}]', 'Area': 1328.0, 'DataStatus': 4, 'InterestScore': 15913, 'CountRatio': 0.005096634003046492, 'DwellRatio': 0.006204896470824333, 'Over15SecRatio': 0.0018489196605068793, 'DensityRatio': 0.0023370433789522646, 'M2Ratio': 0.003101578325012244, 'SketchRectDepartments': [{'Id': 11747, 'Name': '104 AKSESUAR GSM', 'CameraId': 1505, 'DepartmentId': 2345, 'DepartmentName': '29 TELEKOM AKSESUAR', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5987, 'Name': '131 YER BAKIM URUNLERI', 'Corners': '[{"x":591.29,"y":59.94},{"x":719.29,"y":60.94},{"x":720.29,"y":230.94},{"x":688.29,"y":230.94},{"x":689.29,"y":299.94},{"x":591.29,"y":299.94}]', 'Area': 28636.5, 'DataStatus': 4, 'InterestScore': 709333, 'CountRatio': 0.08316843058138867, 'DwellRatio': 0.01694893861313984, 'Over15SecRatio': 0.08492245355572821, 'DensityRatio': 0.10417171178021106, 'M2Ratio': 0.06688128592184724, 'SketchRectDepartments': [{'Id': 11746, 'Name': '131 YER BAKIM URUNLERI', 'CameraId': 1517, 'DepartmentId': 2350, 'DepartmentName': '34 TEMIZLEME URUNLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11671, 'Name': '131 YER BAKIM URUNLERI', 'CameraId': 1530, 'DepartmentId': 2350, 'DepartmentName': '34 TEMIZLEME URUNLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11672, 'Name': '131 YER BAKIM URUNLERI', 'CameraId': 1630, 'DepartmentId': 2350, 'DepartmentName': '34 TEMIZLEME URUNLERI', 'Archived': False, 'DataStatus': 4}, {'Id': 11673, 'Name': '131 YER BAKIM URUNLERI', 'CameraId': 1522, 'DepartmentId': 2350, 'DepartmentName': '34 TEMIZLEME URUNLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5988, 'Name': '131 ROWENTA', 'Corners': '[{"x":690.29,"y":231.94},{"x":720.29,"y":231.94},{"x":720.29,"y":299.94},{"x":689.29,"y":299.94}]', 'Area': 2074.0, 'DataStatus': 4, 'M2Ratio': 0.004843880606984484, 'SketchRectDepartments': [{'Id': 11745, 'Name': '131 ROWENTA', 'CameraId': 1518, 'DepartmentId': 2350, 'DepartmentName': '34 TEMIZLEME URUNLERI', 'Archived': False, 'DataStatus': 4}]}, {'Id': 5989, 'Name': '403 DEPOLAMA', 'Corners': '[{"x":323.29,"y":302.85},{"x":321.29,"y":327.85},{"x":395.29,"y":324.85},{"x":391.29,"y":301.85}]', 'Area': 1706.0, 'DataStatus': 4, 'InterestScore': 24306, 'CountRatio': 0.006607994960809598, 'DwellRatio': 0.0073096918840823135, 'Over15SecRatio': 0.0033929642706110284, 'DensityRatio': 0.003569583675814354, 'M2Ratio': 0.003984407095234102, 'SketchRectDepartments': [{'Id': 11748, 'Name': '403 DEPOLAMA', 'CameraId': 1505, 'DepartmentId': 2345, 'DepartmentName': '29 TELEKOM AKSESUAR', 'Archived': False, 'DataStatus': 4}]}]


print(json)

edited_json1 = sorted ( json, key=lambda k: k.get ( 'DensityRatio', 0 ), reverse=False )
print('kotu siralama')
print ( edited_json1 )


def json_isimden_listeye_5(tarih1, tarih2,magaza_no, isim, reverse=True ):
    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
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




x =(json_isimden_listeye_5('01/03/2021', '05/03/2021',  234,"CountRatio",True))
print('birincisi')
print(x[0])

x =(json_isimden_listeye_5('01/03/2021', '05/03/2021',  234,"DwellRatio",True))
print(x)

print("density")
x1 =(json_isimden_listeye_5('01/03/2021', '05/03/2021',  234,"DensityRatio",False))
print(x1)
x =(json_isimden_listeye_5('01/03/2021', '05/03/2021',  234,"DensityRatio",True))
print('outputt')
print(x)
print(x1)

liste1 = [8.32, 4.63, 3.39, 3.34, 3.25, 2.94]
liste2 = [9.32, 5.63, 3.39, 3.34, 3.25, 2.94]

def listeleri_oranla(liste1,liste2):
    liste3=[]
    for element in range(0,len(liste2)):
        print(element)
        print(liste2[element])
        artis = float(liste2[element])/float(liste1[element])
        son_kisim = artis -1

        liste3.append(float (("{:.2f}".format ( float ( son_kisim )*100, 2 )) ))
    return liste3
#print(listeleri_oranla(liste1,liste2))


def json_isimden_listeye_full(edited_json, isim, reverse,id_ ):
    edited_json1 = sorted ( edited_json, key=lambda k: k.get ( isim, 0 ), reverse=reverse )
    #print ( edited_json1 )
    isim_listesi = []
    degerler_listesi = []
    id_listesi = []
    sayi = 0
    for area in range ( 0, len(edited_json1) ):
        if edited_json1[area]['Id'] == id_:
            try:
                istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json1[sayi][isim]) )*100, 2 )) )
                degerler_listesi.append ( istenen_sayi )
                isim_listesi.append ( edited_json1[sayi]["Name"] )
                id_listesi.append ( edited_json1[sayi]["Id"] )
            except Exception as e:
                print(e)
                log_info = str ( f'eksik data, {edited_json1[sayi]["Name"]}, {e}' )
                print ( log_info )
                degerler_listesi.append ( 0 )
                isim_listesi.append ( edited_json1[sayi]["Name"] )
                id_listesi.append ( edited_json1[sayi]["Id"] )

        sayi += 1
    return  id_listesi,isim_listesi,degerler_listesi








print("degisim")
print(json_isimden_listeye_full(json,"DensityRatio",True,5988))

yogunluk_haritasi = "{}/Sketch/{}/Rectangles?sdate={}&edate={}&stime=10:00&etime=22:00&tzoffset={}&layer=1"  ##hatali
json =  request1.get_performancetable ( yogunluk_haritasi, 234, '22/02/2021', '26/02/2021' )
print('2')
print(json)
print('2')

edited_json = ((json["Data"]))
edited_json1 = sorted ( edited_json, key=lambda k: k.get ( 'DensityRatio', 0 ), reverse=False )
print('kotu siralama')
print ( edited_json1 )





json33 =  request1.get_performancetable ( yogunluk_haritasi, 234, '01/03/2021', '05/03/2021' )
edited_json33 = ((json33["Data"]))





def json_id_den_degisim_oranina(tarih1,tarih2,tarih3,tarih4,magaza_no, veri_adi,id, reverse=True):
    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
    edited_json = ((json33["Data"]))
    edited_json1 = sorted ( edited_json, key=lambda k: k.get ( veri_adi, 0 ), reverse=reverse )
    print('kotu siralama11')
    print ( edited_json1 )
    id_listesi = 0
    isim_listesi = 0
    degerler_listesi = 0
    sayi = 0
    toplam_degerler = []



    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih3, tarih4 )
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
            if edited_json1[sayi]['Id'] == id:
                print('before')
                print( edited_json1[sayi][veri_adi] )
                istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json1[sayi][veri_adi]) ) * 100, 2 )) )
                print ( 'After' )
                print(istenen_sayi)

                degerler_listesi = ( istenen_sayi )
                isim_listesi = ( edited_json1[sayi]["Name"] )
                id_listesi = (edited_json1[sayi]['Id'])
        except Exception as e:
            print("error")
            print(e)
            log_info = str ( f'eksik data1, {edited_json1[sayi]["Name"]}, {e}' )
            print ( log_info )
            degerler_listesi = ( 0 )
            isim_listesi = ( edited_json1[sayi]["Name"] )
            id_listesi = ( edited_json1[sayi]['Id'] )

        sayi += 1
    sayi = 0
    for area in range ( len ( edited_json2 ) ):
        try:
            if edited_json2[sayi]['Id'] == id:
                print ( 'before' )
                print ( edited_json2[sayi][veri_adi] )
                istenen_sayi = float ( ("{:.2f}".format ( float ( (edited_json2[sayi][veri_adi]) ) * 100, 2 )) )
                print ( 'After' )
                print ( istenen_sayi )

                degerler_listesi2 = (istenen_sayi)
                isim_listesi2 = (edited_json2[sayi]["Name"])
                id_listesi2 = (edited_json2[sayi]['Id'])
        except Exception as e:
            print ( "error" )
            print ( e )
            log_info = str ( f'eksik data1, {edited_json2[sayi]["Name"]}, {e}' )
            print ( log_info )
            degerler_listesi2 = (0)
            isim_listesi2 = (edited_json2[sayi]["Name"])
            id_listesi2 = (edited_json2[sayi]['Id'])
        sayi += 1
    print('output')
    print(toplam_degerler)
    print ( 'yogunluk_ortalamasi' )
    yogunluk_ortalamasi = (sum(toplam_degerler)/uzunluk_degerleri)
    print(yogunluk_ortalamasi)
    print(id_listesi,id_listesi2,isim_listesi,isim_listesi2,degerler_listesi,degerler_listesi2)
    return  id_listesi,isim_listesi, float(degerler_listesi/degerler_listesi2,),yogunluk_ortalamasi


print('hadi_bakalim')
print(json_id_den_degisim_oranina( '22/02/2021', '26/02/2021','01/03/2021', '05/03/2021',  234,"DensityRatio",5950, reverse=True))


def json_id_den_degisim_oranina(tarih1,tarih2,tarih3,tarih4,magaza_no, veri_adi, reverse=True):
    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
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

    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih3, tarih4 )
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



                        final_list.append([id_listesi,isim_listesi, float ( ("{:.2f}".format ( float ( degerler_listesi2/degerler_listesi -1 ) * 100, 2 )) )])


                except Exception as e:
                    print ( "error" )
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


birlesik_liste = (json_id_den_degisim_oranina( '22/02/2021', '26/02/2021','01/03/2021', '05/03/2021',  234,"DensityRatio", reverse=True))

print(birlesik_liste)

sorted_list =  (BubleSort ( birlesik_liste ))

negatif_liste = negatifse(sorted_list)
pozitif_liste = pozitifse(sorted_list)

print(negatif_liste)
print(pozitif_liste)

son = request1.list_to_string_ve_ile(negatif_liste[2])
print(son)

son = request1.list_to_string_ve_ile(negatif_liste[1])
print(son)






def toplam_oran(tarih1,tarih2,tarih3,tarih4,magaza_no, veri_adi, reverse=True):
    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih1, tarih2 )
    edited_json = ((json33["Data"]))
    edited_json1 = sorted ( edited_json, key=lambda k: k.get ( veri_adi, 0 ), reverse=reverse )
    print('kotu siralama11')
    print ( edited_json1 )
    id_listesi = 0
    isim_listesi = 0
    degerler_listesi = 0
    sayi = 0
    toplam_degerler = []



    json33 = request1.get_performancetable ( yogunluk_haritasi, magaza_no, tarih3, tarih4 )
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



    print(toplam_degerler)
    print ( 'yogunluk_ortalamasi' )
    yogunluk_ortalamasi = (sum(toplam_degerler)/uzunluk_degerleri)
    print(yogunluk_ortalamasi)

    return  yogunluk_ortalamasi
#
# toplam_orannn = toplam_oran( '22/02/2021', '26/02/2021','01/03/2021', '05/03/2021',  234,"CountRatio", reverse=True)
# print(toplam_orannn)