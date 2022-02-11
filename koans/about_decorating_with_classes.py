#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

import functools

class AboutDecoratingWithClasses(Koan):
    def maximum(self, a, b):
        if a>b:
            return a
        else:
            return b

    def test_partial_that_wrappers_no_args(self):
        """
        Before we can understand this type of decorator we need to consider
        the partial.
        """
        max = functools.partial(self.maximum)

        self.assertEqual(23, max(7,23))
        self.assertEqual(10, max(10,-10))

        #partial 'freezes' some arguments for the function and then lets you reuse/just pass in some portion of it later. In the above examples, no args were frozen. 

    def test_partial_that_wrappers_first_arg(self):
        max0 = functools.partial(self.maximum, 0)

        self.assertEqual(0, max0(-4))
        self.assertEqual(5, max0(5))

        #froze the 0 value in this one so we only pass in one argument later

    def test_partial_that_wrappers_all_args(self):
        always99 = functools.partial(self.maximum, 99, 20)
        always20 = functools.partial(self.maximum, 9, 20)

        self.assertEqual(99, always99())
        self.assertEqual(20, always20())
    #in these one we freeze both arguments so they functions always return the same values. 
    # ------------------------------------------------------------------

    class doubleit: #totally missed that this whole class was called double it initially. 
        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args):
            return self.fn(*args) + ', ' + self.fn(*args) 

        def __get__(self, obj, cls=None): #not sure what Get is doing here? from what I can tell nothing. 
            if not obj:
                # Decorating an unbound function
                return self #unbound because it doesn't pass self in as an argument? 
            else:
                # Decorating a bound method
                return functools.partial(self, obj)
                #bound because it passes self in as arguement. the partial freezes the values of self and obj. 

    @doubleit
    def foo(self):
        return "foo"

    @doubleit
    def parrot(self, text):
        return text.upper()

    def test_decorator_with_no_arguments(self):
        # To clarify: the decorator above the function has no arguments, even
        # if the decorated function does

        self.assertEqual("foo, foo", self.foo())
        self.assertEqual('PIECES OF EIGHT, PIECES OF EIGHT', self.parrot('pieces of eight'))

    # ------------------------------------------------------------------

    def sound_check(self):
        #Note: no decorator
        return "Testing..."

    def test_what_a_decorator_is_doing_to_a_function(self):
        #wrap the function with the decorator
        self.sound_check = self.doubleit(self.sound_check)

        self.assertEqual("Testing..., Testing...", self.sound_check())
        #wrapping the funciton in the decorator calls it with the new args from sound_check.
    # ------------------------------------------------------------------

    class documenter:
        def __init__(self, *args):
            self.fn_doc = args[0]

        def __call__(self, fn):
            def decorated_function(*args):
                return fn(*args)

            if fn.__doc__:
                decorated_function.__doc__ = fn.__doc__ + ": " + self.fn_doc
            else:
                decorated_function.__doc__ = self.fn_doc
            return decorated_function

    @documenter("Increments a value by one. Kind of.")
    def count_badly(self, num):
        num += 1
        if num==3:
            return 5
        else:
            return num
    @documenter("Does nothing")
    def idler(self, num):
        "Idler"
        pass

    def test_decorator_with_an_argument(self):
        self.assertEqual(5, self.count_badly(2))
        self.assertEqual("Increments a value by one. Kind of.",
                         self.count_badly.__doc__) #__doc__ the documentation on count_badly. 

    def test_documentor_which_already_has_a_docstring(self):
        self.assertEqual("Idler: Does nothing", self.idler.__doc__)
        #combines the function documentation (fn.__doc__) and the self documentation (self.fn_doc) "idler"

    # ------------------------------------------------------------------

    @documenter("DOH!")
    @doubleit
    @doubleit
    def homer(self):
        return "D'oh"

    def test_we_can_chain_decorators(self):
        self.assertEqual("D'oh, D'oh, D'oh, D'oh", self.homer()) # calls the function in doubleit twice. 
        self.assertEqual("DOH!", self.homer.__doc__)

        #pulls the documentation from the function 'homer'

