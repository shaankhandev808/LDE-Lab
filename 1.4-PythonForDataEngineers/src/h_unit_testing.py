# Section H: Unit Testing.
#
# Unit testing is a very important topic. You want to have
# a way of testing without any manual intervention. 
#
# We're going to setup unit test structure with Pytest, 
# create some test functions, and evaluate tests in 
# command line or VSCode. 
#
# Pytest finds test files automatically, runs functions
# whose names start with test_, and reports wheter assertions
# pass or fail.

# Usually you have a the following folder structure in
# your projects:
# PROJECT
# /data
# /src
# /tests
#
# Tests should be isolated from the source code in its
# own folder. So this will all be written in the test/
# folder under test_g_json_validation.py.
# 
# Write up a pytest.ini so the tests know which folder from 
# which it ought to execute. Place it in the tests/ folder.
# Also place __init__.py in both the src and tests folders.
# It's needed in the src folder so it gets recognized as a
# package. It's needed in the tests folder so that pytest
# can discover and recognize tests in the folder.
#  
# After everything is set up, go to terminal and type:
# $ pytest
# To run the tests. 
# 
# When setting up Pytest.ini:
# [pytest]
# python_functions = test_ *_test
# So any tests with "test_" as prefix and "_test" as suffix
# will run. 

# The cool thing: one of the tests failed! 