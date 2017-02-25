from sharelib import read_test_input

# args: input_array
#       an array of integers
#       3 <= array size <= 100
#       1 <= element <= 10e6
# return: an array of three integers
# more detail see: http://mjm1990.com/article/%E4%B8%89%E8%A7%92%E5%BD%A2%E5%91%A8%E9%95%BF
def max_circumference(input_array):
#return solution1(input_array)
#return solution2(input_array)
#return solution3(input_array)
  return solution4(input_array)

# brute force
# O(n^3)
def solution1(input_array):
  result = []
  max_cir = 0
  n = len(input_array)
  for i in range(0, n):
    for j in range(i+1, n):
      for k in range(j+1, n):
        cir = input_array[i] + input_array[j] + input_array[k]
        m = max(input_array[i], max(input_array[j], input_array[k]))
        if cir - m > m and cir > max_cir:
          max_cir = cir
          result = [input_array[i], input_array[j], input_array[k]]

  return result

# sort and use ai <= aj <= ak and ai > ak - aj
# O(n^2)
def solution2(input_array):
  result = []
  max_cir = 0
  n = len(input_array)
  input_array.sort()
  for k in range(n-1,-1,-1):
    for j in range(k-1,-1,-1):
      i = j - 1
      if i >= 0 and input_array[i] > input_array[k] - input_array[j]:
        cir = input_array[i] + input_array[j] + input_array[k]
        if cir > max_cir:
          max_cir = cir
          result = [input_array[i], input_array[j], input_array[k]]

  return result

# based on solution2 and trim those 3*ak <= max_cir
def solution3(input_array):
  result = []
  max_cir = 0
  n = len(input_array)
  input_array.sort()
  for k in range(n-1,-1,-1):
    if 3 * input_array[k] > max_cir:
      for j in range(k-1,-1,-1):
        i = j - 1
        if i >= 0 and input_array[i] > input_array[k] - input_array[j]:
          cir = input_array[i] + input_array[j] + input_array[k]
          if cir > max_cir:
            max_cir = cir
            result = [input_array[i], input_array[j], input_array[k]]

  return result

# actually, we can prove the first three consective integers
# that satify ai + aj > ak is the solution after sorting and
# starting to examing from the largest ak
# so it can be soloved in O(n) if we use counting sort
def solution4(input_array):
  result = []
  n = len(input_array)
  input_array.sort()
  for k in range(n-1,2,-1):
    if input_array[k-2] + input_array[k-1] > input_array[k]:
      result = [input_array[k-2], input_array[k-1], input_array[k]]
      return result
  return result

# please run 'python solutions.py' to preview the result
if __name__ == '__main__':
  inputs = read_test_input('test_input.txt')
  for i in range(0, len(inputs)):
    input_array = inputs[i]
    actual = max_circumference(input_array)
    actual = map(str, actual)
    print 'test case %d: %s' % (i+1, ','.join(actual))
