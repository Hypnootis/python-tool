import os, shutil
# TODO: Add some tests!
data_path = "data/" # Relative path
# TODO: entrypoint for program

data_files = os.listdir(data_path)
# Data should be a pair of jpg/txt files! Maybe add support for other filetypes or remove filetype dependency
def move_files(files: list): # TODO: Make directory if it doesn't exist...
    if len(files) != 0:
        for file in files:
            if f"{file.split('.')[0]}.txt" in files and f"{file.split('.')[0]}.jpg" in files:
                if file.endswith(".jpg"): 
                    shutil.move(f"{data_path}{file}", f"images/")
                else:
                    shutil.move(f"{data_path}{file}", f"labels/")
            else:
                print(f"{file} is missing a label/image!")
                continue
        print("Finished moving files")
    else:
        print("Directory is empty!")

# Labels and images have the same name but different filetype by design
def split_files(files: list):
    copy_files = files # For getting the split version
    index = 0
    validation, train = [], []
    split_index = len(copy_files) * 0.2
    for file in copy_files:
        copy_file = file.split('.')[0]
        if copy_files.index(file) < split_index:
            shutil.move(f"images/{copy_file}.jpg", f"images/test/")
            shutil.move(f"labels/{copy_file}.txt", f"labels/test/")
        else:
            shutil.move(f"images/{copy_file}.jpg", f"images/train/")
            shutil.move(f"labels/{copy_file}.txt", f"labels/train/")
    print("Done splitting files")


move_files(data_files)

    
paska = os.listdir("images/")
kusi = os.listdir("labels/")
# Ignore the test/train folders TODO: refactor this
kusi.remove("test")
kusi.remove("train")
paska.remove("test")
paska.remove("train")
split_files(paska, "images")
split_files(kusi, "labels")