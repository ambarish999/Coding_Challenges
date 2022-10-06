'''
    Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive integers representing different flux converters -
    which returns a list of integers p where each element in p is the label of the converter that sits on top of the respective converter in q,
    or -1 if there is no such converter. For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7
    in a perfect binary tree of height 3, which is [3, 6, -1].

    The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root, h = 2 represents a perfect binary tree
    with the root and two leaf nodes, h = 3 represents a perfect binary tree with the root, two internal nodes and four leaf nodes (like the example above), and so forth.
    The lists q and p contain at least one but no more than 10000 distinct integers, all of which will be between 1 and 2^h-1, inclusive.
'''

import numpy as np

class Node():

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class PerfectBinaryTree():

    def __init__(self, depth):
        self.depth = depth
        self.root_node_key = (2 ** self.depth) - 1
        self.key_array = [i for i in range(1, self.root_node_key+1)]

    def do_things(self):
        '''
            Runs the required functions in order.
        '''
        
        tree = self.initialize_tree_list()
        new_tree = self.create_tree(tree)
        #arr = self.postorder(new_tree[0])
        return new_tree

    def divide_in_half(self, arr):
        '''
            Divides given array in half using numpy.array_split

            :param arr: <list> Given array
            :return: <list(list)> Two halves of the given array as separate lists within a list
        '''

        two_split = np.array_split(arr, 2)
        return two_split

    def create_node(self, key):
        '''
            Creates the Node object for given key

            :param key: <int> The key for which Node object is created
            :return: <Node> Node object of given key
        '''

        node = Node(key)
        return node

    def initialize_tree_list(self):
        '''
            Initializes a list with the Node object of the root node

            :return: <list> List with one Node item of root node
        '''
        
        tree = []
        root_key = self.key_array.pop()
        root_node = self.create_node(root_key)
        tree.append(root_node)

        return tree

    def create_tree(self, tree):
        '''
            Creates the entire Binary Tree

            :param tree: <list> The initialized tree array containing the root node
            :return: <list> The binary tree. The array still contains one element, but
                            the left and right subtrees are filled
        '''

        two_split = self.divide_in_half(self.key_array)

        left_subtree = self.create_left_subtree(list(two_split[0]))
        right_subtree = self.create_right_subtree(list(two_split[1]))

        tree[0].left = left_subtree
        tree[0].right = right_subtree

        #print(tree[0].key, tree[1].key, tree[2].key)
        return tree

    def create_left_subtree(self, arr):
        '''
            Creates the left subtree from the root node

            :param arr: <list> The split array containing the keys to be filled in the left subtree
            :return: <Node> The left subtree as Node object
        '''

        first_key = arr.pop()
        first_node = self.create_node(first_key)
        left_node = None
        right_node = None

        if len(arr) > 2:
            two_split = self.divide_in_half(arr)
            left_node = self.create_left_subtree(list(two_split[0]))
            right_node = self.create_right_subtree(list(two_split[1]))
        else:
            while len(arr) > 0:
                right_key = arr.pop()
                left_key = arr.pop()

                right_node_temp = self.create_node(right_key)
                left_node_temp = self.create_node(left_key)

                if left_node == None and right_node == None:
                    left_node = left_node_temp
                    right_node = right_node_temp
                else:
                    temp_left = left_node
                    while temp_left.left != None:
                        temp_left = temp_left.left
                    temp_left.left = left_node_temp
                    temp_right = right_node
                    while temp_right.right != None:
                        temp_right = temp_right.right
                    temp_right.right = right_node_temp


        first_node.left = left_node
        first_node.right = right_node

        return first_node
            

    def create_right_subtree(self, arr):
        '''
            Creates the right subtree from the root node

            :param arr: <list> The split array containing the keys to be filled in the right subtree
            :return: <Node> The right subtree as Node object
        '''

        first_key = arr.pop()
        first_node = self.create_node(first_key)
        left_node = None
        right_node = None

        if len(arr) < 2:
            two_split = self.divide_in_half(arr)
            left_node = self.create_left_subtree(list(two_split[0]))
            right_node = self.create_right_subtree(list(two_split[1]))
        else:
            while len(arr) > 0:
                right_key = arr.pop()
                left_key = arr.pop()

                right_node_temp = self.create_node(right_key)
                left_node_temp = self.create_node(left_key)

                if left_node == None and right_node == None:
                    left_node = left_node_temp
                    right_node = right_node_temp
                else:
                    temp_left = left_node
                    while temp_left.left != None:
                        temp_left = temp_left.left
                    temp_left.left = left_node_temp
                    temp_right = right_node
                    while temp_right.right != None:
                        temp_right = temp_right.right
                    temp_right.right = right_node_temp

        first_node.left = left_node
        first_node.right = right_node

        return first_node

    def inorder(self, root, arr=[]):
        '''
            Inorder traversal of the tree. Traverse the left subtree(L), then
            the root(N), and then the right subtree(R)

            :param root: <Node> Root node of the tree
            :param arr: <list> Array to store the keys

            :return: <list> Array of keys
        '''

        if root:
            self.inorder(root.left, arr)

            #print(str(root.key) + "->", end="")
            arr.append(root.key)
            

            self.inorder(root.right, arr)
        return arr

    def postorder(self, root, arr=[]):
        '''
            Postorder traversal of the tree. Traverse the left subtree(L), then
            the right subtree(R), and then the root(N)

            :param root: <Node> Root node of the tree
            :param arr: <list> Array to store the keys

            :return: <list> Array of keys
        '''

        if root:
            self.postorder(root.left)

            self.postorder(root.right)

            #print(str(root.key) + "->", end="")
            arr.append(root.key)
        return arr

    def preorder(self, root, arr=[]):
        '''
            Preorder traversal of the tree. Traverse the root(N), then the left subtree(L),
            and then the right subtree(R)

            :param root: <Node> Root node of the tree
            :param arr: <list> Array to store the keys

            :return: <list> Array of keys
        '''

        if root:
            #print(str(root.key) + "->", end="")
            arr.append(root.key)

            self.preorder(root.left)

            self.preorder(root.right)
        return arr

    def get_parent_of_node(self, node, tree, parent=None, parents_list=[]):
        '''
            Gets the parent node of the given nodes

            :param node: <int> Key to find parent for
            :param tree: <tree> The perfect binary tree
            :param parent: <int> Parent of the node
            :param parents_list: <list> List of parents

            :return: <list> List of parents of each node
        '''

        #for i in node_list:
        if tree:
##            print(tree.key)
            left = tree.left
            right = tree.right
            if int(tree.key) == int(node):
                #parents_list.append(parent)
##                print("PARENT", parent)
                if parent not in parents_list:
                    parents_list.append(parent)
##                print(parents_list)
                return parents_list
            else:
                parent = tree.key
                self.get_parent_of_node(node, left, parent, parents_list)
                self.get_parent_of_node(node, right, parent, parents_list)

        return parents_list
            
                    
                


def solution(h, q):
    '''
        Finds the labels of the converters that sit on top
        of the respective converter in 'q'

        :param h: <int> The height of the perfect binary tree
        :param q: <list(int)> List of positive integers representing
                            the different flux converters

        :return: <list(int)> List of integers representing the labels
                            of the converters that sit on top
                            of the respective converter in 'q'
    '''
    
    tree_object = PerfectBinaryTree(h)
    tree = tree_object.do_things()[0]
    parents_list = []

    for i in q:
        parent = tree_object.get_parent_of_node(i, tree).pop()
        if parent == None:
            parents_list.append(-1)
        else:
            parents_list.append(parent)
        

    return parents_list
                    
                

                
                
        
            

p = solution(3, [7, 3, 5, 1])
n = solution(5, [19, 14, 28])
r = solution(4, [15, 1, 7, 6])
print(p)
print(n)
print(r)
        
