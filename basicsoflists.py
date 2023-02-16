# step 1
beatles =[]
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 2
print("Step 2:", beatles)
# step 3
for member in range(2):
    beatleName = input("New Beatle Name? ")
    beatles.append(beatleName)
print("Step 3:", beatles)
# step 4
del beatles[3:5]
print("Step 4:", beatles)
# step 5
beatles.insert(0,"Ringo Starr")
print("Step 5:", beatles)
# testing list legth
print("The Fab", len(beatles))
