Aim
To implement a deadlock detection mechanism using a wait-for graph.
Learning Objectives
Students should be able to:
● Explain deadlock in distributed systems.
● Construct a wait-for graph.
● Detect cycles in a directed graph.
● Identify processes involved in a deadlock.
Background
A deadlock occurs when a group of processes waits indefinitely for resources held by one
another.
A wait-for graph contains:
● Vertices representing processes.
● A directed edge Pi→Pj, indicating that process Pi is waiting for process Pj.
A cycle in the wait-for graph indicates a possible deadlock.
For example:
P1→P2,P2→P3,P3→P1
The cycle indicates that P1,P2, and P3 are deadlocked.
Requirements
● Accept a directed wait-for graph.
● Display the graph or its adjacency representation.
● Detect whether a cycle exists.
● Display the processes participating in the cycle.
● Report whether the system is deadlock-free.

Suggested Algorithm
1. Create a directed graph using the processes as vertices.
2. Add an edge whenever one process waits for another.
3. Apply DFS or another cycle-detection technique.
4. Maintain visited and recursion-stack information.
5. If a vertex is encountered again in the recursion stack, report a cycle.
6. Display the deadlocked processes.
Expected Input
● Number of processes.
● Number of wait-for relationships.
● Pairs such as (Pi,Pj) where Pi waits for Pj.
Expected Output
● Wait-for graph.
● Cycle information, if present.
● Deadlock status.