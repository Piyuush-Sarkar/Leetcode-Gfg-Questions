class Solution:
    def fourSum(self, arr, target):
        #code here
        n = len(arr)
        ans = []
        arr.sort()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):

                left = j + 1
                right = n - 1

                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        temp = [arr[i], arr[j], arr[left], arr[right]]

                        if temp not in ans:
                            ans.append(temp)

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return ans
