# log-parser-script
## Description
A python script that takes a list of words as input and automatically parses through all the log files in a given folder to find the lines containing those words.

## Suggested Folder Structure
```bash
└── log-parser-script
        ├── logs
        │    ├── log1.log
        │    ├── log2.log
        │    ├── log3.log
        │    └── ...   
        ├── .gitignore
        ├── log_parser.py
        ├── output.log
        └── README.md
```
## Setup
- Please delete the `example.log` file and add all your log files that you want to search inside the `logs` folder.
- On the [line 4](log_parser.py#L4) of the `log_parser.py` file, add the list of words you want to search in the log files.
    - Example: 
        ```python 
        TEXT_TO_FIND = ["word1", "word2", "word3", "word4"] # words to find inside the log files
        ``` 
- If you intend to change the folder structure, add the suitable folder path to the log files on [line 5](log_parser.py#L5) of the `log_parser.py` file
    - Example: 
        ```python 
        PATH_TO_LOGS = "path/to/logs" # path to the log files
        ``` 

## Command to Execute the Script
```bash
python log_parser.py
```

## Output
Once the script is executed, it will automatically create an `output.log` file in the same directory as `log_parser.py` file. All the lines in the log files that contain the words will be appended to the `output.log` file.