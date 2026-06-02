import libvirt


class VMController:
    def __init__(self):
        self.conn = libvirt.open("qemu:///system")

        if self.conn is None:
            raise Exception("Failed to connect to libvirt")

    def list_vms(self):
        domains = self.conn.listAllDomains()

        results = []

        for domain in domains:
            results.append({
                "name": domain.name(),
                "id": domain.ID(),
                "active": domain.isActive()
            })

        return results

    def close(self):
        self.conn.close()