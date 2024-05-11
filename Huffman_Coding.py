#符号数: Q:[8-15] ,进制R:[2-5], 重序列N:[1-3]
import heapq
from collections import Counter
def Huffman_Coding(Q,N,R):
    #judge Q,R,N is legal
    if len(Q)>=8 and len(Q)<=15 and R>=2 and R<=5 and N>=1 and N<=3:
    #state is true
    #calculate P of every symbol
        letter_counts = Counter(Q)

    # 计算每个字母出现的概率
        total_letters = len(Q)
        huffman_list=[]
        for letter, count in letter_counts.items():
            letter_and_prob = [letter,count / total_letters]
            huffman_list.append(letter_and_prob)
            #letters.append(letter)
            #probabilities.append(count / total_letters)
        huffman_list = sorted(huffman_list, key=lambda x: x[1], reverse=True)
        print(huffman_list)

        #return huffman_list
    else:
        State = 'Illegal Input,try again plz'
        return State

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

    #展现 编码的结果，平均码长 、信息熵 等性能指标

