import Module_3 as rm

tasks = []

def schedule_cleaning(room_id, task_type="Routine Clean"):
    try:
        # Check if room actually exists first
        all_rooms = rm.get_all_rooms()
        if not any(r['room_id'] == room_id for r in all_rooms):
            print(f"❌ Cannot schedule: Room {room_id} does not exist.")
            return

        task = {
            "task_id": len(tasks) + 1,
            "room_id": room_id,
            "type": task_type,
            "status": "Pending",
            "assigned_to": None
        }
        tasks.append(task)
        rm.update_room_status(room_id, "Cleaning")
        print(f"✅ Cleaning task scheduled for Room {room_id}.")
    except Exception as e:
        print(f"Error scheduling cleaning: {e}")

def assign_staff(task_id, staff_name):
    try:
        for task in tasks:
            if task["task_id"] == task_id:
                task["assigned_to"] = staff_name
                print(f"✅ Task {task_id} assigned to {staff_name}.")
                return
        print("❌ Task ID not found.")
    except Exception as e:
        print(f"Error assigning staff: {e}")

def complete_task(task_id):
    try:
        for task in tasks:
            if task["task_id"] == task_id:
                task["status"] = "Completed"
                rm.update_room_status(task["room_id"], "Available")
                print(f"✅ Task {task_id} complete. Room {task['room_id']} is Available.")
                return
        print("❌ Task ID not found.")
    except Exception as e:
        print(f"Error completing task: {e}")

def view_housekeeping_status():
    print("\n--- Housekeeping Tasks ---")
    try:
        if not tasks:
            print("No active tasks.")
        for t in tasks:
            print(f"ID: {t['task_id']} | Room: {t['room_id']} | Status: {t['status']} | Staff: {t['assigned_to']}")
    except Exception as e:
        print(f"Error viewing tasks: {e}")