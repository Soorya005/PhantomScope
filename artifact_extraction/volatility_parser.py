import subprocess


class VolatilityParser:

    def run_plugin(self, memory_file, plugin):

        command = [
            "vol",
            "-f",
            memory_file,
            plugin
        ]

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            print(e)
            return None