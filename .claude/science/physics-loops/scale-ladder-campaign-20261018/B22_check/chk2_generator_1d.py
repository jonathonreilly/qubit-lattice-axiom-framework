"""B22 check 2: 1D Dirac walk, generator lapse (Definition B), by a different path from B22's runner:
the step is built as a DENSE real-space matrix from its two gate layers (own code), H_F = i log W is
obtained from a complex Schur decomposition of that matrix (no Bloch eigensolver), lapses are dense
diagonal matrices, the bracket is a dense commutator, and the predictions use ANALYTIC omega(k)
(cos omega = cos theta cos k, derived from tr W(k) = 2 cos theta cos k) and analytic derivatives.

Model (same physics as B22): sites 2i = a_i, 2i+1 = b_i; layer 1 on (a_i, b_i): [[-i s, c], [c, -i s]];
layer 2 on (b_i, a_{i+1}): swap.  Lapse is cell-diagonal (same value on a_i, b_i), cell coordinate X = i.
"""
import time
import numpy as np
from scipy.linalg import schur, expm

PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"\n        {detail}" if detail else ""))
t0 = time.time()

def step_matrix(Lc, th):
    n = 2 * Lc; c, s = np.cos(th), np.sin(th)
    U1 = np.zeros((n, n), complex); U2 = np.zeros((n, n), complex)
    for i in range(Lc):
        a, b = 2 * i, 2 * i + 1
        U1[a, a] = -1j * s; U1[a, b] = c; U1[b, a] = c; U1[b, b] = -1j * s
        a2 = (2 * i + 2) % n
        U2[b, a2] = 1; U2[a2, b] = 1
    return U2 @ U1

def floquet_generator(W, shift=0.0):
    T, Z = schur(np.exp(1j * shift) * W, output='complex')
    lam = np.diag(T)
    offd = np.abs(T - np.diag(lam)).max()
    om = -np.angle(lam)                     # W u = e^{-i om} u, principal branch
    return (Z * om) @ Z.conj().T, offd

def omega(k, th): return np.arccos(np.cos(th) * np.cos(k))
def omega_d(k, th):
    o = omega(k, th); return np.cos(th) * np.sin(k) / np.sin(o)
def gfun(k, th):            # (1/2) d^2 omega^2 / dk^2, analytic
    o = omega(k, th); d = omega_d(k, th)
    return d**2 + o * np.cos(o) * (1 - d**2) / np.sin(o)

def kspace_op(Lc, f):       # cell-momentum multiplier f(k) acting identically on a and b
    k = 2 * np.pi * np.fft.fftfreq(Lc)
    F = np.fft.fft(np.eye(Lc), axis=0) / np.sqrt(Lc)        # F[k, x]
    O = F.conj().T @ np.diag(f(k)) @ F
    return np.kron(O, np.eye(2))

def low_proj(Lc, kc, center=0.0):
    return kspace_op(Lc, lambda k: (np.abs((k - center + np.pi) % (2 * np.pi) - np.pi) < kc).astype(float))

anti = lambda A, B: A @ B + B @ A

# ---------------------------------------------------------------- dispersion
for th in (0.0, 0.5, 1.0):
    W = step_matrix(64, th)
    ev = np.sort(np.abs(np.angle(np.linalg.eigvals(W))))
    k = 2 * np.pi * np.fft.fftfreq(64)
    ref = np.sort(np.r_[omega(k, th), omega(k, th)])
    if th == 0.0: errd = 0
    errd = max(errd, np.abs(ev - ref).max())
check("D1 [exact identity, numerical] the dense step's eigenphases are +-arccos(cos theta cos k)"
      " (tr W(k) = 2 cos theta cos k, det W(k) = 1)", errd < 1e-10, f"max deviation {errd:.1e}")
th_ = np.array([0.2, 0.5, 1.0])
check("D2 [analytic] (1/2) d^2 omega^2/dk^2 at k = 0 equals theta cot theta (omega'' = cot theta at the gap minimum)",
      np.allclose(gfun(1e-6, th_), th_ / np.tan(th_), rtol=1e-6), f"{gfun(1e-6, th_)} vs {th_ / np.tan(th_)}")

# ---------------------------------------------------------------- bracket on the low-energy subspace
Lc = 256; n = 2 * Lc; X = np.repeat(np.arange(Lc, dtype=float), 2)
print("\n  bracket, dense, Lc = 256; relative error of P(K - pred)P, P = |k| < 0.15 (both bands)")
print("  theta  lapses            err(first-order symbol)   err(-i v^2 G[w], v^2 = th cot th)   err(v = 1)")
res = {}
for th in (0.0, 0.5, 1.0):
    W = step_matrix(Lc, th); H, offd = floquet_generator(W)
    P = low_proj(Lc, 0.15)
    Q = kspace_op(Lc, lambda k: omega(k, th) * omega_d(k, th) * (1 if th > 0 else 1))
    if th == 0.0:
        Q = kspace_op(Lc, lambda k: np.where(np.abs(k) < np.pi - 1e-9, k, 0.0))      # omega = |k|: omega omega' = k
    pop = kspace_op(Lc, lambda k: k)
    v2 = 1.0 if th == 0 else th / np.tan(th)
    for lab, mk in (("cos,sin (uniform w)", 0), ("cos q1, cos q2 (non-uniform w)", 1)):
        for mult in (1, 2):
            if mk == 0:
                q = 2 * np.pi * 2 * mult / Lc
                Nv, Mv = np.cos(q * X), np.sin(q * X); wv = q * np.ones(n)
            else:
                q1, q2 = 2 * np.pi * 2 * mult / Lc, 2 * np.pi * 3 * mult / Lc
                Nv, Mv = np.cos(q1 * X), np.cos(q2 * X)
                wv = Nv * (-q2 * np.sin(q2 * X)) - Mv * (-q1 * np.sin(q1 * X))
            HN = 0.5 * (Nv[:, None] * H + H * Nv[None, :]); HM = 0.5 * (Mv[:, None] * H + H * Mv[None, :])
            K = HN @ HM - HM @ HN
            wd = np.diag(wv)
            pred = -0.5j * anti(wd, Q); dirac = -0.5j * v2 * anti(wd, pop); lc = -0.5j * anti(wd, pop)
            nr = lambda A: np.linalg.norm(P @ A @ P)
            e = [nr(K - x) / nr(x) for x in (pred, dirac, lc)]
            res[(th, mk, mult)] = e
            if mult == 1:
                print(f"  {th:.1f}   {lab:31s}  {e[0]:.2e}                  {e[1]:.2e}                       {e[2]:.2e}")
ok = all(res[(th, mk, 1)][0] < 2e-3 for th in (0.0, 0.5, 1.0) for mk in (0, 1))
sc = all(res[(th, mk, 2)][0] / res[(th, mk, 1)][0] > 3.0 for th in (0.5, 1.0) for mk in (0, 1))
check("B1 [numerical, own dense implementation] generator bracket = -i(1/2){w, Op(omega omega')} on |k| < 0.15,"
      " for uniform AND non-uniform w; residual scales ~ q^2 (x>3 on doubling q) for the massive walk", ok and sc,
      "; ".join(f"th={th}: {res[(th,0,1)][0]:.1e}/{res[(th,1,1)][0]:.1e} -> 2q {res[(th,0,2)][0]:.1e}/{res[(th,1,2)][0]:.1e}"
                for th in (0.0, 0.5, 1.0)))
okd = all(res[(th, mk, 1)][1] < 0.02 for th in (0.5, 1.0) for mk in (0, 1))
disc = all(res[(th, mk, 1)][2] > 5 * res[(th, mk, 1)][1] for th in (0.5, 1.0) for mk in (0, 1))
check("B2 [numerical] low-energy bracket is -i v^2 G[w] with v^2 = theta cot theta (node cone), not v = 1 (causal cone)",
      okd and disc)

# ---------------------------------------------------------------- k ~ pi species, momentum offset, W^2 generator
th = 0.5; v2 = th / np.tan(th)
W = step_matrix(Lc, th)
H1, _ = floquet_generator(W); H2, _ = floquet_generator(W @ W)
Ppi = low_proj(Lc, 0.15, center=np.pi)
q = 2 * np.pi * 2 / Lc; Nv, Mv = np.cos(q * X), np.sin(q * X); wd = q * np.eye(n)
prel = kspace_op(Lc, lambda k: (k - np.pi + np.pi) % (2 * np.pi) - np.pi)
plat = kspace_op(Lc, lambda k: np.mod(k, 2 * np.pi))            # lattice momentum branch [0, 2pi): ~pi near the node
def brk(H):
    HN = 0.5 * (Nv[:, None] * H + H * Nv[None, :]); HM = 0.5 * (Mv[:, None] * H + H * Mv[None, :]); return HN @ HM - HM @ HN
nr = lambda A: np.linalg.norm(Ppi @ A @ Ppi)
K1, K2 = brk(H1), brk(H2)
e_prin = nr(K1 + 0.5j * v2 * anti(wd, prel)) / nr(0.5j * v2 * anti(wd, prel))
pred_ratio = np.pi / th
e2_rel = nr(K2 + 0.5j * 4 * v2 * anti(wd, prel)) / nr(0.5j * 4 * v2 * anti(wd, prel))
e2_lat = nr(K2 + 0.5j * 4 * v2 * anti(wd, plat)) / nr(0.5j * 4 * v2 * anti(wd, prel))
check("B3 [numerical + analytic] species at k ~ pi: principal-branch generator misses -i v^2 G[w] by ~ pi/theta"
      " (it is the E0 = pi offset term of M5a: (1/2)d(omega^2) with omega = pi - omega~ gives -(pi - theta)/theta x);"
      " the W^2 generator gives 4 v^2 G[w] when G uses the momentum RELATIVE to the node, and fails grossly with the"
      " lattice momentum (the M5b k* term)", abs(e_prin - pred_ratio) / pred_ratio < 0.05 and e2_rel < 0.02 and e2_lat > 10,
      f"principal: rel. dev {e_prin:.3f} vs pi/theta = {pred_ratio:.3f}; W^2: relative-momentum G {e2_rel:.1e},"
      f" lattice-momentum G {e2_lat:.1f}")

# ---------------------------------------------------------------- gapless: W^N for non-integer N
W0 = step_matrix(512, 0.0); H0, _ = floquet_generator(W0)
Wh = expm(-0.5j * H0)                                 # constant lapse 1/2 (Definition B's W_N)
row = np.abs(Wh[512, :]).reshape(-1, 2).max(axis=1)   # cell-resolved |<x|W^{1/2}|x0>|
r = np.arange(1, 120); amp = np.array([max(row[(256 + rr) % 512], row[(256 - rr) % 512]) for rr in r])
sel = amp > 1e-12
pw = np.polyfit(np.log(r[sel][5:]), np.log(amp[sel][5:]), 1)[0]
check("B4 [numerical] massless (gapless) walk: Definition B's W_N for constant N = 1/2 has power-law ~1/r tails"
      " (not quasi-local in the usual exponentially/rapidly-decaying sense)", -1.3 < pw < -0.7,
      f"power-law exponent of |W^(1/2)(r)| = {pw:.3f}")

# ---------------------------------------------------------------- exponentiated group commutator on packets
Lc = 512; n = 2 * Lc; X = np.repeat(np.arange(Lc, dtype=float), 2)
print("\n  exponentiated (expm, dense), Lc = 512, N = A cos, M = A sin, q = 2pi/Lc, packets sigma = 12")
print("  theta  A   k0     dx         -w g(k0)    ratio")
rows = []
for th in (0.0, 0.5):
    W = step_matrix(Lc, th); H, _ = floquet_generator(W)
    q = 2 * np.pi / Lc
    for A in (6, 12):
        HN = 0.5 * (np.cos(q * X)[:, None] * H + H * np.cos(q * X)[None, :])
        HM = 0.5 * (np.sin(q * X)[:, None] * H + H * np.sin(q * X)[None, :])
        WN, WM = expm(-1j * A * HN), expm(-1j * A * HM)
        C = WN @ WM @ WN.conj().T @ WM.conj().T
        w = A * A * q
        # positive-band packets from the dense spectrum of the uniform generator restricted near k0
        for k0 in (0.15, -0.15):
            kk = 2 * np.pi * np.fft.fftfreq(Lc)
            amp = np.exp(-((kk - k0) * 12) ** 2) * np.exp(-1j * kk * 130.0)
            # Bloch vector of the + band from the 2x2 block of the dense step
            psi = np.zeros(n, complex)
            for j, kj in enumerate(kk):
                if abs(amp[j]) < 1e-12: continue
                c, s = np.cos(th), np.sin(th)
                Wk = np.array([[c * np.exp(-1j * kj), -1j * s * np.exp(-1j * kj)], [-1j * s * np.exp(1j * kj), c * np.exp(1j * kj)]])
                ev, V = np.linalg.eig(Wk); jj = np.argmax(-np.angle(ev)); v = V[:, jj] / np.linalg.norm(V[:, jj])
                v = v * np.exp(-1j * np.angle(v[np.argmax(abs(v))]))
                cellwave = np.exp(1j * kj * np.arange(Lc))
                psi += amp[j] * np.kron(cellwave, v)
            psi /= np.linalg.norm(psi)
            # sanity: psi is an eigen-band state of the dense step (Bloch convention check)
            Hpsi = H @ psi; band_ok = np.real(np.vdot(psi, Hpsi)) > 0
            out = C @ psi
            xm = lambda p: np.sum(np.abs(p)**2 * (X + 0.5 * (np.arange(n) % 2)))
            dx = xm(out) - xm(psi)
            pr = -w * (gfun(k0, th) if th > 0 else 1.0)
            rows.append((th, A, k0, dx, pr, band_ok))
            print(f"  {th:.1f}   {A:2d}  {k0:+.2f}  {dx:9.4f}  {pr:9.4f}   {dx / pr:.4f}  {'+band' if band_ok else 'BAND?'}")
ok5 = all(abs(r_[3] / r_[4] - 1) < 0.05 and r_[5] for r_ in rows)
check("B5 [numerical, dense expm] exponentiated generator-lapse group commutator displaces +band packets of both"
      " chiralities by -w g(k0) within 5%", ok5)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}  ({time.time() - t0:.1f} s)")
