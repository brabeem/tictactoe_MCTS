from logging import root
import math
from cpttt import *
global gamm
gamm = 0.1

class node(object):
    
    def __init__(self,parent=None,state=None,action=None):
        self.wins_node_i = 0
        self.num_of_sims_node_i = 0
        self.children = []
        self.parent = parent 
        self.board_state = state
        self.action = action


#   Do something to avoid division by zero and handle zero by zero condition    
    def calc_UCB(self):
        # print("wins_node_i",self.wins_node_i)
        # print("num_of_sims_node_i",self.num_of_sims_node_i)
        # print("self.parent.num_of_sims_node_i",self.parent.num_of_sims_node_i)
        return (self.wins_node_i/(self.num_of_sims_node_i+0.001)) + 2*(math.sqrt(math.log10(self.parent.num_of_sims_node_i+1)/(self.num_of_sims_node_i+0.001))) 
    
    ##returns child with maximum UCB##
    def choose_with_max_UCB(self):
        child_tracker = self.children[0]
        UCB_tracker = self.children[0].calc_UCB()
        for child in self.children:
            UCB =  child.calc_UCB()
            if UCB > UCB_tracker:
                UCB_tracker = UCB
                child_tracker = child
        return child_tracker
    

# True if the passed node is a leaf node else return False
    def isLeafNode(self):
        if len(self.children) == 0:
            return True
        else:
            return False

# simulate from the node which called it
    def roll_out(self):
        return simulate(self.board_state)
    



#Increase the wins as well as number of simulations for wins and loses conditions##
    def backpropagate(self,resul,depth = 0):
        if self.parent == None:
            return 
        self.parent.num_of_sims_node_i += 1
        self.parent.wins_node_i += (resul * (gamm ** depth))
        depth += 1
        self.parent.backpropagate(resul,depth)

            
# Expand if the node is not in the terminal state otherwise just return
    def expand(self):
        if terminal(self.board_state):
            return
        else:
            lst = actions(self.board_state)
            for each_action in lst:
                each_child_state = result(self.board_state,each_action)
                each_child_node = node(parent=self,state=each_child_state,action=each_action)
                self.children.append(each_child_node)




##This function decides to simulte , expand or just walk through the tree##
def funct(Node):
    if not Node.isLeafNode():
        max_UCB_child = Node.choose_with_max_UCB()
        funct(max_UCB_child)
    else:
        if terminal(Node.board_state):
            if winner(Node.board_state) == AI:
                Node.wins_node_i += 1
                Node.backpropagate(1,1)
                Node.num_of_sims_node_i += 1
            else:
                Node.backpropagate(0,1)
                Node.num_of_sims_node_i += 1

        elif Node.num_of_sims_node_i == 0:
            winners = Node.roll_out()
            if winners == AI:
                Node.wins_node_i += 1
                Node.backpropagate(1,1)
            else:
                Node.backpropagate(0,1)
            Node.num_of_sims_node_i += 1
        else:
            Node.expand()



##board ko state chai thik nai pass vairaxa##

def main(board_state):
    root_node = node(parent=None,state=board_state)
    global AI
    AI = player(board_state)
    root_node.expand()
    for i in range(2000):
        funct(root_node)
    return choose_action(root_node)

    
    ##choose the action according to the maximum number of simulations performed##
   
    ##Done testing maximum action nai choose gariraxa##
    ##number of child nodes pani thik nai baniraxa##
def choose_action(root_node):
    maxi = -3000
    max_tracker = None
    for each_child in root_node.children:
        if each_child.num_of_sims_node_i > maxi:    
            max_tracker = each_child.action
            maxi = each_child.num_of_sims_node_i
    return max_tracker


###TODO####
#this thing works only for winning not defending if the opponent is gonna win 
# so to make this a good defender we introduce losing games in next version
# where we consider number of loses in the UCB value so that the branch that leads 
# to the maximum win and minimum lose maximizes the UCB value 











            


        
