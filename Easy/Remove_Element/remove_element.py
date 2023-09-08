nums = [4,5]
val = 1

leng = len(nums)
if leng == 1:
    if nums[leng - 1] == val:
        print(leng - 1)
if leng == 0:
    print(leng)

for i in range(leng):
    while nums[i] == val and i < leng:
        for j in range(i, leng - 1):
            nums[j] = nums[j + 1]
        leng -= 1
        if nums[i] != val:
            break
print(leng)

