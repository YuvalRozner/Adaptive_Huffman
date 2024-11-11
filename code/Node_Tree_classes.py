import math

class CharCodeDict:
    def __init__(self):
        self.char_code_dict = {}
        self.char_code_dict_create()

    def char_code_dict_create(self):
        """Generate binary codes for the English alphabet based on their position."""
        m = 26  # Number of characters in the alphabet
        e = int(math.floor(math.log2(m)))  # Length of the binary code
        r = m - 2 ** e  # Remaining characters after 2^e
        for k in range(1, m + 1):
            if 1 <= k <= 2 * r:
                self.char_code_dict[chr(97 + k - 1)] = format(k - 1, f'0{e + 1}b')
            else:
                self.char_code_dict[chr(97 + k - 1)] = format(k - r - 1, f'0{e}b')

    def get_code(self, char):
        return self.char_code_dict[char]

    def get_char(self, code):
        for char, binary_code in self.char_code_dict.items():
            if code == binary_code:
                return char
        return None

    def get_codes(self):
        return self.char_code_dict

class Node:
    def __init__(self, symbol=None, weight=0, index=None, parent=None): # the node constructor.
        self.symbol = symbol
        self.weight = weight
        self.left = None
        self.right = None
        self.parent = parent
        self.index = index

    def __repr__(self):
        return f"Node(symbol={self.symbol}, weight={self.weight}, index={self.index})"


from ctypes import alignment
from tqdm import tqdm


class Tree:
    def __init__(self): # the tree constructor. """"
        self.root = Node(symbol="nyt", weight=0, index=51) # root begins as a new nyt.
        self.NYT = self.root # always keep a pointer to the nyt node. (biggins being the root itself.)
        self.char_to_node = [None] * 26  # Initialize with 26 None values
        self.char_code_dict = CharCodeDict()
        self.imgCounter = 0


    def insert(self, symbol): # insert a new node into the tree if not yet exist.
        found = self.char_to_node[ord(symbol) - ord('a')]
        if found:
            found.weight += 1
            self.increase_weight(found.parent)
        else:
            self.insertNew(symbol)


    def insertNew(self, symbol): # insert a new node and a new nyt on the old nyt.
        currentNYTnode = self.NYT
        ind = currentNYTnode.index - 2 # calc the index values for the sons.
        currentNYTnode.left = Node('nyt', 0, index=ind, parent=currentNYTnode) # new NYT in left.
        currentNYTnode.right = Node(symbol, 1, index=ind+1, parent=currentNYTnode) # new symbol son in right.
        dic_ind = ord(symbol) - ord('a')
        self.char_to_node[dic_ind] = currentNYTnode.right # add the symbol to the dictionary.
        self.increase_weight(currentNYTnode) # going up the tree and increase the weights.
        self.NYT = self.NYT.left # set the NYT to the left son.

        # if self.imgCounter<350 or self.imgCounter>659600: self.visualize(filename = 'images/tree_'+str(self.imgCounter).zfill(6))
        # self.imgCounter+=1


    def increase_weight(self, node): # recursively goes up the tree and increase the weights.
        if node:
            swapWith = self.find_node_to_swap(node)
            if(swapWith):
                self.swap_nodes(node, swapWith)
            node.weight += 1
            if node.parent:
                self.increase_weight(node.parent)


    def find_node_to_swap(self, target_node):
        def search(node):
            if node is None: return None
            if node.weight < target_node.weight: return None
            if node.index < target_node.index: return None
            if node != target_node and node.weight == target_node.weight:
                return node
            right_result = search(node.right)
            left_result = None
            if node.right and (node.weight - node.right.weight) >= target_node.weight:
                left_result = search(node.left)
            if left_result and right_result:
                if left_result.weight == target_node.weight and right_result.weight == target_node.weight:
                    return left_result if left_result.index > right_result.index else right_result
                elif left_result.weight == target_node.weight:
                    return left_result
                elif right_result.weight == target_node.weight:
                    return right_result
            return left_result or right_result

        best_node = search(self.root)
        return best_node if best_node and best_node.index > target_node.index else None


    def swap_nodes(self, node1, node2): # Swap two nodes in the tree.
        # Swap the parents
        node1.parent, node2.parent = node2.parent, node1.parent
        # Update the parent 1's left or right child pointers
        if node1.parent:
            if node1.parent.left == node2: node1.parent.left = node1
            else: node1.parent.right = node1
        if node2.parent:
            if node2.parent.left == node1:  node2.parent.left = node2
            else: node2.parent.right = node2
        node1.index, node2.index = node2.index, node1.index # Swap the indices

        # if self.imgCounter<350 or self.imgCounter>659600: self.visualize(filename = 'images/tree_'+str(self.imgCounter).zfill(6))
        # self.imgCounter+=1


    def find_path_to_root(self, target_node):
        path = ""
        current = target_node
        while current.parent:
            if current.parent.left is current: path = "0" + path
            elif current.parent.right is current: path = "1" + path
            current = current.parent
        return path


    def divide_node_weight_by_two(self):
        for node in self.char_to_node:
          if node:
            node.weight = math.ceil(node.weight / 2)
        self.fix_parent_weight()


    def fix_parent_weight(self):
        # Helper function to perform post-order traversal
        def post_order_traversal(node):
            if node is None: return 0
            if node in self.char_to_node: return node.weight
            left_weight = post_order_traversal(node.left)
            right_weight = post_order_traversal(node.right)
            # Update the weight of the current node
            if node.left is not None and node.right is not None:
                node.weight = node.left.weight + node.right.weight
            elif node.left is not None:
                node.weight = node.left.weight
            elif node.right is not None:
                node.weight = node.right.weight
            else:
                node.weight = 0  # Leaf nodes
            return node.weight
        # Start the traversal from the root
        post_order_traversal(self.root)

    def encode_text(self, text, inertion, with_inertion=False):
        encoded_string = ""
        i = 1
        for char in tqdm(text, desc="yuval"):
            dic_ind = ord(char) - ord('a')
            if self.char_to_node[dic_ind] is None:
                nyt_code = self.find_path_to_root(self.NYT)
                char_code = self.char_code_dict.get_code(char)
                encoded_string += nyt_code + char_code
                self.insert(char)
            else:
                path_code = self.find_path_to_root(self.char_to_node[dic_ind])
                encoded_string += path_code
                self.insert(char)

            if with_inertion and i % inertion == 0:
                self.divide_node_weight_by_two()
            i += 1
        return encoded_string


    def visualize(self, filename, isDisplay = False):
        from graphviz import Digraph
        from IPython.display import display, Image
        if not self.root: return
        dot = Digraph()
        dot.attr(label='Adaptive Huffman Coding Tree\nYuval Rozner', fontsize='30', labelloc='t')
        #dot.attr(size="16!,16!")
        #dot.attr(ratio='fill')
        # Add nodes and edges
        def add_nodes_edges(node):
            if node:
                # Assign node labels
                node_label = f'( {node.symbol} )\n{node.weight} |  #{node.index}'
                if node.symbol=='nyt': node_label = f'{node.weight} |  #{node.index}'
                if self.NYT == node: node_label = f'(NYT)\n#{node.index}'
                # Assign colors
                node_color = 'lightblue' if node.symbol != 'nyt' else 'lightgreen' if self.NYT == node else 'lightgrey'
                # Create the main node with color
                dot.node(str(id(node)), node_label, style='filled', fillcolor=node_color, shape='circle', margin='0.005')
                # Add edges to
                if node.left:
                    dot.edge(str(id(node)), str(id(node.left)), label='0', color='green')
                    add_nodes_edges(node.left)
                if node.right:
                    dot.edge(str(id(node)), str(id(node.right)), label='1', color='darkgreen')
                    add_nodes_edges(node.right)
        add_nodes_edges(self.root)
        # Render the graph to a PNG file
        dot.format = 'png'
        dot.render(filename, format='png', cleanup=True)
        # Display the graph inline
        if isDisplay: display(Image(filename = filename+'.png'))


tree = Tree()
with open("/content/rozner_text.txt", "r") as file:
    text = file.read()

encoded_text = tree.encode_text(text, with_inertion=True, inertion=173)
min_len = len(encoded_text)
print( f"\n --------output ecncoded len: {len(encoded_text)}")

tree.visualize(isDisplay=True, filename = 'final_tree - without inertion')