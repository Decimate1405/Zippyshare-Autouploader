import os
import shlex
import time
import subprocess
import sys
import shutil
from ast import literal_eval
from random import choice
from getpass import getpass

script_dir = os.path.dirname(os.path.realpath(__file__))
links_dir = os.path.join(script_dir, 'links')
archive_dir = os.path.join(script_dir, 'archives')
logdir = os.path.join(script_dir, 'chromedriver_log')

print('Zippylinks by DeciMat3.')
print('')
input_folders = input('List of Path(s) to folders/files for upload. (gets auto-split with rar) (format like this: ["/path/to1", "/path/to2"]: ')
input_folders = literal_eval(input_folders)
if not isinstance(input_folders, list):
    sys.exit('Wrong format for input folders!')

delete_flag = input('Delete files when done? (input folder too) (y/n): ')
if delete_flag != 'y' and delete_flag != 'n':
    sys.exit('Invalid option!')
if delete_flag == 'y':
    delete_flag = True
else:
    delete_flag = False

def random_text(length):
    return ''.join([choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(length)])

def getBasePath(folder):
    # format folder
    cwd = os.getcwd()
    if "\\" in cwd:
        if folder[-1] != "\\":
            folder = folder+"\\"
    if "/" in cwd:
        if folder[-1] != "/":
            folder = folder+"/"
    count0 = 0
    foldertrigger = False
    for x in folder[::-1]:
        count0 -= 1
        if x == "\\" or x == "/":
            if foldertrigger:
                break
            foldertrigger = True
    index = count0+len(folder)
    folder_basename = folder[index:].replace("\\", "/")
    return folder_basename

for input_folder in input_folders:

    archive_specific_dir = os.path.join(archive_dir, random_text(14))
    os.mkdir(archive_specific_dir)

    links_file_dir = os.path.join(
        links_dir, getBasePath(input_folder).replace('/', ''))+'.LINKS_'+random_text(5)+'.txt'

    # rar-ing
    args1 = ['rar', 'a', '-m0', '-v500m', os.path.join(
        archive_specific_dir, getBasePath(input_folder).replace('/', '')), input_folder]
    rar_process = subprocess.Popen(args1, stdout=sys.stdout, stderr=sys.stderr)
    exit_code = rar_process.wait()

    #plowup
    if os.path.isdir(input_folder):
    	args2 = 'plowup zippyshare '+archive_specific_dir+'/*'+' > '+links_file_dir
    else:
        args2 = 'plowup zippyshare '+archive_specific_dir +' > '+links_file_dir
    #args2 = shlex.split(args2)
    print('running', args2)
    up_p = subprocess.Popen(args2, shell=True, stdout=sys.stdout, stderr=sys.stderr)
    exit_code2 = up_p.wait()
    print('Upload done, links saved to', links_file_dir)

    if delete_flag:
        print('Deleting files...')
        subprocess.check_call(['sudo','chmod', '777', input_folder])
        shutil.rmtree(archive_specific_dir)
        try:
            shutil.rmtree(input_folder)
        except NotADirectoryError:
            os.remove(input_folder)
input("All done! Press ENTER to exit")
