#!/usr/bin/env python3
"""B12 / P-T3: one-loop Lambda ratio, heat-kernel (native saddle) vs Wilson single-plaquette action.

Actions (SU(N), Haar measure, one class function per plaquette, X = -i log U_P, tr T^aT^b = d_ab/2):
  Wilson : w_W(U)  = exp[(beta_W/N) Re tr U],           g_W^-2 = beta_W/(2N)
  HK     : w_HK(U) = sum_lam d_lam chi_lam(U) exp(-tau C2(lam)),  tau = g_HK^2/2  (=3/beta_HK, SU(3))
Small-field: -log w = g^-2 [tr X^2 + c4 tr X^4 + c22 (tr X^2)^2] + e2 tr X^2 + ...
  Wilson: c4=-1/12, c22=0, e2=0.   HK (Eskin closed form): c4=c22=0, e2=-N/24.
One-loop: the plaquette-function difference enters only through (i) e2 and (ii) the tadpole of the
quartic term with <q^a q^b> = w d^ab, w = (2/d) g^2 (d-dim isotropic Euclidean).
  <trX^4>_qq = w(2N^2-3)/N trB^2,  <(trX^2)^2>_qq = w(N^2+1) trB^2
=> g_HK^-2 = g_W^-2 + c(d),  c(d) = N/24 - (2/d)(2N^2-3)/(12N).
Lambda_HK/Lambda_W = exp(-c/(2 b0)),  b0 = 11N/(48 pi^2)  [Lambda a = exp(-1/(2 b0 g^2)) (b0 g^2)^(-b1/2b0^2)].
Independent check (C): in d=2 single-plaquette weights factorise, so exact fundamental-character
matching must reproduce c(2): tau_eff = (N/beta)(1 + k/beta), k = -2N c(2) = (N^2-2)/4 (SU(3): 7/4).
"""
import itertools, math
import numpy as np
from mpmath import mp, besseli, matrix, det, log as mlog, mpf

FAILS = []
def check(name, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}: {name} {detail}")
    if not ok: FAILS.append(name)

def gens(N):
    T = []
    for i in range(N):
        for j in range(i + 1, N):
            A = np.zeros((N, N), complex); A[i, j] = A[j, i] = 0.5; T.append(A)
            B = np.zeros((N, N), complex); B[i, j] = -0.5j; B[j, i] = 0.5j; T.append(B)
    for k in range(1, N):
        D = np.zeros((N, N), complex)
        for m in range(k): D[m, m] = 1
        D[k, k] = -k
        T.append(D / np.sqrt(2 * k * (k + 1)))
    return T

# ---------- (A) exact tadpole contractions by generator sums ----------
print("== (A) tadpole contractions (exact generator sums, w=1) ==")
rng = np.random.default_rng(12)
def quad_coeff(f, B, T):
    # [t^2] f(B + tT) for polynomial f of degree 4 via exact 5-point fit
    ts = np.array([-2, -1, 0, 1, 2], float)
    vals = [f(B + t * T).real for t in ts]
    return np.polyfit(ts, vals, 4)[2]
tr4 = lambda X: np.trace(X @ X @ X @ X)
tr22 = lambda X: np.trace(X @ X) ** 2
for N in (2, 3, 4):
    T = gens(N)
    gram = np.array([[np.trace(a @ b).real for b in T] for a in T])
    check(f"SU({N}) generator Gram = 1/2", np.allclose(gram, 0.5 * np.eye(N * N - 1)))
    b = rng.normal(size=N * N - 1); B = sum(x * t for x, t in zip(b, T)); trB2 = np.trace(B @ B).real
    s4 = sum(quad_coeff(tr4, B, t) for t in T) / trB2
    s22 = sum(quad_coeff(tr22, B, t) for t in T) / trB2
    check(f"SU({N}) <trX^4>_qq/(w trB^2) = (2N^2-3)/N = {(2*N*N-3)/N:.6f}", abs(s4 - (2*N*N-3)/N) < 1e-8, f"got {s4:.10f}")
    check(f"SU({N}) <(trX^2)^2>_qq/(w trB^2) = N^2+1 = {N*N+1}", abs(s22 - (N*N+1)) < 1e-8, f"got {s22:.10f}")

# ---------- (B) heat kernel small-field structure from the character sum ----------
print("== (B) heat kernel: log K + trX^2/(2tau) - sum log(th/sin th) is X-independent ==")
def partitions(N, lmax):
    for lam in itertools.product(range(lmax + 1), repeat=N - 1):
        if all(lam[i] >= lam[i + 1] for i in range(N - 2)):
            yield tuple(lam) + (0,)
def C2(lam, N):
    s = sum(l * (l + N + 1 - 2 * (j + 1)) for j, l in enumerate(lam))
    return 0.5 * (s - sum(lam) ** 2 / N)
def dimW(lam, N):
    d = 1.0
    for i in range(N):
        for j in range(i + 1, N):
            d *= (lam[i] - lam[j] + j - i) / (j - i)
    return d
def char(lam, phi):
    N = len(phi)
    num = np.linalg.det(np.array([[np.exp(1j * (lam[j] + N - 1 - j) * p) for p in phi] for j in range(N)]))
    den = np.linalg.det(np.array([[np.exp(1j * (N - 1 - j) * p) for p in phi] for j in range(N)]))
    return num / den
def logK(phi, tau, N, lmax):
    s = sum(dimW(l, N) * char(l, phi) * math.exp(-tau * C2(l, N)) for l in partitions(N, lmax))
    return math.log(s.real)
for N, tau, lmax in ((2, 0.05, 80), (3, 0.08, 55), (3, 0.04, 75)):
    consts = []
    for _ in range(5):
        p = rng.uniform(-0.9, 0.9, N); p -= p.mean()
        th = [(p[i] - p[j]) / 2 for i in range(N) for j in range(i + 1, N)]
        jac = sum(math.log(t / math.sin(t)) for t in th if abs(t) > 1e-12)
        consts.append(logK(p, tau, N, lmax) + (p @ p) / (2 * tau) - jac)
    spread = max(consts) - min(consts)
    check(f"SU({N}) tau={tau}: closed form exact (=> c4=c22=0 at O(1/g^2), e2=-N/24)", spread < 1e-7, f"spread={spread:.2e}")
# e2 from the Jacobian: sum_{i<j} theta^2/6 = N trX^2/24
p = rng.normal(size=3); p -= p.mean()
lhs = sum(((p[i]-p[j])/2)**2/6 for i in range(3) for j in range(i+1, 3)); rhs = 3*(p@p)/24
check("sum_{i<j} theta_ij^2/6 = N trX^2/24 (SU(3))", abs(lhs - rhs) < 1e-12)

# ---------- (C) d=2 independent route: exact fundamental-character matching ----------
print("== (C) d=2 / single plaquette: exact Bessel-determinant matching vs c(2) ==")
mp.dps = 50
def cW(lam, beta, N):
    x = mpf(beta) / N; s = mpf(0); n = 0
    while True:
        tot = mpf(0)
        for m in ((n,) if n == 0 else (n, -n)):
            M = matrix(N, N)
            for i in range(N):
                for j in range(N):
                    M[i, j] = besseli(lam[j] + i - j + m, x)
            tot += det(M)
        s += tot
        if n > 3 and abs(tot) < mpf(10) ** (-45) * abs(s): break
        n += 1
    return s
def c_d(N, d): return mpf(N) / 24 - mpf(2) / d * (2 * N * N - 3) / (12 * mpf(N))
for N in (2, 3, 4):
    CF = mpf(N * N - 1) / (2 * N); ks = []
    betas = (100, 200, 400, 800)
    for beta in betas:
        aF = cW((1,) + (0,) * (N - 1), beta, N) / (N * cW((0,) * N, beta, N))
        tau = -mlog(aF) / CF
        ks.append(beta * (tau * beta / N - 1))
    # Richardson (k(beta) = k + a/beta + b/beta^2)
    r1 = [2 * ks[i + 1] - ks[i] for i in range(3)]
    r2 = [(4 * r1[i + 1] - r1[i]) / 3 for i in range(2)]
    pred = -2 * N * c_d(N, 2)
    check(f"SU({N}) d=2 k = -2N c(2) = (N^2-2)/4 = {float(pred):.4f}", abs(r2[-1] - pred) < 2e-3,
          f"raw k(800)={float(ks[-1]):.5f} richardson={float(r2[-1]):.6f}")

# ---------- (D) tadpole weights ----------
print("== (D) tadpole weights ==")
L = 16; k = 2 * np.pi * np.arange(L) / L; kh2 = 4 * np.sin(k / 2) ** 2
K = np.meshgrid(kh2, kh2, kh2, kh2, indexing="ij"); den = sum(K); msk = den > 0
w4 = np.mean((K[0] + K[1])[msk] / den[msk])
check("d=4 plaquette tadpole w/g^2 = 2/d = 1/2 (L=16, zero mode removed)", abs(w4 - 0.5) < 1e-12, f"got {w4:.12f}")
# Hamiltonian (a_t->0, 3D spatial lattice, KS electric term): w_s/g^2 = (1/3) int d^3k/(2pi)^3 |khat|
def Iabs(Lm):
    kk = 2 * np.pi * (np.arange(Lm) + 0.5) / Lm; s = 4 * np.sin(kk / 2) ** 2
    tot = 0.0
    for a in s:
        tot += np.sqrt(a + s[:, None] + s[None, :]).sum()
    return tot / Lm ** 3
I1, I2 = Iabs(128), Iabs(256)
check("Hamiltonian |khat| integral converged", abs(I1 - I2) < 1e-5, f"I={I2:.7f}")
ws = I2 / 3
print(f"   w_s/g^2 (spatial plaquette, Hamiltonian) = {ws:.6f}")

# ---------- (E) results ----------
print("== (E) coupling shift and Lambda ratio ==")
for N in (2, 3):
    b0 = 11 * N / (48 * math.pi ** 2)
    c4 = float(c_d(N, 4)); exact = (3 - N * N) / (24 * N)
    check(f"SU({N}) c(4) = (3-N^2)/(24N) = {exact:.6f}", abs(c4 - exact) < 1e-15)
    R = math.exp(-c4 / (2 * b0)); Rc = math.exp(math.pi ** 2 * (N * N - 3) / (11 * N * N))
    check(f"SU({N}) Lambda_HK/Lambda_W = exp(pi^2 (N^2-3)/(11 N^2)) = {Rc:.5f}", abs(R - Rc) < 1e-12,
          f"(c={c4:.6f}, delta beta_HK-beta_W = 2N c = {2*N*c4:.4f})")
    # Hamiltonian limit, magnetic plaquette function only (same KS electric term):
    dW = -ws * (2 * N * N - 3) / (12 * N); dHK = -N / 24
    cH = 0.5 * (dW - dHK)
    print(f"   SU({N}) Hamiltonian-limit (magnetic f only): c_H = {cH:.6f}, Lambda_H,HK/Lambda_H,W = {math.exp(-cH/(2*b0)):.4f}; "
          f"one-loop speed-of-light shift v^2-1 = g^2 x {dW - dHK:.5f} (must be retuned)")

# ---------- (F) reconciliation with repo W2 = (3 - 7Q/4 + Q^2/4) W ----------
print("== (F) reconciliation: -7Q/4 in repo W2 is the probe's 7/4 = d=2 shift ==")
import sympy as sp
b, Q = sp.symbols("beta Q", positive=True)
C2s = (b * Q - 3) / 3                     # Q(x_p) = (3 C2 + 3)/beta
y = C2s * sp.Rational(21, 4) / b**2         # C2*(tau_eff - 3/beta) at O(beta^-2)
coeff = sp.limit(sp.expand(-y) * b, b, sp.oo)  # beta^-1 coefficient of exp(-y) at fixed Q
check("exp(-C2 * 21/(4 beta^2)) = 1 - (7/4) Q/beta + O(beta^-2) at fixed Q", sp.simplify(coeff + sp.Rational(7, 4) * Q) == 0, f"got {coeff}")
print("   Q^2/4 term = non-Casimir residue kappa C2^2/beta^3 with kappa=9/4 -> beta^3 r_lam -> (9/4)(C2^2 - C2 C_F):")
for nm, c2 in (("8", 3), ("6", sp.Rational(10, 3)), ("10", 6), ("27", 8)):
    print(f"     r[{nm}] beta^3 -> {float(sp.Rational(9,4)*(c2**2 - c2*sp.Rational(4,3))):.3f}")
print(f"\nSUMMARY: {'ALL PASS' if not FAILS else 'FAILURES: ' + ', '.join(FAILS)}")
