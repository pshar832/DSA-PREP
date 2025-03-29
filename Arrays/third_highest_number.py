class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float(-inf)

        for x in nums:
            if x in (first,second,third):
                continue
            if x > first:
                first, second,third = x , first, second
            elif x > second:
                second , third = x, second
            elif x > third:
                third = x
        return third if third != float('-inf') else first