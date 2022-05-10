## Ohjelman toteutus

Ohjelmassa on grafinen käyttöliittymä, josta valitaan, mitä tehdään, ja sitten se linkkaa joko huffmania tai lzw:tä käsittelevään tiedostoon valinnan mukaan. Huffman-pakkaukseen on erillinen tiedosto, joka laskee eri merkkien esiintymistiheydet, luo huffman-puun, laskee siitä merkkikoodit, tekee koodien perusteella binääriesityksen tekstistä ja lopuksi pakkaa sekä koodidictionaryn että binäärin tiedostoon. Lisäksi tiedostonkäsittelysyistä tiedostoon talletetaan tavukoodin offset-arvo, että tiedetään kuinka monta bittiä on täytteenä että ensimmäinen tavu saadaan täyteen, sekä dictionaryn koko, jonka avulla purkamisalgoritmi osaa eritellä dictionaryn itse datasta. Huffmanin purkaminen on todella yksinkertainen operaatio, joka on toteutettu omaan pieneen tiedostoonsa.
Lzw-algoritmi minusta tuntui toisaalta suoraviivaisemmalta, mutta toisaalta sellaiselta, jonka toteutuksen yksityiskohtien ymmärtäminen oli vaikeampaa, joten lzw-tiedostosta tuli sellainen, että sekä pakkaus- että purkamisalgoritmit on siellä omina suoraviivaisina kokonaisuuksinaan.

## Suorituskyky ja vertailu

Molemmat algoritmit saavuttavat lähes saman pakkausasteen, hiukan alle 50 %. Teoriassa lzw on sikäli parempi, että siinä ei tarvitse tiedostoon liittää muuta tietoa kuin itse pakattu data, kun taas huffmanissa täytyy lisäksi olla datan aakkoston koodit myös. Käytännössä kuitenkin missään tiedostossa, joka on niin iso, että sen pakkaamisissa olisi mitään järkeä, akkoston koko on aivan merkityksettömän pieni, ja siksi se, että se liitetään pakkaamattomana tekstinä tiedostoon ei vaikuta suorituskykyyn.

## Lähteet

Wikipedia: [Huffman](https://en.wikipedia.org/wiki/Huffman_coding), [Lempel-Ziv-Welch](https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch)
