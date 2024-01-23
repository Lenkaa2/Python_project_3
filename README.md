# Python_project_3
Engeto Online Python Akademie - Project 3

## Election_scraper.py 
Program extrahuje výsledky voleb do parlamentu České republiky z roku 2017 pro vybraný okres a uloží je do .csv souboru.  
Odkaz: https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ (sloupec Výběr obce).

## Instalace knihoven
Knihovny použité v programu a jejich verze jsou uvedeny v souboru requirements.txt

Program se spouští z příkazového řádku a k jeho spuštění je zapotřebí zadat dva argumenty a to v následujícím pořadí: 
"odkaz okresu, pro který chcete výsledky voleb extrahovat" "název výstupního .csv souboru"

Ukázka běhu programu:
Spuštění programu a extrahování výsledků parlamentních voleb pro okres Pardubice: 
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" "pardubice_volby17.csv"

Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576026&xvyber=5302
Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576042&xvyber=5302
Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576051&xvyber=5302

UKLÁDÁM DATA DO SOUBORU: parbubice_volby17.csv
UKONČUJI: election_scraper.py
