# --- Temel Hesap Makinesi Uygulaması ---
print("Hesap Makinesine Hoş Geldiniz!")

try:
    sayi1 = float(input("Birinci sayıyı giriniz: "))
    sayi2 = float(input("İkinci sayıyı giriniz: "))
    islem = input("Yapmak istediğiniz işlemi seçin (+, -, *, /): ")

    if islem == "+":
        print(f"Sonuç: {sayi1 + sayi2}")
    elif islem == "-":
        print(f"Sonuç: {sayi1 - sayi2}")
    elif islem == "*":
        print(f"Sonuç: {sayi1 * sayi2}")
    elif islem == "/":
        if sayi2 != 0:
            print(f"Sonuç: {sayi1 / sayi2}")
        else:
            print("Hata: Bir sayı sıfıra bölünemez!")
    else:
        print("Geçersiz bir işlem girdiniz.")
except ValueError:
    print("Hata: Lütfen sadece sayısal değerler giriniz!")