
bucket_max = 10
bucket_name_part_max = 4

ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyz"

def arrange_command(filenames):
  return subdivide_alpha_buckets(arrange_in_alphabetical_buckets(filenames))

def arrange_in_alphabetical_buckets(filenames):
  alpha_buckets = {}
  for filename in filenames:
    alpha_idx = ALPHANUMERIC.index(filename[0])
    c = ALPHANUMERIC[alpha_idx]
    if c not in alpha_buckets:
      alpha_buckets[c] = []
    alpha_buckets[c].append(filename)
  return alpha_buckets

def subdivide_alpha_buckets(alpha_buckets):
  subdivided = {}
  for c in ALPHANUMERIC:
    current_list = alpha_buckets[c]
    subdivided[c] = arrange_in_buckets(current_list)
  return subdivided

def group_by_similar_name(filenames):
  file_len = len(filenames)
  i = 0
  file_map = {}
  while i < file_len:
    current_file = filenames[i]
    folder_name = current_file[:-1]
    group = True
    while group:
      if i == file_len - 1:
        group = False
      next_file = filenames[i+1]
      if next_file[:-1] == folder_name:
        if folder_name not in file_map:
          file_map[folder_name] = []
        if current_file not in file_map[folder_name]:
          file_map[folder_name].append(current_file)
        file_map[folder_name].append(next_file)
      else:
        group = False
      i += 1
  return file_map

def strip_text_from_files(filenames, text):
  stripping = {}
  for filename in filenames:
    if text in filename:
      stripping[filename] = filename.replace(text, "")
  return stripping

def arrange_in_buckets(filenames):
  list_len = len(filenames)
  bucketed = {}
  i = 0
  while i < list_len:
    bucket = filenames[i:i+bucket_max]
    bucket_name_first = bucket[0][:bucket_name_part_max]
    if bucket_max - 1 >= len(bucket):
      bucket_name_last = bucket[-1][:bucket_name_part_max]
    else:
      bucket_name_last = bucket[bucket_max-1][:bucket_name_part_max]
    bucket_name = bucket_name_first + "-" + bucket_name_last
    bucketed[bucket_name] = bucket
    i = i + bucket_max
  return bucketed



