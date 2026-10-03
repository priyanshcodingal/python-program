class employee:
    def __init__(self):
        print("constructor created!")
    def __del__(self):
        print("object deleted")

def create_obj():
    print("creating object,,,,,,,,,,,,")
    ob = employee()
    print("object created")
    del ob
    print("object deleted")
obj = create_obj()

    