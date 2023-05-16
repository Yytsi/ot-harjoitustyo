# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus toteuttaa pelin, jossa kaksi henkilöä (tai miksei yksikin) liikuttavat hahmoja
toisilla puolilla 2D ruutua yrittäen väistää hirviötä hakemalla kolikon. Hirviö liikkuu aina pelaajaa kohti, jonka
puolella hakematon kolikko sijaitsee. Kolikon kerättyään hirvio alkaa seuraamaan toista
pelaajaa, jonka puolelle uusi kolikko myös ilmestyy.

## Toteutetut toiminnallisuudet
- Molemmat pelaajat voivat samanaikaisesti liikkua näppäimillä.
- Uusi kolikko ilmestyy aina satunnaiseen kohtaan kentässä.
- Hirviö jahtaa aina jompaakumpaa pelaajaa ja peli loppuu kun hirviö osuu
toiseen pelaajista.
- Käyttöliittymä, johon voi laittaa pelaajien nimet ja aloittaa pelin.
- Tietokanta, johon pelaajien tulokset tallennetaan.
- Tulostaulukon näyttäminen (näyttää nykyisen ja parhaimman tuloksen).

## Jatkokehitysideoita
- Pelin parametrien (pelaajien/hirviön nopeus, kolikkojen määrä jne) säätömahdollisuus.
