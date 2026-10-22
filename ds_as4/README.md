To simulate logical clock synchronization among distributed processes using Lamport’s logical
clock algorithm.
Learning Objectives
Students should be able to:
● Explain the need for logical clocks.
● Assign timestamps to distributed events.
● Apply Lamport clock rules.
● Establish a logical ordering of events.
Background
There is no single global physical clock in a distributed system. Therefore, logical clocks are
used to order events.
Lamport’s clock follows these rules:
1. Each process maintains a logical counter.
2. Before executing a local event, the process increments its counter.
3. A message carries the sender’s timestamp.
4. When a process receives a message, it updates its clock as:
Cj=max⁡(Cj,Tm)+1

where:
● Cjis the receiver’s current clock.
● Tm is the timestamp attached to the received message.
Requirements
● Simulate at least three processes.
● Include local events, send events, and receive events.
● Assign timestamps to all events.

● Display the final logical clock of each process.
● Display the event ordering.
Suggested Tasks
1. Initialize the logical clock of every process to zero.
2. Define a sequence of local, send, and receive events.
3. Increment the clock before each local or send event.
4. Attach the timestamp to every sent message.
5. Update the receiver’s clock using Lamport’s rule.
6. Display all events in timestamp order.
7. Explain cases where two events have the same timestamp.
Optional Extension
Implement vector clocks and compare their results with Lamport logical clocks.
Expected Input
● Number of processes.
● Event sequence.
● Sender and receiver details for message events.
Expected Output
● Event names.
● Process identifiers.
● Lamport timestamps.
● Messages send and receive information.
● Logical ordering of events.