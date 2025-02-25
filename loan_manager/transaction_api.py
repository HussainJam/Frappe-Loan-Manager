# didnot work , need to modify 
import frappe
import requests

@frappe.whitelist()
def fetch_transactions():
    try:
        api_url = "http://192.168.0.73:3000/"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            
            for item in data:
                transaction = frappe.get_doc({
                    "doctype": "Transaction",
                    "date": item.get("date"),
                    "description": item.get("description"),
                    "amount": item.get("amount"),
                    "paid_by": item.get("paid_by"),
                    "users": item.get("users"),
                })
                transaction.insert(ignore_permissions=True)

            frappe.db.commit()
            return {"status": "success", "message": "Transactions imported successfully"}

        else:
            return {"status": "error", "message": "Failed to fetch data"}

    except Exception as e:
        frappe.log_error(f"Error in fetch_transactions: {str(e)}")
        return {"status": "error", "message": str(e)}
