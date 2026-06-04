from vm_controller.controller import VMController
from memory_acquisition.dumper import MemoryDumper

controller = VMController()

vms = controller.list_vms()

print("\n=== PhantomScope VM Inventory ===\n")

for vm in vms:
    print(vm)

target = "debian-lab"

print(f"\nChecking VM: {target}")

if controller.start_vm(target):
    print("[+] VM start command issued")

dumper = MemoryDumper()

path = dumper.dump_memory(target)

print("Dump result:", path)

controller.close()