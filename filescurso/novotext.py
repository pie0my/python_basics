from translate import Translator

translator = Translator(to_lang="pt")

try:
    with open('./seraa.txt', mode='r') as my_file:
        texto = my_file.read()
        translation = translator.translate(texto)
        with open('./traduzido.txt', mode='w') as my_file2:
            traduzido = my_file2.write(translation)
except FileNotFoundError as e:
    print('checa o path')
