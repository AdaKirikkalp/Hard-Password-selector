#import random
#karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

#uzunluk = int(input("Şifrenizin uzunluğunu giriniz"))

#sifre = ""

#for i in range(uzunluk):
#    karakter = random.choice(karakterler)
 #   sifre += karakter
#print(sifre)




import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifrenizin uzunluğunu giriniz"))

sifre = []

for i in range(uzunluk):
    karakter = random.choice(karakterler)
    sifre.append(karakter)
print(sifre)
print("şifreniz bu")
