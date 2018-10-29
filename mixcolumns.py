
class Mixcolumns():
    def __init__(self):
        self.galora = [
            ["0x02","0x03","0x01","0x01"],
            ["0x01","0x02","0x03","0x01"],      
            ["0x01","0x01","0x02","0x03"],
            ["0x03","0x01","0x01","0x02"],
            ]

    def mojiretu(self,b):
        """
        int -> bin を生成
        """
        c = bin(b)
        test = c[2:]
        counter = len(test)
        one = []
        for j in test:
            counter -= 1
            if j=="1":
                one.append(counter)

        return one

    def gred(self,t,e):
        """
        Mixcolumnの計算
        """
        test = [s + s1 for s in t for s1 in e]
        d = [x for x in set(test) if test.count(x) > 1]
        test2 = list(set(test))
        for delsd in d:
            test2.remove(delsd)
        test2.sort(key=int,reverse=True)
        return test2

    def bin_create(self,shisu_list):
        """
        指数のリストからbinを生成
        """
        mojiretu = ""
        for i in range(shisu_list[0]+1):
            if i in shisu_list:
                mojiretu += "1"
            else:
                mojiretu += "0"
        bin_c = mojiretu+"b0"
        c_bin = bin_c[::-1]
        return c_bin



    def ajest_byte(self,x):
        #x**8 + x**4 + x**3+x+x**0
        y = "0b100011011"
        while True:
            if len(x)>10:
                s = len(x) - len(y)
                if s!=0:
                    x1 = x[:-s]
                    amari = len(x)+(-s)
                    x2 = x[amari:]
                else:
                    x1 = x
                    x2 =""
                x3 = int(str(x1),2)
                y1 = int(y,2)
                result = bin(x3^y1)
                x = result+x2
            else:
                break
        return int(x,2)

    def xor_int(self,lists):
        sums = lists[0]
        for i,value in enumerate(lists):
            if i !=0:
                sums = sums ^ value

        return sums


    def main(self,value1):
        for i in range(4):
            convert_list = []
            galora = self.galora[i]
            for j in range(len(value1)):
                v1 = self.mojiretu(int(value1[j],16))
                v2 = self.mojiretu(int(galora[j],16))
                result_log = self.gred(v1,v2)
                bin_result = self.bin_create(result_log)
                bin_sd = self.ajest_byte(bin_result)
                convert_list.append(bin_sd)

            v = self.xor_int(convert_list)
            print(hex(v))

s = Mixcolumns()
s.main(["0xd4","0xbf","0x5d","0x30"])
