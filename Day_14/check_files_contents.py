import glob, os

os.chdir("test_dir")

for file in glob.glob("*"): 

    with open (file) as current_file:
        current_file_content=current_file.read()
        if "2" in current_file_content:
             print(current_file_content)
