from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        # Sort only unique card values
        for num in sorted(count):
            if count[num] > 0:
                need = count[num]
                # Greedily form `need` groups starting at `num`
                for i in range(num, num + groupSize):
                    if count[i] < need:
                        return False
                    count[i] -= need

        return True