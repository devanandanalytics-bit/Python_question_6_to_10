# 06 . Palindron check 

def  palindrom_check(text: str) ->bool:
    """
       Check the palindrom string 
       Args: 
            (str) : Input should be string
       Return:
             (bool): If Palindrom is True otherwise False
       Raise: 
            TypeError:
                      If string is empyt
    """
    # validate the input
    if not isinstance(text,str):
        raise TypeError("Input should be string :")
    if text.strip() == "":
        ValueError("Input not to empty :")
    else:
        text.strip().lower()
  #logic 
    reverse_string = ""
    for char in text:
        reverse_string = char + reverse_string
    return reverse_string == text

#<------main Execution----->
if __name__ == "__main__":
    try:
        # taking input
        user_input = input("Enter your string :")
        if palindrom_check(user_input):
            print("The string is palindrome")
        else:
            print("Given string is not palindrom")
        
    except (TypeError,ValueError) as e:
        print(e)
    except Exception as e:
        print("Error",e)

    