class DefaultUpdater(object):
    max_quality = 50

    def __init__(self, item):
        self.item = item

    def increase_quality(self):
        if self.item.quality < self.max_quality:
            self.item.quality += 1

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1

    def decrease_sell_in(self):
        self.item.sell_in -= 1

    def update(self):
        self.decrease_quality()
        self.decrease_sell_in()

        if self.item.sell_in < 0:
            self.decrease_quality()


class AgedBrieUpdater(DefaultUpdater):
    def update(self):
        self.increase_quality()
        self.decrease_sell_in()
        # if self.item.sell_in < 0:
        #     self.increase_quality()


class BackstagePassUpdater(DefaultUpdater):
    days_threshold_min = 10
    days_threshold_max = 5

    def update(self):
        self.increase_quality()
        if self.item.sell_in <= self.days_threshold_min:
            self.increase_quality()
        if self.item.sell_in <= self.days_threshold_max:
            self.increase_quality()
        self.decrease_sell_in()
        if self.item.sell_in < 0:
            self.item.quality = 0


class SulfurasUpdater(DefaultUpdater):
    def update(self):
        pass


class ConjuredUpdater(DefaultUpdater):
    def update(self):
        self.decrease_quality()
        self.decrease_quality()


class ItemUpdater(object):

    class_mapping = {
        "Aged Brie": AgedBrieUpdater,
        "Sulfuras, Hand of Ragnaros": SulfurasUpdater,
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdater
    }

    @classmethod
    def create(cls, item):
        if item.name in cls.class_mapping:
            return cls.class_mapping[item.name](item)
        if item.name[:8] == 'Conjured':
            return ConjuredUpdater(item)
        return DefaultUpdater(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            itemUpdater = ItemUpdater.create(item)
            itemUpdater.update()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    # def update(self):
    # if self.name != "Aged Brie" and self.name != "Backstage passes to a TAFKAL80ETC concert":
    #     if self.quality > 0:
    #         if self.name != "Sulfuras, Hand of Ragnaros":
    #             self.quality = self.quality - 1
    # else:
    #     if self.quality < 50:
    #         self.quality = self.quality + 1
    #         if self.name == "Backstage passes to a TAFKAL80ETC concert":
    #             if self.sell_in < 11:
    #                 if self.quality < 50:
    #                     self.quality = self.quality + 1
    #             if self.sell_in < 6:
    #                 if self.quality < 50:
    #                     self.quality = self.quality + 1
    # if self.name != "Sulfuras, Hand of Ragnaros":
    #     self.sell_in = self.sell_in - 1
    # if self.sell_in < 0:
    #     if self.name != "Aged Brie":
    #         if self.name != "Backstage passes to a TAFKAL80ETC concert":
    #             if self.quality > 0:
    #                 if self.name != "Sulfuras, Hand of Ragnaros":
    #                     self.quality = self.quality - 1
    #         else:
    #             self.quality = self.quality - self.quality
    #     else:
    #         if self.quality < 50:
    #             self.quality = self.quality + 1
