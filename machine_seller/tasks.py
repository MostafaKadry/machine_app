import frappe

def mark_machines_as_sold():
    unsold_machines = frappe.get_all(
        "Machine",
        filters={"selling_status": "unsold"},
        fields=["name"]
    )
    if not unsold_machines:
        return
    for machine in unsold_machines:
        frappe.db.set_value("Machine", machine.name, "selling_status", "sold")
