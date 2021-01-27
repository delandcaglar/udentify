# Udentify Bot

## Udentify_bot


Word dosyalarının otomatik olarak hazırlanıp müşterilere yollanmaya hazır hale gelmesi için yazılmış Python script. 

![udentify](https://i.imgur.com/J9E0ouq.png)




## Yazılım ana mantığı ve dosyaların işlevleri

- s_admin---> selenium botudur. İçerisindeki "magaza_adi_listesi"(excel dosyasına bağlıdır) listesindeki bilgilere göre mağaza resim datalarını toplar, "create_folders.py" ile klasifiye ettiği dosya hiyerarşisindeki uygun yerlere resimleri koyar. Aynı zamanda "haftalık_rapor.py" ve "aylik_rapor.py" scriptlerini başlatır.
- haftalık_rapor.py ve aylik_rapor.py ---> "createfolders.py" ile yaratılmış word dosyalarının içine s_admin ile toplanmış resimleri koyar, ek olarak "request1.py" aracılığı ile mağaza bilgilerini toplar ve word dosyalarına yazar.
- request1.py --> Udentify API'ından data toplar.




## 1. Udentify_bot nasıl çalışır hale getirilir

pyhthon 3.7+ environment kullanılmalıdır. Bu sürüm 3.8.3 de denenmiştir.(ileriki updatelerde bazı library'ler problem çıkarabileceğinden anaconda python işlemleri çok daha kolaylaştırır)


Udentify_bot'a başlamak için sadece [bu repository'i](https://github.com/delandcaglar/udentify.git) kopyala.





### 1.1 Anaconda Python indir:

```
https://docs.anaconda.com/anaconda/install/
mac için(terminalde kullanmak için şu adımları gerçekleştiebilirsin):
```
### 1.2 Gerekli library'leri indir:
```
Anaconda Powershell Prompt'u aç
cd {dosyanin konumu} # örnek: cd C:\Users\Administrator\Desktop\udentify-master\bot_udentify_win
İndirdiğiniz dosyaların directory'sine gidin
Şu komut normalde işe yaramalı ama büyük olasılıla ben bir şeyi yanlış yaptım.....
python -m pip install -r requirements.txt
Bu yüzden dosya konumundayken python s_admin.py yazacağız hata çıktığında büyük olasılıkla bu x library'si eksik gibi bir şey olacak requirements.txt dosyasına girilip gerekli librarynin ismi ve versiyonu kopyalanmalı
ardından örnek olarak pip install docx==0.2.4 gibi yazılmalı 
şu ana kadar sadece docx librarysinde bbir hata çıkabilir exception yazan hata çıkıyorsa 
pip install python-docx==0.8.10 yazın bu o sorunu çözecektirr onun dışında bir sıkıntıı çıkmamalı
```

### 1.3 Gerekli library'leri indir:
```
chrome veeriyonuna bak
version 88 ise aşağıdaki likten 88 i diyelim 87 isi 87 yi indir.
chrome driver'i indir
https://chromedriver.chromium.org/downloads
indirilen driver'ı udentify/bot_udentify dosyasina sürükleme kopyala yapiştır yap. 
```

## 2. Nasil Kullanılır

### 2.1 Mağza adlarını doldur:

![udentify](https://i.imgur.com/BtKGgmv.png)
```
Kullanmak için istenen_magazalar.xlsx excel dosyasına gidilip aşağıdaki örnekteki gibi doldurulmalıdır. Büyük küçük harfler çok önemlidir yanlış yazıldığı şartlar altında program çalışmaz.
- Örnek --> under armour,under armour zorlu center,239, 01/01/2021, 19/01/2021,160,[["BOYS","GIRLS"],["WOMEN'S RUN","MEN'S RUN"]],Zorlu Center
- Excel dosyasının içinde başlıklar görülmektedir.

```

### 2.2 Script'i çalıştır:
```
cd {dosyanin konumu}
python s_admin.py 

```

### 2.3 Dosyalari topla:
```
word dosyalarının her biri firms/{firma ismi}/{firma ismi + konumu}.docx olarak dosyalanmıştır.
Dosyaları kopyalanmaya hazır haldedir.
firms/{firma ismi}/ statik {firma ismi + konumu} konumunda mağazaların statik dosyaları bulunmaktadır.

```
## 3. Executable yapmak istiyorsan

### 3.1 Executable yap:

```
pip install pyinstaller
```
```
pyinstaller --onefile --add-binary='/System/Library/Frameworks/
Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' s_admin.py
```

### 3.2 Linux ile Executable yapmak için buraya bakılabilinir:

```
https://github.com/rajbot/kivy_pyinstaller_linux_example/blob/master/bootstrap.sh
```




## Yazarlar

 **TeamUdentify**

Backend ana mantığı İlke Deland Çağlar ve Rıdvan Çilli tarafından yapılmıştır. Projeyi başlattığı için Can Dörtkardeşlere teşekkür ederiz.
Yazılımda katkısı olan diğer kişikleri görmek için şu listeye bakabilirsiniz: [katkıda bulunanlar](https://github.com/delandcaglar/udenfity/graphs/contributors).
