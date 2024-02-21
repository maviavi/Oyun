#15.09.2023
import os
import time
import random
from anytree import Node, RenderTree
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.completion import WordCompleter
from termcolor import colored
from colorama import init, Fore
from tabulate import tabulate
init(autoreset=True) #otoreset ve coloramayı otomatize et
qqualitazotoontobdlkkvndlfjk = 0 #Şifrelipara kodu "money%50//"
#01000111 01100001 01101101 01100101 00100000 01001111 01110110 01100101 01110010 Game Over 
colors = ["green","red","green","red","green","red",]
binary = 0
os.system('cls')
for harf in "01100011 01111001 01100010 01100101 01110010 00101101 01100011 01101101 01100100":
        print(getattr(Fore,"GREEN") + harf, end="", flush=True)
        time.sleep(0.02)
while binary < 15:
    for renk in colors:
        os.system('cls')
        print(colored("01100011 01111001 01100010 01100101 01110010 00101101 01100011 01101101 01100100",renk))
        print(colored("""01000101 01101110 01110100 01100101 01110010 00100000 00100010 01101101 01101111 01101110 01100101 01111001
00100101 00110101 00110000 00101111 00101111 00110101 00110000 00100101 00100010 00100000 01100001 01101110
01100100 00100000 01100111 01100101 01110100 00100000 01101000 01100001 01101100 01100110 00100000 01111001 
01101111 01110101 01110010 00100000 01010111 00101101 01000011 01101111 01101001 01101110 00100000 01100010
01100001 01101100 01100001 01101110 01100011 01100101 00100000 01100010 01100001 01100011 01101011 00100001
        """,renk))
        time.sleep(0.02)
        binary += 1
        os.system("cls")

os.system("cls")
print(colored("""
 #####    ##   ##   #####     #######   ######              #####    ##   ##   #####
##   ##   ##   ##   ##   ##   ##        ##   ##            ##   ##   ### ###   ##  ##
##        ##   ##   ##   ##   ##        ##   ##            ##        #######   ##   ##
##         #####    ######    #####     ##   ##   ######   ##        ## # ##   ##   ##
##          ###     ##   ##   ##        ######             ##        ##   ##   ##   ##
##   ##     ###     ##   ##   ##        ##  ##             ##   ##   ##   ##   ##  ##
 #####      ###     #####     #######   ##   ##             #####    ##   ##   #####
""",'green'))
#BU SAÇMALIKLAR YERİNE BİR WHİLE TRUE İLE EĞİTİM MODU EKLE
print(colored("""
Örnek komutlar: /burası sonradan eğitim moduna dönüşecek
#1 ==> "help" komutu: daha fazla yardımcı komut gösterir. Örnek --> help -error3: error3 İsimli Hatanın Neden Kaynaklı Olduğunu Açıklar.
#2 ==>  "bakiye" komutu:  Bulunduğun Andaki Bakiye Miktarını Bir Bilgi Kutusu Kullanarak Ekranına Yazdırır. 
#3 ==> "sat" komutu: Belirttiğin Ürünü Satar Ve Bakiyen  Artar. Örnek --> sat -muz: Muz İsimli Ürünlerini Satar Ve Paran Artar.
#4 ==> "al" komutu: Belirttiğin Ürünü Satın Alır Ve Bakiyen Azalır. Örnek --> al -elma: Elma İsimli Ürünleri Alır ve Paran Azalır.
#5 ==> "Bellek" Komutu: Belleğinizde Neler Bulunduğunu Gösterir.
#6 ==> "komutlar" komutu: Oyundaki Tüm komutları Gösterir.
          \n""",'red'))

                                                    ###FONKSİYONLAR###

#KULLANICI İSTEDİĞİNDE ÇALIŞACAK OLAN KOMUTLAR:  

def komutlarıyazdır():
    print()
        # Ağaç yapısını oluştur
    komutlar = Node(colored("KOMUTLAR","blue",attrs=['bold']))
    geri = Node(colored("x",'red',attrs=['bold']), parent=komutlar)
    aciklamax = Node(colored("Herhangi bir yerde 'vazgeçmek' görevini yerine getirir ve komutun çalışmasını sonlandırır",'green'), parent=geri)
    help = Node(colored("help",'red',attrs=['bold']), parent=komutlar)
    help_error1 = Node(colored("help -error1: ",'red',attrs=['bold'])+colored("Hatanın neden kaynaklı olduğunu ekrana yazdırır",'green'), parent=help)
    help_error2 = Node(colored("help -error2: ",'red',attrs=['bold'])+colored("Hatanın neden kaynaklı olduğunu ekrana yazdırır",'green'), parent=help)
    help_error3 = Node(colored("help -error3: ",'red',attrs=['bold'])+colored("Hatanın neden kaynaklı olduğunu ekrana yazdırır",'green'), parent=help)
    help_error4 = Node(colored("help -error4: ",'red',attrs=['bold'])+colored("Hatanın neden kaynaklı olduğunu ekrana yazdırır",'green'), parent=help)
    help_error5 = Node(colored("help -error5: ",'red',attrs=['bold'])+colored("Hatanın neden kaynaklı olduğunu ekrana yazdırır",'green'), parent=help)
    boşluk = Node("",parent=help)

    child2 = Node(colored("İŞLEM KOMUTLARI: ",'blue',attrs=['bold']), parent=komutlar)
    boşluk = Node("", parent=child2)
    kacincigüvenlik = Node(colored("güvenlik: ",'red',attrs=['bold']) + colored("Kaçıncı güvenlikde olduğunu ve vergiye kaç güvenlik kaldığını gösteriri",'green'),parent=child2)
    bakiye = Node(colored("bakiye: ",'red',attrs=['bold']) + colored("Bakiyenizi gösterir",'green'), parent=child2)
    Bellek = Node(colored("Bellek: ",'red',attrs=['bold']) + colored("Belleğinizi gösterir",'green'), parent=child2)
    al = Node(colored("al: ",'red',attrs=['bold']) + colored("Bir ürün almanızı sağlar",'green'), parent=child2)
    sat = Node(colored("sat: ",'red',attrs=['bold']) + colored("Bir ürün satmanızı sğalar",'green'), parent=child2)
    boşluk = Node("", parent=child2)




    # Ağaç yapısını görselleştir
    for pre, fill, node in RenderTree(komutlar):
        print(f"{pre}{node.name}")
def helperrors():
    global helpcompleter
    while True:
        try:    
            print("")
            helpistek = str(prompt(mavirenkliprompt.format("'help -error1' formatında komut gir [x = vazgeç] : "),completer=helpcompleter).lower())
            
            if helpistek == "help -error1":
                print(colored("\n error1 : ",'red') + colored("Geçersiz bir komut girildiğini ifade eder! <=<>=> Gereksiz BÜYÜK veya küçük harf kullanımından, eksik komutlardan veya sayısal komutlar gibi olmayan geçersiz komutlardan kaynaklanır",'green'))
                
                break
            elif helpistek == "help -error2":
                print(colored("\n error2 : ",'red') + colored("Belirli bir sınırın dışında girdi girildiğinde bu hatayı alırsın. Genelde satın alma evresinde görülür!",'green'))
                break
            elif helpistek == "help -error3":
                print("\nVeri Yadware!")
                break
            elif helpistek == "help -error4":
                print("\nVeri Yadware!")       
                break
            elif helpistek == "help -error5":
                print("\nVeri Yadware!")
                break
            elif helpistek == "x":
                break
        except ValueError:
            print(colored("Burada Sadece 'help errorX' komutları kullanılabilir" , 'red'))
def bakiyegoster():
    print()
    print(tabulate([[colored("Bakiyeniz:",'blue',attrs=['bold']),colored("{} W-Coin",'yellow',attrs=['bold']).format(f'{Bakiye:,}')]],tablefmt="rst"))
def Belleğigör():
    data = [[colored("Tahta ",'cyan'),colored(', '.join(Oyuncunun_Zayıf_Malware_lerı),'magenta'),"25 - 70"+colored(" W-Coin arası","yellow")], [colored("Taş ",'cyan'),colored(', '.join(Oyuncunun_Güçlü_Maleare_lerı),'magenta'),"170 - 400"+colored(" W-Coin arası","yellow")], [colored("Demir ",'cyan'),colored(', '.join(Oyuncunun_Kusursuz_Malware_lerı),'magenta'),"600 - 1300"+colored(" W-Coin arası","yellow")]]
    print(tabulate(data,headers=[colored("KATEGORİLER",'blue'),colored("AKSESUARLARIN","blue"),colored("FİYAT ARALIĞI",'blue')],tablefmt='double_grid'))
def piyasaürünbulucu():
        global piyasa
        bulunanlar = []
        for _ in range(5):
            randoms = random.choice(piyasa)
            bulunanlar.append(randoms)
        data = [[colored("Çeşitli Ürünler: ",'cyan'),colored(', '.join(bulunanlar),'magenta')]]
        print()
        print(tabulate(data,headers=[colored("PİYASA","blue"),colored("Ürünler","blue")],tablefmt="double_grid"))
def güvenlikügöster():
    global güvenlik
    print(colored("{}. güvenlikdesin!".format(güvenlik),"grey",attrs=['bold']))
    i = int(güvenlik)
    if güvenlik % 30 != 0 and güvenlik > 0:
        while True:
            i = i +1 
            if i % 7 == 0:
                print("Vergi alınmasına {} güvenlik kaldı!".format(i))
                break

#AZ YER KAPLAMASI GEREKEN BİRDEN FAZLA KULLANILAN KODLAR
def GelenMüşterininTarzınıBelirleyici():
    global GelenMüşteri
    GelenMüşteri = random.choice(çaylakların_listesi)
    if random.random() < TecrübelilerinGelmeOlasılığı:
        GelenMüşteri = random.choice(tecrubelilerin_listesi)
        return GelenMüşteri
    if random.random() < HatasızlarınGelmeOlasılığı:
        GelenMüşteri = random.choice(hatasizların_listesi)
        return GelenMüşteri
def GelenMüşterininTeklifEdeceğiFiyat():
    global MüşterininTeklifEdeceğiFiyat
    if GelenMüşteri in çaylakların_listesi:
        MüşterininTeklifEdeceğiFiyat = random.randint(100,300)
    if GelenMüşteri in tecrubelilerin_listesi:
        MüşterininTeklifEdeceğiFiyat = random.randint(1000,5000)
    if GelenMüşteri in hatasizların_listesi:
        MüşterininTeklifEdeceğiFiyat = random.randint(10000,15000)
def ÜrünRenkgiBelirleyici():
    global ÜrünRengi
    global MüşterininElindekiÜrün
    if MüşterininElindekiÜrün in Zayıf_Malware_ler:
        ÜrünRengi = "white"
    if  MüşterininElindekiÜrün in Güçlü_Maleare_ler:
        ÜrünRengi = "green"
    if MüşterininElindekiÜrün in Kusursuz_Malware_ler:
        ÜrünRengi = "red"
def MüşteriRengiBelirleyici():
    global MüşteriRengi
    global GelenMüşteri
    if GelenMüşteri in çaylakların_listesi:
        MüşteriRengi = "white"
    if GelenMüşteri in tecrubelilerin_listesi:
        MüşteriRengi = "green"
    if GelenMüşteri in hatasizların_listesi:
        MüşteriRengi = "red"
def MüşteriÜrünSatarkenEdeceğiSohbet():
    global GelenMüşteri
    if MüşterininElindekiÜrün in spywarelistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(spyware_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in rootkitlistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(rootkit_satış_yorumarı),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in adwarelistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(adware_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in wiperlistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(wiper_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in wormlistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(worm_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in trojanlistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(trojan_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
    elif MüşterininElindekiÜrün in ransomwarelistesi:
        print()
        print(tabulate([[colored("Satıcı:",'blue',attrs=['bold']),colored(GelenMüşteri,MüşteriRengi)],[colored("Yazılım:",'blue',attrs=['bold']),colored(MüşterininElindekiÜrün,ÜrünRengi)]],tablefmt="rst"))
        print()
        HarfHarfCümleYazıcı(random.choice(hitaplar),"GREEN")
        print()
        HarfHarfCümleYazıcı(random.choice(ransomware_satış_yorumları),'GREEN')
        print()
        HarfHarfCümleYazıcı(random.choice(teklifetmetarzı).format(MüşterininTeklifEdeceğiFiyat),'GREEN')
        print()
def appendsistemi():
    if MüşterininElindekiÜrün in Zayıf_Malware_ler:
        Oyuncunun_Zayıf_Malware_lerı.append(MüşterininElindekiÜrün)
    elif MüşterininElindekiÜrün in Güçlü_Maleare_ler:
        Oyuncunun_Güçlü_Maleare_lerı.append(MüşterininElindekiÜrün)
    elif MüşterininElindekiÜrün in Kusursuz_Malware_ler:
        Oyuncunun_Kusursuz_Malware_lerı.append(MüşterininElindekiÜrün)
def müşteriiknaolmaolasılığı():
    global Yüzde50IknaOlmaOlasılığı,Yüzde35IknaOlmaOlasılığı,Yüzde20IknaOlmaOlasılığı
    if dükkanseviyesi == 1:
        if GelenMüşteri in çaylakların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.75
            Yüzde35IknaOlmaOlasılığı = 0.30
            Yüzde50IknaOlmaOlasılığı = 0.15
        elif GelenMüşteri in tecrubelilerin_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.55
            Yüzde35IknaOlmaOlasılığı = 0.25
            Yüzde50IknaOlmaOlasılığı = 0.10
        elif GelenMüşteri in hatasizların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.45
            Yüzde35IknaOlmaOlasılığı = 0.10
            Yüzde50IknaOlmaOlasılığı = 0.05
    elif dükkanseviyesi == 2:
        if GelenMüşteri in çaylakların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.80
            Yüzde35IknaOlmaOlasılığı = 0.35
            Yüzde50IknaOlmaOlasılığı = 0.15
        elif GelenMüşteri in tecrubelilerin_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.70
            Yüzde35IknaOlmaOlasılığı = 0.35
            Yüzde50IknaOlmaOlasılığı = 0.10
        elif GelenMüşteri in hatasizların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.70
            Yüzde35IknaOlmaOlasılığı = 0.30
            Yüzde50IknaOlmaOlasılığı = 0.15
    elif dükkanseviyesi == 3:
        if GelenMüşteri in çaylakların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.85
            Yüzde35IknaOlmaOlasılığı = 0.40
            Yüzde50IknaOlmaOlasılığı = 0.20
        elif GelenMüşteri in tecrubelilerin_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.85
            Yüzde35IknaOlmaOlasılığı = 0.43
            Yüzde50IknaOlmaOlasılığı = 0.18
        elif GelenMüşteri in hatasizların_listesi:
            Yüzde20IknaOlmaOlasılığı = 0.90
            Yüzde35IknaOlmaOlasılığı = 0.45
            Yüzde50IknaOlmaOlasılığı = 0.23
def MüşteriyleFiyatAzaltmaPazarlığı():
    global güvenlik,Bakiye,karar
    global Yüzde50IknaOlmaOlasılığı,Yüzde35IknaOlmaOlasılığı,Yüzde20IknaOlmaOlasılığı
    tktktktkt = WordCompleter(["teklifi kabul et","kabul et","al","onayla","teklifi reddet","reddet","alma","kabul etme","pazarlık yap"])
    karar = prompt(mavirenkliprompt.format("Teklifi kabul et veya teklifi reddet yada pazarlık yap: "),completer=tktktktkt)
    if Bakiye >= MüşterininTeklifEdeceğiFiyat and karar == "teklifi kabul et" or  karar == "kabul et" or karar == "al" or karar =="onayla":
        Bakiye =  Bakiye - MüşterininTeklifEdeceğiFiyat
        appendsistemi()
        güvenlik -= 1
        print()
        yazılımsatmaanimasyonu("Yazılım satın alınıyor")
        print("\033[F\033[K", end="")
        print(colored("İşleminiz Gerçekleşti! Bakiyenden ",'green')+colored("{} W-Coin".format(MüşterininTeklifEdeceğiFiyat),'yellow')+colored(" eksildi!",'green'))
        bakiyegoster()
    elif Bakiye < MüşterininTeklifEdeceğiFiyat and karar == "teklifi kabul et" or  karar == "kabul et" or karar == "al" or karar =="onayla":
        print()
        print(colored("Bu yazılımı alacak kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
        print()
    elif karar == "teklifi reddet" or karar == "alma" or karar == "kabul etme" or karar == "teklifi reddet" or karar == "reddet":
        pass
    elif Bakiye > MüşterininTeklifEdeceğiFiyat and karar == "pazarlık yap":
        UserTeklif = int(prompt(mavirenkliprompt.format("Yeni fiat teklif et: ")))
        while True:
            try:
                if UserTeklif >= MüşterininTeklifEdeceğiFiyat: 
                    yanlışKarar = prompt(mavirenkliprompt.format("Müşterinin teklif ettiği fiyattan daha büyük bir fiyat teklifinde bulundun! Satın almak istediğinden emin misin?"),completer=OnayCompleter)
                    if yanlışKarar == "evet" and Bakiye >= yanlışKarar:
                        Bakiye =  Bakiye - yanlışKarar
                        appendsistemi()
                        güvenlik -= 1
                        print()
                        yazılımsatmaanimasyonu("Yazılım satın alınıyor")
                        print("\033[F\033[K", end="")
                        print(colored("İşleminiz Gerçekleşti! Bakiyenden ",'green')+colored("{} W-Coin".format(yanlışKarar),'yellow')+colored(" eksildi!",'green'))
                        bakiyegoster()
                        break
                    elif yanlışKarar == "evet" and Bakiye < yanlışKarar:
                       print(colored("Bu yazılımı alacak kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
                       break
                    elif yanlışKarar == "hayır" or yanlışKarar == "hayir":
                        break
                    else:
                        print(colored('Sadece evet veya hayır ile yanıt ver! <type: -error1>','red'))
                elif UserTeklif < MüşterininTeklifEdeceğiFiyat and UserTeklif >= MüşterininTeklifEdeceğiFiyat - (MüşterininTeklifEdeceğiFiyat*0.20):
                    müşteriiknaolmaolasılığı()
                    if random.random() <  Yüzde20IknaOlmaOlasılığı and Bakiye >= UserTeklif:
                        Bakiye =  Bakiye - UserTeklif
                        appendsistemi()
                        güvenlik -= 1
                        print()
                        yazılımsatmaanimasyonu("Yazılım satın alınıyor")
                        print("\033[F\033[K", end="")
                        print(colored("İşleminiz Gerçekleşti! Bakiyenden ",'green')+colored("{} W-Coin".format(UserTeklif),'yellow')+colored(" eksildi!",'green'))
                        bakiyegoster()
                        break
                    elif random.random() < Yüzde20IknaOlmaOlasılığı and Bakiye < UserTeklif:
                        print(colored("Bu yazılımı alacak kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
                    elif random.random() > Yüzde20IknaOlmaOlasılığı: 
                        print(colored(random.choice(pazarlıkteklifireddetme)))
                        break
                elif UserTeklif < MüşterininTeklifEdeceğiFiyat-(MüşterininTeklifEdeceğiFiyat * 0.20) and UserTeklif >= MüşterininTeklifEdeceğiFiyat - (MüşterininTeklifEdeceğiFiyat * 0.35):
                    müşteriiknaolmaolasılığı()
                    if random.random() < Yüzde35IknaOlmaOlasılığı and  Bakiye >= UserTeklif:
                        Bakiye =  Bakiye - UserTeklif
                        appendsistemi()
                        güvenlik -= 1
                        print()
                        yazılımsatmaanimasyonu("Yazılım satın alınıyor")
                        print("\033[F\033[K", end="")
                        print(colored("İşleminiz Gerçekleşti! Bakiyenden ",'green')+colored("{} W-Coin".format(UserTeklif),'yellow')+colored(" eksildi!",'green'))
                        bakiyegoster()
                        break
                    elif random.random() < Yüzde35IknaOlmaOlasılığı and  Bakiye < UserTeklif:
                        print(colored("Bu yazılımı alacak kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
                    elif random.random() > Yüzde35IknaOlmaOlasılığı:
                        print(colored(random.choice(pazarlıkteklifireddetme)))
                        break
                elif UserTeklif < MüşterininTeklifEdeceğiFiyat - (MüşterininTeklifEdeceğiFiyat*0.35) and UserTeklif >= MüşterininTeklifEdeceğiFiyat - (MüşterininTeklifEdeceğiFiyat*0.50):
                    müşteriiknaolmaolasılığı()
                    if random.random() < Yüzde50IknaOlmaOlasılığı and  Bakiye >= UserTeklif:
                        Bakiye =  Bakiye - UserTeklif
                        appendsistemi()
                        güvenlik -= 1
                        print()
                        yazılımsatmaanimasyonu("Yazılım satın alınıyor")
                        print("\033[F\033[K", end="")
                        print(colored("İşleminiz Gerçekleşti! Bakiyenden ",'green')+colored("{} W-Coin".format(UserTeklif),'yellow')+colored(" eksildi!",'green'))
                        bakiyegoster()
                        break
                    elif random.random() < Yüzde50IknaOlmaOlasılığı and  Bakiye < UserTeklif:
                        print(colored("Bu yazılımı alacak kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
                    elif random.random() > Yüzde50IknaOlmaOlasılığı:
                        print(colored(random.choice(pazarlıkteklifireddetme)))
                        break
                else:
                    print(colored("Bu da ne saçma bir teklif! Benim de bir yerde kar etmem gerekiyor.","red"))
                    break
            except ValueError:
                print(colored("Sadece tam sayı değeri girebilirsin! <type: -error1>","red"))
    elif Bakiye < MüşterininTeklifEdeceğiFiyat-(MüşterininTeklifEdeceğiFiyat*0.30) and karar == "pazarlık yap":
        print(colored("Bu yazılımın %70'lik payını karşılayabilecek kadar W-Coin'e sahip değilsin","red",attrs=["bold"]))
    elif karar == "x":
        pass
    else:
        print()
        print(colored("al veya alma komutu ile doğru komut girdiğinden emin ol! <type: -error1>","red"))
        print()

def sat():
    SatSatma = WordCompleter(["sat","satma"])
    global Bakiye, güvenlik, vergi_durumu, UrunIsimTamamlayici
    global Oyuncunun_Zayıf_Malware_lerı,Oyuncunun_Güçlü_Maleare_lerı
    global Belleğigör, bakiyegoster, güvenlikügöster, helperrors




    while True:
        if güvenlik % 30 == 0 and güvenlik > 0 and vergi_durumu == False:
            break
        try:
            print()
            satılacak_mal = str(prompt(mavirenkliprompt.format("[Web] Satacağın Malı Seç: "),completer=UrunIsimTamamlayici).lower())
            if satılacak_mal == "Bellek":
                Belleğigör()
            elif satılacak_mal == "bakiye":
                bakiyegoster()
            elif satılacak_mal == "güvenlik":
                güvenlikügöster()
            elif satılacak_mal == "help":
                helperrors()
            elif satılacak_mal in Oyuncunun_Zayıf_Malware_lerı:
                while True:
                    try:
                        print("")
                        satış_fiyatı = int(prompt(mavirenkliprompt.format("[Web] Satacağın {}'ın değerini belirle [ 0 - 50 W-Coin arası ]: ".format(satılacak_mal))))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 50:
                            break
                        else:
                            print()
                            print(colored("0 W-Coin ile 50 W-Coin arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,'red'))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Zayıf_Malware_lerı.remove(satılacak_mal)
                            güvenlik += 1
                            vergi_durumu = False
                            print()
                            yazılımsatmaanimasyonu("satılıyor")
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} W-Coin".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
                            bakiyegoster()
                            break
                        elif onaylamak == "satma"or onaylamak =="Satma":
                            print()
                            print(colored("İşlem İptal Edildi!",'red'))
                            break
                        else:
                            print()
                            print(colored("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! <type: -error1> ",'red'))
                    except ValueError:
                        print(colored ("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme! <type: -error1> ",'red'))
                if güvenlik % 30 == 0 and güvenlik > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi güvenlikü",'green'))
                    break
                
                ######RENKLENDİRME VE TEXT EDİTİ BURADA KALDI

            elif satılacak_mal in Oyuncunun_Güçlü_Maleare_lerı:
                while True:
                    try:
                        print()
                        satış_fiyatı = int(input(colored("[Web] Satacağın {}'ın değerini belirle [0 W-Coin - 250 W-Coin arası ]".format(satılacak_mal),'blue')))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 250:
                            break
                        else:
                            print()
                            print(colored("0 W-Coin ile 250 W-Coin arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,"red"))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Güçlü_Maleare_lerı.remove(satılacak_mal)
                            güvenlik += 1
                            vergi_durumu = False
                            print()
                            yazılımsatmaanimasyonu("satılıyor")
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} W-Coin".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
                            bakiyegoster()
                            break
                        elif onaylamak == "satma" or onaylamak == "Satma":
                            break
                        else:
                            print()
                            print(colored("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! <type: -error1> ",'red'))
                    except ValueError:
                        print()
                        print(colored ("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme! <type: -error1> ",'red'))
                if güvenlik % 30 == 0 and güvenlik > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi güvenlikü",'green'))
                    break
            elif satılacak_mal in Oyuncunun_Kusursuz_Malware_lerı:
                while True:
                    try:
                        satış_fiyatı = int(input(colored("[Web] Satacağın {}'ın değerini belirle [0 W-Coin - 1000 W-Coin arası ]".format(satılacak_mal),'blue')))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 1000:
                            break
                        else:
                            print()
                            print(colored("0 W-Coin ile 1000 W-Coin arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,"red"))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Kusursuz_Malware_lerı.remove(satılacak_mal)
                            güvenlik += 1
                            vergi_durumu = False
                            print()
                            yazılımsatmaanimasyonu("satılıyor")
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} W-Coin".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
                            bakiyegoster()
                            break
                        elif onaylamak == "satma" or onaylamak == "Satma":
                            break
                        else:
                            print()
                            print(colored("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! <type: -error1> ",'red'))
                    except ValueError:
                        print()
                        print(colored ("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme! <type: -error1> ",'red'))
                if güvenlik % 30 == 0 and güvenlik > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi güvenlikü",'green'))
                    break
            elif satılacak_mal == "x":
                break
            else: 
                print()
                print(colored("Böyle bir yazılımın yok! Lütfen Belleğinde bulunan yazılımlardan bir seçim yap. <type: error3>",'red'))
        except ValueError:
            print(colored("Yazılımın adını doğru ve eksiksiz girdiğinizden emin olun <type: -error1>",'red'))
def al():
    global vergi_durumu, güvenlik, piyasa, Bakiye, UrunIsimTamamlayici,MüşterininElindekiÜrün,MüşteriRengi
    global Zayıf_Malware_ler, Güçlü_Maleare_ler,karar
    global Oyuncunun_Zayıf_Malware_lerı, Oyuncunun_Güçlü_Maleare_lerı
    global piyasaürünbulucu, Belleğigör, bakiyegoster, güvenlikügöster,helperrors
    global GelenMüşteri
    while True:
        GelenMüşterininTarzınıBelirleyici()
        GelenMüşterininTeklifEdeceğiFiyat()
        if GelenMüşteri in çaylakların_listesi:
            MüşterininElindekiÜrün = random.choice(Zayıf_Malware_ler)
            MüşteriRengiBelirleyici()
            ÜrünRenkgiBelirleyici()
            MüşteriÜrünSatarkenEdeceğiSohbet()
            print()
            MüşteriyleFiyatAzaltmaPazarlığı()
            if karar == "x":
                break
        elif GelenMüşteri in tecrubelilerin_listesi:
            MüşterininElindekiÜrün = random.choice(Güçlü_Maleare_ler)
            MüşteriRengiBelirleyici()
            ÜrünRenkgiBelirleyici()
            MüşteriÜrünSatarkenEdeceğiSohbet()
            print()
            MüşteriyleFiyatAzaltmaPazarlığı()
            if karar == "x":
                break
        elif GelenMüşteri in hatasizların_listesi:
            MüşterininElindekiÜrün = random.choice(Kusursuz_Malware_ler)
            MüşteriRengiBelirleyici()
            ÜrünRenkgiBelirleyici()
            MüşteriÜrünSatarkenEdeceğiSohbet()
            print()
            MüşteriyleFiyatAzaltmaPazarlığı()
            if karar == "x":
                break
        else:
            print()
            print("Error")
            print()
            break

#KONSOLDA OLUŞACAK YAZI ANİMASYONLARI

def HarfHarfCümleYazıcı(cümle, color):
    def deleteline():
        print("\033[K", end="")
    for harf in cümle:
        renkliharfler = getattr(Fore, color) + harf
        print(renkliharfler, end="", flush=True)
        time.sleep(0.009)
        deleteline()
def yazılımsatmaanimasyonu(almisatmi):
    liste = [".","..","..."]
    print()
    def deleteline():
        print("\033[F\033[K", end="") #Bu kod parçası, terminalde veya konsol penceresinde en son yazdırılan metni temizleyerek, yeni bir metni aynı satırda yazdırmak için kullanılabilir
        
    i = random.randint(0,2)
    while i < 3: 
        for list in liste:
            deleteline()
            print(colored("{}{}".format(almisatmi,list),'green'))
            time.sleep(0.15)
        i += 1
def müşteribekleniyorANIMASYON():
    liste = [".","..","..."]
    print()
    def deleteline():
        print("\033[F\033[K", end="") #Bu kod parçası, terminalde veya konsol penceresinde en son yazdırılan metni temizleyerek, yeni bir metni aynı satırda yazdırmak için kullanılabilir
        
    i = random.randint(0,1)
    while i < 3: 
        for list in liste:
            deleteline()
            print(colored("SıradanMüşteriler bekleniyor{}".format(list),'green'))
            time.sleep(0.15)
        i += 1


#OTOMATİK OLARAK ÇAĞRILAN FONKSİYONLAR 

def vergisistemi():
    global güvenlik
    global Bakiye
    if güvenlik % 30 == 0:
        oran = Bakiye * 0.1
        Bakiye = Bakiye - int(oran)
        print(colored("Ticaretinizin {}. güvenlikü! Tebrikler. ".format(güvenlik),'green'))
        print(colored("İmparatorluk tarafından bakiyenizden",'green')  +colored(" %10 ",'red',attrs=['bold'])  +colored("oranında vergi kesildi! <=<>=> güvenlikcel bakiye:",'green')  +colored(" {} W-Coin".format(Bakiye),'yellow'))


######################      #########################       ##########################      ##############################     
######################      #########################       ##########################      ##############################
######################      #########################       ##########################      ##############################

#PROMPT TAMAMLAYICILAR
UrunIsimTamamlayici = WordCompleter(["bakiye","güvenlik","help","Bellek","spyware (zayıf)", "rootkit (zayıf)", "adware (zayıf)", "wiper (zayıf)", "worm (zayıf)", "trojan (zayıf)", "ransomware (zayıf)", "spyware (güçlü)", "rootkit (güçlü)", "adware (güçlü)", "wiper (güçlü)", "worm (güçlü)", "trojan (güçlü)", "ransomware (güçlü)", "spyware (kusursuz)", "rootkit (kusursuz)", "adware (kusursuz)", "wiper (kusursuz)", "worm (kusursuz)", "trojan (kusursuz)", "ransomware (kusursuz)"])
helpcompleter = WordCompleter(["help -error1","help -error2","help -error3","help -error4","help -error5"])
KomutCompleter = WordCompleter(["darkweb","help","bellek","bakiye","komutlar","güvenlik","al","sat","x"])
OnayCompleter = WordCompleter(["evet","hayir"])


#PROMPT RENKLENDİRİCİLER
mavirenkliprompt = HTML('<ansiblue><b>{}</b></ansiblue>')
kirmizirenkliprompt = HTML('<ansired><b>{}</b></ansired>')

hitaplar = ["Hey!","Orada mısın?","Merhaba.","Beni tanıdın mı?","Baksana","ellohay!","..."]
teklifetmetarzı = ["Teklifim {} W-Coin","sana bu yazılımı {} W-Coin karşılığında veririm","{} W-Coin teklif ediyorum","{} W-Coine ne dersin? Bence gayet uygun","Bu kaliteyi {} W-Coine sana verebilirim","{} W-Coin. Anlaştık mı?"]

pazarlıkteklifireddetme = ["Hmm... Bu fiyat çok az, biraz daha düşünmem gerekiyor."]

#DETAYLI MÜŞTERİ YORUMLARI UZUN KISIM
spywarelistesi = ["spyware (zayıf)","spyware (güçlü)","spyware (kusursuz)"]
spyware_alış_yorumları = ["Bu sıralar bazı verileri takip etmeliyimde. Hayır hayır reklam için değil!","Bu yazılım en az benim kadar bilgi meraklısı!","İzle ve gör","Aslında bilgi elde etmenin daha basit yolları var ama bu da olur","Geçen sefer 189 WPM hızında birine rastladım. Ekrandaki görüntünün akış hızına inanamadım!"]
spyware_satış_yorumları = ["Bu yazılım işine yarayabilir. Daha çok kar edersin","Bunu spyware'i elimden çıkarmama yardımcı olur musun? küçük sorunlar yaratıyorda","Yazılımı bizzat kendi ellerimle kop... kopara kopara yazdım. Emeğim var bu spyware'de","Almak ister misin?","Sende kalsın","Bende çok çeşitli spyware yazılımları var dostum. Birini de sana vermek istedim.","Veri izlemek ister misin?","Sakın kendi makinende çalıştırma! şaka yaptım "]

rootkitlistesi = ["rootkit (zayıf)","rootkit (güçlü)","rootkit (kusursuz)"]
rootkit_alış_yorumarı = ["Bu yazılımla kendimi güvende hissediyorum!","Adeta bir gölge olacağım","Bayım benim her sistemde yetklili olabilmem gerekiyor. Bu benim işim!","Saklambaç oynamak istiyordum ama bir yazılım gerekliymiş.","Sistemleri boşu boşuna yormamak adına bazı dosyalarımı gizliyorum. Bence mantıklı.","Erişim kısıtlamalarından nefret ettiğimi biliyor muydun?"]
rootkit_satış_yorumarı = ["Gizliliği sevdiğini duymuştum. Sana bir gizlilik iksiri buldum","Biraz zorlandım ama sonunda bu rootkit'i yazmayı başardım.","Senin daha gizli olduğunu biliyorum. Bunu başka birine satmak istersin diye düşündüm.","Rootkit yazılımları hakettikleri değeri görmüyorlar bence. Sence de haklı değil miyim?","Al, daha pahalıya sat.","Bu yazılımlar ileride değerlenecek gibi hissettiriyor","Kendime özgü bir yöntemim var bu yazılımda","Bu güne kadar sisteme yakalanmadım"]

adwarelistesi = ["adware (zayıf)","adware (güçlü)","adware (kusursuz)"]
adware_alış_yorumları = ["Ücretsiz bir uygulamadan gelir elde etmek istiyordumda. Bu yazılım tam bana göre!","Bir insan neden bir sitenin DevTools'undan geçici reklam kaldırır ki?! aslında mantıklı ","Reklamlar güzeldir","Reklamlar insanların yeni uygulamalardan haberdan olmasını sağlar, neden sevilmediklerini bilmiyorum.","AdBlocker kullanan isanları sevmiyorum. (Kendim hariç)"]
adware_satış_yorumları = ["","","","","","","",""]

wiperlistesi = ["wiper (zayıf)","wiper (güçlü)","wiper (kusursuz)"]
wiper_alış_yorumları = ["Elinde olamamsı gereken bilgileri olan birine rastladım. Bir şeylere el atmam gerekiyor.","1tb'ı var ama 500mg'ı kalacak :D","Küçük bir işim var. Yaklaşık 250gb gereksiz bilgi yok etmem gerekiyor","Küçük bir şaka yapacağım","Artık fabrika ayarlarına geri dönmesine gerek kalmayacak"]
wiper_satış_yorumları = ["","","","","","","",""]

wormlistesi = ["worm (zayıf)","worm (güçlü)","worm (kusursuz)"]
worm_alış_yorumları = ["Neyseki bilgisayarlar tek tuşla karantinaya alınamıyor","E-posta göndermekten yoruldum","Zayıf ağları çok seviyorum çok sevimliler","worm da ne? denemek istiyorum","İşime yarıyor... yarıyorlar."]
worm_satış_yorumları = ["","","","","","","",""]

trojanlistesi = ["trojan (zayıf)","trojan (güçlü)","trojan (kusursuz)"]
trojan_alış_yorumları = ["Ben masumum, yani kısa süreliğine","Sisteme girebilirsem rahat edeceğim. Önce bu yazılımı almalıyım","Sistemi çökertmek çok kolay olacak","Bu şey bir yerden tanıdık geliyor","Acaba 32gb 'Özet Ders Notları' dosyası şüphe uyandırır mı ya?"]
trojan_satış_yorumları = ["","","","","","","",""]

ransomwarelistesi = ["ransomware (zayıf)","ransomware (güçlü)","ransomware (kusursuz)"]
ransomware_alış_yorumları = ["Çok pahalı anahtarlarım var dostum","Nasıl güçlü bir şifre oluşturabileceklerini uygulamalı bir şekilde öğretmek istediğim birileri var","Havalı bir cüzdan adresi de buldum mu bu iş tamam","Bu sıralar W-Coin yükselecek diye duydum. Sanırım biraz W-Coin biriktirmeliyim","for döngüleri olmasaydı kim bilir ne yapardık!"]
ransomware_satış_yorumları = ["","","","","","","",""]


#PİYASADA BULUNAN YAZILIMLAR
Zayıf_Malware_ler = ["spyware (zayıf)","rootkit (zayıf)","adware (zayıf)","wiper (zayıf)","worm (zayıf)","trojan (zayıf)","ransomware (zayıf)"]
Güçlü_Maleare_ler   = ["spyware (güçlü)","rootkit (güçlü)","adware (güçlü)","wiper (güçlü)","worm (güçlü)","trojan (güçlü)","ransomware (güçlü)"]
Kusursuz_Malware_ler = ["spyware (kusursuz)","rootkit (kusursuz)","adware (kusursuz)","wiper (kusursuz)","worm (kusursuz)","trojan (kusursuz)","ransomware (kusursuz)"]
piyasa = Güçlü_Maleare_ler + Zayıf_Malware_ler + Kusursuz_Malware_ler

#GELECEK MÜŞTERİ VE SATICILAR
çaylakların_listesi = ["Ali", "Ayşe", "Mehmet", "Elif", "Ahmet", "Zeynep", "Hüseyin", "Ece", "Kemal", "Aslı"]
tecrubelilerin_listesi = ["ShadowBlade", "Sorceress", "RogueMaster", "AstralWanderer", "EternalSpecter", "FrostByte", "LunarShade", "ArcaneWhisper", "VengefulHex", "NebulaDancer"]
hatasizların_listesi = ["Xephyr", "Cryp7ix", "A3on", "NyxStar", "VortexEclipse", "SylphInferno", "ZephyrCipher", "LunaCronos", "AbyssSynth", "NebulaViper"]







#BELLEKTE BULUNAN YAZILIMLAR
Oyuncunun_Zayıf_Malware_lerı = [random.choice(Zayıf_Malware_ler)]
Oyuncunun_Güçlü_Maleare_lerı = []
Oyuncunun_Kusursuz_Malware_lerı = []


#HATA UYARILARI
İNTEGERvalueerror = "SADECE TAM SAYI GİREBİLİRSİN! <type: -error1>"
intvalueerror = "SADECE TAM SAYI DEĞERİ DEĞER GİREBİLİRSİN! <type: -error1>"
STRİNGvalueerror = "SAYISAL DEĞER GİREMEZSİN! <type: -error1>"
GecersizOnayError = "Geçersiz girdi! Sadece belirtilen şekilde ifadenizi girin! <type: -error1>"



#OYUNU ZORLAŞIRMAK İÇİN HIRSIZLIK VE REKLAM GİBİ AKSİYON VE İÇERİK EKLE
#reklam kaldırma olabilir yüzde %5 ganimet bolluğu için x tl dersin o da yüzde 10 alır
# 7 güvenlikde bir Şans kutusu satın alma şansı olsun
güvenlik = 0
ÇaylaklarınGelmeOlasılığı = 0.8
TecrübelilerinGelmeOlasılığı = 0.15
HatasızlarınGelmeOlasılığı = 0.05
dükkanseviyesi = 1
Bakiye = 1000
güvenlik = 10


while True:
    vergi_durumu = True

    try:
        print()
        girdi = str(prompt(mavirenkliprompt.format("[Ev] Bir komut gir: ") , completer=KomutCompleter)).strip()
        if girdi == "help" or girdi == "h":
            helperrors()   
        elif girdi == "bellek":
            Belleğigör()
        elif girdi == "bakiye":
            bakiyegoster()
        elif girdi == "komutlar" or girdi == "k":
            komutlarıyazdır()
        elif girdi=="güvenlik" or girdi == "g":
            güvenlikügöster()
        elif girdi == "al" or girdi == "a":
            al()      
        elif girdi == "sat" or girdi == "s":
            sat()
        elif girdi == "darkweb" or girdi == "d":
            pass
        elif girdi == "money%50//50%":
            if qqualitazotoontobdlkkvndlfjk < 1:
                Bakiye = Bakiye + int((Bakiye * 0.5))
                qqualitazotoontobdlkkvndlfjk +=1
            else:
                print(colored("\nLütfen doğru komutu girdiğinden emin ol! <type: -error1>",'red'))
        else:
            print(colored("\nLütfen doğru komutu girdiğinden emin ol! <type: -error1>",'red'))
    except ValueError:
        print(colored("\nLütfen doğru komutu girdiğinden emin ol! <type: -error1>",'red'))
#VERGİYİ BURADAN ALIYORSUN 
#AL VE SAT def fonksiyonlarının başlangıcında bu koşul while true'yı kırar.
    if güvenlik % 30 == 0 and güvenlik > 0 and vergi_durumu == False:
        vergisistemi()
