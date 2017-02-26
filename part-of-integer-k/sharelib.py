def read_test_input(filename):
  inputs = []
  fh = open(filename)
  for line in fh.readlines():
    line = line.strip()
    pair = line.split('=')
    if pair[0] == 'a':
      input_array = pair[1].split(',')
      input_array = map(int, input_array)
      inputs.append(input_array)
    elif pair[0] == 'k':
      k = int(pair[1])
      inputs.append(k)
  return inputs
