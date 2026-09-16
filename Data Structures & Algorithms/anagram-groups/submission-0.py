class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26

            #for character in string s
            for c in s:
                #subtracts ascii to map character 0-26 and adds 1 to count
                count[ord(c) - ord('a')] += 1

            #count is a list not hashable but tuples are so convert
            #Append string to hash at frequency value
            result[tuple(count)].append(s)
        return list(result.values())
        