import unittest
from datetime import datetime, timedelta

# Import your modules
import Module_1 as rsvp
import Module_3 as rooms
import Module_5 as bill

class TestHMS(unittest.TestCase):

    def setUp(self):
        rsvp.reservations.clear()
        rsvp.waitlist.clear()
        bill.invoices.clear()
        for r in rooms.rooms:
            r["status"] = "Available"

    # ... [Previous tests remain here] ...

    # ==========================================
    # NEW TEST: PAST DATE RESTRICTION
    # ==========================================
    def test_create_reservation_past_date(self):
        """Test that the system REJECTS dates in the past."""
        
        # Calculate yesterday's date dynamically
        yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        
        print(f"\nTesting rejection of past date: {yesterday}")
        
        # Attempt to book for yesterday
        rsvp.create_reservation("Marty McFly", "room1", yesterday)
        
        # Assertion: Reservation list should still be empty
        self.assertEqual(len(rsvp.reservations), 0)
        
    def test_create_reservation_future_date(self):
        """Test that the system ACCEPTS dates in the future."""
        
        # Calculate tomorrow's date dynamically
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        
        rsvp.create_reservation("Doc Brown", "room1", tomorrow)
        
        # Assertion: Reservation should exist
        self.assertEqual(len(rsvp.reservations), 1)
        self.assertEqual(rsvp.reservations[0]["check_in"], tomorrow)

if __name__ == '__main__':
    unittest.main()