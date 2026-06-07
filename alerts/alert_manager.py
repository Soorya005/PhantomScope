class AlertManager:

    @staticmethod
    def generate(hidden_processes):

        alerts = []

        for process in hidden_processes:

            alerts.append({
                "severity": "HIGH",
                "type": "Hidden Process",
                "process": process
            })

        return alerts