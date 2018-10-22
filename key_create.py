from Crypto import Random

class Key_Create():
    def __init__(self):
        self.counter = Counter_N(None,None)

    def create_key(self,bit_len):
        key_size = int(bit_len/8)
        key_bin = Random.get_random_bytes(key_size)
        tmp_list = []
        for j in range(key_size):
            counter = j +1
            t = key_bin[j:counter]
            numbers = int.from_bytes(t,'big')
            tmp_list.append(numbers)
        return tmp_list

