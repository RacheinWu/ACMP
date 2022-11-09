class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            new_num_bottles = int(numBottles / numExchange)  # 3 = 9 / 3
            # print(new_num_bottles)
            res += new_num_bottles                           # 9 + 3 = 12
            # print(res)
            new_num_bottles += numBottles % numExchange      # 3 + (9 % 3) = 3
            # print(new_num_bottles)
            numBottles = new_num_bottles                     # 3
            # print(numBottles)
            # print("----------------------------------------------")
        return res


so = Solution()
print(so.numWaterBottles(numBottles = 15, numExchange = 4))