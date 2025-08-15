# Search Tools Collection

Bu koleksiyon çeşitli arama araçlarını içerir.

## Ana Dosyalar

- **`instant_search_main.py`** - Ana arama scripti (`/usr/local/bin/s` kopyası)
  - Terminal'de `s` komutu ile çalışır  
  - 8 farklı site açar: Cisco OneSearch, Circuit, Claude, Google, LinkedIn, GitHub, ChatGPT, Perplexity, Wikipedia
  - Sorguyu clipboard'a kopyalar

- **`instant_search.py`** - Alternatif versiyon

## Kullanım

Terminal'de:
```bash
s "arama terimi"
```

Veya script'i doğrudan çalıştır:
```bash
python3 instant_search_main.py "arama terimi"
```

## Kurulum

Ana script `/usr/local/bin/s` konumunda kurulu ve PATH'te mevcut.

## Not

Eski search ve search2 dizinleri archive'a taşındı. Aktif olan sadece bu search-final dizini.