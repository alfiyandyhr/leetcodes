class Solution:
  def romanToInt(s:str) -> int:
    ruleDict = {'M':1000, 'D': 500, 'C': 100,
                'L': 50, 'X': 10, 'V':5, 'I':1}
    ret = 0
    i = 0
    while i < len(s):
      if i+1 == len(s):
        ret += ruleDict[s[i]]
      else:
        if ruleDict[s[i]] >= ruleDict[s[i+1]]:
          ret += ruleDict[s[i]]
        else:
          ret += ruleDict[s[i+1]] - ruleDict[s[i]]
          i += 1
      i += 1
    return ret

# s = "III"
# s = "LVIII"
s = "MCMXCIV"

print(Solution.romanToInt(s))