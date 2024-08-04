#!/usr/bin/env python3

import runpy
import pytest

class TestNameError:
    '''
    a_name_error.py
    '''

    def test_name_error(self):
        '''
        Contains defined name "hello_world"
        '''
        with pytest.raises(NameError):
            runpy.run_path('lib/a_name_error.py')

class TestSyntaxError:
    '''
    a_syntax_error.py
    '''

    def test_syntax_error(self):
        '''
        Multiplies two numbers
        '''
        with pytest.raises(SyntaxError):
            runpy.run_path('lib/a_syntax_error.py')

class TestTypeError:
    '''
    a_type_error.py
    '''

    def test_type_error(self):
        '''
        Adds two numbers
        '''
        with pytest.raises(TypeError):
            runpy.run_path('lib/a_type_error.py')

class TestAssertionError:
    '''
    an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        Evaluates two equal values
        '''
        with pytest.raises(AssertionError):
            runpy.run_path('lib/an_assertion_error.py')
