
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        if self.input_string:
            print(self.input_string.upper())
        else:
            print("No string to print.")


string_manipulator = StringManipulator()


string_manipulator.getString()


string_manipulator.printString()
