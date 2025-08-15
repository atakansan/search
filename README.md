# Search Tools Collection

Bu koleksiyon çeşitli arama araçlarını içerir.

## Ana Dosyalar

- **`instant_search_main.py`** - Ana arama scripti (`/usr/local/bin/s` kopyası)
  - Terminal'de `s` komutu ile çalışır  
  - 9 farklı site açar (sıralama):
    1. OneSearch (Cisco)
    2. Circuit (Cisco)
    3. Perplexity AI
    4. Google
    5. Claude AI
    6. ChatGPT
    7. GitHub
    8. Wikipedia
    9. LinkedIn
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

## Kurulum (Paket olarak)

### PyPI'dan kurulum (yakında)
```bash
pip install instant-search
```

### GitHub'dan kurulum
```bash
pip install git+https://github.com/atakansan/search.git
```

### Platform notları
- **macOS**: Tam destek, clipboard otomatik çalışır
- **Windows**: Tam destek, clipboard otomatik çalışır  
- **Linux**: Clipboard için `xclip` veya `xsel` gerekli:
  ```bash
  # Ubuntu/Debian
  sudo apt install xclip
  # veya
  sudo apt install xsel
  
  # Fedora/RHEL
  sudo dnf install xclip
  ```

### Manuel kurulum
```bash
git clone https://github.com/atakansan/search.git
cd search
pip install -e .
```

Kurulumdan sonra şu komutlarla kullanabilirsin:
```bash
instant-search "arama terimi"
isearch "arama terimi"  
s "arama terimi"
```

## Geliştirme

```bash
git clone https://github.com/atakansan/search.git
cd search
pip install -e .
```

## Not

Eski search ve search2 dizinleri archive'a taşındı. Aktif olan sadece bu search-final dizini.