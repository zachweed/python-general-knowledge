# Assume that we have a string message AAAAAAABBBCCCCCCCDDEEEEEE comprising of 25 characters to be encoded. The string message can be an unsorted one as well. We will have two phases in encoding - building the Huffman tree (a binary tree), and generating the encoded data. The following steps illustrate the Huffman encoding:
# A. Huffman Encoding

    # Phase 1 - Build the Huffman Tree

    # 1. Build a list with the frequency of each character - done, list with each character represented as a node with frequency
    # 2. Sort the list ascending. The list will be a min-heap - done, list was sorted using operator and sorting by frequency
    #   i. [['D', 2],['B', 3], ['E', 6], ['A', 7], ['C', 7]]
    # 3. Pop the two nodes with the lowest frequency from the list - done
    # 4. Create a new node where the frequency is equal to the sum of the two nodes' frequencies. - done
    #  i. This new node will become an internal node in the Huffman Tree
    #    - Insert the two nodes as children of this node - done
    #    - The lower frequency node will be a left child and the higher frequency will be the right child - done
    #    - Re-insert this node back into the min-heap - done

    # Phase 2 - Generate the encoded data

    # 1. Traverse the tree from the root to each leaf node and generate a binary code for each character
    #   - The whole code for a given character cannot be a prefix of any other code
    #   - The binary code is shorter for the more frequent character and vice-versa
    #   - Each node present in the original min-heap becomes a leaf node in the final Huffman Tree
    #   - The heap above could be represented as:
    #     [
    #       ['D', 2, 000],['B', 3, 001], ['E', 6, 01], ['A', 7, 10], ['C', 7, 11]
    #     ]
    #   - This would create 1010101010101000100100111111111111111000000010101010101


# B. Huffman Decoding


    # 1. Given encoded data, and the pointer to the root of a huffman tree, it can be decoded as such:
    #  1. Declare a blank string
    #  2. Traversing from left to right:
    #    i. if the node is 0, move to the left child
    #    ii. if the node is 1, move to the right child
    #    iii. if the node is a leaf (has no children), append the character of the leaf to the string
    #  3. Repeat step 2 until the encoded data has been completely traversed.

import sys
import operator

class Tree:
    def __init__(self, root):
        self.root = root

    def contains_value(self, value):
        nodes = traverse_tree
        for node in nodes:
            if node.value == value:
                return True
        return False

    def value_to_binary(self, value):
       return

    def traverse(self):
        nodes = []
        next_nodes = [self.root]

        while len(next_nodes) > 0:
            for node in next_nodes:
                next_nodes.remove(node)
                if node.left is not None:
                    next_nodes.append(node.left)
                    node.left.binary = value_to_binary(node.left.value)
                if node.right is not None:
                    next_nodes.append(node.right)
                    node.right.binary = value_to_binary(node.right.value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.binary = None
        self.frequency = 1

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def set_frequency(self, frequency):
        self.frequency = frequency

    def set_binary(self, binary):
        self.binary = binary

    def get_left_child(self, node):
        return self.left

    def get_right_child(self, node):
        return self.right

    def get_frequency(self, frequency):
        return self.frequency

    def get_binary(self, binary):
        return self.binary


# "The size"
# "thesize"
# t -> 1, h -> 1, s -> 1, i -> 1, z -> 1, e -> 2
#
# Node(value: t, frequency: 1), Node(value: h, frequency: 1)
# Node(value: None, frequency: 2, left: Node(value: t, frequency: 1), right: Node(value: h, frequency: 1))
#

def huffman_encoding(data):
    frequency_list = list()
    huffman_tree = list()
    min_heap = {}
    min_heap_c = []
    for char in data:
        if char != ' ':
            if char in min_heap:
                min_heap[char] += 1
            else:
                min_heap[char] = 1

    min_heap = sorted(min_heap.items(), key=lambda x: x[1])
    print(min_heap)

    for i in range(0, len(min_heap)):
        if len(min_heap) == 0:
            break
        else:
            left_node = min_heap.pop()
            left_value = left_node[0]
            left_node_binary = format(ord(left_value), 'b')
            left_node_binary =
            if len(min_heap) > 0:
                right_node = min_heap.pop()
                right_node_binary = format(ord(right_node[0]), 'b')
            new_frequency = left_node[1] + right_node[1]
            new_node = Node(new_frequency)
            new_node.left = left_node
            new_node.right = right_node
            min_heap_c.append(new_node)

    return min_heap_c



if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    heap = huffman_encoding(a_great_sentence)
    for pair in heap:
        print(pair.value)
        print(pair.left)
        print(pair.left.binary)
        print(pair.right)
        print(pair.right.binary)

    #for branch in tree:

   # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
   # print ("The content of the encoded data is: {}\n".format(encoded_data))

# decoded_data = huffman_decoding(encoded_data, tree)

# print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# print ("The content of the encoded data is: {}\n".format(decoded_data))
