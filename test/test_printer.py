from datetime import datetime, timedelta
from programme import Programme
from printer import SchedulePrinter

def test_printer_output(capsys):
    start = datetime(2025, 4, 19, 10, 0)
    end = start + timedelta(hours=2)
    programme = Programme("Test Show", start, end)
    printer = SchedulePrinter([programme], use_seconds=False)
    printer.print()

    captured = capsys.readouterr()
    assert "2025-04-19 10:00–12:00 (2h): Test Show" in captured.out
