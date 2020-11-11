class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[bit ^ 1 for bit in bits][::-1] for bits in A]
