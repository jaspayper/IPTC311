invoices = []

def create_invoice(guest_name, room_id, amount):
    try:
        invoice = {
            "invoice_id": len(invoices) + 1,
            "guest": guest_name,
            "room_id": room_id,
            "total_amount": amount,
            "paid_amount": 0,
            "status": "Unpaid",
            "charges": [{"description": "Room Charge", "amount": amount}]
        }
        invoices.append(invoice)
        print(f"✅ Invoice #{invoice['invoice_id']} created for {guest_name}. Total: ₱{amount}")
        return invoice['invoice_id']
    except Exception as e:
        print(f"Error creating invoice: {e}")
        return -1

def get_active_invoice_by_room(room_id):
    try:
        for inv in invoices:
            if inv["room_id"] == room_id and inv["status"] != "Paid":
                return inv
        return None
    except Exception:
        return None

def add_charge(invoice_id, description, amount):
    try:
        if not isinstance(amount, (int, float)):
            print("❌ Charge amount must be a number.")
            return False

        for inv in invoices:
            if inv["invoice_id"] == invoice_id:
                inv["charges"].append({"description": description, "amount": amount})
                inv["total_amount"] += amount
                print(f"✅ Added {description} (₱{amount}) to Invoice #{invoice_id}.")
                return True
        print("❌ Invoice not found.")
        return False
    except Exception as e:
        print(f"Error adding charge: {e}")
        return False

def record_payment(invoice_id, amount, method):
    try:
        if amount <= 0:
            print("❌ Payment amount must be positive.")
            return

        for inv in invoices:
            if inv["invoice_id"] == invoice_id:
                inv["paid_amount"] += amount
                print(f"✅ Payment of ₱{amount} received via {method}.")
                
                if inv["paid_amount"] >= inv["total_amount"]:
                    inv["status"] = "Paid"
                    print(f"🎉 Invoice #{invoice_id} is fully settled.")
                return
        print("❌ Invoice not found.")
    except Exception as e:
        print(f"Error recording payment: {e}")

def show_invoice(guest_name):
    print(f"\n--- Invoice for {guest_name} ---")
    try:
        found = False
        for inv in invoices:
            if inv["guest"].lower() == guest_name.lower():
                found = True
                print(f"ID: {inv['invoice_id']} | Status: {inv['status']} | Room: {inv['room_id']}")
                for item in inv["charges"]:
                    print(f"  - {item['description']}: ₱{item['amount']}")
                print(f"  Total: ₱{inv['total_amount']} | Paid: ₱{inv['paid_amount']}")
                print(f"  Balance: ₱{inv['total_amount'] - inv['paid_amount']}")
                print("-" * 30)
        
        if not found:
            print("No invoices found for this guest.")
    except Exception as e:
        print(f"Error showing invoice: {e}")