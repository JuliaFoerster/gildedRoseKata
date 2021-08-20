# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_regular_items_decrease_by_one(self):
        items = [Item.create_item("chocolate", 1, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 2)

    def test_quality_goes_up_for_improving_products_aged_brie(self):
        items = [Item.create_item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 2)

    def sell_in_decreases_when_day_passed_without_sell(self):
        items = [Item.create_item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update()
        self.assertEquals(items[0].sell_in, 0)

    def test_quality_goes_up_for_improving_products_backstage_passes(self):
        items = [Item.create_item("Backstage passes to a TAFKAL80ETC concert", 16, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 2)

    def test_quality_goes_up_by_two_for_improving_products_with_10_days_or_less_left_backstage_passes(self):
        items = [Item.create_item("Backstage passes to a TAFKAL80ETC concert", 8, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 20)

    def test_quality_goes_up_by_three_for_improving_products_with_5_days_or_less_left(self):
        items = [Item.create_item("Backstage passes to a TAFKAL80ETC concert", 4, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 21)

    def test_quality_decrease_twice_as_fast_after_sell_by(self):
        items = [Item.create_item("Chocolata", 0, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 16)


    def test_backstage_passes_and_brie_go_to_quality_zero_after_sell_by(self):
        items = [Item.create_item("Backstage passes to a TAFKAL80ETC concert", 0, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 0)


    def test_sulfuras_neverSold(self):
        items = [Item.create_item("Sulfuras, Hand of Ragnaros", 1, 18)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 18)
        self.assertEquals(items[0].sell_in, 1)

    def test_quality_does_not_increase_past_50(self):
        items = [Item.create_item("Aged Brie", 10, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals(items[0].quality, 50)

    # def test_conjured_items_decrease_in_quality_twice_as_fast(self):

if __name__ == '__main__':
    unittest.main()



