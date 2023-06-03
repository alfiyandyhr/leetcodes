class Solution:
    def plusOne(digits: list) -> list:
        # Convert the list into a single int
        res = 0
        for i, elem in enumerate(digits[::-1]):
            res += elem * 10**i
    
        # Plus one to that int (int operations)
        res += 1

        # Construct a list out of that resulting integer
        res = str(res)
        ret = []
        for char in res:
            ret.append(int(char))
        
        return ret

digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9]

print(Solution.plusOne(digits))