class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for letter in strs:
            sort = ''.join(sorted(letter))
            result[sort].append(letter)
        return list(result.values())