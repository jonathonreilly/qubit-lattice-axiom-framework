AUDIT_INPUT_PATHS = ('docs/NO_PRINCIPLE_TESTED_FORCES_A_NONZERO_TURN_GRADED_TICK_WINDING_BECAUSE_CHIRAL_WALLS_EXIST_AT_ZERO_WINDING_TIME_REVERSAL_FORBIDS_THE_FAMILY_CLASS_AND_FEWEST_CHANGES_SELECTS_ZERO_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""tick-winding-origin: does any adopted or independently motivated principle FORCE the update tick's turn-graded winding W != 0
(the slab-parity condition for mod-3 families)?
 0  rederived: copy-flip W = f(q_l,+) + f(q_m,-), zero iff q_m = q_l, and every copy-flip W has all three components nonzero.
 a  chirality: a W = 0 slab already has one-handed walls; gappable-mirror consistency holds for every N_f at W = 0.
 b  T / chiral / axis-reversing lemma (each forces a zero component of W); CL-1's tick has all three, FREEZE none; T-closure
    control; T breaking without W.
 c  FREEZE halves CTWIST's winding; a fewest-changes cost is minimal at W = 0 and blind to U -> U^+.
 d  W is additive; the W = 0 class holds the identity and all turn-commuting circuits; least information selects W = 0.
Labels: [T] exact, [F] finite diagnostic, [S] reading. FREEZE and the slab are rebuilt inline from slab-parity / floquet-pi-slab
(same seed and draw order). Every line reports a RESULT; the synthesis verdict follows criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space, schur

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
w = np.exp(2j * np.pi / 3); I8 = np.eye(8)
# ------------------------------------------------ FREEZE rebuild (twist-local-single, same seed and draw order)
def nullsp(rows): return null_space(np.vstack(rows), rcond=1e-9)
def cm(o): return np.kron(o, I8) - np.kron(I8, o.T)
def axang(R):
    ev, vv = np.linalg.eig(R); n = np.real(vv[:, np.argmin(abs(ev - 1))])
    th = np.arccos(np.clip((np.trace(R) - 1) / 2, -1, 1)); K = np.array([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
    return (n if np.allclose(expm(th * K), R) else -n), th
C3d = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0.0]])
CELL = list(it.product([0, 1], repeat=3)); A = np.array(CELL); IDX = {a: 4 * a[0] + 2 * a[1] + a[2] for a in CELL}
def eta_s(i, a): return [1, (-1) ** a[0], (-1) ** (a[0] + a[1])][i]
def Wl(i, k, odd):
    M = np.zeros((8, 8), complex)
    for a in CELL:
        if a[i] == (1 if odd else 0):
            b = list(a); b[i] = 1 - a[i]; b = tuple(b); ph = np.exp(2j * k[i]) if odd else 1
            M[IDX[b], IDX[a]] = eta_s(i, a) * ph; M[IDX[a], IDX[b]] = eta_s(i, a) * np.conj(ph)
    return M
Re = sum(Wl(i, np.zeros(3), 0) for i in range(3)) / np.sqrt(3)
def U1(k, eps=0.3): return expm(1j * eps * sum(Wl(i, k, 1) for i in range(3)) / np.sqrt(3)) @ expm(-1j * eps * Re)
hh = 1e-6; Av = []
for i in range(3):
    d = np.zeros(3); d[i] = hh; Av.append(1j * (U1(d) - U1(-d)) / (2 * hh))
Ah = [a / np.sqrt(np.trace(a @ a).real / 8) for a in Av]
S = [-0.25j * (Ah[(i + 1) % 3] @ Ah[(i + 2) % 3] - Ah[(i + 2) % 3] @ Ah[(i + 1) % 3]) for i in range(3)]
chi = 1j * Ah[0] @ Ah[1] @ Ah[2]
kt = [rng.uniform(-1, 1, 3) for _ in range(2)]
P = np.zeros((8, 8))
for a in CELL:
    b = tuple(np.rint(C3d @ (np.array(a) - .5) + .5).astype(int)); P[IDX[b], IDX[a]] = 1
for sgn in it.product([1, -1], repeat=8):
    T3 = np.diag(sgn) @ P
    if all(np.allclose(T3 @ U1(k) @ T3.T, U1(C3d @ k)) for k in kt): break
nl, th = axang(C3d)
tt = expm(-1j * th * sum(nl[i] * S[i] for i in range(3))).conj().T @ T3
if not np.allclose(np.linalg.matrix_power(tt, 3), I8, atol=1e-6): tt = -tt
PL = (I8 + chi) / 2; PR = I8 - PL; sig = [2 * s for s in S]
tau3 = (tt - tt.conj().T) / (1j * np.sqrt(3)); tau3 = (tau3 + tau3.conj().T) / 2
Pw = (I8 + tau3) / 2; Pb = I8 - Pw
Cb = nullsp([cm(o) for o in sig + [chi]]); Yr = (Cb @ rng.normal(size=Cb.shape[1])).reshape(8, 8)
tp = np.zeros((8, 8), complex)
for Pq in (PL, PR):
    Zb = Pq @ Pw @ Yr @ Pb @ Pq; tp += Zb / np.sqrt(np.trace(Zb @ Zb.conj().T).real / 2)
tau1 = tp + tp.conj().T; tau2 = -1j * (tp - tp.conj().T); gam = [tau3 @ s for s in sig]
def Uc(K):
    c, s = np.cos(K), np.sin(K); H = (np.sqrt(2) / 3) * (c[0] + np.conj(w) * c[1] + w * c[2])
    return c.sum() / 3 * I8 + 1j * (H * tp + np.conj(H) * tp.conj().T + sum(s[i] * gam[i] for i in range(3)) / np.sqrt(3))
Cm = nullsp([cm(o) for o in sig + [tau1, tau2, tau3]])
for j in range(Cm.shape[1]):
    e = Cm[:, j].reshape(8, 8); a = (e - chi @ e @ chi) / 2
    if np.linalg.norm(a) > 1e-6: Ex = a + a.conj().T; break
Ex = Ex / np.sqrt(np.trace(Ex @ Ex).real / 8); Y = Pw + Pb @ Ex
Pp = (I8 + chi @ tau3) / 2; Pm = I8 - Pp
def UF(K): return Pp @ (Y @ Uc(K) @ Y.conj().T) + Pm @ (1j * tau3)
Pq1, Pq2 = Pp @ (I8 + tau3) / 2, Pp @ (I8 - tau3) / 2            # node labels: tau3 = +1 -> q 1, tau3 = -1 -> q 2 (A1)

# ------------------------------------------------ tools on the axis (floquet-pi-slab)
def sectors(n):
    e, v = np.linalg.eig(np.kron(np.eye(n), T3)); lb = np.round(np.angle(e) / (2 * np.pi / 3)).astype(int) % 3
    return [np.linalg.qr(v[:, lb == a])[0] for a in range(3)]
def wind(U, SEC, n=400):
    ks = np.linspace(0, 2 * np.pi, n + 1); out = []
    for Sx in SEC:
        d = np.array([np.linalg.det(Sx.conj().T @ U(k * np.ones(3)) @ Sx) for k in ks])
        out.append(int(round(np.sum(np.angle(d[1:] / d[:-1])) / (2 * np.pi))))
    return out
def flow(U, SEC, k0, e0, dk=1e-3, c=0.1, W=None):
    f = []
    for Sx in SEC:
        cnt = []
        for k in (k0 + dk, k0 - dk):
            ev, vv = np.linalg.eig(Sx.conj().T @ U(k * np.ones(3)) @ Sx); thx = np.angle(ev * np.exp(-1j * e0))
            m = (thx > 0) & (thx < c)
            if W is not None: m &= np.array([np.linalg.norm(W @ Sx @ vv[:, j]) ** 2 > 0.5 for j in range(len(ev))])
            cnt.append(int(m.sum()))
        f.append(cnt[0] - cnt[1])
    return f
form = lambda q, h: [h * (int(a == (q + 2) % 3) - int(a == (q + 1) % 3)) for a in range(3)]
def slab(K, Ls, g, pat=None, bonds=('q1', 'q2')):
    pat = pat if pat is not None else [l % 2 for l in range(Ls)]
    F = UF(K); U0 = np.zeros((8 * Ls, 8 * Ls), complex); HA = np.zeros_like(U0); HB = np.zeros_like(U0)
    for l, p in enumerate(pat): U0[8 * l:8 * l + 8, 8 * l:8 * l + 8] = F if p == 0 else F.conj().T
    for l in range(Ls - 1):
        H = HA if l % 2 == 0 else HB; lb = bonds[l % 2]
        Pq = {'q1': Pq1, 'q2': Pq2, 'both': Pp, 'none': 0 * Pp}[lb]
        H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] += Pq; H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] += Pq
    return expm(-1j * g * HB) @ expm(-1j * g * HA) @ U0
X2 = np.array([[0, 1], [1, 0]])
def bulk(K, k, g, alt=True):
    F = UF(K); Z = np.zeros((8, 8)); U0 = np.block([[F, Z], [Z, F.conj().T if alt else F]])
    XB = np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]])
    return expm(-1j * g * np.kron(XB, Pq2)) @ expm(-1j * g * np.kron(X2, Pq1)) @ U0

g = 0.5
def walls(Ls, K0, e0, **kw):
    U = slab(K0 * np.ones(3), Ls, g, **kw); e, v = np.linalg.eig(U); sel = np.abs(np.angle(e * np.exp(-1j * e0))) < 1e-6
    Z = np.linalg.qr(v[:, sel])[0]; Op = np.kron(np.diag(np.arange(Ls) * 1.), I8) + 0.01 * np.kron(np.eye(Ls), tau3)
    xe, Uz = np.linalg.eigh(Z.conj().T @ Op @ Z); Z = Z @ Uz
    TL = np.kron(np.eye(Ls), T3); SG = [np.kron(np.eye(Ls), s) for s in sig]; out = []
    for i in range(0, len(xe), 2):
        B = Z[:, i:i + 2]; dq = np.linalg.det(B.conj().T @ TL @ B); Ad = []
        for j in range(3):
            d = np.zeros(3); d[j] = 1e-6
            Ad.append(B.conj().T @ (1j * (slab(K0 * np.ones(3) + d, Ls, g, **kw) - slab(K0 * np.ones(3) - d, Ls, g, **kw)) / 2e-6 @ U.conj().T) @ B)
        M = np.array([[np.trace(Ad[a] @ B.conj().T @ SG[b] @ B).real / 2 for b in range(3)] for a in range(3)])
        out.append((int(round(np.mean(xe[i:i + 2]))), [x for x in range(3) if np.isclose(dq, w ** (2 * x), atol=1e-6)][0], int(np.sign(np.linalg.det(M)))))
    return out
S1 = sectors(1); WF = wind(UF, S1)
def UA(K): return Y @ Uc(K) @ Y.conj().T
def zero_comp(Wv): return any(x == 0 for x in Wv)

# ================================================================ 0. the copy-flip class
print("== 0. rederived: the copy-flip class of W")
cf = {(ql, qm): [a + b for a, b in zip(form(ql, 1), form(qm, -1))] for ql in range(3) for qm in range(3)}
ok0 = (sum(WF) == 0 and all((cf[p] == [0, 0, 0]) == (p[0] == p[1]) for p in cf)
       and all(not zero_comp(cf[p]) for p in cf if p[0] != p[1]) and cf[(2, 1)] == WF)
check("0 [T]", ok0, "W lies in Z[Z3] with augmentation 0; a copy-flipped wall pair (light q_l hand +, mirror q_m hand -) needs "
      "W = f(q_l,+) + f(q_m,-) with f(q,h) = h(e_(q+2) - e_(q+1)); W = 0 <=> q_m = q_l, and every copy-flip W (q_m != q_l) is "
      "+-((1,1,1) - 3 e_a): ALL THREE components nonzero. FREEZE's W_F is the (2,1) element",
      f"W_F {WF}; copy-flip W: " + " ".join(f"{p}:{tuple(cf[p])}" for p in cf if p[0] != p[1]))

# ================================================================ (a) chirality
print("== (a) chirality: one-handed light content with a gappable mirror")
Ls = 6; SE = sectors(Ls); Usl = lambda K: slab(K, Ls, g)
Wn = np.kron(np.diag([1.] * (Ls // 2) + [0.] * (Ls - Ls // 2)), I8); Wfar = np.kron(np.eye(Ls), I8) - Wn
W6 = wind(Usl, SE); Fn = flow(Usl, SE, 0, 0, W=Wn); Ff = flow(Usl, SE, 0, 0, W=Wfar); wl = walls(Ls, 0., 0.)
okA1 = W6 == [0, 0, 0] and Fn == form(2, 1) and Ff == form(2, -1) and wl == [(0, 2, 1), (Ls - 1, 2, -1)]
check("a1 [T]/[F]", okA1, "a W = 0 slab (even Ls = 6, F/F^+ layers, label gates) already has a ONE-HANDED light q 2 on the near "
      "wall with its mirror on the far wall: the near-wall flow f(2,+) != 0 is the single-wall anomaly inflowed by the slab, while W "
      "is the SUM of both walls' flows. Chirality of each wall does not need W != 0", f"W {W6}; near F_0 {Fn}, far F_0 {Ff}; walls "
      f"(layer, q, hand) {wl}")
allowed = lambda ql, qm: [N for N in range(1, 13) if (N * (ql - qm)) % 3 == 0]
okA2 = all(allowed(q, q) == list(range(1, 13)) for q in range(3)) and allowed(2, 1) == [3, 6, 9, 12]
check("a2 [T]", okA2, "gappable-mirror consistency (anomaly-family-count index N_f (q_l - q_m) = 0 mod 3 with Omega twist "
      "k = -q_m) holds for EVERY N_f when q_m = q_l, i.e. at W = 0; W != 0 only RESTRICTS N_f to multiples of 3. Chirality plus "
      "gappability are satisfied in the W = 0 class: they do not force W != 0", f"q_m = q_l: N_f {allowed(2, 2)[:4]}...; "
      f"(q_l, q_m) = (2,1): {allowed(2, 1)}")

# ================================================================ (b) time reversal / record arrow
print("== (b) time reversal, chiral and axis-reversing symmetries")
def forced_zero(sg):             # W_a = -W_sig(a) for all a, with sum W = 0: is some component forced to vanish?
    M = np.array([[1. * (b == a) + (b == sg[a]) for b in range(3)] for a in range(3)] + [[1., 1., 1.]])
    Nl = null_space(M); return Nl.shape[1] == 0 or any(np.all(abs(Nl[a]) < 1e-12) for a in range(3)), Nl.shape[1]
lem = []
for anti in (True, False):
    for s_ in (1, -1):
        for c in range(3):
            # Theta T3 Theta^-1 = w^c T3^s; an antiunitary conjugates the eigenvalue, so sector a -> sig(a)
            if anti: sg = [((-s_ * a) + c) % 3 for a in range(3)]
            else: sg = [((s_ * a) + c) % 3 for a in range(3)]
            lem.append(forced_zero(sg)[0])
check("b1 [T]", all(lem), "lemma: a Floquet antiunitary T (U(k) -> U(-k)^+), a unitary chiral symmetry (U -> U^+) or an "
      "axis-reversing rotation (kappa -> -kappa) that normalises the turn group (Theta T3 Theta^-1 = w^c T3^(+-1)) maps sector a to "
      "sig(a) and forces W_a = -W_sig(a); for every one of the 12 (type, s, c) cases this forces a ZERO component of W (the map is "
      "an involution with a fixed point, or a shift that kills W). Every copy-flip W has all components nonzero (line 0), so EACH "
      "such symmetry FORBIDS the family class. K-dependent sector-mapping Theta are covered too", f"{sum(lem)}/12 cases force a zero component")
Ks = [rng.uniform(-np.pi, np.pi, 3) for _ in range(5)]
def inter(U, typ, nrm=None):    # invertible on-cell V with  A(K) V = V B(K); nrm = (c, s): also V T3 = w^c T3^s V
    rows = []
    for K in Ks:
        A_, B_ = {'T': (U(-K).conj().T, U(K).conj()), 'chiral': (U(K).conj().T, U(K)), 'inv': (U(-K), U(K))}[typ]
        rows.append(np.kron(I8, A_) - np.kron(B_.T, I8))
    if nrm is not None: rows.append(np.kron(I8, w ** nrm[0] * np.linalg.matrix_power(T3, nrm[1] % 3)) - np.kron(T3.T, I8))
    N = null_space(np.vstack(rows), rcond=1e-9)
    if N.shape[1] == 0: return 0, 0.
    V = (N @ (rng.normal(size=N.shape[1]) + 1j * rng.normal(size=N.shape[1]))).reshape(8, 8, order='F')
    sv = np.linalg.svd(V, compute_uv=False); return N.shape[1], sv[-1] / sv[0]
Bh = expm(1j * 0.3 * Re); kk = rng.uniform(-np.pi, np.pi, 3)
tK = np.linalg.norm(Bh @ U1(kk).conj() @ Bh.conj().T - U1(-kk).conj().T)
cl = {t: inter(U1, t, (0, 1)) for t in ('T', 'chiral', 'inv')}
fr = {t: inter(UF, t) for t in ('T', 'chiral', 'inv')}
Rm = np.array([[0, -1, 0], [-1, 0, 0], [0, 0, -1.]]); Pr = np.zeros((8, 8))
for a in CELL:
    b = tuple(np.rint(Rm @ (np.array(a) - .5) + .5).astype(int)); Pr[IDX[b], IDX[a]] = 1
C2 = None
for sg in it.product([1, -1], repeat=8):
    Ts = np.diag(sg) @ Pr
    if all(np.allclose(Ts @ U1(k) @ Ts.T, U1(Rm @ k)) for k in kt): C2 = Ts; break
c2inv = np.linalg.norm(C2 @ T3 @ C2.T - T3.T) if C2 is not None else 9.
okB2 = (tK < 1e-12 and all(cl[t][0] >= 1 and cl[t][1] > 1e-3 for t in cl) and all(fr[t][1] < 1e-9 for t in fr)
        and c2inv < 1e-12 and wind(U1, S1) == [0, 0, 0] and not zero_comp(WF))
check("b2 [T]/[F]", okB2, "CL-1's tick has T: Theta = K up to the half-tick conjugation B = exp(i eps R_e) (exact identity), plus "
      "an on-cell chiral and a k -> -k unitary intertwiner, each commuting with T3 (so W = 0 entirely); its 24-rotation covariance "
      "also contains the axis-reversing C2' about (1,-1,0), which maps T3 -> T3^-1 (so W_0 = 0 on its own). FREEZE has no invertible "
      "on-cell intertwiner of any of the three types (generic intertwiner singular), as the lemma requires", f"K-identity {tK:.0e}; CL-1 (dim, cond) T {cl['T'][0]},{cl['T'][1]:.2f} chiral "
      f"{cl['chiral'][0]},{cl['chiral'][1]:.2f} inv {cl['inv'][0]},{cl['inv'][1]:.2f}; FREEZE cond T {fr['T'][1]:.0e} chiral "
      f"{fr['chiral'][1]:.0e} inv {fr['inv'][1]:.0e}; C2' T3 C2'^T - T3^-1 {c2inv:.0e}")
Z8 = np.zeros((8, 8)); S2 = sectors(2)
WT = wind(lambda K: np.block([[UF(K), Z8], [Z8, UF(-K).T]]), S2)
check("b3 [T]/[F]", WT == [0, 0, 0], "control: the T-closure of FREEZE (FREEZE plus its T partner U_F(-k)^T, which is FREEZE's "
      "image under Theta = K) has W = 0: restoring T removes the family class, as the lemma says", f"W(FREEZE + T partner) {WT}")
def tavg(M): return sum(np.linalg.matrix_power(T3, j) @ M @ np.linalg.matrix_power(T3, j).T for j in range(3)) / 3
def Dk(K): return np.diag(np.exp(-1j * A @ K))
gates = [expm(-1j * tavg((lambda X: X + X.conj().T)(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))))) for _ in range(6)]
def Ucov(K):
    Pr_ = I8
    for j, Cg in enumerate(gates): Pr_ = Pr_ @ (Dk(K) @ Cg @ Dk(K).conj().T if j % 2 else Cg)
    return Pr_
Wc = wind(Ucov, S1); rc = {t: inter(Ucov, t) for t in ('T', 'chiral', 'inv')}
check("b4 [T]/[F]", Wc == [0, 0, 0] and all(rc[t][1] < 1e-9 for t in rc), "breaking T does NOT force W != 0: a random depth-6 "
      "turn-commuting cube-local circuit has no invertible on-cell T, chiral or inversion intertwiner, yet W = 0 (floquet-pi-slab "
      "B1). So T breaking is NECESSARY for the family class, not sufficient. The record "
      "arrow is a property of the records (register: 'the record set only grows, while the update is reversible'), it never "
      "enters the unitary U, so it cannot set U's determinant winding [S]", f"W {Wc}; cond T {rc['T'][1]:.0e} chiral "
      f"{rc['chiral'][1]:.0e} inv {rc['inv'][1]:.0e}")
# ================================================================ (c) FREEZE from fewest changes
print("== (c) is FREEZE's 'disagreeing half does not hop' a fewest-changes consequence?")
def UFid(K): return Pp @ UA(K) + Pm
def Urev(K): return Pp @ UA(K) + Pm @ UA(K).conj().T
Wc1 = {n: wind(f, S1) for n, f in (('CTWIST', Uc), ('U_A (run)', UA), ('FREEZE', UF), ('freeze, no quarter phase', UFid),
                                    ('reverse', Urev))}
okC1 = (Wc1['CTWIST'] == Wc1['U_A (run)'] == [2 * x for x in WF] and Wc1['FREEZE'] == Wc1['freeze, no quarter phase'] == WF
        and Wc1['reverse'] == [0, 0, 0] and np.linalg.norm(Ex @ T3 - T3 @ Ex) < 1e-12)
check("c1 [T]/[F]", okC1, "where W comes from: W(CTWIST) = W(U_A) = 2 W_F (eta_x commutes with T3 and swaps Pi+ and Pi-, so each "
      "half carries W_F); freezing the disagreeing half gives W_F, running it 2 W_F, reversing it 0. FREEZE does not create the "
      "winding, it HALVES one already present in the supplied CTWIST", " ".join(f"{n}: {tuple(v)}" for n, v in Wc1.items()))
ng = 6; grid = [np.array(x) for x in it.product(np.linspace(0, 2 * np.pi, ng, endpoint=False), repeat=3)]
def cost(U):     # per-tick probability that a mode leaves its site, and its cell (site-averaged), from the K = 0 Fourier block
    U0 = sum(U(K) for K in grid) / len(grid)
    return float(1 - np.mean(abs(np.diag(U0)) ** 2)), float(1 - np.mean(np.sum(abs(U0) ** 2, axis=0)))
TK = {'identity': (lambda K: I8), 'CL-1 tick eps 0.3': U1, 'CL-1 tick eps 0.05': (lambda K: U1(K, 0.05)), 'CTWIST': Uc,
      'U_A (run)': UA, 'FREEZE': UF, 'freeze, no quarter phase': UFid, 'reverse': Urev}
Cs = {n: cost(f) for n, f in TK.items()}; Wt = {n: Wc1.get(n, wind(f, S1)) for n, f in TK.items()}
nz = [n for n in TK if Wt[n] != [0, 0, 0]]
okC2 = (Cs['identity'] == (0.0, 0.0) and min(Cs[n][0] for n in nz) > Cs['CL-1 tick eps 0.05'][0]
        and Cs['freeze, no quarter phase'][0] < Cs['FREEZE'][0] and Cs['FREEZE'][1] < Cs['U_A (run)'][1]
        and abs(Cs['U_A (run)'][0] - Cs['reverse'][0]) < 1e-12 and abs(Cs['U_A (run)'][1] - Cs['reverse'][1]) < 1e-12)
check("c2 [T]/[F]", okC2, "fewest changes (per-tick probability a mode leaves its site / its cell): the global minimum is the "
      "identity (W = 0), and adopted-form W = 0 ticks go to zero cost continuously (eps -> 0) while every W != 0 tick tested costs "
      "O(1); cost(U) = cost(U^+) exactly on a sector, so 'run' (2 W_F) and 'reverse' (0) cost the same: the measure is blind to W. "
      "CTWIST moves every mode off its cell (zero K = 0 block). Inside the supplied CTWIST + Pi split freezing beats running (cell cost), but the cheapest frozen half is the identity, not FREEZE's i "
      "tau3 quarter phase (same W_F)", "; ".join(f"{n} {Cs[n][0]:.3f}/{Cs[n][1]:.3f} W{tuple(Wt[n])}" for n in TK))

# ================================================================ (d) minimal information among tick classes
print("== (d) least information among tick classes")
Wh = wind(lambda K: UF(K) @ U1(K), S1); Wh2 = wind(lambda K: UF(K) @ UF(K), S1)
okD = Wc == [0, 0, 0] and Wh == WF and Wh2 == [2 * x for x in WF] and wind(lambda K: I8, S1) == [0, 0, 0]
check("d1 [T]/[F]", okD, "W is additive under composition (W(F U_CL1) = W_F, W(F F) = 2 W_F), so the classes are cosets of Z[Z3]_0. "
      "The W = 0 class contains the identity, CL-1's tick and every circuit of turn-commuting cube-local gates (line b4); a "
      "nonzero class needs gates that are NOT individually turn-commuting (floquet-pi-slab B2). Any least-information / "
      "least-structure selection therefore picks W = 0: the wrong direction", f"W(F U_CL1) {Wh}, W(F F) {Wh2}, W(id) (0, 0, 0)")
print("   d2 [S] the minimal nonzero copy-flip element would be +-W_F (n = +-1), but no principle tested forces the copy-flip class")
P = dict(a_chirality=False, b_T_or_arrow=False, c_fewest_changes=False, d_least_info=False)
print(f"   synthesis (criteria_pre_run): W != 0 forced by {P} -> FAIL. Chirality and gappability hold at W = 0; T, chiral and "
      "axis-reversing symmetries (all present in CL-1's 24-rotation tick) each FORBID the family class, and T breaking is "
      "necessary, not sufficient; fewest changes and least information both select W = 0. A W != 0 tick remains a CL-1-level choice")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
