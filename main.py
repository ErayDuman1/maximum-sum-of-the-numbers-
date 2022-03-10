import sys


def is_prime(nmbr):
    Flag = True
    if nmbr > 1:
        for i in range(2, nmbr):
            if (nmbr % i) == 0:
                Flag = False
                break
        else:
            Flag = True

    else:
        Flag = False
    return Flag


class Edge:
    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight


class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]

        for edge in edges:
            if not is_prime(edge.weight):
                self.adjList[edge.source].append(edge)


def create_edges(numbers):
    edges = [Edge(0, 1, int(numbers[0]))]

    n = 0
    temp = 0
    for i in range(len(numbers)):
        temp += i
        if temp == len(numbers):
            break
        n = n + 1

    index = 2
    hold = 5
    count1 = 0
    count2 = 0
    j = 0
    for i in range(int(n * (n - 1) / 2)):

        edges.append(Edge(i + 1, index, int(numbers[index - 1])))
        index += 1
        edges.append(Edge(i + 1, index, int(numbers[index - 1])))

        if index != hold:
            index += 1
        else:
            if count1 == 0:
                hold += 3
                count1 = 2
                count2 = 1
            elif count1 == count2:
                hold += 3
                count1 += 1
                count2 = 1
            elif count1 != count2:
                hold += 1
                count2 += 1

        j = i + 2

    for i in range(j, len(numbers) + 1):
        edges.append(Edge(i, len(numbers) + 1, 0))
    return edges


def dfs(graph, v, discovered, departure, time):
    discovered[v] = True

    for e in graph.adjList[v]:
        u = e.dest
        if not discovered[u]:
            time = dfs(graph, u, discovered, departure, time)

    departure[time] = v
    time = time + 1

    return time


def find_longest_distance(graph, source, N):
    departure = [-1] * N

    discovered = [False] * N
    time = 0

    for i in range(N):
        if not discovered[i]:
            time = dfs(graph, i, discovered, departure, time)

    cost = [sys.maxsize] * N
    cost[source] = 0

    for i in reversed(range(N)):

        v = departure[i]

        for e in graph.adjList[v]:
            u = e.dest
            w = e.weight * -1

            if cost[v] != sys.maxsize and cost[v] + w < cost[u]:
                cost[u] = cost[v] + w

    return cost[N - 1] * -1


if __name__ == '__main__':
    file = open("orthogonal.txt", 'r')
    number = file.read()
    numbers=number.split()
    N = len(numbers)+2
    graph = Graph(create_edges(numbers), N)
    source = 0
    print(find_longest_distance(graph, source, N))
