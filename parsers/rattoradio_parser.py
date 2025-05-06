import re
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from programme import Programme

class RattoradioParser:
    def __init__(self, html, year=2025, two_hour_mode=False):
        self.soup = BeautifulSoup(html, 'html.parser')
        self.year = year
        self.two_hour_mode = two_hour_mode

    def parse(self):
        programmes = []
        panels = self.soup.select('.panel')

        for panel in panels:
            heading = panel.select_one('.panel-title a')
            if not heading:
                continue
            date_obj = self._parse_finnish_date(heading.text.strip())

            for item in panel.select('ul.time-list li'):
                time_tag = item.find('time')
                title_tag = item.find('span')
                if not time_tag or not title_tag:
                    continue
                start_str, end_str, start_time, duration = self._parse_time_range(time_tag.text.strip())
                start_dt = datetime.combine(date_obj, start_time.time())
                end_dt = start_dt + duration
                prog = Programme(title_tag.text.strip(), start_dt, end_dt)

                if self.two_hour_mode and duration >= timedelta(hours=2):
                    programmes.extend(self._split_to_chunks(prog))
                else:
                    programmes.append(prog)

        return sorted(programmes, key=lambda p: p.start_dt)

    def _parse_finnish_date(self, date_str):
        match = re.search(r'(\d{1,2})\.(\d{1,2})\.', date_str)
        if not match:
            raise ValueError(f"Invalid date format: {date_str}")
        day, month = map(int, match.groups())
        return datetime(self.year, month, day).date()

    def _parse_time_range(self, time_str):
        start_str, end_str = re.sub(r'–|&ndash;', '-', time_str).split('-')
        fmt = "%H:%M"
        start = datetime.strptime(start_str.strip(), fmt)
        end = datetime.strptime(end_str.strip(), fmt)
        if end <= start:
            end += timedelta(days=1)
        return start_str, end_str, start, end - start

    def _split_to_chunks(self, prog, chunk_hours=2):
        chunk_seconds = chunk_hours * 3600
        num_chunks = int(prog.duration.total_seconds() // chunk_seconds)
        chunks = []
        for i in range(num_chunks):
            chunk_start = prog.start_dt + timedelta(seconds=i * chunk_seconds)
            chunk_end = chunk_start + timedelta(seconds=chunk_seconds)
            chunks.append(Programme(f"{prog.title} (segment {i+1})", chunk_start, chunk_end))
        return chunks
