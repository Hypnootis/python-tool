import os, shutil, random

data_path = "data/" # Relative path

data_files = os.listdir(data_path)

new_file = {"name": "", "type": ""} # Type is 'test' or 'train'

# Split is for test/train, i.e. a value of 0.8 means a 80/20 split
def move_files(files: list):
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

        # sorted_file = {"name": file, "type": ""}    


def split_files(files: list, destination: str):
    # Split files
    index = 0
    validation, train = [], []
    # split_index = int(random.randint(0, len(files) - (len(files) * 0.2) )) # TODO: Don't assume that each file has a pair
    split_index = len(files) * 0.2
    for file in files:
        if files.index(file) < split_index:
            shutil.move(f"{destination}/{file}", f"{destination}/test/")
            print(f"Moved {file} to test")
        else:
            shutil.move(f"{destination}/{file}", f"{destination}/train/")
            print(f"Moved {file} to train")


move_files(data_files)

    
paska = os.listdir("images/")
kusi = os.listdir("labels/")
kusi.remove("test")
kusi.remove("train")
paska.remove("test")
paska.remove("train")
print(paska)
split_files(paska, "images")
split_files(kusi, "labels")