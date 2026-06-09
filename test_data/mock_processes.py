from models.process import Process

MEMORY_VIEW = [
    Process(1, "systemd"),
    Process(100, "bash"),
    Process(200, "sleep"),
    Process(300, "python")
]

OS_VIEW = [
    Process(1, "systemd"),
    Process(100, "bash")
]