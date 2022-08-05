"""
from commands.filename_commands import *
from commands.file_manip_commands import *
from commands.zip_commands import *
"""
import commands.filename_commands as fc
import commands.file_manip_commands as fmc
import commands.zip_commands as zc

"""
commands_map = {
  "arrange_in_buckets": filename_commands.arrange_command,
  "group_by_similar_name": filename_commands.group_by_similar_name,
  "strip_text": filename_commands.strip_text_from_files,
  "get_file_list": file_manip_commands.get_file_list,
  "move_mapped_files": file_manip_commands.move_mapped_files,
  "unzip_files": zip_commands.unzip_files_in_dir
}
"""

commands_map = {
  "arrange_in_buckets": fc.arrange_command,
  "group_by_similar_name": fc.group_by_similar_name,
  "strip_text": fc.strip_text_from_files,
  "get_file_list": fmc.get_file_list,
  "move_mapped_files": fmc.move_mapped_files,
  "move_files_to_dir": fmc.move_files_to_dir,
  "remove_files": fmc.remove_files,
  "unzip_files": zc.unzip_files_in_dir
}
