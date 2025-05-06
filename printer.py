class SchedulePrinter:
    def __init__(self, programmes, use_seconds=False):
        self.programmes = programmes
        self.use_seconds = use_seconds

    def print(self):
        for prog in self.programmes:
            data = prog.to_dict(use_seconds=self.use_seconds)
            print(f"{data['date']} {data['start']}–{data['end']} ({data['duration']}): {data['title']}")
