import subprocess


class BannerExtractor:

    @staticmethod
    def extract(dump_path):
        try:
            result = subprocess.run(
                ["vol", "-f", dump_path, "banners.Banners"],
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            return f"Error: {e}"