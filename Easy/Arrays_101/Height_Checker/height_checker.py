def heightChecker(heights):
    counter = 0
    s_heights = sorted(heights)
    for i in range(len(heights)):
        if heights[i] != s_heights[i]:
            counter += 1
    return counter


h = [1,2,3,6,5]
print(heightChecker(h))