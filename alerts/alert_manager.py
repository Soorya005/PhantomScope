class AlertManager:

    @staticmethod
    def generate(hidden_processes):

        alerts = []

        suspicious_processes = [
            "bash",
            "sh",
            "python",
            "nc",
            "netcat"
        ]

        for process in hidden_processes:

            severity = "MEDIUM"

            if process.name in suspicious_processes:
                severity = "CRITICAL"

            alerts.append({
                "severity": severity,
                "type": "Hidden Process",
                "pid": process.pid,
                "process": process.name
            })

        return alerts