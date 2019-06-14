# Json-to-Nested-Dictionary
Conversion of Dictionary to nested dictionaries
Given an input as json array (each element is a flat dictionary) write a program that will parse this json, and return a nested dictionary of dictionaries of arrays, with keys specified in command line arguments and the leaf values as arrays of flat dictionaries matching appropriate groups
python nest.py nesting_level_1 nesting_level_2 … nesting_level_n
For example, when invoked like this:
cat input.json | python nest.py currency country city
Please note, that the nesting keys should be stripped out from the dictionaries in the leaves.
Also please note that the program should support an arbitrary number of arguments, that is arbitrary levels of nesting.


Solution Implemented:
Script Handles 5 Data Inputs(5 Test Cases of Json Validation), single Json entry, multiple Json entry, missing key error and a Json syntax error for testing.
Script accepts input only from File so that it can process the Json according based on nesting parameters provided as arguments in command line.
Approach used to Convert Json:
1) Read json Input from file
2) Reorder each json dictionary(each element in json) based on the order of nesting mentioned
3) Nest the dictionary and print the output on Terminal

