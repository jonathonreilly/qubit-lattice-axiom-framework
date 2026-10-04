"""A53 t2_check: brute-force control of the singlet-product factorization used in t2_prod.
Open 18-site region 3x3x2 (rule terms inside only), split into cluster A (8 sites) and B (10 sites); product state
psi_A x psi_B with RANDOM singlets (lowest singlets of random SU(2)-invariant rules on A and B).  Exact <H> on the
18-site S^z = 0 sector vs the factorized formula: <H_A> + <H_B> + 2+2 four-spin products (pairing inside the split:
C_A C_B; across: (1/3) C_A C_B); bilinears A-B and 3+1 / 2+1+1 splits dropped.
Negative control: S = 1, m = 0 states on A and B (formula must fail via the cross terms).  Usage: t2_check.py"""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(250)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a53lib import *
t0 = time.time(); rng = np.random.default_rng(7)
allr = [np.array(o) for o in itertools.product(range(3), range(3), range(2))]
A = allr[:8]; B = allr[8:]; reg = A + B; f = open_index(reg); nA, nB = 8, 10
S18 = Sector(18, flip=False)
def rand_states(n):
    Sn = Sector(n, flip=False)
    rp = {k: rng.normal() for k in itertools.combinations(range(n), 2)}
    rf = {k: rng.normal(size=3) for k in itertools.combinations(range(n), 4) if rng.random() < 0.3}
    w, U = np.linalg.eigh(dense_matrix(make_mv_gen(GenHam(rp, rf, n), Sn), Sn.D)); out = {}
    for q in range(Sn.D):
        C = paircorr(U[:, q], Sn); Sv = C.sum() / 4
        if abs(Sv) < 1e-8 and "singlet" not in out: out["singlet"] = (U[:, q], C)
        if abs(Sv - 2) < 1e-8 and "S=1,m=0" not in out: out["S=1,m=0"] = (U[:, q], C)
        if len(out) == 2: break
    return out, Sn
stA, SA = rand_states(nA); stB, SB = rand_states(nB)
cid = lambda s: 0 if s < nA else 1; loc = lambda s: s if s < nA else s - nA
for L, key in ((6, "B4_inner"), (8, "B4_r4")):
    ks, J, c4 = load_rule(L, key)
    pairs = bilinear_pairs(reg, f, ks, J); fours = four_sets(reg, f, c4)
    mv18 = make_mv_gen(GenHam(pairs, fours, 18), S18)
    HPA, HFA, HPB, HFB, inter, nsplit = {}, {}, {}, {}, [], {}
    for (i, j), Jv in pairs.items():
        if cid(i) == cid(j):
            D = HPA if cid(i) == 0 else HPB; k = (min(loc(i), loc(j)), max(loc(i), loc(j))); D[k] = D.get(k, 0.) + Jv
    for Sg, w in fours.items():
        c = [cid(s) for s in Sg]; l = [loc(s) for s in Sg]; sp = tuple(sorted([c.count(0), c.count(1)])); nsplit[sp] = nsplit.get(sp, 0) + 1
        if len(set(c)) == 1:
            D = HFA if c[0] == 0 else HFB
            o = sorted(range(4), key=lambda q: l[q]); k4 = tuple(l[q] for q in o); inv = {o[q]: q for q in range(4)}
            acc = D.setdefault(k4, np.zeros(3))
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                pr = tuple(sorted(tuple(sorted((inv[a], inv[b]))) for a, b in ((u, v), (x, y)))); acc[PAIRINGS.index(pr)] += w[pi]
        elif sp == (2, 2):
            for pi, ((u, v), (x, y)) in enumerate(PAIRINGS):
                if c[u] == c[v]:
                    (a, b), (cc, d) = ((u, v), (x, y)) if c[u] == 0 else ((x, y), (u, v)); fac = 1.
                else:
                    a = u if c[u] == 0 else v; b = v if a == u else u          # a in A, b in B
                    cc = x if c[x] == 0 else y; d = y if cc == x else x
                    (a, b, cc, d) = (a, cc, b, d); fac = 1. / 3.             # C_A[a, cc] C_B[b, d]
                inter.append((fac * w[pi], l[a], l[b], l[cc], l[d]))
    mvA = make_mv_gen(GenHam(HPA, HFA, nA), SA); mvB = make_mv_gen(GenHam(HPB, HFB, nB), SB)
    for nm in ("singlet", "S=1,m=0"):
        xa, CA = stA[nm]; xb, CB = stB[nm]
        va = np.zeros(1 << nA); va[SA.confs] = xa; vb = np.zeros(1 << nB); vb[SB.confs] = xb
        x = np.kron(vb, va)[S18.confs]; Eex = x @ mv18(x) / (x @ x)
        Ef = xa @ mvA(xa) / (xa @ xa) + xb @ mvB(xb) / (xb @ xb) + sum(m * CA[a, b] * CB[c, d] for m, a, b, c, d in inter)
        print(f"[L{L} {key}] {nm:8s}: exact <H> {Eex:+.12f}  factorized {Ef:+.12f}  diff {Eex - Ef:+.1e}   splits {nsplit}")
print(f"done [{time.time()-t0:.1f}s]")
