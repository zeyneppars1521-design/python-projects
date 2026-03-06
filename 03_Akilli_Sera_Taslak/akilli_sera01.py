# Akıllı Sera Karar Destek Sistemi Taslağı
def sera_kontrol(sicaklik, nem):
    print(f"--- Mevcut Durum: Sıcaklık {sicaklik}°C, Nem %{nem} ---")
    
    # Yapay Zeka Mantığı (Basit Karar Ağacı)
    if sicaklik > 30:
        return "🔥 Durum: Çok sıcak! Havalandırma sistemi açılıyor."
    elif sicaklik < 15:
        return "❄️ Durum: Çok soğuk! Isıtıcılar aktif ediliyor."
    elif nem < 40:
        return "💧 Durum: Toprak kurumuş! Sulama sistemi başlatılıyor."
    else:
        return "✅ Durum: Her şey yolunda. Bitkileriniz güvende."

# Test edelim
print(sera_kontrol(32, 50))