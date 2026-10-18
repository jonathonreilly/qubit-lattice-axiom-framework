#!/usr/bin/env python3
"""C2_check ck2: independent routes for claim 2 (continuum Sakharov coefficient and measure dependence).

K1  a1 = (1/6 - zeta) R from the exact spectrum of -Delta + zeta R on the round S^4 (radius 1, R = 12, Vol = 8 pi^2/3):
    Tr e^{-sO} = Vol/(16 pi^2 s^2) [1 + s a1 + O(s^2)], fitted from the spectral sum (no perturbative expansion; C2 used
    Duhamel + Gaussian loop integrals on a plane-wave background).
K2  proper-time integral (sympy): W = -1/2 int_{1/L^2} ds/s Tr e^{-sO} -> coefficient of int sqrt g R and of int sqrt g;
    Euclidean S_E = -(1/16 pi G) int sqrt g R  =>  1/(16 pi G) = (1/6 - zeta) L^2/(32 pi^2) = (1 - 6 zeta) L^2/(192 pi^2).
K3  covariant dimension-6 operator (c6 a^2/2) sqrt g R g^{mn} d phi d phi: its one-loop tadpole <(d phi)^2> = L^4/(16 pi^2)
    (same proper-time regulator) shifts 1/(16 pi G) by -c6 a^2 L^4/(32 pi^2), i.e. O(L^2) when a L = O(1).
K4  1D circle, pure-gauge metric g = f'^2: proper-time heat trace of the covariant O = g^{-1/2} D is diffeo invariant
    (isospectral with flat), that of the flat-measure Hessian D = -d g^{-1/2} d is not (measure/regulator dependence).
"""
import time
import numpy as np
import sympy as sp

T0 = time.time()
RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.1f}s] {msg}", flush=True)

# ---------------- K1
l = np.arange(0, 4000, dtype=float)
deg = (2 * l + 3) * (l + 1) * (l + 2) / 6
lam = l * (l + 3)
def a1_fit(zeta):
    ss = np.linspace(2e-4, 2e-3, 12)
    F = np.array([6 * s * s * np.sum(deg * np.exp(-s * (lam + 12 * zeta))) - 1 for s in ss])   # Vol/(16pi^2) = 1/6
    c = np.polyfit(ss, F, 4)
    return c[-2], c[-1]    # linear coefficient, constant (should be ~0)
ok = True
for z in (0.0, 1 / 6, 0.3, -0.25):
    c1, c0 = a1_fit(z)
    exp_ = (1 / 6 - z) * 12
    print(f"   zeta = {z:+.4f}: fitted a1 = {c1:.8f}, expected (1/6 - zeta) R = {exp_:.8f}, const residual {c0:.1e}")
    ok &= abs(c1 - exp_) < 1e-5 and abs(c0) < 1e-8
check("K1", ok, "a1 = (1/6 - zeta) R from the exact S^4 spectrum (independent of C2's plane-wave Duhamel route)")

# ---------------- K2
s, L, zeta, G = sp.symbols("s Lambda zeta G", positive=True)
a1R = (sp.Rational(1, 6) - zeta)      # coefficient multiplying R
W_R = -sp.Rational(1, 2) * sp.integrate(1 / s * 1 / (16 * sp.pi ** 2 * s ** 2) * s * a1R, (s, 1 / L ** 2, sp.oo))
W_0 = -sp.Rational(1, 2) * sp.integrate(1 / s * 1 / (16 * sp.pi ** 2 * s ** 2), (s, 1 / L ** 2, sp.oo))
inv16piG = sp.simplify(-W_R)          # S_E = -(1/16 pi G) int sqrt g R
ok2 = (sp.simplify(W_0 + L ** 4 / (64 * sp.pi ** 2)) == 0 and
       sp.simplify(inv16piG - (1 - 6 * zeta) * L ** 2 / (192 * sp.pi ** 2)) == 0 and
       sp.simplify(16 * sp.pi * inv16piG.subs(zeta, 0) - L ** 2 / (12 * sp.pi)) == 0)
print(f"   W contains {sp.simplify(W_0)} int sqrt g  +  {sp.factor(W_R)} int sqrt g R;  1/(16 pi G) = {sp.factor(inv16piG)}")
check("K2", ok2, "proper time with Lambda^2 := 1/s_min: W = -L^4/(64 pi^2) int sqrt g - (1/6 - zeta) L^2/(32 pi^2) int sqrt g R; "
      "1/(16 pi G) = (1 - 6 zeta) L^2/(192 pi^2), 1/G = L^2/(12 pi) at zeta = 0 (C2's P2 coefficient and convention confirmed)")

# ---------------- K3
p2 = sp.Symbol("p2", positive=True)
# <d_m phi d_m phi> = int d^4p/(2pi)^4 p^2 int_{1/L^2} ds e^{-s p^2};  int d^4p/(2pi)^4 p^2 e^{-s p^2} = 2/(16 pi^2 s^3)
dphi2 = sp.integrate(2 / (16 * sp.pi ** 2 * s ** 3), (s, 1 / L ** 2, sp.oo))
c6, a = sp.symbols("c6 a")
shift = -(c6 * a ** 2 / 2) * dphi2         # W gets +<op>; S_E coefficient of sqrt g R is -1/(16 pi G)
ratio = sp.simplify(shift / ((sp.Rational(1, 6)) * L ** 2 / (32 * sp.pi ** 2)))
print(f"   <(d phi)^2> = {dphi2};  delta 1/(16 pi G) = {sp.factor(shift)};  ratio to the zeta = 0 Sakharov term = {ratio}")
check("K3", sp.simplify(dphi2 - L ** 4 / (16 * sp.pi ** 2)) == 0 and sp.simplify(ratio + 6 * c6 * a ** 2 * L ** 2) == 0,
      "a covariant dim-6 coupling (c6 a^2/2) sqrt g R (d phi)^2 -- allowed by closure and by Ward, outside C2's <= 2-derivative "
      "ansatz -- shifts 1/(16 pi G) by -6 c6 (a Lambda)^2 x the Sakharov value: O(1) when a Lambda = O(1)")

# ---------------- K4
M = 160
x = 2 * np.pi * np.arange(4 * M) / (4 * M)
eps = 0.25
f_p = 1 + eps * np.cos(x) + 0.5 * eps * np.sin(2 * x)        # f'(x): diffeo of the circle (int f' = 2 pi, f' > 0)
g = f_p ** 2
n = np.arange(-M, M + 1)
def fourier_mat(func):
    c = np.fft.fft(func) / len(func)
    idx = (n[:, None] - n[None, :]) % len(func)
    return c[idx]
Dm = (n[:, None] * n[None, :]) * fourier_mat(g ** -0.5)          # D = -d g^{-1/2} d  (symbol n m c_{n-m})
Sg = fourier_mat(np.sqrt(g))                                     # multiplication by sqrt g
Dm = 0.5 * (Dm + Dm.conj().T); Sg = 0.5 * (Sg + Sg.conj().T)
evD = np.sort(np.linalg.eigvalsh(Dm).real)
# O = g^{-1/2} D  <->  generalised problem D v = lam sqrt g v
w_, V = np.linalg.eigh(Sg)
Sih = V @ np.diag(w_ ** -0.5) @ V.conj().T
evO = np.sort(np.linalg.eigvalsh(Sih @ Dm @ Sih).real)
flat = np.sort((n.astype(float)) ** 2)
lowO = np.abs(evO[:41] - flat[:41]).max()
def ht(ev, s):
    return np.sum(np.exp(-s * ev))
s0 = 0.05
dO, dD = ht(evO, s0) - ht(flat, s0), ht(evD, s0) - ht(flat, s0)
pred = np.mean(f_p ** 0.5) * 2 * np.pi / np.sqrt(4 * np.pi * s0) - 2 * np.pi / np.sqrt(4 * np.pi * s0)
print(f"   low O eigenvalues vs n^2: max dev {lowO:.1e};  heat-trace shift at s = {s0}: O {dO:.2e}, D {dD:.3e} "
      f"(leading-symbol estimate int (g^(1/4) - sqrt g)/sqrt(4 pi s) = {pred:.3e})")
check("K4", lowO < 1e-8 and abs(dO) < 1e-6 and abs(dD) > 1e-2,
      "proper time on the covariant O is diffeo invariant, on the flat-measure Hessian D it is not -- already at the "
      "leading (cosmological, k^0) order int g^(1/4) != int sqrt g; Ward at any order is a regulator/measure property")
print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.1f}s)")
