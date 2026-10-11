"""Lane RI / probe I2 (a): the coarse-cell Poincare generators of an N-site-cell network vs the fine lattice's.
Exact dyadic arithmetic (float64 exact for these integer fields and dyadic coefficients), d = 1, L1 scalar.

Fine L1 scalar (fine units, b = 1):  t(x) = pi^2/2 + m^2 phi^2/2 + [(dphi(x))^2 + (dphi(x-1))^2]/4,
fine boost K_f = sum_x x t(x), fine momentum P_f = -{K_f, H} (= L1's sum of link energy currents).
Coarse cells X = {N X, ..., N X + N - 1}:
  unimproved cell density T(X) = sum_{x in X} t(x);   K_c = sum_X X T(X);   P_c := -{K_c, H}  (coarse units)
  improved   T'(X) = T(X) - [B(X) - B(X-1)],  B(X) = sum_{x in X} (delta(x)/N) t(x),  delta(x) = x - N X
             (a cell-local improvement, range one cell)  =>  K'_c = K_f / N  and  P'_c = P_f / N exactly.
Checks: (1) {K_f, H} + P_f == 0 and {P_f, H} == 0;  (2) {P_c, H} != 0 (the unimproved coarse momentum is not
conserved: its interband part oscillates);  (3) K'_c - K_f/N == 0 and P'_c - P_f/N == 0 exactly;
(4) Lemma-D invariance: P_c - P_f/N = -{K_c - K_f/N, H} is a time derivative of a coarse-periodic total, so its
    band-diagonal one-particle symbol vanishes; checked as: its time average along the free flow -> 0.
"""
import numpy as np
out = []
def P(s=""):
    print(s, flush=True); out.append(s)
rng = np.random.default_rng(1110)
M2 = 0.25
L = 96

def sh(f, s): return np.roll(f, -s)
def dphi(f): return sh(f, 1) - f
def tdens(phi, pi):
    d = dphi(phi)
    return 0.5 * pi**2 + 0.5 * M2 * phi**2 + 0.25 * (d**2 + sh(d, -1)**2)
def flowH(phi, pi):
    return pi, (sh(phi, 1) + sh(phi, -1) - 2 * phi) - M2 * phi
def brH(F, phi, pi):
    """{F, H} = dF/dt along the H flow, exact for quadratic F (polarization)."""
    a, b = flowH(phi, pi)
    return (F(phi + a, pi + b) - F(phi - a, pi - b)) / 2
x = np.arange(L).astype(float)
def Kf(phi, pi): return np.sum(x * tdens(phi, pi))
def Pf(phi, pi): return -brH(Kf, phi, pi)
def cells(N):
    X = np.floor(x / N); dl = x - N * X
    return X, dl
def Kc(N):
    X, _ = cells(N)
    return lambda phi, pi: np.sum(X * tdens(phi, pi))
def Kc_impr(N):
    X, dl = cells(N)
    # T'(X) = T(X) - B(X) + B(X-1);  sum_X X T'(X) = K_c + sum_X B(X)
    return lambda phi, pi: np.sum(X * tdens(phi, pi)) + np.sum((dl / N) * tdens(phi, pi))
def rand_fields():
    phi = np.zeros(L); pi = np.zeros(L)
    s = slice(30, 60)
    phi[s] = rng.integers(-5, 6, 30); pi[s] = rng.integers(-5, 6, 30)
    return phi, pi

mx1 = mx1b = 0.0
for _ in range(10):
    phi, pi = rand_fields()
    mx1 = max(mx1, abs(brH(Kf, phi, pi) + Pf(phi, pi)))
    mx1b = max(mx1b, abs(brH(Pf, phi, pi)))
P(f"(1) fine: max|{{K_f,H}} + P_f| = {mx1}, max|{{P_f,H}}| = {mx1b}  (fine momentum conserved, exact)")
for N in (2, 3, 4, 8):
    m2 = m3a = m3b = 0.0; rel = []
    for _ in range(10):
        phi, pi = rand_fields()
        Pc = lambda f, p: -brH(Kc(N), f, p)
        m2 = max(m2, abs(brH(Pc, phi, pi)))
        rel.append(abs(Pf(phi, pi)) / N)
        m3a = max(m3a, abs(Kc_impr(N)(phi, pi) - Kf(phi, pi) / N))
        Pci = lambda f, p: -brH(Kc_impr(N), f, p)
        m3b = max(m3b, abs(Pci(phi, pi) - Pf(phi, pi) / N))
    P(f"N={N}: (2) unimproved coarse momentum: max|{{P_c,H}}| = {m2:.3g} (nonzero: not conserved; compare max|P_f/N| = {max(rel):.3g})"
      f";  (3) improved: max|K'_c - K_f/N| = {m3a}, max|P'_c - P_f/N| = {m3b}")

# (4) time average of the unimproved difference along the exact free flow (spectral, periodic chain)
P("(4) time-average of (P_c - P_f/N) along the free flow (band-diagonal part); P_f/N for scale:")
kk = 2 * np.pi * np.fft.fftfreq(L)
w = np.sqrt(M2 + 4 * np.sin(kk / 2)**2)
def evolve(phi, pi, t):
    F, G = np.fft.fft(phi), np.fft.fft(pi)
    Ft = F * np.cos(w * t) + G * np.sin(w * t) / w
    Gt = -F * w * np.sin(w * t) + G * np.cos(w * t)
    return np.fft.ifft(Ft).real, np.fft.ifft(Gt).real
for N in (2, 4, 8):
    phi, pi = rand_fields()
    Pc = lambda f, p: -brH(Kc(N), f, p)
    pf = Pf(phi, pi) / N
    row = []
    for T in (100.0, 400.0, 1600.0):
        ts = np.linspace(0, T, 8001)
        dif = np.array([Pc(*evolve(phi, pi, t)) - Pf(*evolve(phi, pi, t)) / N for t in ts])
        row.append(f"T={T:5.0f}: |<diff>_t| = {abs(dif.mean()):.2e}")
    P(f"   N={N}: rms(P_c - P_f/N) = {dif.std():.2e}, |P_f/N| = {abs(pf):.2e};  " + "  ".join(row))
P("-> the N-site-cell network's coarse Poincare generators equal the fine lattice's after a cell-local improvement;")
P("   without it the coarse momentum is not even conserved (pure interband oscillation, zero band-diagonal part).")
open('i2_poincare_exact.out', 'w').write('\n'.join(out) + '\n')
