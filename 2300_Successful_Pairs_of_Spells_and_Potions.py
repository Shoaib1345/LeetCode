import bisect
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for spell in spells:
            min_potion = (success + spell - 1) // spell
            index = bisect.bisect_left(potions, min_potion)
            count = m - index
            result.append(count)

        return result
