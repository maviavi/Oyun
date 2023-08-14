import random
from anytree import Node, RenderTree
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

print ("""
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
""")
print("""
Şimdi Girebileceğin Bazı Kodlar Var!
Hadi Birkaç Örneğini Göstereyim:

#1 ==> "help" komutu: daha fazla yardımcı komut gösterir. Örnek --> help -error3: error3 İsimli Hatanın Neden Kaynaklı Olduğunu Açıklar.

#2 ==>  "bakiye" komutu:  Bulunduğun Andaki Bakiye Miktarını Bir Bilgi Kutusu Kullanarak Ekranına Yazdırır. 
          
#3 ==> "sat" komutu: Belirttiğin Ürünü Satar Ve Bakiyen  Artar. Örnek --> sat -muz: Muz İsimli Ürünlerini Satar Ve Paran Artar.
          
#4 ==> "al" komutu: Belirttiğin Ürünü Satın Alır Ve Bakiyen Azalır. Örnek --> al -elma: Elma İsimli Ürünleri Alır ve Paran Azalır.
      
#5 ==> "envanter" Komutu: Envanterinizde Neler Bulunduğunu Gösterir.

#6 ==> "komutlar" komutu: Oyundaki Tüm komutları Gösterir. Çok Yer Kaplar Ona Göre! ;) 
          
          """)

def komutlarazı():
    print("")
        # Ağaç yapısını oluştur
    komutlar = Node("Komutlar")
    geri = Node("x", parent=komutlar)
    aciklamax = Node("Herhangi bir yerde 'vazgeçmek' görevini yerine getirir ve komutn çalışmasını sonlandırır", parent=geri)
    help = Node("'help'", parent=komutlar)
    help_error1 = Node("'help -error1'        Hatanın neden kaynaklı olduğunu ekrana yazdırır", parent=help)
    help_error2 = Node("'help -error2'        Hatanın neden kaynaklı olduğunu ekrana yazdırır", parent=help)
    help_error3 = Node("'help -error3'        Hatanın neden kaynaklı olduğunu ekrana yazdırır", parent=help)
    help_error4 = Node("'help -error4'        Hatanın neden kaynaklı olduğunu ekrana yazdırır", parent=help)
    help_error5 = Node("'help -error5'        Hatanın neden kaynaklı olduğunu ekrana yazdırır", parent=help)
    boşluk = Node("",parent=help)

    child2 = Node("İŞLEM KOMUTLARI: ", parent=komutlar)
    boşluk = Node("", parent=child2)
    kacincigün = Node("'gün'      Kaçıncı günde olduğunu ve vergiye kaç gün kaldığını gösteriri",parent=child2)
    bakiye = Node("'bakiye'           Bakiyenizi gösterir", parent=child2)
    envanter = Node("'envanter'           Envanterinizi gösterir", parent=child2)
    al = Node("'al'           Bir ürün almanızı sağlar", parent=child2)
    sat = Node("'sat'         Bir ürün satmanızı sğalar", parent=child2)
    boşluk = Node("", parent=child2)




    # Ağaç yapısını görselleştir
    for pre, fill, node in RenderTree(komutlar):
        print(f"{pre}{node.name}")

def helperrors():
    global helpcompleter
    while True:
        try:    
            helpistek = str(prompt("'help -error1' şeklinde komut gir [x = vazgeç]  : " ,completer=helpcompleter).lower())
            if helpistek == "help -error1":
                print("""
Error1 Lütfen Doğru Komutu Girdiğinizden Emin Olun!

Komut Gir Kısmında Sayısal Değer Veya Tanımlı Olmayan Bir Metin Değeri Giremezsiniz!

Küçük Yazım Yanlışları Da Buna Dahildir 

""")
                break
            elif helpistek == "help -error2":
                print("veri Yok!")
                break
            elif helpistek == "help -error3":
                print("Veri Yok!")
                break
            elif helpistek == "help -error4":
                print("Veri Yok!")       
                break
            elif helpistek == "help -error5":
                print("Veri Yok!")
                break
            elif helpistek == "x":
                break
        except ValueError:
            print("Burada Sadece 'help errorX' komutları kullanılabilir" )
                 
def showmoney():
    print("Bakiyeniz","{} altın".format(Bakiye))

def envanterigör():
    print("""

    Tahta Aksesuarların: {}
          
    Taş Aksesuarların: {}
          
    Demir Aksesuarların: {}
        

""".format(Oyuncunun_Tahta_Aksesuarları,Oyuncunun_Taş_Aksesuarları,Oyuncunun_Demir_Aksesuarları))
    
def günügöster():
    global gün
    print("{}. Gündesin!".format(gün))

def vergisistemi():
    global gün
    global Bakiye
    if gün % 7 == 0:
        oran = Bakiye * 0.1
        Bakiye = Bakiye - int(oran)
        print("Ticaretinizin {}. günü! Tebrikler. ".format(gün))
        print("İmparatorluk tarafından bakiyenizden %10 oranında vergi kesildi. {} altın".format(Bakiye))

#ÜSTTEKİ KOMUTLAR GÜNÜ ARTIRMAZ!


#BU KOMUTLARDA HER BİR İNPUT GÜN'E 0.25 EKLER
def satmak():
    SatSatma = WordCompleter(["sat","satma"])
    global Bakiye
    global Oyuncunun_Tahta_Aksesuarları
    global Oyuncunun_Taş_Aksesuarları
    global gün
    global vergi_durumu
    global UrunIsimTamamlayici

    while True:
        if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
            break
        try:

            satılacak_mal = str(prompt("Satacağın Malı Seç:",completer=UrunIsimTamamlayici).lower())
            if satılacak_mal in Oyuncunun_Tahta_Aksesuarları:
                while True:
                    try:
                        satış_fiyatı = int(input("Satacağın {}'ın değerini belirle [0 altın - 20 altın arası ]".format(satılacak_mal)))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 20:
                            break
                        else:
                            print("0 altın ile 20 altın arasında bir fiyat belirle!")
                    except ValueError:
                        print(intvalueerror)
                while True:
                    try:
                        onaylamak = str(prompt("Sat - Satma : ",completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Tahta_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print("İşleminiz Gerçekleşti! {} altın para kazandın tebrikler!".format(satış_fiyatı))
                            print("Bakiyeniz: {} altın".format(Bakiye)) 
                            break
                        elif onaylamak == "satma"or onaylamak =="Satma":
                            break
                        else:
                            print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin!")
                    except ValueError:
                        print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme")
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print("vergi günü")
                    break
                while True:
                    try:
                        envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                        if envanterigormekistermisin in ["0","1","evet","hayir"]:
                            if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                if not Oyuncunun_Tahta_Aksesuarları == []:
                                    print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                if not Oyuncunun_Taş_Aksesuarları == []:
                                    print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                if not Oyuncunun_Demir_Aksesuarları == []:
                                    print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                break
                            elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                break
                        elif envanterigormekistermisin == "x":
                            break
                        else:
                            print(GecersizOnayError)
                    except ValueError:
                        print(GecersizOnayError)
            elif satılacak_mal in Oyuncunun_Taş_Aksesuarları:
                while True:
                    try:
                        satış_fiyatı = int(input("Satacağın {}'ın değerini belirle [0 altın - 50 altın arası ]".format(satılacak_mal)))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 50:
                            break
                        else:
                            print("0 altın ile 50 altın arasında bir fiyat belirle!")
                    except ValueError:
                        print(intvalueerror)
                while True:
                    try:
                        onaylamak = str(prompt("Sat - Satma : ",completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Taş_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print("İşleminiz Gerçekleşti! {} altın para kazandın tebrikler!".format(satış_fiyatı))
                            print("Bakiyeniz: {} altın".format(Bakiye)) 
                            break
                        elif onaylamak == "satma" or onaylamak == "Satma":
                            break
                        else:
                            print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin!")
                    except ValueError:
                        print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme")
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print("vergi günü")
                    break
                while True:
                    try:
                        envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                        if envanterigormekistermisin in ["0","1","evet","hayir"]:
                            if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                if not Oyuncunun_Tahta_Aksesuarları == []:
                                    print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                if not Oyuncunun_Taş_Aksesuarları ==  []:
                                    print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                if not Oyuncunun_Demir_Aksesuarları == []:
                                    print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                break
                            elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                break
                        elif envanterigormekistermisin == "x":
                            break
                        else:
                            print(GecersizOnayError)
                    except ValueError:
                        print(GecersizOnayError)
            elif satılacak_mal in Oyuncunun_Demir_Aksesuarları:
                while True:
                    try:
                        satış_fiyatı = int(input("Satacağın {}'ın değerini belirle [0 altın - 200 altın arası ]".format(satılacak_mal)))
                        if satış_fiyatı >= 0 and satış_fiyatı <= 200:
                            break
                        else:
                            print("0 altın ile 200 altın arasında bir fiyat belirle!")
                    except ValueError:
                        print(intvalueerror)
                while True:
                    try:
                        onaylamak = str(prompt("Sat - Satma : ",completer=SatSatma))
                        if onaylamak == "sat" or onaylamak == "Sat":            
                            Bakiye =  Bakiye + satış_fiyatı
                            Oyuncunun_Demir_Aksesuarları.remove(satılacak_mal)
                            gün += 0.5
                            vergi_durumu = False
                            print("İşleminiz Gerçekleşti! {} altın para kazandın tebrikler!".format(satış_fiyatı))
                            print("Bakiyeniz: {} altın".format(Bakiye)) 
                            break
                        elif onaylamak == "satma" or onaylamak == "Satma":
                            break
                        else:
                            print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin!")
                    except ValueError:
                        print("Sadece 'Sat' veya 'Satma' ifadesi girebilirsin! Sayısal değer girme")
                if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
                    print("vergi günü")
                    break
                while True:
                    try:
                        envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                        if envanterigormekistermisin in ["0","1","evet","hayir"]:
                            if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                if not Oyuncunun_Tahta_Aksesuarları == []:
                                    print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                if not Oyuncunun_Taş_Aksesuarları ==  []:
                                    print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                if not Oyuncunun_Demir_Aksesuarları == []:
                                    print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                break
                            elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                break
                        elif envanterigormekistermisin == "x":
                            break
                        else:
                            print(GecersizOnayError)
                    except ValueError:
                        print(GecersizOnayError)
            elif satılacak_mal == "x":
                break
        except ValueError:
            print("Ürünün adını doğru ve eksiksiz girdiğinizden emin olun")

def al():
    global vergi_durumu
    global gün
    global piyasa
    global Tahta_Aksesuarlar
    global Taş_Aksesuarlar
    global Bakiye
    global Oyuncunun_Tahta_Aksesuarları
    global Oyuncunun_Taş_Aksesuarları
    global UrunIsimTamamlayici
    while True:
        DEMİRyüksekfiyat = random.randint(50,300)
        TAŞortafiyat = random.randint(20,60)
        TAHTAdüşükfiyat = random.randint(5,30)
        if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
            break
        try:
            satınalınacakmal = str(prompt("Almak istediğin ürünün adını gir: [ 'i' komutu piyasada hazırda bulunan ürünleri gösterir] [x] ",completer=UrunIsimTamamlayici).lower())

            if satınalınacakmal ==  "i":
                bulunanlar = []
                for _ in range(10):
                    randoms = random.choice(piyasa)
                    bulunanlar.append(randoms)
                print("Piyasada bu ürünler bulunabildi {}".format(bulunanlar), "Tabiki doğru tahminle farklı ürünler de bulunabilir, şansa bağlı!")
            elif satınalınacakmal in piyasa:
                if satınalınacakmal in Tahta_Aksesuarlar:
                    while True:
                        try:            
                            alveyaalma = prompt("Almak üzere olduğun tahta ürünün fiyatı {} altın ! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(TAHTAdüşükfiyat),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if alveyaalma == "1" or alveyaalma == "evet":
                                    Bakiye = Bakiye - TAHTAdüşükfiyat
                                    Oyuncunun_Tahta_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print("İşleminiz gerçekleşti tebrikler! Bakiyenizden {} altın eksildi".format(TAHTAdüşükfiyat))
                                    print("Bakiyeniz: {} altın".format(Bakiye))
                                    if gün % 7 == 0:
                                        print("vergi günü")
                                        break
                                    while True:
                                        try:
                                            envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                                            if envanterigormekistermisin in ["0","1","evet","hayir"]:
                                                if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                                    if not Oyuncunun_Tahta_Aksesuarları == []:
                                                        print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                                    if not Oyuncunun_Taş_Aksesuarları ==  []:
                                                        print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                                    if not Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                                    if Oyuncunun_Tahta_Aksesuarları == [] and Oyuncunun_Taş_Aksesuarları == [] and Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Envanterin Boş!")
                                                    break
                                                elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                                    break
                                            elif envanterigormekistermisin == "x":
                                                break
                                            else:
                                                print(GecersizOnayError)
                                        except ValueError:
                                            print(GecersizOnayError)
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print(GecersizOnayError)
                        except ValueError:
                            print(GecersizOnayError)
                elif satınalınacakmal in Taş_Aksesuarlar:
                    while True:
                        try:            
                            alveyaalma = prompt("Almak üzere olduğun ürünün fiyatı {} altın ! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(TAŞortafiyat),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if alveyaalma == "1" or alveyaalma == "evet":
                                    Bakiye = Bakiye - TAŞortafiyat
                                    Oyuncunun_Taş_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print("İşleminiz gerçekleşti tebrikler! Bakiyenizden {} altın eksildi".format(TAŞortafiyat))
                                    print("Bakiyeniz: {} altın".format(Bakiye))
                                    if gün % 7 == 0:
                                        print("vergi günü")
                                        break
                                    while True:
                                        try:
                                            envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                                            if envanterigormekistermisin in ["0","1","evet","hayir"]:
                                                if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                                    if not Oyuncunun_Tahta_Aksesuarları == []:
                                                        print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                                    if not Oyuncunun_Taş_Aksesuarları ==  []:
                                                        print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                                    if not Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                                    if Oyuncunun_Tahta_Aksesuarları == [] and Oyuncunun_Taş_Aksesuarları == [] and Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Envanterin Boş!")
                                                    break
                                                elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                                    break
                                            elif envanterigormekistermisin == "x":
                                                break
                                            else:
                                                print(GecersizOnayError)
                                        except ValueError:
                                            print(GecersizOnayError)
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print("SADECE 0 VEYA 1 İLE  YANIT VER")
                        except ValueError:
                            print(GecersizOnayError)
                elif satınalınacakmal in Demir_Aksesuarlar:
                    while True:
                        try:            
                            alveyaalma = prompt("Almak üzere olduğun ürünün fiyatı {} altın ! Satın almak ister misin? [Evet = 1 , Hayir = 0 , 'x']  ".format(DEMİRyüksekfiyat),completer=OnayCompleter).lower()
                            if alveyaalma in ["0","1","hayir","evet"]:
                                if alveyaalma == "1" or alveyaalma == "evet":
                                    Bakiye = Bakiye - DEMİRyüksekfiyat
                                    Oyuncunun_Demir_Aksesuarları.append(satınalınacakmal)
                                    gün += 0.5
                                    vergi_durumu = False
                                    print("İşleminiz gerçekleşti tebrikler! Bakiyenizden {} altın eksildi".format(DEMİRyüksekfiyat))
                                    print("Bakiyeniz: {} altın".format(Bakiye))
                                    if gün % 7 == 0:
                                        print("vergi günü")
                                        break
                                    while True:
                                        try:
                                            envanterigormekistermisin = prompt("Envanteri görmek ister misin? [Evet = 1  ,  Hayir = 0 , 'x']", completer=OnayCompleter)
                                            if envanterigormekistermisin in ["0","1","evet","hayir"]:
                                                if envanterigormekistermisin == "1" or envanterigormekistermisin == "evet":
                                                    if not Oyuncunun_Tahta_Aksesuarları == []:
                                                        print("Tahta Aksesuarların: ", Oyuncunun_Tahta_Aksesuarları)
                                                    if not Oyuncunun_Taş_Aksesuarları ==  []:
                                                        print("Taş Aksesuarların: ", Oyuncunun_Taş_Aksesuarları)
                                                    if not Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Demir Aksesuarların: ", Oyuncunun_Demir_Aksesuarları)
                                                    if Oyuncunun_Tahta_Aksesuarları == [] and Oyuncunun_Taş_Aksesuarları == [] and Oyuncunun_Demir_Aksesuarları == []:
                                                        print("Envanterin Boş!")
                                                    break
                                                elif envanterigormekistermisin == "0" or envanterigormekistermisin == "hayir":
                                                    break
                                            elif envanterigormekistermisin == "x":
                                                break
                                            else:
                                                print(GecersizOnayError)
                                        except ValueError:
                                            print(GecersizOnayError)
                                    break
                                elif alveyaalma == "0" or alveyaalma == "hayir":
                                    break
                            elif alveyaalma == "x":
                                break
                            else:
                                print("SADECE 0 VEYA 1 İLE  YANIT VER")
                        except ValueError:
                            print(GecersizOnayError)
            elif satınalınacakmal == "x":
                break
            else:
                print("Ürün ismini doğru girdiğinden emin ol!")
        except ValueError:
            print(STRİNGvalueerror)
            
#PROMPT TAMAMLAYICI
UrunIsimTamamlayici = WordCompleter(["kiliç (tahta)", "kalkan (tahta)", "ok (tahta)", "yay (tahta)", "zirh (tahta)", "migfer (tahta)", "mizrak (tahta)", "kiliç (taş)", "kalkan (taş)", "ok (taş)", "yay (taş)", "zirh (taş)", "migfer (taş)", "mizrak (taş)", "kiliç (demir)", "kalkan (demir)", "ok (demir)", "yay (demir)", "zirh (demir)", "migfer (demir)", "mizrak (demir)"])
helpcompleter = WordCompleter(["help -error1","help -error2","help -error3","help -error4","help -error5"])
KomutCompleter = WordCompleter(["help","envanter","bakiye","komutlar","gün","al","sat","x"])
OnayCompleter = WordCompleter(["evet","hayir"])


gün = 0
Bakiye = 100 

İNTEGERvalueerror = "SADECE TAM SAYI GİREBİLİRSİN!"
intvalueerror = "SADECE TAM SAYI DEĞERİ DEĞER GİREBİLİRSİN!"
STRİNGvalueerror = "SAYISAL DEĞER GİREMEZSİN!"
GecersizOnayError = "Geçersiz girdi! Sadece belirtilen şekilde ifadenizi girin!"


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
        girdi = str(prompt("Bir Komut Gir:  " , completer=KomutCompleter))
        if girdi == "help" :
            helperrors()   
        elif girdi == "envanter":
            envanterigör()
        elif girdi == "bakiye":
            showmoney()
        elif girdi == "komutlar":
            komutlarazı()
        elif girdi=="gün":
            günügöster()


        ################################################################################


        elif girdi == "al":
            al()      
        elif girdi == "sat":
            satmak()
        else:
            print("Error1","Lütfen doğru komutu girdiğinizden emin olun!")
    except ValueError:
        print("Error1","Lütfen doğru komutu girdiğinizden emin olun!")
#VERGİYİ BURADAN ALIYORSUN 
#AL VE SAT def fonksiyonlarının başlangıcında bu koşul while true'yı kırar.
    if gün % 7 == 0 and gün > 0 and vergi_durumu == False:
        vergisistemi()
