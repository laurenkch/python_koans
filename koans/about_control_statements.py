#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        if True:
            result = 'true value'
        else:
            result = 'false value'
        self.assertEqual('true value', result)

        #as is, this one is always true, never false and never even reads the second result. 

    def test_if_then_statements(self):
        result = 'default value'
        if True:
            result = 'true value'
        self.assertEqual('true value', result)

        #result starts off 'default value' but reaches if true (which is always true) so ends up as 'true value'

    def test_if_then_elif_else_statements(self):
        if False:
            result = 'first value'
        elif True:
            result = 'true value'
        else:
            result = 'default value'
        self.assertEqual('true value', result)

        # if false is false, so it doesn't do anything/read further. then else if true is read and is true so the result is assigned as 'true value'. we never read 'else' since true is always true. 

    def test_while_statement(self):
        i = 1
        result = 1
        while i <= 10:
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

        #result * i
        #1*1 
        #1*2
        #2*3
        #6*4
        #24*5
        #120*6
        #720*7
        #5040*8
        #40320*9
        #362880*10
        #3628800

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result = result * i
            i += 1
        self.assertEqual(3628800, result)

        #same as above, just with a break

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1,3,5,7,9], result)

        #even numbers are divisible by two and have a remainder of 0. The continue breaks you out of the loop and takes you back to the beginning. 
        #so, odd numbers will go past the continue in the code to the append. 
        #even numbers don't append but will return you to the start of the loop
    
    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = []
        for item in phrase:
            result.append(item.upper())
        self.assertEqual(["FISH", "AND", "CHIPS"], result)

        #goes through each item in phrase and then changes it to uppercase. 

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + "'   Answer: '" + answer + "'")
        #adds to the list "Contestant: Lancelot Answer: Blue" etc. 

        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        #this one I initially really messed up the spacing/quotations. 

        self.assertRegex(result[2], text)

        self.assertNotRegex(result[0], text)
        self.assertNotRegex(result[1], text)
        self.assertNotRegex(result[3], text)

        #Also took me a bit to realize that the asserts at the very end were saying that it did not equal the result at indexes 0, 1, 3 and it should only equal the result at index 2. 
