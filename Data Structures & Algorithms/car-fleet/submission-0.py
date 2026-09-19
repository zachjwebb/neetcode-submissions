class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired = [(pos, s) for pos, s in zip(position, speed)]
        paired.sort(reverse=True)

        stack = []

        for p, s in paired:
            ft = ((target - p)/s)
            stack.append(ft)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)
            
        
