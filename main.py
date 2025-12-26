"""
The main file to handle the operations of task-cli
Modules Needed:
- os
- sys
- json
"""

import os
from sys import argv
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
        Result = Func(*argv[2:])
        
        if isinstance(Result, list):
            if not Result:
                print(f"There are {len(Result)} Tasks, Let's make some with Python3 add 'Description' ")
            else:
                print(f"There are {len(Result)} Tasks: ",*list(map(lambda x: x["description"], Result)), sep="\n\t")
            return
        
        print(Result)
        
        
    except Exception as e:
        print(e)

if __name__ == "__main__":
        main()
