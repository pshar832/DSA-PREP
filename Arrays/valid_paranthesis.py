class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       mapper = {')':'(','}':'{',']':'['}

       for char in s:
          if char in mapper:
            top_element = stack.pop() if stack else '#'
            if mapper[char] != top_element:
                return False
          else:
            top_element = stack.append(char)
       return not stack