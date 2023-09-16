def fibonacci_sequence(n):

  #  Base case
    if n==0:
        return

  #  Recursive case
    else:
      print(n)
    
    fibonacci_sequence(n * 2)

# test case
n=88
fibonacci_sequence(n)
