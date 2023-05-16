## Testausdokumentti
Testattu on Monster, Player ja DatabaseHandler luokan toiminnallisuutta. Monster ja
Player testeissä on käytetty myös PlayZone luokkaa.

### Pelin logiikan varmistaminen
Monster- luokka testaa voiko se saavuttaa pelaajat jahtaamalla heitä ja Player- luokka
testaa voiko pelaaja 1 kulkea vasemman seinän lävitse.

### Tietokannan testaus
Tietokanta asettaa juurihakemiston "data" kansioon "test.db" tiedoston, jos sitä
ei siellä vielä ole. Tietokannan "scores" taulu tyhjennetään ja testataan seuraavat asiat:

- Onhan taulu tyhjä aluksi?
- Jos taulu sisältää yhden pistetuloksen, palauttaako oikein?
- Jos on monta eriarvoista tulosta, antaako suurimman?
- Jos on monta samanarvoista tulosta, antaako ensimmäiseksi saadun?
- Jos joukkueen nimet ovat outoja, laskeeko tietokanta kumminkin oikein?

### coverage-report
<img width="752" alt="Screenshot 2023-05-16 at 12 32 26" src="https://github.com/Yytsi/ot-harjoitustyo/assets/20990023/47aca1de-1fbb-4c57-893b-a025c7cf3860">
