"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discrod: Lenkaa2
"""

import csv
import sys
import requests
from bs4 import BeautifulSoup

registrovani_volici = []
volebni_ucast = []
platne_hlasy = []

def get_html(link):
    obsah = requests.get(link)
    soup = BeautifulSoup(obsah.text, "html.parser")
    print(f"Stahuji data z: {link}")
    return soup

if len(sys.argv) == 3:
    html = get_html(sys.argv[1])
else:
    print("Zadán nesprávný počet argumentů. Argumenty musí být tři. "
          "1. Název souboru, 2. URL adresa v uvozovkách, 3. Libovolný název výstupního .csv souboru.")
    quit()

def seznam_mest() -> list:
    mesta = []
    hledani_mest = html.find_all("td", "overflow_name")
    for mesto in hledani_mest:
        mesta.append(mesto.text)
    return mesta

def url_adresy() -> list:
    cesta = []
    hledani_linku = html.find_all("td", "cislo", "href")
    for link_mesto in hledani_linku:
        link_mesto = link_mesto.a["href"]
        cesta.append(f"https://volby.cz/pls/ps2017nss/{link_mesto}")
    return cesta

def id_mest() -> list:
    mesto_id = []
    hledani_id = html.find_all("td", "cislo")
    for id in hledani_id:
        mesto_id.append(id.text)
    return mesto_id

def kandidujici_strany() -> list:
    strany_kand = []
    mesto_link = url_adresy()
    html_adresa = requests.get(mesto_link[0])
    html_obce = BeautifulSoup(html_adresa.text, "html.parser")
    strany = html_obce.find_all("td", "overflow_name")
    for strana in strany:
        strany_kand.append(strana.text)
    return strany_kand

def volici_ucast_hlasy() -> None:
    """Funkce přidává do proměnných volici, volebni_ucast, platne_hlasy celkový počet
    registrovaných voličů, volební účasti a platných hlasů za jednotlivé obce"""
    cesta = url_adresy()
    for c in cesta:
        cesta_html = requests.get(c)
        obec_html = BeautifulSoup(cesta_html.text, "html.parser")
        volici = obec_html.find_all("td", headers="sa2")
        for volic in volici:
            volic = volic.text
            registrovani_volici.append(volic.replace('\xa0', ' '))
        ucast = obec_html.find_all("td", headers="sa3")
        for cast in ucast:
            cast = cast.text
            volebni_ucast.append(cast.replace('\xa0', ' '))
        hlasy = obec_html.find_all("td", headers="sa6")
        for hlas in hlasy:
            hlas = hlas.text
            platne_hlasy.append(hlas.replace('\xa0', ' '))
    
def vysledky_stran() -> list:
    adresy = url_adresy()
    pocet_hlasu = []
    for adresa in adresy:
        html_adresa = get_html(adresa)
        vyhledavani_hlasu = html_adresa.find_all("td", "cislo", headers=["t1sb4", "t2sb4"])
        docasny = []
        for v in vyhledavani_hlasu:
            docasny.append(v.text + ' %')
        pocet_hlasu.append(docasny)
    return pocet_hlasu

def tvorba_csv() -> list:
    radky = []
    volici_ucast_hlasy()
    mesta = seznam_mest()
    hledani_id = id_mest()
    pocet_hlasu = vysledky_stran()
    zipped = zip(hledani_id, mesta, registrovani_volici, volebni_ucast, platne_hlasy)
    volby_list = []
    for h, m, r, v, p in zipped:
        volby_list.append([h, m, r, v, p])
    zip_all = zip(volby_list, pocet_hlasu)
    for vl, ph in zip_all:
        radky.append(vl + ph)
    return radky

def volby2017(web_adresa, soubor) -> None:
    try:
        hlavicka = ['Kód obce', 'Název obce', 'Registrovaní voliči', 'Vydané obálky', 'Platné hlasy']
        obsah = tvorba_csv()
        strany_kand = kandidujici_strany()
        print("UKLÁDÁM DATA DO SOUBORU:", soubor)
        for strana in strany_kand:
            hlavicka.append(strana)
        with open(soubor, 'w', newline='') as f:
            f_writer = csv.writer(f)
            f_writer.writerow(hlavicka)
            f_writer.writerows(obsah)
        print("UKONČUJI:", sys.argv[0])
    except IndexError:
        print("Nastala chyba. Nejspíš máte špatný odkaz nebo jste jej zapomněli dát do uvozovek.")
        quit()

if __name__ == '__main__':
    address = sys.argv[1]
    file_name = sys.argv[2]
    volby2017(address, file_name)