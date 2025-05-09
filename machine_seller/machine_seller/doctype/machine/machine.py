# Copyright (c) 2025, mostafa k. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

@frappe.whitelist()
def get_spare_parts(type):
		if type:
			return frappe.get_all("Spare Part", filters={"type": type}, fields=["spare_part_name", "type"])
		return []

class Machine(Document):
	def validate(self):
		if not self.type and self.spare_parts:
			frappe.throw("Please select Machine Type before adding Spare Parts.")

		if self.type:
			if self.spare_parts:
				for spare_part in self.spare_parts:
					if spare_part.type != self.type:
						frappe.throw(f"Spare part {spare_part.spare_part} does not match the machine type {self.type}.")

	