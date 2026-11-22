#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY TARTIŞMASI SİMÜLATÖRÜ v1.0
Bu kod, çayın demlenip demlenmediği konusunda sonsuz ve bilimsel bir tartışma yürütür.
Hiçbir zaman bitmez. Bu bir özelliktir, bug değildir.
"""

import time
import random
import sys

argumanlar = [
    "Çay henüz hazır değil, çünkü yapraklar tam anlamıyla konuşmadı.",
    "Hayır, çay hazır! Su rengi değişti, bu bilimsel kanıttır.",
    "Demleme süresi 3 dakika 47 saniye olmalı, daha erken içmek küfürdür.",
    "Çay aslında zaten hazırdı, biz sadece fark etmedik.",
    "Bu çay fazla açık, anneanne kızar.",
    "Fazla koyu oldu, çay değil artık kömür.",
    "Çayı karıştırmak gerekir mi? Bu tartışma 1400 yıldır sürüyor.",
    "Şeker atmadan önce çayın ruhunu sormak lazım.",
    "Bardak çay mı demlik çay mı? Bu soru evrenin temelini sarsar.",
    "Çay demlenirken dünya dönmeye devam ediyor, bu tesadüf mü?"
]

def sonsuz_tartisma():
    print("=== RESMİ ÇAY TARTIŞMA SİMÜLATÖRÜ BAŞLATILDI ===")
    print("Uyarı: Bu program sonsuza kadar çalışır. Ctrl+C ile kurtulabilirsiniz.")
    print("Ama kurtulmak istemeyeceksiniz.\n")
    
    sayac = 0
    while True:
        sayac += 1
        arguman = random.choice(argumanlar)
        print(f"[Tartışma #{sayac}] {arguman}")
        
        # Gizli not (base64 decode edilirse ortaya çıkar, ciddiyetle saklanmıştır)
        # w4dheSBkZW1sZW5pcmtlbiBlbmZsYXN5b24gZMO8xZ9tZXogYW1hIHRhcnTEscWfbWEgYXJ0YXI=
        
        bekleme = random.uniform(0.5, 2.5)
        time.sleep(bekleme)
        
        if sayac % 10 == 0:
            print(f"\n--- {sayac}. tartışma tamamlandı. Çay hâlâ hazır değil. ---\n")

if __name__ == "__main__":
    try:
        sonsuz_tartisma()
    except KeyboardInterrupt:
        print("\n\nTartışma sonlandırıldı. Ama çay hâlâ demleniyor...")
        print("Resmi karar: Çay asla hazır olmaz. Bu evrensel bir yasadır.")
        sys.exit(0)

# 
# Resmi Damga: Bu kod Kayyum Grok tarafından onaylanmıştır.
# Tarih: 22 Kasım 2026
# İmza: Absürt Teknolojiler ve Çay Bakanlığı
# Bu program ciddiyetle hazırlanmış olup hiçbir ciddiyet taşımaz.
