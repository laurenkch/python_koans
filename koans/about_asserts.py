#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(True) # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(True, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(2, 1 + 1)

        # assertEqual says the two values are equal and will error if they aren't. 

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = 2
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

        # in order for the assertTrue to come back without error, the comparison inside needs to evaluate to true. So, the expected_value needs to equal the actual_value.

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = 2
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

        #this does the same thing as above, but in a shorter syntax. It says the two values inside are equal and will throw an error if not. 

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        assert True

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> "navel" <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(str, "navel".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

