#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutClasses(Koan):
    class Dog:
        "Dogs need regular walkies. Never, ever let them drive."

    def test_instances_of_classes_can_be_created_adding_parentheses(self):
        # NOTE: The .__name__ attribute will convert the class
        # into a string value.
        fido = self.Dog() 
        self.assertEqual('Dog', fido.__class__.__name__)
            #fido is the same class as Dog. 
    def test_classes_have_docstrings(self):
        self.assertRegex(
            self.Dog.__doc__, 'Dogs need regular walkies. Never, ever let them drive.')

    # ------------------------------------------------------------------

    class Dog2:
        def __init__(self):
            self._name = 'Paul'

        def set_name(self, a_name):
            self._name = a_name

    def test_init_method_is_the_constructor(self):
        dog = self.Dog2()
        self.assertEqual('Paul', dog._name)

    def test_private_attributes_are_not_really_private(self):
        dog = self.Dog2()
        dog.set_name("Fido")
        self.assertEqual('Fido', dog._name) #we changed the value of ._name even though it was supposed to belong to Dog 2
        # The _ prefix in _name implies private ownership, but nothing is truly
        # private in Python.

    def test_you_can_also_access_the_value_out_using_getattr_and_dict(self):
        fido = self.Dog2()
        fido.set_name("Fido")

        self.assertEqual("Fido", getattr(fido, "_name")) 
        # getattr(), setattr() and delattr() are a way of accessing attributes
        # by method rather than through assignment operators

        self.assertEqual("Fido", fido.__dict__["_name"])
        # Yes, this works here, but don't rely on the __dict__ object! Some
        # class implementations use optimization which result in __dict__ not
        # showing everything.

        #__dict__ pulls all attributes for the thing you attach it to, aka. object. 

    # ------------------------------------------------------------------

    class Dog3:
        def __init__(self):
            self._name = None

        def set_name(self, a_name):
            self._name = a_name

        def get_name(self):
            return self._name

        name = property(get_name, set_name)

    def test_that_name_can_be_read_as_a_property(self):
        fido = self.Dog3()
        fido.set_name("Fido")

        # access as method
        self.assertEqual("Fido", fido.get_name())

        # access as property
        self.assertEqual("Fido", fido.name)

        #accessing the same thing, different ways. 

    # ------------------------------------------------------------------

    class Dog4:
        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name #a funtion that returns the ._name value for each instance. 

        @name.setter
        def name(self, a_name):  #sets the a_name variable to the 'self._name' attribute
            self._name = a_name

    def test_creating_properties_with_decorators_is_slightly_easier(self):
        fido = self.Dog4()

        fido.name = "Fido" #passes "Fido" into the name.setter function defined above as the variable a_name 
        self.assertEqual("Fido", fido.name)

    # ------------------------------------------------------------------

    class Dog5:
        def __init__(self, initial_name):
            self._name = initial_name

        @property
        def name(self):
            return self._name

    def test_init_provides_initial_values_for_instance_variables(self):
        fido = self.Dog5("Fido")
        self.assertEqual("Fido", fido.name)

        #this one we set it as we create the instance. 

    def test_args_must_match_init(self):
        with self.assertRaises(TypeError):
            self.Dog5()

        # THINK ABOUT IT:
        # Why is this so?
        #I would guess it tries to assign the name right away and without the name as a string in there the code would return errors. 

    def test_different_objects_have_different_instance_variables(self):
        fido = self.Dog5("Fido")
        rover = self.Dog5("Rover")

        self.assertEqual(False, rover.name == fido.name)

        #each would have their own name, they do not match. 

    # ------------------------------------------------------------------

    class Dog6:
        def __init__(self, initial_name):
            self._name = initial_name

        def get_self(self):
            return self

        def __str__(self):
            return "<Dog name '" + self._name + "'>"

        def __repr__(self):
            return "<Dog named '" + self._name + "'>"

        #not entirely sure why we needed to define it if it is the same thing as __repr__. Or maybe it was just an exercise and you'd normally define it if it was something different. 

    def test_inside_a_method_self_refers_to_the_containing_object(self):
        fido = self.Dog6("Fido")

        self.assertEqual("<Dog named 'Fido'>", repr(fido.get_self()))  # Not a string! #had to put repr ahead of the second value to get it into a string instead of an object. 

    def test_str_provides_a_string_version_of_the_object(self):
        fido = self.Dog6("Fido")

        self.assertEqual("Fido", fido._name)  # changed to fido._name from str(fido) which returned an object of fido not a string. 

    def test_str_is_used_explicitly_in_string_interpolation(self):
        fido = self.Dog6("Fido")

        self.assertEqual("My dog is <Dog name 'Fido'>", "My dog is " + str(fido)) #name not named since this was converted to a string. 

    def test_repr_provides_a_more_complete_string_version(self):
        fido = self.Dog6("Fido")
        self.assertEqual("<Dog named 'Fido'>", repr(fido))
        #not sure why it's more complete, but it is what is set for the repr

    def test_all_objects_support_str_and_repr(self):
        seq = [1, 2, 3]

        self.assertEqual('[1, 2, 3]', str(seq))
        self.assertEqual("[1, 2, 3]", repr(seq))

        self.assertEqual("STRING", str("STRING"))
        self.assertEqual("'STRING'", repr("STRING"))
    #Oh, I guess maybe repr is more complete because it includes the parenthesis around the oustide of the return. 