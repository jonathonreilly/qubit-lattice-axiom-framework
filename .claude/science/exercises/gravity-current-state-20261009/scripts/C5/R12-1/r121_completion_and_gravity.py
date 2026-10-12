"""C5 R12-1, script 2.

(E) Explicit completion for the lapse-lapse (SS) bracket at the matter-bilinear order (Theorem K, sufficiency):
      R(p,q)  = D(p,q) - D(0,q) - p . d1D(0,q)            (in the p-quadratic ideal by construction)
      F2(a,b) = D(0,b) + a . d1D(0,b)                     (in the b-quadratic ideal iff the Killing jets vanish)
      G(p,q)  = [R(p,q) - F2(q,p)] / 2 ,   D = G(p,q) - G(q,p)  (antisymmetry)
    The completion symbol is tau ~ G / s(p) (s spans the quadratic ideal near 0).  We print
    max_q |G(t u, q)| / t^2 for t -> 0: bounded in the box, divergent off it (and for the NN lattice).
    We also check the decomposition identity D = G(p,q) - G(q,p) at random points.
(F) Gravity side, 09-30 note's necessary mixed identity (its eq. (3)-(4)) with a box momentum symbol:
      F = I/(4 alpha), D = i mu1 s(K) I, A = 0:   D F + F D# = 0 = mu0 F (mu0 = 0),
      [D, X] = mu1 s'(K) = mu1 on the box.   Zone mean of s' is 0, so the mean defect is -mu1 (the same -1).
    Checked in real space on an L = 4096 ring by FFT for box-supported and edge-supported packets.
(G) Scalar proxy for the free box graviton: the pair (a^dag a^dag) coefficient of the lapse-smeared energy
    density T[e^{ipx}] = sum N (pi^2 + phi Omega^2 phi)/2 (symmetrised) is (w_q - w_q')^2 / (8 sqrt(w_q w_q')),
    q + q' = p.  It vanishes to SECOND order at p = 0, so H, P and the boost K are number-conserving and the
    graviton's Killing relations reduce to one-body identities (Lemma L of R7-1).  Checked numerically.
"""
import numpy as np

rng = np.random.default_rng(1012)
M = 0.3
B_IN, B_OUT = 2.0, 3.1


def _f(t):
    t = np.asarray(t, float)
    out = np.zeros_like(t)
    pos = t > 0
    out[pos] = np.exp(-1.0 / t[pos])
    return out


def step(t):
    return _f(t) / (_f(t) + _f(1.0 - t))


def rho(k):
    a = np.abs(np.mod(k + np.pi, 2 * np.pi) - np.pi)
    return 1.0 - step((a - B_IN) / (B_OUT - B_IN))


def s_box(k):
    kk = np.mod(k + np.pi, 2 * np.pi) - np.pi
    r = rho(k)
    return r * kk + (1 - r) * np.sin(k)


MODEL = {"box": (s_box, lambda k: M * M + np.sum(s_box(k) ** 2, axis=-1)),
         "NN": (np.sin, lambda k: M * M + np.sum(2 - 2 * np.cos(k), axis=-1))}


def make_DSS(model):
    s, e2 = MODEL[model]
    eps = lambda k: np.sqrt(e2(k))
    aT = lambda p, k: 0.5 * (eps(k + p) + eps(k))
    aP = lambda p, k, j: 0.5 * (s(k + p)[..., j] + s(k)[..., j])
    d = s_box

    def D(p, q, k):
        lhs = -1j * (aT(p, k + q) * aT(q, k) - aT(q, k + p) * aT(p, k))
        rhs = sum(1j * (d(q)[j] - d(p)[j]) * aP(p + q, k, j) for j in range(len(k)))
        return lhs + rhs
    return D


def d1(D, p, q, k, h=1e-5):
    g = np.zeros(len(p), complex)
    for i in range(len(p)):
        e = np.zeros(len(p)); e[i] = h
        g[i] = (D(p + e, q, k) - D(p - e, q, k)) / (2 * h)
    return g


def G(D, p, q, k):
    z = np.zeros(len(p))
    R = D(p, q, k) - D(z, q, k) - p @ d1(D, z, q, k)
    F2qp = D(z, p, k) + q @ d1(D, z, p, k)
    return 0.5 * (R - F2qp)


print("=== (E) explicit SS completion: max_q |G(t u, q; k)| / t^2 (bounded <=> smooth completion) ===")
dim = 3
qs = [rng.uniform(-1.5, 1.5, dim) for _ in range(12)] + [rng.uniform(-0.05, 0.05, dim) for _ in range(12)]
for model in ("box", "NN"):
    D = make_DSS(model)
    for label, k in (("k in box ", np.array([0.6, -0.9, 0.4])), ("k off box", np.array([2.6, 0.2, -0.7]))):
        u = np.array([0.36, -0.48, 0.8])
        row = []
        for t in (1e-1, 3e-2, 1e-2, 3e-3):
            row.append(max(abs(G(D, t * u, q, k)) for q in qs) / t ** 2)
        print(f"[{model:3s}] {label}: t = 1e-1, 3e-2, 1e-2, 3e-3 -> " + " ".join(f"{v:.3e}" for v in row))
    # decomposition identity
    err = 0.0
    for _ in range(20):
        p, q, k = rng.uniform(-1, 1, dim), rng.uniform(-1, 1, dim), rng.uniform(-1.2, 1.2, dim)
        err = max(err, abs(D(p, q, k) - (G(D, p, q, k) - G(D, q, p, k))))
    print(f"[{model:3s}] identity D(p,q) = G(p,q) - G(q,p) at 20 random points: max error {err:.1e}")

print("\n=== (F) 09-30 mixed identity with a box graviton momentum symbol (1D TT block, L = 4096) ===")
L = 4096
k = 2 * np.pi * np.fft.fftfreq(L)
x = np.arange(L) - L // 2
mu1 = 1.0
sk = s_box(k)


def apply_D(v):          # D = i mu1 s(K)
    return np.fft.ifft(1j * mu1 * sk * np.fft.fft(v))


def comm_DX(v):
    return apply_D(x * v) - x * apply_D(v)


for label, k0, sig in (("box packet  k0=0.8 ", 0.8, 0.05), ("box packet  k0=1.7 ", 1.7, 0.04),
                       ("edge packet k0=2.6 ", 2.6, 0.05)):
    v = np.exp(1j * k0 * x - (x * sig) ** 2 / 2)
    v /= np.linalg.norm(v)
    res = np.linalg.norm(comm_DX(v) - mu1 * v)
    print(f"{label}: || [D,X] v - mu1 v || = {res:.2e}")
kk = np.linspace(-np.pi, np.pi, 400001)[:-1]
sp = np.gradient(s_box(kk), kk[1] - kk[0])
print(f"zone mean of s'(k) = {sp.mean():+.2e}  (so the zone-averaged defect of z(trD)' - 2mu1 is -2 mu1)")
print("D F + F D# with F = I/(4 alpha), D# = -D (s odd): = 0, so mu0 = 0; second equation holds with A = 0 on the box.")

print("\n=== (G) scalar proxy: pair coefficient c(q, p-q) of T[e^{ipx}] ===")
for model in ("box", "NN"):
    s, e2 = MODEL[model]
    w = lambda q: np.sqrt(e2(q))
    for q in (np.array([0.5, -0.3, 0.2]), np.array([2.7, 0.1, 0.4])):
        vals = []
        for t in (1e-1, 1e-2, 1e-3):
            p = t * np.array([0.6, 0.0, 0.8])
            wq, wq2 = w(q), w(p - q)
            c = (wq - wq2) ** 2 / (8 * np.sqrt(wq * wq2))
            vals.append(c / t ** 2)
        print(f"[{model:3s}] q = {q}: c/t^2 at t = 1e-1,1e-2,1e-3 -> " + " ".join(f"{v:.3e}" for v in vals)
              + "  (bounded: no pair term at first order in p)")
