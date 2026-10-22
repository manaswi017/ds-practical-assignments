
N = 3
events = []


def log_event(pid, event, vector, details):
    events.append((pid, event, vector.copy(), details))


class VectorClock:
    def __init__(self, pid, index):
        self.pid = pid
        self.index = index
        self.clock = [0] * N

    def internal(self, description):
        self.clock[self.index] += 1
        log_event(self.pid, "Internal", self.clock, description)

    def send(self, receiver, mid):
        self.clock[self.index] += 1
        message = {
            "id": mid,
            "vector": self.clock.copy()
        }
        log_event(
            self.pid, "Send", self.clock,
            f"{mid} -> {receiver}"
        )
        return message

    def receive(self, sender, message):
        # Merge the received vector with the local vector
        for i in range(N):
            self.clock[i] = max(
                self.clock[i], message["vector"][i]
            )

        # Count the receive event
        self.clock[self.index] += 1

        log_event(
            self.pid, "Receive", self.clock,
            f"{message['id']} <- {sender}, "
            f"sent VC={message['vector']}"
        )


# Create three distributed processes
P1 = VectorClock("P1", 0)
P2 = VectorClock("P2", 1)
P3 = VectorClock("P3", 2)

# Execute events in a fixed sequence
P1.internal("Calculate data")
m1 = P1.send("P2", "M1")
P2.receive("P1", m1)

P2.internal("Process data")
m2 = P2.send("P3", "M2")
P3.receive("P2", m2)

P3.internal("Store result")
m3 = P3.send("P1", "M3")
P1.receive("P3", m3)

P1.internal("Finish task")

# Display every event in execution order
print(f"{'Process':<10}{'Event':<12}"
      f"{'Vector Clock':<22}Details")
print("-" * 85)

for pid, event, vector, details in events:
    print(
        f"{pid:<10}{event:<12}"
        f"{str(vector):<22}{details}"
    )
