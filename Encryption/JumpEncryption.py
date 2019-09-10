import string
h='abcdefghijklmnopqrstuvwxyz'


w1='sdwp'
w2='pbzcnal'
w3='ijxnlsji'
w4='uif'
w5='eykc'
w6='sqzuq'
result=""

def num(x,y,result):
    result = ""
    for char in x:
        index = string.ascii_lowercase.index(char)+y
        if index >25:
            index =index-26
            abs(index)
        result += h[index]
    return result

for x in range(0,26):
    result = num(w6,x,result)
    print(result)



