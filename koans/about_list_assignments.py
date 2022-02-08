#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(["John", "Smith"], names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual("John", first_name)
        self.assertEqual("Smith", last_name)

        #you can split up an iterable item like this (sort of like destructuring)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual("Sir", title)
        self.assertEqual(["Ricky", "Bobby"], first_names)
        self.assertEqual("Worthington", last_name)

    #title takes the first slot, last_name takes whatever is last, the first_names will take anything else. 

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual("Mr", title)
        self.assertEqual([], first_names)
        self.assertEqual("Bond", last_name)
# the other variables are required, so nothing goes into first_names

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(["Willie", "Rae"], first_name)
        self.assertEqual("Johnson", last_name)

        #since the first variable will get assigned to the first item, it'll equal the whole sublist. 

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual("Rob", first_name)
        self.assertEqual("Roy", last_name)

#the two swapped