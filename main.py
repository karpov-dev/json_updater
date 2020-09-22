import json
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--file_dir', help='Path to JSON file')
parser.add_argument('--file_name', help='JSON file name')
parser.add_argument('--update_dict', help='word_to_change:new_word,word_to_change:new_word')
parser.add_argument('--auto_update', help='True or False. Auto change words or manual changing. Default - manual')
args = parser.parse_args()


if not args.file_dir:
    raise SystemExit('ERROR. Enter file dir.')
FILE_DIR = args.file_dir

if not args.file_name:
    raise SystemExit('ERROR. Enter file name.')
FILE_NAME = args.file_name

if not args.update_dict:
    raise SystemExit('ERROR. Enter update dict.')

UPDATE_DICT = {}
for update_dict_arg in args.update_dict.replace('_', ' ').split(','):
    key_value = update_dict_arg.split(':')
    UPDATE_DICT[key_value[0]] = key_value[1]

AUTO_UPDATE = False


def find_usages(json_data, path):
    if type(json_data) is dict:
        for key in json_data:
            find_usages(json_data[key], key)
    elif type(json_data) is list:
        for list_element in json_data:
            find_usages(list_element, 'list_element')
    elif type(json_data) is str:
        for element_to_update in UPDATE_DICT:
            if re.findall(r'\b' + element_to_update + r'\b', json_data, re.IGNORECASE):
                print('Word: ' + element_to_update + '\nPath: ' + path + '\nValue: ' + json_data)
                if AUTO_UPDATE:
                        json_data = json_data.replace(element_to_update, UPDATE_DICT[element_to_update])
                else:
                    if input('Change to: ' + UPDATE_DICT[element_to_update] + '?\ny/n\nAnswer: ') == 'y':
                        json_data = json_data.replace(element_to_update, UPDATE_DICT[element_to_update])
                        print('New value: ' + json_data)
                print('_________________________________________________________________________________')


with open(FILE_DIR + '/' + FILE_NAME) as file:
    json_data = json.load(file)
find_usages(json_data, 'main')
