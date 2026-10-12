# Integrity fixture sentinel; no scientific computation.
from pathlib import Path
import sys
Path(__file__).with_suffix(".launched").write_text("launched\n")
print("SENTINEL " + Path(__file__).name, flush=True)
sys.exit(0)
