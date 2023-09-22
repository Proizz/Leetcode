def findDisappearedNumbers(nums):
    """
    First Try -> 2slow
    possible_numbers = list(range(1,len(nums)+1))
    for i in nums:
        try:
            possible_numbers.remove(i)
        except:
            continue
    return possible_numbers
    """
    pos_number = set(list(range(1,len(nums)+1)))
    return list(pos_number.difference(set(nums)))


test = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(test))

test = [1, 1]
print(findDisappearedNumbers(test))
