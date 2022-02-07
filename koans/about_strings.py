#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        self.assertEqual(True, isinstance(string, str))

        # assert Equal is comparing the two values. The right hand side is checking the instance of "Hello, world" to see if it's a string. Since it is, it'll return true. The left hand side should also say True.

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        self.assertEqual(True, isinstance(string, str))

        #same as above, but the string is uses single quotes instead of double. 

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        self.assertEqual(True, isinstance(string, str))

        #again, this is just proving that it's true that triple quotes are also strings. 

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        self.assertEqual(True, isinstance(string, str))

        # the above returns true because triple single quotes are strings. 

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        self.assertEqual(True, isinstance(string, str))

        #raw strings are also strings. Raw strings treat backslashes as literal characters instead of code. 

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        self.assertEqual('He said, "Go Away."', string)

        #this works because the outer quotes are singles and we used a different type inside the sentence. The assert is just comparing the sentence I wrote with the variable string. 

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        self.assertEqual("Don't", string)

        #the same as above, but reversed! using '' here would have closed the string too early. 

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        self.assertEqual(True, (a == b))

        # these both result in the the same sentence because we used the backslash to escape the string before putting in the same type as the wrapping symbols.

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        self.assertEqual(52, len(string))

        #len() returns the length of the object. It counts letters, spaces, symbols, and the line break also counts as one

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        self.assertEqual(15, len(string))

    #Same as above, In this case there are 10 letters, 2 symbols and, 3 line breaks


    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        self.assertEqual(True, (a == b))

        #a and b are both equal, but you don't have to escape the quotes around world because we used triple quotes. 

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        self.assertEqual('Hello "world"', string)

        #Because triple quotes indicate an end of the string, you do have to escape if the quote directly abuts the escaping quotes. I used single quotes in my version. 

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        self.assertEqual("Hello, world", string)

        #plus marks concatenates words, so it's the same as typing it all out at once as "Hello, world"

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        self.assertEqual("Hello, world", string)

        # adjacent strings are concencated automatically, so the statement above is the same things as writing out "Hello, world" as one line. 


    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    #although we used the plus symbol to combine hi and there into a variable called string, the original values remain unchanged. 

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        self.assertEqual("Hello, world", hi)

        #when we used += it did alter the original value of hi and added the value of there to the end, resulting in "Hello, world"

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        self.assertEqual("Hello, ", original)

    #although we used the += with hi and there, hi was just a copy of 'original' which remained unaltered and still reads as "Hello, "

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))

        #The string interprets the \n as a break, the length of the string is just one line break. 
