import binascii
class Convert():
    def __init__(self):
        pass

    def convert_bin(self,value):
        """
        文字列を倫理演算できるようにする.
        args:
            vaule -> String 
                     ex) "Hello"
        return:
            bin_l -> list [] int
                    ex) [14,56,78,36,5]
        """
        bin_merge_l = []
        for j in value:
            j_string = "".join(j)
            hex_value = binascii.hexlify(bytes(j_string.encode("utf-8")))
            count = len(hex_value)/2

            bin_l = []
            for number in range(int(count)):
                hex_str = "0x" + str(hex_value[number*2:(number+1)*2].decode("utf-8"))
                bins = int(hex_str,base=16)
                bin_l.append(bins)
            bin_merge_l.append(bin_l)

        return bin_merge_l

    def convert_str(self,value):
        """
        数値を文字列に治す
        args:
            value -> list [] int
                     ex) [14,65,35,35]

        return:
            original_string -> string
                    ex) "Hello"

            
        """
        original_string = ""
        for s_value in value:
            original_l = []
            for val in s_value:
                original_l.append(chr(val))

            tmp_string = "".join(original_l)
            original_string += tmp_string

        return original_string

