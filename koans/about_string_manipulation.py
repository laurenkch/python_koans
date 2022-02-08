#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

        #lets you put variables into a string and tell which one to go where depending on their index number in the function parentheses

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

        #although the order they are put into the parenthesis matters, the order they are called and how they are used in the string do not matter. 

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string)

        #returns the square root of 5 as the first number, then uses the variable decimal_places to include 4 spots following the '.' 

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual('let', string[7:10])

        #starts at 7 (the l) stops at spot 10 

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1])

        # the [1] spot is the second letter, the a. 

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

        #ord returns the unicode value of the character. the unicode value of 'a' is 97.
        #the unicode value of b is 98, so it is equal to the right hand side (97 +1)

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words)

    #default separator is white space, so it'll give you the individual words here. 

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')
        words = pattern.split(string)
        #here we split it according to the pattern we defined above, which looks for ; or , . now, anytime we encounter a , or a ; we'll split the strings. 
        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        self.assertEqual(r'\n', string)
        self.assertEqual(2, len(string))

        #since it's raw, it'll return a string of \n, which is a length of two. 

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual('Now is the time', ' '.join(words))

        #joins the words and uses a whitespace as the separator because ' ' is before the .join. that part tells it what to include as the separator. (could be - or , or anything else).

    def test_strings_can_change_case(self):
        self.assertEqual('Guido', 'guido'.capitalize())
        #capatalize the first letter
        self.assertEqual('GUIDO', 'guido'.upper())
        # changes to all uppercase
        self.assertEqual('timbot', 'TimBot'.lower())
        #changes to all lowercase
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        #capitalizes each new word like a title. 
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())
        #switches cases. 
