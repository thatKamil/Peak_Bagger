import os, sys
import glob
import getpass


# 1. Create file on desktop called "IVIS"
# 2. Direct program to this folder    C:\Users\tksokolo1\Desktop\IVIS
# 3. Start acquisition and export csv files to this folder.
# 4. Should update automatically.
#
#
#
# username = getpass.getuser()
# print(username)
#
# newpath = r'C:\Program Files\arbitrary'
# if not os.path.exists(newpath):
#     os.makedirs(newpath)
#
# files = os.listdir("/Users/tksokolo1/Desktop/programs/IVIS_time")   # Gets a list of all files in directory
# cur = os.getcwd()   # Get current working directory
#
# list_of_files = glob.glob('/Users/tksokolo1/Desktop/programs/IVIS_time/*.csv') # * means all if need specific format then *.csv
# latest_file = max(list_of_files, key=os.path.getctime)
# print(latest_file)

# print(os.getcwd())
# os.chdir("C:\\Users\\tksokolo1\\Desktop")
# os.mkdir('PythonProjects')