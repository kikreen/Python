import pymorphy2 
morph = pymorphy2.MorphAnalyzer() 
sentence = input("Введите предложение: ") 
words = sentence.split() 
for word in words: 
    PW = morph.parse(word)[0] 
    print(f"Слово: {word}, Лемма: {PW.normal_form}, Часть речи: {PW.tag.POS}, Падеж: {PW.tag.case}")