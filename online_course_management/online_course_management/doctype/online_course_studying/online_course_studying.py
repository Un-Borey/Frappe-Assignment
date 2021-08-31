# Copyright (c) 2021, rey flexi solution and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class OnlineCourseStudying(Document):
	def before_submit(self):
		if self.subject != "SUBJECT-00001" and self.is_membership == 0:
			frappe.throw("You only study Html if you not membership")
