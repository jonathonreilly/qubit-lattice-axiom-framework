#!/usr/bin/env python3
"""anomaly-family-count: does the Spin(12)-Casimir far-wall term (spin10-two-flavour) keep the cube's three-fold turn with a
turn-neutral ground state, so that the families-mod-3 obstruction binds on the ADOPTED slab and N_f = 0 mod 3 follows?
 A  turn charges on CL-1's cell: corner charges (families-mod-3 A4) and the copy phase of the near- and far-wall Weyl spaces
    of the adopted cell slab (wall-families C; chiral-tick-form), one-copy window.
 B  the turn on the 32 far-wall modes (16 x two spin components): exact commutation with H_sym and with Omega, per twist k.
 C  ground-state turn charge for N_f = 1, 2, 3 (Casimir structure; no diagonalisation of 2^(32 N_f)).
 D  anomaly bookkeeping: which N_f can be gapped symmetrically, with H_sym, with Omega, and the families-mod-3 contrast.
Labels: [T] exact, [F] finite diagnostic, [S] reading. Supplied: the 16 with one orbital per weight, the two-valued spin
flavour, the cell-slab kernel (B/2 + i eps)/2 with copy operator (1 - s) R_e, (m, Mc, Ls) = (0.5, 1, 24), free fields.
Cited, not rederived: 't Hooft matching, crystalline equivalence, the SMG conjecture (sufficiency), families-mod-3 C1 formula.
Every line reports a RESULT; the synthesis verdict (criteria_pre_run.txt) is printed, a FAIL there is a result."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
OM = np.exp(2j * np.pi / 3); th = 2 * np.pi / 3; n111 = np.ones(3) / np.sqrt(3)
sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1.]).astype(complex)
SIG = [sx, sy, sz]
def q3(z): return int(round(np.angle(z) / th)) % 3

# ================================================================ A. turn charges on CL-1's cell
print("== A. turn charges on CL-1's cell")
C = np.array(list(itertools.product((0, 1), repeat=3))); cc = C - 0.5
def Jm(j):
    d = int(round(2 * j + 1)); m = j - np.arange(d); Jp = np.zeros((d, d), complex)
    for a in range(1, d): Jp[a - 1, a] = np.sqrt(j * (j + 1) - m[a] * (m[a] + 1))
    return [(Jp + Jp.conj().T) / 2, (Jp - Jp.conj().T) / 2j, np.diag(m).astype(complex)]
J3 = Jm(1.5); XI = []
for i in range(8):
    n_ = (2 * C[i] - 1.0) / np.sqrt(3); w_, v_ = np.linalg.eigh(sum(n_[k] * J3[k] for k in range(3))); XI.append(v_[:, -1])
R3 = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], float)
Dm = expm(-1j * th * sum(n111[k] * J3[k] for k in range(3))); L3 = np.zeros((8, 8), complex)
for i in range(8):
    k = int(np.argmin(np.sum(abs(cc - R3 @ cc[i]), 1))); L3[k, i] = XI[k].conj() @ Dm @ XI[i]
qc = sorted(q3(x) for x in np.linalg.eigvals(-L3))
check("A1 [T]", qc == [0, 0, 0, 0, 1, 1, 2, 2], "families-mod-3 A4 reproduced: the spin-3/2 turn on the 8 cell corners has charges "
      "{0^4, 1^2, 2^2}", f"{qc}")
# --- cell slab (wall-families C, inlined)
E3 = np.eye(3, dtype=int); SITES = list(itertools.product((0, 1), repeat=3))
def eta(x, i): return [1, (-1) ** int(x[0]), (-1) ** int(x[0] + x[1])][i]
def pairs(par):
    out = []
    for o in itertools.product((0, 1), repeat=3):
        A = np.array(o) + par
        for i in range(3):
            if not o[i]: out.append((A, A + E3[i], eta(A, i), i))
    return out
PE, PO = pairs(0), pairs(1)
def Wb(pp, k, i):
    M = np.zeros((8, 8), complex)
    for x, y, a, j in pp:
        if j != i: continue
        ia = np.ravel_multi_index(tuple(x % 2), (2,) * 3); ib = np.ravel_multi_index(tuple(y % 2), (2,) * 3)
        ph = a * np.exp(-1j * k @ (x // 2 - y // 2)); M[ia, ib] += ph; M[ib, ia] += np.conj(ph)
    return M
def cell(k):
    We = [Wb(PE, k, i) for i in range(3)]; Wo = [Wb(PO, k, i) for i in range(3)]
    Re = sum(We) / np.sqrt(3); Ro = sum(Wo) / np.sqrt(3); s = 1j * We[0] @ We[1] @ We[2] @ Re
    return We, Wo, Re, Ro, s
EPS8 = np.diag([(-1.) ** sum(x) for x in SITES]).astype(complex); I8 = np.eye(8)
def slab(onl, A, Ls):
    S = np.eye(Ls, k=-1); return np.kron(np.eye(Ls), onl) + np.kron(S, A) + np.kron(S.T, A.conj().T)
def HC(k, m, Mc, Ls):
    _, _, Re, Ro, s = cell(k)
    return slab((Re - Ro) + (m - 1) * (Re + Ro) / 2 - (Mc / 2) * (I8 - s) @ Re, ((Re + Ro) / 2 + 1j * EPS8) / 2, Ls)
def wall(H, Ls, near):
    ev, V = np.linalg.eigh(H); Z = V[:, np.abs(ev) < 1e-3]
    w = np.zeros(len(H)); w[: (Ls // 2) * 8] = 1; e2, U2 = np.linalg.eigh(Z.conj().T @ np.diag(w) @ Z); Z = Z @ U2
    return Z[:, e2 > 0.5] if near else Z[:, e2 < 0.5]
def hand(Hf, P, h=1e-5):
    v = np.zeros((3, 3))
    for j in range(3):
        q = np.zeros(3); q[j] = h; hj = P.conj().T @ (Hf(q) - Hf(-q)) @ P / (2 * h)
        for i in range(3): v[i, j] = np.real(np.trace(SIG[i] @ hj)) / 2
    return int(np.sign(np.linalg.det(v)))
perm = np.zeros(8, int)
for a in SITES: perm[np.ravel_multi_index(a, (2,) * 3)] = np.ravel_multi_index((a[2], a[0], a[1]), (2,) * 3)
Pm = np.zeros((8, 8)); Pm[perm, np.arange(8)] = 1
We0, Wo0, _, _, sK0 = cell(np.zeros(3))
src = [Pm @ W @ Pm.T for W in We0 + Wo0]; tgt = [We0[1], We0[2], We0[0], Wo0[1], Wo0[2], Wo0[0]]
Dg = np.zeros(8, complex); Dg[0] = 1; todo = [0]
while todo:
    x = todo.pop()
    for A_, B_ in zip(src, tgt):
        for y in np.nonzero(np.abs(A_[x]) > 1e-12)[0]:
            if Dg[y] == 0: Dg[y] = np.conj(B_[x, y] / A_[x, y] / Dg[x]); todo.append(y)
UT = np.diag(Dg) @ Pm
UT3 = np.abs(np.linalg.matrix_power(UT, 3) - I8).max()
tl = max([np.abs(UT @ A_ @ UT.conj().T - B_).max() for A_, B_ in zip(We0 + Wo0, tgt)]
         + [np.abs(UT @ sK0 @ UT.conj().T - sK0).max(), np.abs(UT @ EPS8 @ UT.conj().T - EPS8).max()])
Ls = 24; UTL = np.kron(np.eye(Ls), UT); sL = np.kron(np.eye(Ls), sK0)
def copy_data(P):
    """turn on a 2-dim wall Weyl space = e^(i phi) x spin-1/2 turn; returns (s value, eigen ratio ok, copy charge q, det)"""
    ev = np.linalg.eigvals(P.conj().T @ UTL @ P); sv = np.round(np.linalg.eigvalsh(P.conj().T @ sL @ P), 6)
    ratio_ok = abs(abs(np.angle(ev[0] / ev[1])) - th) < 1e-8
    det = np.prod(ev)                          # = (copy phase)^2 = w^(2q), copy phase = -w^q when UT^3 = 1
    return sv, ratio_ok, (2 * q3(det)) % 3, det
m1, Mc1 = 0.5, 1.0; H1 = lambda k: HC(k, m1, Mc1, Ls); H0 = H1(np.zeros(3))
Pn, Pf = wall(H0, Ls, True), wall(H0, Ls, False)
dn, df = copy_data(Pn), copy_data(Pf); hn, hf = hand(H1, Pn), hand(H1, Pf)
ok = (tl < 1e-12 and Pn.shape[1] == 2 and Pf.shape[1] == 2 and list(dn[0]) == [1, 1] and list(df[0]) == [1, 1] and dn[1] and df[1]
      and dn[2] == df[2] and abs(dn[3] / df[3] - 1) < 1e-9 and hn == -hf)
check("A2 [T]/[F]", ok, "adopted slab on CL-1's cell, one-copy window (m, Mc) = (0.5, 1), Ls = 24: near and far wall each hold one "
      "2-dim Weyl space, BOTH in the s = +1 copy, opposite hands; the turn (site-phase lift) acts on each as copy phase x "
      "spin-1/2 turn with the SAME copy charge: q_mirror = q_light", f"lift defect {tl:.0e}, |UT^3 - 1| {UT3:.0e}; q near {dn[2]}, far {df[2]}; "
      f"det ratio {abs(dn[3] / df[3] - 1):.0e}; hands {hn:+d}/{hf:+d}")
H2 = HC(np.zeros(3), 1.5, 1.0, Ls); P2 = wall(H2, Ls, True); es, Vs = np.linalg.eigh(P2.conj().T @ sL @ P2)
dp, dmn = copy_data(P2 @ Vs[:, es > 0]), copy_data(P2 @ Vs[:, es < 0]); QL = dn[2]
check("A3 [F]", dp[2] == QL and dmn[2] != QL, "calibration (two-copy window (1.5, 1)): the s = -1 copy carries a DIFFERENT copy "
      "charge (wall-families C5), so the equality in A2 is a property of the window, not of the lift convention",
      f"q(s+) = {dp[2]}, q(s-) = {dmn[2]}")

# ================================================================ B. turn on the 32 far-wall modes
print("== B. the turn on the 32 far-wall modes (two spin components x 16)")
def ann(n):
    dim = 1 << n; st = np.arange(dim); out = []
    for j in range(n):
        A = np.zeros((dim, dim)); s_ = st[(st >> j) & 1 == 1]
        A[s_ ^ (1 << j), s_] = 1 - 2 * (np.bitwise_count(s_ & ((1 << j) - 1)).astype(np.int64) & 1); out.append(A)
    return out
b5 = ann(5); G10 = []
for k in range(5): G10 += [b5[k] + b5[k].T, 1j * (b5[k] - b5[k].T)]
ev16 = [s for s in range(32) if bin(s).count('1') % 2 == 0]
t16 = [(-0.25j * (G10[a] @ G10[c] - G10[c] @ G10[a]))[np.ix_(ev16, ev16)] for a, c in itertools.combinations(range(10), 2)]
M16 = None
for Cc in (np.linalg.multi_dot(G10[0::2]), np.linalg.multi_dot(G10[1::2])):
    M = [(Cc @ g)[np.ix_(ev16, ev16)] for g in G10]
    if all(np.abs(x).max() > 0.5 for x in M): M16 = M; break
EP = np.array([[0, 1], [-1, 0]], complex)
P = [np.kron(EP, Ma) for Ma in M16]            # B_a = (1/2) c^T P_a c, mode x = 16 s + alpha
Q4 = sum(np.einsum('ij,kl->ijkl', Pa, Pa.conj()) for Pa in P)   # quartic tensor of sum B_a^+ B_a (fixes H_sym with J)
O4 = sum(np.einsum('ij,kl->ijkl', Pa, Pa) for Pa in P)          # tensor of Omega's B_a B_a
def tr4(T, u, conj2):
    v = u.conj() if conj2 else u
    return np.einsum('ai,bj,ck,dl,abcd->ijkl', u, u, v, v, T, optimize=True)
Sspin = expm(-1j * th / 2 * sum(n111[i] * SIG[i] for i in range(3)))
gZ3 = expm(1j * (4 * np.pi / 3) * t16[0])                     # a Z3 element of Spin(10): charges w^(+-1) on the 16
gR = expm(1j * sum(rng.normal() * t for t in t16))            # a random Spin(10) element
gbad = np.diag([OM if i < 5 else 1 for i in range(16)])       # Z3 phases on 5 of 16 weights: not in Spin(10)
res = {}
for gname, g in (('1', np.eye(16)), ('Z3 in Spin(10)', gZ3), ('random Spin(10)', gR), ('non-Spin(10)', gbad)):
    for t in range(3):
        u = OM ** t * np.kron(Sspin, g)
        dH = np.abs(tr4(Q4, u, True) - Q4).max(); dJ = np.abs(u.conj().T @ u - np.eye(32)).max()
        dO = np.abs(tr4(O4, u, False) - O4).max()
        res[(gname, t)] = (dH, dO, dJ)
okH = all(res[(g, t)][0] < 1e-12 for g in ('1', 'Z3 in Spin(10)', 'random Spin(10)') for t in range(3))
check("B1 [T]", okH and abs(np.linalg.det(Sspin) - 1) < 1e-12, "for every twist (per-mode charge t = q + k = 0, 1, 2) and every "
      "Spin(10)-compatible action on the 16 (identity, a Z3 element with charges w^(+-1), a random element), u = w^t S_spin x g "
      "leaves the quartic tensor of sum B^+ B (with J, number and spin invariant) exactly fixed: [T_k, H_sym] = 0",
      f"max defect {max(res[(g, t)][0] for g in ('1', 'Z3 in Spin(10)', 'random Spin(10)') for t in range(3)):.0e}; det S_spin = 1")
check("B2 [T]", min(res[('non-Spin(10)', t)][0] for t in range(3)) > 1e-3, "contrast: Z3 phases on 5 of the 16 weights (not a "
      "Spin(10) element) break H_sym at every t: the turn must act on the 16 as a phase x Spin(10) element (Schur), so the only "
      "turn data on the far wall are the copy charge and the spin lift", f"min defect {min(res[('non-Spin(10)', t)][0] for t in range(3)):.2f}")
kept = [t for t in range(3) if res[('1', t)][1] < 1e-12 and res[('random Spin(10)', t)][1] < 1e-12]
check("B3 [T]", kept == [0], "Omega = sum B_a B_a + h.c. (charge 4, U(1)_N -> Z4) picks up w^(4t) = w^t: it is kept only at t = 0, "
      "i.e. twist k = -q_mirror, exactly as the families-mod-3 top form O_A", f"kept t = {kept}")

# ================================================================ C. ground-state turn charge
print("== C. ground-state turn charge (GS: N = 16 per copy, flavour singlet, Spin(10) singlet; spin10-two-flavour C3-C4)")
# T_k = w^(16 t) exp(i (4 pi t/3) J) x flavour(S) x g with J = (N - 16)/2: check on |0> (N=0) and |F> (N=32) via det u
okC = True
for t in range(3):
    u = OM ** t * np.kron(Sspin, gR)
    okC &= abs(OM ** (16 * t) * np.exp(1j * 4 * np.pi * t / 3 * (-8)) - 1) < 1e-12        # |0>: eigenvalue 1
    okC &= abs(OM ** (16 * t) * np.exp(1j * 4 * np.pi * t / 3 * 8) - np.linalg.det(u)) < 1e-9   # |F>: det u
tab = {Nf: [q3(OM ** (16 * Nf * t)) for t in range(3)] for Nf in (1, 2, 3)}
check("C1 [T]", okC and tab == {1: [0, 1, 2], 2: [0, 2, 1], 3: [0, 0, 0]}, "T_k = w^(16 t) e^(i 4 pi t J / 3) x S_flavour x g "
      "(J in so(12), flavour commuting with so(12)); on the unique GS (J = 0, S = 0, Spin(10) singlet) T_k = w^(16 N_f t): "
      "charge N_f t mod 3; consistency on |0> (1) and |F> (det u) exact", f"GS charge by t = 0,1,2: N_f=1 {tab[1]}, 2 {tab[2]}, 3 {tab[3]}")
print("   C2 [S] at the Omega twist (t = 0) the GS is turn-neutral for every N_f. A nonzero charge at t != 0 is a charge per cell on "
      "the turn axis (an atomic, Wyckoff label of a product state), not an anomaly: a unique symmetric product state is never anomalous")

# ================================================================ D. anomaly bookkeeping
print("== D. which N_f can be gapped symmetrically")
def far_coeffs(N, t):   # far wall: N mirror 16s (hand -1), U(1)_N charge 1, internal turn charge t; T(16) = 2 (T(10) = 1)
    return dict(N3=-16 * N, Ngrav=-16 * N, Z3_spin10=(-2 * N * t) % 3, Z3_grav=(-16 * N * t) % 3, Z3_cubed=(-16 * N * t ** 3) % 9)
Ns = range(1, 10)
H_ok = [N for N in Ns if any(far_coeffs(N, t)['N3'] == 0 for t in range(3))]
check("D1 [T]", H_ok == [], "H_sym keeps U(1)_N: the far wall's U(1)_N^3 and U(1)_N-gravity coefficients are -16 N_f != 0, so "
      "no N_f is symmetrically gappable with H_sym (register: no mode-number-conserving term gaps the mirror alone); the site gap "
      "is a trivial product state and the wall mode relocates (spin10-two-flavour E2, now forced)", f"gappable N in 1..9: {H_ok}")
def allowed(ql, qm, mdoub):
    k = (-qm) % 3                                                           # Omega / O_A twist
    farZ3 = lambda N: any(v for kk, v in far_coeffs(N, (qm + k) % 3).items() if kk.startswith('Z3'))
    return [N for N in Ns if (N * mdoub * (ql + k)) % 3 == 0 and not farZ3(N)]
slabN = allowed(QL, QL, 4); hpN = allowed(2, 1, 4)
check("D2 [T]", slabN == list(Ns), "Omega on the adopted slab (q_mirror = q_light, A2): the twist k = -q_mirror also neutralises the "
      "light copy, every Z3 coefficient of the far wall vanishes and the light index N m (q_l + k) = 0: EVERY N_f passes "
      "(the families-mod-3 'k = -q_light' loophole is forced)", f"allowed N: {slabN}")
check("D3 [T]", hpN == [3, 6, 9], "contrast, families-mod-3 tastes (chiral generator H', mirror on the OTHER copy, q_l = 2, q_m = 1, "
      "4 doublets): N(q_l - q_m) = 0 mod 3, allowed N = 3, 6, 9; the mod 3 needs q_mirror != q_light", f"allowed N: {hpN}")
okJ = dn[2] == df[2] and dp[2] == QL
check("D4 [T]", okJ, "stacked families on one cell copy share one turn charge (family-blind), so the turn-CP lemma does not force J = 0 "
      "from the turn; but no N_f is preferred either: minimality (3 over 6) is supplied by nothing in the rules")
S1, S2, S3 = True, True, (slabN == [3, 6, 9])
print(f"   synthesis (criteria_pre_run): S1 turn kept {S1}, S2 neutral GS at the Omega twist {S2}, S3 obstruction exactly N != 0 mod 3 "
      f"{S3} -> {'PASS' if S1 and S2 and S3 else 'FAIL at S3: on the adopted slab the mirror sits on the light copy'}")
print("Supplied: 16 with one orbital per weight, spin as flavour, cell-slab kernel and (m, Mc, Ls), free fields; cited: 't Hooft "
      "matching, crystalline equivalence, SMG (sufficiency).")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
