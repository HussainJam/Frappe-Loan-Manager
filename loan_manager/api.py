# import frappe
# from frappe import _

# @frappe.whitelist()
# def get_total_payable():
#     total_amount = frappe.db.sql("""
#         SELECT SUM(amount) 
#         FROM `tabTransaction`
#         WHERE docstatus = 1
#     """, as_list=True)

#     return {
#         "value": total_amount[0][0] if total_amount and total_amount[0][0] else 0,
#         "fieldtype": "Currency"
#     }


import frappe

@frappe.whitelist()
def get_total_payable():
    total_amount = frappe.db.sql("""
        SELECT SUM(amount) 
        FROM `tabTransaction`
    """, as_list=True)

    return {
        "value": total_amount[0][0] if total_amount and total_amount[0][0] else 0,
        "fieldtype": "Currency"
    }
