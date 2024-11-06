#!/usr/bin/python3


import shutil
import os

def main():
    
    #changes to that directory
    os.chdir('/home/student/mycode/')
    
    #copies file(source, new)
    shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
    
    #copies directory(source, new)
    shutil.copytree('5g_research/', '5g_research_backup/')


main()

