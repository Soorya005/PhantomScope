class Process:

    def __init__(self, pid, name):
        self.pid = pid
        self.name = name

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name
        }

    def __repr__(self):
        return f"{self.pid}:{self.name}"