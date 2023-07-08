#For döngüsü in'den sonra yazdığımız yapının bütün değerlerinde dolaşıp, eleman sayısı kadar kodu çalıştıracak.
#x in <obje> yapısı ile tanımlandığında x döngünün her adımında in den sonra tanımlanan yapının elemanlarının değerlerini alacak. 


for a in "hello" :
    print(a) 
    #hello da 5 eleman var. For 5 kere çalışıyor.
    #Ekrana hello kelimesinin harflerini yazdırır. 
#range : yazdığımız sayıya kadar olanları gösteriyor. Range'in içine yazılan sayının 1 eksiğine kadar gösteriyor
toplam = 0
for i in range(100) : 
    toplam = toplam + i 
print(toplam)


toplam = 1
for i in range(5) : 
    toplam = toplam * 5
print(toplam)

#Kullanmadığımız değişken olduğunda _ ile gösterilir. 
toplam = 1 
for _ in range(5) : 
    toplam = toplam * 5
print(toplam)

#For loop, while loop kullanarak yazılabilir. Fakat while loop for kullanarak yazılmaz. Çünkü for'da test özelliği yok.

w = "hello"

for c in w : 
    print(c)



l = len(w)
index = 0 

while index < l:
    print(w[index])
    index = index + 1

