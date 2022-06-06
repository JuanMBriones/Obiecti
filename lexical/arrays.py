
class Array:
    def __init__(self, limit, dim, r = 1):
        self.next = None
        self.limit = limit
        self.r = (limit + 1) * r
        self.dim = dim
        self.offset = 0
        self.m = 0
    
    def get_r(self):
        return self.r
    
    def get(self):
        return f"r={self.r}, lim={self.limit}, dim={self.dim}, m={self.m}, offset={self.offset}"

class ArrayList:
    def __init__(self, dim, limits: list):
        self.head = None
        self.r = 1
        self.k = 0

        for i in range(dim):
            self.add(i, limits[i])
        self.size = self.r
    
    def add(self, i, limit):
        curr = self.head

        if not curr:
            self.head = Array(limit, i, self.r)
            self.r = self.head.get_r()
            return

        while curr.next:
            curr = curr.next
        
        curr.next = Array(limit, i, self.r)
        self.r = curr.next.get_r()

    def get_all(self):
        print(self.head)
        curr = self.head

        while curr:
            print(curr.get())
            curr = curr.next
    
    def get_size(self):
        return self.size
    
    def calculate(self):
        curr = self.head
        m = 0
        
        while curr:
            curr.m = self.r / (curr.limit + 1)
            self.r = curr.m

            curr.offset = curr.offset + 0 # 0 as long as we bound our arrays starting on 0, curr.limit * curr.m
            if not curr.next:
                curr.offset = curr.offset * -1
                self.k = curr.offset
            curr = curr.next
