#!/usr/bin/python3

import sys
import os

data_dir = os.path.expanduser('~/todo')
task_list = os.path.join(data_dir, 'task_list.txt')

def task_exists(task):
    tasks = []
    with open(task_list, 'r') as file:
        tasks = file.readlines()
    if f'[ ] {task}\n' in tasks or f'[x] {task}\n' in tasks:
        return True
    return False

def task_completed(task):
    tasks = []
    with open(task_list, 'r') as file:
        tasks = file.readlines()
    if f'[x] {task}\n' in tasks:
        return True
    return False

def add(task):
    if task_exists(task):
        print(f'Error: "{task} already exists.')
        return

    with open(task_list, 'a') as file:
        file.write(f'[ ] {task}\n')
    print(f'Added "{task}" to todo list.') 

def complete(task):
    if not task_exists(task):
        print(f'Error: "{task} doesn\'t exist.')
        return
    if task_completed(task):
        print(f'Error: "{task}" is already marked as completed.')
        return

    lines = []
    updated_lines = []
    with open(task_list, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == f'[ ] {task}':
            line = f'[x] {task}'
        updated_lines.append(line + '\n')

    with open(task_list, 'w') as file:
        file.writelines(updated_lines)

    print(f'Mark "{task}" as completed!')

def remove(task):
    if not task_exists(task):
        print(f'Error: "{task} doesn\'t exist.')
        return

    lines = []
    updated_lines = []
    with open(task_list, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line == f'[ ] {task}' or line == f'[x] {task}':
            continue
        updated_lines.append(line + '\n')

    with open(task_list, 'w') as file:
        file.writelines(updated_lines)

    print('Remove task "' + task + '" from the list.')


def _list():
    print('Task list:')
    with open(task_list, 'r') as file:
        print(file.read())

def help():
    print(
	    'commands:\n'
        '   add:        add a new task to task list\n'
        '   complete:   mark a task as completed\n'
        '   remove:     remove a task off the list\n'
        '   list:       list the tasks in task list\n'
        '   help:       print this help list'
    )

def main():
    command = sys.argv[1]
    task = sys.argv[2] if len(sys.argv)>2 else None
    if command in ('add', 'complete', 'remove') and not task:
        print(f'Error: no task specified for {command}.')
        return

    if command == 'add':
        add(task)
    elif command == 'complete':
        complete(task)
    elif command == 'remove':
        remove(task)
    elif command == 'list':
        _list()
    elif command == 'help':
        help()
    else:
        print('Error: Unknown command.')
        return

if __name__ == '__main__':
    main()