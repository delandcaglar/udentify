# Udentify Bot

## Udentify_bot


Word dosyalarının otomatik olarak hazırlanıp müşterilere yollanmaya hazır hale gelmesi için yazılmış Python script. 

![udentify](https://i.imgur.com/RQoJhvo.png)




## Yazılım ana mantığı ve dosyaların işlevleri

s_admin---> selenium botudur. İçerisindeki "magaza_adi_listesi" listesindeki bilgilere göre mağaza resim datalarını toplar, "create_folders.py" ile klasifiye ettiği dosya hiyerarşisindeki uygun yerlere resimleri koyar. Aynı zamanda "haftalık_rapor.py" ve "aylik_rapor.py" scriptlerini başlatır.
haftalık_rapor.py ve aylik_rapor.py ---> "createfolders.py" ile yaratılmış word dosyalarının içine s_admin ile toplanmış resimleri koyar, ek olarak "request1.py" aracılığı ile mağaza bilgilerini toplar ve word dosyalarına yazar.
request1.py --> Udentify API'ından data toplar.


## Başlarken

Udentify_bot'a başlamak için sadece [bu repository'i](git@github.com:delandcaglar/udentify.git) kopyala.




## Açıklama için youtube videosu

[Buraya tıkla](https://www.youtube.com/channel/UCehC9DKqVdyP_SAJB7beJ1A?view_as=subscriber)



## 1. Udentify_bot nasıl yüklenir:

 pyhthon 3.7+ environment kullanılmalıdır.(ileriki updatelerde bazı library'ler problem çıkarabileceğinden anaconda python işlemleri çok daha kolaylaştırabilir)

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

## 2. Face Detection
Tracks multiple user faces in view of the camera, recording the positions and size fo the face in reference to the camera. Currently, focuses on size as the heuritic to focus. A virtual pan and tilt motion imitates the movement of the neck module as it steers the camera in the world view, as a red dot.

### 2.1 First create you environment, I'm using conda:
```
conda create --name opencv-env python=3.6
conda activate opencv-env
```
### 2.2 install the following libraries using the commands:
```
pip install numpy scipy matplotlib scikit-learn jupyter
pip install opencv-contrib-python
pip install dlib
pip install numpy
pip install cv2
```
## Authors

 **TeamUdentify**

Backend ana mantığı İlke Deland Çağlar ve Rıdvan Çilli tarafından yapılmıştır. Projeyi başlattığı için Can Dörtkardeşlere teşekkür ederiz.
Yazılımda katkısı olan diğer kişikleri görmek için şu listeye bakabilirsiniz: [katkıda bulunanlar](https://github.com/sukeesh/Jarvis/graphs/contributors).