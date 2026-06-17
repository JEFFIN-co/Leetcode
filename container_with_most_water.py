class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        ans=0

        while(left < right):
            wdith=right-left
            area=wdith*min(height[right],height[left])
            ans=max(area , ans)

            if height[left]<height[right]:
                   left+=1
            else:
                 right-=1
        return  ans
