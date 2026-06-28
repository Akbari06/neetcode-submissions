class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def generate_subsets(i,curr,total):
            if total == target:
                res.add(tuple(curr))
                return
            if total > target or i == len(candidates):
                return

            curr.append(candidates[i])
            generate_subsets(i+1,curr, total+candidates[i])
            curr.pop()
            
            generate_subsets(i+1,curr,total)

        generate_subsets(0,[],0)

        return[list(combination) for combination in res]