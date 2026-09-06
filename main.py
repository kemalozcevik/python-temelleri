while True:
    secim = input("\nHesaplama yapmak için Enter'a basın (Çıkmak için 'q'): ")
    if secim == 'q':
        print("Programdan çıkılıyor. Sağlıklı günler!")
        break

    kilo = float(input("Kilonuzu giriniz (kg): "))
    boy = float(input("Boyunuzu metre cinsinden giriniz (orn: 1.75): "))

    vki = kilo / (boy ** 2)
    print("Vücut Kitle İndeksiniz:", round(vki, 2))

    if vki < 18.5:
        print("Durum: Zayıf")
    elif vki < 25:
        print("Durum: Normal kilolu")
    elif vki < 30:
        print("Durum: Fazla kilolu")
    else:
        print("Durum: Obez")