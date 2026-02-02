import frappe
from frappe.utils import nowdate

def setup():
    ensure_warehouse_types()
    setup_company()
    setup_currency()
    setup_defaults()
    frappe.db.commit()
    print("Company and Currency Setup Complete")

def ensure_warehouse_types():
    if not frappe.db.exists("Warehouse Type", "Transit"):
        wt = frappe.new_doc("Warehouse Type")
        wt.name = "Transit"
        wt.warehouse_type_name = "Transit"
        wt.insert()
        print("Created Warehouse Type: Transit")

def setup_company():
    company_name = "Byteflow Enterprises"
    if not frappe.db.exists("Company", company_name):
        company = frappe.new_doc("Company")
        company.company_name = company_name
        company.default_currency = "KES"
        company.country = "Kenya"
        company.insert()
        print(f"Created Company: {company_name}")
    else:
        print(f"Company {company_name} already exists")

def setup_currency():
    # Enable USD
    if frappe.db.exists("Currency", "USD"):
        doc = frappe.get_doc("Currency", "USD")
        if not doc.enabled:
            doc.enabled = 1
            doc.save()
            print("Enabled USD Currency")
    
    # Currency Exchange: 1 USD = 135 KES
    # Check if a valid exchange rate exists for today or generally
    # For simplicity, we create a new one for today if not exists
    if not frappe.db.exists("Currency Exchange", {
        "from_currency": "USD", 
        "to_currency": "KES", 
        "exchange_rate": 135
    }):
        ce = frappe.new_doc("Currency Exchange")
        ce.date = nowdate()
        ce.from_currency = "USD"
        ce.to_currency = "KES"
        ce.exchange_rate = 135
        ce.for_buying = 1
        ce.for_selling = 1
        ce.insert()
        print("Created Fixed Exchange Rate: 1 USD = 135 KES")
    else:
        print("Exchange Rate 1 USD = 135 KES already exists")

def setup_defaults():
    # Global Defaults
    global_defaults = frappe.get_single("Global Defaults")
    global_defaults.default_company = "Byteflow Enterprises"
    global_defaults.default_currency = "KES"
    global_defaults.country = "Kenya"
    global_defaults.save()
    print("Updated Global Defaults (Company: Byteflow Enterprises, Currency: KES, Country: Kenya)")

    # System Settings (optional but good for country)
    sys_settings = frappe.get_single("System Settings")
    sys_settings.country = "Kenya"
    if not sys_settings.language:
        sys_settings.language = "en"
    if not sys_settings.time_zone:
        sys_settings.time_zone = "Africa/Nairobi"
    sys_settings.save()
    print("Updated System Settings Country to Kenya")
