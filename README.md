# Test-train splitter

## What?
A small script that splits a folder with image-label pairs into their own folders, complete with splitting them further into test/train categories (a 20/80 split specifically)


## Why?
You've perhaps used a tool like [YOLO_Label](https://github.com/developer0hye/Yolo_Label) to label your image datasets in preparation for using them with various machine learning applications. With some example applications, they expect a certain structure for the dataset, and having your images and labels in the same folder is usually not it!

#### Expectation:
```
dataset/
  images/
      train/
      test/
  labels/
      train/
      test/
```
#### Reality:
```
dataset/
```
Splitting the files manually is a hassle, how much is 20% of 1552 anyway?

## How?
Drop the splitter.py file to the parent directory of your dataset directory and run it with the directory's name as an argument:
```
python3 splitter.py mydatasetdirectory
```
This creates the expected directory structure in the parent directory as mentioned above and moves your files in to their respective folders

## Note:
* Use at your own risk! No guarantees that this will fix your truck or bring your dog back!
* Labels have to be .txt, images can be whatever
* All data should be in one large directory
* Modify the test/train split by modifying the decimal in the split_files() function, where the comment tells you to
* It splits from the start, meaning the first 20% is moved into test and the remaining 80% is moved into train
* Only tested with ~10 images and labels, as well as with ~1700 images and labels thus far
