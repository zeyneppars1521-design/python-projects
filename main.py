# Şifre Doğrulama Projesi
dogru_sifre = "Zeynep123"
hak = 3

while hak > 0:
    giris = input("Şifrenizi girin: ")
    if giris == dogru_sifre:
        print("Giriş başarılı! Sisteme hoş geldin.")
        break
    else:
        hak -= 1
        print(f"Hatalı şifre. Kalan hak: {hak}")

if hak == 0:
    print("Giriş hakkınız doldu.")
