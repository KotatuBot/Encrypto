from Crypto.Util import *
from Crypto import Random


class Counter_
def byte_number(value):
    tmp_list = []
    for j in range(8):
        counter = j +1
        t = value[j:counter]
        numbers = int.from_bytes(t,'big')
        tmp_list.append(numbers)
    return tmp_list


nonce = Random.get_random_bytes(8)

noce_list = byte_number(nonce)
   
# counter
bit_len = 128
byte_len = int(bit_len/8 - len(noce_list))

counter = 1
counter_number = counter.to_bytes(byte_len,'big')
counter_list = byte_number(counter_number)
