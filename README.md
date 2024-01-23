# Python_project_3
Engeto Online Python Akademie - Project 3

## Election_scraper.py 
Program extrahuje výsledky voleb do parlamentu České republiky z roku 2017 do .csv souboru.

## Instalace knihoven
Pro správný běh programu election_scraper.py je třeba před jeho spuštěním nainstalovat potřebné knihovny (viz requirements.txt).  
Doporučujeme knihovny instalovat do nového virtuálního prostředí pro tento program.  
>
Do příkazového řádku stačí zadat následující příkazy:
>`$ pip3 --version`  
`$ pip3 install -r requirements.txt`

## Spuštění programu
Program se spouští z příkazového řádku a k jeho spuštění jsou zapotřebí dva argumenty:  
1. argument - URL adresa okresu, pro který chcete výsledky voleb extrahovat  uvozovkách
2. argument - název výstupního .csv souboru ve formátu "vysledky_<okres>.csv"
>
__Ukázka spuštění programu pro okres Pardubice:__
1. argument: "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302"
2. argument: "vysledky_Pardubice.csv"
>
_Příkazový řádek:_
>`$ python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" "vysledky_Pardubice.csv"`

Ukázka běhu programu:
Spuštění programu a extrahování výsledků parlamentních voleb pro okres Pardubice: 
python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302" "pardubice_volby17.csv"

Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576026&xvyber=5302
Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576042&xvyber=5302
Stahuji data z: https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=9&xobec=576051&xvyber=5302

UKLÁDÁM DATA DO SOUBORU: parbubice_volby17.csv
UKONČUJI: election_scraper.py
