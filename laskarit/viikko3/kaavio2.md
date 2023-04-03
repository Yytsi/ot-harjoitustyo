```mermaid
classDiagram
    Peli "1" --> "2..8" Pelaaja
    Peli "1" --> "40" Ruutu
    Peli "1" --> "2" Noppa
    Pelaaja "1" --> "1" Pelinappula
    Pelinappula "*" --> "1" Ruutu
    Ruutu "*" --> "1" Toiminto
    Ruutu "*" --> "1" Kortti
    Talo "*" --> "1" Pelaaja
    Hotelli "*" --> "1" Pelaaja
    Ruutu "1" --> "0..4" Talo
    Ruutu "1" --> "0..1" Hotelli
    Kortti "*" --> "1" Toiminto
    Ruutu "*" --> "1" Pelaaja
    
      class Peli{
        aloitusruutu_id
        vankilaruutu_id
      }
      class Hotelli{
      }
      class Pelaaja{
          id
          rahamäärä
          ruutu_id
          pelinappula_id
      }
      class Pelinappula{
        id
      }
      class Ruutu{
        id
        seuraava_id
        ruudun_tyyppi
        sijainti
        hotelli_id
        rakennukset
        kadun_nimi
        omistaja
      }
      class Talo{
        omistaja_id
      }
      
      class Kortti{
        
      }
      class Noppa{

      }
      class Toiminto{
        laatu
      }```
