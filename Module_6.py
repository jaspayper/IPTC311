# Module_6.py: Reporting & Analytics
import csv
from datetime import datetime
import Module_3 as rm
import Module_5 as bm

# ==========================================
# VIEWING FUNCTIONS (Print to Screen)
# ==========================================

def generate_occupancy_report():
    print("\n--- Occupancy Report (View) ---")
    try:
        rooms = rm.get_all_rooms()
        total = len(rooms)
        
        if total == 0:
            print("⚠️ No rooms defined in the system.")
            return

        occupied = len([r for r in rooms if r["status"] == "Occupied" or r["status"] == "Reserved"])
        occupancy_rate = (occupied / total) * 100
        
        print(f"Total Rooms: {total}")
        print(f"Occupied/Reserved: {occupied}")
        print(f"Occupancy Rate: {occupancy_rate:.1f}%")
        
    except ZeroDivisionError:
        print("⚠️ Error: Total rooms is zero, cannot calculate percentage.")
    except Exception as e:
        print(f"❌ An error occurred generating report: {e}")

def generate_financial_report():
    print("\n--- Financial Report (View) ---")
    try:
        total_revenue = 0
        outstanding = 0
        
        if not bm.invoices:
            print("No financial data available.")
            return

        for inv in bm.invoices:
            total_revenue += inv["total_amount"]
            outstanding += (inv["total_amount"] - inv["paid_amount"])
            
        print(f"Total Revenue Generated: ₱{total_revenue}")
        print(f"Outstanding Payments: ₱{outstanding}")
    except Exception as e:
        print(f"❌ An error occurred generating financial report: {e}")

# ==========================================
# EXPORT FUNCTIONS (Save to CSV)
# ==========================================

def export_occupancy_to_csv():
    print("\n--- Exporting Occupancy Report to CSV ---")
    try:
        rooms = rm.get_all_rooms()
        if not rooms:
            print("❌ No data to export.")
            return

        # Generate a unique filename with a timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"occupancy_report_{timestamp}.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write Header
            writer.writerow(["Room ID", "Type", "Price", "Status", "Inventory Items"])
            
            # Write Rows
            for room in rooms:
                # Join inventory list into a single string
                inventory_str = ", ".join(room.get("inventory", []))
                writer.writerow([
                    room["room_id"], 
                    room["type"], 
                    room["price"], 
                    room["status"], 
                    inventory_str
                ])
        
        print(f"✅ Successfully exported to: {filename}")

    except PermissionError:
        print(f"❌ Error: Permission denied. Please close the file '{filename}' if it is open.")
    except Exception as e:
        print(f"❌ An unexpected error occurred during export: {e}")

def export_financial_to_csv():
    print("\n--- Exporting Financial Report to CSV ---")
    try:
        invoices = bm.invoices
        if not invoices:
            print("❌ No invoice data to export.")
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"financial_report_{timestamp}.csv"

        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write Header
            writer.writerow(["Invoice ID", "Guest Name", "Room ID", "Total Amount", "Paid Amount", "Balance", "Status"])
            
            # Write Rows
            for inv in invoices:
                balance = inv["total_amount"] - inv["paid_amount"]
                writer.writerow([
                    inv["invoice_id"],
                    inv["guest"],
                    inv["room_id"],
                    inv["total_amount"],
                    inv["paid_amount"],
                    balance,
                    inv["status"]
                ])
        
        print(f"✅ Successfully exported to: {filename}")

    except PermissionError:
        print(f"❌ Error: Permission denied. Please close the file '{filename}' if it is open.")
    except Exception as e:
        print(f"❌ An unexpected error occurred during export: {e}")