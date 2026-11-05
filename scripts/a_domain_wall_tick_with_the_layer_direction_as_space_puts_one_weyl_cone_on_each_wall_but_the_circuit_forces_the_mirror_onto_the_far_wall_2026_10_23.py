AUDIT_INPUT_PATHS = ('docs/A_DOMAIN_WALL_TICK_WITH_THE_LAYER_DIRECTION_AS_SPACE_PUTS_ONE_WEYL_CONE_ON_EACH_WALL_BUT_THE_CIRCUIT_FORCES_THE_MIRROR_ONTO_THE_FAR_WALL_BOUNDED_THEOREM_NOTE_2026-10-23.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""chiral-tick-form: does a unitary tick (Hamiltonian / Floquet) form of one-handed matter with the mirror removed exist?
 A  domain wall with the extra (layer) direction as SPACE and the tick as time: a 3+1+1 slab Hamiltonian H (strictly
    nearest-neighbour) and a strictly local layered Floquet circuit U (each factor range 1); free fields, momentum space
    on the L^3 torus (exact by Bloch), Ls layers with open ends. Boundary Weyl cones, chirality, mirror overlap, locality,
    rotation covariance, and why the corner / W3 obstruction does not bind one wall (it binds the slab).
 B  exponentially local modified chiral charges in a lattice Hamiltonian: the slab's layer-sign charge (compact, on-site in
    3D, quantised) is not conserved, its violation sits on the middle bond; the 1+1D Onsager template's one-handed
    combination is not quantised (recheck of the cited Chatterjee-Pace-Shao template).
 C  the same circuit at larger steps: quasienergy-pi cones only after the bulk gap closes; W3 = 0 by homotopy for any circuit.
 K  control: the W3 integrator and the walk-sector relation n0 = npi = -W3 on an exact degree-one unitary family.
Labels: [T] exact, [F] finite diagnostic. Supplied model (Wilson-type slab, m, theta, tau, Ls); no physical identification.
Cited, not rederived: Kaplan 1992, Creutz-Horvath 1994 (Hamiltonian domain wall), Zhang-Hu 2001 / Qi-Hughes-Zhang 2008
(4D quantum Hall, 3D Weyl boundary), Rudner-Lindner-Berg-Levin 2013 (anomalous Floquet), Nielsen-Ninomiya 1981,
Chatterjee-Pace-Shao 2024, Gioia-Thorngren 2025 (arXiv:2503.07708, as cited by the nononsite-chiral probe)."""
AUDIT_TIMEOUT_SEC = 120
import os, sys, time, itertools, resource
os.environ['OPENBLAS_NUM_THREADS'] = '1'; os.environ['OMP_NUM_THREADS'] = '1'; os.environ['VECLIB_MAXIMUM_THREADS'] = '1'
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

rng = np.random.default_rng(20261023)
T0 = time.time(); P = F = 0
def check(name, ok, info=""):
    global P, F
    P += bool(ok); F += (not ok)
    print(("PASS" if ok else "FAIL") + f": {name}" + (f"  [{info}]" if info else ""))

s0 = np.eye(2, dtype=complex); sx = np.array([[0, 1], [1, 0]], complex); sy = np.array([[0, -1j], [1j, 0]]); sz = np.diag([1., -1]).astype(complex)
SIG = [sx, sy, sz]
G = [np.kron(sx, sx), np.kron(sx, sy), np.kron(sx, sz), np.kron(sy, s0), np.kron(sz, s0)]   # Gamma_1..3 (space), Gamma_4 (layer), Gamma_5 (mass)
G5 = G[4]; I4 = np.eye(4); A_UP = (G5 + 1j * G[3]) / 2                                     # layer bond s -> s+1 carries A_UP

def bonds(Ls):
    out = []
    for s in range(Ls - 1):
        S = np.zeros((Ls, Ls)); S[s + 1, s] = 1
        out.append(np.kron(A_UP, S) + np.kron(A_UP.conj().T, S.T))
    return out
BCACHE = {}
def hb(Ls):
    if Ls not in BCACHE: BCACHE[Ls] = bonds(Ls)
    return BCACHE[Ls]
def ham(k, Ls, m):
    Is = np.eye(Ls)
    H = sum(np.kron(np.sin(k[i]) * G[i] + np.cos(k[i]) * G5, Is) for i in range(3)) + (m - 4) * np.kron(G5, Is)
    return H + sum(hb(Ls))
def dham(k, Ls, j): return np.kron(np.cos(k[j]) * G[j] - np.sin(k[j]) * G5, np.eye(Ls))
def layer(Ls, th, par):
    X = np.eye(4 * Ls, dtype=complex)
    for b in range(par, Ls - 1, 2):
        h = hb(Ls)[b]; X = X + (np.cos(th) - 1) * h @ h - 1j * np.sin(th) * h     # exact exp(-i th h_b): h_b^3 = h_b
    return X
def walk(k, Ls, m, th, dj=None):
    """U = W_m W_1 W_2 W_3 W_odd W_even, every factor a range-1 gate; dj: derivative in k_dj"""
    Is = np.eye(Ls); U = np.kron(expm(-1j * th * (m - 4) * G5), Is)
    for i in range(3):
        if i == dj: f = -1j * np.sin(th) * (np.cos(k[i]) * G[i] - np.sin(k[i]) * G5)
        else: f = np.cos(th) * I4 - 1j * np.sin(th) * (np.sin(k[i]) * G[i] + np.cos(k[i]) * G5)
        U = U @ np.kron(f, Is)
    return U @ layer(Ls, th, 1) @ layer(Ls, th, 0)
def bulkU(k, m, th):
    """4D bulk walk (periodic layers, two-layer cell for the even/odd bond split)"""
    Z = np.zeros((4, 4)); ex = lambda h: np.eye(8) + (np.cos(th) - 1) * h @ h - 1j * np.sin(th) * h
    p = k[3]; ho = np.block([[Z, A_UP * np.exp(-1j * p)], [A_UP.conj().T * np.exp(1j * p), Z]]); he = np.block([[Z, A_UP.conj().T], [A_UP, Z]])
    U = np.kron(np.eye(2), expm(-1j * th * (m - 4) * G5))
    for i in range(3): U = U @ np.kron(np.eye(2), np.cos(th) * I4 - 1j * np.sin(th) * (np.sin(k[i]) * G[i] + np.cos(k[i]) * G5))
    return U @ ex(ho) @ ex(he)
def bulk_gaps(m, th, N=8, nstart=4):
    """min |eps| and min |eps - pi| of the bulk: N^4 grid, then Nelder-Mead from the best grid points"""
    pts = []
    for k in itertools.product(2 * np.pi * np.arange(N) / N, repeat=4):
        e = np.abs(np.angle(np.linalg.eigvals(bulkU(np.array(k), m, th)))); pts.append((e.min(), np.pi - e.max(), np.array(k)))
    out = []
    for idx in (0, 1):
        f = (lambda q: np.abs(np.angle(np.linalg.eigvals(bulkU(q, m, th)))).min()) if idx == 0 else \
            (lambda q: np.pi - np.abs(np.angle(np.linalg.eigvals(bulkU(q, m, th)))).max())
        pts.sort(key=lambda x: x[idx])
        out.append(min([pts[0][idx]] + [minimize(f, x[2], method='Nelder-Mead', options={'xatol': 1e-7, 'fatol': 1e-10, 'maxiter': 3000}).fun
                                       for x in pts[:nstart]]))
    return tuple(out)
def wall_nodes(k, Ls, m, th, target, tol, hamilton=False):
    """in-window states at k split by layer position into walls; chirality = sign det v, A_j = P dH_eff/dk_j P"""
    if hamilton: H = ham(k, Ls, m); w, V = np.linalg.eigh(H); e = w - target
    else: U = walk(k, Ls, m, th); w, V = np.linalg.eig(U); e = np.angle(w * np.exp(-1j * target))
    sel = np.abs(e) < tol
    if not sel.any(): return {}
    Q, _ = np.linalg.qr(V[:, sel]); X = np.kron(I4, np.diag(np.arange(Ls)))
    xw, xv = np.linalg.eigh(Q.conj().T @ X @ Q); B = Q @ xv; out = {}
    for wall, msk in (('L', xw < Ls / 2), ('R', xw >= Ls / 2)):
        Pw = B[:, msk]
        if Pw.shape[1] != 2: out[wall] = (Pw.shape[1], 0, 0.); continue
        v = np.zeros((3, 3))
        for j in range(3):
            A = Pw.conj().T @ dham(k, Ls, j) @ Pw if hamilton else 1j * Pw.conj().T @ walk(k, Ls, m, th).conj().T @ walk(k, Ls, m, th, j) @ Pw
            for a in range(3): v[j, a] = np.real(np.trace(A @ SIG[a])) / 2
        out[wall] = (2, int(np.sign(np.linalg.det(v))), abs(np.linalg.det(v)))
    return out
def trim_table(Ls, m, th, tol, hamilton=False):
    tab = {}
    for c in itertools.product([0, 1], repeat=3):
        for t in ((0.,) if hamilton else (0., np.pi)):
            r = wall_nodes(np.pi * np.array(c), Ls, m, th, t, tol, hamilton)
            if r: tab[(c, round(t, 2))] = r
    return tab
def W3(Uf, dUf, N):
    tot = 0
    for k in itertools.product(2 * np.pi * (np.arange(N) + 0.5) / N, repeat=3):
        k = np.array(k); Ui = Uf(k).conj().T; a = [Ui @ dUf(k, j) for j in range(3)]
        tot += 3 * np.trace(a[0] @ (a[1] @ a[2] - a[2] @ a[1]))
    return np.real(tot * (2 * np.pi / N) ** 3 / (24 * np.pi ** 2))

M0, TH = 0.6, 0.2      # supplied: copy mass inside the window 0 < m < 2, step small (Hamiltonian-like tick)
print("== A. domain wall, layer direction as space, tick as time (m = 0.6, theta = 0.2)")
k = rng.uniform(-np.pi, np.pi, 3); U = walk(k, 6, M0, TH)
uerr = np.abs(U.conj().T @ U - np.eye(24)).max()
N = 4; cf = np.zeros((N, N, N, 24, 24), complex)
for n in itertools.product(range(N), repeat=3): cf[n] = walk(2 * np.pi * np.array(n) / N, 6, M0, TH)
cf = np.fft.ifftn(cf, axes=(0, 1, 2)); far = max(np.abs(cf[n]).max() for n in itertools.product(range(N), repeat=3) if 2 in n)
Ub = U.reshape(4, 6, 4, 6); srange = max(abs(a - b) for a in range(6) for b in range(6) if np.abs(Ub[:, a, :, b]).max() > 1e-13)
check("A1 [T] the slab tick U is unitary and a product of range-1 gates: range 1 in each space direction (cube-local), range 2 in layers",
      uerr < 1e-12 and far < 1e-12 and srange <= 2, f"unitarity {uerr:.0e}; Fourier weight at |n| = 2: {far:.0e}; layer range {srange}")
g0, gp = bulk_gaps(M0, TH)
gH = min(np.abs(np.linalg.eigvalsh(ham(np.array(k4[:3]), 1, M0) + np.cos(k4[3]) * np.kron(G5, np.eye(1)) + np.sin(k4[3]) * np.kron(G[3], np.eye(1)))).min()
         for k4 in itertools.product(2 * np.pi * np.arange(8) / 8, repeat=4))
check("A2 [F] the 4D bulk is gapped: walk at quasienergy 0 and pi (8^4 grid + local minimisation), Hamiltonian at 0 (8^4 grid)", g0 > 0.05 and gp > 0.5 and gH > 0.3,
      f"walk gap0 {g0:.3f}, gap_pi {gp:.3f}; H gap {gH:.3f}")
tab = trim_table(12, M0, TH, 0.05); tabH = trim_table(12, M0, TH, gH / 2, True)
okA3 = list(tab) == [((0, 0, 0), 0.0)] and tab[((0, 0, 0), 0.0)]['L'][1] == -tab[((0, 0, 0), 0.0)]['R'][1] != 0 and list(tabH) == [((0, 0, 0), 0.0)] \
    and tabH[((0, 0, 0), 0.0)]['L'][1] == tab[((0, 0, 0), 0.0)]['L'][1]
check("A3 [F] exactly one two-component Weyl node per wall, at k = 0 and quasienergy 0, opposite chirality on the two walls; none at the "
      "other 7 corners, none at pi; the Hamiltonian slab agrees (Ls = 12)", okA3,
      f"walk {tab[((0,0,0),0.0)]}; H L,R chirality {tabH[((0,0,0),0.0)]['L'][1]},{tabH[((0,0,0),0.0)]['R'][1]} |det v| {tabH[((0,0,0),0.0)]['L'][2]:.3f}")
bad = 0; ning = 0; Ls = 8
for n in itertools.product(range(12), repeat=3):
    kk = 2 * np.pi * np.array(n) / 12; e = np.abs(np.angle(np.linalg.eigvals(walk(kk, Ls, M0, TH))))
    if (e < g0 / 2).any() or (e > np.pi - gp / 2).any():
        ning += 1; bad += np.linalg.norm(np.angle(np.exp(1j * kk))) > 0.8
cnt6 = sum(int((np.abs(np.angle(np.linalg.eigvals(walk(2 * np.pi * np.array(n) / 6, Ls, M0, TH)))) < g0 / 2).sum())
           for n in itertools.product(range(6), repeat=3))
check("A4 [F] no other boundary nodes anywhere in the zone: every 12^3 grid point with an in-gap state lies within 0.8 of k = 0; on the "
      "L = 6 torus (Ls = 8) the in-gap states are the 4 at k = 0", bad == 0 and cnt6 == 4, f"in-gap points {ning}, far {bad}; L = 6 count {cnt6}")
dH = [np.sort(np.abs(np.linalg.eigvalsh(ham(np.zeros(3), L_, M0))))[0] for L_ in range(3, 10)]
dU = [np.sort(np.abs(np.angle(np.linalg.eigvals(walk(np.zeros(3), L_, M0, TH)))))[0] for L_ in range(3, 10)]
d1 = np.sort(np.abs(np.linalg.eigvalsh(ham(np.zeros(3), 6, 1.0))))[0]
check("A5 [T]/[F] mirror overlap falls as |1 - m|^Ls (exact zero-mode recursion psi_s = (1-m)^s chi, i G5 G4 chi = -chi): the k = 0 "
      "splitting ratio per layer -> 0.4; at m = 1 the wall mode is compact and the overlap vanishes", abs(dH[-1] / dH[-2] - 0.4) < 4e-3
      and abs(dU[-1] / dU[-2] - 0.4) < 4e-3 and d1 < 1e-13,
      "H " + ", ".join(f"{x:.1e}" for x in dH) + f" (Ls 3..9); walk ratio {dU[-1]/dU[-2]:.4f}; m=1: {d1:.0e}; xi = {1/np.log(2.5):.2f} layers")
u2 = np.kron(s0, -1j * sz); u3 = np.kron(s0, expm(-1j * np.pi / 3 * (sx + sy + sz) / np.sqrt(3)))
kk = rng.uniform(-np.pi, np.pi, 3); Ls = 5
e2 = np.abs(ham(np.array([-kk[0], -kk[1], kk[2]]), Ls, M0) - np.kron(u2, np.eye(Ls)) @ ham(kk, Ls, M0) @ np.kron(u2, np.eye(Ls)).conj().T).max()
e3 = min(np.abs(ham(kp, Ls, M0) - np.kron(u3, np.eye(Ls)) @ ham(kk, Ls, M0) @ np.kron(u3, np.eye(Ls)).conj().T).max()
         for kp in (kk[[2, 0, 1]], kk[[1, 2, 0]]))
noX = all(not wall_nodes(np.pi * np.array(c), 12, M0, 0, 0., gH / 2, True) for c in [(1, 0, 0), (1, 1, 0), (1, 1, 1)])
check("A6 [T] the slab Hamiltonian is covariant under the 12 tetrahedral rotations (C2 and C3 generators, spinor lift on Gamma_1..3); "
      "the wall carries NO state at X, M, R, so the corner-stabilizer premise (a walk-invariant light label at X and M) is void",
      e2 < 1e-13 and e3 < 1e-13 and noX, f"C2 {e2:.0e}, C3 {e3:.0e}; wall states at X/M/R: none")
tau = 1.0; Nk = 32; ks = 2 * np.pi * np.arange(Nk) / Nk
Ek = np.array([expm(-1j * tau * ham(np.array([q, 0.3, -0.7]), 4, M0)) for q in ks]); cr = np.fft.ifft(Ek, axis=0)
dec = [np.abs(cr[r]).max() for r in range(9)]
check("A7 [F] the exactly covariant tick exp(-i H tau) is exponentially (faster than exponentially) local: hop weight at distance r",
      all(dec[r + 1] < dec[r] for r in range(1, 8)) and dec[8] < 1e-6, "tau = 1: " + ", ".join(f"{x:.0e}" for x in dec))
ws = W3(lambda q: walk(q, 4, M0, TH), lambda q, j: walk(q, 4, M0, TH, j), 8)
check("A8 [T] where the W3 obstruction binds: the whole slab is a 3D walk built only from gates exp(-i theta h), so it is homotopic to 1 and W3 = 0 exactly (n0 = npi = 0 summed over both walls); one wall "
      "has (n0, npi) = (-1, 0), which no walk-invariant sector of any 3D walk can have (sector relation n0 = npi = -W3, control K): the "
      "light wall is not a walk sector, and the mirror is the far wall", abs(ws) < 1e-6, f"slab W3 (Ls = 4, 8^3) = {ws:.1e}")

print("== K. control: W3 integrator and the sector relation on U = (d0 + i d.sigma)/|d|, d0 = m - sum cos k, d = sin k")
def Ud(q, m):
    d0 = m - np.cos(q).sum(); d = np.sin(q); return (d0 * s0 + 1j * sum(d[i] * SIG[i] for i in range(3))) / np.sqrt(d0 ** 2 + d @ d)
def dUd(q, m, j, h=1e-6):
    e = np.zeros(3); e[j] = h; return (Ud(q + e, m) - Ud(q - e, m)) / (2 * h)
res = {}
for m in (2.0, 4.0):
    w = W3(lambda q: Ud(q, m), lambda q, j: dUd(q, m, j), 16); n = {0: 0, 1: 0}
    for c in itertools.product([0, np.pi], repeat=3):
        c = np.array(c); Uc = Ud(c, m)
        v = np.array([[np.real(np.trace(1j * Uc.conj().T @ dUd(c, m, j) @ SIG[a])) / 2 for a in range(3)] for j in range(3)])
        n[int(np.real(Uc[0, 0]) < 0)] += int(np.sign(np.linalg.det(v)))
    res[m] = (w, n)
check("K1 [T] the integrator returns integers and n0 = npi = -W3 (m = 2: W3 = -1, n0 = npi = +1; m = 4: all 0)",
      abs(res[2.0][0] + 1) < 1e-3 and res[2.0][1] == {0: 1, 1: 1} and abs(res[4.0][0]) < 1e-3 and res[4.0][1] == {0: 0, 1: 0},
      f"m=2 W3 {res[2.0][0]:.4f} n {res[2.0][1]}; m=4 W3 {res[4.0][0]:.0e}")

print("== B. modified chiral charges in a lattice Hamiltonian")
viol = []
for Ls in (6, 8, 10):
    Qw = np.kron(I4, np.diag(np.sign(np.arange(Ls) - (Ls - 1) / 2))); H = ham(np.zeros(3), Ls, M0); C = H @ Qw - Qw @ H
    w, V = np.linalg.eigh(H); low = V[:, np.argsort(np.abs(w))[:4]]
    supp = sorted({(a, b) for a in range(Ls) for b in range(Ls) if np.abs(C.reshape(4, Ls, 4, Ls)[:, a, :, b]).max() > 1e-13})
    viol.append((supp, np.abs(low.conj().T @ C @ low).max()))
mid = all(s == [(L_ // 2 - 1, L_ // 2), (L_ // 2, L_ // 2 - 1)] for (s, _), L_ in zip(viol, (6, 8, 10)))
r1, r2 = viol[1][1] / viol[0][1], viol[2][1] / viol[1][1]
check("B1 [T] the slab's layer-sign charge Q = sign(s - mid) is compact, quantised (+-1) and on-site in 3D, but not conserved: [H, Q] "
      "lives only on the middle bond, and between the wall modes it falls as |1-m|^Ls (the mirror leak is the anomaly's channel)",
      mid and abs(r2 - 0.16) < 0.005 and r1 > r2, f"middle-bond only: {mid}; low-mode element " +
      ", ".join(f"{x[1]:.1e}" for x in viol) + f" (Ls 6, 8, 10; ratio per 2 layers {r1:.3f} -> {r2:.3f}, target 0.16)")
kq = np.linspace(0, 2 * np.pi, 41)
qA = lambda q: np.array([[np.cos(q), 1j * np.sin(q)], [-1j * np.sin(q), -np.cos(q)]]); qV = np.diag([1., -1])
lvA = [np.linalg.eigvalsh(qA(q)) for q in kq]; lvR = [np.abs(np.linalg.eigvalsh((qV - qA(q)) / 2)).max() for q in kq]
check("B2 [T] recheck of the 1+1D template (staggered chain, BdG): the axial charge has levels +-1 (quantised, non-on-site, conserved), "
      "but the one-handed combination (Q_V - Q_A)/2 has levels |sin(k/2)| in [0, 1]: no compact one-handed U(1) to gauge",
      all(np.allclose(np.abs(l), 1) for l in lvA) and min(lvR) < 1e-12 and abs(max(lvR) - 1) < 1e-12, f"levels of q_R: {min(lvR):.0e} .. {max(lvR):.3f}")
print("   B3 [T, cited proof] Nielsen-Ninomiya for exponentially local H: analytic h(k) commuting with a one-body, number-conserving q(k) of"
      "\n      k-independent spectrum has analytic charge projectors (contour integral), so each charge sector is a smooth bundle on T^3 whose"
      "\n      slice Chern number is periodic in k3: net node chirality 0 per charge. Non-on-site is allowed; only non-compact or pairing charges escape.")

print("== C. the same circuit at larger steps: do anomalous (quasienergy-pi) boundary cones appear in a gapped bulk?")
rows = []
for th in (0.3, 0.7):
    c0, cp = bulk_gaps(M0, th); tc = trim_table(12, M0, th, 0.05)
    nL = {t: sum(v['L'][1] for (c, tt), v in tc.items() if tt == t and 'L' in v) for t in (0.0, 3.14)}
    rows.append((th, c0, cp, nL))
check("C1 [F] (pre-set form 'theta = 0.3 gapped, no pi cones' FAILED on the first run; recorded result) the circuit's bulk gap at 0 "
      "closes between theta = 0.2 and 0.3 (wall chirality flips to +1 there); the (-1, -3) wall pattern with cones at the three face corners "
      "at pi appears at theta = 0.7 only with a gapless bulk: no gapped anomalous phase in this family",
      max(rows[0][1], 0) < 1e-3 and rows[0][3][0.0] == 1 and rows[1][3] == {0.0: -1, 3.14: -3} and max(rows[1][1], rows[1][2]) < 1e-3,
      "; ".join(f"theta {r[0]}: gaps {r[1]:.1e}, {r[2]:.1e}, wall L {r[3]}" for r in rows))
wc = W3(lambda q: walk(q, 4, M0, 0.7), lambda q, j: walk(q, 4, M0, 0.7, j), 8)
check("C2 [T] for every step the circuit slab has W3 = 0 (homotopy to 1), so W3 can become a resource only through an index-carrying, "
      "non-circuit element; with a circuit the far-wall mirror is forced", abs(wc) < 1e-6, f"slab W3 at theta 0.7: {wc:.1e}")
print("Supplied: Wilson-type slab (Gamma basis, m = 0.6 in the window 0 < m < 2, theta = 0.2 / 0.3 / 0.7, tau = 1, Ls), free fields, momentum space.")
print("Open: gauging the light wall alone, or gapping the far wall by symmetric interactions (not attempted here).")
print(f"elapsed {time.time()-T0:.1f}s, peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.0f} MB")
print(f"TOTAL: PASS={P} FAIL={F}")
