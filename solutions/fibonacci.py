def fibonacci(num):
    """
    Returns the nth Fib number.

    Parameters:
    n (int): The index in the Fib sequence.

    Returns:
    int: The nth Fib number.
    """



    # Base cases
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    # Starting values for the Fib sequence
    a, b = 0, 1

    # Calculate Fib up to the nth number
    for _ in range(2, num + 1): 
        # The next Fib number is the sum of the previous two
        next_fib = a + b
        # Update a and b for the next iteration
        a, b = b, next_fib
    
    return b





    # if num < 2:
    #     return num
    
    # last_two = (0, 1)

    # for i in range(0, num - 1, 1):
    #     sum = last_two[0] + last_two[1]
    #     last_two = (last_two[1], sum)

    # return last_two[1]

if __name__ == "__main__":
  
  print("Expecting: 0")
  print(fibonacci(0))

  print("")

  print("Expecting: 1")
  print(fibonacci(2))

  print("")

  print("Expecting: 55")
  print(fibonacci(10))

  print("")

  print("Expecting: 1")
  print(fibonacci(1))

  print("")

  print("Expecting: 6765")
  print(fibonacci(20))
