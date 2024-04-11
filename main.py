def f(word_in, cypher, step_count):
    """
    Функция шифрования и дешифрования
    параметры word_in: текст
    параметры cypher: 1 - кодирование, -1 - декодирование
    параметры step_count: шаг шифрования или 0 по длине слова
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
                    x = (step_count if step_count > 0 else len(tmp)) * cypher  # шаг шифрования и дешифрования
                    abc_count = 26 if ord(b) < 123 else 32  # количество букв в алфавите 26 или 32
                    if b.isupper():
                        abc_code = 65 if ord(b) < 123 else 1040  # код буквы в английском и русском алфавите
                        character = (ord(b) - abc_code + x) % abc_count + abc_code  # шифрование и дешифрование букв
                    else:
                        abc_code = 97 if ord(b) < 123 else 1072
                        character = (ord(b) - abc_code + x) % abc_count + abc_code
                    word_out += chr(character)
            tmp = ''
            word_out += a
    return word_out[:-1]


q = input('Введите текст: ')
q1 = int(input('1 - кодирование, -1 - декодирование: '))
q2 = int(input('Целое число, шаг шифрования или 0 по длине слова: '))
print(f(q, q1, q2))

# Введите текст: АA - первая буква кириллица вторая буква латиница
# 1 - кодирование, -1 - декодирование: 1
# Целое число, шаг шифрования или 0 по длине слова: 1
# БB
