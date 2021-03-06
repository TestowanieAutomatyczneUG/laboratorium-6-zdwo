import unittest

class Song:
    def text(self, vers):
        lyrics = ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
                  "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",
                  "On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."]

        if type(vers) is int:
            if 0 < vers <= len(lyrics):
                return lyrics[vers-1]
            else:
                raise Exception("Liczba musi byc > 0 i < 13.")
        elif type(vers) is tuple and type(vers[0]) is int and type(vers[1]) and len(vers) == 2:
            if 0 < vers[0] < vers[1] < 13:
                return "\n".join(lyrics[vers[0] - 1:vers[1]])
            else:
                raise Exception("Liczby musza byc > 0. Pierwsza musi byc mniejsza od drugiej.")
        elif vers == "full" or vers == "all":
            return "\n".join(lyrics)
        else:
            raise Exception("Error")


class SongTest(unittest.TestCase):
    def setUp(self):
        self.temp = Song()

    def test_single_vers(self):
        self.assertEqual(self.temp.text(1), "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.")

    def test_tuple_verses(self):
        self.assertEqual(self.temp.text((1,3)), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_full_song(self):
        self.assertEqual(self.temp.text("full"), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_all_song(self):
        self.assertEqual(self.temp.text("all"), """On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.""")

    def test_int_eq_zero(self):
        with self.assertRaises(Exception):
            self.temp.text(0)

    def test_int_lt_zero(self):
        with self.assertRaises(Exception):
            self.temp.text(-5)

    def test_int_gt_twelve(self):
        with self.assertRaises(Exception):
            self.temp.text(13)

    def test_tup_lt_zero(self):
        with self.assertRaises(Exception):
            self.temp.text((-1,3))

    def test_tup_eq_zero(self):
        with self.assertRaises(Exception):
            self.temp.text((0,5))

    def test_tup_empty(self):
        with self.assertRaises(Exception):
            self.temp.text(())

    def test_tup_wrong_order(self):
        with self.assertRaises(Exception):
            self.temp.text((11,2))

    def test_tup_gt_twelve(self):
        with self.assertRaises(Exception):
            self.temp.text((11,13))

    def test_wrong_str(self):
        with self.assertRaises(Exception):
            self.temp.text("text")

    def test_wrong_type_arr(self):
        with self.assertRaises(Exception):
            self.temp.text([])

    def test_tup_wrong_len_long(self):
        with self.assertRaises(Exception):
            self.temp.text((1,2,3))

    def test_wrong_type_float(self):
        with self.assertRaises(Exception):
            self.temp.text(3.5)

    def test_wrong_type_dict(self):
        with self.assertRaises(Exception):
            self.temp.text({})

    def test_wrong_type_none(self):
        with self.assertRaises(Exception):
            self.temp.text()

    def test_wrong_tup_type_str(self):
        with self.assertRaises(Exception):
            self.temp.text(("one", 2))

    def test_wrong_tup_type_fl(self):
        with self.assertRaises(Exception):
            self.temp.text((1, 2.2))

    def test_wrong_tup_type_dict(self):
        with self.assertRaises(Exception):
            self.temp.text(({}, 2))

    def test_wrong_tup_type_arr(self):
        with self.assertRaises(Exception):
            self.temp.text(([], 2))

    def test_wrong_tup_type_none(self):
        with self.assertRaises(Exception):
            self.temp.text((1, None))

    def test_wrong_tup_type_tup(self):
        with self.assertRaises(Exception):
            self.temp.text(((), 2))
