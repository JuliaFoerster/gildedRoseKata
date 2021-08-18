# -*- coding: utf-8 -*-
from .item import Item

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update(self):
        for item in self.items:
            item.update()


class BackstagePassItem(Item):

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
