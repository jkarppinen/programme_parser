from datetime import datetime, timedelta
from programme import Programme

def test_programme_duration_hours():
    start = datetime(2025, 4, 19, 8, 0)
    end = start + timedelta(hours=2)
    prog = Programme("Test Show", start, end)

    assert prog.duration.total_seconds() == 7200
    data = prog.to_dict(use_seconds=False)
    assert data['duration'] == "2h"

def test_programme_duration_seconds():
    start = datetime(2025, 4, 19, 8, 0)
    end = start + timedelta(minutes=90)
    prog = Programme("Short Show", start, end)

    data = prog.to_dict(use_seconds=True)
    assert data['duration'] == "5400s"
