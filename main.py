import json
import re
import argparse


YEAR = 'year'
MONTH = 'month'
DAY = 'day'
UPDATE = 'update'
DATE = 'date'
WORDS_DICT = {'Kate Client': 'THE BACKGROUND'}
FILE_DIR = '/home/user/Downloads'
FILE_NAME = 'dataFile.json'
MODE = UPDATE
NEW_DATE_VALUE = '01'
AUTO_MODE = False
CONSOLE_MODE = True


def find_and_update(data_string, data_path, regex_pattern, substring, auto_mode):
    # Find substring in data_string and update change it
    if not data_string:
        raise ValueError('Empty string to find substring')
    if not regex_pattern:
        raise ValueError('Empty regex pattern to find substring')
    if not substring:
        raise ValueError('Empty new substring to replace')

    if re.findall(regex_pattern, data_string, re.IGNORECASE):
        print('Path: ' + data_path + '\nChange in: ' + data_string + '\nFrom: '
              + re.search(regex_pattern, data_string).string + '\nTo: ' + substring)
        if not auto_mode and input('y/n\nAnswer: ') == 'n':
            print('CONTINUE\n')
            return data_string
        data_string = re.sub(regex_pattern, substring, data_string)
        print('New string: ' + data_string + '\n')
    return data_string


def change_date(data_string, date_mode, new_value, auto_mode):
    # find date and update part of date
    if not data_string:
        return data_string
    if not date_mode:
        raise ValueError('Empty date mode')
    if not new_value:
        raise ValueError('Empty new date value')

    regex_pattern = r'\b(3[01]|[12][0-9]|0?[1-9])/(1[012]|0?[1-9])/((?:19|20)\d{2})\b'
    if re.findall(regex_pattern, data_string, re.IGNORECASE):
        old_value = data_string
        date_elements = re.split(r'/', data_string)
        if date_mode == DAY:
            date_elements[0] = new_value
        elif date_mode == MONTH:
            date_elements[1] = new_value
        elif date_mode == YEAR:
            date_elements[2] = new_value
        new_date = '/'.join(date_elements)
        if not auto_mode and input('Change from ' + old_value + ' to ' + new_date + '?\nAnswer[y/n]: ') == 'y':
            print('Changed to: ' + new_date + '\n')
            return new_date
        print('CONTINUE' + '\n')
        return old_value


def find_and_update_from_dict(json_string, json_path, convert_dict, auto_mode):
    if not json_string:
        return json_string

    for key in convert_dict:
        regex_pattern = r'\b' + key + r'\b'
        json_string = find_and_update(json_string, json_path, regex_pattern, convert_dict[key], auto_mode)
    return json_string


def read_json_file(file_dir, file_name):
    with open(file_dir + '/' + file_name) as json_file:
        data = json.load(json_file)
    return data


def write_json_file(file_dir, file_name, data):
    with open(file_dir + '/' + 'updated_' + file_name, 'w') as json_file:
        json.dump(data, json_file)


def processing_json_data(json_element, path):
    if type(json_element) is dict:
        for key in json_element:
            json_element[key] = processing_json_data(json_element[key], key)
    elif type(json_element) is list:
        for list_element in json_element:
            processing_json_data(list_element, 'list_element')
    elif type(json_element) is str:
        if MODE == 'update':
            return find_and_update_from_dict(json_element, path, WORDS_DICT, AUTO_MODE)
        if MODE == 'date':
            return change_date(json_element, DAY, NEW_DATE_VALUE, AUTO_MODE)
    return json_element


def parsing_console_args():
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('--file_dir', help="Path to dir with Json. Need use without '/'. For example: /home/data")
    args_parser.add_argument('--file_name', help="Json file name. For example: data_file.json")
    args_parser.add_argument('--auto_mode', help="Enable program auto mode.")
    args_parser.add_argument('--mode', help="Select program mode. May be: update, date.")
    args_parser.add_argument('--date_part', help="Select date part of date mode. May be: day, month, year.")
    args_parser.add_argument('--new_date_part', help="Set new date part to change date. For example: 01, 27, 2021.")
    args_parser.add_argument('--update_dict', help="Words to change. "
                                                   "Format: word_to_change:new_word,word_to_change:new_word. '_' will"
                                                   "replacing to ' ' (space).")
    args = args_parser.parse_args()

    if not args.file_dir:
        raise SystemExit('ERROR. Enter file dir. For instance: /home/user/Downloads')
    FILE_DIR = args.file_dir

    if not args.file_name:
        raise SystemExit('ERROR. Enter file name. For instance: dataFile.json')
    FILE_NAME = args.file_name

    if args.mode == UPDATE:
        if not args.update_dict:
            raise SystemExit('ERROR. Enter update dict. For instance: new_word,word_to_change:new_word')
    elif args.mode == DATE:
        if not args.date_part:
            raise SystemExit('ERROR. Enter date part. May be: day, month, year.')
        if not args.new_date_part:
            raise SystemExit('ERROR. Enter new date part value')

    for update_dict_arg in args.update_dict.replace('_', ' ').split(','):
        key_value = update_dict_arg.split(':')
        WORDS_DICT[key_value[0]] = key_value[1]

    if args.auto_update:
        AUTO_UPDATE = bool(args.auto_update)


if CONSOLE_MODE:
    parsing_console_args()
json_data = read_json_file(FILE_DIR, FILE_NAME)
processing_json_data(json_data, 'json_file')
write_json_file(FILE_DIR, FILE_NAME, json_data)
print('Done!')
