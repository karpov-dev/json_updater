# JSON Updater

1. ARGS:
  DEBUG MODE
    1) True - start code with args from script
    2) False - start code with args from terminal (console)
 
  UPDATE_DICT
    1) Key - need to change word
    2) Value - new word
  
  AUTO_UPDATE
    1) True - updating words automaticly
    2) False - asks user to update each word
  
  FILE_DIR
    1) Path to dir with file (without file name)
  
  FILE_NAME
    1) JSON file name with '*.json'
    
2. CONSOLE ARGS:
  1) --file_dir - file dir without file name
  2) --file_name - json file name
  3) --update_dict - string like 'first_word_to_update:first_new_word,second_word_to_update:second_new_word' and etc. '_' will change to space (' ')
  4) --auto_update - enable auto update. May be True or False. Default - False
  
 3. DESCRIPTION:
  1) Start script
  2) Enter --file_dir, --file_name, --update_dict, --auto_update(not necessarily)
  3) Will created file updated_FILE_NAME.json
