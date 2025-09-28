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

