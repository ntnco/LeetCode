class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        arr1, arr2 = [], []
        
        self.leafRec(root1, arr1)
        self.leafRec(root2, arr2)
        return arr1 == arr2

    
    def leafRec(self, root, arr):
        if not root.left and not root.right:
            arr.append(root.val)
        if root.left:
            self.leafRec(root.left, arr)
        if root.right:
            self.leafRec(root.right, arr)
