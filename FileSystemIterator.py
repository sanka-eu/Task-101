import os
import fnmatch

#class definition
class FileSystemIterator:
	def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
		self.root = root
		self.only_files = only_files
		self.only_dirs = only_dirs
		self.pattern = pattern

		#elements of the file system
		self.files = []
		self.find_files()

		#zeroing the index
		self.index = 0

	#filling the list
	def find_files(self):
		#bypass the file system with the root directory self.root
		for root, dirs, files in os.walk(self.root):
			#only files
			if self.only_files:
				#pattern
				if self.pattern:
					self.files.extend([os.path.join(root, file) for file in files if fnmatch.fnmatch(file, self.pattern)])
				#no pattern
				else:
					self.files.extend([os.path.join(root, file) for file in files])
			#only dirs
			elif self.only_dirs:
				self.files.extend([os.path.join(root, dir) for dir in dirs])
			#files and dirs
			else:
				#pattern
				if self.pattern:
					self.files.extend([os.path.join(root, name) for name in dirs + files if fnmatch.fnmatch(name, self.pattern)])
				#no pattern
				else:
					self.files.extend([os.path.join(root, name) for name in dirs + files])
		#zeroing index
		self.index = 0

	#iterator methods
	def __iter__(self):
		return self

	def __next__(self):
		if self.index >= len(self.files):
			raise StopIteration
		item = self.files[self.index]
		self.index += 1
		return item
