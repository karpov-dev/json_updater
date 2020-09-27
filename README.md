# JSON Updater
This script contains two modes. First mode called "update". Second mode called "date" 
Update mode find substring or word in string and change substring to new substring.
Date mode find date with "dd/mm/yyyy" format, divide date and change part of date to new value.
You can start script from IDE or from terminal. To start script from IDE you should change constant "CONSOLE MODE" to False, to start from terminal - True.
    Terminal args:
        --file_dir - Path to json dir. Need use without '/'. For instance: /home/jsonFiles.
        --file_name - Json file name. For example: data_file.json.
        --auto_mode - Enable script auto mode. Script will work automaticly. May be: True, False. Default - False.
        --mode - Select script mode. May be: update, date.
        --date_part - Select date part to date mode. May be: day, month, year.
        --new_date_part - New date part value. For instance: 01, 28, 2007.
        --update_dict - Need for update mode. Format: word_to_change:new_word,word_to_change:new_word. '_' will change to ' ' (space).
    Date mode steps from Terminal:
        1) for day: python3 main.py --file_dir /home/data --file_name data_file.json --mode date --date_part day --new_date_part 01
        2) for month: python3 main.py --file_dir /home/data --file_name data_file.json --mode date --date_part month --new_date_part 01
        3) for year: python3 main.py --file_dir /home/data --file_name data_file.json --mode date --date_part year --new_date_part 2007
        4) for month automaticly: python3 main.py --file_dir /home/data --file_name data_file.json --mode date --date_part month --new_date_part 01 --auto_mode True
    Date mode steps from IDE:
        1) Open main.py 
        2) Change Console_mode from True to False
        3) Set FILE_DIR 
        4) Set FILE_NAME
        5) Set MODE to DATE 
        6) Set NEW_DATE_VALUE
        7) Start script
        8) If need change AUTO_MODE
    Update mode steps from Terminal:
        1) python3 main.py --file_dir /home/data --file_name data_file.json --mode update --update_dict Kate_Client:Robert_Test,test:TEST
    Update mode from IDE:
        1) Set FILE_DIR
        2) Set FILE_NAME
        3) Change CONSOLE_MODE from True to False
        4) Fill WORDS_DICT. Key - value to find, Value - new value
