def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()

    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()

        else:
            words[i] = words[i].upper()

    return " ".join(words)

sentence = input()
result = reverse_sentence(sentence)
print(result)
    
# ------------------------------------------------------------------
"""
def reverse_words(sentence):
    words = sentence.split()  
    words.reverse()  
    return " ".join(words)  
 
print(reverse_words(sentence))
"""