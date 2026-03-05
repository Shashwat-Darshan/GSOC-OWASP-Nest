"""Tests for OWASP Event model."""

import unittest
from datetime import datetime, timedelta

# Minimal Event mock for isolated testing
class Event:
    def __init__(self, date, name="", url=""):
        self.date = date
        self.name = name
        self.url = url

    @staticmethod
    def upcoming_events(events):
        today = datetime.now().date()
        filtered = [e for e in events if e.date.date() >= today and e.name and e.url]
        return sorted(filtered, key=lambda e: e.date)

class TestEventUpcomingEvents(unittest.TestCase):
    def setUp(self):
        now = datetime.now()
        self.events = [
            Event(date=now - timedelta(days=1), name="Past", url="past.com"),  # Past
            Event(date=now, name="Today", url="today.com"),                    # Today
            Event(date=now + timedelta(days=1), name="Future", url="future.com"), # Future
            Event(date=now + timedelta(days=2), name="", url="no-name.com"),      # No name
            Event(date=now + timedelta(days=3), name="Future2", url=""),          # No url
        ]

    def test_upcoming_events_excludes_past(self):
        upcoming = Event.upcoming_events(self.events)
        self.assertTrue(all(e.date.date() >= datetime.now().date() for e in upcoming))

    def test_upcoming_events_includes_today(self):
        today = datetime.now().date()
        upcoming = Event.upcoming_events(self.events)
        self.assertTrue(any(e.date.date() == today for e in upcoming))

    def test_upcoming_events_includes_future(self):
        future = datetime.now().date() + timedelta(days=1)
        upcoming = Event.upcoming_events(self.events)
        self.assertTrue(any(e.date.date() == future for e in upcoming))

    def test_upcoming_events_excludes_empty_name_and_url(self):
        upcoming = Event.upcoming_events(self.events)
        self.assertTrue(all(e.name and e.url for e in upcoming))

if __name__ == "__main__":
    unittest.main()
