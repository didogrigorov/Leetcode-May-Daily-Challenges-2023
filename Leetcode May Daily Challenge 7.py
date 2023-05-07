from bisect import bisect
from typing import List


def longestObstacleCourseAtEachPosition(obstacles: List[int]) -> List[int]:
    result = []
    second_arr = [10**8] * (len(obstacles) + 1)

    for n in obstacles:
        index = bisect(second_arr, n)
        result.append(index + 1)
        second_arr[index] = n

    return result

obstacles = [3,1,5,6,4,2]

print(longestObstacleCourseAtEachPosition(obstacles))