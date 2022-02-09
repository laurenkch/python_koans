#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'MacLeod', 'Ramirez', 'Matunas', 'Malcolm'}, there_can_only_be_only_one)

        #like sets in js, there are not duplicate values in sets. used [] instead of {} the first time, forgot we changed it to a set

    def test_empty_sets_have_different_syntax_to_populated_sets(self):
        self.assertEqual({1,2,3}, {1, 2, 3})
        self.assertEqual(set(), set())

        #you cannot just say {} for an emtpy set, because it's an emtpy dictionary. have to say set(). But you can use {} if you have a populated set. 

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(set, {1, 2, 3}.__class__) # a set
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__) #a dictionary since it has key value pairs. 

        self.assertEqual(dict, {}.__class__)

        #An empty curly would be a dictionary by default, which is why you have to say set() for an empty set.  

    def test_creating_sets_using_strings(self):
        self.assertEqual(set({'12345'}), {'12345'})
        self.assertEqual({'1','2','3','4','5'}, set('12345'))

        #when you make a string into a set with set() it'll split out each character unless you add curly brackets to the inside. 

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1','2','3','4','5'], sorted(set('12345')))

        #originally had this with curly brackets, but turns out sorted outputs as a list. Also, I forgot that sets are unordered by nature so it wouldn't stay as 1, 2, 3, 4, 5 that way. 

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual({'Willie'}, scotsmen - warriors) #take the list of scotsmen and subtract the list of warriors
        self.assertEqual({'MacLeod', 'Wallace', 'Willie',
                         'Leonidas'}, scotsmen | warriors) #including all people found in list scotsmen or list warriors. aka. all of them (but only once since sets don't repeat)
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors) #people who are both scotsmen and warriors
        self.assertEqual({'Willie',
                         'Leonidas'}, scotsmen ^ warriors) # the symmetric difference, or values that are unique to each set, excluding overlap.

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') )

        #using set this way with just parenthesis will spread out the letters in the string. so each individual letter of cow is in the set, but the string of 'cow' is not. 

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake'))
        # <= tests if every element in the set is in other, which it is
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) ) 

        #true, because 'cake' is a set that exists inside the set of 'cherry cake'. another way to do the same thing as above. 

        self.assertEqual(False, set('cake') > set('pie'))

        # false. set('pie') is not in the set('cake')

        #docs say this operator:
        # tests whether the set is a proper superset of other, that is, set >= other and set != other.
