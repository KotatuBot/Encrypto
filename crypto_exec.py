class Crypto_Exec():

    def __init__(self,bit):
        self.size = int(bit/8)

    def padding_genrate(self,padding_len):
        p_list = []
        for j in range(padding_len):
            p_list.append(padding_len)

        return p_list

    def block_add(self,value,padding):
        value_change = value[-1]+padding
        value[-1] = value_change
        print(padding)
        return value

    def strip_padding(self,value,padding):
        if padding[0] > 0:
            test = self.size - padding[0]
            e = value[-1][:test]
            value[-1] = e
        return value





    def block_split(self,value):
        """
        ブロックごとに分割する.

        Return:
            block_list -> ブロックのリスト
        """
        padding_list = []
        if len(value)%self.size != 0:
            padding = self.size - int(len(value) % self.size)
            if padding > 0:
                padding_list = self.padding_genrate(padding)

        block_list = []
        moding = len(value) % self.size
        for number in range(int(len(value)/self.size)):
            number += 1
            size_start = self.size * (number -1)
            size_end = self.size * number
            value_s = value[size_start:size_end]
            block_list.append(value_s)
        if moding > 0:
            block_list.append(value[size_end:])

        print(block_list)

        return block_list,padding_list



if __name__ == "__main__":
    ce = Crypto_Exec(128)
    t,v = ce.block_split("AAAAAABBBBBBBBCCCCCCCCDDD")
    print(t)
    print(v)
