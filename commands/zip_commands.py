import zipfile
from file_item import FileItemCollection

zip_file_types = [".zip", ".7z"]

def unzip_files_in_dir(coll, zip_file_dir, dry_run=False):
  if isinstance(dry_run, FileItemCollection):
    coll = dry_run
    dry_run = False

  for basename, file_item in coll.file_collection().items():
    print(f"FILE ITEM: {file_item}")
    if file_item.is_folder or file_item.extension not in zip_file_types:
      continue
    if file_item.extension == ".zip":
      with zipfile.ZipFile(file_item.source_path, 'r') as zipped:
        print(f"ZIP FILE CONTENTS: {zipped.infolist()}")
        if not dry_run:
          zipped.extractall(zip_file_dir)
        print(f"Extracted {file_item.source_path} to {zip_file_dir}")



