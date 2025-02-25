import frappe
from frappe import _


@frappe.whitelist()
def get_paid_amount_for_logged_in_user():
    user = frappe.session.user
    value = calculate_paid_amount(user)  

    return {
        "value": value,
        "fieldtype": "Currency",
        "route_options": {"from_date": "2023-05-23"},
        "route": ["query-report", "Permitted Documents For User"]
    }

def calculate_paid_amount(user):
    
    return 800.00 
