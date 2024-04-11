def f(word_in, cypher, step):
    """
    Функция шифрования и дешифрования
    параметры word_in: текст
    параметры cypher: 1 - кодирование, -1 - декодирование
    параметры step: шаг шифрования 0 по длине слова
    возвращает: зашифрованный или дешифрованный текст
    """
    word_out = ''
    tmp = ''
    for a in word_in + ' ':
        if a.isalpha():
            tmp += a
        else:
            if tmp:
                for b in tmp:
                    x = (step if step > 0 else len(tmp)) * cypher  # шаг шифрования и дешифрования
                    abc_count = 26 if ord(b) < 123 else 32
                    if b.isupper():
                        abc_code = 65 if ord(b) < 123 else 1040
                        c = (ord(b) - abc_code + x) % abc_count + abc_code
                    else:
                        abc_code = 97 if ord(b) < 123 else 1072
                        c = (ord(b) - abc_code + x) % abc_count + abc_code
                    word_out += chr(c)
            tmp = ''
            word_out += a
    return word_out[:-1]

q = input('Введите текст: ')
q1 = int(input('1 - кодирование, -1 - декодирование: '))
q2 = int(input('Шаг шифрования 0 по длине слова: '))
print(f(q, q1, q2))

# Enter text: Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.
# 1 - кодирование, -1 - декодирование: -1
# Шаг шифрования 0 по длине слова: 25
# The grass is always greener on the other side of the fence.
