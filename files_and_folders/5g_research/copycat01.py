#!/usr/bin/env python3

import shutil
import os

# change to the base dir
os.chdir("/home/student/mycode/files_and_folders")

# copy the sdn_network.txt file to "".copy
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copy the entire directory 
shutil.copytree("5g_research/", "5g_research_backup/")


