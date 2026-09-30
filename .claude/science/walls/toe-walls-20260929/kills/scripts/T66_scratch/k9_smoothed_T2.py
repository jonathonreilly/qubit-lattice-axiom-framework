"""Side check (not part of the attack): is the E2 obstruction specific to T2 having the lapse at the momentum's own site?
Replace T2[N] by T2 with the lapse smoothed, N~(n) = sum_j w_j N(n+j), in both {G2,T2} and T2[ell]. E2 alone (PP sector) + weak ell conditions, planar."""
import sys, itertools
from k7_GC import *
import k7_GC
import solve

R = int(sys.argv[1]); RL = int(sys.argv[2]); W = sys.argv[3]
weights = {'site': {0: F(1)}, 'smooth': {-1: F(1, 4), 0: F(1, 2), 1: F(1, 4)}, 'fwd': {0: F(1, 2), 1: F(1, 2)}}[W]

def T2s_of_lapse(lapse_mono_fn, alpha=ALPHA, c=CC):
    """functional sum_n sum_j w_j Ylapse(n+j) PP(n); lapse_mono_fn(shift) -> tuple of parameter variables located at n+shift."""
    out = {}
    pre = 1 / (4 * alpha)
    for j, wj in weights.items():
        base = lapse_mono_fn(j)
        for aa in COMPS:
            add(out, base + (V('P', aa, 0), V('P', aa, 0)), wj * pre * (1 - c))
        for aa, bb in itertools.combinations(COMPS, 2):
            add(out, base + (V('P', aa, 0), V('P', bb, 0)), wj * pre * (-2 * c))
    return out

T2N = T2s_of_lapse(lambda j: (V('N', 0, j),))
cols, rows, entries, b = solve.build(R, 'full')   # (identity rows unused below)
nc0 = len(cols)
rows = {}; entries2 = []; b = {}
def rid(key):
    if key not in rows: rows[key] = len(rows)
    return rows[key]
G1 = G1X()
for j, (lab, d) in enumerate(cols):
    fam, u = lab
    gc = {}
    if fam == 'G2':
        g2 = G2X(u); gc = bracket(g2, T2N)
    elif fam == 'T3':
        gc = bracket(G1, T3_of(u, 'N'))
    for mono, cf in gc.items():
        entries2.append((rid(('GC', mono)), j, cf))
ell = [(a, bb) for a in range(-RL, RL + 1) for bb in range(-RL, RL + 1)]
for k_, (a, bb) in enumerate(ell):
    gc = T2s_of_lapse(lambda j, a=a, bb=bb: (Xv(a + j), V('N', 0, bb + j)))     # smoothing applied to Y(n)=xi(n+a)N(n+b) as a whole
    for mono, cf in gc.items():
        entries2.append((rid(('GC', mono)), nc0 + k_, -cf))
r0 = rid(('ELLW0',)); r1 = rid(('ELLW1',)); r2 = rid(('ELL1',))
for k_, (a, bb) in enumerate(ell):
    entries2.append((r0, nc0 + k_, F(1)))
    if a != 0: entries2.append((r1, nc0 + k_, F(a)))
    if bb != 0: entries2.append((r2, nc0 + k_, F(bb)))
b[r2] = F(1)
cols2 = cols + [(('ell', e), None) for e in ell]
print(f"R={R} ellR={RL} lapse in T2 = {W}: E2 alone + weak ell:", solve_sys(cols2, rows, entries2, b, match=False), flush=True)
