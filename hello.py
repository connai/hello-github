def say_hello(name):
    return f"你好，{name}！欢迎来到 GitHub。"


def add(a, b):
    """返回两数之和"""
    return a + b


if __name__ == "__main__":
    print(say_hello("wuxiuxiao"))
    print(f"1 + 2 = {add(1, 2)}")
