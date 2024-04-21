import json

# open
with open('printer.JSON', 'r') as file:

  # read
  data = json.load(file)

  # add
  data["id"] = 