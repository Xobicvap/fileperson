from command import *
from command_map import commands_map
from condition_map import conditions_map
import json

loop_types = ["until", "while"]

def load_command_json(json_file):
  with open(json_file, "r") as command_file:
    command_json = json.load(command_file)
    return command_json

def loop_error():
  raise Exception("Loop needs command_queue and condition")

def load_json(json_file="commands.json"):
  command_json = load_command_json(json_file)
  command_units_list = command_json["orchestrator"]
  print(f"COMMAND UNITS LIST: {command_units_list}")
  command_units = []
  command_unit = None
  for command_unit_map in command_units_list:
    print(f"COMMAND UNITS MAP: {command_unit_map}")
    if "command_queue" in command_unit_map:
      print("GETTING COMMAND QUEUE")
      command_unit = load_command_queue(command_unit_map["command_queue"])
    else:
      for loop_type in loop_types:
        if loop_type in command_unit_map:
          command_unit = load_loop(command_unit_map[loop_type], loop_type)
    command_units.append(command_unit)
  return Orchestrator(command_units)

def load_loop(loop_map, loop_type):
  if "command_queue" in loop_map:
    command_queue = load_command_queue(loop_map["command_queue"])
  else:
    loop_error()

  if "condition" in loop_map:
    condition = load_condition(loop_map["condition"])
  else:
    loop_error()

  return Loop(loop_type, command_queue, condition)

def load_condition(condition_json_map):
  predicate = conditions_map[condition_json_map["condition_type"]]
  arg_source = condition_json_map["arg_source"]
  return Condition(predicate, arg_source)

def load_command_queue(commands_arr):
  command_queue = CommandQueue()
  print(f"EXISTING COMMANDS? {command_queue}")
  for command_data in commands_arr:
    fxn = commands_map[command_data["fxn"]]
    name = command_data["fxn"]
    result_dest = command_data["result_dest"]
    arg_source = None if "arg_source" not in command_data else command_data["arg_source"]
    args = []
    if "args" in command_data:
      for arg in command_data["args"]:
        args.append(arg)

    command = Command(name, fxn, result_dest, args, arg_source)
    print(f"ADDING COMMAND {command}")
    command_queue.add(command)
  print(f"COMMAND QUEUE: {command_queue}")
  return command_queue

