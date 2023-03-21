word = input("Please Enter a word: ").lower()
text = input("Please Enter a text: ").lower()
found = True
start = 0


for ch in word:
    pos = text.find(ch , start)
    if pos <0:
        found = False
    break
    start = pos + 1
if found:
    print("Yes")
else:
    print("No")
