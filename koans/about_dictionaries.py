#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *

class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        self.assertEqual(0, len(empty_dict))

        #an emtpy dictionary has a lenght of 0 and equals {}

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual(2, len(babel_fish))

        #this dictionary has 2 pairs. 

    def test_accessing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two'])

        #returns the value of the corresponding key

    def test_changing_dictionaries(self):
        babel_fish = { 'one': 'uno', 'two': 'dos' }
        babel_fish['one'] = 'eins'

        expected = { 'two': 'dos', 'one': 'eins' }
        self.assertDictEqual(expected, babel_fish)

        #gives a new assignment to the key 'one'

    def test_dictionary_is_unordered(self):
        dict1 = { 'one': 'uno', 'two': 'dos' }
        dict2 = { 'two': 'dos', 'one': 'uno' }

        self.assertEqual(True, dict1 == dict2)

        #althouh the dictionaries are in different orders, they are still equal.


    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual(2, len(babel_fish.keys()))
        #there are two keys
        self.assertEqual(2, len(babel_fish.values()))
        #there are two values
        self.assertEqual(True, 'one' in babel_fish.keys())
        #true, 'one' is a key in babel_fish
        self.assertEqual(False, 'two' in babel_fish.values())
        #false, 'two' is a key but is not a value in babel_fish
        self.assertEqual(False, 'uno' in babel_fish.keys())
        #false, 'uno' is a value in babel_fish, it is not a key.
        self.assertEqual(True, 'dos' in babel_fish.values())
        #true, 'dos' is a value in the dictionary of babel_fish. 

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards))
        #5 key, value pairs in the dictionary of cards
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])

        #all keys were assigned the same value of 42. 

