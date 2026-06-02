class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result_dict = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in result_dict:
                result_dict[key] = []
            result_dict[key].append(word)

        return list(result_dict.values())
    

            