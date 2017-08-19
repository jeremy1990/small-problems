def recursive_f(n):
  if n <= 2:
    return n
  else:
    return recursive_f(n-1) + 2 * recursive_f(n-2) + 3 * recursive_f(n-3)

def tail_recursive_f(n):
  return trf(2, 1, 0, n)

def trf(a, b, c, n):
  if n == 0:
    return c
  else:
    return trf(a+2*b+3*c, a, b, n-1)

def test_f():
  for n in range(0, 10):
    recf = recursive_f(n)
    trecf = tail_recursive_f(n)
    if recf == trecf:
      print 'when n is %d, result is %d' % (n, recf)
    else:
      print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def main():
  test_f()

if __name__ == '__main__':
  main()
