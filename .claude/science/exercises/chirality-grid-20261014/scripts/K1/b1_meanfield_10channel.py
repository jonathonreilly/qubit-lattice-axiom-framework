"""K1 tests B0, B1, B2, B3 and follow-up A5 (see ../PREREG.md).

B0: G_SM content of the 10 of Spin(10) (via SU(5): 10 = 5 + 5bar; 5 = (3,1,-1/3) + (1,2,1/2)).
B1: mean-field (Hartree in the 10-vector pairing channel) onset coupling.  Uniform condensate Phi along one 10
    direction pairs psi(k) psi(-k) (same corner, since corners are self-conjugate) with form factor f(k)^2 (both legs
    filtered).  Walker |h(k)| = |sin k|.  Spectrum E = sqrt(|sin k|^2 + |Phi|^2 f(k)^4).  Gap equation onset:
        1/g_c  proportional to  I[f] = < f(k)^4 / |sin k| >_BZ
    with every combinatorial factor common to all variants, so g_c(X2)/g_c(control) = I[1] / I[f].
    Also: light-sector check: E at hw1 corners stays 0 in the broken phase (f(hw1) = 0).
B2/B3: overlap kernel K(r) = FT of f^2 (anticommutator {psi_S(x), psi_S(x+r)^dag} per component).
A5: two Majorana chains with on-site coupling m: single-particle gap vs m.
"""
import numpy as np, itertools
from fractions import Fraction as Fr

out = []
def P(*a):
    s = " ".join(str(x) for x in a); print(s); out.append(s)

# ---------------- B0 ----------------
ten = [("(3,1,-1/3)", 3, 1, Fr(-1, 3)), ("(3b,1,+1/3)", 3, 1, Fr(1, 3)), ("(1,2,+1/2)", 1, 2, Fr(1, 2)),
       ("(1,2,-1/2)", 1, 2, Fr(-1, 2))]
assert sum(a * b for _, a, b, _ in ten) == 10
sing = [n for n, c, w, y in ten if c == 1 and w == 1 and y == 0]
P("B0: 10 of Spin(10) under G_SM =", " + ".join(n for n, *_ in ten), f"; G_SM singlets: {len(sing)}")
P("B0 verdict:", "PASS (any 10-vector condensate breaks G_SM)" if not sing else "FAIL")

# ---------------- filters ----------------
def f_F1(p):
    s2 = np.sin(p / 2) ** 2; c2 = np.cos(p / 2) ** 2
    return 1 - (s2[0] * c2[1] * c2[2] + s2[1] * c2[0] * c2[2] + s2[2] * c2[0] * c2[1])
def f_NN(p):
    return (1 - np.cos(p[0]) - np.cos(p[1]) - np.cos(p[2])) / 2
def f_one(p):
    return np.ones_like(p[0])
filters = {"control f = 1 (EP-like channel, unfiltered)": f_one, "X2 f_F1 (27-site cube)": f_F1,
           "X2 f_NN (7-site star)": f_NN}

corners = list(itertools.product((0, 1), repeat=3))
for name, f in filters.items():
    vals = {c: float(f(np.pi * np.array(c, float).reshape(3, 1, 1, 1)).ravel()[0]) for c in corners}
    P(f"  {name}: f at corners (hw0..hw3 order) =", {c: round(v, 4) for c, v in vals.items()})

# ---------------- B1: onset integrals on midpoint grids (no grid point on a corner) ----------------
def bz_avg(fun, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    acc = 0.0
    for kx in k:                                   # slice to keep memory small
        p = np.stack(np.meshgrid(np.array([kx]), k, k, indexing="ij"))
        acc += fun(p).sum()
    return acc / N ** 3
res = {}
for N in (64, 128, 192):
    row = {}
    for name, f in filters.items():
        I = bz_avg(lambda p: f(p) ** 4 / np.sqrt((np.sin(p) ** 2).sum(0)), N)
        row[name] = I
    res[N] = row
    P(f"B1 grid N={N}: I[f] = <f^4/|sin k|> :", {n: round(v, 5) for n, v in row.items()})
Ictl = res[192]["control f = 1 (EP-like channel, unfiltered)"]
for name in filters:
    if name.startswith("control"): continue
    r = Ictl / res[192][name]
    reading = ("channel survives the filter (ratio < 3)" if r < 3 else
               "filter suppresses the channel (ratio > 10)" if r > 10 else "partially suppressed (3..10)")
    P(f"B1: g_c({name}) / g_c(control) = I[1]/I[f] = {r:.3f}  ->  {reading}")
# light sector in the broken phase: E(hw1 + q) with Phi = 1 for small q
for name, f in filters.items():
    if name.startswith("control"): continue
    for q in (1e-2, 1e-3):
        p = (np.array([np.pi, 0, 0]) + q * np.array([0.6, 0.48, 0.64])).reshape(3, 1, 1, 1)
        E = np.sqrt((np.sin(p) ** 2).sum(0) + f(p) ** 4).ravel()[0]
        P(f"  {name}: broken-phase E(hw1 + q), |q| = {q:g}: {E:.3e} (|q| = {q:.1e}; massless if E ~ |q|)")

# ---------------- B2 / B3: overlap kernel ----------------
for name, f in filters.items():
    N = 32
    k = np.arange(N) * 2 * np.pi / N
    p = np.stack(np.meshgrid(k, k, k, indexing="ij"))
    F2 = f(p) ** 2
    K = np.fft.ifftn(F2).real                     # K(r) = <f^2 e^{ikr}>
    K0 = K[0, 0, 0]
    Kabs = np.abs(K.copy()); Kabs[0, 0, 0] = 0
    imax = np.unravel_index(np.argmax(Kabs), K.shape)
    rmax = tuple(int(i if i <= N // 2 else i - N) for i in imax)
    nonorth = np.sqrt((F2 ** 2).mean() - F2.mean() ** 2) / F2.mean()
    support = int((np.abs(K) > 1e-12).sum())
    P(f"B2/B3 {name}: K(0) = {K0:.4f}; max_(r!=0)|K(r)|/K(0) = {Kabs.max()/K0:.4f} at r = {rmax}; "
      f"sqrt(sum_(r!=0)|K|^2)/K(0) = {nonorth:.4f}; support size of K = {support} sites")
    if not name.startswith("control"):
        P(f"   reading: {'NOT atomic (>= 0.2): strong-coupling limit is a frustrated many-body problem' if Kabs.max()/K0 >= 0.2 else 'near-atomic (< 0.2)'}")

# ---------------- A5: two Majorana chains, emanant anomaly nu = 2 vs translation-invariant gapping ----------------
# Majorana chain i sum chi_j chi_{j+1}: single-particle h(k) = 2 sin k (k in (-pi, pi]); on-site i m chi1 chi2 couples
# the chains with -m sigma_y in chain space  ->  bands 2 sin k +- m.
P("\nA5: two Majorana chains + on-site i m chi1 chi2 (translation-invariant, (-1)^F kept); emanant Z2 nu = 2 mod 8")
k = np.linspace(-np.pi, np.pi, 20001)
for m in (0.0, 0.5, 1.5, 1.99, 2.01, 2.5, 3.0):
    gap = min(np.abs(2 * np.sin(k) + m).min(), np.abs(2 * np.sin(k) - m).min())
    P(f"   m = {m:4.2f}: single-particle gap = {gap:.4f}  (prediction {max(0, abs(m) - 2):.4f})")
# exact check with explicit lattice matrices (L = 40, periodic Majorana chains)
L = 40
A = np.zeros((2 * L, 2 * L))
for c in range(2):
    for j in range(L):
        a, b = c * L + j, c * L + (j + 1) % L
        A[a, b] += 1; A[b, a] -= 1               # H = (i/2) sum A_ab chi_a chi_b  with A antisymmetric (convention)
def gap_lattice(m):
    B = A.copy()
    for j in range(L):
        B[j, L + j] += m; B[L + j, j] -= m
    ev = np.linalg.eigvalsh(1j * B)
    return np.abs(ev).min()
P("   lattice check (L = 40, eigenvalues of iA):", {m: round(gap_lattice(m), 4) for m in (0.5, 1.5, 2.5, 3.0)})

open(__file__.replace('.py', '.out'), 'w').write("\n".join(out) + "\n")
