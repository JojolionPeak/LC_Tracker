class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        count = n
        product = 1

        while product % t != 0:
            s = str(count)
            product = 1

            for i in s:
                product *= int(i)
                print(product, t, product % t)

            if product % t != 0:
                count += 1
                continue
            else:
                break

        return count
