#!/usr/bin/env python3
"""B25 part 1: transpose / antiunitary-type tastes -- letter rules, the index lemma, and which good pairs are reachable.
 (i)   exact transposition rules of the letters (finite identities checked at random k):
         S^n(k)^T = S^n(k);  R_L(k) = D_k R0 D_k^-1 with D_k = diag(e^{-i k.f_c/2}), R0 real symmetric, so R_L(k)^T = R_L(-k)
         and W(k)^T is again a palette word at the same k: reversed, constants transposed, R_L -> sigma S R_L S^-1 sigma;
         PH_j^T = PH_j (H_on real);  PLm_i^T = PLm_{3-i} (Lambda imaginary antisymmetric);
         L_abc^T = i^c L_{(b-c)(a-c)(-c)};  PL(phi)^T = e^{i phi} PL(-phi);  Y PP Y = 1 - PP, hence Y PL(phi) Y = PL(phi)^T.
 (ii)  letter gauge table: diagonal (h, h') with O = h X h'^-1 for X = O, O^T, and X = any other palette letter (or its
       transpose) [PC + plane letters]: only scalars for generic letters (transposable ones have O^T = +-O exactly);
       plane letters: C_P (U) and Y C_P (T); L202 larger.  Delta(m) = diag(e^{i m.f_c}) is scalar iff m in bcc(2pi),
       plane-constant (in C_P) iff m in pi Z^3, in Y C_P iff m in (pi/2)(1,1,1) + pi Z^3   (m on (pi/8)Z^3, exhaustive).
 (iii) INDEX LEMMA (abstract, proof in FINDINGS): let Lambda_ind(E) be the tastes t for which W(k+t) is k-independently
       similar to W(k) [U], W(k)^T [T] (both w = 1), or to w W(k)^-1 [I], w W(k)^* [K] with w = e^{2iE}.  Then
       [Lambda_ind(E) : Lambda_u] <= 4 and the point group acts trivially on Lambda_ind(E)/Lambda_u.
       Exhaustive check over all nested pairs of the 13 O-invariant lattices 2piZ^3 <= L <= (pi/8)Z^3 (+ bcc(pi/4)):
       no pair with index <= 4 and trivial O action is 'good' (C2pair mod Lambda_u within Tfix mod Lambda_sp, linear
       action around k*, (pi/32) grid).  Hence good pairs need spectral tastes WITHOUT a k-independent intertwiner.
Prints PASS/FAIL, TOTAL."""
import sys, os, time, collections, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from b25lib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(25); KS = rng.uniform(-np.pi, np.pi, (4, 3))
# ---------------- (i)
Dk = lambda k: np.diag(np.exp(-1j * fc @ k / 2))
R0 = Wb(['R'], np.zeros((1, 3)))[0]
ok = all(np.allclose(Wb([L], k[None])[0].T, Wb([L], k[None])[0]) for L in ('S', 'Si', 'S2', 'S2i', 'S4', 'S4i') for k in KS)
ok &= all(np.allclose(Wb(['R'], k[None])[0], Dk(k) @ R0 @ np.linalg.inv(Dk(k))) for k in KS) and np.allclose(R0, R0.T) and np.abs(R0.imag).max() < 1e-14
ok &= all(np.allclose(Wb(['R'], k[None])[0].T, Wb(['R'], -k[None])[0]) for k in KS)
ok &= all(np.allclose(np.diag(Wb(['S'], k[None])[0]), sig * np.diag(Dk(k)) ** -2) for k in KS)
check("(i) S^n(k)^T = S^n(k); R_L(k) = D_k R0 D_k^-1 (R0 real symmetric) so R_L(k)^T = R_L(-k); S(k) = sigma D_k^-2", ok)
w_ = ['S2', PC['L123'], 'R', PC['H31'], 'Si', PLANE['L101']]; Sg = np.diag(sig).astype(complex)
wt = []
for L in w_[::-1]: wt += ([Sg, 'S', 'R', 'Si', Sg] if isinstance(L, str) and L == 'R' else [L if isinstance(L, str) else L.T])
ok = all(np.allclose(Wb(w_, k[None])[0].T, Wb(wt, k[None])[0]) for k in KS)
ok &= all(np.allclose(Wb(['R'], k[None])[0].T, Wb([Sg, 'S', 'R', 'Si', Sg], k[None])[0]) for k in KS)
check("(i) W(k)^T = reversed word with transposed on-site letters at the SAME k, where R_L(k)^T = sigma S R_L S^-1 sigma (R_L changes the S-power pattern)", ok)
ok = all(np.allclose(P.T, P) for P in PH) and all(np.allclose(PLm[i].T, PLm[3 - i]) for i in range(4))
I4 = [1, 1j, -1, -1j]
ok2 = all(np.allclose(PC[f"L{a}{b}{c}"].T, I4[c] * PC[f"L{(b - c) % 4}{(a - c) % 4}{(-c) % 4}"]) for a in range(4) for b in range(4) for c in range(4))
ok3 = all(np.allclose(PL(ph).T, np.exp(1j * ph) * PL(-ph)) and np.allclose(Ymat @ PL(ph) @ Ymat, PL(ph).T) for ph in np.pi / 6 * np.arange(12))
check("(i) PH^T = PH; PLm_i^T = PLm_{3-i}; L_abc^T = i^c L_{(b-c)(a-c)(-c)} (all 64); PL(phi)^T = e^{i phi}PL(-phi) = Y PL(phi) Y",
      ok and ok2 and ok3 and np.allclose(Ymat @ PP @ Ymat, np.eye(12) - PP))
# ---------------- (ii) letter gauge table
def gauge(O, X):
    rows = []
    for c in range(12):
        for d in range(12):
            if abs(O[c, d]) > 1e-12 or abs(X[c, d]) > 1e-12:
                r = np.zeros(24, complex); r[c] = X[c, d]; r[12 + d] = -O[c, d]; rows.append(r)
    u, s, vh = np.linalg.svd(np.array(rows)); return vh[np.sum(s > 1e-9):].conj()
def invertible(null):
    if len(null) == 0: return False
    v = rng.normal(size=len(null)) @ null + 1j * rng.normal(size=len(null)) @ null; return np.abs(v).min() > 1e-8
LET = {**PC, **PLANE, **PLANE6}
SPECIAL = {'H00', 'L000'} | set(PLANE) | set(PLANE6) | {'L202'}
gen_scalar = True; transp = collections.Counter(); cross = collections.Counter()
for n, O in LET.items():
    gU, gT = gauge(O, O), gauge(O, O.T)
    if n not in SPECIAL:
        gen_scalar &= (len(gU) == 1)
        if invertible(gT):
            v = gT[0]; h, hp = v[:12] / v[0], v[12:] / v[0]
            s_ = 'O^T=+O' if np.allclose(O.T, O) else ('O^T=-O' if np.allclose(O.T, -O) else 'other')
            transp[s_] += 1
            gen_scalar &= np.allclose(h, 1) and np.allclose(hp, hp[0]) and s_ != 'other'
        else: transp['none'] += 1
check("(ii) generic palette letters (PC minus identities/plane/L202) have only scalar gauges; transposable ones satisfy O^T = +-O exactly (trivial transpose gauge)",
      gen_scalar, f"{dict(transp)}")
okP6 = True; c6 = collections.Counter()
for n, O in P6.items():
    if n in ('H0.0', 'L0.0.0'): continue
    gU, gT = gauge(O, O), gauge(O, O.T)
    if invertible(gT) and len(gU) == 1: okP6 &= np.allclose(O.T, O) or np.allclose(O.T, -O)
    c6[(len(gU), bool(invertible(gT)))] += 1
check("(ii) same for the 1872 pi/6 letters: gauge dims in {1 (generic), 3 (plane), 6}; every transposable generic one has O^T = +-O",
      okP6 and set(d for d, _ in c6) <= {1, 3, 6}, f"{dict(c6)}")
R0g = gauge(R0, R0)
check("(ii) R0 (R_L at k=0) is block-diagonal over the three coordinate planes (4-cycles), gauge dim 6",
      len(R0g) == 6 and all(abs(R0[a, b]) < 1e-12 for a in range(12) for b in range(12) if not any(fcI[a, i] == 0 and fcI[b, i] == 0 for i in range(3))))
# cross relations between distinct letters (and transposes) of PC + plane
names = list(PC) + list(PLANE)
for a in names:
    for b in names:
        for tr_ in (0, 1):
            if a == b and not tr_: continue
            X = LET[b].T if tr_ else LET[b]
            if invertible(gauge(LET[a], X)):
                same = np.allclose(LET[a], X * (LET[a][np.unravel_index(np.abs(X).argmax(), X.shape)] / X[np.unravel_index(np.abs(X).argmax(), X.shape)]))
                cross['proportional' if same else ('plane' if a in SPECIAL and b in SPECIAL else 'OTHER')] += 1
check("(ii) every diagonal-gauge relation O = h X h'^-1 between distinct PC/plane letters (X = O' or O'^T) is a proportionality or a plane/L202 relation",
      cross['OTHER'] == 0, f"{dict(cross)}")
def in_space(D, basis):
    A = np.array([b.ravel() for b in basis]).T; x = np.linalg.lstsq(A, D.ravel(), rcond=None)[0]; return np.allclose(A @ x, D.ravel())
Cp = [np.diag((fcI[:, i] == 0).astype(float)) for i in range(3)]          # plane-constant diagonals
cls = collections.Counter(); okD = True
for m in itertools.product(range(16), repeat=3):
    mm = np.array(m) * np.pi / 8; D = np.diag(np.exp(1j * fc @ mm)); mi = np.array(m)
    sc_ = np.allclose(D, D[0, 0] * np.eye(12)); inC = in_space(D, Cp); inYC = in_space(Ymat @ D, Cp)
    exp_sc = all(x % 16 == 0 for x in mi) or all(x % 16 == 8 for x in mi)
    exp_C = all(x % 8 == 0 for x in mi); exp_YC = all(x % 8 == 4 for x in mi)
    okD &= (sc_ == exp_sc) and (inC == exp_C) and (inYC == exp_YC); cls[(sc_, inC, inYC)] += 1
check("(ii) Delta(m) scalar iff m in bcc(2pi); in C_P iff m in piZ^3; in Y C_P iff m in (pi/2)(1,1,1)+piZ^3 (all 4096 m in (pi/8)Z^3)", okD, f"{dict(cls)}")
ok = all(np.allclose(Ymat @ PLANE[p] @ Ymat, PLANE[p].T) for p in PLANE) and np.allclose(Ymat @ PC['L202'] @ Ymat, -PC['L202'])
check("(ii) plane letters: (Y, Y) is a transpose gauge (Y P Y = P^T); L202: Y L202 Y = -L202 (unitary, w = -1)", ok)
# ---------------- (iii) index lemma vs good pairs
ROT = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), int)
        for i in range(3): M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1: ROT.append(M)
tr = [int(np.trace(R)) for R in ROT]
isT = np.array([t in (3, 0) or (t == -1 and np.all(np.abs(np.diag(R)) == 1)) for R, t in zip(ROT, tr)])
C2 = [i for i, t in enumerate(tr) if t == -1]
C2P = [(i, j) for i in C2 for j in C2 if i < j and np.array_equal(ROT[i] @ ROT[j], ROT[j] @ ROT[i])]
N = 64                                                                    # (pi/32) grid, mod 64
def lat64(nm):
    return {tuple(2 * c for c in v) for v in LATS[nm]}
grid = np.array(list(itertools.product(range(N), repeat=3)))
def fixmat(L):
    memb = np.zeros((N,) * 3, bool)
    for v in L: memb[v] = True
    return np.array([memb[tuple(((grid @ R.T - grid) % N).T)] for R in ROT])
L64 = {nm: lat64(nm) for nm in LATS}; FX = {nm: fixmat(L) for nm, L in L64.items()}
def good(nu, ns):
    p = np.zeros(len(grid), bool)
    for i, j in C2P: p |= FX[nu][i] & FX[nu][j]
    return int((p & ~np.all(FX[ns][isT], axis=0)).sum()) == 0
def o_trivial(nu, ns):
    Lu = L64[nu]
    return all(tuple(int(x) % N for x in (R @ np.array(t) - np.array(t))) in Lu for t in L64[ns] for R in ROT)
rows = []
for nu in LATS:
    for ns in LATS:
        if nu == ns or not LATS[nu] <= LATS[ns]: continue
        idx = len(LATS[ns]) // len(LATS[nu]); rows.append((nu, ns, idx, o_trivial(nu, ns), good(nu, ns)))
ng = sum(r[4] for r in rows); adm = [r for r in rows if r[2] <= 4 and r[3]]
print(f"   strictly nested pairs: {len(rows)}; good: {ng}; admissible (index <= 4, O-trivial quotient): {[(r[0], r[1], r[2]) for r in adm]}")
print("   good pairs (index, O-trivial):", [(r[0], r[1], r[2], r[3]) for r in rows if r[4]])
sub = [r for r in rows if all(x not in ('sc(2)', 'fcc(2)', 'bcc(4)') for x in r[:2])]
check("(iii) reproduces B24_check chk4 on the 10 lattices down to pi/4: 42 strictly nested pairs, 29 good", len(sub) == 42 and sum(r[4] for r in sub) == 29, f"{len(sub)} {sum(r[4] for r in sub)}")
check("(iii) INDEX LEMMA consequence: no admissible pair (index <= 4 with O acting trivially on Lambda_sp/Lambda_u) is good",
      all(not r[4] for r in adm) and len(adm) > 0, f"{len(adm)} admissible, all bad")
exp_adm = {(f"sc({a})", f"bcc({a})") for a in (32, 16, 8, 4)} | {(f"fcc({b})", f"sc({b})") for b in (16, 8, 4, 2)}
check("(iii) the admissible pairs are exactly (sc(a), bcc(a)) and (fcc(b), sc(b)) (the maximal O-trivial extensions; scale-covariant)",
      {(r[0], r[1]) for r in adm} == exp_adm)
check("(iii) every good pair has index >= 4 and a NON-trivial O action on the quotient", all(r[2] >= 4 and not r[3] for r in rows if r[4]))
# numerical illustration of the lemma's key step on the B24_check example: the (pi/4)(1,1,1) taste is T-type, its double is U-type
w = build24(('S2', 'p', 'S2', 'o'), ('L101', 'H13'))
d = {k: inter_dim(w, (4, 4, 4), k) for k in 'UT'}; d2 = {k: inter_dim(w, (8, 8, 8), k) for k in 'UT'}
check("(iii) example S2.L101.S2.H13: t = (pi/4)(1,1,1) has a T intertwiner and no U one; 2t = (pi/2)(1,1,1) has a U one",
      d['T'] > 0 and d['U'] == 0 and d2['U'] > 0, f"{d} {d2}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
