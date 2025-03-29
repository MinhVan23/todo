#!/usr/bin/python3

import sys
import os
import shutil
import subprocess

script_path = os.path.abspath(sys.argv[0])
src_path = os.path.join(os.path.dirname(script_path), 'todo.py')
todo_path = os.path.expanduser('~/todo')

def install():
    if os.path.exists('/usr/local/bin/todo'):
        print('Error: Todo is already installed.')
        return
    subprocess.run(['sudo', 'cp', src_path, '/usr/local/bin/todo'])
    print('Install todo to /user/local/bin.')
    os.mkdir(todo_path)
    with open(os.path.join(todo_path, 'task_list.txt'), 'w') as file:
        pass
    print(f'Create folder to store user\'s data at {todo_path}')
    print('Todo is installed successfully!')

def uninstall():
    if not os.path.exists('/usr/local/bin/todo'):
        print('Error: Todo is not installed.')
        return
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