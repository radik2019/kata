
'''
link:  https://www.codewars.com/kata/56ef9790740d30a7ff000199/train/python

'''

class Node:

    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root, lst=[]):

	if tree_root.child_nodes is None:
		return lst
	for k in tree_root.child_nodes:
		lst.append(k.data)
	for i in tree_root.child_nodes:
		tree_to_list(i)
	return lst



#Node(3,4)    
#print(tree_to_list(Node(36,[Node(4),Node(37)])))
 

print(tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])), 
[1, 2, 3, 3, 4, 5, 7])

