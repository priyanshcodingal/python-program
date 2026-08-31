try:
    name=input("enter a username")
    numerator=int(input("enter the numerator"))
    denumerator=int(input("enter denominator"))
    result = numerator/denumerator
except ZeroDivisionError as e:
    print("execption : ",e)
except ValueError as e:
    print("Excpetion : ",e)
except:
    print("Invalid Choice")
finally:
    print("This will execute no matter what")


    
