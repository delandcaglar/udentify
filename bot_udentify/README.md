# Udentify Bot

## Udentify_bot


Word dosyalarının otomatik olarak hazırlanıp müşterilere yollanmaya hazır hale gelmesi için yazılmış Python script. 

![udentify](https://i.imgur.com/RQoJhvo.png)




## Yazılım ana mantığı ve dosyaların işlevleri

- s_admin---> selenium botudur. İçerisindeki "magaza_adi_listesi" listesindeki bilgilere göre mağaza resim datalarını toplar, "create_folders.py" ile klasifiye ettiği dosya hiyerarşisindeki uygun yerlere resimleri koyar. Aynı zamanda "haftalık_rapor.py" ve "aylik_rapor.py" scriptlerini başlatır.
- haftalık_rapor.py ve aylik_rapor.py ---> "createfolders.py" ile yaratılmış word dosyalarının içine s_admin ile toplanmış resimleri koyar, ek olarak "request1.py" aracılığı ile mağaza bilgilerini toplar ve word dosyalarına yazar.
- request1.py --> Udentify API'ından data toplar.




## 1. Udentify_bot nasıl yüklenir

pyhthon 3.7+ environment kullanılmalıdır.(ileriki updatelerde bazı library'ler problem çıkarabileceğinden anaconda python işlemleri çok daha kolaylaştırır)




Udentify_bot'a başlamak için sadece [bu repository'i](https://github.com/delandcaglar/udentify.git) kopyala.





### 1.1 Anaconda Python indir:



```
https://docs.anaconda.com/anaconda/install/
```
### 1.2 Gerekli library'leri indir:
```
İndirdiğiniz dosyalaarın directory'sine gidin
python -m pip install -r requirements.txt
```


## 2. Nasil Kullanılır

### 2.1 Mağza adlarını doldur:
```
Kullanmak için s_admin.py scriptine gidilip aşağıdaki örnekteki gibi "magaza_adi_listesi" adlı liste doldurulmalıdır.
- Örnek --> magaza_adi_listesi = [["Under Armour","Akasya",240,"Under Armour Akasya"],["Under Armour","Zorlu Center",239,"Under Armour Zorlu Center"]
- 1. mağaza ismi, 2. mağaza konumu, 3. api kodu, 4. mağaza adı + mağaza konumu 

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
firms/{firma ismi}/ statik {firma ismi + konumu} konumunda mağazaların statik dosyaları bulunkamtadır.

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
Yazılımda katkısı olan diğer kişikleri görmek için şu listeye bakabilirsiniz: [katkıda bulunanlar](https://github.com/sukeesh/Jarvis/graphs/contributors).