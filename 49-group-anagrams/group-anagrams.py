class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = {}
        for item in strs:
            key = "".join(sorted(item))
            if key in check:
                check[key].append(item)
            else:
                check[key] = [item]
        return (list(check.values()))

        