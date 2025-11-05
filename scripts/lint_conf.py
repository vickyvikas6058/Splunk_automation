import yaml, sys
from pathlib import Path

def check_duplicates(file, key):
    data = yaml.safe_load(Path(file).read_text())
    names = [x['name'] for x in data.get(key, [])]
    dups = set([n for n in names if names.count(n) > 1])
    if dups:
        print(f"Duplicate {key}: {dups}")
        sys.exit(1)
    print(f"{file} OK")

check_duplicates("src/indexes.yaml", "indexes")
check_duplicates("src/inputs.yaml", "inputs")
