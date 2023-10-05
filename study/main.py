class Solution(object):

    def romanToInt(self, s):
        rom_num = {"i": 1, "v": 5, "x": 10, "l": 50, "c": 100, "d": 500, "m": 1000}
        listRoman = [x.lower() for x in s]
        totalSum = 0
        stored_value = 0
        for i in reversed(listRoman):  # xxiv
            if stored_value == 0:
                totalSum = totalSum + rom_num.get(i)
                print("First Calculation: " + str(rom_num.get(i)))
            else:
                if rom_num.get(i) < rom_num.get(stored_value):
                    totalSum = totalSum - rom_num.get(i)
                    print("Subtraction: " + str(rom_num.get(i)))
                else:
                    totalSum = totalSum + rom_num.get(i)
                    print("Addition: " + str(rom_num.get(i)))
            stored_value = i
            print("")
        return totalSum


solution = Solution()
print(solution.romanToInt("xd"))
