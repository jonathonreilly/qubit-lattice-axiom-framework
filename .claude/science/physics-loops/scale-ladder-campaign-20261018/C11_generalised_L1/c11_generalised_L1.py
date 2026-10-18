"""C11: generalised L1 lemma for the 12-mode corner model at +-k*, k* = (pi/2)(1,-1,1).

Lemma (see FINDINGS.md).  For a translation-invariant unitary letter U, O-covariant up to chi in {A1, A2},
and a doublet D_b (b = +-1: D+ = E1/2-type block, D- = E5/2-type block of the 12-mode rep at k*):
    U(k*) D_b = D_{chi b},   P_b U^dag d_i U P_b = i v_U^{(b)} tau^{(b)}_i,  v real,
with tau^{(b)} the unique Hermitian T1 triple on D_b normalised to tau_i tau_j = delta_ij + i eps_ijk tau_k.
For W = U_1...U_m with prod chi_j = +1 and D_a an isolated 2-fold level of W(k*):
    P_a W^dag d_i W P_a = i (sum_j v_j^{(b_j)}) tau^{(a)}_i,  b_j = a * prod_{l>j} chi_l,
so the cone is untilted and isotropic with speed |sum_j v_j^{(b_j)}|.

Model code: ../B26_check/mymodel.py (independent from-scratch build), imported read-only.
Prediction uses letter-level derivatives only; the "actual" side differentiates the whole word numerically
(no product rule) and also diagonalises W(k*+delta q) directly.
"""
import os, sys, itertools, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B26_check'))
from mymodel import *          # noqa: F401,F403  (numpy as np, PROPER, Sk, bloch, RL, RTX, A0m, DP, DM, ONB, ...)
from scipy.linalg import expm

NPASS = 0; NFAIL = 0
def report(ok, msg):
    global NPASS, NFAIL
    ok = bool(ok); NPASS += ok; NFAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {msg}", flush=True)

rng = np.random.default_rng(20261018)
KST = np.array([1, -1, 1]) * np.pi / 2
KPTS = {'+k*': KST, '-k*': -KST}
DOUB = {+1: DP, -1: DM}
EPS = np.zeros((3, 3, 3))
for i, j, k in itertools.permutations(range(3)):
    EPS[i, j, k] = np.linalg.det(np.eye(3)[[i, j, k]])

# =========================================================================================== 1. group at k*
print("== 1. little group, projective representation, irreps")
ok = True
for kname, k0 in KPTS.items():
    for g in PROPER:
        ok &= np.allclose(wrap(g['M'].T @ k0 + np.pi * g['lam'] - k0), 0, atol=1e-12)
report(ok, "all 24 proper rotations fix +k* and -k* (R^T k + pi*lam = k mod 2pi): little group = O")

def find_rot(M):
    for i, g in enumerate(PROPER):
        if np.array_equal(g['M'], M): return i
ok = True; signs = set()
for g in PROPER:
    for h in PROPER:
        p = g['U'] @ h['U']; q = PROPER[find_rot(g['M'] @ h['M'])]['U']
        s = [s for s in (1, -1) if np.allclose(p, s * q)]
        ok &= len(s) == 1; signs |= set(s)
report(ok and signs == {1, -1}, "rho(g)=U_R (12x12, real orthogonal) composes up to a sign, with both signs occurring: "
       "a genuinely projective rep; {+-U_R} is a 48-element group")
# which double cover?  O x Z2 has 19 involutions, GL(2,3) has 13, 2O has 1.
def ninv(els): return sum(1 for X in els if np.allclose(X @ X, np.eye(12)) and not np.allclose(X, np.eye(12)))
inv_a = ninv([s * g['U'] for g in PROPER for s in (1, -1)])
inv_b = ninv([s * (1 if g['chi'] == 1 else 1j) * g['U'] for g in PROPER for s in (1, -1)])
report(inv_a == 13 and inv_b == 1,
       f"{{+-U_R}} has {inv_a} involutions: it is GL(2,3), the non-split double cover of O isoclinic to 2O (O x Z2 would have 19); "
       f"relifting odd elements g -> i g gives a group with {inv_b} involution, i.e. 2O. Relifting rescales odd-element "
       f"operators by i, which changes no conjugation, no Schur statement and no chi_A2 relation, so the 2O irrep names apply")

ok = all(np.allclose(g['U'] @ D, D @ (D.conj().T @ g['U'] @ D), atol=1e-12) for g in PROPER for D in (DP, DM))
report(ok, "D+ and D- (the B26-build doublets {H_on=2, Lambda=-+2sqrt2}) are rho-invariant")
chiP = np.array([np.trace(DP.conj().T @ g['U'] @ DP) for g in PROPER])
chiM = np.array([np.trace(DM.conj().T @ g['U'] @ DM) for g in PROPER])
chiA2 = np.array([g['chi'] for g in PROPER])
nP = np.mean(np.abs(chiP) ** 2); nM = np.mean(np.abs(chiM) ** 2); ovl = np.mean(np.conj(chiP) * chiM)
report(abs(nP - 1) < 1e-12 and abs(nM - 1) < 1e-12 and abs(ovl) < 1e-12,
       f"D+ and D- irreducible and inequivalent (<chi,chi> = {nP:.3f}, {nM:.3f}; <chi+,chi-> = {abs(ovl):.1e})")
report(np.allclose(chiM, chiA2 * chiP, atol=1e-12),
       "A2 (x) D+ = D-: chi_{D-}(g) = chi_A2(g) chi_{D+}(g) for all 24 lifts (lift-sign independent), i.e. A2 (x) E1/2 = E5/2")
PG = np.eye(12) - DP @ DP.conj().T - DM @ DM.conj().T
chiG = np.array([np.trace(PG @ g['U']) for g in PROPER]); nG = np.mean(np.abs(chiG) ** 2)
comm = []
for g in PROPER: comm.append(np.kron(g['U'], g['U']) - np.eye(144))
sv = np.linalg.svd(np.vstack(comm), compute_uv=False); dcomm = int(np.sum(sv < 1e-9))
oG = max(abs(np.mean(np.conj(chiG) * chiP)), abs(np.mean(np.conj(chiG) * chiM)))
report(abs(nG - 4) < 1e-10 and dcomm == 6 and oG < 1e-12,
       f"8-dim complement: <chi,chi> = {nG:.3f}, no D+ or D- content (overlap {oG:.1e}), full commutant dim = {dcomm} = 1+1+4; "
       f"with projective irreps of dims 2,2,4 only, complement = 2 x G3/2, so D+ and D- have multiplicity 1")

# =========================================================================================== 2. T1 triple
print("== 2. Wigner-Eckart: T1 triples on End(D)")
def t1_triples(Din, Dout, chi_letter=1):
    """Triples (Y_1,Y_2,Y_3), Y_i: D_in -> D_out, with rho_out (sum_j R_ij Y_j) rho_in^-1 = chi(g) Y_i  for all g.
    Returns an orthonormal basis of the solution space (each a 3x2x2 complex array)."""
    rows = []
    for g in PROPER:
        ro = Dout.conj().T @ g['U'] @ Dout; ri = Din.conj().T @ g['U'] @ Din; c = g['chi'] if chi_letter == -1 else 1
        # linear map on vec(Y) (Y: 3x2x2) -> 3x2x2
        L = np.zeros((12, 12), complex)
        for i in range(3):
            for j in range(3):
                # term: R_ij * ro Y_j ri^-1 ; vec(A Y B) = kron(A, B^T) vec(Y) (row-major)
                L[4 * i:4 * i + 4, 4 * j:4 * j + 4] += g['M'][i, j] * np.kron(ro, np.linalg.inv(ri).T)
            L[4 * i:4 * i + 4, 4 * i:4 * i + 4] -= c * np.eye(4)
        rows.append(L)
    _, s, Vh = np.linalg.svd(np.vstack(rows))
    null = Vh[np.sum(s > 1e-9):].conj()
    return [v.reshape(3, 2, 2) for v in null]
TAU = {}
for b, D in DOUB.items():
    sols = t1_triples(D, D)
    Y = sols[0]
    ph = np.trace(Y[0] @ Y[0]) / 2; Y = Y / np.sqrt(ph)       # Y_x^2 = 1 (Y_x^2 is a multiple of 1)
    if not np.allclose(Y[0], Y[0].conj().T): Y = Y * 1j
    if not np.allclose(Y[0] @ Y[1], 1j * Y[2]): Y = -Y
    herm = all(np.allclose(Y[i], Y[i].conj().T) for i in range(3))
    alg = all(np.allclose(Y[i] @ Y[j], (i == j) * np.eye(2) + 1j * sum(EPS[i, j, k] * Y[k] for k in range(3))) for i in range(3) for j in range(3))
    tr = max(abs(np.trace(Y[i])) for i in range(3))
    report(len(sols) == 1 and herm and alg and tr < 1e-12,
           f"D{'+' if b > 0 else '-'}: the T1-triple space in End(D) is {len(sols)}-dim; normalised it is a Hermitian, traceless "
           f"Pauli triple tau_i tau_j = delta_ij + i eps_ijk tau_k (A1/tilt part forced to 0)")
    TAU[b] = Y
for (a, b) in ((+1, -1),):
    n1 = len(t1_triples(DOUB[a], DOUB[b], 1)); n2 = len(t1_triples(DOUB[a], DOUB[b], -1))
    report(n1 == 0 and n2 == 1, f"Hom(D+,D-) contains no T1 (dim {n1}) [so no first-order D+<->D- mixing for an A1 word], "
           f"and one T1(x)A2 = T2 (dim {n2})")
    n3 = len(t1_triples(DOUB[a], DOUB[a], -1))
    report(n3 == 0, f"End(D+) contains no T2 (dim {n3}) [consistent: an A2 letter's derivative leaves D+ entirely]")

# =========================================================================================== 3. letters
print("== 3. letters: covariance, scalar/swap action, v values")
def sym_avg(X):
    acc = {}
    for g in PROPER:
        for a, B in conjG(g, X).items(): acc[a] = acc.get(a, 0) + B / 24
    return acc
def rand_H(scale):
    X = {}
    for a in itertools.product((-2, -1, 0, 1, 2), repeat=3):
        if sum(abs(x) for x in a) <= 2 and rng.random() < 0.5:
            X[a] = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12))
    H = sym_avg(X); Hh = {}
    for a, B in H.items(): Hh[a] = Hh.get(a, 0) + B / 2
    for a, B in dag(H).items(): Hh[a] = Hh.get(a, 0) + B / 2
    nrm = np.linalg.norm(bloch(Hh, rng.uniform(-np.pi, np.pi, 3)), 2)
    return {a: B * scale / nrm for a, B in Hh.items()}
class Letter:
    def __init__(self, name, chi, f): self.name, self.chi, self.f = name, chi, f
def L_S(p): return Letter(f"S^{p}", 1, lambda k, p=p: Sk(k, p))
def L_A(p): return Letter(f"A0S^{p}", -1, lambda k, p=p: A0m @ Sk(k, p))
L_RL = Letter("R_L", 1, lambda k: bloch(RL, k))
L_RT = Letter("Rt", 1, lambda k: bloch(RTX, k))
def L_expRL(th, nm): return Letter(nm, 1, lambda k, th=th: expm(1j * th * bloch(RL, k)))
def L_onsite():
    V = rand_onsite_unitary(rng); return Letter("onsite", 1, lambda k, V=V: V)
def L_expH(scale=None, a2=False):
    s = rng.uniform(0.3, 3.0) if scale is None else scale; H = rand_H(s)
    if a2: return Letter("A0exp(iH)", -1, lambda k, H=H: A0m @ expm(1j * bloch(H, k)))
    return Letter("exp(iH)", 1, lambda k, H=H: expm(1j * bloch(H, k)))

def covariant(L, ntest=2):
    for _ in range(ntest):
        k = rng.uniform(-np.pi, np.pi, 3); Uk = L.f(k)
        for g in PROPER:
            c = g['chi'] if L.chi == -1 else 1
            if not np.allclose(g['U'] @ L.f(g['M'].T @ k + np.pi * g['lam']) @ g['U'].T, c * Uk, atol=1e-9): return False
    return True
H_FD = 1e-5
def dfd(f, k, h=H_FD):
    out = []
    for i in range(3):
        dk = np.zeros(3); dk[i] = h; out.append((f(k + dk) - f(k - dk)) / (2 * h))
    return out
def letter_v(L, k0, b):
    """Returns (v, residual of P U^dag dU P = i v tau fit, imag part of v, maps_ok) for input doublet D_b."""
    D = DOUB[b]; Do = DOUB[b * L.chi]; U = L.f(k0)
    maps_ok = np.allclose(U @ D, Do @ (Do.conj().T @ U @ D), atol=1e-9)
    if L.chi == 1:
        X = D.conj().T @ U @ D; maps_ok &= np.allclose(X, X[0, 0] * np.eye(2), atol=1e-9)
    dU = dfd(L.f, k0)
    M = [D.conj().T @ U.conj().T @ dU[i] @ D for i in range(3)]
    vc = sum(np.trace(TAU[b][i] @ M[i]) for i in range(3)) / (6j)
    res = max(np.abs(M[i] - 1j * vc.real * TAU[b][i]).max() for i in range(3))
    return vc.real, res, abs(vc.imag), maps_ok

named = [L_S(1), L_S(2), L_S(-1), L_S(-2), L_RL, L_RT,
         Letter("E+", 1, lambda k: expm(1j * np.pi / 4 * bloch(RL, k))), Letter("E-", 1, lambda k: expm(-1j * np.pi / 4 * bloch(RL, k)))]
named += [L_expRL(m * np.pi / 6, f"exp(i{m}pi/6 R_L)") for m in (1, 2, 3, 5)] + [L_expRL(0.7317, "exp(0.7317i R_L)")]
named += [L_onsite() for _ in range(3)] + [L_A(p) for p in (-2, -1, 0, 1, 2)]
named += [L_expH() for _ in range(6)] + [L_expH(a2=True) for _ in range(2)]
VT = {}
ok_cov = True; ok_fit = True; worst = 0; tab = []
for L in named:
    cv = covariant(L); ok_cov &= cv
    row = [L.name]
    for kname, k0 in KPTS.items():
        for b in (+1, -1):
            v, res, im, mok = letter_v(L, k0, b); VT[(id(L), kname, b)] = v
            ok_fit &= mok and res < 1e-7 and im < 1e-7; worst = max(worst, res, im)
            row.append(v)
    tab.append(row)
report(ok_cov, f"all {len(named)} test letters are O-covariant with their declared character (24 rotations, random k)")
report(ok_fit, f"each letter preserves (A1) / swaps (A2) D+-, A1 letters are scalars there, and P U^dag dU P = i v tau "
       f"with v real, at +-k* (worst residual {worst:.1e})")
print("   letter                v(D+,+k*)   v(D-,+k*)   v(D+,-k*)   v(D-,-k*)")
for r in tab: print("   %-20s" % r[0] + "".join("%12.6f" % x for x in r[1:]))
r23 = np.sqrt(2) / 3
vS = tab[0][1:]
report(np.allclose(vS, [r23, -r23, r23, -r23], atol=1e-8),
       "v_S = +sqrt2/3 on D+ and -sqrt2/3 on D- at both +k* and -k* (tau orientation: tau_x tau_y = +i tau_z) [expected from B20 L1]")
okadd = all(np.allclose(tab[i][1:], p * np.array(vS), atol=1e-8) for i, p in ((1, 2), (2, -1), (3, -2)))
report(okadd, "v_{S^p} = p v_S for p = 2, -1, -2 (letter-level additivity)")
zero = [r for r in tab if r[0] in ("R_L", "Rt", "E+", "E-", "onsite") or r[0].startswith("exp(") and "R_L" in r[0]]
report(all(np.allclose(r[1:], 0, atol=1e-8) for r in zero),
       f"v = 0 for R_L, Rt, E+-, exp(i theta R_L) (theta = pi/6,pi/3,pi/2,5pi/6,0.7317) and random symmetric on-site letters ({len(zero)} letters)")
okA = all(np.allclose(tab[i][1:], p * np.array(vS), atol=1e-8) for i, p in zip(range(16, 21), (-2, -1, 0, 1, 2)))
report(okA, "A2 letters A0 S^a: v^(b) (input doublet b) = a * v_S^(b), i.e. A0 contributes nothing but the label swap")
gen = [r for r in tab if "exp(iH)" in r[0]]
print("   generic exp(iH): v(D+,+k*) + v(D-,+k*) =", [round(r[1] + r[2], 4) for r in gen], "(nonzero: no +- antisymmetry in general)")

# =========================================================================================== 4. random words
print("== 4. random words: predicted |sum v| vs actual degenerate perturbation theory")
def rand_letter_pool():
    r = rng.random()
    if r < 0.18: return L_S(int(rng.choice([1, 2, -1, -2])))
    if r < 0.28: return L_RL
    if r < 0.36: return L_RT
    if r < 0.46: return L_onsite()
    if r < 0.54: return Letter("E+", 1, lambda k: expm(1j * np.pi / 4 * bloch(RL, k))) if rng.random() < .5 else Letter("E-", 1, lambda k: expm(-1j * np.pi / 4 * bloch(RL, k)))
    if r < 0.60: m = int(rng.integers(1, 6)); return L_expRL(m * np.pi / 6, f"exp(i{m}pi/6 R_L)")
    if r < 0.80: return L_expH()
    if r < 0.92: return L_A(int(rng.integers(-2, 3)))
    return L_expH(a2=True)
def rand_word(min_generic=0):
    while True:
        m = int(rng.integers(2, 7)); w = [rand_letter_pool() for _ in range(m)]
        if sum(L.chi == -1 for L in w) % 2: continue
        if sum("exp(iH)" in L.name for L in w) < min_generic: continue
        return w
def word_f(w):
    def f(k):
        X = np.eye(12, dtype=complex)
        for L in w: X = X @ L.f(k)
        return X
    return f
def predicted(w, k0, a):
    """sum_j v_j^{(b_j)}, b_j = label of the doublet entering letter j from the right."""
    tot = 0.0; b = a
    for L in reversed(w):
        v, _, _, _ = letter_v(L, k0, b); tot += v; b *= L.chi
    assert b == a
    return tot
def actual(w, k0, D, ndir=24):
    f = word_f(w); W = f(k0); dW = dfd(f, k0)
    M = [D.conj().T @ W.conj().T @ dW[i] @ D for i in range(3)]
    sp = []; tilt = 0
    for _ in range(ndir):
        q = rng.normal(size=3); q /= np.linalg.norm(q)
        h = -1j * sum(q[i] * M[i] for i in range(3)); h = (h + h.conj().T) / 2
        e = np.linalg.eigvalsh(h); sp.append((e[1] - e[0]) / 2); tilt = max(tilt, abs(e[0] + e[1]) / 2)
    return M, np.array(sp), tilt
def direct_slope(w, k0, D, w0, delta=1e-4, ndir=3):
    """Half the eigenphase splitting of the two eigenvectors of W(k*+delta q) with the largest weight on D, over delta.
    (The O-symmetric second-order term on D is a scalar, so the half-splitting is accurate to O(delta^2).)"""
    f = word_f(w); out = []
    for _ in range(ndir):
        q = rng.normal(size=3); q /= np.linalg.norm(q)
        sl = []
        for dl in (delta, delta / 2):
            ev, V = np.linalg.eig(f(k0 + dl * q)); wt = np.linalg.norm(D.conj().T @ V, axis=0) / np.linalg.norm(V, axis=0)
            idx = np.argsort(-wt)[:2]; ph = np.angle(ev[idx] / w0); sl.append(abs(ph[0] - ph[1]) / 2 / dl)
        out.append((4 * sl[1] - sl[0]) / 3)                     # Richardson: removes the O(delta^2) term
    return np.array(out)
def isolated_doublet(W, D, gap=1e-6):
    X = D.conj().T @ W @ D
    if not (np.allclose(W @ D, D @ X, atol=1e-9) and np.allclose(X, X[0, 0] * np.eye(2), atol=1e-9)): return None, False
    w0 = X[0, 0]; ev = np.linalg.eigvals(W); n_near = np.sum(np.abs(ev - w0) < gap)
    return w0, n_near == 2

t0 = time.time()
NW = 260; n_lev = 0; n_gen = 0; worst_sp = 0; worst_sign = 0; worst_iso = 0; worst_tilt = 0; worst_dir = 0; n_dir = 0
n_4 = 0; skipped = 0; preserve_fail = 0; zero_speed = 0
for t in range(NW):
    w = rand_word(min_generic=1 if t % 2 == 0 else 0)
    f = word_f(w)
    for kname, k0 in KPTS.items():
        W = f(k0)
        for a, D in DOUB.items():
            w0, iso = isolated_doublet(W, D)
            if w0 is None: preserve_fail += 1; continue
            if not iso: skipped += 1; continue
            pv = predicted(w, k0, a)
            M, sp, tilt = actual(w, k0, D)
            worst_sp = max(worst_sp, np.abs(sp - abs(pv)).max())
            worst_iso = max(worst_iso, sp.max() - sp.min()); worst_tilt = max(worst_tilt, tilt)
            worst_sign = max(worst_sign, max(np.abs(M[i] - 1j * pv * TAU[a][i]).max() for i in range(3)))
            if abs(pv) < 1e-6: zero_speed += 1
            if n_dir < 300:
                ds = direct_slope(w, k0, D, w0); worst_dir = max(worst_dir, np.abs(ds - abs(pv)).max()); n_dir += 1
            n_lev += 1; n_gen += any("exp(iH)" in L.name for L in w)
print(f"   {NW} words, {n_lev} isolated 2-fold D+- levels at +-k* ({n_gen} from words with a generic exp(iH) letter); "
      f"{skipped} D levels degenerate with another level (not 2-fold, excluded here); {zero_speed} with sum v = 0; {time.time() - t0:.0f}s")
report(preserve_fail == 0, "every even-A2 word preserves D+ and D- at +-k* and is a scalar there (Schur, all words)")
report(n_lev >= 200 and worst_sp < 1e-6,
       f"speed from DPT of the whole word = |sum_j v_j^(b_j)| on all {n_lev} levels (worst |dev| {worst_sp:.1e})")
report(worst_iso < 1e-6 and worst_tilt < 1e-6,
       f"cones isotropic (spread of speed over 24 directions {worst_iso:.1e}) and untilted (tilt {worst_tilt:.1e})")
report(worst_sign < 1e-6, f"signed statement: P W^dag dW P = i (sum v) tau^(a) entrywise (worst {worst_sign:.1e}); chirality = sign(sum v) "
       f"in the fixed tau orientation")
report(worst_dir < 1e-6, f"direct diagonalisation of W(k*+delta q), delta = 1e-4 and 5e-5, Richardson-extrapolated, on {n_dir} levels "
       f"x 3 directions: half eigenphase splitting / delta = |sum v| (worst {worst_dir:.1e})")

# ---------------------------------------------------------------- B26 sign-flipped n_eff
print("== 5. B26 reproduction: words in S^p, A_a = A0 S^a, R_L, Rt and symmetric on-site letters")
ok = True; nflip = 0; nb = 0
for t in range(160):
    while True:
        m = int(rng.integers(3, 8)); w = []
        for _ in range(m):
            r = rng.random()
            w.append(L_A(int(rng.integers(-2, 3))) if r < 0.35 else L_S(int(rng.choice([1, 2, -1, -2]))) if r < 0.6
                     else L_RL if r < 0.7 else L_RT if r < 0.8 else L_onsite())
        if sum(L.chi == -1 for L in w) % 2 == 0: break
    # B26's formula: n_eff = sum over S-powers p of (-1)^{# A0 to the left}, the A0 inside A_a counted as left of its S^a
    n_eff = 0; nA = 0; n_raw = 0
    for L in w:
        if '^' not in L.name: continue
        p = int(L.name.split('^')[1])
        if L.chi == -1: nA += 1
        n_eff += (-1) ** nA * p; n_raw += p
    f = word_f(w)
    for kname, k0 in KPTS.items():
        W = f(k0)
        for a, D in DOUB.items():
            w0, iso = isolated_doublet(W, D)
            if w0 is None or not iso: continue
            pv = predicted(w, k0, a); _, sp, _ = actual(w, k0, D, ndir=6)
            ok &= abs(abs(pv) - abs(n_eff) * r23) < 1e-7 and np.abs(sp - abs(n_eff) * r23).max() < 1e-6
            nb += 1; nflip += abs(n_eff) != abs(n_raw)
report(ok and nb > 100, f"path-sum |sum v| = |n_eff| sqrt2/3 = DPT speed on {nb} doublets (B26's sign-flipped n_eff; "
       f"{nflip} with |n_eff| != |n_raw|)")

# ---------------------------------------------------------------- 4-fold D+ (+) D- levels
print("== 6. scope: 4-fold D+ (+) D- levels (tuned with the symmetric on-site letter Z = exp(i alpha P_D+))")
PDP = DP @ DP.conj().T
report(all(np.allclose(g['U'] @ PDP @ g['U'].T, PDP) for g in PROPER), "P_D+ is an O-symmetric on-site operator, so Z is a legal A1 letter with v = 0")
n4 = 0; nmix = 0; ndiff = 0; worst4 = 0; worst_off = 0; gen4 = 0; ndiff_gen = 0; nL1 = 0; L1_equal = True
for t in range(120):
    generic = t % 2 == 0
    if generic: w = rand_word(min_generic=1)
    else:
        while True:
            w = [rng.choice([L_S(int(rng.choice([1, 2, -1, -2]))), L_RL, L_RT, L_onsite(), L_A(int(rng.integers(-2, 3)))]) for _ in range(int(rng.integers(2, 6)))]
            if sum(L.chi == -1 for L in w) % 2 == 0: break
    for kname, k0 in KPTS.items():
        W = word_f(w)(k0)
        wp = (DP.conj().T @ W @ DP)[0, 0]; wm = (DM.conj().T @ W @ DM)[0, 0]
        alpha = np.angle(wm / wp); Zm = expm(1j * alpha * PDP)
        w2 = w + [Letter("Z", 1, lambda k, Zm=Zm: Zm)]
        W2 = word_f(w2)(k0); B = np.hstack([DP, DM]); X = B.conj().T @ W2 @ B
        if not np.allclose(X, X[0, 0] * np.eye(4), atol=1e-9): continue
        ev = np.linalg.eigvals(W2)
        if np.sum(np.abs(ev - X[0, 0]) < 1e-6) != 4: continue       # G3/2 accidentally degenerate too: skip
        f2 = word_f(w2); dW = dfd(f2, k0)
        M = [B.conj().T @ W2.conj().T @ dW[i] @ B for i in range(3)]
        off = max(np.abs(M[i][:2, 2:]).max() + np.abs(M[i][2:, :2]).max() for i in range(3)); worst_off = max(worst_off, off)
        pp = predicted(w2, k0, +1); pm = predicted(w2, k0, -1)
        dev = max(max(np.abs(M[i][:2, :2] - 1j * pp * TAU[1][i]).max(), np.abs(M[i][2:, 2:] - 1j * pm * TAU[-1][i]).max()) for i in range(3))
        # eigenvalues of the 4x4 first-order matrix along random directions: {+-|pp|, +-|pm|}
        for _ in range(4):
            q = rng.normal(size=3); q /= np.linalg.norm(q)
            h = -1j * sum(q[i] * M[i] for i in range(3)); h = (h + h.conj().T) / 2
            dev = max(dev, np.abs(np.sort(np.linalg.eigvalsh(h)) - np.sort([pp, -pp, pm, -pm])).max())
        worst4 = max(worst4, dev); n4 += 1
        if abs(abs(pp) - abs(pm)) > 1e-3:
            ndiff += 1; ndiff_gen += generic
        if not generic:
            nL1 += 1; L1_equal &= abs(abs(pp) - abs(pm)) < 1e-8 and (abs(pp) < 1e-8 or np.sign(pp) == -np.sign(pm))
        gen4 += generic
report(n4 >= 100 and worst_off < 1e-6, f"{n4} tuned 4-fold D+(+)D- levels: first-order D+<->D- block vanishes (worst {worst_off:.1e}) - no mixing")
report(worst4 < 1e-6, f"the two cones are untilted, isotropic, at |sum v^(+)| and |sum v^(-)| (worst dev {worst4:.1e})")
report(L1_equal and nL1 > 0, f"old-palette words (S, R_L, Rt, on-site, A0S^a): equal speeds |n_eff| sqrt2/3, opposite chirality ({nL1} levels; B20 L1 4-fold)")
report(ndiff_gen > 0, f"with generic exp(iH) letters the two speeds differ: {ndiff_gen} of {gen4} generic 4-fold levels have "
       f"| |v+| - |v-| | > 1e-3 (L1's equal-speed 4-fold statement does NOT generalise)")

print(f"TOTAL PASS={NPASS} FAIL={NFAIL}")
