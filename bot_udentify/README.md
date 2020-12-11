# Udentify Bot

## Udentify_bot


Word dosyalarının otomatik olarak hazırlanıp müşterilere yollanmaya hazır hale gelmesi için yazılmış Python script. 

![udentify](https://i.imgur.com/RQoJhvo.png)




## Yazılım ana mantığı ve dosyaların işlevleri

- s_admin---> selenium botudur. İçerisindeki "magaza_adi_listesi" listesindeki bilgilere göre mağaza resim datalarını toplar, "create_folders.py" ile klasifiye ettiği dosya hiyerarşisindeki uygun yerlere resimleri koyar. Aynı zamanda "haftalık_rapor.py" ve "aylik_rapor.py" scriptlerini başlatır.
- haftalık_rapor.py ve aylik_rapor.py ---> "createfolders.py" ile yaratılmış word dosyalarının içine s_admin ile toplanmış resimleri koyar, ek olarak "request1.py" aracılığı ile mağaza bilgilerini toplar ve word dosyalarına yazar.
- request1.py --> Udentify API'ından data toplar.




## Başlarken

Udentify_bot'a başlamak için sadece [bu repository'i](https://github.com/delandcaglar/udentify.git) kopyala.




## Açıklama için youtube videosu

Windows üzrinden nasıl yükleneceğini gösteren videoya ulaşmak için [buraya tıkla](https://www.youtube.com/channel/UCehC9DKqVdyP_SAJB7beJ1A?view_as=subscriber).



## 1. Udentify_bot nasıl yüklenir:

 pyhthon 3.7+ environment kullanılmalıdır.(ileriki updatelerde bazı library'ler problem çıkarabileceğinden anaconda python işlemleri çok daha kolaylaştırır)

To install the necessary kinba libraries for mac OS X:

Download espeak on mac: http://macappstore.org/espeak/

Download pyaudio:
```
xcode-select --install
brew remove portaudio
brew install portaudio
pip3 install pyaudio
```
Download ffmpeg:

`brew install ffmpeg`

Download wkhtmltopdf: https://wkhtmltopdf.org/downloads.html

Then run
`cd Jarvis-master`
then run
`./test.sh`

if it does not work run __main__.py in installer file

`python installer/__main__.py`

Selenium'u indir
`python3 -m pip install kivy`

Then run 
`python3 s_admin.py`



### Executable yapmak için:

pip install pyinstaller
```
pyinstaller --onefile --add-binary='/System/Library/Frameworks/
Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' s_admin.py
```

### Linux kullanılacaksa methodology burada var:

https://github.com/rajbot/kivy_pyinstaller_linux_example/blob/master/bootstrap.sh

## 2. Nasil Kullanılır

### 2.1 Mağza adlarını doldur:
```
Kullanmak için s_admin.py scriptine gidilip aşağıdaki örnekteki gibi "magaza_adi_listesi" adlı liste doldurulmalıdır.
- Örnek --> magaza_adi_listesi = [["Under Armour","Akasya",240,"Under Armour Akasya"],["Under Armour","Zorlu Center",239,"Under Armour Zorlu Center"]
- 1. mağaza ismi, 2. mağaza konumu, 3. api kodu, 4. mağaza adı + mağaza konumu 

```

### 2.3 Script'i çalıştır:
```
cd {dosyanin konumu}
python s_admin.py 

```

### 2.3 Dosyalari toplama:
```
word dosyalarının her biri firms/{firma ismi}/{firma ismi + konumu}.docx olarak dosyalanmıştır.
Dosyaları kopyalanmaya hazır haldedir.
firms/{firma ismi}/ statik {firma ismi + konumu} konumunda mağazaların statik dosyaları bulunkamtadır.

```
## Yazarlar

 **TeamUdentify**

Backend ana mantığı İlke Deland Çağlar ve Rıdvan Çilli tarafından yapılmıştır. Projeyi başlattığı için Can Dörtkardeşlere teşekkür ederiz.
Yazılımda katkısı olan diğer kişikleri görmek için şu listeye bakabilirsiniz: [katkıda bulunanlar](https://github.com/sukeesh/Jarvis/graphs/contributors).