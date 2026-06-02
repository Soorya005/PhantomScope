from vm_controller.controller import VMController

controller = VMController()

print("=== PhantomScope VM Inventory ===")

for vm in controller.list_vms():
    print(vm)

controller.close()