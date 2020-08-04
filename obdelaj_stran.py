import re
import orodja


vrstica = re.compile(
    r'<td>(?P<drzava>.*?)\s*</td>\s*'
    r'<td>(?P<valuta>.*?)\s*</td>\s*'
    r'<td>(?P<okrajsava>.*?)</td>\s*'
    r'<td>(?P<sifra>.*?)</td>\s*'
    r'<td>(?P<tecaj>.*?)</td>'
)


def podatki_v_vrstici(vrst): 
    '''Funkcija iz podatkov v vrsticah naredi slovar glede na dana gesla.'''
    seznam_gesel = ['drzava', 'valuta', 'okrajsava', 'sifra', 'tecaj']
    nova_vrstica = vrstica.search(vrst).groupdict()
    for geslo in seznam_gesel:
        nova_vrstica[geslo] = nova_vrstica[geslo]
    nova_vrstica['tecaj']=float(nova_vrstica['tecaj'].replace(',','.'))
    return nova_vrstica


def vrstice_na_spletni_strani(ime_datoteke):
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for row in vrstica.finditer(vsebina):
        yield podatki_v_vrstici(row.group(0))

def nalozi_strani():
    url = ('https://www.bsi.si/statistika/devizni-tecaji-in-plemenite-kovine/dnevna-tecajnica-referencni-tecaji-ecb')
    ime_datoteke = (f'/Users/nik/Desktop/UVP-projekt/Zajem podatkov/zajeta_stran.html')
    orodja.shrani_spletno_stran(url, ime_datoteke, vsili_prenos=False)

spl_str = ('/Users/nik/Desktop/UVP-projekt/Zajem podatkov/zajeta_stran.html')


vse_vrstice = []
def zdruzi_vrstice():
    for vrstica in vrstice_na_spletni_strani(spl_str):
        vse_vrstice.append(vrstica)


def ustvari_json():
    orodja.zapisi_json(vse_vrstice, "/Users/nik/Desktop/UVP-projekt/Zajem podatkov/zajeta_stran.json")

imena_polj = ['drzava', 'valuta', 'okrajsava', 'sifra', 'tecaj']

def ustvari_csv():
    orodja.zapisi_csv(vse_vrstice, imena_polj, "/Users/nik/Desktop/UVP-projekt/Zajem podatkov/zajeta_stran.csv")


nalozi_strani()
zdruzi_vrstice()
ustvari_json()
ustvari_csv()
