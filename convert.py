import binascii

class Convert_Bin():
    def __init__(self):
        pass

    def convert_bin(value):
        """
        文字列を倫理演算できるようにする.
        """
        hex_value = binascii.hexlify(bytes(value.encode("utf-8")))
        count = len(hex_value)/2

        bin_l = []
        for number in range(int(count)):
            hex_str = "0x" + str(hex_value[number*2:(number+1)*2].decode("utf-8"))
            bins = int(hex_str,base=16)
            bin_l.append(bins)

        return bin_l

