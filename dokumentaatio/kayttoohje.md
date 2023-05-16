## Käyttöohje

Lataa projektin viimeisimmän [releasen](https://github.com/Yytsi/ot-harjoitustyo/releases/tag/palautus) koodi valitsemalla Source code.

Projekti vaatii vähintään Python version 3.8 (joka on ilmaistu poetry- riippuvuuslistassa).

## Käynnistäminen
Aluksi asenna riippuvuudet:
```
poetry install
```

Pelin voi nyt käynnistää näin:
```
poetry run invoke start
```

Testit suoritetaan näin:
```
poetry run invoke test
```

Pylint tarkistukset voi suorittaa näin:
```
poetry run invoke lint
```

## Pelaus
Vasen pelaaja ohjaa hahmoa näppäimillä WASD ja oikea pelaaja nuolinäppäimillä. Kentän ulkopuolelle ei voi liikkua eikä keskirajaa voi ylittää. Kolikon haettua hirviö vaihtaa jahtaamaansa pelaajaa. Hirviön osuttua pelaajaan peli päättyy.

## Muut toiminnot
Testikattavuusraportti muodostuu näin:
```
poetry run invoke coverage-report
```
Muodostetun index.html tiedoston löytää htmlcov hakemistosta.


Koodin tarkistukset voi suorittaa näin:
```
poetry run invoke lint
```
