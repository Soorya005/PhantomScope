class VMCoreParser:

    @staticmethod
    def parse(vmcore_text):
        result = {}

        for line in vmcore_text.splitlines():

            if "OSRELEASE" in line:
                result["kernel_version"] = line.split()[-1]

            elif "BUILD-ID" in line:
                result["build_id"] = line.split()[-1]

            elif "PAGESIZE" in line:
                result["page_size"] = line.split()[-1]

            elif "KERNELOFFSET" in line:
                result["kernel_offset"] = line.split()[-1]

        return result