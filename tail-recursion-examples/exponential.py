# recursive exponential O(n)
def rec_expt_n(b, n):
  if n == 0:
    return 1
  else:
    return b * rec_expt_n(b, n-1)

# tail recursive exponential O(n)
def tail_rec_expt_n(b, n):
  return tren(b, n, 1)

def tren(b, n, product):
  if n == 0:
    return product
  else:
    return tren(b, n-1, product*b)

# recursive exponential O(log n)
def rec_expt_log(b, n):
  if n == 0:
    return 1
  elif is_even(n):
    return square(rec_expt_log(b, n/2))
  else:
    return b * rec_expt_log(b, n-1)

def is_even(n):
  return n % 2 == 0

def square(n):
  return n * n

# tail recursive exponential O(log n)
def tail_rec_expt_log(b, n):
  return trel(b, n, 1, b)

def trel(b, n, acc, temp):
  if n == 0:
    return acc
  elif n & 1 is 1:
    return trel(b, n>>1, acc*temp, square(temp))
  else:
    return trel(b, n>>1, acc, square(temp))

def test_f_n():
  for n in range(0, 11):
    recf = rec_expt_n(3, n)
    trecf = tail_rec_expt_n(3, n)
    if recf == trecf:
      print 'when n is %d, result is %d' % (n, recf)
    else:
      print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def test_f_log():
  for n in range(0, 11):
    recf = rec_expt_log(3, n)
    trecf = tail_rec_expt_log(3, n)
    if recf == trecf:
      print 'when n is %d, result is %d' % (n, recf)
    else:
      print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def main():
  print 'test O(n)'
  test_f_n()
  print '===================='
  print 'test O(log n)'
  test_f_log()

if __name__ == '__main__':
  main()
