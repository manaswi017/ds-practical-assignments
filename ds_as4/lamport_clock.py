
class LamportClock:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0

    def internal(self, description):
        self.clock += 1
        log_event(self.pid, "Internal", self.clock, description)

    def send(self, receiver, mid):
        self.clock += 1
        msg = {"id": mid, "timestamp": self.clock}
        log_event(
            self.pid, "Send", self.clock,
            f"{mid} -> {receiver}"
        )
        return msg

    def receive(self, sender, msg):
        self.clock = max(self.clock, msg["timestamp"]) + 1
        log_event(
            self.pid, "Receive", self.clock,
            f"{msg['id']} <- {sender}, sent ts={msg['timestamp']}"
        )


events = []

def log_event(pid, event, timestamp, details):
    events.append((pid, event, timestamp, details))


P1 = LamportClock("P1")
P2 = LamportClock("P2")
P3 = LamportClock("P3")

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

print(f"{'Process':<10}{'Event':<12}{'Timestamp':<12}Details")
print("-" * 60)
for pid, event, ts, details in events:
    print(f"{pid:<10}{event:<12}{ts:<12}{details}")
