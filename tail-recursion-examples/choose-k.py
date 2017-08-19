def rec_choose_k(n, k):
  if k is 0 or k is n:
    return 1
  else:
    return rec_choose_k(n-1, k) + rec_choose_k(n-1, k-1)

def tail_rec_choose_k(n, k):
  return trck(n, k, 0, 0, [0]*(k+1))

def trck(n, k , cn, ck, arr):
  if cn > n:
    return arr[0]
  elif cn == n and ck < k:
    return arr[k]
  elif ck == 0:
    arr[ck] = 1
    return trck(n, k, cn+1, k, arr)
  else:
    if cn == ck:
      arr[ck] = 1
    else:
      arr[ck] = arr[ck] + arr[ck-1]
    return trck(n, k, cn, ck-1, arr)

def test_f():
  for n in range(0, 10):
    for k in range(0, n+1):
      recf = rec_choose_k(n, k)
      trecf = tail_rec_choose_k(n, k)
      if recf == trecf:
        print 'when n is %d, k is %d, result is %d' % (n, k, recf)
      else:
        print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def main():
  test_f()

if __name__ == '__main__':
  main()
