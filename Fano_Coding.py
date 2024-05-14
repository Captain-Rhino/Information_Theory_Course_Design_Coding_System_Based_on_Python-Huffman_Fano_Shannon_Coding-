import numpy as np
def fano_encode(symbol_probabilities, code='', codes={}):
    if len(symbol_probabilities) == 1:
        codes[symbol_probabilities[0][0]] = code
        return codes
    total_probability = sum(prob for symbol, prob in symbol_probabilities)
    half_probability = 0
    min_difference = float('inf')
    split_index = -1
    for i, (symbol, prob) in enumerate(symbol_probabilities):
        half_probability += prob
        difference = abs(half_probability - total_probability / 2)
        if difference < min_difference:
            min_difference = difference
            split_index = i
    fano_encode(symbol_probabilities[:split_index + 1], code + '0', codes)
    fano_encode(symbol_probabilities[split_index + 1:], code + '1', codes)
    return codes

#计算平均码长
def aver_code_length(symbol_probabilities):
    aver_len = 0
    fano_code = fano_encode(symbol_probabilities)
    for i in symbol_probabilities:
        for symbol,code in fano_code.items():
            if i[0]==symbol:
                aver_len += i[1]*len(code)
    return aver_len

#计算信息熵
def Entropy(symbol_probabilities):
    entropy = 0
    for i in symbol_probabilities:
        entropy += i[1] * np.log2( 1 / i[1] )
    return entropy
# 示例使用
# symbol_probabilities = [['a', 0.4], ['b', 0.3], ['c', 0.2], ['d', 0.1]]
# fano_codes = fano_encode(symbol_probabilities)
# ave_len = aver_code_length(symbol_probabilities)
# Info_entropy = Entropy(symbol_probabilities)
# print("Fano Codes:\n",fano_codes,"Aver_length:\n",ave_len,'\nInfo_Entropy:\n',Info_entropy)


