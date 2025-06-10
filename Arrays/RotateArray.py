def rotate_array(l: list[int], k: int):
    if k > len(l):
        k = k % len(l)
    for i in range(k):
        temp = l[-1]
        l.pop()
        l.insert(0, temp)
    return l

#method 2 (fast)
def array_rotation(nums: list[int], k: int):
    k = k % len(nums)
    new = nums[len(nums) - k:] + nums[:len(nums) - k]
    nums.clear()
    nums.extend(new)
    return nums