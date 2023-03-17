k = int(input("Enter the number of words: "))
words_count = {}
distinct = []

for i in range(k):
    while True:
        word = input("Enter a lowercase word: ").strip()
        if word.islower():
            break
        else:
            print("Input only lowercase letters.")
    
    if word in words_count:
        words_count[word] += 1
    else:
        words_count[word] = 1
        distinct.append(word)
        
print("Number of distinct words:", len(distinct))
for word in distinct:
    print(words_count[word], end=' ')
print()






