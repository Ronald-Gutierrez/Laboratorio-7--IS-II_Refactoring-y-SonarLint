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

    # actualizar elementos predeterminados
    def update_default(self, item):

        # disminuir la calidad
        if item.quality > self.min_quality:
            item.quality -= 1
            # si han pasado los días de venta, disminuya la calidad dos veces
            if item.sell_in <= 0:
                item.quality -= 1

        # disminuir sell_in días
        item.sell_in -= 1

    # actualizacion de 'Aged Brie'
    def update_aged_brie(self, item):

        # aumentar la calidad
        if item.quality < self.max_quality:
            item.quality = item.quality + 1
            # si han pasado los días de venta, disminuye la calidad dos veces 
            if item.sell_in <= 0:
                item.quality += 1

        # disminuir sell_in días
        item.sell_in -= 1

    # actualizar 'Sulfuras' - Legendary item
    def update_sulfuras(self, item):
        pass

    # actualizar 'Backstage Passes'
    def update_backstage_passes(self, item):

        # aumentar la calidad
        if 10 >= item.sell_in > 5:
            item.quality += 2
        elif 5 >= item.sell_in > 0:
            item.quality += 3
        elif item.sell_in <= 0:
            item.quality = 0
        else:
            item.quality += 1

        if item.quality > self.max_quality:
            item.quality = self.max_quality

        # disminuir sell_in días
        item.sell_in -= 1

    # actualizar 'Conjured' - nuevo elemento que se agregará
    def update_conjured(self, item):

        # decrease quality
        if item.quality > self.min_quality:
            item.quality -= 2
            # si han pasado los días de venta, disminuya la calidad dos veces
            if item.sell_in <= 0:
                item.quality -= 2

        if item.quality < self.min_quality:
            item.quality = self.min_quality

       # disminuir sell_in días
        item.sell_in -= 1