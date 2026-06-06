import json


class ReportGenerator:

    @staticmethod
    def generate(report_data):

        with open("report.json", "w") as f:
            json.dump(report_data, f, indent=4)

        return "report.json"