# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items, max_quality=50, min_quality=0, legendary_quality=80):
        self.items = items
        self.max_quality = max_quality
        self.min_quality = min_quality
        self.legendary_quality = legendary_quality

    def get_items(self):
        return self.items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.update_sulfuras(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name == "Conjured Mana Cake":
                self.update_conjured(item)
            else:
                self.update_default(item)

    # update default items
    def update_default(self, item):

        # decrease quality
        if item.quality > self.min_quality:
            item.quality = item.quality - 1
            # if sell in days have passed, decrease quality twice
            if item.sell_in <= 0:
                item.quality = item.quality - 1

        # decrease sell_in days
        item.sell_in = item.sell_in - 1

    # update 'Aged Brie'
    def update_aged_brie(self, item):

        # increase quality
        if item.quality < self.max_quality:
            item.quality = item.quality + 1
            # if sell in days have passed, decrease quality twice ??? not explicitely mentioned but original code works that way
            if item.sell_in <= 0:
                item.quality = item.quality + 1

        # decrease sell_in days
        item.sell_in = item.sell_in - 1

    # update 'Sulfuras' - Legendary item
    def update_sulfuras(self, item):
        pass

    # update 'Backstage Passes'
    def update_backstage_passes(self, item):

        # increase quality
        if 10 >= item.sell_in > 5:
            item.quality = item.quality + 2
        elif 5 >= item.sell_in > 0:
            item.quality = item.quality + 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality = item.quality + 1

        if item.quality > self.max_quality:
            item.quality = self.max_quality

        # decrease sell_in days
        item.sell_in = item.sell_in - 1

    # update 'Conjured' - new item to be added
    def update_conjured(self, item):

        # decrease quality
        if item.quality > self.min_quality:
            item.quality = item.quality - 2
            # if sell in days have passed, decrease quality twice
            if item.sell_in <= 0:
                item.quality = item.quality - 2

        if item.quality < self.min_quality:
            item.quality = self.min_quality

        # decrease sell_in days
        item.sell_in = item.sell_in - 1