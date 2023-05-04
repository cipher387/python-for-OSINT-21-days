import glob, os, re 

regexp = re.compile('[a-zA-Z0-9-_.]+@[a-zA-Z0-9-_.]+')

os.chdir("test_dir")

for file in glob.glob("*"): 

    with open (file) as current_file:
        current_file_content=current_file.read()       
        if regexp.search(current_file_content):
            print("Math in file: "+file)
            print(current_file_content)
