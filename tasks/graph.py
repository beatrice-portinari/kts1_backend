from typing import Any

__all__ = (
    'Node',
    'Graph'
)


from collections import deque

class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def _dfs(self, node, visited, result) -> list[Node]:
        if node not in visited:
            result.append(node)
            visited.add(node)
            for item in node.outbound:
                self._dfs(item, visited, result)
        return result

    def dfs(self):
        return self._dfs(self._root, set(), [])

    def _bfs(self, node, visited, queue, result) -> list[Node]:
        queue.append(node)
        visited.add(node)

        while queue:
            cur_node = queue[0]
            result.append(cur_node)
            queue.popleft()

            for item in cur_node.outbound:
                if item not in visited:
                    visited.add(item)
                    queue.append(item)

        return result


    def bfs(self):
        return self._bfs(self._root, set(), deque(), [])
