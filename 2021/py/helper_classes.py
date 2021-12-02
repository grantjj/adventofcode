from collections import defaultdict


class DataFile:

	def __init__(self, path=None):
		self.body = None
		if path is not None:
			self.path = path

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._filetype = path[path.rfind('.')+1:]
		self._path = path

	@property
	def filetype(self):
		return self._filetype

	@filetype.setter
	def filetype(self, filetype):
		self._filetype = filetype


class DataStore:
	'''
	Class to define a data store helper, to read in data
	You'll need to define a file object (DataFile) prior to using, or you can register it to the
	catalog and then pass that around
	'''

	def __init__(self):
		self._catalog = defaultdict(DataFile)

	def register_file(self, path):
		self._catalog[path] = DataFile(path)
		return self._catalog[path]

	def get(self, file_obj):

		if file_obj.filetype == 'txt':
			print("Ingesting file as txt")
			with open(file_obj.path, 'rb') as f:
				body = f.read()

		return body
