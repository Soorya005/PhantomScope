import json
import os

from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate(report):

        os.makedirs(
            "reports",
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        filename = (
            f"reports/report_{timestamp}.json"
        )

        with open(
            filename,
            "w"
        ) as file:

            json.dump(
                report,
                file,
                indent=4
            )

        return filename