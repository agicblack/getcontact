from collections import Counter
import operator
from natasha import NamesExtractor

def name_max(text):
    extractor = NamesExtractor()
    matches = extractor(text)
    name_natasha = []
    for match in matches:
        start, stop = match.span
        name_massiv = text[start:stop]
        name_natasha.append(name_massiv)

    counter = dict(Counter(name_natasha))
    max_name = max(counter.items(), key=operator.itemgetter(1))[0]
    return max_name

text = '''
    Андрей Тимофеев
    Андрей Спб
    Андрей Челентос
    Андрей Катин
    Андрей
     Онлрей
     Экс Бойфренд Aka Реальный Долбоеб
     Андрей Chelentos
     Andrey Tymofeev
     Андрей Тим
     Андрюша :
     Андрей 💑
     .andrey
     Andrey
'''
test=name_max(text)
print(test)
#

