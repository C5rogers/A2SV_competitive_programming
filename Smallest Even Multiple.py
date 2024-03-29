class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return (2 * n) // math.gcd(2, n)
