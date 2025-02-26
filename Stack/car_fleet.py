class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[i,j] for i,j in zip(position, speed)]
        stack = [] # captures time of each car

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)