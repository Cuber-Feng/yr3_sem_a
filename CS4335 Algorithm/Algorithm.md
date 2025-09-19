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

    ```python
    GENERIC_MST(G, w)
    1 A:={}
    2 while A does not form a spanning tree do
    3  find an edge (u,v) that is safe for A
    4  A:=A∪{(u,v)}
    5 return A
    ```

- In Kruskal's algorithm,
  - The set A is a forest.
  - The safe edge added to A is always a shortest edge in the graph that connects two distinct components.

- In Prim's algorithm,
  - The set A forms a single tree.
  - The safe edge added to A is always a least-weight edge connecting the tree to a node not in the tree
