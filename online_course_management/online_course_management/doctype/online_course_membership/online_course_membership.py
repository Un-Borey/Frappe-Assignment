# Copyright (c) 2021, rey flexi solution and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class OnlineCourseMembership(Document):
	def validate(self):
		if self.from_date > self.to_date:
			frappe.throw("From date cannot be bigger than to date")
			frappe.msgprint(" ==== ")

