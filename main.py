from vm_controller.controller import VMController

from artifact_extraction.banner import BannerExtractor
from artifact_extraction.vmcoreinfo import VMCoreInfoExtractor
from artifact_extraction.parser import VMCoreParser

from reporting.report_generator import ReportGenerator

from cross_view.detector import CrossViewDetector
from test_data.mock_processes import MEMORY_VIEW, OS_VIEW

from alerts.alert_manager import AlertManager


DUMP_PATH = "dumps/debian-lab3.dump"


def main():

    print("\n=== PhantomScope VM Inventory ===\n")

    controller = VMController()
    vms = controller.list_vms()

    if not vms:
        print("No virtual machines found.")
    else:
        for vm in vms:
            print(vm)

    print("\n" + "=" * 50)
    print("=== Kernel Banner Extraction ===")
    print("=" * 50)

    banner_output = BannerExtractor.extract(DUMP_PATH)
    print(banner_output)

    print("\n" + "=" * 50)
    print("=== VMCOREINFO Extraction ===")
    print("=" * 50)

    vmcore_output = VMCoreInfoExtractor.extract(DUMP_PATH)
    print(vmcore_output)

    print("\n" + "=" * 50)
    print("=== Parsing Forensic Artifacts ===")
    print("=" * 50)

    parsed_data = VMCoreParser.parse(vmcore_output)

    report = {
        "vm_name": "debian-lab",
        "dump_file": DUMP_PATH,
        "forensic_data": parsed_data
    }

    report_file = ReportGenerator.generate(report)

    print("\nParsed Report:\n")
    print(report)

    print(f"\nReport saved to: {report_file}")

    print("\n" + "=" * 50)
    print("=== Cross View Analysis ===")
    print("=" * 50)

    hidden_processes = CrossViewDetector.compare(
        MEMORY_VIEW,
        OS_VIEW
    )

    if hidden_processes:

        print("\nPotential Hidden Processes Detected:\n")

        for process in hidden_processes:
            print(f"[!] {process}")

    else:
        print("\nNo hidden processes detected.")

    print("\n" + "=" * 50)
    print("=== Alert Generation ===")
    print("=" * 50)

    alerts = AlertManager.generate(hidden_processes)

    if alerts:
        for alert in alerts:
            print(alert)
    else:
        print("No alerts generated.")

    print("\n" + "=" * 50)
    print("=== PhantomScope Analysis Complete ===")
    print("=" * 50)


if __name__ == "__main__":
    main()