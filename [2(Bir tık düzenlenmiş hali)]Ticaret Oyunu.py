import random
from anytree import Node, RenderTree
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.completion import WordCompleter
from termcolor import colored
from tabulate import tabulate




#BU SAÇMALIKLAR YERİNE BİR WHİLE TRUE İLE EĞİTİM MODU EKLE
print (colored("""
 ############################################################
#                                                            #
#    Merhaba! Veriye dayalı Ticaret Oyununa Hoş Geldin.      #
#                                                            #
#                                                            #
#                                                            #
#                                                            #
#    Oyun Başlangıcında 100 altın'a sahipsin.                #
#                                                            #
#    Ticaret Yaparak Bu Parayı Büyüt!                        #
#                                                            #
 ############################################################
""","green"))
print("""
Şimdi Girebileceğin Bazı Kodlar Var!
Hadi Birkaç Örneğini Göstereyim:

#1 ==> "help" komutu: daha fazla yardımcı komut gösterir. Örnek --> help -error3: error3 İsimli Hatanın Neden Kaynaklı Olduğunu Açıklar.

#2 ==>  "bakiye" komutu:  Bulunduğun Andaki Bakiye Miktarını Bir Bilgi Kutusu Kullanarak Ekranına Yazdırır. 
          
#3 ==> "sat" komutu: Belirttiğin Ürünü Satar Ve Bakiyen  Artar. Örnek --> sat -muz: Muz İsimli Ürünlerini Satar Ve Paran Artar.
          
#4 ==> "al" komutu: Belirttiğin Ürünü Satın Alır Ve Bakiyen Azalır. Örnek --> al -elma: Elma İsimli Ürünleri Alır ve Paran Azalır.
      
#5 ==> "envanter" Komutu: Envanterinizde Neler Bulunduğunu Gösterir.

#6 ==> "komutlar" komutu: Oyundaki Tüm komutları Gösterir.
          
          \n""")

def komutlarıyazdır():
    print("")
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
    kacincigün = Node(colored("gün: ",'red',attrs=['bold']) + colored("Kaçıncı günde olduğunu ve vergiye kaç gün kaldığını gösteriri",'green'),parent=child2)
    bakiye = Node(colored("bakiye: ",'red',attrs=['bold']) + colored("Bakiyenizi gösterir",'green'), parent=child2)
    envanter = Node(colored("envanter: ",'red',attrs=['bold']) + colored("Envanterinizi gösterir",'green'), parent=child2)
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
                print("\nVeri Yok!")
                break
            elif helpistek == "help -error4":
                print("\nVeri Yok!")       
                break
            elif helpistek == "help -error5":
                print("\nVeri Yok!")
                break
            elif helpistek == "x":
                break
        except ValueError:
            print(colored("Burada Sadece 'help errorX' komutları kullanılabilir" , 'red'))

def bakiyegoster():
    print()
    print(tabulate([[colored("Bakiyeniz:",'blue',attrs=['bold']),colored("{} altın",'yellow',attrs=['bold']).format(f'{Bakiye:,}')]],tablefmt="rst"))

def envanterigör():
    print()
    data = [[colored("Tahta ",'cyan'),colored(', '.join(Oyuncunun_Tahta_Aksesuarları),'magenta'),"25 - 70"+colored(" altın arası","yellow")], [colored("Taş ",'cyan'),colored(', '.join(Oyuncunun_Taş_Aksesuarları),'magenta'),"170 - 400"+colored(" altın arası","yellow")], [colored("Demir ",'cyan'),colored(', '.join(Oyuncunun_Demir_Aksesuarları),'magenta'),"600 - 1300"+colored(" altın arası","yellow")]]
    print(tabulate(data,headers=[colored("KATEGORİLER",'blue'),colored("AKSESUARLARIN","blue"),colored("FİYAT ARALIĞI",'blue')],tablefmt='double_grid'))
def günügöster():
    global gün
    print(colored("{}. Gündesin!".format(gün),"grey",attrs=['bold']))
    i = int(gün)
    if gün % 7 != 0 and gün > 0:
        while True:
            i = i +1 
            if i % 7 == 0:
                print("Vergi alınmasına {} gün kaldı!".format(i))
                break

def vergisistemi():
    global gün
    global Bakiye
    if gün % 7 == 0:
        oran = Bakiye * 0.1
        Bakiye = Bakiye - int(oran)
        print(colored("Ticaretinizin {}. günü! Tebrikler. ".format(gün),'green'))
        print(colored("İmparatorluk tarafından bakiyenizden",'green')  +colored(" %10 ",'red',attrs=['bold'])  +colored("oranında vergi kesildi! <=<>=> Güncel bakiye:",'green')  +colored(" {} altın".format(Bakiye),'yellow'))

#ÜSTTEKİ KOMUTLAR GÜNÜ ARTIRMAZ!

def piyasaürünbulucu():
        global piyasa
        bulunanlar = []
        for _ in range(5):
            randoms = random.choice(piyasa)
            bulunanlar.append(randoms)
        data = [[colored("Çeşitli Ürünler: ",'cyan'),colored(', '.join(bulunanlar),'magenta')]]
        print()
        print(tabulate(data,headers=[colored("PİYASA","blue"),colored("Ürünler","blue")],tablefmt="double_grid"))
        

#BU KOMUTLARDA HER BİR İNPUT GÜN'E 0.5 EKLEMELİ



def satmak():
    SatSatma = WordCompleter(["sat","satma"])
    global Bakiye, gün, vergi_durumu, UrunIsimTamamlayici
    global Oyuncunun_Tahta_Aksesuarları,Oyuncunun_Taş_Aksesuarları
    global envanterigör, bakiyegoster, günügöster, helperrors




    while True:
        if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
            break
        try:
            print()
            satılacak_mal = str(prompt(mavirenkliprompt.format("Satacağın Malı Seç: "),completer=UrunIsimTamamlayici).lower())
            if satılacak_mal == "envanter":
                envanterigör()
            elif satılacak_mal == "bakiye":
                bakiyegoster()
            elif satılacak_mal == "gün":
                günügöster()
            elif satılacak_mal == "help":
                helperrors()
            elif satılacak_mal in Oyuncunun_Tahta_Aksesuarları:
                while True:
                    try:
                        print("")
                        satış_fiyatı = int(prompt(mavirenkliprompt.format("Satacağın {}'ın değerini belirle [ 0 - 50 altın arası ]: ".format(satılacak_mal))))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 50:
                            break
                        else:
                            print()
                            print(colored("0 altın ile 50 altın arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,'red'))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Tahta_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print()
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} altın".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
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
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi günü",'green'))
                    break
                
                ######RENKLENDİRME VE TEXT EDİTİ BURADA KALDI

            elif satılacak_mal in Oyuncunun_Taş_Aksesuarları:
                while True:
                    try:
                        print()
                        satış_fiyatı = int(input(colored("Satacağın {}'ın değerini belirle [0 altın - 250 altın arası ]".format(satılacak_mal),'blue')))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 250:
                            break
                        else:
                            print()
                            print(colored("0 altın ile 250 altın arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,"red"))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Taş_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print()
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} altın".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
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
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi günü",'green'))
                    break
            elif satılacak_mal in Oyuncunun_Demir_Aksesuarları:
                while True:
                    try:
                        satış_fiyatı = int(input(colored("Satacağın {}'ın değerini belirle [0 altın - 1000 altın arası ]".format(satılacak_mal),'blue')))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 1000:
                            break
                        else:
                            print()
                            print(colored("0 altın ile 1000 altın arasında bir fiyat belirle! <type: -error1>",'red'))
                    except ValueError:
                        print()
                        print(colored(intvalueerror,"red"))
                while True:
                    try:
                        print()
                        onaylamak = str(prompt(mavirenkliprompt.format("Sat - Satma: "),completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Demir_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print()
                            print(colored("İşleminiz Gerçekleşti! ",'green')+colored("{} altın".format(satış_fiyatı),'yellow')+colored(" kazandın tebrikler!",'green'))
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
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print()
                    print(colored("vergi günü",'green'))
                    break
            elif satılacak_mal == "x":
                break
            else: 
                print()
                print("Böyle bir ürünün yok! Lütfen Envanterinde bulunan ürünlerden bir seçim yap. <type: error3>",'red')
        except ValueError:
            print(colored("Ürünün adını doğru ve eksiksiz girdiğinizden emin olun <type: -error1>",'red'))

def al():
    global vergi_durumu, gün, piyasa, Bakiye, UrunIsimTamamlayici
    global Tahta_Aksesuarlar, Taş_Aksesuarlar
    global Oyuncunun_Tahta_Aksesuarları, Oyuncunun_Taş_Aksesuarları
    global piyasaürünbulucu, envanterigör, bakiyegoster, günügöster, helperrors

    while True:
        DEMİRyüksekfiyat = random.randint(600,1300)
        TAŞortafiyat = random.randint(170,400)
        TAHTAdüşükfiyat = random.randint(25,70)
        if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
            break
        try:
            print()
            satınalınacakmal = str(prompt(mavirenkliprompt.format("Almak istediğin ürünün adını gir: [ 'i' komutu piyasada hazırda bulunan ürünleri gösterir] [x] "),completer=UrunIsimTamamlayici).lower())
            if satınalınacakmal ==  "i":
                piyasaürünbulucu()
            elif satınalınacakmal == "envanter":
                envanterigör()
            elif satınalınacakmal == "bakiye":
                bakiyegoster()
            elif satınalınacakmal == "gün":
                günügöster()
            elif satınalınacakmal == "help":
                helperrors()
            elif satınalınacakmal in piyasa:
                if satınalınacakmal in Tahta_Aksesuarlar:
                    while True:
                        try:    
                            print()      
                            alveyaalma = prompt(mavirenkliprompt.format("Almak üzere olduğun tahta ürünün fiyatı {} altın! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(TAHTAdüşükfiyat)),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if Bakiye >= TAHTAdüşükfiyat and alveyaalma == "1" or alveyaalma == "evet"  :
                                    Bakiye = Bakiye - TAHTAdüşükfiyat
                                    Oyuncunun_Tahta_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print()
                                    print(colored("İşleminiz Gerçekleşti! Bakiyenizden ",'green')+colored("{} altın".format(TAHTAdüşükfiyat),'yellow')+colored(" eksildi!",'green'))
                                    bakiyegoster()
                                    break
                                elif Bakiye < TAHTAdüşükfiyat and alveyaalma == "1" or alveyaalma == "evet"  :
                                    print()
                                    print(colored("Bakiyeniz Bu Ürünü Alabilmek İçin Yetersiz! Bakiye: {} altın <type: -error2>".format(Bakiye),"red"))
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print()
                                print(colored(GecersizOnayError,'red'))
                        except ValueError:
                            print()
                            print(colored(GecersizOnayError))
                    if gün % 7 == 0:
                        print()
                        print(colored("vergi günü",'green'))
                        break
                elif satınalınacakmal in Taş_Aksesuarlar:
                    while True:
                        try:            
                            print()
                            alveyaalma = prompt(mavirenkliprompt.format("Almak üzere olduğun taş ürünün fiyatı {} altın! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(TAŞortafiyat)),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if Bakiye >= TAŞortafiyat and alveyaalma == "1" or alveyaalma == "evet":
                                    Bakiye = Bakiye - TAŞortafiyat
                                    Oyuncunun_Taş_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print()
                                    print(colored("İşleminiz Gerçekleşti! Bakiyenizden ",'green')+colored("{} altın".format(TAŞortafiyat),'yellow')+colored(" eksildi!",'green'))
                                    bakiyegoster()
                                    break
                                elif Bakiye < TAŞortafiyat and alveyaalma =="1" or alveyaalma == "evet":
                                    print(colored("Bakiyeniz Bu Ürünü Alabilmek İçin Yetersiz! Bakiye: {} altın <type: -error2>".format(Bakiye),"red"))
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print()
                                print(colored(GecersizOnayError,'red'))
                        except ValueError:
                            print()
                            print(colored(GecersizOnayError))
                    if gün % 7 == 0:
                        print()
                        print(colored("vergi günü",'green'))
                        break
                elif satınalınacakmal in Demir_Aksesuarlar:
                    while True:
                        try:      
                            print()      
                            alveyaalma = prompt(mavirenkliprompt.format("Almak üzere olduğun demir ürünün fiyatı {} altın! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(DEMİRyüksekfiyat)),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if Bakiye >= DEMİRyüksekfiyat and alveyaalma == "1" or alveyaalma == "evet":
                                    Bakiye = Bakiye - DEMİRyüksekfiyat
                                    Oyuncunun_Demir_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print()
                                    print(colored("İşleminiz Gerçekleşti! Bakiyenizden ",'green')+colored("{} altın".format(DEMİRyüksekfiyat),'yellow')+colored(" eksildi!",'green'))
                                    bakiyegoster()
                                    break
                                elif Bakiye < DEMİRyüksekfiyat and alveyaalma == "1" or alveyaalma == "evet":
                                    print(colored("Bakiyeniz Bu Ürünü Alabilmek İçin Yetersiz! Bakiye: {} altın <type: -error2>".format(Bakiye),"red"))
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print()
                                print(colored(GecersizOnayError,'red'))
                        except ValueError:
                            print()
                            print(colored(GecersizOnayError))
                    if gün % 7 == 0:
                        print()
                        print(colored("vergi günü",'green'))
                        break
            elif satınalınacakmal == "x":
                break
            else:
                print()
                print(colored("Ürün ismini doğru girdiğinden emin ol! Piyasada böyle bir ürün bulunamadı. <type: -error1>",'red'))
        except ValueError:
            print(colored(STRİNGvalueerror,'red'))
            
#PROMPT TAMAMLAYICI
UrunIsimTamamlayici = WordCompleter(["bakiye","gün","help","envanter","kiliç (tahta)", "kalkan (tahta)", "ok (tahta)", "yay (tahta)", "zirh (tahta)", "migfer (tahta)", "mizrak (tahta)", "kiliç (taş)", "kalkan (taş)", "ok (taş)", "yay (taş)", "zirh (taş)", "migfer (taş)", "mizrak (taş)", "kiliç (demir)", "kalkan (demir)", "ok (demir)", "yay (demir)", "zirh (demir)", "migfer (demir)", "mizrak (demir)"])
helpcompleter = WordCompleter(["help -error1","help -error2","help -error3","help -error4","help -error5"])
KomutCompleter = WordCompleter(["help","envanter","bakiye","komutlar","gün","al","sat","x"])
OnayCompleter = WordCompleter(["evet","hayir"])

gün = 0
Bakiye = 100


#PROMPT RENKLENDİRİCİLER
mavirenkliprompt = HTML('<ansiblue><b>{}</b></ansiblue>')
kirmizirenkliprompt = HTML('<ansired><b>{}</b></ansired>')

#HATA MESAJLARI
İNTEGERvalueerror = "SADECE TAM SAYI GİREBİLİRSİN! <type: -error1>"
intvalueerror = "SADECE TAM SAYI DEĞERİ DEĞER GİREBİLİRSİN! <type: -error1>"
STRİNGvalueerror = "SAYISAL DEĞER GİREMEZSİN! <type: -error1>"
GecersizOnayError = "Geçersiz girdi! Sadece belirtilen şekilde ifadenizi girin! <type: -error1>"


#piyasadaki random ürünler
Tahta_Aksesuarlar = ["kiliç (tahta)","kalkan (tahta)","ok (tahta)","yay (tahta)","zirh (tahta)","migfer (tahta)","mizrak (tahta)"]
Taş_Aksesuarlar   = ["kiliç (taş)","kalkan (taş)","ok (taş)","yay (taş)","zirh (taş)","migfer (taş)","mizrak (taş)"]
Demir_Aksesuarlar = ["kiliç (demir)","kalkan (demir)","ok (demir)","yay (demir)","zirh (demir)","migfer (demir)","mizrak (demir)"]
piyasa = Taş_Aksesuarlar + Tahta_Aksesuarlar + Demir_Aksesuarlar

#ENVANTER
Oyuncunun_Tahta_Aksesuarları = [random.choice(Tahta_Aksesuarlar),random.choice(Tahta_Aksesuarlar)]
Oyuncunun_Taş_Aksesuarları = [random.choice(Taş_Aksesuarlar)]
Oyuncunun_Demir_Aksesuarları = []

#VERGİ SİSTEMİ EKLE               ++eklendi++

#OYUNU ZORLAŞIRMAK İÇİN HIRSIZLIK VE REKLAM GİBİ AKSİYON VE İÇERİK EKLE
#reklam kaldırma olabilir yüzde %5 ganimet bolluğu için x tl dersin o da yüzde 10 alır
# 7 günde bir Şans kutusu satın alma şansı olsun


while True:
    vergi_durumu = True

    try:
        print()
        girdi = str(prompt(mavirenkliprompt.format("Bir komut gir:") , completer=KomutCompleter)).strip()
        if girdi == "help" :
            helperrors()   
        elif girdi == "envanter":
            envanterigör()
        elif girdi == "bakiye":
            bakiyegoster()
        elif girdi == "komutlar":
            komutlarıyazdır()
        elif girdi=="gün":
            günügöster()


        ################################################################################


        elif girdi == "al":
            al()      
        elif girdi == "sat":
            satmak()
        else:
            print(colored("\nError1","Lütfen doğru komutu girdiğinden emin ol! <type: -error1>",'red'))
    except ValueError:
        print(colored("\nError1","Lütfen doğru komutu girdiğinden emin ol! <type: -error1>",'red'))
#VERGİYİ BURADAN ALIYORSUN 
#AL VE SAT def fonksiyonlarının başlangıcında bu koşul while true'yı kırar.
    if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
        vergisistemi()
