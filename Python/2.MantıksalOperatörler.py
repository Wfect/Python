not True #False return eder. 

not False # True return eder. 

not 5 < 6 #False return eder. Öncelikle 5 < 6 ifadesine bakılır. Sonra not alınır

not 5 == 5 # False return eder. 

a = 2
b=3
not a < b #False return eder. 

#AND 
#Sadece iki değerde true ise true return eder. 

#OR
#Sadece iki değerde false ise false return eder. 

#SHORT CIRCUIT
print("SHORT CIRCUIT")

#Short circut ,fadenin tamamının değerlendirilmesine gerek olmadığında,
#geri kalan kısmın değerlendirilmeden atlanması anlamına gelir.
#Bu durum, "and" ve "or" operatörleriyle ilgilidir.
#"and" operatörü kullanıldığında, Python ifadenin sol tarafının
#False (yalan) değerini verirse, ifadenin geri kalanı
#değerlendirilmeden False olarak kabul edilir.
#Eğer sol taraf True (doğru) ise, sağ tarafın değeri ifade
#sonucunu belirler.

#"or" operatörü kullanıldığında, Python ifadenin sol tarafının
#True (doğru) değerini verirse, ifadenin geri kalanı değerlendirilmeden
#True olarak kabul edilir. Eğer sol taraf False (yalan) ise, sağ tarafın
#değeri ifade sonucunu belirler.
(5 < 3) and print("hello") # False return eder. 
# And ifadesinde sol taraf false ise sağ taraftaki ifadeye bakmaya gerek yok. 
# And ifadesinde sol taraf true olur ise sağ tarafa bakmak gerekir. 
(5 > 3) or  print("hello") # True return eder 

(5 < 3) or print("hello") #hello return eder. 

(5 > 3) and print("hello") #Hey return eder. 

# & da and gibi çalışır fakat short circuit yapmaz. 
# | da or gibi çalışır fakat short circuit yapmaz. 



