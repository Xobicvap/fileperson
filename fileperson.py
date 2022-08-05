import command_loader
import sys

if len(sys.argv) != 2:
  json_file = "commands.json"
else:
  json_file = sys.argv[1]

print(f"LOADING {json_file}")
orch = command_loader.load_json(json_file)

orch()
