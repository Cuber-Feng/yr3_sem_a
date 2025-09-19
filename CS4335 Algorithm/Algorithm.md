# CS4335 Algorithm

## Lecture 1

主要用伪代码&自然语言

## Lecture 2

Greedy Algorithm

## Lecture 3

- Greedy Proofs:
  - 常见证明方式:
    - 设G是贪心的结果, OPT是最理想的结果
    - 改变OPT, 让它变成G, 同时 quality 不变化

### Minimum Spanning Tree (MST)

- Definition of MST
  - Spanning Tree
    - 对于一个连通无向图 G = (V, E)，其生成树是包含图中所有顶点 V 的一个无环连通子图，也就是一个树（tree）且顶点集合与原图相同、边是原图的子集
  - Minimum Spanning Tree
    - 当原图是带权图（每条边有权重）时，最小生成树是权重总和最小的生成树。
- Generic MST algorithm
- Kruskal's algorithm
- Prim's algorithm
