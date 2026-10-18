#!/usr/bin/env python3
"""B24 part 2a: exact letter-level taste rules (finite Fourier-polynomial identities, checked at random k), the
on-site commutant facts that limit them, and the resulting taste lattices of word classes (spectral detector).
  (i)   S^n(k + t) = S^n(k) Delta_n(t),  Delta_n(t) = diag(exp(i n t.f_c))      (n = +-1, +-2, +-4)
  (ii)  R_L(k + t) = D_t R_L(k) D_t^{-1},   D_t = diag(exp(-i t.f_c / 2))       (link hops preserve the corner position v + f_c/2)
  (iii) inside the 6-dim PSG-symmetric on-site algebra: commutant of {Z_x,Z_y,Z_z} = span{1, PP} (dim 2);
        commutant of {Z_i, Y} = scalars; L202 anticommutes with Y; no symmetric element connects antipodal corners (f -> -f);
        a symmetric element with a nonzero diagonal and connected support only admits scalar diagonal gauges.
  (iv)  word-class taste lattices (spectral; omega = 1 part Lambda_0), e.g. generic S^a G S^b G' -> bcc((2pi/|a+b|-type)),
        any word with R_L between S letters -> within 2piZ^3 + pi(1,1,1).
  (v)   gauge-chain construction: for W = S^a A S^b B with Delta_a(t) A = A Delta_a(t) (A plane letter, t in (pi/a)Z^3) and
        Delta_{a+b}(t) = 1, the diagonal V = Delta_a(t)... realises V W(k) V^-1 = W(k+t) exactly; checked on examples.
Prints PASS/FAIL, TOTAL."""
import sys, os, time, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b24lib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(2410); KS = rng.uniform(-np.pi, np.pi, (4, 3))
TS = [np.pi / 4 * rng.integers(-8, 8, 3) for _ in range(6)] + [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)]
Delta = lambda n, t: np.diag(np.exp(1j * n * fc @ t))
ok1 = all(np.allclose(Wb([L], (k + t)[None])[0], Wb([L], k[None])[0] @ Delta(PW[L], t)) for L in ('S', 'Si', 'S2', 'S2i', 'S4', 'S4i') for k in KS for t in TS)
check("(i) S^n(k+t) = S^n(k) diag(exp(i n t.f_c)) for n = +-1,+-2,+-4 and arbitrary t", ok1)
Dt = lambda t: np.diag(np.exp(-1j * fc @ t / 2))
ok2 = all(np.allclose(Wb(['R'], (k + t)[None])[0], Dt(t) @ Wb(['R'], k[None])[0] @ np.linalg.inv(Dt(t))) for k in KS for t in TS)
check("(ii) R_L(k+t) = D_t R_L(k) D_t^-1, D_t = diag(exp(-i t.f_c/2)), arbitrary real t (continuous 'position' symmetry of the link hopping)", ok2)
# (iii) commutants inside the symmetric on-site algebra
Bs = ONSITE_BASIS
def sub(conds):
    A = np.array([np.concatenate([np.concatenate([c(b).ravel().real, c(b).ravel().imag]) for c in conds]) for b in Bs]).T
    u, s, vh = np.linalg.svd(A); return len(Bs) - int(np.sum(s > 1e-9))
dZ = sub([lambda X, Z=Z: Z @ X - X @ Z for Z in Zs]); dZY = sub([lambda X, Z=Z: Z @ X - X @ Z for Z in Zs] + [lambda X: Ymat @ X - X @ Ymat])
check("(iii) symmetric on-site algebra has dim 6; its Z-commutant has dim 2 (= span{1, PP}); its {Z, Y}-commutant has dim 1",
      len(Bs) == 6 and dZ == 2 and dZY == 1 and all(np.allclose(Z @ PP, PP @ Z) for Z in Zs) and onsite_check(PP), f"{len(Bs)} {dZ} {dZY}")
anti = np.array([[np.all(fcI[a] == -fcI[b]) for b in range(12)] for a in range(12)])
check("(iii) no symmetric on-site element has an antipodal-corner (f_c -> -f_c) matrix element", all(np.abs(b[anti]).max() < 1e-12 for b in Bs))
check("(iii) L202 anticommutes with Y and commutes with the Z_i; the plane letters are exactly PP + e^{i phi}(1-PP) up to phase",
      np.allclose(Ymat @ PC['L202'], -PC['L202'] @ Ymat) and np.allclose(PC['L202'], PL(np.pi)) and np.allclose(PC['L101'], PL(np.pi / 2)) and np.allclose(PC['L303'], PL(3 * np.pi / 2)))
# generic letters admit only scalar diagonal gauges: G A G'^-1 = w A with G, G' diagonal  =>  G scalar
def diag_gauge_dim(A):
    # unknowns g (12), g' (12) complex, with w = 1 WLOG absorbed: g_c A_cd = A_cd g'_d  (linear) -> dimension of solution space
    rows = []
    for c in range(12):
        for d in range(12):
            if abs(A[c, d]) > 1e-12:
                r = np.zeros(24, complex); r[c] = A[c, d]; r[12 + d] = -A[c, d]; rows.append(r)
    M = np.array(rows); s = np.linalg.svd(M, compute_uv=False); return 24 - int(np.sum(s > 1e-9))
dims = collections.Counter(diag_gauge_dim(M) for n, M in PC.items())
check("(iii) diagonal gauge pairs (G, G') with G A G'^-1 = A: dimension 1 (scalars) for every Clifford H/L letter except the plane letters and identities",
      all(diag_gauge_dim(M) == 1 for n, M in PC.items() if n not in ('H00', 'L000', 'L101', 'L202', 'L303')), f"dims over PC: {dict(dims)}")
check("(iii) plane letters with phi != pi admit exactly the plane-constant diagonal gauges (dim 3); L202 (zero diagonal) admits dim 6",
      diag_gauge_dim(PC['L101']) == 3 and diag_gauge_dim(PC['L303']) == 3 and diag_gauge_dim(PC['L202']) == 6, f"{diag_gauge_dim(PC['L101'])} {diag_gauge_dim(PC['L202'])}")
# (v) explicit gauge-chain tastes: Z-type and Y-type for mixed powers
def taste_ok(w, t, V, om):
    return all(np.allclose(om * V @ Wb(w, k[None])[0] @ np.linalg.inv(V), Wb(w, (k + t)[None])[0]) for k in KS)
A = PC['H20']; G2 = PC['H13']; P2 = PC['L202']; P1 = PC['L101']
ex = []
# S^a P S^b G : gauge 1 -> Delta_a^-1 across S^a ... realised by V = 1 when Delta_a(t) commutes with P and Delta_{a+b}(t) = 1
for (a, b, P) in [(2, 2, P1), (1, 1, P2), (4, 4, P1), (2, -4, P1), (4, -2, P2), (1, 4, P2)]:
    sk = [{1: 'S', 2: 'S2', 4: 'S4', -2: 'S2i', -4: 'S4i', -1: 'Si'}[a], P, {1: 'S', 2: 'S2', 4: 'S4', -2: 'S2i', -4: 'S4i', -1: 'Si'}[b], G2]
    for i in range(3):
        t = np.pi / abs(a) * np.eye(3)[i]
        # word = S^a P S^b G ; W(k+t) = S^a D_a P S^b D_b G ; with V = Delta_a(t)^{-1}?  solve: take V = Delta_{a+b}(t) (= 1 if (a+b) t.f in 2pi Z)
        Da = Delta(a, t); Dab = Delta(a + b, t)
        if not np.allclose(Da @ P, P @ Da): continue
        if not np.allclose(Dab, Dab[0, 0] * np.eye(12)): continue
        ex.append((a, b, i, taste_ok(sk, t, np.eye(12), Dab[0, 0])))
check("(v) S^a P S^b G with Delta_a(t) in comm(P) and Delta_{a+b}(t) scalar: W(k+t) = Delta W(k) exactly, V = 1 (t = (pi/|a|) e_i)",
      len(ex) > 0 and all(e[3] for e in ex), f"{len(ex)} cases {ex}")
# Z-type taste (B20) with V = Z_i for S^a A S^a P (generic A) and t = (pi/a) e_i
okZ = all(taste_ok([nm, A, nm, P2], np.pi / a * np.eye(3)[i], Zs[i], 1.0) for a, nm in ((1, 'S'), (2, 'S2'), (4, 'S4')) for i in range(3))
check("(v) Z-type taste for every power: Z_i W(k) Z_i = W(k + (pi/a) e_i) for S^a A S^a L202 (A generic), a = 1, 2, 4", okZ)
okY = all(taste_ok([nm, A, nm, P2], np.pi / (2 * a) * np.ones(3), Ymat, -1.0) for a, nm in ((1, 'S'), (2, 'S2'), (4, 'S4')))
check("(v) Y-type taste: Y W(k) Y = -W(k + (pi/2a)(1,1,1)) for S^a A S^a L202, a = 1, 2, 4", okY)
# (iv) lattice census over random words of each class (spectral detector)
classes = collections.defaultdict(collections.Counter)
names_g = [n for n in PC if n not in ('H00', 'L000', 'L101', 'L202', 'L303')]
pw = ['S', 'Si', 'S2', 'S2i', 'S4', 'S4i']
for trial in range(120):
    m = rng.integers(2, 4); w = []; has_R = trial % 3 == 0; has_P = trial % 2 == 0
    for j in range(m):
        w.append(pw[rng.integers(6)])
        if has_R and j == 0: w.append('R')
        w.append(PC[names_g[rng.integers(len(names_g))]] if not (has_P and j == 0) else PLANE[list(PLANE)[rng.integers(3)]])
    if nS(w) == 0: continue
    Lt, L0 = lattices(w)
    classes[('R' if has_R else 'noR')][lat_name(L0)] += 1
print("  random-word census of spectral Lambda_0 types:", {k: dict(v) for k, v in classes.items()})
allnames = set(n for v in classes.values() for n in v)
check("(iv) every Lambda_0 met is sc or bcc (no fcc type) and every R_L word has Lambda_0 within 2piZ^3 + pi(1,1,1) (|Lambda_0/2piZ^3| <= 2)",
      all(not n.startswith('fcc') for n in allnames) and all(int(n.split('|')[1]) <= 2 for n in classes['R']))
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
