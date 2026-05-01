def say_hello(name):
    return f"Hello, {name}! Welcome to GitHub."


def add(a, b):
    """返回两数之和"""
    return a + b


def subtract(a, b):
    """返回两数之差"""
    return a - b


def multiply(a, b):
    """返回两数之积"""
    return a * b


def divide(a, b):
    """返回两数之商，除数为0时返回错误提示"""
    if b == 0:
        return "错误：除数不能为0"
    return a / b


if __name__ == "__main__":
    print(say_hello("wuxiuxiao"))
    print(f"1 + 2 = {add(1, 2)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"3 x 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")
