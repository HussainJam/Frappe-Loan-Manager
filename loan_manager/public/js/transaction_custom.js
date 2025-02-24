frappe.ui.form.on('Transaction', {
    refresh: function(frm) {
        frm.add_custom_button(__('Fetch Transactions'), function() {
            frappe.call({
                method: "loan_manager.api.fetch_transactions",
                callback: function(response) {
                    if (response.message) {
                        frappe.msgprint(__('Transactions fetched successfully!'));
                        frappe.msgprint(JSON.stringify(response.message, null, 2)); // Debugging
                    }
                }
            });
        });
    }
});
