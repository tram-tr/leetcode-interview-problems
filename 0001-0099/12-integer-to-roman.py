class Solution:
    def intToRoman(self, num: int) -> str:
        translate = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        # 1994
        # M - 994
        # CM - 900
        # XC - 90
        # IV - 4

        ans = ''
        arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        for i in arr:
            while (num > 0):
                if (i <= num):
                    num -= i
                    ans += translate[i]
                else:
                    break
                
        return ans
                
        
