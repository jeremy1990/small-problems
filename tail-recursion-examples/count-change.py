def rec_count_change(amount):
  return rcc(amount, 5)

def rcc(amount, kinds_of_coins):
  if amount is 0:
    return 1
  elif amount < 0 or kinds_of_coins is 0:
    return 0
  else:
    return rcc(amount, kinds_of_coins-1) + rcc(amount-first_denomination(kinds_of_coins), kinds_of_coins)

def first_denomination(kinds_of_coins):
  coins = [0, 1, 5, 10, 25, 50]
  return coins[kinds_of_coins]

def tail_rec_count_change(amount):
  return trcc(amount, 5, 0, 1, [0]*(amount+1))

def trcc(amount, kinds_of_coins, ca, ck, arr):
  if ck > kinds_of_coins:
    return arr[amount]
  elif ca > amount:
    return trcc(amount, kinds_of_coins, 0, ck+1, arr)
  else:
    if ca == 0:
      arr[ca] = 1
    else:
      remain = ca - first_denomination(ck)
      if remain >= 0:
        arr[ca] = arr[ca] + arr[remain]
    return trcc(amount, kinds_of_coins, ca+1, ck, arr)

def test_f():
  for n in range(0, 101):
    recf = rec_count_change(n)
    trecf = tail_rec_count_change(n)
    if recf == trecf:
      print 'when n is %d, result is %d' % (n, recf)
    else:
      print 'something went wrong: %d (recursive result), %d (tail recursive result)' % (recf, trecf)

def main():
  test_f()

if __name__ == '__main__':
  main()
