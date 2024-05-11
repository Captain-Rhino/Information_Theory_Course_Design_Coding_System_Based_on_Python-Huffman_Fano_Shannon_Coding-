import heapq
from collections import Counter
class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.children = []

    def __lt__(self, other):
        return self.probability < other.probability

def build_huffman_tree(probabilities, radix):
    priority_queue = [Node(symbol, prob) for symbol, prob in probabilities]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        merged_prob = 0
        merged_children = []
        for _ in range(min(radix, len(priority_queue))):
            child = heapq.heappop(priority_queue)
            merged_prob += child.probability
            merged_children.append(child)
        merged_node = Node(None, merged_prob)
        merged_node.children = merged_children
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(root, code="", codes=None):
    if codes is None:
        codes = {}

    if root.symbol is not None:
        codes[root.symbol] = code
    if root.children:
        for i, child in enumerate(root.children):
            generate_huffman_codes(child, code + str(i), codes)

    return codes

def huffman_encode(symbol_probabilities, radix):
    root = build_huffman_tree(symbol_probabilities, radix)
    huffman_codes = generate_huffman_codes(root)
    return huffman_codes

# 调用函数进行编码
Q = "Hello world"
N = 2
R = 4
symbol_probabilities = [['a', 0.4], ['b', 0.3], ['c', 0.2], ['d', 0.1]]
huffman_codes = huffman_encode(symbol_probabilities, N)

# 打印结果
for symbol, code in huffman_codes.items():
    print(f"Symbol: {symbol}, Code: {code}")
