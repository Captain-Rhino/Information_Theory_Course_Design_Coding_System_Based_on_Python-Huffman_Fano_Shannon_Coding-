import Huffman_Coding as H
#符号 symbol
Symbols = 'Hello world'
#N重编码
N = 1
#进制 Number System
R = 2
Encoding_Info = H.Huffman_Coding(Symbols,N,R)
print(Encoding_Info)