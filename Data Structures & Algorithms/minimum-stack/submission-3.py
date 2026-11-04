class MinStack:

    def __init__(self):
        self.stack = []
        self.offset = None 

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.offset = val
        else:
            new_val = val - self.offset
            if new_val >= 0:
                self.stack.append(new_val)
            else:
                self.stack.append(new_val)
                self.offset = val
        

    def pop(self) -> None:
        if not self.stack:
            return None

        stored_val = self.stack.pop(-1)
        if stored_val < 0:
            self.offset -= stored_val     

    def top(self) -> int:
        if not self.stack:
            return None
        top = self.stack[-1]
        if top > 0:
            return top + self.offset
        return self.offset
        

    def getMin(self) -> int:
        if not self.stack:
            return None
        return self.offset
        
