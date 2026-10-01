# Q7. Count vowel in a string

def vowel_count(text :str) ->int:
    """
     This function is check count the number of vowels in given string

     Parameter: 
               (str): Input should be string
     Return:
            (int): Return in to intiger
     Raise:
           TypeError : Number should be string
    """
    if not isinstance(text,str):
        raise TypeError("Input should be string :")
    vowels = "aieou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count = count + 1
    return count        

# -----main Execution-----
if __name__ == "__main__":
    try:
        # taking input
        user_input = input("Enter your string :")
        # Function calling
        result = vowel_count(user_input)
        print(result)
    except TypeError as e:
        print("Error",e)
    except Exception as e:
        print(e)
    