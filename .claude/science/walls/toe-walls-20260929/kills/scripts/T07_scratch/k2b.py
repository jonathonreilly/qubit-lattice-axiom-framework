import sys, json
from k2_scaling import run
w = float(sys.argv[1]); g = float(sys.argv[2]); alpha = 1.0
L = int(max(120, 40 * w + 2 * 8 * w * 2))
r = run(L, w, alpha, g)
print(json.dumps(r), flush=True)
