Aim
To implement a coordinator election algorithm for selecting a leader in a distributed system
using the Bully or Ring algorithm.
Learning Objectives
Students should be able to:
● Explain the need for coordinator election.
● Simulate communication among distributed processes.
● Select a coordinator after process failure.
● Compare the Bully and Ring election algorithms.
Background
A coordinator or leader is responsible for managing certain activities in a distributed system. If
the coordinator fails, another process must be selected as the new coordinator.
Bully Algorithm
The process that detects coordinator failure starts an election by sending messages to
processes with higher identification numbers. If no higher process responds, the initiating
process becomes the coordinator. Otherwise, a higher process continues the election.
Ring Algorithm
Processes are logically arranged in a ring. An election message circulates around the ring,
collecting process identifiers. The process with the highest identifier is selected as coordinator.
Requirements
● Represent at least five processes.
● Assign a unique identifier to every process.
● Mark one process as the current coordinator.
● Simulate coordinator failure.
● Initiate a new election.
● Display election messages and the newly selected coordinator.