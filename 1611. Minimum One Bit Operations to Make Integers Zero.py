class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        fun = [0] * 32
        // function[i] = x
        // Means it will take x operations to make the ith bit 1
        fun[0] = 1
        for i in range(1, 32):
            fun[i] = 2 * fun[i - 1] + 1
        res = 0
        sign = 1
        for i in range(30, -1, -1):
            if (n >> i) & 1 == 0:
                continue
            if sign > 0:
                res += fun[i]
            else:
                res -= fun[i]
            sign *= -1

        return res
