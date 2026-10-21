#!/usr/bin/env python3
"""Reviewer check of the 3<->3 cube move (ctqmc.cube_moves), L=2, fixed base state and fixed event times.
At V=0 every valid closed event sequence with the same nF has the same weight, so the cube move alone must leave
the UNIFORM distribution on its communicating class invariant.
Independent part (own code): lattice, circulation test, enumeration of the exact one-call transition kernel
  K(X->Y) = 1/(2 nF) * 1/N' * min(1, N'/N)   [N, N' = valid orderings of T, T' from the state before e1]
as described in NOTE §2.4, and checks that K is symmetric (=> detailed balance w.r.t. uniform).
Code under test: the block's cube_moves, called with ntry=1; its empirical transition frequencies are compared
with K row by row (chi^2), and its long-run occupancy with uniform.  usage: rs1_cube_move_db.py SEED NF NCALLS"""
import os, sys, itertools, math
import numpy as np
from scipy import stats
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))
import ctqmc  # code under test (cube_moves) and for the convention cross-check only

seed, NF, NCALLS = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
L = int(sys.argv[4]) if len(sys.argv) > 4 else 2
rng = np.random.default_rng(seed)
def vid(x, y, z): return ((x % L) * L + y % L) * L + z % L
nv = L**3; nl = 3 * nv
E3 = np.eye(3, dtype=int)
coords = list(itertools.product(range(L), repeat=3))
pl = np.zeros((3 * nv, 4), dtype=np.int64)
for (x, y, z) in coords:
    c = np.array([x, y, z]); v = vid(x, y, z)
    for o, (a, b) in enumerate(((0, 1), (1, 2), (0, 2))):
        pl[3*v+o] = [3*v+a, 3*vid(*(c+E3[a]))+b, 3*vid(*(c+E3[b]))+a, 3*v+b]
npl = 3 * nv
def circ(s, q):   # oriented circulation: + on first two links, - on last two
    t = s[pl[q, 0]] + s[pl[q, 1]] - s[pl[q, 2]] - s[pl[q, 3]]
    return abs(t) == 4
cubes = []
for (x, y, z) in coords:
    v = vid(x, y, z); c = np.array([x, y, z])
    cubes.append([3*v+0, 3*vid(*(c+E3[2]))+0, 3*v+1, 3*vid(*(c+E3[0]))+1, 3*v+2, 3*vid(*(c+E3[1]))+2])
cube_links = [sorted(set(pl[f].ravel().tolist()) for f in cf) for cf in cubes]
cube_links = [sorted(set(int(l) for f in cf for l in pl[f])) for cf in cubes]
lplaq = [[q for q in range(npl) if l in pl[q]] for l in range(nl)]
touch = [set(q for l in cl for q in lplaq[l]) for cl in cube_links]
pcube = [[ci for ci, cf in enumerate(cubes) if q in cf] for q in range(npl)]
assert all(len(x) == 2 for x in pcube)
# convention cross-check with the block (to pass arrays to the code under test)
lat = ctqmc.Lat(L)
assert np.array_equal(lat.plinks, pl)
cf_b, cl_b, pc_b = ctqmc.cube_tables(lat)
assert all(sorted(cf_b[i]) == sorted(cubes[i]) for i in range(nv))
assert all(sorted(pc_b[q]) == sorted(pcube[q]) for q in range(npl))

def gauss_ok(s):
    d = np.zeros(nv, dtype=int)
    for v in range(nv):
        for a in range(3):
            l = 3*v+a
            d[v] += s[l]; d[vid(*(np.array(coords[v]) + E3[a]))] -= s[l]
    return np.all(d == 0)

def valid_closed(s0, seq):
    s = s0.copy()
    for q in seq:
        if not circ(s, q): return False
        s[pl[q]] *= -1
    return np.array_equal(s, s0)

# ---- base state: own canonical-type state, randomised by flips of circulating plaquettes ----
s0 = np.zeros(nl, dtype=np.int64)
for (x, y, z) in coords:
    v = vid(x, y, z); s0[3*v] = (-1)**y; s0[3*v+1] = (-1)**x; s0[3*v+2] = (-1)**x
assert gauss_ok(s0)
# ---- random closed sequence of length NF containing a cube class ----
def make_seq():
    while True:
        k = (NF - 6) // 2
        # at L>2 bias the walk to stay near cube 0 so that windows are dense
        near = sorted(touch[0])
        s = s0.copy(); walk = []
        for _ in range(k):
            fl = [q for q in (near if L > 2 else range(npl)) if circ(s, q)]
            q = int(rng.choice(fl)); walk.append(q); s[pl[q]] *= -1
        ci = int(rng.integers(nv)) if L == 2 else int(rng.choice([c for c in range(nv) if set(cubes[c]) & set(near)]))
        perms = [p for p in itertools.permutations(cubes[ci]) if valid_closed(s, list(p))]
        if not perms: continue
        cubeseq = list(perms[int(rng.integers(len(perms)))])
        seq = walk + cubeseq + walk[::-1]
        assert valid_closed(s0, seq)
        return seq
seq0 = make_seq()
ft = np.sort(rng.random(NF))

NNP = [0, 0]   # (#proposals with N != N', #proposals)
def kernel(seq, acc_rule=True):
    """exact one-call kernel {Y: prob} (excluding staying) from configuration seq (time ordered)."""
    n = len(seq); out = {}
    s = s0.copy(); before = []
    for i in range(n):
        before.append(s.copy()); s[pl[seq[i]]] *= -1
    for i in range(n):
        for c in pcube[seq[i]]:
            win = [i]
            for j in range(i+1, n):
                if seq[j] in touch[c]:
                    win.append(j)
                    if len(win) == 3: break
            if len(win) < 3: continue
            T = [seq[w] for w in win]
            if len(set(T)) < 3 or not all(t in cubes[c] for t in T): continue
            Tp = [f for f in cubes[c] if f not in T]
            st = before[i]
            def nvalid(F):
                ok = []
                for p in itertools.permutations(F):
                    ss = st.copy(); good = True
                    for q in p:
                        if not circ(ss, q): good = False; break
                        ss[pl[q]] *= -1
                    if good: ok.append(p)
                return ok
            N = len(nvalid(T)); okp = nvalid(Tp); Np = len(okp)
            assert N >= 1
            if Np == 0: continue
            NNP[1] += 1; NNP[0] += (N != Np)
            for p in okp:
                y = list(seq)
                for w, q in zip(win, p): y[w] = q
                y = tuple(y)
                out[y] = out.get(y, 0.0) + (1.0 / (2*n)) * (1.0 / Np) * (min(1.0, Np / N) if acc_rule else 1.0)
    return out

# ---- BFS of the communicating class with the exact kernel ----
start = tuple(seq0); cls = {start: 0}; order = [start]; K = {}
h = 0
while h < len(order):
    x = order[h]; h += 1
    K[x] = kernel(list(x))
    for y in K[x]:
        assert valid_closed(s0, list(y))
        if y not in cls: cls[y] = len(order); order.append(y)
n = len(order)
npass = nfail = 0
def chk(name, ok, extra=""):
    global npass, nfail
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {extra}"); npass += bool(ok); nfail += (not ok)
print(f"[INFO] L={L} seed={seed} nF={NF} class size={n}")
asym = max(abs(K[x].get(y, 0.0) - K[y].get(x, 0.0)) for x in order for y in K[x])
chk("exact kernel symmetric K(X,Y)=K(Y,X) (detailed balance w.r.t. uniform)", asym < 1e-12, f"max|asym|={asym:.2e}")
nontriv = sum(len(K[x]) for x in order)
print(f"[INFO] proposals with N != N': {NNP[0]} of {NNP[1]}")
if L > 2:
    chk("test exercises the N'/N factor (some proposals have N != N')", NNP[0] > 0)
K0 = {x: kernel(list(x), acc_rule=False) for x in order}
asym0 = max(abs(K0[x].get(y, 0.0) - K0[y].get(x, 0.0)) for x in order for y in K0[x])
print(f"[INFO] control: same kernel with acceptance 1 instead of min(1,N'/N): max|asym|={asym0:.3e} (nonzero => the N'/N factor is needed)")
chk("class nontrivial (moves exist)", n >= 2, f"(transitions={nontriv})")
# ---- run the block's cube_moves, ntry=1 per call ----
ctqmc.nb_seed(seed + 99)
fp = np.array(seq0, dtype=np.int64); ftc = ft.copy(); s0c = s0.copy()
counts = {}; occ = np.zeros(n)
x = start
for it in range(NCALLS):
    ctqmc.cube_moves(s0c, ftc, fp, NF, pl, lat.lplaqs, cf_b, cl_b, pc_b, 1)
    y = tuple(int(v) for v in fp)
    if y not in cls:
        chk("block move left the exact class", False, str(y)); break
    counts.setdefault(x, {}); counts[x][y] = counts[x].get(y, 0) + 1
    occ[cls[y]] += 1
    x = y
assert np.array_equal(s0c, s0) and np.array_equal(ftc, ft)
# row-wise chi^2 of empirical transitions vs exact kernel (stay prob = 1 - sum)
chi2 = 0.0; dof = 0; worst = 0.0
for x0, row in counts.items():
    tot = sum(row.values())
    probs = dict(K[x0]); probs[x0] = 1.0 - sum(K[x0].values())
    for y, p in probs.items():
        e = tot * p
        o = row.get(y, 0)
        if e > 0:
            chi2 += (o - e)**2 / e; dof += 1
        elif o > 0:
            worst = max(worst, o)
    dof -= 1
chk("block never made a transition the exact kernel forbids", worst == 0)
pv = 1 - stats.chi2.cdf(chi2, dof)
chk("empirical one-call transition frequencies of the block code match the exact kernel (p>0.001)",
    pv > 1e-3, f"chi2={chi2:.1f} dof={dof} p={pv:.3f}")
# occupancy vs uniform (batch means over 20 blocks for the error)
expected = NCALLS / n
print(f"[INFO] occupancy: min={occ.min():.0f} max={occ.max():.0f} expected={expected:.0f}")
# exact stationary check: uniform is invariant for the block's (empirically equal) kernel, and the exact kernel's
# spectral gap gives the relaxation time; compare occupancy deviations with the exact asymptotic variance
P = np.zeros((n, n))
for x0 in order:
    for y, p in K[x0].items(): P[cls[x0], cls[y]] += p
    P[cls[x0], cls[x0]] += 1 - sum(K[x0].values())
ev = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
tau = 1 / (1 - ev[1]) if ev[1] < 1 else np.inf
pi_u = np.ones(n) / n
chk("uniform is exactly stationary for the exact kernel", np.abs(pi_u @ P - pi_u).max() < 1e-12)
chk("exact kernel irreducible on the class (second |eigenvalue| < 1)", ev[1] < 1 - 1e-12, f"tau_relax={tau:.1f} calls")
# total-variation distance of the empirical occupancy from uniform, vs. a crude bound from tau
tv = 0.5 * np.abs(occ / NCALLS - pi_u).sum()
print(f"[INFO] TV(empirical occupancy, uniform) = {tv:.3f}; NCALLS/tau = {NCALLS / tau:.0f}")
chk("empirical occupancy consistent with uniform (TV < 3*sqrt(n*tau/NCALLS))", tv < 3 * np.sqrt(n * tau / NCALLS))
print(f"TOTAL: PASS={npass} FAIL={nfail}")
