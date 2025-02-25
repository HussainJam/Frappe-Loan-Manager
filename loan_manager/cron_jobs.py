# Copy fron Chatgpt , but didnot work properly 
import requests
import frappe

@frappe.whitelist()
def fetch_data_from_api():
    url = "http://192.168.0.73:3000/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  
        for item in data:
            transaction = frappe.get_doc({
                "doctype": "Transaction",
                "description": item.get("description"),
                "date": item.get("date"),
                "paid_by": item.get("paid_by"),
               
            })
            transaction.insert(ignore_permissions=True) 
    else:
        frappe.log_error(
            f"Failed to fetch data from API: {response.status_code}",
            "API Fetch Error"
        )
