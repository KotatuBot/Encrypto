from convert import Convert_Bin

class Mode():
    def __init__(self):
        pass

    def encrypto(self,values):
        return values

    def decrypto(self,values):
        return values


    def ECB_encrypto(self,value):
        encrypto_list = []
        for tip in value:
            encrypto_S = encrypto(value)
            encrypto_list.append(encrypto_S)
        return encrypto_list

    def ECB_decrypto(self,value):
        decrypto_list = []
        for tip in value:
            decrypto_S = decrypto(value)
            decrypto_list.append(decrypto_S)

        return decrypto_list

    def CBC_encrypto(self,hira_value,IV):
        encrypto_list = []
        for number,tip in enumerate(hira_value):
            if number == 0:
                xor_result = IV^tip
                encrypto_value = self.encrypto(xor_result)
                encrypto_list.append(encrypto_value)
            else:
                encrypto_value = encrypto_list[-1]^tip
                values = self.encrypto(encrypto_value)
                encrypto_list.append(values)
        return encrypto_list

    def CBC_decrypto(self,encrypto_value,IV):
        decrypto_list = []
        for number,tip in enumerate(encrypto_value):
            decrypto_txt = self.decrypto(tip)
            if number == 0:
                xor_result = IV^decrypto_txt
                decrypto_list.append(xor_result)
            else:
                # encrypto value ^ encrypto value +1
                xor_result = encrypto_value[number-1]^decrypto_txt
                decrypto_list.append(xor_result)

        return decrypto_list


if __name__ == "__main__":
    mode = Mode()
    cb = Convert_Bin()
    value = cb.convert_bin("*&*#JLJFLJFlasjlfj5362")
    test = mode.CBC_encrypto(value,15)
    atai = mode.CBC_decrypto(test,15)
    print(atai)
    correct = cb.convert_str(atai)
    print(correct)


    
        
