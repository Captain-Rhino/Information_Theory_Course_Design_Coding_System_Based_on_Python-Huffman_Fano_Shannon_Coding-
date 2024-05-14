import Huffman_Coding as H
import Fano_Coding    as F
import Shannon_Coding as S
import numpy as np
from collections import Counter
def sort_symbol(Symbols):
    symbol_counts = Counter(Symbols)
    # 计算总字母数
    total_symbols = len(Symbols)
    # 计算每个字母的概率
    symbol_probabilities = [[symbol, count / total_symbols] for symbol, count in symbol_counts.items()]
    # 从大到小排序
    symbol_probabilities = sorted(symbol_probabilities, key=lambda x: x[1], reverse=True)
    return symbol_probabilities
#任意种编码都需要的操作
# 符号 symbol
Symbols = input('Symbols:')
while len(Symbols)>15 or len(Symbols)<8:
    Symbols = input('Ensure input symbols_length is between 8 and 15(including 8 and 15)')

symbol_probabilities = sort_symbol(Symbols)
total_symbols = len(symbol_probabilities)
#这里是Huffman_Encoding
#Huffman编码需要N和R
#e.g symbol='aaaabbbccd'
# 如果N=1 发送'a' 'a' 'a' 'a' 'b' 'b' 'b' 'c' 'c' 'd'，对应a,b,c,d的probability
# 如果N=2 发送'aa' 'aa' 'bb' 'bc' 'cd'，对应aa,bb,bc,cd的probability
N = int(input('选择N重信源编码，1<=N<=3，同时注意symbol_length是N的整数倍:\n'))
while N>3 or N<1 or total_symbols % N != 0:
    N = int(input('1<=N<=3，注意symbol_length是N的整数倍!!!\n'))

#进制 Radix
R = int(input('选择R进制Huffman编码，2<=R<=5:\n'))
while R>5 or R<2:
    R = int(input('选择R进制Huffman编码，注意2<=R<=5！:\n'))

#得到huffman编码表(      e.g.:  (a:001,b:010....)          )
Huffman_table = H.huffman_encode(symbol_probabilities,R,N)#这里输入的symbol_prob...务必按照从大到小排序
print('Huffman编码表:\n',Huffman_table)
# for symbol,huffman_code in Huffman_table.items():
#     print(symbol,huffman_code,'\n')

#得到编码后的结果,平均码长，信息熵
pre_coding_symbol =  [Symbols[i:i+N] for i in range(0, len(Symbols), N)]
Symbols_After_Huffman_Encoding =[]

#1.对照Huffman码表编码，打印编码后的Symbols
for i in pre_coding_symbol:
    for symbol,huffman_code in Huffman_table.items():
        if i==symbol:
            Symbols_After_Huffman_Encoding.append(huffman_code)
print('经过Huffman编码后的信息:',Symbols_After_Huffman_Encoding)
#2.计算并打印平均码长
Aver_len_H = H.aver_code_length(symbol_probabilities,R,N)
print('平均码长:',Aver_len_H)
#3.计算并打印信息熵以及编码效率
Info_Entropy_H = H.Entropy(symbol_probabilities,N)
print('N重信源编码后的信息熵:',Info_Entropy_H)
Ave_l_lbr_H = Aver_len_H * np.log2(R)
Encoding_Efficiency_H = Info_Entropy_H / Ave_l_lbr_H
print('编码效率:',Encoding_Efficiency_H)
#---Huffman END---


#这里是Fano_Encoding
Symbols_After_Fano_Encoding = []
Fano_table = F.fano_encode(symbol_probabilities)#这里输入的symbol_prob...务必按照从大到小排序
print('\nFano编码表:\n',Fano_table)

#1.对照Fano码表编码，打印编码后的Symbols
for i in Symbols:
    for symbol,fano_code in Fano_table.items():
        if i==symbol:
            Symbols_After_Fano_Encoding.append(fano_code)
print('经过Fano编码后的信息:',Symbols_After_Fano_Encoding)

#2.计算并打印平均码长
Aver_len_F = F.aver_code_length(symbol_probabilities)
print('平均码长:',Aver_len_F)
#3.计算并打印信息熵以及编码效率
Info_Entropy_F = F.Entropy(symbol_probabilities)
print('N重信源编码后的信息熵:',Info_Entropy_F)
Ave_l_lbr_F = Aver_len_F * np.log2(2)
Encoding_Efficiency_F = Info_Entropy_F/Ave_l_lbr_F
print('编码效率:',Encoding_Efficiency_F)
#---Fano END---



#这里是Shannon_Encoding
print(symbol_probabilities)
Symbols_After_Shannon_Encoding = []
Shannon_table = S.shannon_encode(symbol_probabilities)#这里输入的symbol_prob...务必按照从大到小排序
print('\nShannon编码表:\n',Shannon_table)

#1.对照Shannon_码表编码，打印编码后的Symbols
for i in Symbols:
    for symbol,fano_code in Shannon_table.items():
        if i==symbol:
            Symbols_After_Shannon_Encoding.append(fano_code)
print('经过Shannon编码后的信息:',Symbols_After_Shannon_Encoding)

#2.计算并打印平均码长
Aver_len_S= S.aver_code_length(symbol_probabilities)
print('平均码长:',Aver_len_S)
#3.计算并打印信息熵以及编码效率
Info_Entropy_S = S.Entropy(symbol_probabilities)
print('N重信源编码后的信息熵:',Info_Entropy_S)
Ave_l_lbr_S = Aver_len_S * np.log2(2)
Encoding_Efficiency_S = Info_Entropy_S/Ave_l_lbr_S
print('编码效率:',Encoding_Efficiency_S)