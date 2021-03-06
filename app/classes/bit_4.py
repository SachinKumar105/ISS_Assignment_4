def reverse(string):
        string = string[::-1]
        return string

class number_4bit:
    def __init__(self):
        self.num = 0

    def b2d_4_unsigned(self, str):
        i = 0
        decimal = 0
        j = len(str)-1

        for i in range(4):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        return (decimal)

    def b2d_4_signed(self, str):
        i = 0
        decimal = 0
        j = len(str)-1

        for i in range(3):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        if str[0] == '1':
            decimal = decimal*-1

        return (decimal)

    def b2d_4_ones(self, str):
        i = 0
        decimal = 0
        j = len(str)-1
        msb = -(pow(2, 3)-1)*int(str[0])

        for i in range(3):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        decimal = decimal+msb
        return (decimal)

    def b2d_4_twos(self, str):
        i = 0
        decimal = 0
        j = len(str)-1
        msb = -(pow(2, 3)*int(str[0]))
        for i in range(3):
            z = pow(2, i)
            decimal = decimal + z*int(str[j])
            j = j-1

        decimal = decimal+msb
        return (decimal)

    def dec2bin(self, val):

        b = ""
        while val > 0:
            if(val%2== 0):
                b = b+'0'
            else:
                b = b+'1'
            val = int(val)/2

        reverse(b)
        return b

    def bit4_add(self, list_b1, list_b2):
        # ans=[]

        umax = 15
        umin = 0
        smax = 7
        smin = -7
        omax = 7
        omin = -7
        tmax = 7
        tmin = -8
        sum_twos = list_b1[0]+list_b2[0]
        # ans.append(sum_unsigned)
        sum_ones = list_b1[1]+list_b2[1]
        # ans.append(sum_signed)
        sum_unsigned = list_b1[2]+list_b2[2]
        # ans.append(sum_ones)
        sum_signed = list_b1[3]+list_b2[3]
        # ans.append(sum_twos)
        res=sum_unsigned

        if sum_unsigned > umax or sum_unsigned < umin:
            sum_unsigned = "Overflow"

        if sum_signed > smax or sum_signed < smin:
            sum_signed = "Overflow"

        if sum_ones> omax or sum_ones < omin:
            sum_ones = "Overflow"

        if sum_twos > tmax or sum_twos < tmin:
            sum_twos = "Overflow"

        return (res,sum_twos,sum_ones,sum_unsigned, sum_signed)


# a = number()
# unsigned = a.b2d_4_unsigned("1100")
# print(unsigned)
# signed = a.b2d_4_signed("1100")
# print(signed)
# ones = a.b2d_4_ones("1100")
# print(ones)
# twos = a.b2d_4_twos("1100")
# print(twos)
