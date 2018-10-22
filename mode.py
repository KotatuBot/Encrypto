from counter_n import Counter_N
from convert import Convert
class Mode():
    def __init__(self):
        pass

    def encrypto(self,values):
        return values

    def decrypto(self,values):
        return values

    def IV_genrate(self,IV):
        cb = Convert()
        IV_de = cb.convert_bin(IV)
        IV_list = [value[0] for value in IV_de]
        return IV_list

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
                xor_result = [ i^v for(i,v) in zip(IV,tip)]
                encrypto_value = self.encrypto(xor_result)
                encrypto_list.append(encrypto_value)
            else:
                encrypto_value = [ e^v for(e,v) in zip(encrypto_list[-1],tip)]
                values = self.encrypto(encrypto_value)
                encrypto_list.append(values)
        return encrypto_list

    def CBC_decrypto(self,encrypto_value,IV):
        decrypto_list = []
        for number,tip in enumerate(encrypto_value):
            decrypto_txt = self.decrypto(tip)
            if number == 0:
                xor_result = [i^d for(i,d) in zip(IV,decrypto_txt)]
                decrypto_list.append(xor_result)
            else:
                # encrypto value ^ encrypto value +1
                xor_result = [e^d for(e,d) in zip(encrypto_value[number-1],decrypto_txt)]
                decrypto_list.append(xor_result)

        return decrypto_list

    def CFB_encrypto(self,hira_value,IV):
        encrypto_list = []
        for number,tip in enumerate(hira_value):
            if number == 0:
                IV_en = self.encrypto(IV)
                xor_result = IV_en^tip
                encrypto_list.append(xor_result)
            else:
                encrypto_en = self.encrypto(encrypto_list[-1])
                xor_result = encrypto_en^tip
                encrypto_list.append(xor_result)
        return encrypto_list

    def CFB_decrypto(self,encrypto_value,IV):
        decrypto_list = []
        for number,tip in enumerate(encrypto_value):
            if number == 0:
                IV_de =  self.decrypto(IV)
                xor_result = IV_de^tip
                decrypto_list.append(xor_result)
            else:
                decrypto_de = self.decrypto(decrypto_list[-1])
                decrypto_value = decrypto_de^tip
                decrypto_list.append(decrypto_value)
        return decrypto_list 


    def OFB_mode(self,value,IV):
        value_list = []
        for number,tip in enumerate(value):
            if number == 0:
                IV_en = self.encrypto(IV)
                xor_result = IV_en^tip
                value_list.append(xor_result)
                stream_key = IV_en
            else:
                stream_key = self.encrypto(stream_key)
                xor_result = stream_key^tip
                value_list.append(xor_result)
        return value_list

    def Counter_mode(self,value_l,Nonce_byte,key_length,block,mode="encrypto",stream_key=None):
        if mode == "encrypto":
            counter = Counter_N(Nonce_byte,key_length)
            counter.noce_genrate()
            counter.counter_block(block)
            stream_key = counter.merge_block()
        
        mode_list = []
        for num in range(len(value_l)):
            tmp_list = []
            for nums in range(len(value_l[num])):
                xor_result = value_l[num][nums]^stream_key[num][nums]
                tmp_list.append(xor_result)
            mode_list.append(tmp_list)

        return mode_list,stream_key

