from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
# import secrets1
from selenium.webdriver.support.ui import Select
import secrets1
#import cv2
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import os
import create_folders
import aylik_rapor


global_test = False
console = False  #development mode icinn true yap


ek_sure = float(1)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
class udentify_bot():
    def __init__(self):
        # get scroll Height
        # close browser
        option = webdriver.ChromeOptions ()
        #option.add_argument ( '--headless' ) #kapatmak icin
        option.add_argument ( "--start-maximized" )
        #option.add_argument ( f"--window-size=1080,{720}" )  ##boyut hatasindan kurtulmak icin
        option.add_argument ( "--hide-scrollbars" )
        self.driver = webdriver.Chrome ( executable_path="/Applications/chromedriver", options=option )

        height = self.driver.execute_script (
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight )" )
        print ( height )
        sleep ( 2+ek_sure )

    def login(self):
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click ()
        self.driver.get ( 'https://app.udentify.co/Login' )
        self.driver.find_element_by_xpath ( '//*[@id="loginUsername"]' )
        email_in = self.driver.find_element_by_xpath ( '//*[@id="loginUsername"]' )
        email_in.send_keys ( secrets1.username )
        self.driver.find_element_by_xpath ( '//*[@id="loginPassword"]' )
        pw_in = self.driver.find_element_by_xpath ( '//*[@id="loginPassword"]' )
        pw_in.send_keys ( secrets1.password )
        click('//*[@id="root"]/div/div[2]/div/form/div[3]/button')
        print("logged in") ## store a log in yapiliyor
        sleep ( 4+ek_sure )

    def select_firm(self,sirket_adi,magza_adi):
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click ()
        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )
        click ( '//*[@id="Home"]/nav/div/div[2]/div[1]/ul/li[1]/a' )  # trends e git so kose
        print ( "Sirket secmeye girildi" )  # sayfaya girdikten sonra biraz bekle
        sleep ( 4+ek_sure )

        deger_yolla('//*[@id="name"]', f"{sirket_adi}")
        sleep(1+ek_sure)
        print("sirket adi girildi")

        click('//*[@id="SelectedUser"]/div[2]/div/div/div/div[2]/div[1]/ul/li')
        print ( "sirket ismine tiklandi" )

        sleep(4+ek_sure)

        click ( '//*[@id="CompanyHome"]/nav/div/div[2]/div[1]/ul/li[2]/a' )
        print("magza seciliyor")

        deger_yolla ( '//*[@id="name"]', f"{magza_adi}" )
        print ( "magza adi girildi" )
        sleep ( 3 + ek_sure )

        click ( '//*[@id="SelectStore"]/div[2]/div/div/div/div[2]/div[1]/ul/li' )
        print ( "magaza adina tiklandi" )



    def go_trends(self , performans_tablosu_no,ilk_tarih,son_tarih,path,): ##path burada statik dosya icin
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/Trends?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate{son_tarih}&filterType=0" )

        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click ()

        def giris_yap(xpath, keys):
            self.driver.find_element_by_xpath (xpath )
            email_in = self.driver.find_element_by_xpath (xpath)
            email_in.send_keys ( keys )
            sleep ( 2 + ek_sure )

        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/trends_{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin

        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )

        sayfaya_git ( performans_tablosu_no, ilk_tarih, son_tarih )
        sleep ( 4 + ek_sure)


        take_screen_shot('//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div', path, f"density_haftalik")
        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[3]', path,f"density_aylik" )
        print("density screen shot alindi")

        self.driver.find_element_by_xpath ( '//*[@id="3"]/span' )
        interest_btn = self.driver.find_element_by_xpath ( '//*[@id="3"]/span' )
        interest_btn.click ()

        sleep ( 3 + ek_sure )

        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div', path, f"interest_haftalik" )
        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[3]', path,
                           f"interest_aylik" )

        print ( "interest screen shot alindi" )

        self.driver.find_element_by_xpath ( '//*[@id="1"]/span' )
        visitor_btn = self.driver.find_element_by_xpath ( '//*[@id="1"]/span' )
        visitor_btn.click ()

        sleep ( 3 + ek_sure )

        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div', path, f"visitor_haftalik" )
        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[3]', path,
                           f"visitor_aylik" )
        print ( "visitor screen shot alindi" )

        self.driver.find_element_by_xpath ( '//*[@id="2"]/span' )
        meantime_btn = self.driver.find_element_by_xpath ( '//*[@id="2"]/span' )
        meantime_btn.click ()

        sleep ( 3 + ek_sure )
        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[2]/div', path, f"meantime_haftalik" )
        take_screen_shot ( '//*[@id="trends"]/div/div/div/div[3]/div/div/div[2]/div/div[3]', path,
                           f"meantime_aylik" )
        print ( "meantime screen shot alindi" )




        # self.driver.find_element_by_xpath ( '//*[@id="CompanyHome"]/nav/div/div[2]/div[1]/ul/li[3]/a' )
        # density_map_btn = self.driver.find_element_by_xpath ( '//*[@id="CompanyHome"]/nav/div/div[2]/div[1]/ul/li[3]/a' )
        # density_map_btn.click ()

    def download_performance_table(self,path):
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click ()

        def giris_yap(xpath, keys):
            self.driver.find_element_by_xpath (xpath )
            email_in = self.driver.find_element_by_xpath (xpath)
            email_in.send_keys ( keys )
            sleep ( 2 + ek_sure )

        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )

        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )

        click('//*[@id="Home"]/nav/div/div[2]/div[1]/ul/li[4]/a')
        print("performans tablosuna girildi")

        sleep(3+ ek_sure)

        click ( '//*[@id="Charts"]/div/header/div[3]/div[1]/i' )
        print ( "tarih butonuna tiklandi" )


        sleep ( 3 + ek_sure )

        click('//*[@id="Charts"]/div/header/div[3]/div[2]/div[2]/span/div[1]/div[1]/button[1]/span')
        print("bugune basildi")

        sleep ( 3 + ek_sure )

        click('//*[@id="Charts"]/div/header/div[3]/div[2]/div[2]/span/div[1]/div[2]/div[1]/input')
        print("gun oncesi tusuna basildi")




        sleep ( 1 + ek_sure )

        self.driver.find_element_by_xpath (
            '//*[@id="Charts"]/div/header/div[3]/div[2]/div[2]/span/div[1]/div[2]/div[1]/input' )
        gun_sayisi_performance_table_btn = self.driver.find_element_by_xpath (
            '//*[@id="Charts"]/div/header/div[3]/div[2]/div[2]/span/div[1]/div[2]/div[1]/input' )

        # gun_sayisi_performance_table_btn.send_keys ( Keys.DELETE ) #keys.BACKSPACE

        haftalik_sure = int ( 7 )
        uzunluk = len ( str ( haftalik_sure ) )
        print ( uzunluk )
        starter_point = 0

        gun_sayisi_performance_table_btn.send_keys ( haftalik_sure )
        sleep ( 1 + ek_sure )
        while starter_point < uzunluk:
            gun_sayisi_performance_table_btn.send_keys ( Keys.ARROW_RIGHT )
            starter_point = starter_point + 1
            sleep ( 1 )

        sleep ( 1 + ek_sure )
        gun_sayisi_performance_table_btn.send_keys ( Keys.BACKSPACE )  # keys.BACKSPACE  ##DELETE

        # gun_sayisi_performance_table_btn.send_keys ( Keys.CONTROL, "a", )  # keys.BACKSPACE

        # gun_sayisi_performance_table_btn.send_keys ( 72 )

        click('//*[@id="Charts"]/div/header/div[3]/div[2]/div[2]/span/div[4]/button/span')
        print("uygulaya basildi")

        sleep ( 3 + ek_sure )

        click('//*[@id="Charts"]/div/div/div/div/div[3]/div/div[1]/div[2]/i')
        sleep(2+ ek_sure)
        print ( "indirme 1 basildi" )

        click('//*[@id="Charts"]/div/div/div/div/div[3]/div/div[1]/div[2]/div/span[1]/span/div/i')

        print("indirme 2 basildi")

        ##katmannlari sonra ekle

        click('//*[@id="Charts"]/nav/div/div[2]/div[1]/ul/li[2]/a')
        sleep(3+ek_sure)
        print ( "magazaya geri donuldu" )


        # self.driver.close ()

        sleep ( 3 + ek_sure )
        self.driver.save_screenshot ( "/Users/ilkedelandcaglar/Downloads/udentıfy/demore/customer_density.png" )

        print ( 'Bitti______' )

    def go_heat_map(self,path):
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()

        def giris_yap(xpath, keys):
            self.driver.find_element_by_xpath ( xpath )
            email_in = self.driver.find_element_by_xpath ( xpath )
            email_in.send_keys ( keys )
            sleep ( 2 + ek_sure )

        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath ( xpath )
            element.screenshot ( f"{path}/{isim}.png" )

        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )

        def scroll_until_location(xpath):
            find_location = self.driver.find_element_by_xpath (xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )

        def scroll_and_take_screenshot(xpath,path, isim):
            element = self.driver.find_element_by_xpath ( xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", element )
            element.screenshot ( f"{path}{isim}.png" )

        click ( '//*[@id="Home"]/nav/div/div[2]/div[1]/ul/li[7]/a' )  # trends e git so kose
        print ( "Heat map e girildi" )  # sayfaya girdikten sonra biraz bekle
        sleep ( 4 + ek_sure )

        # click ( '// *[ @ id = "SelectStore"] / div[2] / div / div / div / div[2] / div[1] / ul / li[1] / span' )

        sleep ( 3 + ek_sure )

        take_screen_shot ( '//*[@id="Heatmap"]/div/div/div/div/div[1]/div/div/div[2]/div/div/div/canvas', path, "anagiris" )
        print ( "ana giris screen shot alindi" )



        # self.driver.find_element_by_xpath ( '//*[@id="CompanyHome"]/nav/div/div[2]/div[1]/ul/li[3]/a' )
        # density_map_btn = self.driver.find_element_by_xpath ( '//*[@id="CompanyHome"]/nav/div/div[2]/div[1]/ul/li[3]/a' )
        # density_map_btn.click ()

        # self.driver.close ()

    def magaza_data_topla(self,path):
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click()

        def giris_yap(xpath, keys):
            self.driver.find_element_by_xpath (xpath )
            email_in = self.driver.find_element_by_xpath (xpath)
            email_in.send_keys ( keys )
            sleep ( 2 + ek_sure )

        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )

        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )
        def scroll_until_location(xpath):
            find_location = self.driver.find_element_by_xpath (xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )


        def scroll_and_take_screenshot(xpath,path, isim):
            try:
                element = self.driver.find_element_by_xpath ( xpath )
                self.driver.execute_script ( "arguments[0].scrollIntoView();", element )
                self.driver.execute_script ( "window.scrollBy(0, -65)" )  ##by yap To lari
                sleep(3)
                element.screenshot ( f"{path}{isim}.png")
            except Exception as ee:
                try:
                    print ( "screenshot hata 1" )
                    print(ee)
                    element = self.driver.find_element_by_xpath ( xpath )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", element )
                    self.driver.execute_script ( "window.scrollBy(0, -150)" ) ##by yap To lari
                    sleep ( 3 )
                    element.screenshot ( f"{path}{isim}.png")
                except Exception as ee:
                    print ( "screenshot hata 2" )
                    print(ee)
                    print ( '_________________Error handling basarisiz' )
                    element = self.driver.find_element_by_xpath ( xpath )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", element )
                    self.driver.execute_script ( "window.scrollBy(0, +300)" )
                    sleep ( 3 )
                    element.screenshot ( f"{path}{isim}.png" )

        def scroll_and_click(xpath):
            try:
                self.driver.find_element_by_xpath ( xpath )
                density_btn = self.driver.find_element_by_xpath (xpath )
                density_btn.click()
            except Exception as ee:
                try:
                    print ( "click hata 1" )
                    print(ee)
                    find_location = self.driver.find_element_by_xpath (xpath )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )
                    self.driver.execute_script ( "window.scrollBy(0, -150)" )
                    self.driver.find_element_by_xpath ( xpath )
                    density_btn = self.driver.find_element_by_xpath ( xpath )
                    density_btn.click ()
                except Exception as ee:
                    print ( "click hata 1" )
                    print ( ee )
                    print('_________________Error handling basarisiz')
                    find_location = self.driver.find_element_by_xpath ( xpath )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )
                    self.driver.execute_script ( "window.scrollBy(0, +300)" )
                    self.driver.find_element_by_xpath ( xpath )
                    density_btn = self.driver.find_element_by_xpath ( xpath )
                    density_btn.click ()

        def scroll_and_click_class_name(class_name):
            try:
                self.driver.find_element_by_class_name ( class_name )
                density_btn = self.driver.find_element_by_class_name (class_name )
                density_btn.click()
            except Exception as ee:
                try:
                    print ( "click hata 1" )
                    print(ee)
                    find_location = self.driver.find_element_by_class_name(class_name )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )
                    self.driver.execute_script ( "window.scrollBy(0, -150)" )
                    self.driver.find_element_by_class_name( class_name )
                    density_btn = self.driver.find_element_by_xpath ( class_name )
                    density_btn.click ()
                except Exception as ee:
                    print ( "click hata 1" )
                    print ( ee )
                    print('_________________Error handling basarisiz')
                    find_location = self.driver.find_element_by_class_name ( class_name )
                    self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )
                    self.driver.execute_script ( "window.scrollBy(0, +300)" )
                    self.driver.find_element_by_class_name ( class_name )
                    density_btn = self.driver.find_element_by_class_name ( class_name )
                    density_btn.click ()

        click('//*[@id="Home"]/nav/div/div[2]/div[1]/ul/li[2]/a')
        print("magazaya gidildi")

        sleep(3+ ek_sure)

        click ( '//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/ul/li[3]' )
        print ( "hava durumu iptal edildi" )

        sleep ( 3 + ek_sure )

        click ( '//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/ul/li[4]' )
        print ( "toptan satis adedi iptal edildi" )


        sleep ( 3 + ek_sure )

        click ( '//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/ul/li[5]' )
        print ( "toptan satis adedi iptal edildi" )



        sleep ( 3 + ek_sure )

        print("kucuk deneme")
        scroll_and_take_screenshot('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]', path, "toplam_kisi_sure")


        print("buyuk basari ")




        #find_location = self.driver.find_element_by_xpath('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]')
        #self.driver.execute_script ( "arguments[0].scrollIntoView();",find_location )




        #belki erro ustteki kismdan kaynakli
        #self.driver.execute_script("window.scrollBy(0,1000)","")

        sleep(4)

        #take_screen_shot('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]',path, "gunluk_toplam_kisi_ve_sure")


        #resim cekme fonksiyonunu gelistirdin



        ####kontrol____________________
        #scroll_until_location('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]')

        #self.driver.execute_script("window.scrollBy(0,-200)","")



        #self.driver.execute_script ( "window.scrollTo(0, -100)" ) #-- yukari kaydiriyor !!!!!!!!!!!

        # to var bide by var



        scroll_and_click('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/span')


        #find_location = self.driver.find_element_by_xpath ('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/span')
        #self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location)
        #____________________________

        print("scroll")

        scroll_and_take_screenshot('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[2]', path, "yogunluk_yogunluk_ortalamasi" )





        sleep ( 2 )

        #click ( '//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]/span' )
        #__________________________

        #click('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]')
        print("yogunluga bastin")



        sleep ( 2 )

        #scroll_and_take_screenshot('//*[@id="Home"]/div/div/div/div/div[2]/div/div/div/div[3]/button[2]',path, "gunluk_yogunluk_yogunluk_ortalamasi")
        print ( "yogunlugun resmini cektin" )

    def performans_tablosu_topla_final(self,performans_tablosu_no,ilk_tarih,son_tarih,path):
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/PerformanceTable?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )

        def saatlik_sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/PerformanceTable?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )
        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin


        sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih)

        element = self.driver.find_element_by_class_name ( "rt-tbody" )
        aaaa= "performans_tablosu"
        element.screenshot ( f"{path}/{aaaa}.png" )

        #gereksiz kod
        # content = self.driver.find_element_by_css_selector ('.col-xl-12:nth-of-type(2) .PageContent__Title' ).get_attribute ( 'outerHTML' )
        # aaaa = "1111"
        # if content == '<h1 class="PageContent__Title">Kasadaki Müşteri Sayısı &amp; Ortalama Geçirilen Süre (sn)</h1>':
        #     print ( content )
        # content.screenshot ( f"{path}/{aaaa}.png" )

    def magaza_data_topla_final(self,performans_tablosu_no,ilk_tarih,son_tarih,path):
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate{son_tarih}&filterType=1" )
        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin

        def saatlik_sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate{son_tarih}&filterType=0" )


        def isimlerde_ss_al(grafik_isimleri,grafik_isimleri_word_icin,grafik_adi,onceki_siralama): #bbot hata neden vermiyo
            sabit_katsayi = 1 + onceki_siralama
            liste_katsayi = 1
            toplam_grafik_sayisi = 0
            for grafik in grafik_isimleri:
                try:
                    content1 = self.driver.find_element_by_css_selector (f'.{grafik_adi}:nth-of-type({sabit_katsayi})' )
                    content = self.driver.find_element_by_css_selector (
                        f'.{grafik_adi}:nth-of-type({sabit_katsayi}) .PageContent__Title' ).get_attribute ( 'outerHTML' )
                    if content == grafik_isimleri[liste_katsayi-1]:
                        print("baklol")
                        print ( content )
                        toplam_grafik_sayisi += 1
                        content1.screenshot ( f"{path}/{grafik_isimleri_word_icin[liste_katsayi-1]}.png" )
                    print("katsayi artti")
                except Exception as e:
                    print(e)
                sabit_katsayi += 1
                liste_katsayi += 1
            sabit_katsayi = 0
            liste_katsayi = 0
            return toplam_grafik_sayisi

        sayfaya_git ( performans_tablosu_no, ilk_tarih, son_tarih )
        grafik_isimleri = ['<h1 class="PageContent__Title">Giren Kişi Sayısı</h1>',
                           '<h1 class="PageContent__Title">Kasadaki Müşteri Sayısı &amp; Ortalama Geçirilen Süre (sn)</h1>',
                           '<h1 class="PageContent__Title">Mağaza Önünden Geçen Müşteri Sayısı</h1>']  # bu kisim maksimum gerekli ismleri gerektiriir
        grafik_isimleri_word_icin = ["Giren_Kişi_Sayısı_gunluk", "Kasadaki_Müşteri_Sayısı_gunluk", "Mağaza_Önünden_Geçen_Müşteri_Sayısı_gunluk"]

        grafik_sayisi = isimlerde_ss_al(grafik_isimleri,grafik_isimleri_word_icin,"col-xl-12",0)

        grafik_isimleri_1 = ['<h1 class="PageContent__Title">En Çok Ziyaret Edilen Alanlar (kişi adet)</h1>','<h1 class="PageContent__Title">En Çok Vakit Geçirilen Alanlar (kişi sn)</h1>']
        grafik_isimleri_word_icin_1 = ["En_Çok_Ziyaret_Edilen_Alanlar_kişi_adet_gunluk", 'En_Çok_Vakit_Geçirilen_Alanlar_kişi_sn_gunluk']

        grafik_sayisi_1 = isimlerde_ss_al ( grafik_isimleri_1, grafik_isimleri_word_icin_1,"col-lg-6", grafik_sayisi )

        saatlik_sayfaya_git(performans_tablosu_no, ilk_tarih, son_tarih )

        print("elma")

        grafik_isimleri = ['<h1 class="PageContent__Title">Giren Kişi Sayısı</h1>',
                           '<h1 class="PageContent__Title">Kasadaki Müşteri Sayısı &amp; Ortalama Geçirilen Süre (sn)</h1>',
                           '<h1 class="PageContent__Title">Mağaza Önünden Geçen Müşteri Sayısı</h1>']  # bu kisim maksimum gerekli ismleri gerektiriir
        grafik_isimleri_word_icin = ["Giren_Kişi_Sayısı_saatlik", "Kasadaki_Müşteri_Sayısı_saatlik",
                                     "Mağaza_Önünden_Geçen_Müşteri_Sayısı_saatlik"]

        grafik_sayisi = isimlerde_ss_al ( grafik_isimleri, grafik_isimleri_word_icin, "col-xl-12", 0 )

        grafik_isimleri_1 = ['<h1 class="PageContent__Title">En Çok Ziyaret Edilen Alanlar (kişi adet)</h1>',
                             '<h1 class="PageContent__Title">En Çok Vakit Geçirilen Alanlar (kişi sn)</h1>']
        grafik_isimleri_word_icin_1 = ["En_Çok_Ziyaret_Edilen_Alanlar_kişi_adet_saatlik",
                                       'En_Çok_Vakit_Geçirilen_Alanlar_kişi_sn_saatlik']

        grafik_sayisi_1 = isimlerde_ss_al ( grafik_isimleri_1, grafik_isimleri_word_icin_1, "col-lg-6", grafik_sayisi )



    def isi_tablosu_topla_final(self,performans_tablosu_no,ilk_tarih,son_tarih,path):
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/Heatmap?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=0" )
            sleep ( 3 )
        def saatlik_sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/PerformanceTable?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )
        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin

        def scroll_until_location(xpath):
            find_location = self.driver.find_element_by_xpath (xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )





        sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih)


        def kamera_resimlerini_al():
            isim_listesi = []
            content = self.driver.find_elements_by_css_selector ( '.col-xl-6 .Black__UnderLine' )
            sayi = 1
            for element in content:
                content_isim = self.driver.find_element_by_css_selector (f'.col-xl-6:nth-of-type({sayi}) .Black__UnderLine' ).get_attribute ( 'outerHTML' )
                print(content_isim)
                isim_listesi.append(str(content_isim[29:-5]))
                content1 = self.driver.find_element_by_css_selector ( f'.col-xl-6:nth-of-type({sayi})' )
                self.driver.execute_script ( "arguments[0].scrollIntoView();", content1 )
                self.driver.execute_script ( "window.scrollBy(0, -65)" ) #burada error olabilir bak
                content1.screenshot ( f"{path}/isi_haritasi{sayi}.png" )
                sayi += 1
            sayi = 0
            return isim_listesi

        isim_listesi = kamera_resimlerini_al()
        print(isim_listesi)

    def yogunluk_haritasi_final(self,performans_tablosu_no,ilk_tarih,son_tarih,path):
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/Area?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=0" )
            sleep ( 3 )
        def saatlik_sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/PerformanceTable?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )
        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin

        def scroll_until_location(xpath):
            find_location = self.driver.find_element_by_xpath (xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )

        def hangisine_tekabul_ediyor(liste):
            if "(Müşteri Sayısı x Geçirilen Süre)" in liste:
                return "yogunluk"
            if "(Yoğunluk / Metrekare)" in liste:
                return "Yoğunluk_m2"
            if "(Ürün Sayısı)" in liste:
                return "satış_urun_sayisi"
            if "(Ürün Sayısı / Metrekare)" in liste:
                return "satıs_tutari_m2"
            if "(Toplam Tutar)" in liste:
                return "satis_toplam"



        sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih)

        content = bot.driver.find_elements_by_css_selector ( '.areaContainer ' )

        toplam_grafik_sayisi = len(content)

        baslangic_numarasi = 1
        for element in content:
            yazilar = bot.driver.find_element_by_css_selector (f'.areaContainer:nth-of-type({baslangic_numarasi}) .page-title :nth-child(1)' ).get_attribute ( 'outerHTML' )
            sonuc_yazisi = hangisine_tekabul_ediyor(yazilar)
            if sonuc_yazisi is not None:
                yogunluk_resim = bot.driver.find_element_by_css_selector ( f'.areaContainer:nth-of-type({baslangic_numarasi}) ' )
                self.driver.execute_script ( "arguments[0].scrollIntoView();", yogunluk_resim )
                self.driver.execute_script ( "window.scrollBy(0, -65)" )
                yogunluk_resim.screenshot ( f"{path}/yogunluk_haritasi{sonuc_yazisi}.png" )
            print(sonuc_yazisi)
            baslangic_numarasi += 1

        liste = ['<h4>Yoğunluk/M2<span style="font-size: 15px;"> (Yoğunluk / Metrekare)</span><span style="float: right;"><span><i title="Under Armour - Zorlu Center - 01/12/2020 - 18/12/2020 - Yoğunluk/M2.xlsx" class="icon download link"></i></span></span></h4>',
                 '<h4>Satış<span style="font-size: 15px;"> (Ürün Sayısı)</span><span style="float: right;"><span><i title="Under Armour - Zorlu Center - 01/12/2020 - 18/12/2020 - Satış.xlsx" class="icon download link"></i></span></span></h4>',
                 '<h4>Satış(Tutar)/M2<span style="font-size: 15px;"> (Ürün Sayısı / Metrekare)</span><span style="float: right;"><span><i title="Under Armour - Zorlu Center - 01/12/2020 - 18/12/2020 - Satış(Tutar)/M2.xlsx" class="icon download link"></i></span></span></h4>',
                 '<h4>Satış<span style="font-size: 15px;"> (Toplam Tutar)</span><span style="float: right;"><span><i title="Under Armour - Zorlu Center - 01/12/2020 - 18/12/2020 - Satış.xlsx" class="icon download link"></i></span></span></h4>',
                 '(Müşteri Sayısı x Geçirilen Süre)',
                 '',]




    def alansal_performans_tablosu_data_final(self,performans_tablosu_no,ilk_tarih,son_tarih,path,departman_id):
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih,departman_id):
            self.driver.get ( f"https://app.udentify.co/Department/{departman_id}?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=0" )
            sleep ( 3 )
        def sayfaya_git_gunluk(performans_tablosu_no,ilk_tarih,son_tarih,departman_id):
            self.driver.get ( f"https://app.udentify.co/Department/{departman_id}?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )
        def saatlik_sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/PerformanceTable?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate={son_tarih}&filterType=1" )
            sleep ( 3 )
        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/{isim}.png")  #test icin

        def scroll_until_location(xpath):
            find_location = self.driver.find_element_by_xpath (xpath )
            self.driver.execute_script ( "arguments[0].scrollIntoView();", find_location )


        def isimlerde_ss_al(grafik_isimleri,grafik_isimleri_word_icin,grafik_adi,onceki_siralama): #bbot hata neden vermiyo
            sabit_katsayi = 1 + onceki_siralama
            liste_katsayi = 1
            toplam_grafik_sayisi = 0
            for grafik in grafik_isimleri:
                try:
                    content1 = self.driver.find_element_by_css_selector (f'.{grafik_adi}:nth-of-type({sabit_katsayi})' )
                    content = self.driver.find_element_by_css_selector (
                        f'.{grafik_adi}:nth-of-type({sabit_katsayi}) .PageContent__Title' ).get_attribute ( 'outerHTML' )
                    if content == grafik_isimleri[liste_katsayi-1]:
                        print("baklol")
                        print ( content )
                        toplam_grafik_sayisi += 1
                        content1.screenshot ( f"{path}/{grafik_isimleri_word_icin[liste_katsayi-1]}.png" )
                    print("katsayi artti")
                except Exception as e:
                    print(e)
                sabit_katsayi += 1
                liste_katsayi += 1
            sabit_katsayi = 0
            liste_katsayi = 0
            return toplam_grafik_sayisi


        def infolari_yazdir(saatlik):
            grafik_isimleri = ['<h1 class="PageContent__Title">Alana Giriş Sayısı &amp; Ortalama Geçirilen Süre</h1>']  # bu kisim maksimum gerekli ismleri gerektiriir
            grafik_isimleri_word_icin = [f"Alana_Giriş_Sayısı_&_Ortalama_Geçirilen_Süre_{saatlik}"]
            grafik_sayisi = isimlerde_ss_al ( grafik_isimleri, grafik_isimleri_word_icin, "col-xl-12", 0 )
            grafik_isimleri1 = ['<h1 class="PageContent__Title">Edinme Hunisi</h1>',
                               '<h1 class="PageContent__Title">Bildirimler</h1>']  # bu kisim maksimum gerekli ismleri gerektiriir
            grafik_isimleri_word_icin1 = [f"Edinme_Hunisi{saatlik}",f"Bildirimler{saatlik}"]
            grafik_sayisi2 = isimlerde_ss_al ( grafik_isimleri1, grafik_isimleri_word_icin1, "col-xl-6", grafik_sayisi )
            yogunluk_butonu = '<span class="buttontext">Yoğunluk</span>'

            content = bot.driver.find_element_by_css_selector (
                '.col-xl-12:nth-of-type(1) .uButton.Button__Section.default .buttontext:nth-of-type(1)' ).get_attribute (
                'outerHTML' )
            if content == yogunluk_butonu:
                buton = bot.driver.find_element_by_css_selector ('.col-xl-12:nth-of-type(1) .uButton.Button__Section.default .buttontext:nth-of-type(1)' )
                buton.click()
                sleep(3)
                grafik_isimleri2 = [
                    '<h1 class="PageContent__Title">Alana Giriş Sayısı &amp; Ortalama Geçirilen Süre</h1>']  # bu kisim maksimum gerekli ismleri gerektiriir
                grafik_isimleri_word_icin2 = [f"Alana_Giriş_Sayısı_&_Ortalama_Geçirilen_Süre_yogunluk_{saatlik}"]
                grafik_sayisi = isimlerde_ss_al ( grafik_isimleri2, grafik_isimleri_word_icin2, "col-xl-12", 0 )

        sayfaya_git ( performans_tablosu_no, ilk_tarih, son_tarih, departman_id )
        infolari_yazdir ( "saatlik" )
        sayfaya_git_gunluk( performans_tablosu_no, ilk_tarih, son_tarih, departman_id )
        infolari_yazdir ( "gunluk" )

    def go_oneriler(self , performans_tablosu_no,ilk_tarih,son_tarih,path,): ##path burada statik dosya icin
        def sayfaya_git(performans_tablosu_no,ilk_tarih,son_tarih):
            self.driver.get ( f"https://app.udentify.co/Suggestions?StoreID={performans_tablosu_no}&sDate={ilk_tarih}&eDate{son_tarih}&filterType=0" )
        def click(xpath):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath (xpath )
            density_btn.click ()

        def giris_yap(xpath, keys):
            self.driver.find_element_by_xpath (xpath )
            email_in = self.driver.find_element_by_xpath (xpath)
            email_in.send_keys ( keys )
            sleep ( 2 + ek_sure )

        def take_screen_shot(xpath, path, isim):
            element = self.driver.find_element_by_xpath (xpath)
            element.screenshot ( f"{path}/{isim}.png" )
            print(f"{path}/degisim_{isim}.png")  #test icin

        def deger_yolla(xpath, deger):
            self.driver.find_element_by_xpath ( xpath )
            density_btn = self.driver.find_element_by_xpath ( xpath )
            density_btn.click ()
            density_btn.send_keys ( deger )

        sayfaya_git ( performans_tablosu_no, ilk_tarih, son_tarih )
        sleep ( 4 + ek_sure)


        take_screen_shot('//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[2]/div[2]', path, f"density_haftalik")
        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[3]', path,
                           f"density_aylik" )
        print("density screen shot alindi")

        self.driver.find_element_by_xpath ( '//*[@id="2"]/span' )
        interest_btn = self.driver.find_element_by_xpath ( '//*[@id="2"]/span' )
        interest_btn.click ()

        sleep ( 3 + ek_sure )

        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[2]/div[2]', path, f"interest_haftalik" )
        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[3]', path,
                           f"interest_aylik" )

        print ( "interest screen shot alindi" )

        self.driver.find_element_by_xpath ( '//*[@id="3"]/span' )
        visitor_btn = self.driver.find_element_by_xpath ( '//*[@id="3"]/span' )
        visitor_btn.click ()

        sleep ( 3 + ek_sure )

        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[2]/div[2]', path, f"visitor_haftalik" )
        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[3]', path,
                           f"visitor_aylik" )
        print ( "visitor screen shot alindi" )

        self.driver.find_element_by_xpath ( '//*[@id="4"]/span' )
        meantime_btn = self.driver.find_element_by_xpath ( '//*[@id="4"]/span' )
        meantime_btn.click ()

        sleep ( 3 + ek_sure )
        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[2]/div[2]', path, f"meantime_haftalik" )
        take_screen_shot ( '//*[@id="Suggestion"]/div[3]/div/div[2]/div/div[3]', path,
                           f"meantime_aylik" )
        print ( "meantime screen shot alindi" )




path = "/Users/ilkedelandcaglar/Downloads/udentify/bot_udentify/demo_re_sunum1/" ##bunu dosya duzeni olarak dynami ayarla
sirket_adi= "Under Armour"
magza_adi = "Akasya"
magaza_adi_listesi = [["Under Armour","Akasya",240,"Under Armour Akasya",160,240,[["a","b"],["c","d"]]],["Under Armour","Zorlu Center",239,"Under Armour Zorlu Center",160,240,[["a","b"],["c","d"]]]] #["Under Armour","İstinye Park",228,"Under Armour Istinye Park"]
degisken_path = (f"{BASE_DIR}/bot_udentify/demo_re") ##bbosluk birakma error olur

#bot.magaza_data_topla_final(240, '15/10/2020', '30/10/2020','/Users/ilkedelandcaglar/Downloads/udentify/bot_udentify/demo_re/')


ilk_tarih = '15/10/2020'
son_tarih = '30/10/2020'

if console == True :
    print("konsol modu aktif")


else:

    if global_test == True:

        for magaza in magaza_adi_listesi:
            create_folders.dosya_yaratici ( magaza,BASE_DIR )
            print("base/dir")
            magza_statik_dosya_location = (f"{BASE_DIR}/Statik {magaza[3]} ")
            print(magza_statik_dosya_location)
            bot = udentify_bot ()
            bot.login ()
            bot.select_firm ( magaza[0], magaza[1] )
            magza_statik_dosya_location = os.path.join ( BASE_DIR,f"bot_udentify/firms/{magaza[0]}/Statik {magaza[3]}/" )
            bot.go_trends ( 228,ilk_tarih,son_tarih,magza_statik_dosya_location )
            bot.magaza_data_topla ( magza_statik_dosya_location )
            aylik_rapor.start_writing_on_docx(magaza[0],magaza[3],magaza[2],ilk_tarih,son_tarih,magaza[4],magaza[5],magaza[6]) # degistirdin bak

    else:
        print("local doyalardan biri deneniyor")
        bot = udentify_bot ()
        bot.login ()
        bot.select_firm ( sirket_adi, magza_adi ) #magza_adi"İstinye Park"
        # bot.magaza_data_topla_final ( 240, ilk_tarih, son_tarih, path )
        # bot.yogunluk_haritasi_final(240,ilk_tarih,son_tarih,path)#228
        # bot.performans_tablosu_topla_final ( 240, ilk_tarih, son_tarih, path )
        # bot.alansal_performans_tablosu_data_final ( 240, ilk_tarih, son_tarih, path, 4796 )
        bot.go_trends(228,ilk_tarih,son_tarih,path)
        bot.go_oneriler ( 228, ilk_tarih, son_tarih, path )
        # bot.isi_tablosu_topla_final ( 240, ilk_tarih, son_tarih, path )









        #bot.go_trends(degisken_path)
        #bot.magaza_data_topla (f"/Users/ilkedelandcaglar/Downloads/udentify/bot_udentify/demo_re/")

sleep(1)






def job(sirket_adi,magza_adi):
    bot = udentify_bot()
    bot.login ()
    bot.select_firm(sirket_adi,magza_adi)

    bot.go_trends (degisken_path)


#job(sirket_adi,magza_adi)

#bot.magaza_data_topla()
#bot = udentifybot ()
#bot.login ()
#bot.select_firm()
#bot.magaza_data_topla()







#bot.go_trends()
#bot.download_performance_table()
##bot.go_heat_map() calismiyor













