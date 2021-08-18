# -*- coding: utf-8 -*-
import unittest

from ..src.gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)


    def test_quality_of_item_never_negative(self):
        items = [Item("Test Item", 0, 0)]
        rose = GildedRose(items)
        rose.update_quality()
        self.assertEqual(items[0].quality, 0)


    def test_sellin_value_decreases_by_one_each_day(self):
        items = [Item("Test Item", 5, 20)]
        sellin_value_before = items[0].sell_in
        rose = GildedRose(items)
        rose.update_quality()
        sellin_value_after = items[0].sell_in
        self.assertEqual(sellin_value_before - sellin_value_after, 1)


    def test_quality_value_decreases_each_day(self):
        items = [Item("Test Item", 5, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertTrue(quality_value_after < quality_value_before)


    def test_quality_value_of_aged_brie_increases_each_day(self):
        items = [Item("Aged Brie", 5, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertTrue(quality_value_after > quality_value_before)


    def test_quality_value_of_aged_brie_stays_same_when_at_max_quality_value(self):
        items = [Item("Aged Brie", 5, 50)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_after, quality_value_before)


    def test_quality_degrades_twice_as_fast_after_sell_by_date(self):
        items = [Item("Test Item", 1, 50)]
        quality_value_1 = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_2 = items[0].quality
        rate_of_quality_decrease_before_sell_by_date = quality_value_2 - quality_value_1
        rose.update_quality()
        quality_value_3 = items[0].quality
        rate_of_quality_decrease_after_sell_by_date = quality_value_3 - quality_value_2
        self.assertEqual(2 * rate_of_quality_decrease_before_sell_by_date, rate_of_quality_decrease_after_sell_by_date)


    def test_sulfuras_quality_stays_same(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_before, quality_value_after)


    def test_backstage_passes_quality_increases_if_sellin_date_more_than_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_before, quality_value_after - 1)


    def test_backstage_passes_quality_increases_by_2_if_sellin_date_between_6_and_10_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_before, quality_value_after - 2)


    def test_backstage_passes_quality_increases_by_3_if_sellin_date_between_1_and_5_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 1, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_before, quality_value_after - 3)


    def test_backstage_passes_quality_is_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after_concert = items[0].quality
        self.assertEqual(quality_value_after_concert, 0)


    def test_conjured_items_degrade_in_quality_twice_as_fast_as_normal_items(self):
        items = [Item("Conjured", 6, 20)]
        quality_value_before = items[0].quality
        rose = GildedRose(items)
        rose.update_quality()
        quality_value_after = items[0].quality
        self.assertEqual(quality_value_after - quality_value_before, 2)



if __name__ == '__main__':
    unittest.main()
