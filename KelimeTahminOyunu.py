"""  Öğrenci No: 22100011074
     Ad-Soyad: Sude Özsoy    """

import random

kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case",
                  "program", "information", "set", "code", "function", "process", "application", "software",
                  "class", "point", "type", "network", "tree", "object", "element", "input", "operation", "level",
                  "memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
                  "compute", "sequence", "computer", "bit", "probability", "machine", "array", "page", "error",
                  "step", "search", "most", "path", "graph", "web", "length", "several", "security", "proof",
                  "access", "obtain", "matrix", "task", "image", "form", "return", "interface", "resource",
                  "address", "implementation", "loop", "first", "read", "location", "hardware", "behavior",
                  "programming", "field", "key", "parameter", "distribution", "definition", "instance",
                  "interaction", "internet", "representation", "edge", "stack", "return", "procedure",
                  "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                  "detection", "write", "execute", "least", "key"]

toplam_puan = 0                                          # Her yeni kelimede tüm oyunların toplam puanı
while True:
    print('------------------------------------')
    print("Kelime Tahmin Oyunu")
    print("1. Basla, yeni kelime                 Toplam Puanınız: {}\n"
          "2. Sonlandır ".format(toplam_puan))
    secim = int(input(">>"))

    if secim == 1:
        kelime = random.choice(kelime_listesi)            # Listedeki kelimelerden rastgele kelime seçer.
        uzunluk = len(kelime)
        print('Tahmin edilecek kelimenin uzunluğu: {} harf'.format(uzunluk))

        sesli = 'aeıioöuü'                               # puanlamada kullanmak için sesli, sessiz harfler
        sessiz = 'bcçdfgğhjklmnprsştvyzwq'
        turkce = 'çğşıİöü'                               # türkçe karakter kontrolü için
        yazdir = '_' * uzunluk                           # tahminler bunun üzerinden olacak.
        puan = 0                                         # tahmin edilecek kelime için puanlama
        tum_tahminler = ' '                              # daha önce kullandığı harfi kullanmaması için kaydedilir

        if uzunluk % 2 == 1:                             # kelime tekse hak sayisinın kelimenin yarisinin bir üst tam
            hak = uzunluk / 2 + 0.5                      # sayiya yuvarlanması için.
        else:
            hak = uzunluk / 2
        print('Toplam tahmin hakkınız: {}\n'.format(int(hak)))

        while hak != 0:
            while True:
                print('------------------------------------')
                print('Güncel puan: {}  Güncel hak: {}'.format(puan, int(hak)))
                print("Kelime: '{}'".format(yazdir))
                tahmin = input('Harf giriniz >> ').lower()
                if tahmin in tum_tahminler:              # Daha önce harfin kullanılıp kullanılmadığına bakar.
                    print('Daha önce {} harfini kullandınız. Farklı harf tuşlayınız.\n'.format(tahmin))
                    continue
                elif tahmin in turkce:                   # Turkçe karakter olup olmadığına bakar.
                    print('Türkçe karakter kullandınız. Farklı harf tuşlayınız.\n')
                    continue
                elif len(tahmin) > 1:                    # Birden fazla harf girilip girilmediğine bakar.
                    print('Sadece bir harf kullanmalısınız. Tekrar deneyin.\n')
                    continue
                else:
                    break
            tum_tahminler += tahmin                      # Kullanılan harfi kaydeder.

            sira = 0                                     # kelimenin tahmin edilen harfinin sirasini kontrol eder
            kontrol = 0                                  # tahminin doğru veya yanlışlığını kontrol etmek için
            for i in kelime:                             # kelimedeki harfleri dolaşacak
                if i == tahmin:                          # tahmin edilen harf dogruysa şart sağlanacak
                    kontrol = 1
                    yazdir = yazdir[:sira] + i + yazdir[sira + 1:uzunluk]  # dogru tahmin gösterilip gerisi '_' kalacak.
                    if tahmin in sesli:                  # sesli ve sessiz harflerdeki puanlandırma farkı için
                        puan += 3
                    else:
                        puan += 2
                sira += 1                                # kelimenin bi sonraki sirasina geçişini sağlar

            if kontrol == 1:
                print('Doğru tahmin yaptınız.\n')
            else:
                hak -= 1
                puan -= 4
                print('Yanlış tahmin yaptınız.\n')

            if hak == 0:                                 # hak kalmadıysa menüye yönlendirir.
                print('------------------------------------')
                print('Tahmin hakkınız bitti! Kelime: {}\nAldığınız puan: {}\n'.format(kelime, puan))
                toplam_puan += puan                      # her oyun sonu kelimeden aldığı puanı toplama ekler.
                break

            if yazdir == kelime:                         # kelimenin doğru tahmin edildiğini gösterir.
                print('Tebrikler! Kelimeyi doğru tahmin ettiniz. ')
                print('Kelime: {}\nAldığınız puan: {}\n'.format(kelime, puan))
                toplam_puan += puan
                break

    if secim == 2:                                       # oyunu sonlandırır.
        break
