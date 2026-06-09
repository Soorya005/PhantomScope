class Statistics:

    @staticmethod
    def generate(hidden_processes, alerts):

        return {
            "hidden_process_count": len(hidden_processes),
            "alert_count": len(alerts),
            "critical_alerts": len(
                [
                    alert
                    for alert in alerts
                    if alert["severity"] == "CRITICAL"
                ]
            ),
            "medium_alerts": len(
                [
                    alert
                    for alert in alerts
                    if alert["severity"] == "MEDIUM"
                ]
            )
        }