try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.') 

    try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)        
except ValueError:
    print('I do not know what to do.')    
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')    
except:
    print('Something strange has happened here... Sorry!')
    #ZeroDivisionError  division in which the divider is zero Yes, they are: /, //, and %.
    #ValueError when a function (like int() or float()) receives an argument of a proper type
    #TypeError when you try to apply a data whose type cannot be accepted in the current context
    #AttributeError  when you try to activate a method which doesn't exist in an item you're dealing with
    #SyntaxError This exception is raised when the control reaches a line of code which violates Python's grammar