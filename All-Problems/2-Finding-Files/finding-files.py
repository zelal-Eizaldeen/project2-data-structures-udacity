## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

def find_files(suffix, path):
  if suffix == '':
    return []
  if len(os.listdir(path)) == 0:
    return []

  path_elements = os.listdir(path)
  path_files = [file for file in path_elements if ('.' + suffix) in file]
  path_folder = [folder for folder in path_elements if '.' not in folder]

  for folder in path_folder:
    path_files.extend(find_files(suffix=suffix, path=path + '/' + folder))
  return path_files


# Tests
path_base = os.getcwd() + '/testdir'
print(f"PATH ONE: {find_files(suffix='c', path=path_base)}")
path2 = os.getcwd() + '/testdir/subdir1'
print(f"PATH TWO: {find_files(suffix='c', path=path2)}")


