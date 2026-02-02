
const add_download_button = function (frm) {
    if (!frm.is_new()) {
        frm.add_custom_button(__('Download Options'), function () {
            let d = new frappe.ui.Dialog({
                title: 'Download Options',
                fields: [
                    {
                        fieldtype: 'HTML',
                        fieldname: 'buttons_area',
                    }
                ]
            });

            d.fields_dict.buttons_area.$wrapper.html(`
                <div style="padding: 10px; display: flex; justify-content: space-around;">
                    <button class="btn btn-primary btn-sm" id="btn-pdf">PDF</button>
                    <button class="btn btn-default btn-sm" id="btn-csv">CSV</button>
                </div>
            `);

            d.get_close_btn().show();

            d.$wrapper.find('#btn-pdf').on('click', function () {
                frm.print_doc();
                d.hide();
            });

            d.$wrapper.find('#btn-csv').on('click', function () {
                download_csv(frm);
                d.hide();
            });

            d.show();
        });
    }
};

const download_csv = function (frm) {
    let row_data = [];

    // Headers
    let headers = ["Item Code", "Item Name", "Description", "Qty", "Rate", "Amount", "Currency"];
    row_data.push(headers);

    // Items
    (frm.doc.items || []).forEach(item => {
        row_data.push([
            item.item_code,
            item.item_name,
            item.description || "",
            item.qty,
            item.rate,
            item.amount,
            frm.doc.currency // Ensure document currency is used
        ]);
    });

    // Convert to CSV string
    let csv_content = "";
    row_data.forEach(row => {
        let row_str = row.map(val => `"${val}"`).join(",");
        csv_content += row_str + "\r\n";
    });

    // Trigger Download
    const blob = new Blob([csv_content], { type: 'text/csv;charset=utf-8;' });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", `${frm.doc.name}_${frm.doc.currency}.csv`);
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
};

frappe.ui.form.on("Sales Invoice", {
    refresh: function (frm) {
        add_download_button(frm);
    }
});

frappe.ui.form.on("Purchase Order", {
    refresh: function (frm) {
        add_download_button(frm);
    }
});
