class Crypto_Exec():

    def __init__(self):
        self.size = 6
        self.padding = "A"


    def block_split(self,value):
        """
        ブロックごとに分割する.

        Return:
            block_list -> ブロックのリスト
        """
        if len(value)%self.size != 0:
            padding = self.size - int(len(value) % self.size)
            paddings = ""
            for count in range(padding):
                paddings += self.padding
            value += paddings

        block_list = []
        for number in range(int(len(value)/self.size)):
            number += 1
            size_start = self.size * (number -1)
            size_end = self.size * number
            value_s = value[size_start:size_end]
            block_list.append(value_s)

        return block_list


if __name__ == "__main__":
    ce = Crypto_Exec()
    t = ce.block_split("AAAAAABBBBBBBBCCCCCCCC")
    print(t)
