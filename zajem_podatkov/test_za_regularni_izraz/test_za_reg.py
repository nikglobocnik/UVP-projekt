import re
import requests

vzorec = (
    r'<td>(?P<drzava>.*?)</td>\n\s*<td>(?P<valuta>.*?)</td>\n\s*<td>(?P<okrajsava>.*?)</td>\n\s*<td>(?P<sifra>.*?)</td>\n\s*<td>(?P<tecaj>.*?)</td>'
)

zadetki = []
counter = 0

with open(f"/Users/nik/Desktop/UVP-projekt/zajem_podatkov/test_za_regularni_izraz/rocno.html", encoding='utf-8') as file:
    vsebina = file.read()

for zadetek in re.finditer(vzorec, vsebina):
    zadetki.append(zadetek.groupdict())
    counter += 1

print(counter)