alphabet = "abcdefghijklmnopqrstuvwxyz"
#Python strings are immutable
#del alphabet[0] alphabet.append("A")
print(alphabet[1])
#Don't think that a string's immutability limits your ability to operate with strings.
#will work without bending Python's rules,

alphabet = "bcdefghijklmnopqrstuvwxy"

alphabet = "a" + alphabet
alphabet = alphabet + "z"

print(alphabet)
