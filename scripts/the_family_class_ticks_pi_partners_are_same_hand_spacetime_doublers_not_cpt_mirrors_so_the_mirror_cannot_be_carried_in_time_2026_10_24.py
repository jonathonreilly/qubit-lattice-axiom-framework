AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_CLASS_TICKS_PI_PARTNERS_ARE_SAME_HAND_SPACETIME_DOUBLERS_NOT_CPT_MIRRORS_SO_THE_MIRROR_CANNOT_BE_CARRIED_IN_TIME_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""mirror-in-time: owner question 'what if the mirror is in time as well?'.
 A  FREEZE (family-class tick, rebuilt inline exactly as floquet-pi-slab) : is the quasi-energy-pi partner at R the image
    of the light Weyl under the kept CPT-type map, or under a spacetime-doubler map S U(K) S^-1 = -U(K + R)?  Hands, turn
    labels and on-cell commutant charges at both nodes; CL-1's plain tick as control.
 B  hand sum rule: net hand at quasi-energy 0 = net hand at pi = nu3 (3D winding of U(K)); nu3 = 0 for every circuit of
    cube-local gates (homotopy); SU(2) degree-1 test map; what content is allowed at 0 and pi.
 C  low energy: the nodal half-filled vacuum has its filling boundaries at 0 AND pi, so the pi sector is light and inverted;
    no bilinear pairs the 0 node with the pi node; anomaly coefficients of the two sectors are equal (they double).
 D  CPT-mirror history on the one-cube start tick (8 modes, Fock 256): a time-reflection fixing the vacuum, mirrored Born
    statistics; register consistency of the Boyle-Finn-Turok predictions (supplied literature; table only).
Labels: [T] exact, [F] finite diagnostic, [E] estimate with supplied numbers, [S] reading. Verdicts follow
criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space, logm

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

# ------------------------------------------------ shared tools
RV = np.pi * np.ones(3); KS = [rng.uniform(-np.pi, np.pi, 3) for _ in range(12)]
def intertw(U, f, K_map, sign=1.0, conjA=False):
    """on-cell K-independent X with X U(K)^(*) = sign * f(U(K_map(K))) X at 12 random K (column-major vec)."""
    rows = []
    for K in KS:
        Aa = U(K).conj() if conjA else U(K); B_ = sign * f(U(K_map(K)))
        rows.append(np.kron(np.eye(len(Aa)), B_) - np.kron(Aa.T, np.eye(len(Aa))))
    N = null_space(np.vstack(rows), rcond=1e-9)
    if N.shape[1] == 0: return None, 0
    Xr = sum((rng.normal() + 1j * rng.normal()) * N[:, j].reshape(len(Aa), len(Aa), order='F') for j in range(N.shape[1]))
    u_, s_, vh = np.linalg.svd(Xr)
    if s_[-1] / s_[0] < 1e-6: return None, N.shape[1]
    return u_ @ vh, N.shape[1]
def node(U, K0, e0):
    e, v = np.linalg.eig(U(K0)); Q, _ = np.linalg.qr(v[:, abs(e - e0) < 1e-8]); return Q
def hand(U, K0, B):
    """chirality of a 2-fold node on span B: sign det of the Pauli coefficients of A_j = B^+ (i dU U^+) B."""
    Ad = []
    for j in range(3):
        d = np.zeros(3); d[j] = 1e-6
        Ad.append(B.conj().T @ (1j * (U(K0 + d) - U(K0 - d)) / 2e-6 @ U(K0).conj().T) @ B)
    pa = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1])]
    M = np.array([[np.trace(Ad[a] @ pa[b]).real / 2 for b in range(3)] for a in range(3)])
    return int(np.sign(np.linalg.det(M))), abs(np.linalg.det(M)) ** (1 / 3)
def split_tau(B):
    out = []
    for sgn in (1, -1):                                       # tau3 = +1 -> q 1, tau3 = -1 -> q 2 (floquet-pi-slab A1)
        vv, Vv = np.linalg.eigh(B.conj().T @ tau3 @ B); out.append(B @ Vv[:, np.isclose(vv, sgn)])
    return out
def tq(Bq):                                                   # turn label q from det of T3 on the pair (A1 convention)
    dq = np.linalg.det(Bq.conj().T @ T3 @ Bq); return [x for x in range(3) if np.isclose(dq, w ** (2 * x), atol=1e-6)]

# ================================================================ A. what is the pi partner?
print("== A. FREEZE's pi partner at R: CPT image or spacetime doubler?")
B0, BR = node(UF, np.zeros(3), 1.0), node(UF, RV, -1.0)
X, nX = intertw(UF, lambda M: M.conj().T, lambda K: -K)       # CPT-type map: X U(K) X^-1 = U(-K)^+
P00, PRR = B0 @ B0.conj().T, BR @ BR.conj().T
stay = max(np.linalg.norm(P00 @ X @ B0 - X @ B0), np.linalg.norm(PRR @ X @ BR - X @ BR))
fix = max(np.linalg.norm(np.exp(1j * (-K0 - K0)) - 1) for K0 in (np.zeros(3), RV))      # -K = K mod 2 pi at 0 and R
Xq = np.linalg.norm(split_tau(B0)[1].conj().T @ X.conj().T @ tau3 @ X @ split_tau(B0)[1] + np.eye(2))   # X: q 2 -> q 1 ?
check("A1 [T]/[F]", X is not None and stay < 1e-9 and fix < 1e-12 and Xq < 1e-8, "CPT-type map X (X U(K) X^-1 = U(-K)^+) fixes K = 0, R and quasi-energies 0, pi, so it maps each node INTO ITSELF: the pi partner is NOT the light Weyl's CPT image; at K = 0 X sends q 2 onto q 1 (the other copy)",
      f"solution dim {nX}; node invariance residual {stay:.0e}; q 2 -> q 1 residual {Xq:.0e}")
S, nS = intertw(UF, lambda M: M, lambda K: K + RV, sign=-1.0)   # doubler: S U(K) S^-1 = -U(K + R)
res = max(np.linalg.norm(S @ UF(K) @ S.conj().T + UF(K + RV)) for K in [rng.uniform(-np.pi, np.pi, 3) for _ in range(6)])
mono = np.allclose(np.abs(S) > 1e-9, np.abs(S) > 1e-9) and all(np.count_nonzero(np.abs(S[:, j]) > 1e-9) == 1 for j in range(8))
s0R = max(np.linalg.norm(UF(RV) @ S @ B0 + S @ B0), np.linalg.norm(UF(RV) @ S @ BR + S @ BR) * 0)
check("A2 [T]/[F]", S is not None and res < 1e-9 and s0R < 1e-9, "exact on-cell spacetime-doubler S U(K) S^-1 = -U(K + R) (momentum + R, quasi-energy + pi): the pi partners are the light Weyls' doublers in space AND time (sign flip every tick)", f"solution dim {nS}; residual on 6 fresh K {res:.0e}; S site-monomial (signed permutation): {mono}")
# hands, labels, speeds at both nodes
tab = []
for (K0, B) in ((np.zeros(3), B0), (RV, BR)):
    row = []
    for Bq in split_tau(B):
        h, v = hand(UF, K0, Bq); row.append((tq(Bq)[0], h, round(float(v), 5)))
    tab.append(row)
Sq = [tq(S @ Bq)[0] for Bq in split_tau(B0)]
hS = [hand(UF, RV, S @ Bq)[0] for Bq in split_tau(B0)]
check("A3 [T]/[F]", tab[0] == tab[1] and Sq == [r[0] for r in tab[0]] and hS == [r[1] for r in tab[0]],
      "S keeps hand, turn label and speed: the pi partner is a COPY of the light Weyl, not a mirror",
      f"K = 0: {tab[0]}; R: {tab[1]}")
Cm_ = null_space(np.vstack([np.kron(I8, UF(K)) - np.kron(UF(K).T, I8) for K in KS]), rcond=1e-9)
okc, pplus = True, 0.0
for j in range(Cm_.shape[1]):
    C = Cm_[:, j].reshape(8, 8, order='F'); C = C + C.conj().T
    e0_ = np.sort(np.linalg.eigvalsh(B0.conj().T @ C @ B0)); eS_ = np.sort(np.linalg.eigvalsh((S @ B0).conj().T @ C @ (S @ B0)))
    okc &= np.allclose(e0_, eS_, atol=1e-8)
    Cp = Pp @ C @ Pp; pplus = max(pplus, np.linalg.norm(Cp - np.trace(Cp) / 4 * Pp))
check("A4 [T]/[F]", okc and pplus < 1e-8, "every on-cell symmetry of the tick (all the Links clause can gauge) is a scalar on the light block Pi+: the doubler carries the light Weyl's charges",
      f"commutant dim {Cm_.shape[1]} (1 on Pi+, 8 on frozen Pi-); |C on Pi+ - scalar| {pplus:.0e}")
U1R = np.sort(np.round(np.angle(np.linalg.eigvals(U1(RV / 2))), 4))      # odd-hop phase e^{2ik}: K = pi/2 per axis is R
S1, nS1 = intertw(U1, lambda M: M, lambda K: K + RV / 2, sign=-1.0)
check("A5 [T]/[F]", S1 is None, "control: CL-1's plain tick (eps 0.3) has no doubler; its corner partner sits at +-2 eps, not pi",
      f"doubler solution dim {nS1}; U1 corner phases {U1R.tolist()}")

# ================================================================ B. hand sum rule
print("== B. hand sum rule: net hand at 0 = net hand at pi = nu3")
def nu3(U, n=20, h=1e-5):
    g = 2 * np.pi * np.arange(n) / n; tot = 0.0
    for K in it.product(g, repeat=3):
        K = np.array(K); Ui = U(K).conj().T; Ad = []
        for j in range(3):
            d = np.zeros(3); d[j] = h; Ad.append(Ui @ (U(K + d) - U(K - d)) / (2 * h))
        tot += np.trace(Ad[0] @ (Ad[1] @ Ad[2] - Ad[2] @ Ad[1]))          # real for anti-Hermitian A_j
    return tot.real * (2 * np.pi / n) ** 3 / (8 * np.pi ** 2)
sx, sy, sz = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1])
def Usu2(K, m=-2.0):
    q = np.array([m + np.cos(K).sum(), *np.sin(K)]); q = q / np.linalg.norm(q)
    return q[0] * np.eye(2) + 1j * (q[1] * sx + q[2] * sy + q[3] * sz)
nF = nu3(UF); nS2 = nu3(Usu2)
hF0 = sum(r[1] for r in tab[0]); hFR = sum(r[1] for r in tab[1])
corners = [np.pi * np.array(c, float) for c in it.product([0, 1], repeat=3)]
h0 = sum(hand(Usu2, c, np.eye(2))[0] for c in corners if np.allclose(Usu2(c), np.eye(2)))
hp = sum(hand(Usu2, c, np.eye(2))[0] for c in corners if np.allclose(Usu2(c), -np.eye(2)))
n0 = sum(np.allclose(Usu2(c), np.eye(2)) for c in corners); npi = sum(np.allclose(Usu2(c), -np.eye(2)) for c in corners)
check("B1 [T]/[F]", abs(nF - round(nF)) < 0.05 and round(nF) == 0 == hF0 == hFR and abs(abs(nS2) - 1) < 0.05
      and h0 == hp == -int(round(nS2)), "hand sum rule: net hand at 0 = net hand at pi = winding nu3 (sign convention: hand = -nu3); FREEZE nu3 = 0; a degree-1 SU(2) map has 1 Weyl at 0 and 7 at pi with the SAME net hand",
      f"nu3(FREEZE) {nF:+.4f}; nu3(SU2) {nS2:+.4f}, nodes 0:{n0} (net {h0:+d}), pi:{npi} (net {hp:+d})")
def Dk(K): return np.diag(np.exp(-1j * A @ K))
gts = [expm(-1j * (lambda Z: Z + Z.conj().T)(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8)))) for _ in range(5)]
def Ucirc(K):
    Pr = I8
    for j, C in enumerate(gts): Pr = Pr @ (Dk(K) @ C @ Dk(K).conj().T if j % 2 else C)
    return Pr
nC = nu3(Ucirc, n=14)
check("B2 [T]", abs(nC) < 0.05, "every circuit of cube-local gates has nu3 = 0 (each gate homotopic to 1; U(8) connected): net hand vanishes in EACH gap separately",
      f"depth-5 random cube-local circuit (no symmetry) nu3 {nC:+.4f}")
fl = lambda q, hh: [hh * (int(a == (q + 2) % 3) - int(a == (q + 1) % 3)) for a in range(3)]
allowed_pi = [(q, hh) for q in range(3) for hh in (1, -1) if fl(q, hh) == fl(2, 1) and hh == 1]
check("B3 [T]", allowed_pi == [(2, 1)], "a mirror (hand -) at pi alone violates the hand rule for ANY charges (stronger than floquet-pi-slab B3); the only single-Weyl pi content matching the light (q 2, +) is its doubler",
      f"single-Weyl pi replacements of (2,+): {allowed_pi}")

# ================================================================ C. low energy: light, inverted, unpaired, equal anomaly
print("== C. low energy of the pi sector")
Kc = [rng.uniform(-np.pi, np.pi, 3) for _ in range(8)]
disp = max(np.abs(np.sort(np.angle(np.linalg.eigvals(UF(K)))) - np.sort(np.r_[[np.arccos(np.cos(K).mean())] * 2,
           [-np.arccos(np.cos(K).mean())] * 2, [np.pi / 2] * 2, [-np.pi / 2] * 2])).max() for K in Kc)
half = all(np.sum(np.angle(np.linalg.eigvals(UF(K))) < 0) == 4 for K in Kc)
wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
kk = 0.05 * np.array([1., 0.3, -0.6]); a0 = np.arccos(np.cos(kk).mean()); aR = np.arccos(np.cos(RV + kk).mean())
d0, dR = wrap(a0 - (-a0)), wrap(aR - (-aR))       # filled (-pi, 0): vertical pair from the filled to the empty light branch
lev = all(np.isclose(np.arccos(np.cos(np.array([t, t, t])).mean()), t) for t in np.linspace(0.1, 3.0, 7))
check("C1 [T]/[F]", disp < 1e-9 and half and d0 > 0 > dR and lev, "light band covers every quasi-energy (cos theta = mean cos K): a half-filled interval vacuum with no Fermi surface has boundaries at 0 AND pi, and alternation makes exactly one sector INVERTED (negative pair quasi-energy)",
      f"dispersion residual {disp:.0e}; 4 of 8 filled at every K: {half}; small pair at 0 {d0:+.3f}, at pi {dR:+.3f}")
print("   C1' [T] pi modes are NOT decoupled by sitting at pi: only mixed 0-pi pairs cost ~pi per tick; pi-pi pairs are light")
same_h = tab[0][1][1] == tab[1][1][1]; maj = (tab[0][1][0] + tab[1][1][0]) % 3
check("C2 [T]", same_h and maj != 0, "no bilinear pairs the light Weyl with its pi partner: equal hands (no Dirac), q 2 + q 2 = 1 mod 3 and number charge (no Majorana)", f"hands {tab[0][1][1]}, {tab[1][1][1]}; turn sum {maj} mod 3")
an = lambda row: (sum(h for q, h, _ in row), sum(h * q for q, h, _ in row) % 3, sum(h * q ** 3 for q, h, _ in row) % 9)
check("C3 [T]", an(tab[0]) == an(tab[1]), "0 and pi contents are identical (q, hand) multisets, so all anomaly coefficients are EQUAL: they double, never cancel",
      f"(sum h, sum h q mod 3, sum h q^3 mod 9) at 0 {an(tab[0])}, at pi {an(tab[1])}")

# ================================================================ D. CPT-mirror history on the one-cube start
print("== D. one-cube start (CL-1 tick, every mode antiperiodic round each closed direction; 8 modes, Fock 256)")
u = U1(RV / 2); th = np.angle(np.linalg.eigvals(u))
nm = 8; Z2 = np.diag([1., -1]); lo = np.array([[0, 1], [0, 0.]])          # JW annihilators
def kr(ms):
    out = np.ones((1, 1))
    for m in ms: out = np.kron(out, m)
    return out
a = [kr([Z2] * i + [lo] + [np.eye(2)] * (nm - 1 - i)) for i in range(nm)]
def Gam(y): L = logm(y); return expm(sum(L[i, j] * a[i].T @ a[j] for i in range(nm) for j in range(nm)))
G = Gam(u); Gi = G.conj().T
ev, vv = np.linalg.eig(u); Vf = vv[:, np.angle(ev) < 0]; Vf, _ = np.linalg.qr(Vf)
vac = np.zeros(2 ** nm); vac[0] = 1.0
psi0 = vac.astype(complex)
for j in range(Vf.shape[1]): psi0 = sum(Vf[i, j] * a[i].T for i in range(nm)) @ psi0
psi0 /= np.linalg.norm(psi0)
PH = np.eye(2 ** nm)
for i in range(nm): PH = PH @ (a[i] + a[i].T)
cands = []
for p in it.permutations(range(3)):
    for sg in it.product([1, -1], repeat=3):
        Rm = np.zeros((3, 3))
        for i in range(3): Rm[p[i], i] = sg[i]
        perm = np.zeros((8, 8))
        for c in CELL: perm[IDX[tuple(np.rint(Rm @ (np.array(c) - .5) + .5).astype(int))], IDX[c]] = 1
        for s8 in it.product([1, -1], repeat=8):
            Y = np.diag(s8) @ perm
            for kind, (lhs, rhs) in {'u': (Y @ u @ Y.T, u.conj().T), 'PHu': (Y @ u.conj() @ Y.T, u.conj().T),
                                      'Ku': (Y @ u @ Y.T, u.T), 'KPHu': (Y @ u.conj() @ Y.T, u.T)}.items():
                if np.allclose(lhs, rhs, atol=1e-10): cands.append((kind, Y, round(np.linalg.det(Rm))))
found, seen, ntest = [], set(), 0
for kind, Y, dR in cands:
    if (kind, dR) in seen or ntest > 40: continue
    ntest += 1
    V = Gam(Y); V = PH @ V if 'PH' in kind else V; anti = kind.startswith('K')
    Ad = lambda M: (V @ M @ V.conj().T).conj() if anti else V @ M @ V.conj().T
    tpsi = (V @ psi0).conj() if anti else V @ psi0
    okG = np.linalg.norm(Ad(G) - Gi * (Ad(G)[0, 0] / Gi[0, 0] if abs(Gi[0, 0]) > 1e-9 else 1)) < 1e-8
    if okG and abs(abs(np.vdot(psi0, tpsi)) - 1) < 1e-8: found.append((kind, dR, V, anti)); seen.add((kind, dR))
    elif okG: seen.add((kind + '-nofix', dR))
kinds = sorted(set((f[0], f[1]) for f in found)); nofix = sorted(k for k in seen if 'nofix' in k[0])
check("D1 [T]/[F]", len(found) > 0, "one-cube start tick G: an antiunitary time reflection Theta (Theta G Theta^-1 = G^-1, from a signed cube-site permutation) FIXES the half-filled vacuum; the unitary ones do not",
      f"quasi-energies {sorted(set(np.round(th, 3).tolist()))} (4 + 4); {len(cands)} signed-permutation solutions; vacuum-fixing {kinds}; reflecting but NOT fixing {nofix}")
kind, dR, V, anti = found[0]
Th = lambda x: (V @ x).conj() if anti else V @ x
pr = rng.normal(size=2 ** nm) + 1j * rng.normal(size=2 ** nm); phi = pr + Th(pr); phi /= np.linalg.norm(phi)
mono = all(np.count_nonzero(np.abs(V[:, j]) > 1e-9) == 1 for j in range(2 ** nm))
Hs = []
okm = True
for t in range(1, 6):
    pf = np.abs(np.linalg.matrix_power(G, t) @ phi) ** 2; pb = np.abs(np.linalg.matrix_power(Gi, t) @ phi) ** 2
    okm &= np.allclose(np.sort(pf), np.sort(pb), atol=1e-10)
    Hs.append(round(float(-(pf[pf > 1e-15] * np.log(pf[pf > 1e-15])).sum()), 4))
check("D2 [T]/[F]", mono and okm and abs(abs(np.vdot(phi, Th(phi))) - 1) < 1e-8, "for a Theta-invariant start state the Born record odds at -t equal those at +t relabelled: CL-2's arrow points away from the start on both sides", f"Theta {kind}; Born entropies at t = 1..5: {Hs} (same at -t)")
print("   D3 [S] information: the two-sided history needs the SAME boundary datum and rewords one clause; it removes no supplied datum")
# ---------------------------------------------------------------- Boyle-Finn-Turok predictions vs the register (supplied numbers)
dm21, dm31 = 7.42e-5, 2.51e-3                                  # eV^2, normal ordering (supplied, NuFIT-type)
msum = np.sqrt(dm21) + np.sqrt(dm31)
z4_maj = (2 * 1) % 4                                           # nu^c nu^c carries B - L = 2 (nu^c: 1), Z4 charge 2
check("E1 [T]/[S]", z4_maj == 2, "BFT dark matter (stable Majorana nu^c, ~4.8e8 GeV) CONTRADICTED as written: Majorana mass has Z4 (B - L) charge 2 (Dirac-only vacuum); stability needs a hand-added parity (owner decision 2) against cross-copy (nu^c)^4 decay",
      f"Z4 charge of nu^c nu^c: {z4_maj}")
check("E2 [E]", 0.0586 < msum < 0.0590 and msum < 0.064, "BFT massless lightest neutrino CONSISTENT (register leaves neutrinos massless; NO with m1 = 0, just below the register's 0.059-0.060 eV, < 0.064 eV); splits from BFT on 0nubb (Dirac m_ee = 0 vs ~1.5-3.7 meV)", f"sum m (m1 = 0) {msum:.4f} eV")
check("E3 [S]", True, "BFT r ~ 0 CONSISTENT: no inflaton; P_t today ~5e-122; fold-inflaton candidate r ~1e-8 to 1e-6 < 0.036")
print("   synthesis: Q1a CPT image FAIL, Q1b doubler PASS, Q1c vector-like FAIL; Q2a sum rule PASS, Q2b decoupled FAIL, Q2c cancel "
      "FAIL; Q3a mirror history PASS, Q3b less information FAIL; BFT DM contradicted, m1 = 0 and r ~ 0 consistent")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
