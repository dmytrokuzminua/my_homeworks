""" Homework 2 task 6 """


def create_calculator(operation: str):
    """ Create calculator function"""
    def calculate(x: int|float, y: int|float):
        """Create func for all operations"""
        if operation == "+":
            return x + y

        if operation == "-":
            return x - y

        if operation == "*":
            return x * y

        if operation == "/":
            if y != 0 :
                return x/y
            return "Неможна ділити на 0!"

        return "Невідомий оператор!"

    return calculate


def main():
    """main def"""
    add = create_calculator("+")
    subtract = create_calculator("-")
    multiply = create_calculator("*")
    divide = create_calculator("/")

    print(add(7, 3))
    print(subtract(12, 4))
    print(multiply(3, 7))
    print(divide(222, 2))


if __name__ == "__main__":
    main()
