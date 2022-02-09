#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutExceptions(Koan):

    class MySpecialError(RuntimeError):
        pass

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.mro()
        self.assertEqual('RuntimeError', mro[1].__name__)
        self.assertEqual('Exception', mro[2].__name__)
        self.assertEqual('BaseException', mro[3].__name__)
        self.assertEqual('object', mro[4].__name__)

        #mro = method resolution order. the order the program will use to look up the classes to find a method or attribute. in this case, we passed in "RuntimeError" so that's the first name, then it goes up to the less specific 'Exception', then 'BaseException' and finally 'object.'

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'

            ex2 = ex

        self.assertEqual('exception handled', result)
        # this function self.fail always fails so it will reassign result as 'exception handled'

        self.assertEqual(True, isinstance(ex2, Exception))
        self.assertEqual(False, isinstance(ex2, RuntimeError))
        #ex2 is an exception because that's what we used to make it in except Exception as ex:

        #runtimeerror is a subclass of exception, but exception isn't an instance of runtimeerror so the second one is false. 

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual("Oops", ex2.args[0])

        #arguements passed in are "Oops"

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]

        self.assertEqual('exception handled', result)
        self.assertEqual('My Message', msg)

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual('no damage done', result)

        #I assumed it would pass by the second part without doing anything since pass is in there. 


    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual('always run', result)

        #finally actions always run so the result will always be 'always run'
