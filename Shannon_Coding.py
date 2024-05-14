import numpy as np
import math
def shannon_encode(symbol_probabilities):
    shannon_codes={}
    for i in range(len(symbol_probabilities)):
        pre_prob = 0
        prob_i = symbol_probabilities[i][1] #第i个的概率
        code_len_i = math.ceil(np.log2(1 / symbol_probabilities[i][1]))#第i个的码长
        for j in range(i):#第i个之前（0 -> i - 1）的前项概率和
            pre_prob += symbol_probabilities[j][1]
        bin_i = de2bi(pre_prob)#这里返回去除掉 ’0.‘ 后的二进制数

        shannon_code_i = ''.join(bin_i[0:code_len_i])
        shannon_codes[symbol_probabilities[i][0]] = shannon_code_i
        #print(prob_i, code_len_i, pre_prob,bin_i,'    ',shannon_code_i,'\n')
    return shannon_codes


#十进制小数转二进制
def de2bi(dec):
    result = []         #result = [‘0.‘]
    for i in range(30):
        dec = dec * 2
        dec_int = int(dec)
        result.append(str(dec_int))
        dec = dec - dec_int
        #if dec == 0:
            #break
    return result


def aver_code_length(symbol_probabilities):
    aver_len = 0
    shannon_code = shannon_encode(symbol_probabilities)
    for i in symbol_probabilities:
        for symbol,code in shannon_code.items():
            if i[0]==symbol:
                aver_len += i[1]*len(code)
    return aver_len

#计算信息熵
def Entropy(symbol_probabilities):
    entropy = 0
    for i in symbol_probabilities:
        entropy += i[1] * np.log2( 1 / i[1] )
    return entropy

# symbol_probabilities = [['e', 0.4], ['n', 0.1], ['w', 0.1], ['b', 0.1], ['v', 0.1], ['r', 0.1], ['y', 0.1]]
# #
# shannon_encode(symbol_probabilities)
# b = aver_code_length(symbol_probabilities)
# c = Entropy(symbol_probabilities)
# print(a,'\n',b,'\n',c)
# # for i in range(len(symbol_probabilities)):
#     pre_prob = 0
#     prob_i = symbol_probabilities[i][1]  # 第i个的概率
#     code_len_i = math.ceil(np.log2(1 / symbol_probabilities[i][1]))  # 第i个的码长
#     for j in range(i):  # 第i个之前（0 -> i - 1）的前项概率和  ( python特性取不到i )
#         pre_prob += symbol_probabilities[j][1]

# fano_codes = fano_encode(symbol_probabilities)
# ave_len = aver_code_length(symbol_probabilities)
# Info_entropy = Entropy(symbol_probabilities)
# print("Fano Codes:\n",fano_codes,"Aver_length:\n",ave_len,'\nInfo_Entropy:\n',Info_entropy)
