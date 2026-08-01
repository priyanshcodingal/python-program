medical_cause= input("enter your medical cause y/n  ")

if medical_cause == "y":
    print("you are allowed for the examination")
else:
    attendance = int(input("enter your atendance:"))
    if attendance >= 75:
        print("you are allowed for the examination")
    else:
      print("you are not allowed for the examination")

