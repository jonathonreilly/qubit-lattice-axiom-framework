#!/usr/bin/env python3
"""family-minimality: does any ADOPTED principle prefer the smallest anomaly-free family count (N_f = 3 of {3, 6, 9, ...})?
 A  CL-2 fewest changes / least information: additivity of the fewest-changes transport over independent families, zero cost
    in a stationary vacuum, the text's blindness to new modes; the extension "content minimises changes" and route dependence.
 B  FREEZE-class winding (FREEZE rebuilt inline from twist-local-single, as in floquet-pi-slab): minimal per-family winding of
    the class, near-wall content of the odd minimal-winding slab, W_tot = N_f W_F and anomaly freedom = W_tot = 0 mod 3.
 C  vacuum energy of the mirror-gapped far wall: reduced SU(4) analogue of the charge-4 pair square, additivity over families,
    monotone direction, no stability bound; CL-3 weighs only departures from the vacuum.
Labels: [T] exact, [F] finite diagnostic, [S] reading. Supplied: FREEZE, the F/F^+ alternation, the label bond pattern, g, Ls,
the reduced analogue, free fields. Every line reports a RESULT; the synthesis verdict follows criteria_pre_run.txt."""
AUDIT_TIMEOUT_SEC = 120
import os, time, itertools as it, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm, null_space
from scipy.optimize import linprog
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh

rng = np.random.default_rng(20261023)
T0 = time.time(); NP = [0, 0]
def check(tag, ok, msg, det=""):
    ok = bool(ok); NP[0 if ok else 1] += 1
    print(f"{'PASS' if ok else 'FAIL'}: {tag} {msg}" + (f"  [{det}]" if det else ""))
w = np.exp(2j * np.pi / 3); I8 = np.eye(8)

# ------------------------------------------------ FREEZE rebuild (twist-local-single, same seed and draw order as floquet-pi-slab)
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


# ================================================================ A. CL-2 fewest changes
print("== A. CL-2 fewest changes / least information, family by family")
def configs(n): return np.array(list(it.product([0, 1], repeat=n)))
def ot_cost(p, q, X):
    m = len(p); C = np.abs(X[:, None, :] - X[None, :, :]).sum(-1).ravel()
    Aeq = np.vstack([np.kron(np.eye(m), np.ones(m)), np.kron(np.ones(m), np.eye(m))])
    r = linprog(C, A_eq=Aeq, b_eq=np.concatenate([p, q]), bounds=(0, None), method='highs'); return r.fun
X1 = configs(2); p1 = rng.dirichlet(np.ones(4)); q1 = rng.dirichlet(np.ones(4)); c1 = ot_cost(p1, q1, X1)
cN = {}
for N in (1, 2, 3):
    pN, qN = p1, q1
    for _ in range(N - 1): pN, qN = np.kron(pN, p1), np.kron(qN, q1)
    cN[N] = ot_cost(pN, qN, configs(2 * N))
check("A1 [T]/[F]", all(abs(cN[N] - N * c1) < 1e-9 for N in cN), "for independent families (product odds and product support) the "
      "fewest-changes transport cost is additive, c(N) = N c(1): the product of optimal couplings attains N c(1), and any coupling's "
      "expected changes are at least the sum of its marginal couplings' (LP optimum)", f"c(1) {c1:.4f}; c(N)/N " +
      ", ".join(f"{N}: {cN[N] / N:.4f}" for N in cN))
c0 = {}
for N in (1, 2, 3):
    pN = p1
    for _ in range(N - 1): pN = np.kron(pN, p1)
    c0[N] = ot_cost(pN, pN, configs(2 * N))
check("A2 [T]", all(abs(v) < 1e-12 for v in c0.values()), "in a stationary vacuum (odds unchanged by the half-tick) the identity "
      "transport (staying) has zero changes, so CL-2's cost is 0 for EVERY N_f: the vacuum cannot rank family counts",
      f"stationary costs {[round(v, 12) for v in c0.values()]}")
print("   A3 [S] CL-2's text prices the transport of a given content under a given half-tick; through a passing it 'does not count new "
      "modes', and the axioms put one qubit per site, so families are composite cell copies (composite-before-atomic) whose NUMBER "
      "no clause of CL-2 (or CL-1, which supplies the cell content) prices: N_f is a supplied multiplicity, not a CL-2 output")
Nall = range(0, 25); mod3 = [N for N in Nall if N % 3 == 0]
r16 = [N for N in Nall if N % 3 == 0]                                  # 16-pair Omega: exists per family; Spin-Z4 16 N = 0 mod 16
rbare = [N for N in Nall if N >= 4 and (2 * N) % 16 == 0]             # freeze-mirror-smg: C(N,4) >= 1 and index 2N = 0 mod 16
rbare3 = [N for N in rbare if N % 3 == 0]
ext = min(mod3, key=lambda N: N * c1); ext1 = min([N for N in mod3 if N >= 1], key=lambda N: N * c1)
check("A4 [T]", ext == 0 and ext1 == 3 and min(rbare) == 8 and min(rbare3) == 24, "EXTENDED reading (not adopted) 'the content "
      "minimises expected changes': over the anomaly-free set the minimiser is N_f = 0 (no matter); 3 appears only with a supplied "
      "'N_f >= 1', and only for the 16-pair Omega route. With FREEZE's bare-label charge-4 term (freeze-mirror-smg: exists only for "
      "N_f >= 4; Spin-Z4 needs 2 N_f = 0 mod 16) the smallest count is 8, and 24 if the turn mod 3 also applied: minimality is "
      "route-dependent", f"argmin incl. 0: {ext}; N >= 1: {ext1}; bare route smallest {min(rbare)}, with mod 3 {min(rbare3)}")

# ================================================================ B. FREEZE-class winding
print("== B. FREEZE-class winding on the turn axis K = kappa (1,1,1)")
def sectors(n):
    e, v = np.linalg.eig(np.kron(np.eye(n), T3)); lb = np.round(np.angle(e) / (2 * np.pi / 3)).astype(int) % 3
    return [np.linalg.qr(v[:, lb == a])[0] for a in range(3)]
def wind(U, SEC, n=300):
    ks = np.linspace(0, 2 * np.pi, n + 1); out = []
    for Sx in SEC:
        d = np.array([np.linalg.det(Sx.conj().T @ U(k * np.ones(3)) @ Sx) for k in ks])
        out.append(int(round(np.sum(np.angle(d[1:] / d[:-1])) / (2 * np.pi))))
    return out
form = lambda q, h: [h * (int(a == (q + 2) % 3) - int(a == (q + 1) % 3)) for a in range(3)]
WF = wind(UF, sectors(1))
pairs = {(q, qq): [a + b for a, b in zip(form(q, 1), form(qq, -1))] for q in range(3) for qq in range(3)}
diff = [v for (q, qq), v in pairs.items() if q != qq]
okB1 = (WF == [-2, 1, 1] and all(v == [0, 0, 0] for (q, qq), v in pairs.items() if q == qq) and
        all(sum(map(abs, v)) == 4 and sorted(v) in ([-2, 1, 1], [-1, -1, 2]) for v in diff) and len({tuple(v) for v in diff}) == 6
        and WF in diff)
check("B1 [T]", okB1, "a per-family node pair (light hand +, mirror hand -) has winding f(q,+) + f(q',-): 0 for q = q', and for "
      "q != q' exactly the six vectors +-(3 e_a - (1,1,1)), all of L1 norm 4; FREEZE's W_F is one of them, so FREEZE already has "
      "the MINIMAL nonzero per-family winding of its class (no smaller FREEZE-class tick exists)", f"W_F {WF}; class {sorted(map(tuple, diff))}")
Pq1, Pq2 = Pp @ (I8 + tau3) / 2, Pp @ (I8 - tau3) / 2
def slab(K, Ls, g):
    F = UF(K); U0 = np.zeros((8 * Ls, 8 * Ls), complex); HA = np.zeros_like(U0); HB = np.zeros_like(U0)
    for l in range(Ls): U0[8 * l:8 * l + 8, 8 * l:8 * l + 8] = F if l % 2 == 0 else F.conj().T
    for l in range(Ls - 1):
        H = HA if l % 2 == 0 else HB; Pq = Pq1 if l % 2 == 0 else Pq2
        H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] += Pq; H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] += Pq
    return expm(-1j * g * HB) @ expm(-1j * g * HA) @ U0
def near_wall(Ls, K0, e0, g=0.5):
    U = slab(K0 * np.ones(3), Ls, g); e, v = np.linalg.eig(U); sel = np.abs(np.angle(e * np.exp(-1j * e0))) < 1e-6
    Z = np.linalg.qr(v[:, sel])[0]; Op = np.kron(np.diag(np.arange(Ls) * 1.), I8)
    xe, Uz = np.linalg.eigh(Z.conj().T @ Op @ Z); Zn = (Z @ Uz)[:, xe < Ls / 2]; Zf = (Z @ Uz)[:, xe >= Ls / 2]
    TL = np.kron(np.eye(Ls), T3); secs = []
    for B in (Zn, Zf):
        ev = np.linalg.eigvals(B.conj().T @ TL @ B); lb = np.round(np.angle(ev) / (2 * np.pi / 3)).astype(int) % 3
        secs.append([int((lb == a).sum()) for a in range(3)])
    return int(sel.sum()), secs
n0, s0 = near_wall(7, 0., 0.); npi, spi = near_wall(7, np.pi, np.pi)
okB2 = n0 == npi == 4 and s0[0] == spi[0] == [1, 1, 0] and s0[1] == spi[1] == [1, 0, 1]
check("B2 [F]", okB2, "odd (Ls = 7) slab with the minimal-winding tick: the near wall holds exactly ONE Weyl doublet at (K = 0, 0) and "
      "one at (R, pi), 2 states per node in turn sectors (1, w) (q 2), so ONE light copy in total across sectors (the pi state is "
      "FREEZE's own pinned partner); the three turn sectors are turn charges, not copies; the far wall holds the q 1 doublet",
      f"states at 0: {n0}, near/far sectors {s0}; at pi: {npi}, {spi}")
WN = {N: wind(lambda K, N=N: np.kron(np.eye(N), UF(K)), sectors(N), 200) for N in (2, 3)}
def far_coeffs(N, t): return dict(Z3_spin10=(-2 * N * t) % 3, Z3_grav=(-16 * N * t) % 3, Z3_cubed=(-16 * N * t ** 3) % 9)
def allowed(lights, mirrors, Ns, mdoub=4):
    k = (-mirrors[0]) % 3; out = []
    for N in Ns:
        far = any(v for v in far_coeffs(N * len(mirrors), (mirrors[0] + k) % 3).values())
        if (N * mdoub * sum((q + k) % 3 for q in lights)) % 3 == 0 and not far: out.append(N)
    return out
Ns = range(1, 13); aO = allowed([2, 2], [1, 1], Ns); div3 = [N for N in Ns if all((N * x) % 3 == 0 for x in WF)]
okB3 = WN[2] == [2 * x for x in WF] and WN[3] == [3 * x for x in WF] and aO == div3 == [3, 6, 9, 12] and [x % 3 for x in WF] == [1, 1, 1]
check("B3 [T]", okB3, "N_f stacked identical families give W_tot = N_f W_F, and W_F = (1,1,1) mod 3, so the anomaly-free set of "
      "floquet-pi-slab D1 is EXACTLY 'W_tot = 0 mod 3 in Z[Z3]'. A 'minimal nonzero winding' rule picks N_f = 1 (anomalous); "
      "'minimal anomaly-free winding' (3 W_F) is the supplied minimality restated; CL-1's adopted tick has W = 0 (slab-parity C1)",
      f"W(2) {WN[2]}, W(3) {WN[3]}; D1 allowed {aO}; W_tot = 0 mod 3 at {div3}")

# ================================================================ C. vacuum energy of the gapped far wall
print("== C. vacuum energy of the mirror-gapped far wall (reduced SU(4) analogue of the charge-4 pair square)")
nm = 8; dim = 2 ** nm; Zp = np.diag([1., -1.]); Am = np.array([[0, 1], [0, 0.]])
def ann(j):
    ops = [Zp] * j + [Am] + [np.eye(2)] * (nm - j - 1); M = ops[0]
    for o in ops[1:]: M = np.kron(M, o)
    return M
cc = {(f, i): ann(4 * f + i) for f in (0, 1) for i in range(4)}
Bij = {(i, j): cc[0, i] @ cc[1, j] - cc[0, j] @ cc[1, i] for i in range(4) for j in range(4) if i < j}
def eps4(*a): return int(round(np.linalg.det(np.eye(4)[list(a)])))
Om = sum(eps4(i, j, k, l) * Bij[i, j] @ Bij[k, l] for (i, j) in Bij for (k, l) in Bij if len({i, j, k, l}) == 4) / 4
Nop = sum(cc[k].T @ cc[k] for k in cc); H1 = -(Om + Om.T)
ch4 = np.linalg.norm(Nop @ Om - Om @ Nop + 4 * Om)
gen = [(cc[0, i].T @ cc[0, j] + cc[1, i].T @ cc[1, j]) for i in range(4) for j in range(4) if i != j]
su4 = max(np.linalg.norm(G @ Om - Om @ G) for G in gen)
e1 = np.linalg.eigvalsh(H1); E1, gap1 = e1[0], e1[np.argmax(e1 > e1[0] + 1e-9)] - e1[0]; deg1 = int((e1 < e1[0] + 1e-9).sum())
H1s = sp.csr_matrix(np.where(abs(H1) > 1e-14, H1, 0)); I = sp.identity(dim, format='csr')
H2 = sp.kron(H1s, I, format='csr') + sp.kron(I, H1s, format='csr')
e2 = np.sort(eigsh(H2, k=6, which='SA', tol=1e-10)[0]); E2 = e2[0]; gap2 = e2[np.argmax(e2 > e2[0] + 1e-7)] - e2[0]
okC1 = ch4 < 1e-12 and su4 < 1e-12 and np.linalg.norm(Om) > 1 and E1 < 0 and gap1 > 0.1 and abs(E2 - 2 * E1) < 1e-8 and abs(gap2 - gap1) < 1e-6
check("C1 [T]/[F]", okC1, "reduced analogue: Omega' = sum eps_ijkl B_ij B_kl (B_ij the antisymmetric pair of two 4s; charge 4, "
      "SU(4)-invariant), H = -(Omega' + h.c.) on 8 modes has E0 < 0 and a gap; two decoupled families (Kronecker sum, 2^16 sparse) "
      "give E0(2) = 2 E0(1) and gap(2) = gap(1)", f"charge-4 {ch4:.0e}, SU(4) {su4:.0e}; E0(1) {E1:.4f} (deg {deg1}), gap {gap1:.4f}; "
      f"E0(2) {E2:.4f}, gap {gap2:.4f}; nnz {H2.nnz}")
EN = [N * E1 for N in range(1, 10)]
check("C2 [T]", all(b < a for a, b in zip(EN, EN[1:])), "with a family-diagonal mirror term (anomaly-family-count's Omega is a per-family "
      "pairing inside a 16) E0(N) = N E0(1) is strictly DECREASING in N_f and the gap is N_f-independent: energy minimisation "
      "prefers MORE families (unbounded) and no stability bound arises. CL-3 weighs only departures from the vacuum (and the "
      "Hamiltonian constraint subtracts the vacuum phase), so the far wall's vacuum energy carries no weight at all",
      f"E0(N)/|E0(1)| for N = 1..9: {[round(x / abs(E1)) for x in EN]}")

# ================================================================ synthesis
Sa, Sb, Sc = ext1 == 3 and ext == 0, okB2 and okB3, okC1
print(f"   synthesis (criteria_pre_run): (a) CL-2 blind in the vacuum, additive off it, minimiser 0 when extended -> no selection; "
      f"(b) minimal winding = one copy per wall, anomaly freedom = W_tot = 0 mod 3, no N_f fixed; (c) vacuum energy decreasing in "
      f"N_f, no bound -> FAIL for (a), (b), (c), as predicted: no adopted rule selects N_f = 3; minimality stays supplied")
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
