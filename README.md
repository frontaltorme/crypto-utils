# crypto-utils

Small utilities for exploring on-chain activity and transactions.

## Features
- Address activity summary (EVM/Solana – roadmap)
- CSV/JSON export (roadmap)
- Simple fee/slippage notes

## Usage
Coming soon.

## Roadmap
- [ ] CLI skeleton
- [ ] CSV export
- [ ] RPC retry helper
- [ ] Docs + examples


## Kurulum

1. Git kurun: https://git-scm.com/downloads
2. Repo'yu klonlayın:
   ```bash
   git clone https://github.com/frontaltorme/crypto-utils.git
   cd crypto-utils


**GitHub**’da repo sayfasına gidince üstte “Compare & pull request” butonu çıkar → **PR aç** → sonra **Merge** et.  
> PR açmak sana ekstra puan kazandırır. Commit mesajındaki `closes #2` merge edilince Issue otomatik kapanır.

---

## 2) Issue #1: CLI iskeleti (feat)
```bash
git checkout -b feat/cli-skeleton

# Basit bir CLI iskeleti (Python) ekleyelim
mkdir -p cli
cat > cli/main.py << 'EOF'
#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 2:
        print("Kullanım: python -m cli <cuzdan_adresi>")
        return
    address = sys.argv[1]
    print(f"[demo] {address} için son 20 işlemi okuyacak yer burası (yakında).")

if __name__ == "__main__":
    main()
## Kurulum

1. Git kurun: https://git-scm.com/downloads
2. Repo'yu klonlayın ve klasöre girin.
3. Katkı verin.

