class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=='(' or ch=='[' or ch=='{':
                stack.append(ch)
            elif len(stack)==0:
                return False
            else:
                item = stack.pop()
                if item =='(' and not ch==')':
                    return False
                if item =='[' and not ch==']':
                    return False  
                if item =='{' and not ch=='}':
                    return False
        return (len(stack) == 0) 





        