def isYearLeap(year):   # Leap year formula
    if year % 4 == 0 and year % 100 != 0 :     
        return True 
    elif year % 400 == 0 :
        return True
    else :
        return False
                
testData = [1900, 2000, 2016, 1987]         # Test Data as reference
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")