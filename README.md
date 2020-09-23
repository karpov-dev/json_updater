# json_updater

ARGS:
  DEBUG MODE
    True - start code with args from script
    False - start code with args from terminal (console)
 
  UPDATE_DICT
    Key - need to change word
    Value - new word
  
  AUTO_UPDATE
    True - updating words automaticly
    False - asks user to update each word
  
  FILE_DIR
    Path to dir with file (without file name)
  
  FILE_NAME
    JSON file name with '*.json'
    
CONSOLE ARGS:
  --file_dir - file dir without file name
  --file_name - json file name
  --update_dict - string like 'first_word_to_update:first_new_word,second_word_to_update:second_new_word' and etc. '_' will change to space (' ')
  --auto_update - enable auto update. May be True or False. Default - False
  
 DESCRIPTION:
  1) Start script
  2) Enter --file_dir, --file_name, --update_dict, --auto_update(not necessarily)
  3) Will created file updated_FILE_NAME.json
