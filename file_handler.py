from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"

# Create data directory automatically
DATA_DIR.mkdir(exist_ok=True)

def get_file_path(filename):
    return DATA_DIR / filename


def read_records(filename):
    """Read all records from a text file."""

    path = get_file_path(filename)

    try:
        with open(path, "r", encoding="utf-8") as file:
            return [
                line.strip().split("|")
                for line in file
                if line.strip()
            ]

    except FileNotFoundError:
        return []


def append_record(filename, record):
    """Append a new record to a file."""

    path = get_file_path(filename)

    with open(path, "a", encoding="utf-8") as file:
        file.write("|".join(map(str, record)) + "\n")


def write_records(filename, records):
    """Overwrite a file with the supplied records."""

    path = get_file_path(filename)

    with open(path, "w", encoding="utf-8") as file:
        for record in records:
            file.write("|".join(map(str, record)) + "\n")
