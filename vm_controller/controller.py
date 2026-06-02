import libvirt


class VMController:
    def __init__(self):
        self.conn = libvirt.open("qemu:///system")

        if self.conn is None:
            raise Exception("Failed to connect to libvirt")

    def list_vms(self):
        domains = self.conn.listAllDomains()

        vm_list = []

        for domain in domains:
            vm_list.append({
                "name": domain.name(),
                "id": domain.ID(),
                "active": domain.isActive()
            })

        return vm_list

    def get_vm_info(self, vm_name):
        try:
            domain = self.conn.lookupByName(vm_name)

            state, max_mem, memory, vcpus, cpu_time = domain.info()

            return {
                "name": domain.name(),
                "state": state,
                "max_memory_kb": max_mem,
                "memory_kb": memory,
                "vcpus": vcpus,
                "cpu_time_ns": cpu_time
            }

        except libvirt.libvirtError:
            return {"error": "VM not found"}

    def start_vm(self, vm_name):
        try:
            domain = self.conn.lookupByName(vm_name)

            if not domain.isActive():
                domain.create()

            return True

        except libvirt.libvirtError:
            return False

    def shutdown_vm(self, vm_name):
        try:
            domain = self.conn.lookupByName(vm_name)

            if domain.isActive():
                domain.shutdown()

            return True

        except libvirt.libvirtError:
            return False

    def close(self):
        self.conn.close()