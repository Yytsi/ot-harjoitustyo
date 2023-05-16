# CatchIt peli

Hauska kahden pelaajan joukkuepeli, jossa hirviötä paetaan hakemalla kolikkoa omalta puolelta hirviön edestä.


## Dokumentaatio

[Käyttöohje](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

[Arkkitehtuurikuvaus](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Testausdokumentti](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/testausdoc.md)

## Käynnistäminen

Aluksi asennetaan riippuvuudet: ```poetry install```.

Pelin voi käynnistää näin: ```poetry run invoke start```.

Testit suoritetaan näin: ```poetry run invoke test```.

Pylint tarkistukset voi suorittaa näin: ```poetry run invoke lint```.

## Pelaus
Vasen pelaaja ohjaa hahmoa näppäimillä WASD ja oikea pelaaja nuolinäppäimillä. Kentän ulkopuolelle ei voi liikkua eikä keskirajaa voi ylittää. Kolikon haettua hirviö vaihtaa jahtaamaansa pelaajaa. Hirviön osuttua pelaajaan peli päättyy.

## Julkaisut

[Viikko 5](https://github.com/Yytsi/ot-harjoitustyo/releases/tag/viikko5)
[Viikko 6](https://github.com/Yytsi/ot-harjoitustyo/releases/tag/viikko6)
[loppupalautus](https://github.com/Yytsi/ot-harjoitustyo/releases/tag/loppupalautus)

## Kuvien lisenssi
Pelin käyttämät kuvat ovat sivustolta [itch.io](https://itch.io/), josta on valittu sellaiset kuvat jotka eivät vaatineet mainintaa lisenssistä tai mistään.
