#符号数: Q:[8-15] ,进制R:[2-5], 重序列N:[1-3]
from collections import Counter
def Huffman_Coding(Q,N,R):
    #judge Q,R,N is legal
    if len(Q)>=8 and len(Q)<=15 and R>=2 and R<=5 and N>=1 and N<=3:
    #state is true
    #calculate P of every symbol
        letter_counts = Counter(Q)

    # 计算每个字母出现的概率
        total_letters = len(Q)
        letters = []
        probabilities = []
        for letter, count in letter_counts.items():
            letters.append(letter)
            probabilities.append(count / total_letters)
        print(letters,probabilities)
    else:
        State = 'Illegal Input,try again plz'
        return State

