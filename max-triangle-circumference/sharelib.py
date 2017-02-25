def read_test_input(filename):
  # a list of array of integers
  # 3 <= array size <= 100
  # 1 <= element <= 10e6
  inputs = []
  fh = open(filename)
  for line in fh.readlines():
    line = line.strip()
    input_array = line.split(',')
    input_array = map(int, input_array)
    inputs.append(input_array)
  return inputs
