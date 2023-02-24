from typing import List

class Node:
    def __init__(self, num: int) -> None:
        self.parent: Node = None
        self.data = num
        self.left: Node = None
        self.right: Node = None

class BST:
    def __init__(self, node: Node) -> None:
        self.root: Node = node

    def is_empty(self) -> bool:
        return self.root is None
    
    def insert(self, data: int, target: Node) -> None:
        # (0, 10) <- 12
        if target.right != None and data > target.data:
            self.insert(data, target.right)
        # (0, 10) <- -20
        elif target.left != None and data < target.data:
            self.insert(data, target.left)
        # (None, 20) <- 10
        elif target.left == None and (target.data > data ):
            target.left = Node(data)
            target.left.parent = target
        #  (10, None) <- 20
        elif target.right == None and (target.data < data):
            target.right = Node(data)
            target.right.parent = target

    def preorder(self, target: Node) -> List[Node]:
        buffer = []
        if target != None:
            print('->', target.data, end=" ")
            buffer.append(target)
            self.preorder(target.left)
            self.preorder(target.right)
        return buffer

    def inorder(self, target: Node) -> List[Node]:
        if target != None:
            self.inorder(target.left)
            print('->', target.data, end=" ")
            self.inorder(target.right)

    def postorder(self, target: Node) -> List[Node]:
        buffer = []
        if target != None:
            self.postorder(target.left)
            self.postorder(target.right)
            print('->', target.data, end=" ")
            buffer.append(target)
        return buffer

    def search(self, data: int, target: Node) -> Node | None:
        if target is None or data == target.data:
            return target
        if data > target.data:
            return self.search(data, target.right)
        if data < target.data:
            return self.search(data, target.left)

    def delete(self, data: int, start: Node):

        target = self.search(data, start)
        
        # If the target is a leaf
        if target.left == None and target.right == None:
            # Handle if the target is root
            if self.root == target:
                self.root = None
                return
            
            # find if it's the left or right child
            if target.parent.left.data == target.data:
                target.parent.left = None
            else:
                target.parent.right = None
            return
        
        # If the target has a child or children
        # Check if the left subtree is available or not
        if target.left != None:
            # Get the node which will replace the delete target
            replacement = self.findMax(target.left)
            # Handle delete target left child
            if target.left != replacement:
                replacement.left = target.left
            else:
                if target.left.left != None:
                    replacement.left = target.left.left
                else:
                    # The replacement left pointer should no longer point to any node since the target doesn't have left child
                    replacement.left = None
            # Handle target right child
            if target.right != None and target.right != replacement:
                replacement.right = target.right
            else:
                # The replacement right pointer should no longer point to any node since the target doesn't have right child
                replacement.right = None
            # handle replacement parent right pointer
            replacement.parent.right = None
            
        # The right subtree should be available
        if target.right != None:
            # The replacement should be the min val node on the right subtree
            replacement = self.findMin(target.right)
            # Only handle delete target right child (since the left child is None)
            if target.right != replacement:
                replacement.right = target.right
            else:
                if target.right.right != None:
                    replacement.right = target.right.right
                else:
                    # Target doesn't have a right child, the replacement right pointer should point to any node
                    replacement.right = None
            # handle replacement parent left pointer
            replacement.parent.left = None
           
        # Handle delete target parent and check is delete target a root
        if self.root != target:
            # If the delete target has a parent
            if target.parent.left != None and target.parent.left.data == target.data:
                target.parent.left = replacement
            else:
                target.parent.right = replacement
        else:
            # Simply replace the root
            self.root = replacement

    def findMin(self, start: Node) -> Node:
        if start.left != None:
            return self.findMin(start.left)
        return start
    
    def findMax(self, start: Node) -> Node:
        if start.right != None:
            return self.findMax(start.right)
        return start


myBST= BST(Node(1)) 
myBST.insert(0, myBST.root) 
myBST.insert(100, myBST.root) 
myBST.insert(90, myBST.root) 
myBST.insert(80, myBST.root) 
myBST.inorder(myBST.root)
print()
myBST.delete(1, myBST.root)
myBST.inorder(myBST.root)
print(myBST.is_empty())