import glob, os

os.chdir("test_dir")

for file in glob.glob("*.txt"): 

    with open (file) as current_file:
        print(current_file.readlines())
