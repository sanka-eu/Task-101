import sys
sys.path.append("../")

from fileSystemIteratorClass import FileSystemIterator

FSI = FileSystemIterator.FileSystemIterator

for item in FSI("../", False, False, None):
    print(item)
 
print("################################")
 
print(next(FSI("../", False, False, None)))
