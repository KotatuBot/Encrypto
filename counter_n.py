from Crypto.Util import *
from Crypto import Random


class Counter_N():
    def __init__(self,Byte,bit_length):
        """
        Byte -> 8
        bit_length -> 128
        """
        self.nonce_list = ""
        self.byte = Byte
        self.counter = 1
        self.counter_list = []
        self.bit_len = bit_length
        self.stream_key = []

    def byte_number(self,value):
        tmp_list = []
        for j in range(8):
            counter = j +1
            t = value[j:counter]
            numbers = int.from_bytes(t,'big')
            tmp_list.append(numbers)
        return tmp_list

    def noce_genrate(self):
        self.nonce = Random.get_random_bytes(self.byte)
        self.nonce_list = self.byte_number(self.nonce)


    def counter_genrate(self):
        byte_len = int(self.bit_len/8 - len(self.nonce_list))

        counter_number = self.counter.to_bytes(byte_len,'big')
        number = self.byte_number(counter_number)
        self.counter_list.append(number)

    def counter_block(self,block_number):
        for n in range(block_number):
            self.counter_genrate()
            self.counter += 1

    def merge_block(self):
        stream_key = []
        for block in self.counter_list:
            block_value = self.nonce_list + block 
            self.stream_key.append(block_value)


if __name__ == "__main__":
    cou = Counter_N(8,128)
    cou.noce_genrate()
    cou.counter_block(8)
    cou.merge_block()
    print(cou.stream_key)
