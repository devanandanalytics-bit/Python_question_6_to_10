# 09. sum_of_digit

def sum_of_digit(n :int) ->int:
    """
    Calculate the sum of digits of a non-negative integer.

    Parameters:
            n(int): The numbers whose digits will be summed.
    Returns:
        int: Sum of the digits.
    Raises: 
         TypeError: If input is not an integers.
         ValueError: If input is negative
    """
    if not isinstance(n,int):
        raise TypeError("Input must be an input .")
    if n < 0:
        raise ValueError("Input must a positive number")

    #logic
    total = 0
    while n > 0:
        digit = (n%10)
        total = total + digit
        n = n // 10
    return total
# main execution
if __name__ == "__main__":
    num = int(input("Enter your number : "))
    try:
        num = int(num)
    except ValueError:
        print("Error","Please enter valid integer only .")
    else:
        try:
            result = sum_of_digit(num)
            print(f"sum of digits is {result}")
        except (TypeError,ValueError) as error:
            print("Error",error)