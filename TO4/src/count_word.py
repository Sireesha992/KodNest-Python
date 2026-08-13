n = (8, "python", "java", "python", "sql","java","html","python")
word_frequency={}
for word in n:
    if word in word_frequency:
        word_frequency[word]+=1
    else:
        word_frequency[word]=1
for word, count in word_frequency.items():
    print(f"{word}:{count}")