# import frappe
# from frappe import _

# def execute(filters=None):
#     columns = [
#         {"label": _("Name"), "fieldname": "name", "fieldtype": "Data", "width": 150},
#         {"label": _("Date"), "fieldname": "date", "fieldtype": "Date", "width": 100},
#         {"label": _("Description"), "fieldname": "description", "fieldtype": "Data", "width": 250},
#         {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "width": 100},
#     ]
    
#     conditions = []
#     if filters.get("from_date"):
#         conditions.append("transaction_date >= %(from_date)s")
#     if filters.get("to_date"):
#         conditions.append("transaction_date <= %(to_date)s")
#     if filters.get("user"):
#         conditions.append("User = %(user)s")

#     # Construct the SQL query
#     transactions = frappe.db.sql("""
#         SELECT 
#             name,
#             transaction_date AS date,
#             description,
#             amount 
#         FROM 
#             `tabTransactions` 
#         WHERE 
#             docstatus < 2
#             {conditions}
#         ORDER BY 
#             transaction_date
#     """.format(conditions=" AND ".join(conditions) if conditions else ""), 
#     as_dict=1, 
#     params={
#         'from_date': filters.get("from_date"),
#         'to_date': filters.get("to_date"),
#         'user': filters.get("user")
#     })

#     return columns, transactions


def formatter(value, row, column, data, default_formatter):
    if column.get("fieldname") == "amount":
        if value > 0:
            return f'<span style="color: green;">{value}</span>'
        elif value < 0:
            return f'<span style="color: red;">{value}</span>'
    return default_formatter(value, row, column, data)
