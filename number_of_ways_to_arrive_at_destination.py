MOD = 10**9 + 7

class Solution:
    def construct_graph(self, roads):
        graph = defaultdict(list)
        for src, dst, t in roads:
            graph[src].append((dst, t))
            graph[dst].append((src, t))  # Add the reverse edge
        return graph

    def can_reach(self, src, dst, graph):
        dist = [math.inf]*(dst+1)
        ways = [0]*(dst+1)
        pq = [(0, src)]
        dist[src]=0
        ways[src] = 1
        heapify(pq)
        while pq:
            time,node = heappop(pq)

            if time > dist[node]: 
                continue

            for neg, wt in graph[node]:
                if dist[neg] > time+wt:
                    dist[neg] = time+wt
                    ways[neg] = ways[node]
                    heappush(pq, (time+wt, neg))

                elif dist[neg] == time+wt:
                    ways[neg] = (ways[neg]+ways[node]) % MOD

        return ways[dst]

        
    def approach1(self, n, roads):
        ways = 0
        graph = self.construct_graph(roads)
        return self.can_reach(0, n-1, graph)

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        return self.approach1(n, roads)
        
