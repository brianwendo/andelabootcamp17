def data_type(data):
  if type(data) == None:
    return 'no value'
  elif type(data) == str:
    return len(data)
  elif type(data) == bool:
    return data
  elif type(data) == int:
    if data < 100:
      return 'less than 1000'
    elif data > 100:
      return 'more than 100'
    else:
      return 'equal to 100'
  elif type(data) == list:
    if len(data) < 3:
      return None
    else:
      return data[2]