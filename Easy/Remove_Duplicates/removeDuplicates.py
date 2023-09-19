def removeDuplicates(nums) -> int:
    # check for:
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return 1

    # sort array
    i = 0
    pointer = 1
    leng = 1
    while i < len(nums)-1:
        if nums[i] != nums[i+1]:
            nums[pointer] = nums[i+1]
            pointer += 1
            print("Wechsel")
        i+=1

    # count length
    for i in range(0, len(nums)-1):
        if nums[i] < nums[i+1]:
            leng += 1
        else:
            break;
    return leng


test = [1, 1, 2]
k = removeDuplicates(test)
print(test[:k])

test = [1, 2]
k = removeDuplicates(test)
print(test[:k])

test = [1, 1]
k = removeDuplicates(test)
print(test[:k])


test = [1, 1 ,1,1, 2,2,2,3]
k = removeDuplicates(test)
print(test[:k])

test = [1, 2 , 3]
k = removeDuplicates(test)
print(test[:k])


test = [1,2,4,4,4,5,5]
k = removeDuplicates(test)
print(test[:k])

test = [-3,-1,0,0,0,3,3]
k = removeDuplicates(test)
print(test[:k])

test = [1, 2, 2, 3]
k = removeDuplicates(test)
print(test[:k])