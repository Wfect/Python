#Veri Objeleri 2'ye ayrılır
    #Scalar: Daha alt parçalara bölünemeyen yapılar(sayılar gibi)
    #Non-scalar: Daha alt parçalara bölünebilen yapılardır. 
#Boolean
    # Bir ifadenin doğru veya yanlış olduğunu belirten yapıdır.abs
    # 2>3 false
#Type
    #Objelerin tiplerine type() ile bakılır. 
    # type(2) int, type(2.3) float, type(true) bool
#Type Casting
    #Data objelerinin tiplerini dönüştürmeye denir. 
    #int(2.4) 2, int(2.8) 2 : Burda sadece sayının tam kısmı alınır. 
#Operators and Expressions
    #İşlemlerde ifadelerden birisi floatsa sonuç float tipinde olur.
#String
    #("örnek") veya ('örnek') olarak belirtilir.
    #String non-scaler bir veri objesidir.
    #String İmmutable veri tipidir. Yani elemanların değeri değiştirilemez. 

print("Stringlere Değer Atama (Variables Assignment) ")

merhaba = "Hello World"
print(merhaba)

print("5" + "4") #Birleştirme yapıyor. 
print("Merhaba" + "Selam") 
print("Merhaba" + " " + "Selam") #boşluk bırakır
print("---------------")

print("Stinglerde Ardisik Birlestirme")
#Stringlerde * işlemi birleştirmeyi sağlar.
print(4*"selam ")
print(len("4")) # Stringin kaç karakterden oluştuğunu gösterir. Boşluklarıda sayar. 
print(len("selam merhaba"))

print("--------------")
print("Stringlerde indexing")
#İndexing 0 dan başlar.
#Son elemanı elde etmek için [-1] yazarız. Sondan ikinci için [-2] 
isim = "name"
print(isim[1])
print("name"[1]) 
print("---------------")
print("Slicing")
#Birden fazla elemanı listelemek istiyorsak print(isim[0:3]) olarak gösterebiliriz. 
print(isim[0:3]) # Önemli nokta 0. eleman dahil edilirken 3. eleman dahil edilmez. 
#Başlangıcı belirtmezsek python default olarak başlangıç değerini 0 alıyor. 
print(isim[:3])
#Bitişi belirtmezsek python stringin sonuna kadar alıyor. Son elemanıda dahil ediyor. 
#Slicing yaparken bitiş olarak verdiğimiz değer en büyük indeximizden büyükse hata almayız, sadece sonuna kadar almış olur
#Başlangıç:bitiş olarak slicing yapabileceğimiz gibi, başlangıç:bitiş:adım formunda da slicing yapabiliriz.
#Burada adım parametresi kaçar kaçar gideceğimizi belirler.
print(isim[0:8:2])
#Adım eksi bir değer de olabilir. Böylece ters yönce gitmiş oluruz.
#Ama başlangıç değerinin bitiş değerinden büyük olması lazım bunu yapabilmem için.
#0.indexten 10. indexe 2 azalarak gidemez, o yüzden boş string döndürür
print(isim[0:10:-1]) #boş string döndürür
print(isim[::-1])

print("---------------------")
print("Kullanıcıdan Input Alma")

x=int(input("Bir sayi giriniz: ")) # input sonucunda string değer elde edilir

print(x + 5 )



