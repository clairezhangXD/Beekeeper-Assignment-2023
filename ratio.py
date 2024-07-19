from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree
from node import TreeNode

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        """
        Time complexity: O(1)
        """
        self.bst = BinarySearchTree()
    
    def add_point(self, item: T):
        """
        :complexity best: O(CompK) inserts the item at the root.
        :complexity worst: O(CompK * log(N)) inserting at the bottom of the tree where N is the number of elements in
        the BST.
        CompK is the complexity of comparing the keys
        """
        self.bst[item] = item
    
    def remove_point(self, item: T):
        """
        :complexity best: O(CompK) delete the item at the root.
        :complexity worst: O(CompK * log(N)) deleting at the bottom of the tree where N is the number of elements
         in the BST.
        CompK is the complexity of comparing the keys
        """
        del self.bst[item]

    def ratio(self, x, y) -> list[T]:
        """
        Time complexity:
        Best = worst: O(O + log(N))
        Best: O(O + log(N)), where N is the total number of points currently in the Percentile object, and O is the
        number of points returned.
        O(1) is time complexity of obtaining the min and max points, when both are the root.
        O(O + log(N)) is time complexity of ratio_aux which recursively traverses the BST to find the points
        between the min and max points, without needing to visit every node, which is the overall time complexity.

        Worst: O(log(N) + log(N) + O + log(N)) = O(3log(N) + O) = O(log(N) + O), where N is the total number of points
        currently in the Percentile object, and O is the number of points returned.
        O(log(N)+log(N)) is time complexity of obtaining the min and max points when calling kth_smallest, and both
        the min and max point are the root.
        O(O + log(N)) is time complexity of ratio_aux which recursively traverses the BST to find the points between the
        min and max points, without needing to visit every node.
        """

        # nums_gt is the number of points that aren't included in res due to not meeting larger than criteria
        nums_gt = ceil(x*len(self.bst)/100)
        # nums_st is the number of points that aren't included in res due to not meeting smaller than criteria
        nums_st = ceil(y*len(self.bst)/100)

        # min point is the smallest point included in res
        min_point = self.bst.kth_smallest(nums_gt+1, self.bst.root).key
        # max point is the biggest point included in res
        max_point = self.bst.kth_smallest(len(self.bst)-nums_st, self.bst.root).key

        return self.ratio_aux(self.bst.root, min_point, max_point, [])  # return all points between min and max points

    def ratio_aux(self, current: TreeNode, min_point, max_point, res: list[T]):
        """
        Time complexity:
        Best = Worst: O(O + log(N)), where N is the total number of points
        currently in the Percentile object, and O is the number of points returned.
        Because this recursive algorithm does partial inorder traversal, O(O) is time complexity of visiting all the
        points that are definitely within the min and max points range, whereas O(log(N)) accounts for the nodes that
        are visited on the way down to the output nodes, which could be leaf nodes, thus the time it takes to visit
        these nodes is the depth (log(N)).
        """

        if current is None:
            return res

        # Left subtree
        if current.key > min_point:
            self.ratio_aux(current.left, min_point, max_point, res)

        # Current
        if min_point <= current.key <= max_point:
            res.append(current.key)

        # Right subtree
        if current.key < max_point:
            self.ratio_aux(current.right, min_point, max_point, res)

        return res


if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
