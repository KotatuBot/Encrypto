from convert import Convert
from mode import Mode
from crypto_exec import Crypto_Exec
from key_create import Key_Create
"""
test python
"""

def CBC_test1():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec(128)
    string = "THISAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATTTTTTTTTTTTT"
    # ブロック分割
    b,padding = ce.block_split(string)
    # intのリスト型に分割
    value = cb.convert_bin(b)
    # paddingを付与
    value = ce.block_add(value,padding)
    IV = "B"*16
    # IV生成
    t = mode.IV_genrate(IV)
    # 暗号化
    test = mode.CBC_encrypto(value,t)
    # 復号
    atai = mode.CBC_decrypto(test,t)
    # padding除去
    ce.strip_padding(atai,padding)
    # 文字列に直す
    correct = cb.convert_str(atai)
    print(correct)

def CFB_test():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec(128)
    string = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    b = ce.block_split(string)
    value = cb.convert_bin(b)
    IV = "C"*16
    t = mode.IV_genrate(IV)
    testd = mode.CFB_encrypto(value,t)
    correct = mode.CFB_decrypto(testd,t)
    td = cb.convert_str(correct)
    print(td)


def OFB_test():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec(128)
    string = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    b = ce.block_split(string)
    value = cb.convert_bin(b)
    IV = "B"*16
    t = mode.IV_genrate(IV)
    encrypto = mode.OFB_mode(value,t)
    decrypto = mode.OFB_mode(encrypto,t)
    t = cb.convert_str(decrypto)

def CTR_test():
    mode = Mode()
    cb = Convert()
    ce = Crypto_Exec(128)
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

def key_test():
    kc = Key_Create()
    b = kc.create_key(256)
    print(b)



if __name__ == "__main__":
    CBC_test1()
