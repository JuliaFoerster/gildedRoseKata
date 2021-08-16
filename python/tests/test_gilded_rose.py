# -*- coding: utf-8 -*-
import unittest

from ..src.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

        # import ipdb
        # ipdb.set_trace()

    def test_quality_of_item_never_increases_above_50(self):
        items = [Item("Test Item", 0, 50)]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertTrue(items[0].quality <= 50)


    def test_quality_of_item_never_negative(self):
        items = [Item("Test Item", 0, 10)]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertTrue(items[0].quality >= 0)


    # def test_brie_quality_increases(self):
    #     items = [Item("Aged Brie", 5, 40)]






if __name__ == '__main__':
    unittest.main()
