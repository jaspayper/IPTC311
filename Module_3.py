# Room Configuration
rooms = [
    {"room_id": 101, "type": "room1", "price": 100, "status": "Available", "inventory": ["Towels", "Minibar"]},
    {"room_id": 102, "type": "room2", "price": 200, "status": "Available", "inventory": ["Towels", "Minibar", "TV"]},
    {"room_id": 103, "type": "room3", "price": 300, "status": "Available", "inventory": ["Towels", "Minibar", "Jacuzzi"]}
]

damage_logs = []

def get_all_rooms():
    return rooms

def update_room_status(room_id, new_status):
    try:
        for room in rooms:
            if room["room_id"] == room_id:
                room["status"] = new_status
                # print(f"Room {room_id} status updated to {new_status}.") # Optional log
                return True
        print(f"❌ Room ID {room_id} not found.")
        return False
    except Exception as e:
        print(f"Error updating room status: {e}")
        return False

def log_damage(room_id, item, cost):
    try:
        # Validate cost is a number
        if not isinstance(cost, (int, float)) or cost < 0:
            print("❌ Invalid cost. Must be a positive number.")
            return 0
        
        log = {
            "room_id": room_id,
            "item": item,
            "cost": cost,
            "date": "2025-12-01" 
        }
        damage_logs.append(log)
        print(f"✅ Damage logged for Room {room_id}: {item} (₱{cost}).")
        return cost
    except Exception as e:
        print(f"Error logging damage: {e}")
        return 0