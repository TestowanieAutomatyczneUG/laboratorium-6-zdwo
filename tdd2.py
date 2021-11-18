import unittest

def roman(x):
    if x < 4:
        result = "I"*x
    return result

class RomanNumeralsTest(unittest.TestCase):

    def test_1_is_a_single_i(self):
        self.assertEqual(roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(roman(3), "III")

    @unittest.skip("nd")
    def test_4_being_5_1_is_iv(self):
        self.assertEqual(roman(4), "IV")

    @unittest.skip("nd")
    def test_5_is_a_single_v(self):
        self.assertEqual(roman(5), "V")

    @unittest.skip("nd")
    def test_6_being_5_1_is_vi(self):
        self.assertEqual(roman(6), "VI")

    @unittest.skip("nd")
    def test_9_being_10_1_is_ix(self):
        self.assertEqual(roman(9), "IX")

    @unittest.skip("nd")
    def test_20_is_two_x_s(self):
        self.assertEqual(roman(27), "XXVII")

    @unittest.skip("nd")
    def test_48_is_not_50_2_but_rather_40_8(self):
        self.assertEqual(roman(48), "XLVIII")

    @unittest.skip("nd")
    def test_49_is_not_40_5_4_but_rather_50_10_10_1(self):
        self.assertEqual(roman(49), "XLIX")

    @unittest.skip("nd")
    def test_50_is_a_single_l(self):
        self.assertEqual(roman(59), "LIX")

    @unittest.skip("nd")
    def test_90_being_100_10_is_xc(self):
        self.assertEqual(roman(93), "XCIII")

    @unittest.skip("nd")
    def test_100_is_a_single_c(self):
        self.assertEqual(roman(141), "CXLI")

    @unittest.skip("nd")
    def test_60_being_50_10_is_lx(self):
        self.assertEqual(roman(163), "CLXIII")

    @unittest.skip("nd")
    def test_400_being_500_100_is_cd(self):
        self.assertEqual(roman(402), "CDII")

    @unittest.skip("nd")
    def test_500_is_a_single_d(self):
        self.assertEqual(roman(575), "DLXXV")

    @unittest.skip("nd")
    def test_900_being_1000_100_is_cm(self):
        self.assertEqual(roman(911), "CMXI")

    @unittest.skip("nd")
    def test_1000_is_a_single_m(self):
        self.assertEqual(roman(1024), "MXXIV")

    @unittest.skip("nd")
    def test_3000_is_three_m_s(self):
        self.assertEqual(roman(3000), "MMM")