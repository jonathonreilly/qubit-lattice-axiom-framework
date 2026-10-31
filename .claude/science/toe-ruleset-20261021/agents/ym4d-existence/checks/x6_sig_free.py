"""Check x6 (session 7): non-triviality of the soft OS space in the free Gaussian soft chain.

Criteria: checks/x6_criteria.md (written before this script). Reads no external files.
A: cross-plane covariance c(r) of a block flux (transfer formula, 4D FFT, continuum).
B: signal-to-noise bound Var E[f(D+eta)|D] <= (2/pi)||f||^2 s^2/tau^2; c(X) eigenvalues.
C: Monte Carlo of the free soft chain (one straight step + white noise) vs closed form.
D: informational: (F)-type mismatch vs constant couplings.
"""
import os, sys, time, math
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import numpy as np
from scipy import integrate, special

L = 3
t_start = time.time()
out = []
def pr(*a):
    s = " ".join(str(x) for x in a)
    print(s); out.append(s)

def D2(k, ell):
    """|sum_{j<ell} e^{-ikj}|^2."""
    s = np.sin(k / 2.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.where(np.abs(s) < 1e-15, float(ell) ** 2, (np.sin(k * ell / 2.0) / np.where(np.abs(s) < 1e-15, 1.0, s)) ** 2)
    return r

# ---------------- A1: transfer formula, infinite time ----------------
def c_transfer(r, N0=None, single_mode=False):
    ell = L ** r
    ns = 3 * ell
    k = 2 * np.pi * np.arange(ns) / ns
    kh2 = 4 * np.sin(k / 2) ** 2
    d2 = D2(k, ell)
    x0 = np.arange(ell, 2 * ell)
    total = 0.0
    if single_mode:
        idx = [(1, 0, 0), (ns - 1, 0, 0), (0, 1, 0), (0, ns - 1, 0)]
        for (i1, i2, i3) in idx:
            om2 = kh2[i1] + kh2[i2] + kh2[i3]
            E = np.arccosh(1 + om2 / 2)
            num = (kh2[i1] + kh2[i2]) * d2[i1] ** 2 * d2[i2] ** 2 * d2[i3]
            tsum = np.sum(np.exp(-E * x0))
            G = np.exp(-E) / (2 * np.sinh(E))
            total += num * ell ** -8 * tsum ** 2 * G
        return total / ns ** 3
    A12 = (kh2[:, None] + kh2[None, :])
    S12 = (d2[:, None] ** 2) * (d2[None, :] ** 2)
    om12 = kh2[:, None] + kh2[None, :]
    for i3 in range(ns):
        om2 = om12 + kh2[i3]
        num = A12 * S12 * d2[i3]
        mask = num > 0
        E = np.arccosh(1 + om2[mask] / 2)
        if N0 is None:
            tsum = np.exp(-E * ell) * (1 - np.exp(-E * ell)) / (1 - np.exp(-E))
            G = np.exp(-E) * tsum ** 2 / (2 * np.sinh(E))
        else:
            # periodic time: G(n) = cosh(E(N0/2 - n)) / (2 sinh E sinh(E N0/2)), n = x0 + x0' + 1
            n = x0[:, None] + x0[None, :] + 1
            G = np.zeros_like(E)
            for a in range(ell):
                for b in range(ell):
                    nn = n[a, b]
                    G += np.cosh(E * (N0 / 2 - nn)) / (2 * np.sinh(E) * np.sinh(E * N0 / 2))
        total += np.sum(num[mask] * G) * ell ** -8
    return total / ns ** 3

# ---------------- A2: 4D FFT on periodic lattice ----------------
def tent(ell):
    u = np.arange(2 * ell - 1)
    return np.minimum(u + 1, 2 * ell - 1 - u).astype(float)

def psi_array(ell, N0, ns, tblock=1):
    psi = np.zeros((N0, ns, ns, ns))
    m = tent(ell)
    prof = np.zeros(ns); prof[: 2 * ell - 1] = m
    b3 = np.zeros(ns); b3[:ell] = 1.0
    tt = np.zeros(N0); tt[tblock * ell:(tblock + 1) * ell] = 1.0
    psi = tt[:, None, None, None] * prof[None, :, None, None] * prof[None, None, :, None] * b3[None, None, None, :]
    return psi * ell ** -4

def symbol12(shape):
    ks = [2 * np.pi * np.fft.fftfreq(n) for n in shape]
    kh = [4 * np.sin(k / 2) ** 2 for k in ks]
    K0, K1, K2, K3 = np.meshgrid(*kh, indexing="ij")
    den = K0 + K1 + K2 + K3
    with np.errstate(divide="ignore", invalid="ignore"):
        S = np.where(den > 0, (K1 + K2) / np.where(den > 0, den, 1), 0.0)
    return S

def c_fft(ell, N0, ns, tblock=1):
    psi = psi_array(ell, N0, ns, tblock)
    t = np.arange(N0)
    th = psi[(-1 - t) % N0]
    S = symbol12(psi.shape)
    conv = np.real(np.fft.ifftn(np.fft.fftn(psi) * S))
    return float(np.sum(th * conv)), float(np.sum(psi * conv))

# ---------------- A3: continuum ----------------
def c_cont(Nt=30, single_mode=False):
    n = np.arange(-Nt, Nt + 1)
    q = 2 * np.pi * n / 3
    def sinc(x):
        return np.where(np.abs(x) < 1e-15, 1.0, np.sin(x) / np.where(np.abs(x) < 1e-15, 1, x))
    s1 = sinc(q / 2)
    total = 0.0
    if single_mode:
        pts = [(2 * np.pi / 3, 0, 0), (-2 * np.pi / 3, 0, 0), (0, 2 * np.pi / 3, 0), (0, -2 * np.pi / 3, 0)]
        for (a, b, c) in pts:
            Q = math.sqrt(a * a + b * b + c * c)
            sc = lambda x: 1.0 if x == 0 else math.sin(x) / x
            I = (math.exp(-Q) - math.exp(-2 * Q)) / Q
            total += (a * a + b * b) * sc(a / 2) ** 4 * sc(b / 2) ** 4 * sc(c / 2) ** 2 * I ** 2 / (2 * Q)
        return total / 27
    Q1, Q2 = np.meshgrid(q, q, indexing="ij")
    S12 = (s1[:, None] ** 4) * (s1[None, :] ** 4)
    for i3, q3 in enumerate(q):
        Qn = np.sqrt(Q1 ** 2 + Q2 ** 2 + q3 ** 2)
        num = (Q1 ** 2 + Q2 ** 2) * S12 * s1[i3] ** 2
        mask = num > 0
        Qm = Qn[mask]
        I = (np.exp(-Qm) - np.exp(-2 * Qm)) / Qm
        total += np.sum(num[mask] * I ** 2 / (2 * Qm))
    return total / 27

def cont_tail_bound(Nt):
    # terms with |n|_inf = R > Nt: count <= 26 R^2 (crude: (2R+1)^3-(2R-1)^3 = 24R^2+2), each <= |q| e^{-2|q|}/2 /27
    # (q_perp^2 <= |q|^2, sinc <= 1, I <= e^{-|q|}/|q|), |q| >= 2 pi R/3, |q| <= 2 pi sqrt3 R/3
    b = 0.0
    for R in range(Nt + 1, Nt + 400):
        qmin = 2 * np.pi * R / 3; qmax = qmin * math.sqrt(3)
        b += (24 * R * R + 2) * qmax * math.exp(-2 * qmin) / 2 / 27
    return b

pr("== A: cross-plane covariance c(r) of a block flux (unit coupling), block side 3^r, spatial torus 3 blocks ==")
cA = {}
for r in (1, 2, 3, 4):
    t0 = time.time()
    cA[r] = c_transfer(r)
    sm = c_transfer(r, single_mode=True)
    pr(f"A1 r={r}: c={cA[r]:.10e}  single-mode={sm:.6e}  c>=single: {cA[r] >= sm}  ({time.time()-t0:.1f}s)")
cinf = c_cont(30); smc = c_cont(single_mode=True); tb = cont_tail_bound(30)
pr(f"A3 continuum c_inf={cinf:.10e} (tail bound {tb:.2e}); single-mode continuum={smc:.6e}")
for r in (1, 2, 3, 4):
    pr(f"   r={r}: (c(r)-c_inf)/c_inf = {(cA[r]-cinf)/cinf:+.4e}")
A2ok = True
for r in (1, 2):
    ell = L ** r; ns = 3 * ell; N0 = 16 * ell
    cf, vf = c_fft(ell, N0, ns)
    ct = c_transfer(r, N0=N0)
    rel = abs(cf - ct) / abs(ct)
    A2ok &= rel <= 1e-9
    pr(f"A2 r={r}: FFT c={cf:.12e}  periodic transfer c={ct:.12e}  rel diff={rel:.2e}  ||Pi_ex psi||^2={vf:.6f}")
passA = all(cA[r] > 0 for r in cA) and A2ok and abs(cA[4] - cinf) / cinf <= 0.05
pr("A:", "PASS" if passA else "FAIL")

# ---------------- B ----------------
pr("== B1: signal-to-noise bound, scalar case ==")
gh_x, gh_w = np.polynomial.hermite_e.hermegauss(200)  # probabilists' Hermite, weight e^{-x^2/2}
gh_w = gh_w / np.sqrt(2 * np.pi)
def var_h(h, s):
    vals = h(s * gh_x)
    m = np.sum(gh_w * vals)
    return np.sum(gh_w * vals ** 2) - m ** 2
maxratio = 0.0; worst = None; nB = 0
tau = 1.0
for s in np.geomspace(0.01, 3.0, 25):
    bound = (2 / np.pi) * s ** 2 / tau ** 2
    for lam in np.geomspace(0.1, 30, 25):
        v1 = (1 + np.exp(-2 * lam ** 2 * s ** 2)) / 2 - np.exp(-lam ** 2 * s ** 2)
        v1 *= np.exp(-lam ** 2 * tau ** 2)
        v2 = (1 - np.exp(-2 * lam ** 2 * s ** 2)) / 2 * np.exp(-lam ** 2 * tau ** 2)
        for name, v in (("cos", v1), ("sin", v2)):
            nB += 1
            if v / bound > maxratio: maxratio, worst = v / bound, (name, s, lam)
    # sign: h(x) = erf(x/(tau sqrt2)); exact Var = E erf^2(D/(tau sqrt 2)) = (2/pi) arcsin(s^2/(s^2+tau^2))  [Gaussian identity]
    v3 = (2 / np.pi) * np.arcsin(s ** 2 / (s ** 2 + tau ** 2))
    v3q = var_h(lambda x: special.erf(x / (tau * np.sqrt(2))), s)
    nB += 1
    if v3 / bound > maxratio: maxratio, worst = v3 / bound, ("sign", s, None)
    if abs(v3 - v3q) > 1e-6: pr(f"   warning: sign closed form vs quadrature {v3} {v3q}")
    for a in np.linspace(-2, 2, 21):
        h = lambda x, a=a: special.ndtr((x - a) / tau)
        v4 = integrate.quad(lambda x: special.ndtr((x - a) / tau) ** 2 * np.exp(-x * x / (2 * s * s)) / (s * np.sqrt(2 * np.pi)), -12 * s, 12 * s, epsabs=1e-14, limit=200)[0] \
             - special.ndtr(-a / np.sqrt(s * s + tau * tau)) ** 2
        nB += 1
        if v4 / bound > maxratio: maxratio, worst = v4 / bound, ("ind", s, a)
pr(f"B1: {nB} cases, max Var/bound = {maxratio:.6f} at {worst}")
passB1 = maxratio <= 1 + 1e-9

pr("== B2: c(X) = smallest nonzero eigenvalue of P_X d d^* P_X (periodic 4^4) ==")
n = 4
def lid(x, mu):
    return ((((x[0] % n) * n + x[1] % n) * n + x[2] % n) * n + x[3] % n) * 4 + mu
def e(mu):
    v = [0, 0, 0, 0]; v[mu] = 1; return v
def add(x, y): return [a + b for a, b in zip(x, y)]
def plaq_row(x, mu, nu):
    row = np.zeros(4 * n ** 4)
    row[lid(x, mu)] += 1; row[lid(add(x, e(mu)), nu)] += 1
    row[lid(add(x, e(nu)), mu)] -= 1; row[lid(x, nu)] -= 1
    return row
o = [0, 0, 0, 0]
shapes = {
    "one plaquette": [(o, 1, 2)],
    "two, shared link, same plane": [(o, 1, 2), (e(1), 1, 2)],
    "two, shared link, different planes": [(o, 1, 2), (o, 1, 3)],
    "2x2 planar square": [(o, 1, 2), (e(1), 1, 2), (e(2), 1, 2), (add(e(1), e(2)), 1, 2)],
    "six faces of a 3-cube": [(o, 1, 2), (e(3), 1, 2), (o, 1, 3), (e(2), 1, 3), (o, 2, 3), (e(1), 2, 3)],
}
passB2 = True
for name, X in shapes.items():
    M = np.array([plaq_row(x, a, b) for (x, a, b) in X])
    ev = np.linalg.eigvalsh(M @ M.T)
    nz = ev[ev > 1e-9]
    pr(f"B2 {name}: dim V_X={len(nz)} of |X|={len(X)}, c(X)={nz.min():.6f}")
    passB2 &= nz.min() > 1e-9
    if name == "one plaquette": passB2 &= abs(nz.min() - 4) < 1e-12
    if name == "six faces of a 3-cube": passB2 &= len(nz) == 5
pr("B:", "PASS" if (passB1 and passB2) else "FAIL")

# ---------------- C: Monte Carlo ----------------
pr("== C: Monte Carlo of the free soft chain (fine 54 x 9^3, one straight step) ==")
N0, ns = 54, 9
shape = (N0, ns, ns, ns)
ks = [2 * np.pi * np.fft.fftfreq(m) for m in shape]
kh = [4 * np.sin(k / 2) ** 2 for k in ks]
KK = np.meshgrid(*kh, indexing="ij")
den = KK[0] + KK[1] + KK[2] + KK[3]
with np.errstate(divide="ignore"):
    amp = np.where(den > 0, 1 / np.sqrt(np.where(den > 0, den, 1)), 0.0)
cP, vP = c_fft(3, N0, ns)
pr(f"C closed-form inputs (r=1, N0=54): <theta psi, Pi_ex psi>={cP:.8e}, <psi, Pi_ex psi>={vP:.8e}")
rng = np.random.default_rng(20261028)
def sample_Y(g0, sig2):
    A = []
    for mu in range(4):
        w = rng.standard_normal(shape)
        A.append(g0 * np.real(np.fft.ifftn(np.fft.fftn(w) * amp)))
    B = []
    for mu in range(4):
        s = A[mu] + np.roll(A[mu], -1, axis=mu) + np.roll(A[mu], -2, axis=mu)
        s = s.reshape(N0 // 3, 3, ns // 3, 3, ns // 3, 3, ns // 3, 3).sum(axis=(1, 3, 5, 7)) / 81.0
        s = s + np.sqrt(sig2) * rng.standard_normal(s.shape)
        B.append(s)
    Y = B[1] + np.roll(B[2], -1, axis=1) - np.roll(B[1], -1, axis=2) - B[2]
    return Y
passC = True
for name, g0, sig2, nsamp in (("C1", 1.0, 0.05, 40000), ("C2", 0.05, 0.05, 40000)):
    t0 = time.time()
    v = g0 ** 2 * vP + 4 * sig2
    c = g0 ** 2 * cP
    lam = 1 / np.sqrt(v)
    exact = np.exp(-lam ** 2 * (v - c)) - np.exp(-lam ** 2 * v)
    S1 = np.empty(nsamp, complex); S2 = np.empty(nsamp, complex)
    T = N0 // 3
    p = np.arange(T)
    for i in range(nsamp):
        Y = sample_Y(g0, sig2)
        Yp = Y[(p + 1) % T]; Yt = Y[(p - 2) % T]
        S1[i] = np.mean(np.exp(1j * lam * (Yp - Yt)))
        S2[i] = np.mean(np.exp(1j * lam * Y))
    m2 = S2.mean()
    Z = S1.real - 2 * np.real(np.conj(m2) * S2)
    est = S1.real.mean() - abs(m2) ** 2
    se = Z.std(ddof=1) / np.sqrt(nsamp)
    z = (est - exact) / se
    ok = abs(z) <= 4
    if name == "C1":
        ok &= exact / se > 5
    passC &= ok
    pr(f"{name}: g0={g0}, sigma^2={sig2}, lambda={lam:.4f}, v={v:.6f}, c={c:.6e}: MC Q={est:.6e} +- {se:.2e}, "
       f"closed form {exact:.6e}, z={z:+.2f}, closed/SE={exact/se:.1f}, Var-term check E e^(i lam Y)={m2.real:.5f} vs {np.exp(-lam**2*v/2):.5f}  ({time.time()-t0:.0f}s)")
pr("C:", "PASS" if passC else "FAIL")

# ---------------- D: informational ----------------
pr("== D (informational): sup_lambda Q, (F)-type mismatch vs constant couplings; m=2, kappa=20, beta=0.37, g=1 ==")
v1 = vP  # ||Pi_ex psi||^2 at r=1 (finite-volume proxy)
c1 = cinf
kap, beta, g2, m = 20.0, 0.37, 1.0, 2
def gr2(rr): return 1.0 / (1.0 / g2 + beta * rr * math.log(L))
def Nnoise(Kc):
    return (4 / 3) * sum(gr2(m + 1 + nn) / kap * (2 * L ** (-2 * nn) + L ** (-4 * nn)) for nn in range(Kc - m))
def supQ(c, v):
    xs = np.geomspace(1e-3, 1e4, 4000) / max(v, 1e-12)
    return float(np.max(np.exp(-xs * v) * (np.exp(xs * c) - 1)))
for Kc in (5, 10, 30, 100, 1000, 10000):
    g02 = 1.0 / (1.0 / g2 + beta * Kc * math.log(L))
    qF = supQ(g02 * c1, g02 * v1 + Nnoise(Kc))
    qC = supQ(g2 * c1, g2 * v1 + (4 / 3) * sum(g2 / kap * (2 * L ** (-2 * nn) + L ** (-4 * nn)) for nn in range(Kc - m)))
    pr(f"D K={Kc}: (F)-type sup Q={qF:.4e} (g0^2={g02:.4e}, K*supQ={Kc*qF:.4f});  constant couplings sup Q={qC:.4e}")

allpass = passA and passB1 and passB2 and passC
pr("OVERALL:", "PASS" if allpass else "FAIL")
pr(f"wall time {time.time()-t_start:.1f}s")
