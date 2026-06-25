import heapq
class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        self.arr.sort()
        length = len(self.arr)
        
        if length % 2 != 0:
            return float(self.arr[length // 2])
        else:
            mid = length // 2
            return float((self.arr[mid] + self.arr[mid - 1]) / 2)
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()