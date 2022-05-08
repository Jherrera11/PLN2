'''
Jose Juan Herrera Reyes    6°B    ICI
'''
import nltk
nltk.download('stopwords')
print("Jose Juan Herrera Reyes")
carpeta_nombre="D:\\Documentos\\6-B\\Optativa\\Documentos\\"
archivo_nombre = "Archivo.txt"
with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
print("------------------------------------------")
palabras_funcionales=nltk.corpus.stopwords.words("spanish")
for palabras_funcioal in palabras_funcionales:
    '''print(palabras_funcioal)'''
print("------------------------------------------")
tokens=nltk.word_tokenize(texto,"spanish")
tokens_limpios=[]
for token in tokens:
    if token not in palabras_funcionales:
        tokens_limpios.append(token)
        '''print(tokens_limpios)'''
print(len(tokens))
print(len(tokens_limpios))
texto_limpio_nltk=nltk.Text(tokens_limpios)
distribucion_limpia=nltk.FreqDist(texto_limpio_nltk)
distribucion_limpia.plot(40)