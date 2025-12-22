# ShopUtils - modul - dostupan za upotrebu u celoj aplikaciji

Ovaj modul sadrzi:

- Klasu ShopUtils, koja u sebi ima metode za:
    - konverziju **RSD -> EUR**
    - konverziju **EUR -> RSD**
    - racunanje **cene sa porezom**

Primeri upotrebe:

```python
print(ShopUtils.rsd_to_eur(1170)) # 10.00
```

## Pravila i formule:
RSD -> EUR
Formula:

- EUR = RSD / EUR_TO_RSD
    - Primer: 1170 / 117 = 10.00

EUR -> RSD

Formula:

- RSD = EUR * EUR_TO_RSD
    - Primer: 10 * 117 = 1170.00 

## Pravila upotrebe - API
ShopUtils.rsd_to_eur(rsd)

- Ulaz mora biti > 0
- Rezultat je zaokruzen na dve decimale

ShopUtils.eur_to_rsd(eur)

- Ulaz mora biti > 0
- Rezultat je zaokruzen na dve decimale

ShopUtils.price_with_tax(price)

- Ulaz mora biti > 0
- Rezultat je zaokruzen na dve decimale

Kurs je preuzet sa:
[NBS](https://www.nbs.rs/sr_RS/indeks/)