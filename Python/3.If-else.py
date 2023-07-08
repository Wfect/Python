x = int(input("Bir sayi giriniz : "))

if x % 2 == 0:
    print("Girdiginiz sayi çift sayidir ")
else:
    print("Sayi çift sayi değildir.")

#elif if ile yapılan teste ek olarak başka testler yapmak için kullanılır. 

x = int(input("Bir sayi giriniz : "))
if x < 10 :
    print("Sayi 10'dan kücük")
elif x ==10:
    print("Sayi 10'a esit")
else:
    print("Sayi 10'dan büyük")

#NESTED IF
#if içine if yazılmasıdır. 

#Ternary Conditionals
cevap = input("x 2 olsun mu ? y / n : ")
if cevap == 'y':
    x=2
else:
    x=0
print(x)

#Bunun aynısını tek satırda nasıl yaparız?
cevap = input("x 2 olsun mu ? y / n : ")
x = 2 if cevap =='y' else 0
print(x)
