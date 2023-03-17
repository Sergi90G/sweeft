def bigger_is_Greater(w):
    if not w.isalpha():
        return "input must contain only letters"
    s = list(w)  
   
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    if i < 0:
        return "no answer"
  
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i+1:] = reversed(s[i+1:])
    return "".join(s)


t = int(input("enter the number: "))
for _ in range(t):
    w =input("enter lexicographical words: ").strip()
    print(bigger_is_Greater(w))