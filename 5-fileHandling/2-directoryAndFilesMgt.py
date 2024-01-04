import shutil
import os

# get current working directory
print(os.getcwd)

# change directory
os.chdir("home/samson_githinji")

# list directories
os.listdir()
os.listdir("home/samson_githinji")

# make new directory
os.mkdir("test")

# rename existing directory
os.rename("test", "newTest")

# remove file or directory
os.remove("testFile.txt")  # file
os.rmdir("test")  # empty directory

# remove non-empty directory
shutil.rmtree("test")
