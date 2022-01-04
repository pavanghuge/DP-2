# // Time Complexity : 2^N
# // Space Complexity : 2^N
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this :


# // Your code here along with comments explaining your approach


class Solution:
    def minCost(self,costs):
        if costs == None or len(costs)==0:
            return 0

        case1 = self.helper(costs, 0, 0 ,0)
        case2 = self.helper(costs, 0, 1 ,0)
        case3 = self.helper(costs, 0, 2 ,0)
        
        return min(case1, min(case2,case3))

    def helper(self,costs, row, color, costsofar):
        #base case
        if row == len(costs):
            return costsofar 
        #logic
        if color == 0:
           return min(
               self.helper(costs, row+1, 1, costsofar + costs[row][0]),
               self.helper(costs, row+1, 2, costsofar + costs[row][0])
           ) 

        if color == 1:
           return min(
               self.helper(costs, row+1, 0, costsofar + costs[row][1]),
               self.helper(costs, row+1, 2, costsofar + costs[row][1])
           ) 

        if color == 2:
           return min(
               self.helper(costs, row+1, 0, costsofar + costs[row][2]),
               self.helper(costs, row+1, 1, costsofar + costs[row][2])
           )


costs = [[17,2,17],[16,16,5],[14,3,19]]
paint = Solution()
cost =paint.minCost(costs)
print(cost)