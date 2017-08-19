
def rec_fib(n):
  if n <= 1:
    return n
  else:
    return rec_fib(n-1) + rec_fib(n-2)

def tail_rec_fib(n):
  return trf(1, 0, n)

def trf(a, b, n):
  if n == 0:
    return b
  else:
    return trf(a+b, a, n-1)

def test_f():
  for n in range(0, 10):
    recf = rec_fib(n)
    trecf = tail_rec_fib(n)
    if recf == trecf:
      print 'when n is %d, result is %d' % (n, recf)
    else:
      print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def main():
  test_f()

if __name__ == '__main__':
  main()
