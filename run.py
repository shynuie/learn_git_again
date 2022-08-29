def add(arg1: int, arg2: int):
    return arg1 + arg2


if __name__ == "__main__":
    arg1 = int(input("Enter first value: "))
    arg2 = int(input("Enter second value: "))
    print(f"sum = {add(arg1=arg1, arg2=arg2)}")
