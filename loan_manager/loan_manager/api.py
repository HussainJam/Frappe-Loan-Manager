import frappe
import requests

@frappe.whitelist()
def fetch_transactions():
    api_url = "http://192.168.0.73:3000/"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error if API request fails
        data = response.json()

        for entry in data:
            transaction = frappe.get_doc({
                "doctype": "Transaction",
                "date": entry.get("date"),
                "description": entry.get("description"),
                "amount": entry.get("amount"),
                "by": entry.get("by")
            })
            transaction.insert(ignore_permissions=True)

        frappe.db.commit()
        return {"status": "success", "message": "Transactions added successfully!"}

    except Exception as e:
        return {"status": "error", "message": str(e)}
