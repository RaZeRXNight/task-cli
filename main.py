"""
The main file to handle the operations of task-cli
Modules Needed:
- os
- sys
- json
"""

import os
from sys import argv
from shutil import move
import time
import json
import datetime
from scripts.task import *

task_path = os.path.abspath("tasks")
if not os.path.exists(task_path):
    os.mkdir(task_path)

CMD = {
    "add": add_task,
    "update": update_task,
    "delete": delete_task,
    "mark": mark,
    "list": list_task
}

def main():
    try:
        if len(argv) < 2:
            raise Exception("ERROR: INVALID USE OF TASK-CLI, Example use ('python3 main.py add 'Do a Thing'')")
        
        if argv[1] not in CMD:
            raise Exception(f"ERROR: INVALID COMMAND ENTERED: \n\tList of Commands: {list(CMD.keys())}")
        
        Func = CMD[argv[1]]
        print(Func(*argv[2:]))
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
        main()
