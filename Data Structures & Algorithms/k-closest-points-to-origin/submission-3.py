import math
class MinHeap:
    def __init__(self):
        self._data = []
    
    def add(self, val):
        data = self._data
        data.append(val)
        cur = len(data) - 1
        while cur != 0:
            par = (cur - 1) // 2
            if data[par][0] > data[cur][0]:
                data[par], data[cur] = data[cur], data[par]
                cur = par
            else:
                break

    def pop(self):
        data = self._data
        res = data[0]
        if self.remaining_items() == 1:
            data.pop(-1)
            return res
        data[0] = data.pop(-1)
        pos = 0
        max_length = len(data)
        while True:
            most = pos
            l = (pos * 2) + 1
            r = (pos * 2) + 2
            if l < max_length and data[most][0] > data[l][0]:
                most = l
            if r < max_length and data[most][0] > data[r][0]:
                most = r
            if most == pos:
                break
            else:
                data[pos], data[most] = data[most], data[pos]
                pos = most
        return res

    def remaining_items(self):
        return len(self._data)

    def isempty(self):
        return self.remaining_items() == 0

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclid(x, y):
            return math.sqrt(x*x+y*y)

        min_heap = MinHeap()
        for x, y in points:
            dist = euclid(x, y)
            min_heap.add((dist, [x, y]))

        res = []
        for _ in range(k):
            if min_heap.isempty():
                break
            res.append(min_heap.pop()[1])
        return res



        
        