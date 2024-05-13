

def product_except_self(nums: list[int]) -> list[int]:
    result = [1] * len(nums)
    pre, post = 1, 1

    for i in range(len(nums)):
        result[i] = pre
        pre *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        print(i)
        result[i] *= post
        post *= nums[i]

    return result




nums = [1,2,3,4]

print(product_except_self(nums))