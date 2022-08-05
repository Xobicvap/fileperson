from command_map import commands_map

class Condition:
  def __init__(self, predicate, arg_source):
    self.predicate = predicate
    self.arg_source = arg_source

  def __call__(self, args):
    self.predicate(*args)


class Loop:
  def __init__(self, loop_type, command_queue, condition):
    self.loop_type = loop_type
    self.command_queue = command_queue
    self.condition = condition

  def condition_true(self):
    return self.condition(self.command_queue.results[self.condition.arg_source])

  def while_loop(self):
    while self.condition_true():
      self.command_queue()

  def until_loop(self):
    while not self.condition_true():
      self.command_queue()

  def __call__(self):
    if self.loop_type == "while":
      self.while_loop()
    elif self.loop_type == "until":
      self.until_loop()
    else:
      raise Exception("Unrecognized loop type")


class Command:
  def __init__(self, name, fxn, result_dest, args, arg_source = None):
    self.fxn = fxn
    self.result_dest = result_dest
    self.args = args
    self.arg_source = arg_source
    self.name = name

  def __call__(self):
    args = self.args
    return self.fxn(*args)

  def __str__(self):
    return self.name

class CommandQueue:
  def __init__(self):
    self.commands = []
    self.results = self.clear_results()

  def add(self, command):
    self.commands.append(command)

  def __str__(self):
    return ' '.join([str(x) for x in self.commands])

  def __call__(self):
    print(f"COMMANDS TO RUN: {self}")
    for command in self.commands:
      print(f"COMMAND RUNNING: {command.name}")
      print(f"INITIAL ARGS: {command.args}")
      print(f"AND ARG SOURCE: {self.results} WITH KEY {command.arg_source}   ** LEN ARG SOURCE: {len(command.arg_source)}")
      input("PRESS ENTER TO CONTINUE")
      if command.arg_source and len(command.arg_source) == 1:
        arg_source_args = [self.results[command.arg_source]]
        for arg in command.args:
          arg_source_args.append(arg)
        print(f"ARG SOURCE ARGS: {arg_source_args}")
        command.args = arg_source_args
      elif command.arg_source:
        fxn_name, fxn_args = command.arg_source
        if fxn_name not in commands_map:
          raise Exception("Unknown function for argument source")
        fxn = commands_map[fxn_name]
        print(f"FXN: {fxn} ARGS = {fxn_args}")
        arg_source_args = [fxn(*fxn_args)]
        for arg in command.args:
          arg_source_args.append(arg)
        print(f"ARG SOURCE ARGS: {arg_source_args}")
        command.args = arg_source_args
        
      print(f"ARGS: {command.args}")
      result = command()
      self.results[command.result_dest] = result

  def clear_results(self):
    return {"A": [], "B": [], "C": []}


class Orchestrator:
  def __init__(self, command_units):
    self.command_units = command_units

  def __call__(self):
    print(f"COMMAND UNITS: {self.command_units}")
    for command_unit in self.command_units:
      input("Beginning next command...")
      command_unit()
      #print("Finished...")

    #[x() for x in self.command_units]
