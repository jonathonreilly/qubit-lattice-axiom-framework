"""T-X3: OS-reconstructed single-particle spectrum of the free overlap fermion on Z^4.

Pre-registered in ../PREREG.md (incl. Amendment A1) before this script was run.
For each spatial momentum p the Euclidean time correlator C(t;p) = int dp4/2pi e^{ip4 t} D^{-1}
is computed by a direct p4 sum (N4 points) and compared with the analytic decomposition
  light pole (lambda = e^{-E}, sinh E = S, iff beta < sqrt(1+S^2))  +  cut (would-be doublers).
Positivity is tested both on the analytic densities and model-independently on block Hankel
matrices of Gamma*C(t). Controls: Wilson r=1 m=+0.5 (POS), naive m=+0.5 (NEG1),
Wilson r=1 m=-1.5 (CMP).
numpy only; small memory.
"""
import numpy as np, itertools, sys

np.set_printoptions(linewidth=160, precision=4)
s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2); Z2 = np.zeros((2, 2))
def blk(a, b, c, d): return np.block([[a, b], [c, d]])
gk = [blk(Z2, -1j * s, 1j * s, Z2) for s in (s1, s2, s3)]
g4 = blk(Z2, I2, I2, Z2)
G = gk + [g4]
g5 = G[0] @ G[1] @ G[2] @ G[3]
for a in range(4):
    for b in range(4):
        ac = G[a] @ G[b] + G[b] @ G[a]
        assert np.allclose(ac, 2 * (a == b) * np.eye(4))
    assert np.allclose(G[a], G[a].conj().T)
print("gamma5 diag:", np.round(np.diag(g5).real, 12), " offdiag max", np.abs(g5 - np.diag(np.diag(g5))).max())
I4 = np.eye(4)
N4 = 4096
p4 = 2 * np.pi * np.arange(N4) / N4
TMAX = 16

def dirac_symbol(kind, p, par):
    """returns D(p4) array (N4,4,4) for spatial p"""
    s = [np.sin(p[0]), np.sin(p[1]), np.sin(p[2])]
    cs = sum(1 - np.cos(pk) for pk in p)
    sp = sum(s[k] * gk[k] for k in range(3))
    s4 = np.sin(p4)[:, None, None]; c4 = np.cos(p4)[:, None, None]
    if kind == "overlap":
        M = par
        b = cs + 1 - c4 - M
        X = 1j * (sp[None] + s4 * g4[None]) + b * I4[None]
        om = np.sqrt(s4 ** 2 + sum(x * x for x in s) + b ** 2)
        return I4[None] + X / om
    if kind == "wilson":
        m = par
        return 1j * (sp[None] + s4 * g4[None]) + (cs + 1 - c4 + m) * I4[None]
    if kind == "naive":
        m = par
        return 1j * (sp[None] + s4 * g4[None]) + m * I4[None]

def corr(kind, p, par):
    Dinv = np.linalg.inv(dirac_symbol(kind, p, par))
    ts = np.arange(0, TMAX + 1)
    ph = np.exp(1j * np.outer(ts, p4))  # (T,N4)
    return np.einsum('tk,kab->tab', ph, Dinv) / N4

# Gauss-Legendre on u in [0, U], E = E1 + u^2
xg, wg = np.polynomial.legendre.leggauss(3000)
def cut_term(p, M, ts):
    s = np.array([np.sin(pk) for pk in p]); S2 = float(s @ s)
    beta = 1 - M + sum(1 - np.cos(pk) for pk in p)
    sp = sum(s[k] * gk[k] for k in range(3))
    if abs(beta) < 1e-14:
        return np.zeros((len(ts), 4, 4), complex), None, beta
    ch1 = (1 + S2 + beta ** 2) / (2 * abs(beta)); E1 = np.arccosh(ch1)
    U = np.sqrt(60.0 / 1.0)
    u = 0.5 * U * (xg + 1); w = 0.5 * U * wg
    E = E1 + u ** 2; jac = 2 * u
    omabs = np.sqrt(np.maximum(2 * abs(beta) * np.cosh(E) - 1 - S2 - beta ** 2, 0.0))
    den = np.sinh(E) ** 2 - S2
    scal = omabs / den * jac * w / (2 * np.pi)
    out = np.zeros((len(ts), 4, 4), complex)
    for i, t in enumerate(ts):
        if beta > 0:
            mat_w = np.exp(-E * t) * scal
            A = np.einsum('e,ab->ab', mat_w * np.sinh(E), g4) - 1j * mat_w.sum() * sp
        else:
            mat_w = (-1) ** (t - 1) * np.exp(-E * t) * scal
            A = np.einsum('e,ab->ab', mat_w * np.sinh(E), g4) + 1j * mat_w.sum() * sp
        out[i] = A
    return out, E1, beta

def pole_term(p, M, ts):
    s = np.array([np.sin(pk) for pk in p]); S2 = float(s @ s); S = np.sqrt(S2)
    beta = 1 - M + sum(1 - np.cos(pk) for pk in p)
    sp = sum(s[k] * gk[k] for k in range(3))
    out = np.zeros((len(ts), 4, 4), complex)
    if not (beta < np.sqrt(1 + S2)) or S2 == 0:
        return out, None
    E = np.arcsinh(S)
    R = (np.cosh(E) - beta) / np.sinh(2 * E) * (g4 * np.sinh(E) - 1j * sp)
    for i, t in enumerate(ts):
        out[i] = np.exp(-E * t) * R
    return out, E

def hankel(C, n, shift):
    """block Hankel H_ij = Gamma C(i+j-1+shift), i,j=1..n  (C indexed by t)"""
    H = np.zeros((4 * n, 4 * n), complex)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            H[4 * (i - 1):4 * i, 4 * (j - 1):4 * j] = C[i + j - 1 + shift]
    return H

GAMMAS = {"+g4 L": lambda C: np.einsum('ab,tbc->tac', g4, C), "-g4 L": lambda C: -np.einsum('ab,tbc->tac', g4, C),
          "+g4 R": lambda C: np.einsum('tab,bc->tac', C, g4), "-g4 R": lambda C: -np.einsum('tab,bc->tac', C, g4)}

def psd_stats(H):
    Hh = 0.5 * (H + H.conj().T); herm = np.abs(H - H.conj().T).max() / max(np.abs(H).max(), 1e-300)
    ev = np.linalg.eigvalsh(Hh)
    return ev.min() / ev.max(), herm, ev

def hankel_rank(GC, n, tol=1e-11):
    ev = np.linalg.eigvalsh(0.5 * (hankel(GC, n, 0) + hankel(GC, n, 0).conj().T))
    return int((np.abs(ev) > tol * np.abs(ev).max()).sum())

rng = np.random.default_rng(20261014)
def test_momenta():
    P = []
    for _ in range(30):
        P.append(tuple(rng.uniform(-np.pi, np.pi, 3)))
    for c in itertools.product([0, np.pi], repeat=3):
        if c != (0, 0, 0):
            P.append(c)  # exact spatial doubler corners
        P.append(tuple(np.array(c) + rng.normal(0, 0.15, 3)))  # near every corner incl. p~0
    P.append((0.2, 0.0, 0.0)); P.append((0.1, 0.1, 0.0)); P.append((0.05, 0.03, 0.02))
    return P

print("=" * 100)
print("STEP 0: calibrate the reflection convention on the POS control (Wilson r=1, m=+0.5)")
Pcal = [(0.3, 0.2, -0.1), (1.0, 0.0, 2.0), (np.pi, 0, 0), (2.5, -1.2, 0.4)]
ok = {}
for name, f in GAMMAS.items():
    worst = 1.0; hm = 0
    for p in Pcal:
        GC = f(corr("wilson", p, 0.5))
        r0, h0, _ = psd_stats(hankel(GC, 5, 0)); r1, h1, _ = psd_stats(hankel(GC, 5, 1))
        worst = min(worst, r0, r1); hm = max(hm, h0, h1)
    ok[name] = (worst, hm)
    print(f"  Gamma={name}: min eig/max over link(H0)&shift(H1) = {worst:+.3e}; herm defect {hm:.1e}")
cands = [k for k, v in ok.items() if v[0] > -1e-10 and v[1] < 1e-8]
print("  admissible conventions:", cands)
if not cands:
    print("TEST BROKEN: no convention makes POS PSD"); sys.exit(1)
GAM = cands[0]; Gf = GAMMAS[GAM]
print("  USING Gamma =", GAM)

print("=" * 100)
print("STEP 1: controls with the fixed convention (H0 = link form, H1 = shifted form, n=6)")
for kind, par, lab in [("wilson", 0.5, "POS Wilson r=1 m=+0.5"), ("naive", 0.5, "NEG1 naive m=+0.5"),
                       ("wilson", -1.5, "CMP Wilson r=1 m=-1.5")]:
    for p in [(0.3, 0.2, -0.1), (np.pi, 0.0, 0.0), (0.05, 0.03, 0.02)]:
        GC = Gf(corr(kind, p, par))
        r0, h0, _ = psd_stats(hankel(GC, 6, 0)); r1, h1, _ = psd_stats(hankel(GC, 6, 1))
        alt = np.abs(GC[1:TMAX:2]).max(), np.abs(GC[2:TMAX:2]).max()
        ranks = [hankel_rank(GC, n) for n in range(2, 7)]
        print(f"  {lab:24s} p={np.round(p,3)}  H0 min/max={r0:+.2e}  H1 min/max={r1:+.2e}  rank(H0,n=2..6)={ranks}")

print("=" * 100)
print("STEP 2: overlap -- decomposition check, positivity, Hankel rank")
summary = {}
for M in [0.5, 1.0, 1.5, 1.9]:
    ts = np.arange(1, TMAX + 1)
    maxres = 0; worstH0 = 1; worstH1 = 1; npole = 0; npi = 0; minE1 = 9; minEp = 9; rk = []
    weyl_ranks = set(); corner_pole = []
    for p in test_momenta():
        C = corr("overlap", p, M)
        Pt, Ep = pole_term(p, M, ts)
        Ct, E1, beta = cut_term(p, M, ts)
        Cpred = Pt + Ct
        res = np.abs(C[1:] - Cpred).max() / np.abs(C[1:]).max()
        maxres = max(maxres, res)
        is_corner = all(abs(abs(x) - np.pi) < 1e-12 or abs(x) < 1e-12 for x in p)
        if Ep is not None:
            npole += 1; minEp = min(minEp, Ep)
            # rank of light residue in Weyl blocks (Gamma-weighted)
            R = Gf(Pt[:1])[0] * np.exp(Ep)
            ev = np.linalg.eigvalsh(0.5 * (R + R.conj().T))
            rL = int((np.abs(np.linalg.eigvalsh(0.5 * (R[:2, :2] + R[:2, :2].conj().T))) > 1e-10 * np.abs(ev).max()).sum())
            rR = int((np.abs(np.linalg.eigvalsh(0.5 * (R[2:, 2:] + R[2:, 2:].conj().T))) > 1e-10 * np.abs(ev).max()).sum())
            rD = int((np.abs(ev) > 1e-10 * np.abs(ev).max()).sum())
            weyl_ranks.add((rD, rL, rR, bool(ev.min() > -1e-12 * ev.max()), np.abs(R[:2, 2:]).max() < 1e-12))
            if is_corner: corner_pole.append(p)
        if E1 is not None:
            minE1 = min(minE1, E1)
            if beta < 0: npi += 1
        GC = Gf(C)
        r0, _, _ = psd_stats(hankel(GC, 6, 0)); r1, _, _ = psd_stats(hankel(GC, 6, 1))
        worstH0 = min(worstH0, r0); worstH1 = min(worstH1, r1)
        if len(rk) < 3 and Ep is None and E1 is not None and E1 < 1.5:
            rk.append((tuple(np.round(p, 2)), [hankel_rank(GC, n) for n in range(2, 9)]))
    print(f" M={M}: max rel residual (FFT vs pole+cut) = {maxres:.2e}; #p with light pole {npole}/{len(test_momenta())};"
          f" min E_pole {minEp:.3f}; pole at an exact doubler corner: {corner_pole}")
    print(f"        #p with pi-type (lambda<0) cut: {npi}; min E1 over test set {minE1:.3f};"
          f" worst H0 min/max {worstH0:+.2e}; worst H1 min/max {worstH1:+.2e}")
    print(f"        light residue (Gamma-weighted) ranks (Dirac, Weyl-, Weyl+, PSD, block-diag): {weyl_ranks}")
    print(f"        Hankel rank of H0 for n=2..8 at continuum-only momenta: {rk}")
    # Wilson comparator rank at same momentum
    if rk:
        pW = rk[0][0]; GCw = Gf(corr("wilson", pW, 0.5))
        print(f"        (POS Wilson at same p: ranks n=2..8 = {[hankel_rank(GCw, n) for n in range(2, 9)]})")
    summary[M] = dict(maxres=maxres, worstH0=worstH0, worstH1=worstH1, npi=npi, minE1=minE1)

print("=" * 100)
print("STEP 3: closed-form spectrum over the full 16^3 spatial grid + exact corners")
L = 16
ks = 2 * np.pi * np.arange(L) / L
PX, PY, PZ = np.meshgrid(ks, ks, ks, indexing='ij')
S2 = np.sin(PX) ** 2 + np.sin(PY) ** 2 + np.sin(PZ) ** 2
CS = (1 - np.cos(PX)) + (1 - np.cos(PY)) + (1 - np.cos(PZ))
for M in [0.5, 1.0, 1.5, 1.9]:
    beta = 1 - M + CS
    haspole = (beta < np.sqrt(1 + S2)) & (S2 > 0)
    Ep = np.where(haspole, np.arcsinh(np.sqrt(S2)), np.nan)
    with np.errstate(divide='ignore', invalid='ignore'):
        E1 = np.where(np.abs(beta) > 1e-14, np.arccosh((1 + S2 + beta ** 2) / (2 * np.abs(beta))), np.inf)
    corners = [(i, j, k) for i in (0, L // 2) for j in (0, L // 2) for k in (0, L // 2)]
    cE1 = {c: round(float(E1[c]), 3) for c in corners}
    cpole = [c for c in corners if c != (0, 0, 0) and haspole[c]]
    # connectedness / location of pole region: max |p| (periodic distance to 0) inside region
    dist = np.sqrt(np.minimum(PX, 2 * np.pi - PX) ** 2 + np.minimum(PY, 2 * np.pi - PY) ** 2 + np.minimum(PZ, 2 * np.pi - PZ) ** 2)
    light = haspole & (Ep < 0.3)
    print(f" M={M}: pole region: {int(haspole.sum())}/{L**3-1} momenta, max dist from p=0 inside = {np.nanmax(np.where(haspole, dist, np.nan)):.3f};"
          f" light (E_p<0.3) momenta max dist {np.nanmax(np.where(light, dist, np.nan)):.3f}")
    print(f"        doubler corners with a pole: {cpole}; E1 at corners: {cE1}")
    print(f"        min E1 over grid = {np.min(E1):.4f}; #grid momenta with pi-type cut (beta<0) = {int((beta < 0).sum())};"
          f" min E1 over beta<0 = {np.min(np.where(beta < 0, E1, np.inf)):.4f}")
    # pole merging: is E_p < E1 wherever pole exists?
    print(f"        check E_pole < E1 wherever pole exists: {bool(np.all(Ep[haspole] < E1[haspole]))};"
          f" min gap E1-E_pole = {np.min(E1[haspole]-Ep[haspole]):.4f}")
# fine continuous minimisation of E1 for M=1 over the BZ
best = 9
for _ in range(20000):
    p = rng.uniform(-np.pi, np.pi, 3)
    S2_ = float(np.sum(np.sin(p) ** 2)); b_ = float(np.sum(1 - np.cos(p)))
    if b_ > 1e-12:
        best = min(best, np.arccosh((1 + S2_ + b_ ** 2) / (2 * b_)))
print(f" M=1 random-search min E1 over BZ (20000 pts): {best:.4f}  (ln 2 = {np.log(2):.4f})")
print("done")
