"""2D R=2: sensitivity of the matched system to wrong continuum targets (deduped rows, capped lsqr iterations)."""
import sys, time, copy
import numpy as np
import solve2d_fast as sf
import solve2d_fast2 as sf2
from fractions import Fraction as F
tag = sys.argv[1]
iters = int(sys.argv[2])
base = copy.deepcopy(sf.REF2)
if tag == 'xi1flip':
    sf.REF2['xi1'] = [(-c, sl) for c, sl in base['xi1']]
elif tag == 'G2x2':
    sf.REF2['G2'] = [(2 * c, sl) for c, sl in base['G2']]
elif tag == 'T3x32':
    sf.REF2['T3'] = [(1.5 * c, sl) for c, sl in base['T3']]
t0 = time.time()
cols = sf.get_cols(2)
rows, ei, ej, ev, b = sf2.assemble_dedupe(cols, (), None)
nr0 = len(rows)
nrow, nr0_full, ei_f, ej_f, ev_f, b_f = sf.assemble_fast([(l, {}, fs) for l, cs, fs in cols], ('V2', 'T3', 'G2', 'xi1', 'chi'), None)
ei_f = np.array(ei_f); ej_f = np.array(ej_f); ev_f = np.array(ev_f)
sel = ei_f >= nr0_full
ei2 = list(ei) + list(ei_f[sel] - nr0_full + nr0); ej2 = list(ej) + list(ej_f[sel]); ev2 = list(ev) + list(ev_f[sel])
b2 = dict(b)
for i, c in b_f.items():
    if i >= nr0_full: b2[i - nr0_full + nr0] = c
nrow2 = nr0 + (nrow - nr0_full)
print(tag, "rows", nrow2, "cols", len(cols), "t", round(time.time() - t0, 1), flush=True)
res, x, A, bb = sf.solve_fast(nrow2, nr0, ei2, ej2, ev2, b2, len(cols), iters=iters)
print("SENS", tag, "iters cap", iters, res, "t", round(time.time() - t0, 1), flush=True)
