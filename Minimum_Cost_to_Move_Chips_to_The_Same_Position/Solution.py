class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        num_odd = len([p for p in position if p % 2 == 1])
        return min(num_odd, len(position) - num_odd)
