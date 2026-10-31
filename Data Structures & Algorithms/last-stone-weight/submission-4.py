class MaxHeap:
    def __init__(self):
        self._data = []
    
    def add(self, val):
        data = self._data
        data.append(val)
        cur = len(data) - 1
        while cur != 0:
            par = (cur - 1) // 2
            if data[par] < data[cur]:
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
            if l < max_length and data[most] < data[l]:
                most = l
            if r < max_length and data[most] < data[r]:
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
        return len(self._data) == 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = MaxHeap()
        for stone in stones:
            max_heap.add(stone)
        
        while max_heap.remaining_items() > 1:
            i1 = max_heap.pop()
            i2 = max_heap.pop()
            rem = abs(i1 - i2)
            max_heap.add(rem)

        return 0 if max_heap.isempty() else max_heap.pop()
        