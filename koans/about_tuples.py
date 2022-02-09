#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutTuples(Koan):
    def test_creating_a_tuple(self):
        count_of_three =  (1, 2, 5)
        self.assertEqual(5, count_of_three[2])

        #returns the value at the index of 2

    def test_tuples_are_immutable_so_item_assignment_is_not_possible(self):

        count_of_three = (1, 2, 5)
        try:
            count_of_three[2] = "three"
        except TypeError as ex:
            msg = ex.args[0]

        # Note, assertRegex() uses regular expression pattern matching,
        # so you don't have to copy the whole message.

        self.assertRegex(msg, "'tuple' object does not support item assignment")

        #you can't just replace one item in a tuple

    def test_tuples_are_immutable_so_appending_is_not_possible(self):
        count_of_three =  (1, 2, 5)
        with self.assertRaises(AttributeError):
            count_of_three.append("boom")

        # Tuples are less flexible than lists, but faster.

        #can't append a tuple, there is no such attribute for tuples. Can't look up the tree to see what to do. The assertRaises function above looks to see what kind of exception was thrown when you run the function below. 

    def test_tuples_can_only_be_changed_through_replacement(self):
        count_of_three = (1, 2, 5)

        list_count = list(count_of_three)
        list_count.append("boom")
        count_of_three = tuple(list_count)

        self.assertEqual((1,2,5,"boom"), count_of_three)

        #you can change a tuple if you replace the whole thing at once (or make a copy and then replace the whole thing if you're changing a portion)

    def test_tuples_of_one_look_peculiar(self):
        self.assertEqual(int, (1).__class__)
        self.assertEqual(tuple, (1,).__class__)
        self.assertEqual(tuple, ("I'm a tuple",).__class__)
        self.assertEqual(str, ("Not a tuple").__class__)

    #single tuples use parenthesis and a comma at the end. without the comma it is not a tuple. 

    def test_tuple_constructor_can_be_surprising(self):
        self.assertEqual(("S","u","r","p","r","i","s","e","!",), tuple("Surprise!"))

    #making a tuple from a single string will separate out the letters. 

    def test_creating_empty_tuples(self):
        self.assertEqual(() , ())
        self.assertEqual(() , tuple()) #Sometimes less confusing

    #you can make an empty tuple with empty parentheses

    def test_tuples_can_be_embedded(self):
        lat = (37, 14, 6, 'N')
        lon = (115, 48, 40, 'W')
        place = ('Area 51', lat, lon)
        self.assertEqual(('Area 51',(37, 14, 6, 'N'), (115, 48, 40, 'W')) , place)
    
    #tuples can nest and you can drill down in them to read values. 

    def test_tuples_are_good_for_representing_records(self):
        locations = [
            ("Illuminati HQ", (38, 52, 15.56, 'N'), (77, 3, 21.46, 'W')),
            ("Stargate B", (41, 10, 43.92, 'N'), (1, 49, 34.29, 'W')),
        ]

        locations.append( ("Cthulu", (26, 40, 1, 'N'), (70, 45, 7, 'W')) )

        self.assertEqual("Cthulu", locations[2][0])
        self.assertEqual(15.56, locations[0][1][2])

        #didn't realize at first this was a list of tuples and I initially thought you wouldn't be able to add the "Cthulu" one to this list. 
        
