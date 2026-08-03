from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()

    def get(self, key: int) -> int:
        res = self.data.get(key, -1)
        if res != -1:
            self.data.move_to_end(key)
        return res
        

    def put(self, key: int, value: int) -> None:
        # if self.data:

        # if len(self.data) >= self.capacity:
        #     # removing least recently used
        
        #     self.data.popitem(last=False)  
        # self.data[key] = value
        if key in self.data:
            self.data.move_to_end(key)
        elif len(self.data) >= self.capacity:
            self.data.popitem(last=False)
        self.data[key] = value
        

        
