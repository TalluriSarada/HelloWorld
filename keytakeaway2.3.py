for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')

#capitalize() – changes all string letters to capitals;
#center() – centers the string inside the field of a known length;
#count() – counts the occurrences of a given character;
#join() – joins all items of a tuple/list into one string;
#lower() – converts all the string's letters into lower-case letters;
#lstrip() – removes the white characters from the beginning of the string;
#replace() – replaces a given substring with another;
#rfind() – finds a substring starting from the end of the string;
#rstrip() – removes the trailing white spaces from the end of the string;
#split() – splits the string into a substring using a given delimiter;
#strip() – removes the leading and trailing white spaces;
#swapcase() – swaps the letters' cases (lower to upper and vice versa)
#title() – makes the first letter in each word upper-case;
#upper() – converts all the string's letter into upper-case letters.

        s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])
#endswith() – does the string end with a given substring?
#isalnum() – does the string consist only of letters and digits?
#isalpha() – does the string consist only of letters?
#islower() – does the string consists only of lower-case letters?
#isspace() – does the string consists only of white spaces?
#isupper() – does the string consists only of upper-case letters?
#startswith() – does the string begin with a given substring?

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)

s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)
