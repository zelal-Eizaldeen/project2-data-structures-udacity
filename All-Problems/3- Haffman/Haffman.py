import heapq
import sys
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.left = None
        self.right = None
        
    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.value > other.value
class Huffman:
    def encode(self, data):
        if data == "":
            return "", None
        freq_dict = {}
        
        for i in data:
            if i not in freq_dict:
                freq_dict[i] =1
            else:
                freq_dict[i] += 1
        
        dict_items = list(freq_dict.items())
        freq_dict = dict(sorted(dict_items, key=lambda i: i[1]))
        heap = []
        for key in freq_dict:
            print(heap)
            node = Node(key, freq_dict[key])
            heapq.heappush(heap,node)#
        merge_heap = self.merge(heap)
        t = heapq.heappop(merge_heap)
        c = self.codes(t)
        encoded_text = ""
        for char in data:
            encoded_text += c[char]
        return encoded_text, t
    def merge(self, heap):
            if len(heap) == 1:
                node = heapq.heappop(heap)
                new_node = Node(None, node.value)
                new_node.left = node
                heapq.heappush(heap, new_node)
            while len(heap) > 1:
                node1 = heapq.heappop(heap)
                node2 = heapq.heappop(heap)
                new_node = Node(None, node1.value + node2.value)
                new_node.left = node1
                new_node.right = node2
                heapq.heappush(heap, new_node)
            return heap
    def codes(self, tree):
        if tree.left == None and tree.right == None:
            return {tree.char:'0'}
        return self.codes_recursive(tree, "")
    def codes_recursive(self, root, recent):
            codes = {}
            if root is None:
                return {}
            if root.key is not None:
                codes[root.key] = recent
            codes.update(self.codes_recursive(root.left, recent + "0"))
            codes.update(self.codes_recursive(root.right, recent + "1"))
            return codes
        
    def decode(self, encoded_text, tree):
        decoded_string = ""
        if encoded_text == "":
            return decoded_string
        current_node = tree
        for char in encoded_text:
            if char == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right
            if current_node.key is not None:
                decoded_string += current_node.key
                current_node = tree
        return decoded_string
if __name__ == "__main__":
    codes = {}
    huffman_coding = Huffman()
    a_great_sentence = "The bird is the word"
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_coding.encode(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_coding.decode(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    huffman_coding = Huffman()
    a_bad_sentence = ""
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_bad_sentence)))
    print ("The content of the data is: {}\n".format(a_bad_sentence))
    encoded_data, tree = huffman_coding.encode(a_bad_sentence)
    #The size of the data is: 49
    #The content of the data is:
    huffman_coding = Huffman()
    word = "cool"
    print ("The size of the data is: {}\n".format(sys.getsizeof(word)))
    print ("The content of the data is: {}\n".format(word))
    encoded_data, tree = huffman_coding.encode(word)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # The size of the encoded data is: 28
    # The content of the encoded data is: 1000001
    
    huffman_coding = Huffman()
    test_sentence = "aaaa"