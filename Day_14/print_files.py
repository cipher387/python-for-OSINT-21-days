import glob, os

os.chdir("test_dir")


print ("TXT files")
for file in glob.glob("*.txt"): 
    print(file)

print ("ALL files")
for file in glob.glob("*"): 
    print(file)
