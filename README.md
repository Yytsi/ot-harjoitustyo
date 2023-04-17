# CatchIt peli

(Keskeneräinen) Hauska kahden pelaajan joukkuepeli, jossa hirviötä paetaan hakemalla kolikkoa omalta puolelta hirviön edestä.


## Dokumentaatio

[Vaatimusmäärittely](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Changelog](https://github.com/Yytsi/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Käynnistäminen

Aluksi asennetaan riippuvuudet: ```poetry install```.

Pelin voi käynnistää näin: ```poetry run invoke start```.

Testit suoritetaan näin: ```poetry run invoke test```.

Pylint tarkistukset voi suorittaa näin: ```poetry run invoke lint```.

## Pelaus
Vasen pelaaja ohjaa hahmoa näppäimillä WASD ja oikea pelaaja nuolinäppäimillä. Kentän ulkopuolelle ei voi liikkua eikä keskirajaa voi ylittää.

## Kuvien lisenssi
Pelin käyttämät kuvat ovat sivustolta [itch.io](itch.io), joista osaa voi käyttää mainitsematta mitään.
