# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p = deque([p])
        q = deque([q])

        while p and q:
            for _ in range(len(p)):
                nodep = p.popleft()
                nodeq = q.popleft()

                if not nodep and not nodeq:
                    continue
                if not nodep or not nodeq or nodep.val != nodeq.val:
                    return False
                
                p.append(nodep.left)
                p.append(nodep.right)
                q.append(nodeq.left)
                q.append(nodeq.right)
        return True
        