"""A55 c2: can a covariant function of corner records supply the staggered sign?
(a) single record: O-orbit of the 8 diagonals; commutant of the 24 SU(2) lifts on the corner qubit.
(b) two-sublattice backgrounds (f_even, f_odd): find an odd stabiliser element (R, a), sum(a) odd.
(c) all period-2 (coarse) backgrounds F: {0,1}^3 -> 8 diagonals, F(000) = (1,1,1) WLOG: which have no odd
    stabiliser element; stabiliser orders; transitivity on the even / odd classes.
Group acting on period-2 backgrounds: g = (R, a), R in O (24), a in Z2^3: (g.F)(R x + a) = R F(x)."""
import signal, sys, itertools, collections
signal.alarm(105)
import numpy as np
sys.path.insert(0, '/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A52')
from a52lib import ROT, BD, U

BDI = {f: i for i, f in enumerate(BD)}
rho = np.array([[BDI[tuple(int(c) for c in R @ np.array(f))] for f in BD] for R in ROT], dtype=np.uint8)  # rho[g][i]
# (a)
orb = {tuple(int(c) for c in R @ np.array(BD[0])) for R in ROT}
print("(a) O-orbit of (1,1,1): %d diagonals (f and -f in one orbit: %s)" % (len(orb), (-1, -1, -1) in orb))
rng = np.random.default_rng(1)
X = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
Xa = sum(u @ X @ u.conj().T for u in U) / 24
print("    group average of a random corner-qubit operator: off-identity part %.1e (commutant = multiples of 1)" % np.abs(Xa - np.trace(Xa) / 2 * np.eye(2)).max())

CL = list(itertools.product([0, 1], repeat=3))
CI = {c: i for i, c in enumerate(CL)}
EVEN = [i for i, c in enumerate(CL) if sum(c) % 2 == 0]
ODD = [i for i, c in enumerate(CL) if sum(c) % 2 == 1]
G = []                       # (g, a, sigma) with sigma[x] = class index of R x + a
for g, R in enumerate(ROT):
    for a in CL:
        sig = [CI[tuple(int(v) for v in (np.abs(R @ np.array(c)) + np.array(a)) % 2)] for c in CL]
        G.append((g, a, np.array(sig), sum(a) % 2))
print("group elements: %d (odd: %d)" % (len(G), sum(e[3] for e in G)))

def stab(F):
    out = []
    for (g, a, sig, par) in G:
        if all(F[sig[x]] == rho[g][F[x]] for x in range(8)):
            out.append((g, a, par))
    return out
# (b)
cnt = 0; ex = None
for fe in range(8):
    for fo in range(8):
        F = [fe if i in EVEN else fo for i in range(8)]
        st = stab(F)
        odd = [s for s in st if s[2]]
        cnt += bool(odd)
        if fe == 0 and fo == 1:
            ex = odd[0]
print("(b) two-sublattice backgrounds with an odd stabiliser element: %d/64; e.g. f_e=%s, f_o=%s: R=%s, a=%s" % (
    cnt, BD[0], BD[1], ROT[ex[0]].tolist(), ex[1]))

# (c) vectorised over all F with F(000) = 0
n = 8 ** 7
F = np.zeros((n, 8), dtype=np.uint8)
idx = np.arange(n, dtype=np.int64)
for col in range(1, 8):
    F[:, col] = (idx // 8 ** (7 - col)) % 8
del idx
has_odd = np.zeros(n, dtype=bool)
order = np.zeros(n, dtype=np.int16)
for (g, a, sig, par) in G:
    ok = np.all(rho[g][F] == F[:, sig], axis=1)
    if par:
        has_odd |= ok
    else:
        order += ok
surv = np.nonzero(~has_odd)[0]
print("(c) period-2 backgrounds with F(000)=(1,1,1): %d; with no odd stabiliser element: %d (%.1f%%)" % (n, len(surv), 100 * len(surv) / n))
oc = collections.Counter(order[surv].tolist())
print("    even-stabiliser orders among survivors: %s" % sorted(oc.items(), reverse=True))
best = order[surv].max()
bs = surv[order[surv] == best]
print("    largest stabiliser order without odd elements: %d, %d backgrounds" % (best, len(bs)))
# transitivity on even / odd classes, number of distinct records
def summarize(i):
    Fi = [int(v) for v in F[i]]
    st = stab(Fi)
    reach_e = set(); reach_o = set()
    for (g, a, par) in st:
        sig = [s for (gg, aa, s, p) in G if gg == g and aa == a][0]
        reach_e.add(int(sig[EVEN[0]])); reach_o.add(int(sig[ODD[0]]))
    return Fi, st, len(reach_e), len(reach_o), len(set(Fi))
seen = 0
trans = []
for i in surv[np.argsort(-order[surv], kind='stable')][:3000]:
    Fi, st, te, to, nd = summarize(i)
    if te == 4 and to == 4:
        trans.append((len(st), nd, Fi))
print("    among the 3000 most symmetric survivors: %d act transitively on both sublattices" % len(trans))
for (so, nd, Fi) in sorted(trans, key=lambda t: (-t[0], t[1]))[:6]:
    print("      stab %2d, %d distinct records: %s" % (so, nd, {CL[x]: BD[Fi[x]] for x in range(8)}))
np.save('survivors_top.npy', np.array([t[2] for t in sorted(trans, key=lambda t: (-t[0], t[1]))[:50]], dtype=np.int16))
print("done")
