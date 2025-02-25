import frappe
from frappe import _

# Paid Number Card 
@frappe.whitelist()
def get_paid_amount_for_logged_in_user():
    user = frappe.session.user
    value = calculate_paid_amount(user)  

    return {
        "value": value,
        "fieldtype": "Currency",

    }

def calculate_paid_amount(user):
    # For now showing this value bkz permissions is remaining 
    return 800.00 
