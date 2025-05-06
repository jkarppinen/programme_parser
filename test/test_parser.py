import os
from parsers.rattoradio_parser import RattoradioParser

def test_parse_single_day():
    html = """
    <div class="panel">
      <div class="panel-heading">
        <h4 class="panel-title"><a href="#day1">lauantai 19.4.</a></h4>
      </div>
      <div id="day1" class="panel-collapse">
        <ul class="time-list">
          <li><a><time>08:00–10:00</time><span>Test Show</span></a></li>
        </ul>
      </div>
    </div>
    """

    parser = RattoradioParser(html, year=2025)
    schedule = parser.parse()
    assert len(schedule) == 1
    assert schedule[0].title == "Test Show"
    assert schedule[0].start_dt.strftime("%Y-%m-%d %H:%M") == "2025-04-19 08:00"

def test_two_hour_split():
    html = """
    <div class="panel">
      <div class="panel-heading">
        <h4 class="panel-title"><a href="#day1">lauantai 19.4.</a></h4>
      </div>
      <div id="day1" class="panel-collapse">
        <ul class="time-list">
          <li><a><time>00:00–08:00</time><span>Long Show</span></a></li>
        </ul>
      </div>
    </div>
    """
    parser = RattoradioParser(html, year=2025, two_hour_mode=True)
    schedule = parser.parse()
    assert len(schedule) == 4
    assert schedule[0].title.startswith("Long Show (segment 1)")
