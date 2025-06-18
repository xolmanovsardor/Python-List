from task05 import max_words


words = ['salom' , 'hi' , 'bonjur' , 'privet'] 

max_length = len (words[0])
for word in words:
    if len (word) > max_length:
        max_length = len(word)



for word in words:
    if len (word) == max_length:
        max_words.append(word)

print(max_words)