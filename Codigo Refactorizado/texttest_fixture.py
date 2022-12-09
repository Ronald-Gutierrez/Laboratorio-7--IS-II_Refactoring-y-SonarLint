# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    # items predeterminados
    def test_default(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Empire of Jigglypuff", sell_in=1, quality=3),
            Item(name="Charmander 007", sell_in=1, quality=48)
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Dia 1
        self.assertEqual(9, gilded_rose.items[0].sell_in)
        self.assertEqual(19, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(6, gilded_rose.items[1].quality)
        self.assertEqual(0, gilded_rose.items[2].sell_in)
        self.assertEqual(2, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].sell_in)
        self.assertEqual(47, gilded_rose.items[3].quality)

        gilded_rose.update_quality()  # Dia 2
        self.assertEqual(8, gilded_rose.items[0].sell_in)
        self.assertEqual(18, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(5, gilded_rose.items[1].quality)
        self.assertEqual(-1, gilded_rose.items[2].sell_in)
        self.assertEqual(0, gilded_rose.items[2].quality)
        self.assertEqual(-1, gilded_rose.items[3].sell_in)
        self.assertEqual(45, gilded_rose.items[3].quality)

        gilded_rose.update_quality()  # Dia 3
        self.assertEqual(7, gilded_rose.items[0].sell_in)
        self.assertEqual(17, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(4, gilded_rose.items[1].quality)
        self.assertEqual(-2, gilded_rose.items[2].sell_in)
        self.assertEqual(0, gilded_rose.items[2].quality)
        self.assertEqual(-2, gilded_rose.items[3].sell_in)
        self.assertEqual(43, gilded_rose.items[3].quality)

    # Aged Brie
    def test_aged_brie(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Aged Brie", sell_in=5, quality=48),
            Item(name="Aged Brie", sell_in=-2, quality=46),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Dia 1
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(4, gilded_rose.items[1].sell_in)
        self.assertEqual(49, gilded_rose.items[1].quality)
        self.assertEqual(-3, gilded_rose.items[2].sell_in)
        self.assertEqual(48, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Dia 2
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(2, gilded_rose.items[0].quality)
        self.assertEqual(3, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-4, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Dia 3
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(4, gilded_rose.items[0].quality)
        self.assertEqual(2, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-5, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

        gilded_rose.update_quality()  # Dia 4
        self.assertEqual(-2, gilded_rose.items[0].sell_in)
        self.assertEqual(6, gilded_rose.items[0].quality)
        self.assertEqual(1, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(-6, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)

    # Legendary item - Sulfuras
    def test_sulfuras(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Dia 1
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(80, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Dia 2
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(80, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(80, gilded_rose.items[1].quality)

    # Backstage passes
    def test_backstage_passes(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=6, quality=42),
            Item(name="Backstage passes to a TAFKAL80ETC concert",
                 sell_in=2, quality=32),
        ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Dia 1
        self.assertEqual(14, gilded_rose.items[0].sell_in)
        self.assertEqual(21, gilded_rose.items[0].quality)
        self.assertEqual(9, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(5, gilded_rose.items[2].sell_in)
        self.assertEqual(44, gilded_rose.items[2].quality)
        self.assertEqual(1, gilded_rose.items[3].sell_in)
        self.assertEqual(35, gilded_rose.items[3].quality)

        gilded_rose.update_quality()  # Dia 2
        self.assertEqual(13, gilded_rose.items[0].sell_in)
        self.assertEqual(22, gilded_rose.items[0].quality)
        self.assertEqual(8, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(4, gilded_rose.items[2].sell_in)
        self.assertEqual(47, gilded_rose.items[2].quality)
        self.assertEqual(0, gilded_rose.items[3].sell_in)
        self.assertEqual(38, gilded_rose.items[3].quality)

        gilded_rose.update_quality()  # Dia 3
        self.assertEqual(12, gilded_rose.items[0].sell_in)
        self.assertEqual(23, gilded_rose.items[0].quality)
        self.assertEqual(7, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(3, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        self.assertEqual(-1, gilded_rose.items[3].sell_in)
        self.assertEqual(0, gilded_rose.items[3].quality)

        gilded_rose.update_quality()  # Dia 4
        self.assertEqual(11, gilded_rose.items[0].sell_in)
        self.assertEqual(24, gilded_rose.items[0].quality)
        self.assertEqual(6, gilded_rose.items[1].sell_in)
        self.assertEqual(50, gilded_rose.items[1].quality)
        self.assertEqual(2, gilded_rose.items[2].sell_in)
        self.assertEqual(50, gilded_rose.items[2].quality)
        self.assertEqual(-2, gilded_rose.items[3].sell_in)
        self.assertEqual(0, gilded_rose.items[3].quality)

    # Conjured Mana Cake
    def test_conjured(self):
        items = [Item(name="Conjured Mana Cake", sell_in=3, quality=5),
                 Item(name="Conjured Mana Cake", sell_in=1, quality=32)
                 ]

        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()  # Dia 1
        self.assertEqual(2, gilded_rose.items[0].sell_in)
        self.assertEqual(3, gilded_rose.items[0].quality)
        self.assertEqual(0, gilded_rose.items[1].sell_in)
        self.assertEqual(30, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Dia 2
        self.assertEqual(1, gilded_rose.items[0].sell_in)
        self.assertEqual(1, gilded_rose.items[0].quality)
        self.assertEqual(-1, gilded_rose.items[1].sell_in)
        self.assertEqual(26, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Dia 3
        self.assertEqual(0, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-2, gilded_rose.items[1].sell_in)
        self.assertEqual(22, gilded_rose.items[1].quality)

        gilded_rose.update_quality()  # Dia 4
        self.assertEqual(-1, gilded_rose.items[0].sell_in)
        self.assertEqual(0, gilded_rose.items[0].quality)
        self.assertEqual(-3, gilded_rose.items[1].sell_in)
        self.assertEqual(18, gilded_rose.items[1].quality)


if __name__ == '__main__':
    unittest.main()