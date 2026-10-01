# Q8. Write a function to find the second largest element in a list without using built i sorting ?

from typing import List
def second_largest(nums: List[int])->int:
    """
    Find the second largest unique in a list without using sorting.

    Parameters:
           nums (List[int]) : A list of integers.
    Returns:
          int: The second largest unigue value
    Raises:
          TypeError: If input is not a list or elements are not integers.
          ValueError: If the list has fewer than 2 unique elements.
    """
    # validate that input is a list
    if not isinstance(nums,list):
        raise TypeError("Input must be a list of integers.")
    #validate that all elements in the are integers
    if any(not isinstance(current_number,int) for current_number in nums):
        raise ValueError ("All elements of list should be integers.")
    # check List has atliest two elements
    if len(nums) < 2:
        raise ValueError("List should contain atleast two arguments. ")
    if nums[0] > nums[1]:
        largest = nums[0]
        second = nums[1]
    else:
        largest = nums[1]
        second = nums[0]
    for current_number in nums[2:]:
        if current_number > largest:
            second = largest
            largest = current_number
        elif current_number != largest and current_number > second:
            second = current_number
    return second       

# main execution 
if __name__ == "__main__":
    numbers_list = [1,26,90,44,58,60,77,87]
    try:
        result = second_largest(numbers_list)
    except (TypeError,ValueError) as error:
        print(f"Error {error}")
    except Exception as e:
        print(e)
    else:
        print("second largest :",result)
        