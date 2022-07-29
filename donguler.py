#FOR Döngüsü

liste=[1,2,3,4,5,6]
for eleman in liste:
    print(eleman) #listeyi ekrana yazdırır

toplam =0
liste2=[1,2,3,4,5,6,7]

for eleman1 in liste2:
    toplam+= eleman1 #toplam = toplam + eleman1 anlamına gelir
    print("Kümülatif toplam: {}, Eleman değeri: {}".format(toplam,eleman1)) #print ifadesi bir tab boşlukla yazıldığı için for döngüsü içinde yer alır
    # ve her toplamı adım adım gösterir.
    #1 3 6 10 15 21 28 ekran çıktısını verir
print(toplam) #print komutu boşluksuz yazıldığı için for döngüsünün dışındadır ve sadece son ifade olan 28 çıktısını verir


liste3=[1,3,4,6,7,9,12,32,23,43,21,54,64,87,42,94,86,90,77,66,55,99,88,345]
for eleman3 in liste3:
    if eleman3%2==0:
        print(eleman3) #bir listedeki sadece çift sayıları ekrana yazdırdık

demet=[(1,2),(3,4),(5,6),(7,8)]
for (i,j) in demet:
    print("i: {} j: {}".format(i,j))



#WHILE Döngüsü

i=0
while(i<10):
    print(i)
    i+=1 #i 10'dan küçük olan son sayıya kadar 1 artar ve mevcut sayıyı ekrana yazdırır.


j=0
while(j<20):
    print(j)
    j+=2 #j 20'den küçük olan son sayıya kadar 2 artar ve mevcut sayıyı ekrana yazdırır.


index=0
while(index<=len("index")):
    print("index"[:index])
    index+=1 #index yazarak piramit oluşturduk

a=range(0,5) #0'dan 5'e kadar sayı oluşturduk. (5 dahil değil) a'ya da bu sayı dizisini eşitledik
#range(5) yazarsak da olur. herhangi bir başlangıç değeri vermezsek otomatik olarak 0 alır.
print(*a) #bu diziyi yazdırmak için başına* koymamız lazım
print(a) #yıldız koymazsak range(0,5) çıktısını verir

teksayilar=range(1,100,2) #1'den başlayıp 100'e kadar 2'şer atlayarak sayı dizisi oluşturur.
teksayilar2=range(99,0,-2) #99'dan başlayarak 0'a kadar 2'şer azalarak sayı dizisi oluşturur.
print(*teksayilar,"\n",*teksayilar2)












