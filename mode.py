class Mode(self):
    def __init__(self):
        pass

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
                encrypto_value = encrypto(xor_result)
                encrypto_list.append(encrypto_value)
            encrypto_value = encrypto_list[-1]^tip
            encrypto_list.append(encrypto_value)
        return encrypto_list

    
        
