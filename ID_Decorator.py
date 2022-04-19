def idDecorator(card):
    print("+-------------------------------+")
    card()
    print("+-------------------------------+")

@idDecorators
def idCard():
    print("ID: XYZ123")
    print("Name: Pratiksha")
    print("Dept: Electronics")

    idCard()