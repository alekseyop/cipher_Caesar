def f(word_in):
    word_out = ''
    tmp = ''
    for a in word_in:
        if a.isalpha():
            tmp += a
        else:
            if tmp:
                for b in tmp:
                    if b.isupper():
                        c = (ord(b) - 65 + len(tmp)) % 26 + 65
                    else:
                        c = (ord(b) - 97 + len(tmp)) % 26 + 97
                    word_out += chr(c)
            tmp = ''
            word_out += a
    return word_out


print('Sample Input 1:\nDay, mice. "Year" is a mistake!\nSample Output 1:')
print(f('Day, mice. "Year" is a mistake!'))
print('------------------------------------')
print('Sample Input 2:\nmy name is Python!\nSample Output 2:')
print(f('my name is Python!'))
