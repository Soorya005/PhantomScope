import os
import subprocess


class MemoryDumper:
    def __init__(self):
        self.dump_dir = "dumps"
        os.makedirs(self.dump_dir, exist_ok=True)

    def dump_memory(self, vm_name):
        output_file = f"{self.dump_dir}/{vm_name}.dump"

        command = [
            "virsh",
            "dump",
            vm_name,
            output_file,
            "--memory-only"
        ]

        try:
            subprocess.run(command, check=True)
            return output_file

        except subprocess.CalledProcessError as e:
            print(f"Dump failed: {e}")
            return None