def Topla(sayi1,sayi2):
    return sayi1 + sayi2

def Cıkart(sayi1,sayi2):
    return sayi1 - sayi2

def Carp(sayi1,sayi2):
    return sayi1 * sayi2

def Bol(sayi1,sayi2):
    return sayi1 / sayi2

print("Operasyon:")
print("1 : Topla")
print("2 : Cıkart")
print("3 : Carp")
print("4 : Bol")

secenek = input("Operasyon seçiminiz?")

sayi1 = int(input("Birinci sayı?"))
sayi2 = int(input("İkinci sayı"))

if secenek == '1':
    print("Toplam : " + str(Topla(sayi1, sayi2)))
    
if secenek == '2':
    print("Sonuc : " + str(Cıkart(sayi1, sayi2)))
if secenek == '3':
    print("Carpim : " + str(Carp(sayi1, sayi2)))

if secenek == '4':
    print("Bolme : " + str(Bol(sayi1, sayi2)))    