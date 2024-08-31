"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.
"""

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Adjacency list
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            adj[u].append((v, p))
            adj[v].append((u, p))

        # Distances array
        dist = [0.0] * n
        dist[start] = 1.0

        # Queue for BFS
        queue = deque([start])

        while queue:
            curr = queue.popleft()

            for node, prob in adj[curr]:
                new_prob = dist[curr] * prob

                if new_prob > dist[node]:
                    dist[node] = new_prob
                    queue.append(node)

        return dist[end]