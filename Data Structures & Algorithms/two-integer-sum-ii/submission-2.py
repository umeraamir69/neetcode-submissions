class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        poiA, poiB = 0 , len(numbers)-1

        while poiA < poiB :
            total = numbers[poiA] + numbers[poiB]

            if total == target:
                return [poiA+1 , poiB+1]
            elif target > total :
                poiA +=1
            elif target < total :
                poiB -=1