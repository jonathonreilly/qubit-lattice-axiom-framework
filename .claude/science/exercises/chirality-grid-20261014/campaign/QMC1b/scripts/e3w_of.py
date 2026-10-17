"""print the primary E3w of one run file (used by supplementary.sh)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from analysis_b import summarize
r = summarize(sys.argv[1]); print(f"{r['E3w']:.6f} {r['n']}")
