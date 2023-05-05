import pymorphy2


morph = pymorphy2.MorphAnalyzer()
i = morph.parse('галерея')[0].normal_form
print(i)