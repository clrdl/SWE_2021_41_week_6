from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # 원래 인덱스를 포함하여 정렬
    indexed_nums = sorted((num, i) for i, num in enumerate(nums))
    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []
