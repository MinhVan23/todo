#!/usr/bin/python3

import sys
import os

data_dir = os.path.expanduser('~/todo')
task_list = os.path.join(data_dir, 'task_list.txt')

def add(task):
    file = open(task_list, 'a')
    file.write(task + '\n')
    file.close()
    print('Added "' + task + '" to the list!', sep='')

def check(task):
    file = open(task_list, 'r')
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    if task not in lines:
        print('Error: Task "'+task+'" doesn\'t exist')
        exit(1)
    file = open(task_list, 'w')
    for line in lines:
        if line == task:
            continue
        file.write(line)
    file.close()
    print('Check "' + task + '" off the list!', sep='')

def _list():
    print('Task list:')
    file = open(task_list, 'r')
    print(file.read())
    file.close()

def help():
    print(
	    'commands:\n'
        '   add:        add a new task to task list\n'
        '   check:      check a task off the list\n'
        '   list:       list the tasks in task list\n'
        '   help:       print this help list'
    )

def main():
    command = sys.argv[1]
    if command == 'add':
        task = sys.argv[2]
        add(task)
    elif command == 'check':
        task=sys.argv[2]
        check(task)
    elif command == 'list':
        _list()
    elif command == 'help':
        help()
    else:
        print('Error: Unknown command.')
        exit(1)

if __name__ == '__main__':
    main()