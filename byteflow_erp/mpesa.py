import frappe

class MpesaHandler:
    def push_stk(self, phone, amount):
        # Stub implementation
        print(f"STK Push Payload: Phone={phone}, Amount={amount}")
        frappe.msgprint(f"Initiated M-Pesa STK Push for {phone} amount {amount}")

def on_submit_payment_entry(doc, method):
    if doc.mode_of_payment == "M-Pesa":
        # Attempt to get phone number from contact_mobile field if it exists, else default placeholder
        phone = getattr(doc, "contact_mobile", "Unknown")
        amount = doc.paid_amount
        
        handler = MpesaHandler()
        handler.push_stk(phone, amount)
