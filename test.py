from convert import Convert
from mode import Mode
"""
test python
"""

def CBC_test1():
    mode = Mode()
    cb = Convert()
    value = cb.convert_bin("*&*#JLJFLJFlasjlfj5362")
    test = mode.CBC_encrypto(value,15)
    atai = mode.CBC_decrypto(test,15)
    print(atai)
    correct = cb.convert_str(atai)
    print(correct)


if __name__ == "__main__":
    CBC_test1()
