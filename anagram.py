def check(s1, s2):
    s1 = s1.replace(" ", "")
    s2 =  s2.replace(" ", "")

    if(sorted(s1.lower()) == sorted(s2.lower())):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        

s1 = input("Please Enter the First String: ")
s2 = input("Please Enter the Second String: ")
check(s1, s2)
