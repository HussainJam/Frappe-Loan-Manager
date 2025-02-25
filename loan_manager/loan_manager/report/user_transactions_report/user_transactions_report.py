import frappe
from frappe import _



def formatter(value, row, column, data, default_formatter):
    if column.get("fieldname") == "amount":
        if value > 0:
            return f'<span style="color: green;">{value}</span>'
        elif value < 0:
            return f'<span style="color: red;">{value}</span>'
    return default_formatter(value, row, column, data)
