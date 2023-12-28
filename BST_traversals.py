#Author: Kevin Njokom
#Adapted, modified and extended from online tutorials
#Runtime Details 31ms
#Beats 10.98%of users with Python on Leet code
#Memory Details 13.48MB Beats 11.60%of users with Python on Leet code

tree_tuple = ((1,3,None), 2, ((None,3,4),5, (6,7,8)))

#Tuple to tree 
#Creating a binary tree

class TreeNode:
    def __init__(self, key):
        self.key    = key
        self.left   = None
        self.right  = None

def parse_tuple(data):
    #print(data)
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree2 = parse_tuple(tree_tuple)


#tree traversal
#inorder   traversal
#preorder  traversal
#postorder traversal

#inorder -- Left-Root-Right pattern
def traverse_in_order(node):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

traversed_by_inorder = traverse_in_order(tree2)

print(traversed_by_inorder)

#preorder -- Root-Left-Right pattern

def traverse_pre_order(node):
    if node is None:
        return  []
    
    return([node.key] +
               
               traverse_pre_order( node.left ) +

               traverse_pre_order(node.right))

traversed_by_preorder = traverse_pre_order(tree2)

print(traversed_by_preorder)


#preorder -- Left-Right-Root pattern

def traverse_post_order(node):
    if node is None:
        return  []
    
    return(
               
               traverse_post_order( node.left ) +

               traverse_post_order(node.right) +
   
               [node.key])

traversed_by_postorder = traverse_post_order(tree2)

print(traversed_by_postorder)

