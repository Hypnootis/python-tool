import os, shutil, sys

def main():
    try:
        data_path = sys.argv[1]
        data_files = os.listdir(data_path)
        
        create_folders()
        move_files(data_files, data_path)
    
        images_folder = os.listdir("images/")
        labels_folder = os.listdir("labels/")
        # Ignore the test/train folders TODO: refactor this
        images_folder.remove("test")
        images_folder.remove("train")
        labels_folder.remove("test")
        labels_folder.remove("train")
        split_files(images_folder)
        split_files(labels_folder)


    except IndexError:
        print("No data folder argument was given!")
 
def create_folders():
    try:
        os.makedirs("images/test")
        os.makedirs("images/train")
        os.makedirs("labels/test")
        os.makedirs("labels/train")
    except FileExistsError as e:
        print(e)

def move_files(files: list, path: str):
    copied_files = files # For popping purposes
    if len(copied_files) != 0:
        for file in copied_files:
            if f"{file.split('.')[0]}.txt" in files:
                if file.endswith(".txt"): 
                    shutil.move(f"{path}/{file}", f"labels/")
                else:
                    shutil.move(f"{path}/{file}", f"images/")
            else:
                print(f"{file} is missing a label/image!")
                continue

        print("Finished moving files")
    else:
        print("Directory is empty!")

# Labels and images have the same name but different filetype by design
def split_files(files: list):
    copy_files = files # For getting the split version
    split_index = len(copy_files) * 0.2 # Move 20% of the files for testing
    for file in copy_files:
        split_file = file.split('.')[0]
        if copy_files.index(file) < split_index:
            shutil.move(f"images/{file}", f"images/test/")
            shutil.move(f"labels/{split_file}.txt", f"labels/test/")
        else:
            shutil.move(f"images/{file}", f"images/train/")
            shutil.move(f"labels/{split_file}.txt", f"labels/train/")
    print("Done splitting files")

if __name__ == "__main__":
    main()