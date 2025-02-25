# Copyright (c) 2025, Jamal and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Transaction(Document):
	pass


# In your Transaction doctype Python file (transaction.py)
# import requests
# import frappe

# @frappe.whitelist()
# def fetch_data_from_api():
#     url = "http://192.168.0.73:3000/"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()  
#         for item in data:
#             transaction = frappe.get_doc({
#                 "doctype": "Transaction",
#                 "description": item.get("description"),  # Data type: Data
#                 "date": item.get("date"),  # Data type: Date
#                 "paid_by": item.get("paid_by"),  # Data type: Link
#                 "amount": item.get("amount"),  # Data type: Currency
#             })
#             transaction.insert(ignore_permissions=True)  # Use ignore_permissions if needed
#     else:
#         frappe.log_error(
#             f"Failed to fetch data from API: {response.status_code}",
#             "API Fetch Error"
#         )
