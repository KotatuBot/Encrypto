from convert import Convert
from mode import Mode
from crypto_exec import Crypto_Exec
"""
test python
"""

def CBC_test1():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec()
    string = "THISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    b = ce.block_split(string)
    value = cb.convert_bin(b)
    IV = "B"*16
    t = mode.IV_genrate(IV)
    test = mode.CBC_encrypto(value,t)
    atai = mode.CBC_decrypto(test,t)
    correct = cb.convert_str(atai)
    print(correct)

def CFB_test():
    mode = Mode()
    cb = Convert()
    value = cb.convert_bin("*&*#JLJFLJFlasjlfj5362")
    test = mode.CFB_encrypto(value,15)
    print(test)
    correct = mode.CFB_decrypto(test,15)
    print(correct)
    t = cb.convert_str(correct)
    print(t)


def OFB_test():
    mode = Mode()
    cb = Convert()
    value = cb.convert_bin("*&*#JLJFLJFlasjlfj5362")
    encrypto = mode.OFB_mode(value,15)
    print(encrypto)
    decrypto = mode.OFB_mode(encrypto,15)
    print(decrypto)
    t = cb.convert_str(decrypto)
    print(t)

def CTR_test():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec()
    string = "This is your name eding "
    b = ce.block_split(string)
    c = cb.convert_bin(b)
    t,stream_key = mode.Counter_mode(c,8,128,8)
    print("ango")
    print(t)
    v,test = mode.Counter_mode(t,8,128,8,mode="decrypto",stream_key=stream_key)
    print("decrypto")
    test = cb.convert_str(v)
    print(test)



if __name__ == "__main__":
    CBC_test1()
