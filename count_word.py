#El objetivo de este programa es contar el No. de veces que aparece cada palabra en el texto
texto = "Este texto tiene algunas palabras Este es otro texto con algunas palabras diferentes"
words = texto.split(" ")
words_dicts = {}
for word in words:
    if word in words_dicts:
        words_dicts[word] += 1
    else:
        words_dicts[word] = 1

for word, counter in words_dicts.items():
    print("Palabra: ", word, "====No. de veces: ", counter)

