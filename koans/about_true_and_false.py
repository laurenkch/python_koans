#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutTrueAndFalse(Koan):
    def truth_value(self, condition):
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(True))

        #true should equal true. I think. 

    def test_false_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(False))

        #hopefully false equals false too.

    def test_none_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(None))

        #based on the name of the function, it seems like None will be a false value. 

    def test_zero_is_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(0))

        #0 is also a falsey

    def test_empty_collections_are_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value([]))
        self.assertEqual('false stuff', self.truth_value(()))
        self.assertEqual('false stuff', self.truth_value({}))
        self.assertEqual('false stuff', self.truth_value(set()))

        #all of these empties (list, tuple, dictionary, set) are treated as false. 

    def test_blank_strings_are_treated_as_false(self):
        self.assertEqual('false stuff', self.truth_value(""))

        #emtpy strings = false

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual('true stuff', self.truth_value(1))
        self.assertEqual('true stuff', self.truth_value([0]))
        self.assertEqual('true stuff', self.truth_value((0,)))
        self.assertEqual(
            'true stuff',
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual('true stuff', self.truth_value(' ')) #a string with just a space
        self.assertEqual('true stuff', self.truth_value('0'))

#all of these are truthy. 