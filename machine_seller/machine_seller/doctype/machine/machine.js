// Copyright (c) 2025, mostafa k. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Machine", {
    refresh: (frm) => {
        frm.trigger("type");
    },

    type(frm) {
        if (!frm.doc.type) {
            frm.clear_table("spare_parts");
            frm.refresh_field("spare_parts");
            return;
        }

        frappe.call({
            method: "machine_seller.machine_seller.doctype.machine.machine.get_spare_parts",
            args: {
                type: frm.doc.type
            },
            callback: function (r) {
                if (r.message) {
                    
                    frm.clear_table("spare_parts");
                    
                    r.message.forEach(function (spare_part) {
                        let child = frm.add_child("spare_parts");
                        child.spare_part = spare_part.spare_part_name;
                        child.type = spare_part.type;
                    });
                    
                    frm.refresh_field("spare_parts");
                }
            }
        });
    }
});
