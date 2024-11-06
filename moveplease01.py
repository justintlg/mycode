#!/usr/bin/python3

import shutil
import os

def main():

    #change to that directory
    os.chdir('/home/student/mycode')

    #moves file/folder to destination(file/folder, destination)
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompts for new name and saves as xname
    xname = input('What is the new name for kerrigan.obj? ')

    #renames file to above value
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
