from sharelib import read_test_input
from solutions import part_of_integer_k
from time import time

def read_answer(filename):
  answers = []
  fh = open(filename)
  for line in fh.readlines():
    line = line.strip()
    answers.append(line == 'Yes')
  return answers

def is_same(answer, actual):
  return answer == actual

def main():
  inputs = read_test_input('test_input.txt')
  answers = read_answer('answer.txt')
  if type(inputs) != list:
    print 'Error: inputs should be a list'
  if type(answers) != list:
    print 'Error: answers should be a list'
  if len(inputs) != 2*len(answers):
    print 'Error: inputs size not equal to 2 * answer'
    return

  time_elapsed = 0
  total = 0
  correct = 0
  i = 0
  while i < len(inputs):
    start = time()
    actual = part_of_integer_k(inputs[i], inputs[i+1])
    end = time()
    time_elapsed = time_elapsed + end -start
    answer = answers[i/2]
    if is_same(answer, actual):
      correct = correct + 1
    else:
      print 'test case %d: expect %s, actual %s' % (i+1, answer, actual)
    total = total + 1
    i = i + 2

  print 'problem: part of integer k'
  print 'pass rate (correct/total): %d/%d' % (correct, total)
  print 'time elapsed: %.3f' % time_elapsed

# please run: python test.py to test the solutions
if __name__ == '__main__':
  main()
