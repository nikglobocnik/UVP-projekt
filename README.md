# Pretvornik valut

### Projektna naloga pri Uvodu v programiranje

## Osnovno o nalogi

Za končni projekt pri predmetu *Uvod v programiranje* sem se ogločil napisati preprost pretvornik valut. Pretvornik uporablja podatke [Banke Slovenije](https://www.bsi.si/statistika/devizni-tecaji-in-plemenite-kovine/dnevna-tecajnica-referencni-tecaji-ecb), ki se posodobijo ob vsakem zagonu pretvornika. Pretvornik prav tako beleži zgodovino pretvorb.

Spletni vmestnik je bil narejen s pomočjo knjižnice [Bottle](https://bottlepy.org/docs/dev/).

Strežnik poženete tako, da poženete datoteko `pretvornik_valut.py`.

## Priprava podatkov

V repozitoriju se v mapi `zajem_podatkov/zajeti_podatki` nahaja JSON datoteka `zajeta_stran.json`. V njej so podatki o valutah in tečajih 32 držav.

Podatke sem pridobil z zajemom. Ustrezne skripte pa se nahajajo v datoteki `obdelaj_stran.py`, ki se nahaja v mapi `zajem_podatkov/orodja_za_zajem` . V pomoč so mi prišle tudi funkcije iz datoteke `orodja.py`, ki smo jih uporabljali pri predmetu *Programiranje 1*.


*Nik Globočnik, avgust 2020*
