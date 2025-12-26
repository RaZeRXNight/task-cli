"""
Script for managing tasks in the command line.

- Add task
- Update task
- Mark task
- Delete task

- list tasks Status'
"""

import os
from shutil import move
import time
import json
import datetime

task_path = os.path.abspath("tasks")
STATUS = [None, "done", "todo", "in-progress"]
task_template = {
    "id": 0,
    "description": "desc",
    "status": "todo",
    "created_at": "",
    "updated_at": ""
}

def add_task(desc="") :
    file_path = os.sep.join([task_path, f"{str(desc)}.json"])
    cur_id = 0
    
    Tasks_ID = list(map(lambda x: x["id"], list_task()))
    
    if Tasks_ID:
        cur_id = max(Tasks_ID) + 1
    
    if not desc:
        raise Exception(f"ERROR: {desc} is an invalid name")
    
    if os.path.exists(file_path):
        raise FileExistsError(f"ERROR: {desc} Task already exists.")

    with open(file_path, "w") as file:
        task = task_template.copy()
        task["id"] = cur_id
        task["description"] = desc
        task["created_at"] = time.ctime(os.path.getctime(file_path))
        task["updated_at"] = time.ctime(os.path.getmtime(file_path))
        json.dump(task, file)
        return f"Added {desc}#{cur_id}"

def update_task(id, desc):
    if isinstance(id, str):
        if not id.isdigit():
            raise Exception("ERROR: ENTER A VALID ID")
        else:
            id = int(id)
    
    if not desc:
        raise Exception("ERROR: INVALID DESCRIPTION")
    
    task_list = list(filter(lambda x: x["id"] == id, list_task()))
    
    if len(task_list) > 1:
        list(map(lambda x: print(os.path.join([task_path, x])), task_list))
        raise Exception(f"ERROR: DUPLICATE ENTRIES of ID {id}")
    
    if task_list:
        task = task_list[0]
        
        if task["description"] == desc:
            return f"{task["id"]} is already {desc}"
        
        file_name = f"{task["description"]}.json"
        new_file_name = f"{str(desc)}.json"
        file_path = os.path.sep.join([task_path, file_name])
        new_file_path = os.path.sep.join([task_path, new_file_name])
        
        move(file_path, new_file_path)
        with open(new_file_path, "w") as file:
            task["description"] = str(desc)
            task["updated_at"] = datetime.datetime.now().ctime()
            json.dump(task, file)
            return f"Changed ID {id}'s Description to {desc}"
            
    return f"Unable to change ID {id}'s description to {desc}"

def delete_task(id):
    file_list = os.listdir(task_path)
    if id == "_":
        sentinel = ""
        while sentinel not in ["y", "n"]:
            sentinel = input("Are you sure you want to delete every task? (y/n) ").lower()
        
        if sentinel == "y":
            list(map(lambda x: os.remove(os.sep.join([task_path, x])), file_list))
            return f"Deleted Every JSON in {task_path}"
        return 
    else:
        for i in file_list:
            file_path = os.sep.join([task_path, i])
            with open(file_path, "r") as f:
                file_json = json.load(f)
                if file_json["id"] == int(id):
                    os.remove(file_path)
                    return f"Deleted {file_path} Task. "
        
        return f"Unable to find ID {id} in {task_path}, please try another id."

def mark(id, status):
    if isinstance(id, str):
        if not id.isdigit():
            raise Exception("ERROR: ENTER A VALID ID")
        else:
            id = int(id)
    
    if status is None:
        raise Exception("ERROR: No Status Given")
    
    if status not in STATUS:
        raise Exception(f"ERROR: INVALID STATUS GIVEN.\t\n EG. {STATUS}")
    
    task_list = list(filter(lambda x: x["id"] == id, list_task()))
    
    if len(task_list) > 1:
        list(map(lambda x: print(os.path.join([task_path, x])), task_list))
        raise Exception(f"ERROR: DUPLICATE ENTRIES of ID {id}")
    
    if task_list:
        task = task_list[0]
        current_status = task["status"]
        task["status"] = status
        
        if current_status == status:
            return f"{task["id"]} is already {status}"
        
        file_path = os.path.sep.join([task_path, f"{task["description"]}.json"])
        with open(file_path, "w") as file:
            json.dump(task, file)
        
        return f"Changed ID {task["id"]} from {current_status} to {status}"
    
    return f"Unable to change ID {id}'s status to {status}, it may already be {status} or unavailable."

def list_task(status=None):
    if status not in STATUS:
        raise Exception(f"ERROR: INVALID STATUS GIVEN.\t\n EG. {STATUS}")
    
    tasks = list(filter(lambda x: x.split(os.extsep)[-1] == "json", os.listdir(task_path)))
    
    for i in tasks:
        file_path = os.sep.join([task_path, i])
        with open(file_path, "r") as f:
            tasks[tasks.index(i)] = json.load(f)
    
    if status is None:
        return tasks
    return list(filter(lambda x: x["status"] == status, tasks))
