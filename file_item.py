from random import choice


class FileItem:
  def __init__(self, source_path, base_name, extension, is_folder):
    self.source_path = source_path
    self.base_name = base_name
    self.extension = extension
    self.dest_path = None
    self.is_folder = is_folder

  def __str__(self):
    return f"{self.source_path}"

class FileItemCollection:
  def __init__(self):
    self.coll = {}

  def __contains__(self, item):
    return item in self.coll

  def __getitem__(self, key):
    return self.coll[key]

  def add(self, item):
    try:
      self.coll[item.base_name] = item
    except AttributeError:
      self.coll = self.coll | item.coll

  def add_all(self, fileitems):
    for fileitem in fileitems:
      self.add(fileitem)

  def file_collection(self):
    return self.coll

  def list_files(self):
    print("OHAI! MAH FILES:")
    for _, item in self.coll.items():
      print(f"{item}")

  def sort_by_basename(self):
    files_only = [basename for basename,item in self.coll.items()]
    return sorted(files_only)

  def filter_files(self, filter):
    return [basename for basename, item in self.coll.items() if re.match(filter)]

  def flag_files_for_move(self, dest_path):
    for _, item in self.coll.items():
      item.dest_path = dest_path
