AUDIT_INPUT_PATHS = ('docs/THE_FAMILY_CLASS_TICK_HAS_NO_STEP_ANGLE_SO_THE_LAPSE_RIDES_A_WINDING_FREE_LAYER_WHILE_THE_SPEED_TIE_AND_SLAB_SURVIVE_AND_THE_OVERLAP_TAKES_ITS_TIME_EVEN_KERNEL_BOUNDED_THEOREM_NOTE_2026-10-24.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""new-tick-recheck: which results derived with CL-1's W = 0 tick survive the adopted family-class tick
(FREEZE, W_F = (-2,1,1))?  1 lapse in the step;  2 speed tie;  3 overlap (GW, doublers, index);  4 Floquet-pi slab.
Labels: [T] exact, [F] finite diagnostic, [S] estimate / reading. Verdicts follow criteria_pre_run.txt."""
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
# ------------------------------------------------ FREEZE rebuild (twist-local-single / t-breaking-tick-lowenergy, same seed and draw order)
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
def sectors(n):
    e, v = np.linalg.eig(np.kron(np.eye(n), T3)); lb = np.round(np.angle(e) / (2 * np.pi / 3)).astype(int) % 3
    return [np.linalg.qr(v[:, lb == a])[0] for a in range(3)]
def wind(U, SEC, n=300):
    ks = np.linspace(0, 2 * np.pi, n + 1); out = []
    for Sx in SEC:
        d = np.array([np.linalg.det(Sx.conj().T @ U(k * np.ones(3)) @ Sx) for k in ks])
        out.append(int(round(np.sum(np.angle(d[1:] / d[:-1])) / (2 * np.pi))))
    return out
SEC1 = sectors(1); WF = wind(UF, SEC1)
uni = max(np.linalg.norm(UF(K) @ UF(K).conj().T - I8) for K in [rng.uniform(-np.pi, np.pi, 3) for _ in range(3)])
check("0 [T]", uni < 1e-12 and WF == [-2, 1, 1], "FREEZE rebuilt (unitary); turn-graded winding W_F = (-2, 1, 1)", f"unitarity {uni:.0e}, W {WF}")
# ================================================================ 1. lapse in the step
print("== 1. lapse in the step")
Kr = [rng.uniform(-np.pi, np.pi, 3) for _ in range(5)]
BL = np.linalg.eigh(Pp)[1][:, 4:]; dmax = 0.; dcl = 0.
for K in Kr:
    th = np.angle(np.linalg.eigvals(BL.conj().T @ UF(K) @ BL)); dmax = max(dmax, abs(np.cos(th) - np.cos(K).mean()).max())
    dcl = max(dcl, abs(np.cos(np.angle(np.linalg.eigvals(U1(K / 2, np.pi / 2)))) - np.cos(K).mean()).max())
sp = {e: np.sort(abs(np.angle(np.linalg.eigvals(U1(np.array([5e-4, 0, 0]), e)))))[-1] / 1e-3 for e in (0.3, 0.8, np.pi / 2)}
check("1a [T]/[F]", dmax < 1e-12 and dcl < 1e-12 and all(abs(sp[e] - np.sin(e) / np.sqrt(3)) < 1e-6 for e in sp), "FREEZE's light "
      "dispersion cos theta = mean cos K is EXACTLY CL-1's tick at its maximal step eps = pi/2 (all 8 bands of U1(pi/2) obey it; "
      "U1(eps) speed = sin(eps)/sqrt3 per cell). FREEZE has no free step: its light speed is pinned at sin(eps0) = 1",
      f"FREEZE {dmax:.0e}, U1(pi/2) {dcl:.0e}; speeds at eps 0.3, 0.8, pi/2: {[round(float(v), 6) for v in sp.values()]}")
s = 0.9; Rn = np.pi * np.ones(3); dl = 1e-4 * np.array([1, 2, 3.])
def Upow(K, s):
    e, v = np.linalg.eig(UF(K)); return v @ np.diag(np.exp(1j * s * np.angle(e))) @ np.linalg.inv(v)
jump = np.linalg.norm(Upow(Rn + dl, s) - Upow(Rn - dl, s)); smooth = np.linalg.norm(UF(Rn + dl) - UF(Rn - dl))
check("1b [T]", jump > 0.1 and smooth < 1e-2, "no step-angle path inside the class: W is a homotopy invariant of K -> U(K) and the "
      "identity (eps = 0) has W = 0, so no continuous family of tick unitaries joins eps = 0 to FREEZE; the fractional power "
      "U_F^s (s = 0.9) is DISCONTINUOUS at the pi node R (not local). The adopted 'sin(eps_cube) = N sin eps0' has nothing to act on",
      f"|U^s(R+d) - U^s(R-d)| = {jump:.2f} vs |U(R+d) - U(R-d)| = {smooth:.0e}")
def Gl(K, Ng): return Pp @ Y @ (sum((Ng[i] - 1) * np.sin(K[i]) * gam[i] for i in range(3)) / np.sqrt(3)) @ Y.conj().T @ Pp
def UN(K, Ng=np.ones(3)): return expm(1j * Gl(K, Ng)) @ UF(K)
rat = {}
for Ng in (0.9 * np.ones(3), 0.7 * np.ones(3), np.array([0.7, 0.9, 1.1])):
    for i in range(3):
        k = np.zeros(3); k[i] = 1e-2; a = np.sort(abs(np.angle(np.linalg.eigvals(UN(k, Ng)))))[:4]; b = np.sort(abs(np.angle(np.linalg.eigvals(UF(k)))))[:4]
        rat[(tuple(Ng), i)] = (a / b).max() - Ng[i], (a / b).min() - Ng[i]
rerr = max(max(abs(x) for x in v) for v in rat.values())
WN = [wind(lambda K, N=N: UN(K, N * np.ones(3)), SEC1) for N in (0.7, 0.9, 1.3)]
tcov = max(np.linalg.norm(T3 @ UN(k * np.ones(3), 0.9 * np.ones(3)) @ T3.T - UN(k * np.ones(3), 0.9 * np.ones(3))) for k in (0.4, 2.1))
pcov = max(np.linalg.norm(T3 @ Gl(K, 0.8 * np.ones(3)) @ T3.T - Gl(C3d @ K, 0.8 * np.ones(3))) for K in Kr[:3])
check("1c [T]/[F]", rerr < 1e-3 and all(x == WF for x in WN) and tcov < 1e-12 and pcov < 1e-12, "REPAIR (lapse layer): tick = "
      "exp(i G_N) . U_F with G_N = Pi+ Y [sum_i (N sqrt(gamma^ii) - 1) sin K_i gamma_i / sqrt3] Y^+ Pi+ (the tick's OWN linear term). "
      "It is turn-covariant and homotopic to 1, so W = W_F exactly for every N; low quasi-energies scale by N sqrt(gamma^ii) per "
      "axis; every site still ticks every half-tick (no skips, static source = static tick)",
      f"max |ratio - N_i| at |K| = 0.01: {rerr:.0e}; W(N = 0.7, 0.9, 1.3) {WN}; turn {max(tcov, pcov):.0e}")
# ================================================================ 2. speed tie
print("== 2. speed tie")
def cgrav(K, tau): return 2 * np.arcsin(tau * np.sqrt(np.sum(np.sin(K / 2) ** 2)))        # tick-fraction-waves B6 (Lorentzian reading)
def clight(K, U=UF): return np.sort(abs(np.angle(np.linalg.eigvals(BL.conj().T @ U(K) @ BL))))[-1]
dirs = [x / np.linalg.norm(x) for x in [rng.normal(size=3) for _ in range(20)]]
dtie = max(abs(cgrav(k * n, 3 ** -.5) - clight(k * n)) for n in dirs for k in (0.05, 0.4, 1.5))
dN = max(abs(cgrav(0.02 * n, 0.9 * 3 ** -.5) - clight(0.02 * n, lambda K: UN(K, 0.9 * np.ones(3)))) / 0.02 for n in dirs)
sup = min(np.sum(n ** 4) for n in dirs) >= 1 / 3 - 1e-12
check("2 [T]/[F]", dtie < 1e-12 and dN < 1e-5 and sup, "SURVIVES, sharpened: the tie tau = light speed per tick is still ONE "
      "tick/edge ratio, now fixed at tau = 1/sqrt3 (sin eps0 = 1), not free. At tau^2 = 1/3 the graviton relation "
      "sin^2(w/2) = tau^2 sum sin^2(k_i/2) IS cos w = mean cos k, FREEZE's light relation [T]; if both k are in the same lattice "
      "units (the waves note's blocks, [S]) light and graviton agree at EVERY k, not only k -> 0; with the lapse layer both scale by N; graviton never superluminal (tau^2 = 1/3 <= sum khat^4)",
      f"max |w_grav - theta_light| {dtie:.0e} (|k| to 1.5, 20 directions); at N = 0.9 slope gap {dN:.0e}")
# ================================================================ 3. overlap from the new tick's Euclidean kernel
print("== 3. overlap (history-level weighting) from the new tick's kernel")
Hc = lambda K: (np.sqrt(2) / 3) * (np.cos(K[0]) + np.conj(w) * np.cos(K[1]) + w * np.cos(K[2]))
GA = gam + [tau1, tau2]
acom = max(np.linalg.norm(GA[i] @ GA[j] + GA[j] @ GA[i] - 2 * (i == j) * I8) for i in range(5) for j in range(5))
def ncomp(K): h = Hc(K); return np.concatenate([np.sin(K) / np.sqrt(3), [h.real, -h.imag]])
cdec = max(np.linalg.norm(Uc(K) - np.cos(K).mean() * I8 - 1j * sum(c * G for c, G in zip(ncomp(K), GA))) for K in Kr)
s1, s2, s3 = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1., -1])
G4d = [np.kron(s1, s1), np.kron(s1, s2), np.kron(s1, s3), np.kron(s2, np.eye(2)), np.kron(s3, np.eye(2))]   # Cl(5) on 4 spinors
p5 = G4d[0] @ G4d[1] @ G4d[2] @ G4d[3] @ G4d[4]
g5 = G4d[4]; I4 = np.eye(4)
def Xdir(K, k4, m0=0.4):           # direct transcription: tick generator as the spatial part; Gamma4 doubles as the time gamma
    n = ncomp(K); return (1j * G4d[3] * np.sin(k4) + (1 - np.cos(k4)) * I4 + 1j * sum(c * G for c, G in zip(n, G4d))
                         + (1 - np.cos(K).mean()) * I4 - m0 * I4)
hdef = max(np.linalg.norm(g5 @ Xdir(K, 0.3) @ g5 - Xdir(K, 0.3).conj().T) / (2 * abs(Hc(K).imag) * 2) for K in Kr)
check("3a [T]", acom < 1e-12 and cdec < 1e-12 and np.allclose(p5, p5[0, 0] * I4) and abs(hdef - 1) < 1e-9, "the new tick is a "
      "Clifford walk U = f + i n.Gamma over FIVE anticommuting directions (3 hops + the two L-R components Re H, Im H). On one "
      "4-spinor the five exhaust Cl(5) (their product is scalar), so no time gamma anticommutes with all five and gamma5 must be one of "
      "the L-R directions: the direct transcription is NOT g5-hermitian, defect exactly 2|Im H| x |G5| (the T-odd phase). NEEDS REPAIR",
      f"anticomm {acom:.0e}, U = f + i n.Gamma to {cdec:.0e}, defect / (2|Im H||G5|) = {hdef:.6f}")
def Xeven(K, k4, m0, vs=3 ** -.5, rs=None):   # T-even kernel: the tick's hop and scalar part; rs default = tick's own 1 - f
    W = (1 - np.cos(K).mean()) if rs is None else rs * np.sum(1 - np.cos(K))
    return 1j * G4d[3] * np.sin(k4) + 1j * vs * sum(np.sin(K[i]) * G4d[i] for i in range(3)) + (W + 1 - np.cos(k4) - m0) * I4
def Vov(X): e, v = np.linalg.eigh(g5 @ X); return g5 @ (v * np.sign(e)) @ v.conj().T
gr = np.linspace(-np.pi, np.pi, 8, endpoint=False); gw = 0.; zc = {}
for m0 in (0.4, 1.0, 1.7):
    nz = 0
    for kk in it.product(gr, repeat=4):
        X = Xeven(np.array(kk[:3]), kk[3], m0); Dm = I4 + Vov(X)
        if m0 == 0.4: gw = max(gw, np.linalg.norm(g5 @ Dm + Dm @ g5 - Dm @ g5 @ Dm))
        nz += np.linalg.norm(Dm) < 1e-9
    zc[m0] = int(nz)
check("3b [T]/[F]", gw < 1e-12 and zc == {0.4: 1, 1.0: 4, 1.7: 7}, "REPAIR = T-even kernel from the tick's own pieces (hop sin K / "
      "sqrt3, Wilson term = the tick's scalar 1 - f = (1/3) sum(1 - cos K)); it is the Wilson form with r_s = 1/3: GW exact, and D "
      "vanishes only at k = 0 in the window 0 < m0 < 2/3 (corner masses 2 n_s / 3 + 2 n_t); the window is NARROWER than the old 0 < m0 < 2",
      f"GW {gw:.0e} on 8^4; zeros for m0 = 0.4, 1.0, 1.7: {list(zc.values())}")
L4 = 4; NS = L4 ** 4; SITES = list(it.product(range(L4), repeat=4)); SID = {x: i for i, x in enumerate(SITES)}
def links(e, n12, n34):
    U = np.ones((4, NS), complex)
    for (mu, nu, n) in ((0, 1, n12), (2, 3, n34)):
        for i, x in enumerate(SITES):
            U[mu, i] *= np.exp(-2j * np.pi * e * n * x[nu] / L4 ** 2)
            if x[nu] == L4 - 1: U[nu, i] *= np.exp(2j * np.pi * e * n * x[mu] / L4)
    return U
GM = [G4d[0], G4d[1], G4d[2], G4d[3]]
def Xreal(U, m0, v, r):
    X = np.zeros((4 * NS, 4 * NS), complex)
    for i, x in enumerate(SITES):
        X[4 * i:4 * i + 4, 4 * i:4 * i + 4] += (sum(r) - m0) * I4
        for mu in range(4):
            y = list(x); y[mu] = (y[mu] + 1) % L4; j = SID[tuple(y)]
            X[4 * i:4 * i + 4, 4 * j:4 * j + 4] += -(r[mu] * I4 - v[mu] * GM[mu]) / 2 * U[mu, i]
            X[4 * j:4 * j + 4, 4 * i:4 * i + 4] += -(r[mu] * I4 + v[mu] * GM[mu]) / 2 * np.conj(U[mu, i])
    return X
G5L = np.kron(np.eye(NS), g5); KER = {'new': (0.4, [3 ** -.5] * 3 + [1.], [1 / 3] * 3 + [1.]), 'old': (1.0, [1.] * 4, [1.] * 4)}
idx = {}; gwr = 0.; gap = 9.
for nm, (m0, v, r) in KER.items():
    for (e, Q) in ((1, 0), (1, 1), (2, 4)):
        U = links(e, 0 if Q == 0 else 1, 0 if Q == 0 else 1); ev, vv = np.linalg.eigh(G5L @ Xreal(U, m0, v, r)); gap = min(gap, abs(ev).min())
        idx[(nm, Q)] = int(round(-0.5 * np.sum(np.sign(ev))))
        if nm == 'new' and Q == 1:
            Dm = np.eye(4 * NS) + G5L @ (vv * np.sign(ev)) @ vv.conj().T; gwr = np.linalg.norm(G5L @ Dm + Dm @ G5L - Dm @ G5L @ Dm)
okI = all(abs(idx[(nm, Q)]) == Q for nm in KER for Q in (0, 1, 4)) and all(idx[('new', Q)] == idx[('old', Q)] for Q in (0, 1, 4))
check("3c [F]", okI and gwr < 1e-10, "one small background (U(1), 4^4, fluxes (n,n) in the (12), (34) planes): the new-tick "
      "kernel's overlap index equals the old kernel's and the flux prediction, e^2 Q (charge 1: 1, charge 2: 4, Q = 0: 0), GW holds "
      "in the background; so the index-based anomaly checks (overlap-nonabelian / overlap-colour sums) carry over for this kernel",
      f"index new {[idx[('new', Q)] for Q in (0, 1, 4)]}, old {[idx[('old', Q)] for Q in (0, 1, 4)]}; GW {gwr:.0e}; min |g5 X| {gap:.3f}")
# ================================================================ 4. Floquet-pi slab on the adopted tick (with the lapse layer)
print("== 4. family-class slab (floquet-pi-slab construction: layers F, F^+, ...; q 1 / q 2 label gates; g = 0.5)")
g = 0.5; X2 = np.array([[0, 1], [1, 0]])
def slab(K, Ls, N):
    F = UN(K, N * np.ones(3)); U0 = np.zeros((8 * Ls, 8 * Ls), complex); HA = np.zeros_like(U0); HB = np.zeros_like(U0)
    for l in range(Ls): U0[8 * l:8 * l + 8, 8 * l:8 * l + 8] = F if l % 2 == 0 else F.conj().T
    for l in range(Ls - 1):
        H = HA if l % 2 == 0 else HB; Pq = Pq1 if l % 2 == 0 else Pq2
        H[8 * l:8 * l + 8, 8 * l + 8:8 * l + 16] += Pq; H[8 * l + 8:8 * l + 16, 8 * l:8 * l + 8] += Pq
    return expm(-1j * g * HB) @ expm(-1j * g * HA) @ U0
def bulk(K, k, N):
    F = UN(K, N * np.ones(3)); Z = np.zeros((8, 8)); U0 = np.block([[F, Z], [Z, F.conj().T]])
    XB = np.array([[0, np.exp(-1j * k)], [np.exp(1j * k), 0]])
    return expm(-1j * g * np.kron(XB, Pq2)) @ expm(-1j * g * np.kron(X2, Pq1)) @ U0
def bgap(N, n=8):
    gr = np.linspace(-np.pi, np.pi, n, endpoint=False); a0 = ap = 9.
    for K in it.product(gr, repeat=3):
        for k in gr:
            thx = np.angle(np.linalg.eigvals(bulk(np.array(K), k, N))); a0 = min(a0, abs(thx).min()); ap = min(ap, (np.pi - abs(thx)).min())
    return a0, ap
def walls(Ls, K0, e0, N):
    U = slab(K0 * np.ones(3), Ls, N); e, v = np.linalg.eig(U); sel = np.abs(np.angle(e * np.exp(-1j * e0))) < 1e-6
    Z = np.linalg.qr(v[:, sel])[0]; Op = np.kron(np.diag(np.arange(Ls) * 1.), I8) + 0.01 * np.kron(np.eye(Ls), tau3)
    xe, Uz = np.linalg.eigh(Z.conj().T @ Op @ Z); Z = Z @ Uz
    TL = np.kron(np.eye(Ls), T3); SG = [np.kron(np.eye(Ls), s) for s in sig]; out = []
    for i in range(0, len(xe), 2):
        B = Z[:, i:i + 2]; dq = np.linalg.det(B.conj().T @ TL @ B); Ad = []
        for j in range(3):
            d = np.zeros(3); d[j] = 1e-6
            Ad.append(B.conj().T @ (1j * (slab(K0 * np.ones(3) + d, Ls, N) - slab(K0 * np.ones(3) - d, Ls, N)) / 2e-6 @ U.conj().T) @ B)
        M = np.array([[np.trace(Ad[a] @ B.conj().T @ SG[b] @ B).real / 2 for b in range(3)] for a in range(3)])
        out.append((int(round(np.mean(xe[i:i + 2]))), [x for x in range(3) if np.isclose(dq, w ** (2 * x), atol=1e-6)][0], int(np.sign(np.linalg.det(M)))))
    return out
SE7 = sectors(7); R4 = {}
for N in (1.0, 0.9):
    R4[N] = dict(gap=bgap(N), W=wind(lambda K, N=N: slab(K, 7, N), SE7, 200), w0=walls(7, 0., 0., N), wp=walls(7, np.pi, np.pi, N))
want = [(0, 2, 1), (6, 1, -1)]
ok4 = all(min(R4[N]['gap']) > 0.3 and R4[N]['W'] == WF and R4[N]['w0'] == want and R4[N]['wp'] == want for N in R4)
check("4 [F]", ok4, "SURVIVES: the odd (Ls = 7) slab of the adopted tick, at N = 1 and with the lapse layer at N = 0.9, has its bulk "
      "gapped at 0 and pi, W = W_F, the light q 2 (hand +1) on the near wall and the mirror q 1 (hand -1) on the far wall, at "
      "(K = 0, 0) and at its (R, pi) partner: one protected light Weyl per field at quasi-energy 0, its pi partner at cell scale",
      "; ".join(f"N {N}: gap (0, pi) ({R4[N]['gap'][0]:.3f}, {R4[N]['gap'][1]:.3f}), W {R4[N]['W']}, walls {R4[N]['w0']}" for N in R4))
print(f"elapsed {time.time() - T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20:.0f} MB")
print(f"TOTAL: PASS={NP[0]} FAIL={NP[1]}")
