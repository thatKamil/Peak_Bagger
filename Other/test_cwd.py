import os

cwd = os.getcwd()

newpath = r(cwd)
if not os.path.exists(newpath):
    os.makedirs(newpath)

input('Press ENTER to exit')