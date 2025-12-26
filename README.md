# task-cli
Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need to do, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

## Features

This project allows you to manage, create and delete tasks.  Each of which are stored in jsons within the task-cli/tasks folder.  Here are the following things you're able to do:
- Add, Update, and Delete tasks
- Mark a task as in progress or done
- List all tasks
- List all tasks that are done
- List all tasks that are not done
- List all tasks that are in progress

## How to use

### Listing all tasks
- python3 main.py list

### Listing tasks by status
- python3 main.py list done
- python3 main.py list todo
- python3 main.py list in-progress

### Adding a new task
- python3 main.py add "Buy groceries"

### Updating and deleting tasks
- python3 main.py update 1 "Buy groceries and cook dinner"
- python3 main.py delete 1

### Marking a task as in progress or done
- python3 main.py mark-in-progress 1
- python3 main.py mark-done 1


## References
- https://roadmap.sh/projects/task-tracker