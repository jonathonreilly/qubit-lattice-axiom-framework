"""R17-1 s1 (written before running).
(a) Minimal-support Z_N-invariant hop patterns m (G m = 0 mod N, N0914 stencil N0914:95-97), N = 2,3,4,
    compactly supported in a B^3 box (every Gauss row the box touches is imposed), one slot fixed nonzero.
(b) For each minimal pattern, enumerate ALL realizable integer lifts delta (delta_s in {m_s, m_s - N}),
    i.e. the jumps n' - n a clock character Z^m produces on label states, and report:
    #lifts with G delta = 0 (integer-invariant), #lifts with M0 = 0, #lifts with M0 = M1 = 0, min |M0|.
(c) Check the moment identity D(G delta) = -M0(delta) on random patterns (positions: diagonal slot at x,
    face slot at x+(e_i+e_j)/2, Gauss row j at x+e_j/2).
Stencil code as in R16-11 s4 (re-derived against N0914:95-97 by hand before use).
"""
import numpy as np, itertools, sys
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import lil_matrix
TYPES = [(0,0),(1,1),(2,2),(0,1),(1,2),(0,2)]
E3 = np.eye(3, dtype=int)
def G_entries(x, t):
    i, j = TYPES[t]; x = np.array(x); out = []
    if i == j: out += [((tuple(x - E3[j]), j), 1), ((tuple(x), j), -1)]
    else: out += [((tuple(x), j), 1), ((tuple(x + E3[i]), j), -1), ((tuple(x), i), 1), ((tuple(x + E3[j]), i), -1)]
    return out
def pos(x, t):
    i, j = TYPES[t]; p = np.array(x, float)
    if i != j: p = p + 0.5*(E3[i] + E3[j])
    return p
def gpos(g):
    x, j = g; return np.array(x, float) + 0.5*E3[j]
def Gof(supp):  # supp: list of ((x,t), v)
    chk = {}
    for (x, t), v in supp:
        for g, c in G_entries(x, t): chk[g] = chk.get(g, 0) + c*v
    return {g: v for g, v in chk.items() if v != 0}
def M0(supp):
    M = np.zeros((3,3))
    for (x, t), v in supp:
        i, j = TYPES[t]; M[i,j] += v
        if i != j: M[j,i] += v
    return M
def M1(supp):
    M = np.zeros((3,3,3))
    for (x, t), v in supp:
        i, j = TYPES[t]; p = pos(x, t); M[i,j,:] += v*p
        if i != j: M[j,i,:] += v*p
    return M
def Dip(gam):
    D = np.zeros((3,3))
    for g, v in gam.items():
        D[:, g[1]] += v*gpos(g)
    return D
rng = np.random.default_rng(1)
# (c) moment identity check
mx = 0.0
for trial in range(200):
    supp = [((tuple(rng.integers(0,4,3)), int(rng.integers(0,6))), int(rng.integers(-3,4))) for _ in range(8)]
    d = Dip(Gof(supp)); mx = max(mx, np.abs(d + M0(supp)).max())
print("(c) max |D(G delta) + M0(delta)| over 200 random integer patterns = %.1e" % mx)

def minimal(N, B, fix, tl=120):
    slots = [(x, t) for x in itertools.product(range(B), repeat=3) for t in range(6)]
    sidx = {s: n for n, s in enumerate(slots)}
    gs = {}
    for s in slots:
        for g, v in G_entries(*s): gs.setdefault(g, len(gs))
    nS, nG = len(slots), len(gs)
    # variables: m (nS, 0..N-1 int), b (nS, binary support), t (nG, integer)
    nv = 2*nS + nG
    A = lil_matrix((nG, nv))
    for n, s in enumerate(slots):
        for g, v in G_entries(*s): A[gs[g], n] += v
    for g in range(nG): A[g, 2*nS + g] = -N
    cons = [LinearConstraint(A.tocsr(), 0, 0)]
    P = lil_matrix((nS, nv))   # m_s - (N-1) b_s <= 0
    for n in range(nS): P[n, n] = 1; P[n, nS + n] = -(N-1)
    cons.append(LinearConstraint(P.tocsr(), -np.inf, 0))
    lb = np.concatenate([np.zeros(nS), np.zeros(nS), -6*np.ones(nG)])
    ub = np.concatenate([(N-1)*np.ones(nS), np.ones(nS), 6*np.ones(nG)])
    lb[sidx[fix]] = 1
    c = np.concatenate([np.zeros(nS), np.ones(nS), np.zeros(nG)])
    res = milp(c=c, constraints=cons, integrality=np.ones(nv), bounds=Bounds(lb, ub),
               options={'time_limit': tl, 'disp': False})
    if res.x is None: return None, res.message
    m = np.round(res.x[:nS]).astype(int)
    supp = [(slots[n], int(m[n])) for n in range(nS) if m[n]]
    return supp, res.message

def lift_stats(N, supp):
    w = len(supp); nG0 = nM0 = nM01 = 0; minM0 = 1e9; best = None
    for choice in itertools.product([0,1], repeat=w):
        d = [((s), (v if c == 0 else v - N)) for (s, v), c in zip(supp, choice)]
        g = Gof(d); m0 = M0(d); m1 = M1(d)
        if not g: nG0 += 1
        if np.abs(m0).max() < 1e-12:
            nM0 += 1
            if np.abs(m1).max() < 1e-12: nM01 += 1
        nm = np.abs(m0).sum()
        if nm < minM0: minM0 = nm; best = d
    return 2**w, nG0, nM0, nM01, minM0, best

for N in [2, 3, 4]:
    for B, fix in [(4, ((1,1,1), 0)), (4, ((1,1,1), 3))]:
        supp, msg = minimal(N, B, fix)
        if supp is None: print("N=%d B=%d fix=%s: none (%s)" % (N, B, fix, msg)); continue
        modchk = all(v % N == 0 for v in Gof(supp).values())
        xs = np.array([x for (x, t), v in supp])
        print("\nN=%d box %d fixed slot %s: %s" % (N, B, fix, msg))
        print("  weight=%d  G m = 0 mod N: %s  extent=%s" % (len(supp), modchk, xs.max(0)-xs.min(0)+1))
        print("  pattern:", [(tuple(int(a) for a in x), TYPES[t], v) for (x, t), v in supp])
        print("  integer G m (as 0..N-1 lift):", {(tuple(int(a) for a in g[0]), g[1]): v for g, v in Gof(supp).items()})
        print("  M0(as-is lift) =", M0(supp).astype(int).tolist())
        nl, nG0, nM0, nM01, minM0, best = lift_stats(N, supp)
        print("  realizable lifts: %d ; integer-invariant (G delta=0): %d ; M0=0: %d ; M0=M1=0: %d ; min sum|M0| = %g"
              % (nl, nG0, nM0, nM01, minM0))
        print("  a lift attaining min |M0|:", [(TYPES[t], v) for (x, t), v in best], " M0 =", M0(best).astype(int).tolist())
        sys.stdout.flush()
