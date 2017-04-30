class Tree:
    def __init__(self, element, left = None, right = None):
        self.element = element
        self.left = left
        self.right = right

def __str__(self):
    return str(self.element)

def printTreePre(Tree):
    if Tree == None: return
    print (Tree.element),
    printTreePre(Tree.left)
    printTreePre(Tree.right)


def printTreePost(Tree):
    if Tree == None: return
    printTreePost(Tree.left)
    printTreePost(Tree.right)
    print (Tree.element),

def printTreeIn(Tree):
    if Tree == None: return
    printTreeIn(Tree.left)
    print (Tree.element),
    printTreeIn(Tree.right)


Tree = Tree('+', Tree(1), Tree('*', Tree(2), Tree(3)))

def main():
    choice = input('Insert the number of the visit: 1 for Pre-order, 2 for Post-order, 3 for In-order: ')
    choice = int(choice)
    print()
    if choice == 1:
        print("Pre-order visit of the tree: ")
        printTreePre(Tree)
    elif choice == 2:
        print("Post-order visit of the tree: ")
        printTreePost(Tree)
    else:
        print("In-order visit of the tree: ")
        printTreeIn(Tree)

    print("--- End ---")
