class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total gas is less than total cost, it's impossible to complete a circuit
        if sum(gas) < sum(cost):
            return -1

        curr_tank = 0
        start_index = 0

        for i in range(len(gas)):
            curr_tank += gas[i] - cost[i]

            # If tank drops below 0, no station between start_index and i can be the start
            if curr_tank < 0:
                start_index = i + 1
                curr_tank = 0

        return start_index