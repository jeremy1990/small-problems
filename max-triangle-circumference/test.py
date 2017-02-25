from sharelib import read_test_input
from solutions import max_circumference
from time import time

def read_answer(filename):
  # a list of array of three integers
  # three integers are sorted in each array
  answers = []
  fh = open(filename)
  for line in fh.readlines():
    line = line.strip()
    answer_array = line.split(',')
    if len(answer_array) == 1 and answer_array[0] == '':
      answer_array = []
    if len(answer_array) > 0:
      answer_array = map(int, answer_array)
    answers.append(answer_array)
  return answers

def is_same(answer, actual):
  answer.sort()
  actual.sort()
  if len(answer) != len(actual):
    return False
  for i in range(0, len(answer)):
    if answer[i] != actual[i]:
      return False
  return True

def main():
  inputs = read_test_input('test_input.txt')
  answers = read_answer('answer.txt')
  if type(inputs) != list:
    print 'Error: inputs should be a list'
  if type(answers) != list:
    print 'Error: answers should be a list'
  if len(inputs) != len(answers):
    print 'Error: inputs size not equal to answer'
    return

  time_elapsed = 0
  total = 0
  correct = 0
  for i in range(0, len(inputs)):
    start = time()
    actual = max_circumference(inputs[i])
    end = time()
    time_elapsed = time_elapsed + end -start
    answer = answers[i]
    if is_same(answer, actual):
      correct = correct + 1
    else:
      if len(answer) > 0:
        answer = map(str, answer)
      if len(actual) > 0:
        actual = map(str, actual)
      print 'test case %d: expect %s, actual %s' % (i+1, ','.join(answer), ','.join(actual))
    total = total + 1

  print 'problem: max triangle circumference'
  print 'pass rate (correct/total): %d/%d' % (correct, total)
  print 'time elapsed: %.3f' % time_elapsed

# please run: python test.py to test the solutions
if __name__ == '__main__':
  main()
