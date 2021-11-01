roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
roman1 = {}
roman1["I"]=1
roman1["V"]=5
roman1["X"]=10
#i tak dalej
roman2 = dict([("I", 1), ("V", 5), ("X", 10), ("L", 50), ("C", 100), ("D", 500), ("M", 1000)])
def roman2int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    i = 0
    number = 0
    while i < len(s):
            if s[i] != s[-1] and roman[s[i]] < roman[s[i+1]]:
                number+=roman[s[i+1]]
                number-=roman[s[i]]
                i+=2
            else:
            number+=roman[s[i]]
            i+=1
    print(number)
def roman2int2(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    s = s.replace("IV", "IIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("IX", "VIIII")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    for char in s:
        number+=roman[char]
    print(number)






