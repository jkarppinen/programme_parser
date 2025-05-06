import argparse
import sys
import os
import datetime

from parsers.rattoradio_parser import RattoradioParser
from printer import SchedulePrinter

PARSERS = {
    "rattoradio": RattoradioParser
}

def main():
    
    parser = argparse.ArgumentParser(description="HTML schedule parser")
    parser.add_argument("html_file", help="HTML file with schedule")
    parser.add_argument("--parser", choices=PARSERS.keys(), default="rattoradio", help="Which parser to use")
    parser.add_argument("--year", type=int, default=int(datetime.now().year), help="Year (if not defined)")
    parser.add_argument("--two-hour", action="store_true", help="Split shows into 2-hour segments")
    parser.add_argument("--seconds", action="store_true", help="Show durations in seconds")

    args = parser.parse_args()

    if not os.path.exists(args.html_file):
        print(f"Error: File '{args.html_file}' not found.")
        sys.exit(1)

    with open(args.html_file, encoding='utf-8') as f:
        html = f.read()

    ParserClass = PARSERS[args.parser]
    parser_instance = ParserClass(html, year=args.year, two_hour_mode=args.two_hour)
    schedule = parser_instance.parse()

    printer = SchedulePrinter(schedule, use_seconds=args.seconds)
    printer.print()

if __name__ == "__main__":
    main()
