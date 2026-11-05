AUDIT_INPUT_PATHS = ('docs/A_CIRCUIT_SLAB_PUTS_ITS_MIRROR_IN_THE_OTHER_COPY_ONLY_THROUGH_A_NONZERO_TURN_GRADED_WINDING_WHICH_FORCES_EQUAL_FLOW_AT_QUASI_ENERGY_PI_AND_IS_SET_BY_TERMINATION_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""floquet-pi-slab: the copy-flip slab as a Floquet CIRCUIT with wall modes allowed at quasi-energy 0 and pi.
 A  FREEZE (twist-local-single, rebuilt inline) on its turn axis K = kappa (1,1,1): turn-sector winding W of det U_a and the
    eigenphase flows through 0 and pi.
 B  sum rule F_0 = F_pi = W (Z[Z3]); W = 0 for every circuit of cube-local gates that commute with the axis turn; corollaries.
 C  coupled-layer slab: layers alternate FREEZE and its inverse, turn-commuting label gates on alternate bonds; bulk gap at
    0 and pi, wall content at (K = 0, 0) and (R, pi), flows; Ls parity and the bond pattern decide the far copy.
 D  bookkeeping (anomaly-family-count index, Omega twist k = -q_mirror), shared light charge, synthesis.
Labels: [T] exact, [F] finite diagnostic, [S] reading. Supplied: FREEZE, the alternation, the label bond pattern, g, Ls,
free fields. Every line reports a RESULT; the synthesis verdict follows criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space

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

# ------------------------------------------------ tools on the axis
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

# ================================================================ A. FREEZE on its turn axis
print("== A. FREEZE on the turn axis K = kappa (1,1,1)")
Kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)]
uni = max(np.linalg.norm(UF(K) @ UF(K).conj().T - I8) for K in Kr)
axc = max(np.linalg.norm(T3 @ UF(k * np.ones(3)) @ T3.T - UF(k * np.ones(3))) for k in (0.3, 1.7, 2.9))
lab = max(np.linalg.norm(T3 @ X @ T3.T - X) for X in (Pp, tau3, chi))
nod = []
for K0 in (0.0, np.pi):
    for Pq in (Pq1, Pq2):
        vv, Bv = np.linalg.eigh(Pq); B = Bv[:, vv > .5]; dq = np.linalg.det(B.conj().T @ T3 @ B)
        nod.append(([x for x in range(3) if np.isclose(dq, w ** (2 * x))], np.round(np.angle(np.linalg.eigvals(B.conj().T @ UF(K0 * np.ones(3)) @ B)) % (2 * np.pi), 6).tolist()))
okA1 = (uni < 1e-12 and axc < 1e-12 and lab < 1e-12 and np.allclose(np.linalg.matrix_power(T3, 3), I8) and
        [n[0] for n in nod] == [[1], [2], [1], [2]] and all(np.allclose(np.cos(np.array(n[1])), c) for n, c in zip(nod, (1, 1, -1, -1))))
check("A1 [T]/[F]", okA1, "FREEZE rebuilt: unitary; the site-gauged C3 turn T3 (T3^3 = 1) is a symmetry on the axis and keeps Pi+, "
      "tau3, chi; at K = 0 the q 1 (tau3 +1) and q 2 (tau3 -1) Weyl pairs sit at quasi-energy 0, at R at pi",
      f"unitarity {uni:.0e}, axis {axc:.0e}, labels {lab:.0e}")
SEC1 = sectors(1); WF = wind(UF, SEC1); F0 = flow(UF, SEC1, 0, 0); Fp = flow(UF, SEC1, np.pi, np.pi)
ks = np.linspace(0, 2 * np.pi, 2001); g0 = gp = 9.
for k in ks:
    thx = np.angle(np.linalg.eigvals(UF(k * np.ones(3)))); d0 = min(k, 2 * np.pi - k); dp = abs(k - np.pi)
    g0 = min(g0, abs(thx).min() / max(d0, 1e-9)) if d0 > 1e-6 else g0
    gp = min(gp, (np.pi - abs(thx)).min() / max(dp, 1e-9)) if dp > 1e-6 else gp
check("A2 [T]/[F]", WF == F0 == Fp == [-2, 1, 1] and min(g0, gp) > 0.05, "FREEZE's turn-graded winding is NONZERO: W = (-2, 1, 1) "
      "over sectors (1, w, w^2), and the axis flow through 0 (K = 0 node) and through pi (R node) both equal W; no other axis "
      "crossing (|theta| / distance-to-node bounded below)", f"W {WF}, F_0 {F0}, F_pi {Fp}; min slope ratio {min(g0, gp):.2f}")

# ================================================================ B. sum rule and the covariant-gate lemma
print("== B. the Floquet sum rule F_0 = F_pi = W")
def tavg(M): return sum(np.linalg.matrix_power(T3, j) @ M @ np.linalg.matrix_power(T3, j).T for j in range(3)) / 3
def Dk(K): return np.diag(np.exp(-1j * A @ K))
gates = [expm(-1j * tavg((lambda X: X + X.conj().T)(rng.normal(size=(8, 8)) + 1j * rng.normal(size=(8, 8))))) for _ in range(7)]
def Ucov(K):
    Pr = I8
    for j, C in enumerate(gates): Pr = Pr @ (Dk(K) @ C @ Dk(K).conj().T if j % 2 else C)
    return Pr
dcov = max(np.linalg.norm(T3 @ Dk(k * np.ones(3)) @ T3.T - Dk(k * np.ones(3))) for k in (0.4, 2.2))
Wc = wind(Ucov, SEC1)
check("B1 [T]", dcov < 1e-12 and Wc == [0, 0, 0], "lemma: a cube-local gate that commutes with the axis turn has constant det on "
      "every turn sector (even tiling: C; odd tiling: D(K) C D(K)^+ with D(kappa) commuting with T3 on the axis), so ANY circuit "
      "of such gates (and any exp(-i t H) with H turn-symmetric) has W = 0: F_0 = F_pi = 0 SEPARATELY and q_mirror = q_light in "
      "each gap (copy-flip-slab D3 holds gap by gap)", f"[T3, D] {dcov:.0e}; depth-7 random covariant circuit W {Wc}")
print("   B2 [T] corollary: W_F != 0 (A2), so FREEZE is NOT a product of cube-local gates each commuting with the (111) turn, at "
      "ANY depth (exact upgrade of twist-local-single A3, which searched depths 5-9 for all 12 rotations)")
single = [form(q, h) for q in range(3) for h in (1, -1)]
tgt = [a + b for a, b in zip(form(2, 1), form(1, -1))]
check("B3 [T]", tgt == WF and tgt not in single and form(2, 1) != form(1, -1), "consequences: (i) light q 2 at 0 "
      "with the q 1 mirror ONLY at pi is impossible (F_0 = f(2,+) != f(1,-) = F_pi, for any W); (ii) light q 2 and mirror q 1 both "
      "at 0 give F_0 = W = (-2,1,1), so the pi gap must carry the SAME flow, which is no single-Weyl flow: >= 2 extra Weyls at pi "
      "per family (a forced pi doubling); (iii) W = 0 circuits recover q_mirror = q_light", f"f(2,+)+f(1,-) = {tgt}")

# ================================================================ C. the coupled-layer slab
print("== C. coupled-layer slab: layers F, F^+, F, ...; label gates q 1 on bonds (2j,2j+1), q 2 on (2j+1,2j+2)")
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
def bgap(g, n, alt=True):
    gr = np.linspace(-np.pi, np.pi, n, endpoint=False); a0 = ap = 9.
    for K in it.product(gr, repeat=3):
        for k in gr:
            thx = np.angle(np.linalg.eigvals(bulk(np.array(K), k, g, alt))); a0 = min(a0, abs(thx).min()); ap = min(ap, (np.pi - abs(thx)).min())
    return a0, ap
g = 0.5
G0, Gp = bgap(g, 12); win = {gg: round(min(bgap(gg, 6)), 2) for gg in (0.2, 0.8, 1.2, 1.4)}
check("C1 [F]", min(G0, Gp) > 0.3 and win[0.2] > 0.1 and win[0.8] > 0.1, "the alternating bulk (period 2, Bloch k_l) is gapped at "
      "BOTH 0 and pi for g = 0.5 on a 12^4 grid that contains K = 0 and R; a window of g, not a tuned value",
      f"gap at 0 {G0:.3f}, at pi {Gp:.3f}; min gap on 6^4 vs g {win}")
SE2 = sectors(2); ax0 = [wind(lambda K, k=k: bulk(K, k, g, alt=False), SE2, 200) for k in (0.0, 1.3)]
SE6 = sectors(6); WallF = wind(lambda K: slab(K, 6, g, [0] * 6, ('both', 'both')), SE6)
check("C2 [T]/[F]", WallF == [6 * x for x in WF] and all(x == [2 * y for y in WF] for x in ax0), "the alternation is forced by the bulk gap: an all-F stack has "
      "W = Ls W_F (grows with Ls; walls hold a bounded number of Weyls), and its bulk carries 2 W_F per two layers at every k_l, so it is "
      "gapless at 0 and pi on the axis (a nonzero sector winding drives an eigenphase through every eps)", f"all-F Ls 6 W {WallF}; all-F bulk sector winding per 2 layers at k_l = 0, 1.3: {ax0}")
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
res = {}
for Ls in (7, 13, 6, 12):
    SE = sectors(Ls); U = lambda K, Ls=Ls: slab(K, Ls, g); Wn = np.kron(np.diag([1.] * (Ls // 2) + [0.] * (Ls - Ls // 2)), I8)
    res[Ls] = dict(W=wind(U, SE), F0=flow(U, SE, 0, 0), Fp=flow(U, SE, np.pi, np.pi), Fn=flow(U, SE, 0, 0, W=Wn),
                   w0=walls(Ls, 0., 0.), wp=walls(Ls, np.pi, np.pi))
okC3 = all(res[L]['w0'] == res[L]['wp'] == [(0, 2, 1), (L - 1, 1, -1)] and res[L]['W'] == res[L]['F0'] == res[L]['Fp'] == WF
           and res[L]['Fn'] == form(2, 1) for L in (7, 13))
check("C3 [T]/[F]", okC3, "ODD Ls: near wall holds the light q 2 (hand +1) at (K = 0, 0) AND at (R, pi); far wall holds the mirror "
      "q 1 (hand -1, the other copy) at both; F_0 = F_pi = W = W_F, near-wall flow f(2,+). The copy-flipped mirror EXISTS on a "
      "bulk-gapped circuit slab", f"Ls 7: 0: {res[7]['w0']} pi: {res[7]['wp']}; W {res[7]['W']}, near F_0 {res[7]['Fn']}")
okC4 = all(res[L]['w0'] == res[L]['wp'] == [(0, 2, 1), (L - 1, 2, -1)] and res[L]['W'] == res[L]['F0'] == res[L]['Fp'] == [0, 0, 0] for L in (6, 12))
check("C4 [T]/[F]", okC4, "EVEN Ls (same bulk): far wall holds q 2 (q_mirror = q_light), W = F_0 = F_pi = 0: the far copy is a "
      "TERMINATION property (net number of F minus F^+ layers), not a bulk one", f"Ls 6: {res[6]['w0']}; W {res[6]['W']}")
wb = walls(7, 0., 0., bonds=('both', 'none')); Wb = wind(lambda K: slab(K, 7, g, bonds=('both', 'none')), sectors(7))
check("C5 [F]", wb == [(6, 2, 1), (6, 1, -1)] and Wb == WF, "a second bond pattern (both labels on even bonds) with the same "
      "odd Ls puts the whole FREEZE pair on the far wall (same W): the near/far split is a chosen label bond pattern", f"{wb}; W {Wb}")
gsl = 9.
for K in it.product(np.linspace(-np.pi, np.pi, 6, endpoint=False), repeat=3):
    K = np.array(K); thx = np.angle(np.linalg.eigvals(slab(K, 7, g)))
    if not np.allclose(K, 0): gsl = min(gsl, abs(thx).min())
    if not np.allclose(np.cos(K), -1): gsl = min(gsl, (np.pi - abs(thx)).min())
check("C6 [F]", gsl > 0.1, "open Ls 7 slab: no other state at 0 or pi on a 6^3 wall grid off the nodes (the wall Weyls are the "
      "only in-gap content)", f"min gap off nodes {gsl:.3f}")

# ================================================================ D. bookkeeping
print("== D. family-count bookkeeping (anomaly-family-count index, Omega twist k = -q_mirror)")
Ns = range(1, 10)
def far_coeffs(N, t): return dict(Z3_spin10=(-2 * N * t) % 3, Z3_grav=(-16 * N * t) % 3, Z3_cubed=(-16 * N * t ** 3) % 9)
def allowed(lights, mirrors, mdoub=4):
    if len(set(mirrors)) != 1: return None
    k = (-mirrors[0]) % 3; out = []
    for N in Ns:
        far = any(v for v in far_coeffs(N * len(mirrors), (mirrors[0] + k) % 3).values())
        if (N * mdoub * sum((q + k) % 3 for q in lights)) % 3 == 0 and not far: out.append(N)
    return out
odd = [q for (_, q, h) in res[7]['w0'] + res[7]['wp'] if h > 0], [q for (_, q, h) in res[7]['w0'] + res[7]['wp'] if h < 0]
evn = [q for (_, q, h) in res[6]['w0'] + res[6]['wp'] if h > 0], [q for (_, q, h) in res[6]['w0'] + res[6]['wp'] if h < 0]
aO, aE, aR = allowed(*odd), allowed(*evn), allowed([1, 1], [2, 2])
check("D1 [T]", aO == [3, 6, 9] and aE == list(Ns) and aR == [3, 6, 9], "odd-Ls slab (lights {2 at 0, 2 at pi}, mirrors {1, 1}): "
      "N_f = 0 mod 3 is the anomaly-free set; the pi doubling keeps the mod 3 because the node count 2 is prime to 3; the "
      "reflected slab (light 1, mirror 2) gives the same; even Ls: every N_f. Smallest nonzero 3, but 3 over 6 is still supplied",
      f"odd {odd} -> {aO}; even {evn} -> {aE}; reflected {aR}")
check("D2 [T]", set(odd[0]) == {2}, "all light Weyls (both nodes, every stacked family) carry ONE turn charge q 2, so the turn-CP "
      "lemma (J = 0 only for turn-invariant masses on a turn-CHARGED triplet) does not force J = 0; J != 0 allowed, not supplied")
print("   D3 [S] freeze-mirror-smg: on FREEZE's bare label doublet the T-invariant charge-4 mirror term first exists at N_f = 4 "
      "(C(N_f,4)); the Omega used here is anomaly-family-count's per-family 16 pairing. At N_f = 3 the mirror gap needs the 16.")
P1, P2, P3, P4, P5 = okC3 and min(G0, Gp) > 0.3, WF == F0 == Fp and Wc == [0, 0, 0], False, aO == [3, 6, 9], set(odd[0]) == {2}
print(f"   synthesis (criteria_pre_run): P1 slab exists {P1}, P2 sum rule {P2}, P3 forced {P3}, P4 mod 3 {P4}, P5 one light charge, "
      f"pi light = FREEZE's own pinned node {P5} -> FAIL at P3 only: Ls parity and the bond pattern choose the far copy")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
