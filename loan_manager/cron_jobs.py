import requests
import frappe

# Define the API endpoint
api_url = "http://192.168.0.73:3000/"

def fetch_transactions():
    # Fetch data from the API
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        for record in data:
            # Create a new Transaction record
            transaction = frappe.get_doc({
                'doctype': 'Transaction',
                'full_name': record.get('full_name'),
                'email': record.get('email'),
                'date': record.get('date'),
                'paid_by': record.get('paid_by'),
                'description': record.get('description'),
            })
            transaction.insert()
    else:
        frappe.log_error("Failed to fetch data from API", "API Error")

