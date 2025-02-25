// Copyright (c) 2025, Jamal and contributors
// For license information, please see license.txt


frappe.ui.form.on('Transaction', {
    amount: function (frm) {
        update_amount_due_table(frm);
    },
    by: function (frm) {
        update_amount_due_table(frm);
    },
    amount_due_table_add: function (frm) {
        update_amount_due_table(frm);
    },
    amount_due_table_remove: function (frm) {
        update_amount_due_table(frm);
    },
    amount_due_table: function(frm) {
        update_amount_due_table(frm);
    }
});


function update_amount_due_table(frm) {
    let total_amount = frm.doc.amount || 0;
    let payer = frm.doc.by;
    let participants = new Set();

    frm.doc.amount_due_table.forEach(row => {
        if (row.users) {
            participants.add(row.users);
        }
    });

    if (payer) {
        participants.add(payer);
    }
    participants = Array.from(participants);
    let num_people = participants.length;

    if (num_people < 1) {
        frappe.msgprint(__('At least 1 participant is required.'));
        return;
    }

    let per_person_share = (total_amount / num_people).toFixed(2);

    frm.clear_table("amount_due_table");

    participants.forEach(person => {
        let row = frm.add_child("amount_due_table");
        row.users = person; 
        row.amount_due = per_person_share; 
    });

    frm.refresh_field("amount_due_table");
}


