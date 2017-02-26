from sharelib import read_test_input

# args: input_array
#         an array of integers
#       k
#         the expected sum
# return: True if there is a combination of integers having sum of k
#         Otherwise False
def part_of_integer_k(input_array, k):
  return solution1(input_array, 0, k, 0)

# brute force
# O(2^n)
def solution1(input_array, t, k, s):
  if len(input_array) == t:
    return k == s

  if s > k:
    return False

  if solution1(input_array, t+1, k, s):
    return True

  if solution1(input_array, t+1, k, s+input_array[t]):
    return True

  return False

# please run 'python solutions.py' to preview the result
if __name__ == '__main__':
  inputs = read_test_input('test_input.txt')
  i = 0
  while i < len(inputs):
    input_array = inputs[i]
    k = inputs[i+1]
    actual = 'No'
    if part_of_integer_k(input_array, k):
      actual = 'Yes'
    print 'test case %d: %s' % (i/2+1, actual)
    i = i + 2
