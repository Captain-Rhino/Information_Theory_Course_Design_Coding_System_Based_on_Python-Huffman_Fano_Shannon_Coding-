import Huffman_Coding as H
import Shannon_Coding as S
#符号 symbol
Symbols = 'aaaabbbccd'
N = 2
R = 4
symbol_probabilities = [['a', 0.4], ['b', 0.3], ['c', 0.2], ['d', 0.1]]
#N重编码，每次发N个符号
#e.g symbol='aaaabbbccd'
# 如果N=1 发送'a' 'a' 'a' 'a' 'b' 'b' 'b' 'c' 'c' 'd'，对应a,b,c,d的probability
# 如果N=2 发送'aa' 'aa' 'bb' 'bc' 'cd'，对应aa,bb,bc,cd的probability
N = 2
#进制 Radix
R = 2
#Encoding_Info = H.Huffman_Coding(Symbols,N,R)
Encoding_Info = H.huffman_encode(symbol_probabilities,R,N)
print(Encoding_Info)