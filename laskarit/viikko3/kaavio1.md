```mermaid
  classDiagram
    Peli "1" --> "2..8" Pelaaja
    Peli "1" --> "40" Ruutu
    Peli "1" --> "2" Noppa
    Pelaaja "1" --> "1" Pelinappula
    Pelinappula "*" --> "1" Ruutu
      class Peli{
        
      }
      class Pelaaja{
          id
          ruutu_id
          pelinappula_id
      }
      class Pelinappula{
        id
      }
      class Ruutu{
        id
        next_id
      }
      class Noppa{

      }
 ```
