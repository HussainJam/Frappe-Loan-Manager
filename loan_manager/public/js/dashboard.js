frappe.ready(function() {
    const totalAmountCard = {
        label: 'Total Amount',
        value: 0, 
        color: 'blue', 
    };

    const paidAmountCard = {
        label: 'Paid Amount',
        value: 0, 
        color: 'green', 
    };

    function fetchTotalAmount() {
        frappe.db.get_value('Your Doctype', 'Your Document Name', 'total_amount_field', (r) => {
            if (r && r.total_amount_field) {
                totalAmountCard.value = r.total_amount_field;
                updateDashboard();
            }
        });
    }

    function fetchPaidAmount() {
        frappe.db.get_value('Your Doctype', 'Your Document Name', 'paid_amount_field', (r) => {
            if (r && r.paid_amount_field) {
                paidAmountCard.value = r.paid_amount_field;
                updateDashboard();
            }
        });
    }

    function updateDashboard() {
        $('#total-amount-card').text(totalAmountCard.label + ': ' + totalAmountCard.value);
        $('#paid-amount-card').text(paidAmountCard.label + ': ' + paidAmountCard.value);
    }

    fetchTotalAmount();
    fetchPaidAmount();
});
