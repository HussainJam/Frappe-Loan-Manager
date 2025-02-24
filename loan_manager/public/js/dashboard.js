frappe.ready(function() {
    const totalAmountCard = {
        label: 'Total Amount',
        value: 0, // Default value
        color: 'blue', // Card color
    };

    const paidAmountCard = {
        label: 'Paid Amount',
        value: 0, // Default value
        color: 'green', // Card color
    };

    // Function to fetch total amount
    function fetchTotalAmount() {
        frappe.db.get_value('Your Doctype', 'Your Document Name', 'total_amount_field', (r) => {
            if (r && r.total_amount_field) {
                totalAmountCard.value = r.total_amount_field;
                updateDashboard();
            }
        });
    }

    // Function to fetch paid amount
    function fetchPaidAmount() {
        frappe.db.get_value('Your Doctype', 'Your Document Name', 'paid_amount_field', (r) => {
            if (r && r.paid_amount_field) {
                paidAmountCard.value = r.paid_amount_field;
                updateDashboard();
            }
        });
    }

    // Function to update the dashboard with the fetched values
    function updateDashboard() {
        $('#total-amount-card').text(totalAmountCard.label + ': ' + totalAmountCard.value);
        $('#paid-amount-card').text(paidAmountCard.label + ': ' + paidAmountCard.value);
    }

    // Fetch the amounts
    fetchTotalAmount();
    fetchPaidAmount();
});
