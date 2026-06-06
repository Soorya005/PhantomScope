from vm_controller.controller import VMController
from artifact_extraction.banner import BannerExtractor
from artifact_extraction.vmcoreinfo import VMCoreInfoExtractor
from artifact_extraction.parser import VMCoreParser
from reporting.report_generator import ReportGenerator


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
    print("=== PhantomScope Analysis Complete ===")
    print("=" * 50)


if __name__ == "__main__":
    main()