#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *


def my_global_function(a, b):
    return a + b


class AboutMethods(Koan):
    def test_calling_a_global_function(self):
        self.assertEqual(5, my_global_function(2, 3))

    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except TypeError as exception:
            msg = exception.args[0]

        # Note, the text comparison works for Python 3.2
        # It has changed in the past and may change in the future
        self.assertRegex(msg,
                         r'my_global_function\(\) missing 2 required positional arguments')

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        # Note, watch out for parenthesis. They need slashes in front!
        self.assertRegex(
            msg, 
            r'my_global_function\(\) takes 2 positional arguments but 3 were given')

    #python will let you know you added too many or not enough arguments in the exception argument(message)

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(None, self.pointless_method(1, 2))
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        self.assertEqual([1,'default_value'], self.method_with_defaults(1))
        self.assertEqual([1, 2], self.method_with_defaults(1, 2))

        #other variables would get precident before the default, default will only get used if not enough arguments are passed in. 

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        self.assertEqual((), self.method_with_var_args())
        #returns an emtpy tuple.
        self.assertEqual(('one',), self.method_with_var_args('one'))
        self.assertEqual(('one','two'), self.method_with_var_args('one', 'two'))

#

    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(12, function_with_the_same_name(3, 4))
   
    #I thought initially this would be 7, but I guess because we don't use "self" when we call the function 


    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(7, self.function_with_the_same_name(3, 4))

        # this one uses self, so I guess it is therefore linked to the first one where we also put "self" as one of the parameters.

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        self.assertEqual(42, self.another_method_with_the_same_name())

    def test_that_overlapped_method_is_still_there(self):
        self.assertEqual(10, self.link_to_overlapped_method())

        #returns 10 because link to overlapped method ran before the function was changed and is therefore still the old method.

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(None, self.empty_method())

    def test_pass_does_nothing_at_all(self):
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(True, "Still got to this line" != None)

        #I guess the assertequal is true becuase the sting doesn't equal none. 

        #More broadly, pass is used when you want to write a function but it doesn't have a purpose yet. It can't just be empty.  


    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        self.assertEqual('Madagascar', self.one_line_method())


    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertRegex(self.method_with_documentation.__doc__,
                         'A string placed at the beginning of a function is used for documentation')

        #__doc__ returns the documentation, whereas if you just call the function regularly you'd get 'ok'
    # ------------------------------------------------------------------

    class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password'  # Genius!

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual('Fido', rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # This is a little rude, but legal
        self.assertEqual("wagging", rover._tail())

        #I suppose rude because the underscore implies this function won't be used on other objects, just Dog, but here we're calling it on another function anyways. 

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        rover = self.Dog()
        with self.assertRaises(AttributeError):
            password = rover.__password()

        # But this still is!
        self.assertEqual("password", rover._Dog__password())

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection

        #name mangling = the ._Dog part before __password which python seems to add in automatically. 
