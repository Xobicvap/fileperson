from pathlib import Path
from file_item import FileItem, FileItemCollection
import re
import shutil
import os

def get_file_list(dirpath, filter=""):
  p = dirpath if isinstance(dirpath, Path) else Path(dirpath) 
  coll = FileItemCollection()
  for x in p.iterdir():
    item = None
    if x.is_dir():
      subcoll = get_file_list(x, filter)
      coll.add(subcoll)
    if len(filter) > 0:
      if re.search(re.compile(filter), x.name) is not None:
        item = FileItem(str(x), x.name, x.suffix, x.is_dir())
    else:
      item = FileItem(str(x), x.name, x.suffix, x.is_dir())
    if item is not None:
      coll.add(item)
  return coll

def move_files_to_dir(coll, destpath, dry_run=False, copy=False):
  dest = Path(destpath)
  if not dest.exists():
    dest.mkdir(0o775, True)
  print(f"Going to move files! files: {coll.file_collection}")
  for basename, item in coll.file_collection().items():
    filedest = dest.joinpath(basename)
    if copy:
      shutil.copy(item.source_path, str(filedest))
    else:
      filesource = Path(item.source_path)
      filesource.rename(filedest)

def remove_files(coll, dry_run=False):
  for basename, item in coll.file_collection().items():
    print(f"Removing file {item.source_path}")
    try:
      rempath = Path(item.source_path)
      if rempath.exists():
        rempath.unlink()
      else:
        print(f"FILE AT {item.source_path} DOES NOT EXIST")
      #os.remove(item.source_path)
    except:
      print("Couldn't remove file!")

def move_mapped_files(sourcecoll, mapped_files, destroot, dry_run=False, copy=False):
  mapped_items = mapped_files.items()
  mi_iter = iter(mapped_items)
  pathmap = transform_map_to_paths(mi_iter, destroot)
  for basename, destpath in pathmap:
    if basename in sourcecoll:
      dest = Path(destpath).parent
      if not dest.exists:
        print(f"Making dir {dest.name}")
        if not dry_run:
          dest.mkdir(0o775, True)
      if copy:
        print(f"Copying {sourcecoll[basename].source_path} to {destpath}")
        if not dry_run:
          shutil.copy(sourcecoll[basename].source_path, destpath)
      else:
        print(f"Moving {sourcecoll[basename].source_path} to {destpath}")
        if not dry_run:
          filesource = Path(sourcecoll[basename].source_path)
          filesource.rename(Path(destpath))
  
def transform_map_to_paths(mi_iter, current_path=""):
  looping = True
  pathmap = {}
  while looping:
    try:
      dirname, subitem = next(mi_iter)
      if isinstance(subitem, List):
        for filename in subitem:
           pathmap[filename] = str(Path(current_path).joinpath(dirname).joinpath(filename))
      elif isinstance(subitem, Dict):
        pathmap = transform_map_to_paths(iter(subitem), str(Path(current_path).joinpath(dirname)))
    except StopIteration:
      looping = False
  return pathmap




"""
    fileitem = Path(item.source_path)
    if fileitem.exists():
      print(f"FILE EXISTS BEFORE? {fileitem.exists()}")
      os.remove(item.source_path)
      print(f"FILE EXISTS? {fileitem.exists()}")
    else:
      print(f"Cannot remove file {item.source_path}")
"""
