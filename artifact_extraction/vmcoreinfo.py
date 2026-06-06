import subprocess


class VMCoreInfoExtractor:

    @staticmethod
    def extract(dump_path):
        try:
            result = subprocess.run(
                ["vol", "-f", dump_path, "linux.vmcoreinfo.VMCoreInfo"],
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            return f"Error: {e}"