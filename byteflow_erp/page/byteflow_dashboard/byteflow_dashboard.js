
frappe.pages['byteflow_dashboard'].on_page_load = function (wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Dashboard',
        single_column: true
    });

    // Load CSS
    frappe.require('byteflow_dashboard.css');

    // Render logic
    const dashboard = new ByteflowDashboard(page);
    dashboard.render();
};

class ByteflowDashboard {
    constructor(page) {
        this.page = page;
        this.wrapper = $(page.body);
    }

    render() {
        this.wrapper.addClass('byteflow-dashboard');

        this.render_header();
        this.render_quick_actions();
        this.render_metrics();
    }

    render_header() {
        this.wrapper.append(`
            <div class="bf-header">
                <div class="bf-title">Welcome to Byteflow ERP</div>
                <div class="bf-subtitle">Efficient management for modern enterprises in Kenya.</div>
            </div>
        `);
    }

    render_quick_actions() {
        this.wrapper.append(`<div class="bf-section-title">Quick Actions</div>`);

        const actions = [
            {
                title: "New Invoice",
                desc: "Create a new Sales Invoice for a customer.",
                icon: "fa fa-file-invoice-dollar",
                route: "Form/Sales Invoice/New"
            },
            {
                title: "Purchase Order",
                desc: "Raise a new PO for suppliers.",
                icon: "fa fa-shopping-cart",
                route: "Form/Purchase Order/New"
            },
            {
                title: "Record Payment",
                desc: "Log a Payment Entry (M-Pesa/Cash).",
                icon: "fa fa-money-bill-wave",
                route: "Form/Payment Entry/New"
            },
            {
                title: "Customer List",
                desc: "View and manage your customers.",
                icon: "fa fa-users",
                route: "List/Customer"
            }
        ];

        let grid_html = `<div class="bf-grid">`;

        actions.forEach(action => {
            grid_html += `
                <div class="bf-card" onclick="frappe.set_route('${action.route}')">
                    <div class="bf-card-icon"><i class="${action.icon}"></i></div>
                    <div class="bf-card-title">${action.title}</div>
                    <div class="bf-card-desc">${action.desc}</div>
                </div>
            `;
        });

        grid_html += `</div>`;
        this.wrapper.append(grid_html);
    }

    render_metrics() {
        // Placeholder metrics - real ones would fetch via frappe.call
        this.wrapper.append(`<div class="bf-section-title">Key Performance Indicators (Demo)</div>`);

        const metrics = [
            { label: "Today's Revenue", value: "KES 150,000" },
            { label: "Pending Orders", value: "12" },
            { label: "Active Users", value: "5" },
            { label: "Exchange Rate (USD)", value: "135.00" }
        ];

        let metrics_html = `<div class="bf-metrics-grid">`;
        metrics.forEach(m => {
            metrics_html += `
                <div class="bf-metric-card">
                    <div class="bf-metric-value">${m.value}</div>
                    <div class="bf-metric-label">${m.label}</div>
                </div>
            `;
        });
        metrics_html += `</div>`;

        this.wrapper.append(metrics_html);
    }
}
