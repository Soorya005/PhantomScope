from vm_controller.controller import VMController

controller = VMController()

print("\n=== PhantomScope VM Inventory ===\n")

vms = controller.list_vms()

if not vms:
    print("No virtual machines found.")

for vm in vms:
    print(vm)

controller.close()