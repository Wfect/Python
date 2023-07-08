#Kullanıcıdan pozitif sayi bekleyen, negatif sayi girdikce tekrar sayi girmesini isteyen örnek

x = int(input("Bir sayi giriniz : "))

while x < 0 :
    print("Pozitif bir sayi giriniz")
    x = int(input("Bir sayi giriniz: "))
print("Girdiğiniz sayi pozitif ve ", x )

# 0'dan 100'e kadar olan sayıların toplamı 
toplam = 0 
x = 0
while x < 100:
    toplam = toplam + x
    x = x + 1 
print("Toplam : " , toplam)

x = 0 #Burda önce x'i yazıyor. Sonra 1 arttırıp yazıyor. 
while x < 3 : 
    print(x)
    x = x + 1 
#x = 0 Burda x'i 1 arttırıp yazıyor. 1 2 3 
#while x < 3 : 
    #x = x + 1 
    #print(x)
  

