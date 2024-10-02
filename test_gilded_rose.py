# -*- coding: utf-8 -*-
import unittest
from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    # Test 1: Aged Brie increases in quality over time
    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 1)  # Quality should increase by 1

    # Test 2: Backstage passes increase in quality and drop after concert
    def test_backstage_passes_increase_and_drop(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 10, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 5, 20),
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 21)  # More than 10 days, increase by 1
        self.assertEqual(items[1].quality, 22)  # 10 or fewer days, increase by 2
        self.assertEqual(items[2].quality, 23)  # 5 or fewer days, increase by 3
        self.assertEqual(items[3].quality, 0)   # After the concert, quality drops to 0

    # Test 3: Conjured items degrade twice as fast
    def test_conjured_items_degrade_twice_as_fast(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 4)  # Should degrade by 2

if __name__ == '__main__':
    unittest.main()
