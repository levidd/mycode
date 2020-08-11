#!/usr/bin/env python3

import shutil
import os

# change to base dir
os.chdir('/home/student/mycode/files_and_folders')

# move raynor obj to ceph_storage
shutil.move('raynor.obj', 'ceph_storage/')

# get new filename
xname = input('What is the new name for kerrigan.obj? ')

# change kerrigan.obj to xname.obj
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


