import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_oikeat_kassapaate_maarat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullinen_toimii_kateisella_riittava(self):
        return_money = self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+240)
        self.assertEqual(return_money, 1000-240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_toimii_kateisella_riittamaton(self):
        return_money = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(return_money, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_toimii_kateisella_riittava(self):
        return_money = self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+400)
        self.assertEqual(return_money, 1000-400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_toimii_kateisella_riittamaton(self):
        return_money = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(return_money, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_toimii_kortilla_riittava(self):
        maksukortti = Maksukortti(250)
        ret = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(ret, True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(maksukortti.saldo, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_toimii_kortilla_riittamaton(self):
        maksukortti = Maksukortti(200)
        ret = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(ret, False)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_toimii_kortilla_riittava(self):
        maksukortti = Maksukortti(400)
        ret = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(ret, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_toimii_kortilla_riittamaton(self):
        maksukortti = Maksukortti(200)
        ret = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(ret, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_lataa_rahaa_kortille_positiivinen_summa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+1000)
        self.assertEqual(maksukortti.saldo, 2000)
    
    def test_lataa_rahaa_kortille_negatiivinen_summa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(maksukortti.saldo, 1000)