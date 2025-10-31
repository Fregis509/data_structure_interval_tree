
class IntervalNode:
    def __init__(self, interval):
        self.interval = interval  
        self.max_end = interval[1]
        self.height = 1
        self.left = None
        self.right = None


class IntervalTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _update(self, node):
        if not node:
            return None
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node.max_end = max(
            node.interval[1],
            node.left.max_end if node.left else float('-inf'),
            node.right.max_end if node.right else float('-inf')
        )
        return node

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update(y)
        self._update(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self._update(x)
        self._update(y)
        return y

    def insert(self, node, interval):
        if not node:
            return IntervalNode(interval)
        if interval[0] < node.interval[0]:
            node.left = self.insert(node.left, interval)
        else:
            node.right = self.insert(node.right, interval)

        node = self._update(node)
        balance = self._balance_factor(node)

        
        if balance > 1 and interval[0] < node.left.interval[0]:
            return self._rotate_right(node)
        if balance < -1 and interval[0] >= node.right.interval[0]:
            return self._rotate_left(node)
        if balance > 1 and interval[0] >= node.left.interval[0]:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1 and interval[0] < node.right.interval[0]:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def add(self, interval):
        """Public method to add a new interval."""
        self.root = self.insert(self.root, interval)

    def _overlap(self, i1, i2):
        """Check if two intervals overlap."""
        return i1[0] <= i2[1] and i2[0] <= i1[1]

    def search_overlaps(self, node, query, result):
        """Recursive overlap search."""
        if not node:
            return
        if self._overlap(node.interval, query):
            result.append(node.interval)
        if node.left and node.left.max_end >= query[0]:
            self.search_overlaps(node.left, query, result)
        self.search_overlaps(node.right, query, result)

    def find_overlaps(self, query):
        """Return all intervals overlapping with `query`."""
        result = []
        self.search_overlaps(self.root, query, result)
        return result
