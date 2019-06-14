from collections import OrderedDict
import json
import sys
import argparse

#Reordering of the Dictionary based on Nesting Order provided
def reorder(jsn_lst,nest_indexlst):
    reordered_dic=OrderedDict()
    nest_leaf = [key for key, value in jsn_lst.items() if key not in nest_indexlst]
    nest_indexlst.extend(nest_leaf)
    for index,key in enumerate(nest_indexlst):
        try:
            reordered_dic[key]=jsn_lst[key]
        except KeyError:
            print("Missing Key in Json file, please correct it..Key missing",key)
            sys.exit(0)
    return reordered_dic

#Recursive Function to Create Nested Dictionary
def dict_factory(lst):
    if len(lst) == 2:
        return {lst[0][1]: [{lst[1][0]:lst[1][1]}]}
    else:
        return {lst[0][1]: dict_factory(lst[1:])}

#Function to traverse the dictionary and create nested dictionary
def nest_creation(dict,nest):
    nested_dicts={}
    for item in dict:
        reordered_json = (reorder(item, nest))
        json_values = list(reordered_json.items())
        nested_dict = dict_factory(json_values)
        nested_dicts.update(nested_dict)
    print(json.dumps(nested_dicts,indent=2))

if __name__=='__main__':

    parser = argparse.ArgumentParser(description='Parsing a JSON to return nested dictionary of dictionaries of array ',add_help=False)
    parser.add_argument('arguments', nargs='+', help='nesting order')
    args = parser.parse_args()
    # Read Input Json from File input
    for line in sys.stdin:
        try:
            json_data=json.loads(line.rstrip())
        except (IOError,EOFError,FileNotFoundError):
            print("Error: File does not appear to exist.")
            sys.exit(0)
        except (json.decoder.JSONDecodeError):
            print("File has ended, all jsons have been processed")
            sys.exit(0)
#Get the list of arguments
        for key,value in vars(args).items():
            Nest_Order=value
#Calls the function to Nest the Json
        try:
            output=nest_creation(json_data,Nest_Order)
        except (NameError, IOError, TypeError, SyntaxError):
            print("Error: Parsing of Json has failed for following json data\n",json_data)