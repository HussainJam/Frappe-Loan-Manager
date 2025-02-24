frappe.query_reports["User Transactions Report"] = {


    
    "formatter": function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "amount") {
            if (data.amount > 0) {
                return `<span style="color: green; font-weight: bold;">${value}</span>`;
            } else if (data.amount < 0) {
                return `<span style="color: red; font-weight: bold;">${value}</span>`;
            }
        }
        return value;
    }
};
