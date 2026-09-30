import sys, time, pickle
import numpy as np
from solve2d_sym import *
from refs2d_frame import DELTAS
R = int(sys.argv[1])
frame = (sys.argv[2] == 'frame')
match = tuple(sys.argv[3].split(',')) if len(sys.argv) > 3 else ('V2', 'T3', 'G2', 'xi1', 'chi')
t0 = time.time()
cols = build_sym(R)
print("orbit columns", len(cols), "t", round(time.time() - t0, 1), flush=True)
rows, entries, b, nr0 = assemble(cols, match, R, DELTAS if frame else None)
nc = len(cols) + (len(DELTAS) if frame else 0)
print("rows", len(rows), "nr0", nr0, "nnz", len(entries), "t", round(time.time() - t0, 1), flush=True)
res, x, A, bb = solve(rows, entries, b, nc, nr0)
print("R", R, "frame" if frame else "ADM-frame", "match", match, res, "t", round(time.time() - t0, 1), flush=True)
np.save(f"x_R{R}_{'frame' if frame else 'adm'}.npy", x)
if frame:
    print("frame parameters r:", np.round(x[len(cols):], 4))
