import heapq
import numpy as np #use for matrix and log calculate,矩阵以及对数计算使用

class Node:
    def __init__(self, symbol, probability):
        self.symbol = symbol
        self.probability = probability
        self.children = []

    def __lt__(self, other):
        return self.probability < other.probability

def build_huffman_tree(probabilities, radix, N):
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

def huffman_encode(symbol_probabilities, radix,N):
    #判断radix值是否在[2,5]范围内
    if radix>5 or radix<2:
        text = 'R value is INVALID,please try again'
        return text

    symbol_probabilities = N_probabilities(symbol_probabilities,N)
    root = build_huffman_tree(symbol_probabilities, radix,N)
    huffman_codes = generate_huffman_codes(root)

    return huffman_codes
#calculate average code length
def aver_code_length(symbol_probabilities, radix,N):
    huffman_encodes = huffman_encode(symbol_probabilities,radix,N)
    symbol_probabilities = N_probabilities(symbol_probabilities,N)
    Ave_length = 0                                      #Attention!!!
    for symbol, code in huffman_encodes.items():
        #对每一个huffman编码，便历symbol_probabilities
        for i in range(len(symbol_probabilities)):          #正确的前提是，Huffman编码必须正确，也就是传给build_Huffman_tree
            if symbol_probabilities[i][0] == symbol:            #概率symbol_probabitilies必须是降序排列
                Ave_length += symbol_probabilities[i][1] * len(code)
                #print(Ave_length)
    return Ave_length

#calculate info_entropy
def Entropy(symbol_probabilities,N):              #这里仅仅与symbol_probabilities有关
    Entropy = 0                                 # 内容不会出错，与排列顺序无关，一定是正确的
    symbol_probabilities = N_probabilities(symbol_probabilities,N)
    for prob in symbol_probabilities:
        Entropy += prob[1] * np.log2(1 / prob[1])
    return Entropy

#process symbol_probabilities
def N_probabilities(symbol_probabilities,N):
    #处理N重序列信源编码
    if N == 1:
        symbol_probabilities = symbol_probabilities
        return symbol_probabilities
    elif N==2:
        #initialize
        length = len(symbol_probabilities)
        length_2 = length**2
        char_single =[]
        char_matrix = [[0]*length for _ in range(length)]
        prob_matrix = []
        for i in range(length):
            prob_matrix.append(symbol_probabilities[i][1])
        matrix_P1 = np.array(prob_matrix)   #1*N matrix
        matrix_P2 = np.reshape(matrix_P1,(len(matrix_P1),1))    #N*1 matrix
        prob_matrix = np.outer(matrix_P2,matrix_P1)

        # N*N matrix_prob
        #print(prob_matrix)
        #processing char
        for i in range(length):
            char_single.append(symbol_probabilities[i][0])
        for i in range(len(char_matrix)):
            for j in range(length):
                char_matrix[i][j]=char_single[i]+char_single[j]
        #print(char_matrix)

        #mix and send to def:build_huffman_tree
        symbol_probabilities=[]
        temp_char = np.reshape(char_matrix,(1,length_2))[0]
        temp_prob = np.reshape(prob_matrix, (1, length_2))[0]
        for i in range(length_2):
            symbol_probabilities.append([temp_char[i],temp_prob[i]])
        symbol_probabilities = sorted(symbol_probabilities, key=lambda x: x[1], reverse=True)
        return symbol_probabilities

    elif N==3:
        # initialize
        length = len(symbol_probabilities)
        length_3 = length**3
        char_single = []
        char_matrix = [[[0] * length for _ in range(length)] for _ in range(length)]
        prob_matrix = []
        for i in range(length):
            prob_matrix.append(symbol_probabilities[i][1])
        matrix_P1 = np.array(prob_matrix)  # 1*N matrix
        matrix_P2 = np.reshape(matrix_P1, (len(matrix_P1), 1))  # N*1 matrix
        temp_Prob = np.outer(matrix_P2, matrix_P1)
        prob_matrix = np.outer(matrix_P1,temp_Prob)#计算外积
        #prob_matrix = np.reshape(prob_matrix,(1,length_3))[0]
        #print(matrix_P1,'\n',prob_matrix)

        #processing char
        for i in range(length):
            char_single.append(symbol_probabilities[i][0])
        for i in range(len(char_matrix)):
            for j in range(length):
                for k in range(length):
                    char_matrix[i][j][k]=char_single[i]+char_single[j]+char_single[k]
        #print(char_matrix)

        # mix and send to def:build_huffman_tree
        symbol_probabilities = []
        temp_char = np.reshape(char_matrix, (1, length_3))[0]
        temp_prob = np.reshape(prob_matrix, (1, length_3))[0]
        for i in range(length_3):
            symbol_probabilities.append([temp_char[i],temp_prob[i]])
        symbol_probabilities = sorted(symbol_probabilities, key=lambda x: x[1], reverse=True)
        #print(temp_char,'\n',temp_prob)
        return symbol_probabilities
    else:
        text = 'N value is INVALID,please try again'
        return text

# 调用函数进行编码
# Q = "Hello world"
# N = 2
# R = 2
# symbol_probabilities = [['a', 0.4], ['b', 0.3], ['c', 0.2], ['d', 0.1]]
# huffman_code = huffman_encode(symbol_probabilities,R,N)
# ave = aver_code_length(symbol_probabilities,R,N)
# Info_Entropy = Entropy(symbol_probabilities,N)
# print(huffman_code,'\n',ave,'\n',Info_Entropy)



# huffman_codes = huffman_encode(symbol_probabilities, R,N)
# #Aver_code_length = aver_code_length(symbol_probabilities,huffman_codes)
# # 打印结果
# if huffman_codes:
#     for symbol, code in huffman_codes.items():
#        print(f"Symbol: {symbol}, Code: {code}")



