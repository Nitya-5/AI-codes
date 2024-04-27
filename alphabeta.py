class Node:
    def __init__(self,val=float('inf')):
        self.data  = val
        self.child = []

def minimax(depth,node,alpha,beta,indicator):
    if depth == 0: 
        print(depth, node.data)
        return node.data
    else:
        if indicator==0:
            max_val = -float('inf')
            for child in node.child:
                v = minimax(depth-1,child,alpha,beta,1)
                alpha = max(alpha,v)
                if v > max_val:
                    max_val=v
                if beta<=alpha:
                    break
            node.data  = max_val
            print(depth, node.data)
            return max_val
        elif indicator==1:
            min_val  = float('inf')
            for child in node.child:
                v = minimax(depth-1,child,alpha,beta,0)
                if v < min_val:
                    min_val = v
                beta  = min(beta,v)
                if  beta <= alpha:
                    break
            node.data = min_val
            print(depth, node.data)
            return min_val

root = Node()
node1,node2 = Node(),Node()
root.child = [node1,node2]
node3,node4,node5,node6 = Node(),Node(),Node(),Node()
node1.child = [node3,node4]
node2.child = [node5,node6]
node7,node8,node9,node10 = Node(2),Node(3),Node(5),Node(9)
node11,node12,node13,node14 = Node(0),Node(1),Node(7),Node(5)
node3.child = [node7,node8]
node4.child  = [node9,node10]
node5.child = [node11,node12]
node6.child  = [node13,node14]
alpha = -float('inf')
beta = float('inf')
print(minimax(3,root,alpha,beta,0))