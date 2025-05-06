from datetime import datetime, timedelta

class Programme:
    def __init__(self, title, start_dt: datetime, end_dt: datetime):
        self.title = title
        self.start_dt = start_dt
        self.end_dt = end_dt

    @property
    def duration(self) -> timedelta:
        return self.end_dt - self.start_dt

    def to_dict(self, use_seconds=False):
        duration_val = int(self.duration.total_seconds()) if use_seconds else int(self.duration.total_seconds() // 3600)
        unit = "s" if use_seconds else "h"
        return {
            'date': self.start_dt.strftime('%Y-%m-%d'),
            'start': self.start_dt.strftime('%H:%M'),
            'end': self.end_dt.strftime('%H:%M'),
            'duration': f"{duration_val}{unit}",
            'title': self.title
        }
