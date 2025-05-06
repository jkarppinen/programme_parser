# Programme Schedule Parser

This project extracts and processes radio programme schedules from HTML. It supports parsing multi-day schedules, segmenting long shows into smaller blocks, and outputting durations in either hours or seconds.

---

## 📦 Features

- Parses Finnish-style radio schedule HTML (e.g. `lauantai 19.4.`)
- Supports multiple days and long shows
- Optional 2-hour segment splitting
- Duration output in hours or seconds
- Modular and testable codebase with pluggable parsers

---

## 🗂 Project Structure

```
.
├── main.py                    # CLI entry point
├── programme.py               # Programme model
├── printer.py                 # Output formatting
├── parsers/                   # Platform specific parsers
├── test/                      # Unit tests
├── pyproject.toml             # Poetry / dependency configuration
├── poetry.lock
└── README.md
```

---

## 🚀 Usage

### Run parser on HTML file

```bash
python main.py ~/www/ohjelmistokartta.html
```

### Split long shows into 2-hour chunks

```bash
python main.py ~/www/ohjelmistokartta.html --two-hour
```

### Show durations in seconds

```bash
python main.py ~/www/ohjelmistokartta.html --seconds
```

### Select platform parser explicitly

```bash
python main.py ~/www/ohjelmistokartta.html --parser rattoradio
```

---

## 🧪 Running Tests

Install development dependencies:

```bash
poetry install
```

Run tests with `pytest`:

```bash
PYTHONPATH=. poetry run pytest
```

If you're not using Poetry:

```bash
pip install -r requirements.txt  # if applicable
PYTHONPATH=. pytest
```

---

## 🧰 Requirements

- Python 3.9+
- [BeautifulSoup 4](https://pypi.org/project/beautifulsoup4/)
- [pytest](https://pypi.org/project/pytest/)

If you're using [Poetry](https://python-poetry.org/):

```bash
poetry install
```
