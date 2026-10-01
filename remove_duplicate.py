# 10. Remove Duplicate Elements from a List in python

from typing import List,Any
def remove_duplicate(List: List[Any]) ->List[Any]:
    """
    Remove dulicate from a list while maintaining original order.

    Returns:
          List[Any]: A new list with dulicate removed.
    Raises:
         TypeError: If input is not a list.
         ValueError: If the list is empty.
    """

    # validate input is a list
    if not isinstance(List,list):
        raise TypeError("Input must be a list.")
    #validate list is not empty
    if len(List) == 0:
        raise ValueError("List must not be empty.")
    # validate list has only one elements

# logic
    if len(List) == 1:
        print("List has already one elements . No duplicate to remove")
        return List
    result = []
    for i in List:
        if i not in result:
            result.append(i)
    return result

# _____main execution____#

if __name__ == "__main__":
    number_list = [100,2,3,4,5,6,7,8,9,4,5,6]
    # number_list = []
    try:
        result = remove_duplicate(number_list)
    except (TypeError,ValueError) as error:
        print("Error",error)
    except Exception as error:
        print("Something went wrong",error)
    else:
        print("After removing duplicate :",result)
        