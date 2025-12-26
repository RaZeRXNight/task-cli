from main import *
from subprocess import run
from os import getcwd

test_case = [
    ["list"],
    ["add", "thing"],
    ["mark", "0", "done"],
    ["mark", "0", "todo"],
    ["mark", "0", "in-progress"],
    ["update", "0", "forget"],
    ["update", "0", "forget"],
    ["list", "in-progress"],
    ["list", "done"],
    ["delete", "0"],
    ["update", "0", "forget"],
    ["update", "0", "forget"],
    ["update", "0", "forget"],
    ["list"],
    ["mark", "0", "done"],
    ["mark", "0", "todo"],
    ["mark", "0", "in-progress"],
    ["delete", "0"],
    ["update", "0", "forget"],
    ["list"],
]

def test():
    for test in test_case:
        try:
            run(["python3",  "main.py",  *test], cwd=getcwd())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    test()