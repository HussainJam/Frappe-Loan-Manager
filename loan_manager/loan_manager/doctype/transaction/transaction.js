// Copyright (c) 2025, Jamal and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Transaction", {
// 	refresh(frm) {

// 	},
// });

// frappe.ui.form.on('Transaction', {
//     amount: function (frm) {
//         update_amount_due_table(frm);
//     },

//     by: function (frm) {
//         update_amount_due_table(frm);
//     },

//     amount_due_table_add: function (frm) {
//         update_amount_due_table(frm);
//     },

//     amount_due_table_remove: function (frm) {
//         update_amount_due_table(frm);
//     }
// });

// // Function to update the 'Amount Due Table'
// function update_amount_due_table(frm) {
//     // Check if amount and paid by user are set
//     if (!frm.doc.amount || !frm.doc.by) return;

//     let total_amount = frm.doc.amount;
//     let payer = frm.doc.by;
//     let participants = [];

//     // Get all unique users from the 'Amount Due Table'
//     frm.doc.amount_due_table.forEach(row => {
//         if (row.users && !participants.includes(row.users)) {
//             participants.push(row.users);
//         }
//     });

//     // Ensure the payer is included
//     if (payer && !participants.includes(payer)) {
//         participants.push(payer);
//     }

//     let num_people = participants.length;

//     if (num_people < 1) {
//         frappe.msgprint(__('At least 1 participant is required.'));
//         return;
//     }

//     // Calculate the share for each participant
//     let per_person_share = (total_amount / num_people).toFixed(2);

//     // Clear previous data in the table
//     frm.clear_table("amount_due_table");

//     // Populate table with calculated amounts
//     participants.forEach(person => {
//         let row = frm.add_child("amount_due_table");
//         row.users = person; // Assign the user
//         row.amount_due = per_person_share; // Assign the calculated amount due
//     });

//     frm.refresh_field("amount_due_table");
// }

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


// Function to update the 'Amount Due Table'
function update_amount_due_table(frm) {
    let total_amount = frm.doc.amount || 0;
    let payer = frm.doc.by;
    let participants = new Set();

    // Collect unique users from the amount_due_table
    frm.doc.amount_due_table.forEach(row => {
        if (row.users) {
            participants.add(row.users);
        }
    });

    // Add payer to participants if they are not already included
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

    // Clear previous data in the table
    frm.clear_table("amount_due_table");

    // Populate table with calculated amounts
    participants.forEach(person => {
        let row = frm.add_child("amount_due_table");
        row.users = person; 
        row.amount_due = per_person_share; 
    });

    frm.refresh_field("amount_due_table");
}
