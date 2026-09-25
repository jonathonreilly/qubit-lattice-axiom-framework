"""Read-only compact full view of the correspondence output; no filtering of rows."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
data=json.loads((HERE/'post_verification.stdout.txt').read_bytes())
for key,value in data.items():
    print(key)
    if isinstance(value,list):
        for row in value:print(json.dumps(row,separators=(',',':')))
    else:print(json.dumps(value,separators=(',',':')))
