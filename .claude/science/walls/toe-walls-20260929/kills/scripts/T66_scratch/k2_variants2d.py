"""Kill-check driver: 2D ADM-matched R=2 (or R=1) with families removed. Usage: k2_variants2d.py R tag(base|nochi|g2only) [iters]"""
import sys, time
import numpy as np
import solve2d_fast as sf
R = int(sys.argv[1]); tag = sys.argv[2]
iters = int(sys.argv[3]) if len(sys.argv) > 3 else 400000
drop = {'base': (), 'nochi': ('chi',), 'g2only': ('chi', 'xi1'), 'noxi1': ('xi1',)}[tag]
t0 = time.time()
cols = [c for c in sf.get_cols(R) if c[0][0] not in drop]
fams = tuple(f for f in ('V2', 'T3', 'G2', 'xi1', 'chi') if f not in drop)
print(tag, "R", R, "cols", len(cols), "fams", fams, flush=True)
nrow, nr0, ei, ej, ev, b = sf.assemble_fast(cols, fams, None)
print("rows", nrow, "nr0", nr0, "nnz", len(ev), "t", round(time.time() - t0, 1), flush=True)
res, x, A, bb = sf.solve_fast(nrow, nr0, ei, ej, ev, b, len(cols), iters=iters)
print("RESULT", tag, "R", R, res, "t", round(time.time() - t0, 1), "|x|", float(np.linalg.norm(x)), "max|x|", float(np.abs(x).max()), flush=True)
np.save(f"k2_x_R{R}_{tag}.npy", x)
