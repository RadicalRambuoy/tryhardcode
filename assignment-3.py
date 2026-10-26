from itertools import permutations
 
w1 = input("First word: ").upper()
w2 = input("Second word: ").upper()
res = input("Result word: ").upper()
 
letters = list(dict.fromkeys(w1 + w2 + res))
if len(letters) > 10:
    print("More than 10 unique letters. No solution.")
    exit()
 
def value(word, a):
    return int("".join(str(a[ch]) for ch in word))
 
for perm in permutations(range(10), len(letters)):
    a = dict(zip(letters, perm))
    if 0 in (a[w1[0]], a[w2[0]], a[res[0]]):
        continue
    if value(w1, a) + value(w2, a) == value(res, a):
        for ch in letters:
            print(ch, "=", a[ch])
        print(value(w1, a), "+", value(w2, a), "=", value(res, a))
        break
else:
    print("No solution found.")