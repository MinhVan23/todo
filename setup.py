#!/usr/bin/python3

import sys
import os
import shutil
import subprocess

todo_path = os.path.expanduser('~/todo')

def install():
    if os.path.exists('/usr/local/bin/todo'):
        print('Error: Todo is already installed.')
        exit(1)
    subprocess.run(['sudo', 'cp', 'todo.py', '/usr/local/bin/todo'])
    os.mkdir(todo_path)
    file = open(os.path.join(todo_path, 'task_list.txt'), 'w')
    file.close()
    print('Todo is installed successfully!')

def uninstall():
    subprocess.run(['sudo', 'rm', '/usr/local/bin/todo'])
    shutil.rmtree(todo_path)
    print('Todo is uninstalled successfully.')
    
option = sys.argv[1]
if option == '--install':
    install()
elif option == '--uninstall':
    uninstall()
else:
    print('Error: Unknown command.')
    exit(1)