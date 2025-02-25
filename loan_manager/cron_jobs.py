# In your Transaction doctype Python file (transaction.py)
import requests
import frappe

@frappe.whitelist()
def fetch_data_from_api():
    url = "http://192.168.0.73:3000/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON
        for item in data:
            # Create or update the transaction record with the specific fields
            transaction = frappe.get_doc({
                "doctype": "Transaction",
                "description": item.get("description"),
                "date": item.get("date"),
                "paid_by": item.get("paid_by"),
               
            })
            transaction.insert(ignore_permissions=True)  # Use ignore_permissions if needed
    else:
        frappe.log_error(
            f"Failed to fetch data from API: {response.status_code}",
            "API Fetch Error"
        )
