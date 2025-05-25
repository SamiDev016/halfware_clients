# Copyright (c) 2025, SamiDev016 and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ClientForm(Document):
	def after_insert(doc, method):
    		try:
        	payload = {
            "erp": doc.erp,
            "description": doc.description,
        }
        # You can secure this with token or signature later
        response = requests.post("https://demo.halfware.info/api/method/halfware_clients.api.receive_form", json=payload)
        response.raise_for_status()
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error sending client form to demo server")
