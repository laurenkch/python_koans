#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

        # an empty list has a length of zero. 

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)

        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)

    # different ways to add a value to a list. 
    #the : method assigns a value to the index. 
    #the append method puts it at the end of the list. like push. 

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    #similar to reading an array at the index position. negative numbers start at the end and work backwards. -1 is the last item in the list

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2])
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0])
        self.assertEqual([], noms[4:100])
        self.assertEqual([], noms[5:0])

# slices the list the first value is the start value, the second is the end. returns the answer also in a list format list. 
# slicing at the same number (without moving forward or back), returns an empty set
#[2:0] doesn't work because 2 is greater than 0. Doesn't go backward because they aren't negative values. positive just goes forward.
#[4:100] nothing after 4, nothing to return.


    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']

        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])
# default value is 0 if ommitted

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        #this just says a range is a type of range, it is not a list in and of itself.
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        #again, a range does not equal a list with the same values. They aren't the same type (unless you wrap it in a list).
        self.assertEqual([0,1,2,3,4], list(range(5)))
        #if only one number is included, the first value is the default of 0.
        self.assertEqual([5,6,7,8], list(range(5, 9)))

        #ranges stop at the last number they don't include it in the output. but the first number is included. 

    def test_ranges_with_steps(self):
        self.assertEqual([5,4], list(range(5, 3, -1)))
        # third number is the step and it's optional. in this case, counting down 1 number at a time. last number not included. 

        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2)))
        #counting up 2 numbers at a time.

        self.assertEqual([1, 4, 7], list(range(1, 8, 3)))
        #counting up three at a time.
        self.assertEqual([5, 1, -3], list(range(5, -7, -4)))
        #counting down by -4s
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4)))

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not')
        self.assertEqual(['you','shall','not','pass'], knight)

        #inserts 'not at the 2 spot, just after shall. 

        knight.insert(0, 'Arthur')
        self.assertEqual(['Arthur','you','shall','not','pass'], knight)
        #inserts 'Arthur' at the start of the list (the zero spot)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last')

        self.assertEqual([10,20,30,40,'last'], stack)

        #adds 'stack' to the end of the list. 

        popped_value = stack.pop()
        self.assertEqual('last', popped_value)
        self.assertEqual([10,20,30,40], stack)

        #pop returns the value, not a list. 
        #if a number isn't designated, it takes the last value off. 

        popped_value = stack.pop(1)
        self.assertEqual(20, popped_value)
        self.assertEqual([10,30,40], stack)

        # the 1 here indicates which value to pop off, in this case the "20"

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last')

        self.assertEqual([1, 2, 'last'], queue)

        #queue.append will add the value to the end of the list. 

        popped_value = queue.pop(0)
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # removes the first item from the list. moves the other values down by one spot. 

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.

