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

## Ukázka běhu programu 
Kontroluji url adresu a název souboru  
Stahuji data z: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=9&xnumnuts=5302  
Staženo: 5,6%

Úspěšně staženo a uloženo v "vysledky_Pardubice.csv"  
Ukončuji election_scraper.py

## Ukázka výstupu  
ID,Obec,Registrovaní voliči,Vydané obálky,Platné hlasy,Občanská demokratická strana,Řád národa - Vlastenecká unie,CESTA ODPOVĚDNÉ SPOLEČNOSTI,Česká str.sociálně demokrat.,Radostné Česko,STAROSTOVÉ A NEZÁVISLÍ,Komunistická str.Čech a Moravy,Strana zelených,"ROZUMNÍ-stop migraci,diktát.EU",Strana svobodných občanů,Blok proti islam.-Obran.domova,Občanská demokratická aliance,Česká pirátská strana,Referendum o Evropské unii,TOP 09,ANO 2011,Dobrá volba 2016,SPR-Republ.str.Čsl. M.Sládka,Křesť.demokr.unie-Čs.str.lid.,REALISTÉ,SPORTOVCI,Dělnic.str.sociální spravedl.,Svob.a př.dem.-T.Okamura (SPD),Strana Práv Občanů
574741,Bezděkov,262,164,163,18,0,0,5,0,14,9,7,1,2,0,0,20,0,7,58,0,1,3,4,2,0,11,1
574783,Borek,226,161,159,30,0,1,12,1,12,9,2,1,3,2,0,11,0,6,34,0,0,8,1,0,1,25,0
574791,Brloh,193,149,149,8,0,0,10,0,17,11,0,4,1,0,0,17,0,5,43,0,0,9,1,1,0,19,3
574805,Břehy,833,576,573,65,1,0,43,0,30,66,9,4,0,0,0,58,0,18,198,0,2,17,4,0,2,53,3
574813,Bukovina nad Labem,187,139,138,23,1,0,6,0,6,15,0,1,1,0,0,9,0,5,49,0,0,16,0,0,0,6,0
574821,Bukovina u Přelouče,69,51,50,4,0,0,6,0,4,3,1,3,0,0,0,0,0,0,17,0,0,1,0,0,0,10,1




