from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

if __name__ == "__main__":
    # 테스트 케이스 추가
    print("Test Case 1: ")
    nums = [2, 7, 11, 15]
    target = 9
    print("Input: nums =", nums, ", target =", target)
    print("Expected Output: [0, 1]")
    print("Actual Output:", twoSum(nums, target))

    print("\nTest Case 2: ")
    nums = [3, 2, 4]
    target = 6
    print("Input: nums =", nums, ", target =", target)
    print("Expected Output: [1, 2]")
    print("Actual Output:", twoSum(nums, target))

    print("\nTest Case 3: ")
    nums = [3, 3]
    target = 6
    print("Input: nums =", nums, ", target =", target)
    print("Expected Output: [0, 1]")
    print("Actual Output:", twoSum(nums, target))
