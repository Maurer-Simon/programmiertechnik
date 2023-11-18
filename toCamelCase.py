#Problem from Codewars.com instead of writing text with "-" and "_" these
#symbols should be replaced and the letter afterwards should be written in Uppercase.

def to_camel_case(text):
    for i in text:
        if i == "-" or i == "_":
            x = text.index(i)
            upperLetter = text[x+1].upper()
            text = text[0 : x : ] + upperLetter + text[x+1 + 1 : :]
    return text


print(to_camel_case('the_pippi_Was-Hungry'))
print(to_camel_case('the-cat-is-evil'))