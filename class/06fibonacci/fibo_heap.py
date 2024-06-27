class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.total_nodes = 0
    
    class Node:
        def __init__(self, value):
            self.value = value
            self.degree = 0
            self.parent = None
            self.child = None
            self.left = self
            self.right = self
    
    def insert(self, value):
        new_node = self.Node(value)
        if self.min_node is None:
            self.min_node = new_node
        else:
            self._merge_with_root_list(new_node)
            if new_node.value < self.min_node.value:
                self.min_node = new_node
        self.total_nodes += 1
    
    def _merge_with_root_list(self, node):
        node.left = self.min_node
        node.right = self.min_node.right
        self.min_node.right = node
        node.right.left = node

# 測試Fibonacci堆的插入操作
fib_heap = FibonacciHeap()
fib_heap.insert(10)
fib_heap.insert(4)
fib_heap.insert(15)
print(f"最小值為: {fib_heap.min_node.value}")
