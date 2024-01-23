"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lenka Pazourová
email: lenka.pazourova@seznam.cz
discrod: Lenkaa2
"""

import csv
import sys
import os
import requests
from bs4 import BeautifulSoup


def pocet_argumentu(argumenty):
    if len(argumenty) not in range(3, 4):
        print('Zadán nesprávný počet argumentů. Argumenty musí být tři.\n'
              '1. Název souboru.py, 2. URL adresa okresu v uvozovkách, 3. Název výstupního .csv souboru v uvozovkách.')
        quit()

def prvni_argument(url_adresa):
    url_okres = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
    html = requests.get(url_okres)
    soup = BeautifulSoup(html.text, 'html.parser')

    def iterace_td_hlavicky():
        data_list = []
        pocet_tabulek = len(soup.find_all('table', {'class': 'table'}))
        for i in range(1, pocet_tabulek + 1):
            data_list.extend(soup.find_all('td', {'headers': f't{i}sa3'}))
        return data_list

    data_tags = iterace_td_hlavicky()
    obce_list = ["https://volby.cz/pls/ps2017nss/" + (data_tag.a['href'])
                 for data_tag in data_tags]
    if url_adresa not in obce_list:
        print('Chybná url adresa okresu.\n'
              'Na stránce https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ\n'
              'klikněte na "X" ve sloupci "Výběr obce" pro Vámi vybraný okres a url adresu zkopírujte.')
        quit()

def obce_soup():
    url = sys.argv[1]
    html_obec = requests.get(url)
    return BeautifulSoup(html_obec.text, 'html.parser')

def csv_nazev():
    okres_nazev = obce_soup().find('div', {'class': 'topline'})
    obec_tag = okres_nazev.find_all('h3')[1]
    obec_raw = obec_tag.text
    okres = obec_raw.strip().lstrip('Okres: ')
    return f"vysledky_{okres}.csv"

def druhy_argument(okres_z_odkazu, nazev_souboru):
    if okres_z_odkazu != nazev_souboru:
        print("Název .csv souboru musí být ve formátu: 'vysledky_<okres>.csv'")
        quit()

def obce():
    div_inner = obce_soup().find('div', {'id': 'inner'})
    radky = div_inner.find_all('tr')
    return radky

def vysledky(radky_tag, mesto_tag):
    link_tag = radky_tag.find('td', {'class': 'cislo'})
    mesto_link = link_tag.a

    def mesto_soup(town_link_tag_2):
        obec_link = town_link_tag_2["href"]
        mesto_url = f'https://volby.cz/pls/ps2017nss/{obec_link}'
        obec_url = requests.get(mesto_url)
        return BeautifulSoup(obec_url.text, 'html.parser')

    def zakladni_udaje(town_tag, mesto_link_tag):
        div_tag = mesto_soup(mesto_link_tag).find('div', {'id': 'publikace'})
        obce_stats = div_tag.table.find_all('td')

        mesto = town_tag.text
        mesto_id = mesto_link_tag.text
        volici = obce_stats[3].text
        obalky = obce_stats[4].text
        platne_hlasy = obce_stats[7].text

        return {'ID': mesto_id, 'Obec': mesto, 'Registrovaní voliči': volici,
                'Vydané obálky': obalky, 'Platné hlasy': platne_hlasy}

    def kand_strany():
        div_inner = mesto_soup(mesto_link).find('div', {'id': 'inner'})
        strany = [tag.text for tag in (div_inner.find_all
                                        ('td', {'class': 'overflow_name'}))]
        hlasy_1 = [tag.text for tag in (div_inner.find_all
                                        ('td', {'headers': 't1sa2 t1sb3'}))]
        hlasy_2 = [tag.text for tag in (div_inner.find_all
                                        ('td', {'headers': 't2sa2 t2sb3'}))]
        hlasy_a_strany = hlasy_1 + hlasy_2
        strany_a_hlasy = {strany[i]: hlasy_a_strany[i]
                             for i in range(len(strany))}
        return strany_a_hlasy

    dict_vysledky = {}
    dict_vysledky.update(zakladni_udaje(mesto_tag, mesto_link))
    dict_vysledky.update(kand_strany())
    return dict_vysledky

def uloz_soubor(vysledky_dict):
    soubor = open(csv_nazev(), mode='a', newline='\n')
    prvni_radek = list(vysledky_dict.keys())
    zapis = csv.DictWriter(soubor, prvni_radek) 
    if os.path.getsize(csv_nazev()) == 0:
        zapis.writeheader()
    else:
        zapis.writerow(vysledky_dict)
    soubor.close()


def stahovani_a_ukladani():
    for i, tr_tag in enumerate(obce()):
        procenta = round((i + 1) * (100 / len(obce())), 1)
        os.system('cls')
        print(f"Stahuji data z: {sys.argv[1]}'\n"
              f"Staženo: {procenta:>5}%")
        town_tag = tr_tag.find('td', {'class': 'overflow_name'})
        if town_tag is None:
            continue
        else:
            uloz_soubor(vysledky(tr_tag, town_tag))

if __name__ == '__main__':
    os.system('cls')
    print('Kontroluji url adresu a název souboru')
    pocet_argumentu(sys.argv)
    prvni_argument(sys.argv[1])
    druhy_argument(sys.argv[2], csv_nazev())

    vytvoreny_soubor = open(csv_nazev(), mode='w')
    vytvoreny_soubor.close()

    os.system('cls')
    print(f'Stahuji data z: {sys.argv[1]}')
    stahovani_a_ukladani()
    print(f'Úspěšně staženo a uloženo v "{csv_nazev()}"\n'
        'Ukončuji election_scraper.py')
