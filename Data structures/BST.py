class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
        

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
            return
            
        
        else:
            self.InsertNode(self.root , value)

    def InsertNode(self, current, value):
        if value < current.value:
            if current.left == None:
                current.left = Node(value)
                return
                

            else:
                self.InsertNode(current.left, value)
        
        else:
            if current.right == None:
                current.right = Node(value)
             
            
            else:
                self.InsertNode(current.right, value)


    def contains(self, value, root):
        
        
        if root == None:
            return False
        
        if root.value == value:
            return True
        
        elif value < root.value:
            return self.contains(value, root.left)

        else:
            return self.contains(value, root.right)
        

    def delete(self, value):
        count = 1
        node_to_remove = self.FindNode(value, self.root)
        if node_to_remove == None:
            return False

        parent = self.FindParent(value, self.root)
        if node_to_remove == self.root and self.root.left ==None and self.root.right==None:
            self.root = None
        
        elif node_to_remove.left == None and node_to_remove.right == None:
            
            if node_to_remove.value < parent.value:
                parent.left = None
            
            else:
                parent.right = None

        elif node_to_remove.left == None and node_to_remove.right != None:
            if node_to_remove.value < parent.value:
                parent.left = node_to_remove.right

            else:
                parent.right = node_to_remove.right

        elif node_to_remove.left != None and node_to_remove.right == None:
            if node_to_remove.value < parent.value:
                parent.left = node_to_remove.left
            
            else:
                parent.right = node_to_remove.left

        else:
            largest_value = node_to_remove.left

            while largest_value.right != None:
                largest_value = largest_value.right

            self.FindParent(largest_value.value).right = None
            node_to_remove.value = largest_value.value
            return True

    
    def FindParent(self, value, root):
        if value == root.value:
            return None
        
        if value < root.value:
            if root.left == None:
                return None
            elif root.left.value == value:
                return root
            else:
                return self.FindParent(value, root.left)
            
        else:
            if root.right == None:
                return None
            elif root.right.value == value:
                return root
            else:
                return self.FindParent(value, root.right)
            
    def FindNode(self, value, root):
        if root == None:
            return None
        if root.value == value:
            return root
        elif value < root.value:
            return self.FindNode(value, root.left)
        else:
            return self.FindNode(value, root.right)


    def IsMin(self, root):
        if root.left == None:
            return root.value
        self.IsMin(root.left)

    def IsMax(self, root):
        if root.right == None:
            return root.value
        self.IsMax(root.right)



            








tree1 = BST()

tree1.insert(3)
tree1.insert(5)
tree1.insert(2)
tree1.insert(7)

print(tree1.root.ri)











        


        
