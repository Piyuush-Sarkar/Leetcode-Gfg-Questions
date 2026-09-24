class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i=0
        j=0
        arr=[]
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                arr.append(nums1[i])
                i+=1
            else:
                arr.append(nums2[j])
                j+=1
        while i<m:
            arr.append(nums1[i])
            i+=1
        while j<n:
            arr.append(nums2[j])
            j+=1
        for i in range(n+m):
            nums1[i]=arr[i]