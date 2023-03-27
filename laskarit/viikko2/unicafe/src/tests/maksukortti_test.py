import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(150)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.50 euroa")
    
    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")
    
    def test_saldo_ei_muutu_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_rahojen_riittaessa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1000), True)