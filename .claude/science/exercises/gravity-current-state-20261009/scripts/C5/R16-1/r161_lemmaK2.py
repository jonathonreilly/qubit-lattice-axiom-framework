"""R16-1 Lemma K' (no bound on W/d): on the naive-photon edge, with t >= tau = 2 - 2cos b on supp W and T >= tau whenever A' > 0,
   Omega_qq >= (u/2) phi [ (6-t)(T + A' tau)/t^2 - 3 A' (2-t)/(2(t+T)) ]  (t <= 2),  phi = 1/(s(s+B')(s+B'+u)),
so a sufficient condition is (C_b): 2(6-t) tau (t+tau) >= 3 (2-t) t^2 for all t in [tau, 2].
(1) find the smallest b with (C_b); (2) sample Omega_qq/Omega for b >= b0 with W/d up to 1e3 (no (H3))."""
import numpy as np
rng = np.random.default_rng(1612)
def Cb_margin(b):
    tau = 2 - 2 * np.cos(b); t = np.linspace(tau, 2, 20001)
    return np.min(2 * (6 - t) * tau * (t + tau) - 3 * (2 - t) * t ** 2) if tau < 2 else 1.0
bs = np.linspace(0.3, 1.6, 1301); mg = np.array([Cb_margin(b) for b in bs])
b0 = bs[np.argmax(mg >= 0)]
print('(C_b) holds for b >= b0 = %.3f (margin at b=0.5: %+.3f, 1.0: %+.3f, 1.2: %+.3f, 1.4: %+.3f)' % (b0, Cb_margin(0.5), Cb_margin(1.0), Cb_margin(1.2), Cb_margin(1.4)))
def omega(q, u, dy, dz, Wy, Wz, lam):
    t = 2 - 2 * np.cos(q); T = dy ** 2 + dz ** 2 + lam ** 2; s = np.sqrt(t + T); B = Wy + Wz; Ap = (Wy / dy) ** 2 + (Wz / dz) ** 2
    D = s + B
    return u * (D ** 2 - t * (1 - Ap)) / (2 * t * s * D * (D + u))
for b in (b0, 1.0, 1.4):
    n = 400000; tau_d = 2 * np.sin(b / 2)
    q = rng.uniform(b, np.pi, n); u = 10 ** rng.uniform(-4, 3, n)
    qy = rng.uniform(0, np.pi, n); qz = rng.uniform(0, np.pi, n)
    dy, dz = 2 * np.sin(np.maximum(qy, 1e-3) / 2), 2 * np.sin(np.maximum(qz, 1e-3) / 2)
    Wy = np.where(qy > b, 10 ** rng.uniform(-3, 3, n) * dy, 0.0); Wz = np.where(qz > b, 10 ** rng.uniform(-3, 3, n) * dz, 0.0)
    lam = 10 ** rng.uniform(-3, 1, n)
    h = 1e-3; f = lambda sh: omega(q + sh, u, dy, dz, Wy, Wz, lam)
    d2 = (-f(2 * h) + 16 * f(h) - 30 * f(0) + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
    r = d2 / f(0)
    print('b=%.3f: W/d up to 1e3, lam up to 10, u up to 1e3: min Omega_qq/Omega = %+.4e, fraction negative %.1e' % (b, r.min(), np.mean(r < 0)))
for b in (0.3, 0.5):
    n = 400000
    q = rng.uniform(b, np.pi, n); u = 10 ** rng.uniform(-4, 3, n)
    qy = rng.uniform(0, np.pi, n); qz = rng.uniform(0, np.pi, n)
    dy, dz = 2 * np.sin(np.maximum(qy, 1e-3) / 2), 2 * np.sin(np.maximum(qz, 1e-3) / 2)
    Wy = np.where(qy > b, 10 ** rng.uniform(-3, 3, n) * dy, 0.0); Wz = np.where(qz > b, 10 ** rng.uniform(-3, 3, n) * dz, 0.0)
    lam = 10 ** rng.uniform(-3, 1, n)
    h = 1e-3; f = lambda sh: omega(q + sh, u, dy, dz, Wy, Wz, lam)
    d2 = (-f(2 * h) + 16 * f(h) - 30 * f(0) + 16 * f(-h) - f(-2 * h)) / (12 * h * h)
    r = d2 / f(0)
    print('b=%.3f (below b0, outside the lemma): min Omega_qq/Omega = %+.4e, fraction negative %.1e' % (b, r.min(), np.mean(r < 0)))
