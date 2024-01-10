'''  Translator to change vowel into h '''

def transl(phrase):
    transalte =""

    for i in phrase:
        if i in "AEIOUaeiou":
            if i.isupper() :
                 transalte = transalte + "H"
            else:
                transalte = transalte + "h"

        else:
            transalte =  transalte + i
    return transalte

print(transl(input('Enter a phrase : ')))


