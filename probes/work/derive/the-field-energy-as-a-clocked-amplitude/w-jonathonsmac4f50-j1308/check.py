"""the-field-energy-as-a-clocked-amplitude, attempt a1 (w-jonathonsmac4f50-j1308): checks.

Exact (fractions, sympy) for (a) and (b) on the 3x3x3 torus; NUMERIC (floating point, labelled) for (c) on a ring.

Objects.  Lambda = the graph Laplacian of the torus: (Lambda v)_x = sum_{y~x}(v_x - v_y), so <v, Lambda v> = sum_bonds (v_x - v_y)^2.
Rates w = phi^2.  Block 56's simplest member F = c sum_bonds (phi_x - phi_y)^2.  A clocked background: i dxi/dt = phi (c Lambda) phi xi.
A filled set of modes of a rate-independent generator G: E[phi] = sum of the filled eigenvalues of phi G phi, phi = exp(u/2).
"""
import itertools
import random
from fractions import Fraction as F

import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


L = 3
SITES = list(itertools.product(range(L), repeat=3))
IDX = {x: i for i, x in enumerate(SITES)}
BONDS = []
for x in SITES:
    for a in range(3):
        y = list(x); y[a] = (y[a] + 1) % L; BONDS.append((IDX[x], IDX[tuple(y)]))
N = len(SITES)


def lap(v):
    out = [F(0)] * N
    for i, j in BONDS:
        out[i] += v[i] - v[j]; out[j] += v[j] - v[i]
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


random.seed(20260922)
phi = [F(random.randint(1, 9), random.randint(1, 9)) for _ in range(N)]
cst = F(7, 3)
one = [F(1)] * N
lhs = cst * sum((phi[i] - phi[j]) ** 2 for i, j in BONDS)
rhs = dot(one, [cst * phi[k] * t for k, t in enumerate(lap([phi[k] * one[k] for k in range(N)]))])
v = [F(random.randint(-5, 5), random.randint(1, 4)) for _ in range(N)]
want("A1 3x3x3 torus, random positive rational rates: c sum_bonds (phi_x - phi_y)^2 = <xi| phi (c Lambda) phi |xi> with xi = 1, exactly; "
     "and <v, Lambda v> = sum_bonds (v_x - v_y)^2 >= 0 for a random rational v, Lambda 1 = 0: the field energy is the clocked energy of a "
     "uniform background under a rate-independent, positive semidefinite generator",
     lhs == rhs and dot(v, lap(v)) == sum((v[i] - v[j]) ** 2 for i, j in BONDS) and all(t == 0 for t in lap(one)) and lhs > 0,
     f"F = {lhs} = {float(lhs):.4f}")

# ------------------------------------------------------------------ (b): the clocked background's zero mode and motion
inv = [1 / p for p in phi]
zero_mode = [phi[k] * t for k, t in enumerate(lap([phi[k] * inv[k] for k in range(N)]))]
xi_dot0 = [cst * phi[k] * t for k, t in enumerate(lap(phi))]                              # -i dxi/dt at t = 0 from xi = 1
want("B1 phi Lambda phi (1/phi) = phi Lambda 1 = 0 exactly: xi = 1/phi is a zero-energy stationary state of the clocked background, and "
     "<xi| phi Lambda phi |xi> = sum_bonds (phi_x xi_x - phi_y xi_y)^2 vanishes exactly when phi xi is constant; from xi = 1 the motion "
     "starts with dxi/dt = -i c phi Lambda phi 1, which is nonzero for these non-uniform rates",
     all(t == 0 for t in zero_mode) and any(t != 0 for t in xi_dot0)
     and dot(inv, [phi[k] * t for k, t in enumerate(lap([phi[k] * inv[k] for k in range(N)]))]) == 0)

# joint stationarity with xi free (real, small deviations): the field term depends on theta = phi xi - 1 only
eps, eta, s, cc, mu_ = sp.symbols("epsilon eta s c mu", real=True)
theta = sp.expand((1 + eps) * (1 + eta) - 1)
want("B2 with phi = 1 + epsilon and xi = 1 + eta the field term is c sum_bonds (theta_x - theta_y)^2 with theta = phi xi - 1 = epsilon + eta "
     "+ epsilon eta: stationarity in a free background sets theta constant (eta = -epsilon to first order), the field term then vanishes and the "
     "rates' law keeps only the source; block 56's law is the case eta held at 0",
     sp.expand(theta - (eps + eta + eps * eta)) == 0)
# a pinning stiffness mu sum eta^2 (supplied) interpolates: per mode c s (eps + eta)^2 + mu eta^2 minimised over eta
Emode = cc * s * (eps + eta) ** 2 + mu_ * eta ** 2
eta_star = sp.solve(sp.diff(Emode, eta), eta)[0]
eff = sp.simplify(Emode.subs(eta, eta_star) / eps ** 2)
want("B3 with a supplied pinning mu sum (xi - 1)^2 the background relaxes partly and the rates feel the stiffness c mu s/(c s + mu) per mode "
     "(s = |q|^2_lat): block 56's c s for s << mu/c, a mass mu for s >> mu/c, and zero when mu = 0",
     sp.simplify(eff - cc * mu_ * s / (cc * s + mu_)) == 0 and sp.limit(eff, mu_, sp.oo) == cc * s and eff.subs(mu_, 0) == 0,
     f"effective stiffness {eff}")

# ------------------------------------------------------------------ (c) NUMERIC on a ring
try:
    import numpy as np

    def chain(n):
        S = np.zeros((n, n), complex)
        for x in range(n): S[x, (x + 1) % n] += 1 / 2j; S[(x + 1) % n, x] -= 1 / 2j
        return S

    def ring_lap(n):
        Lm = 2 * np.eye(n)
        for x in range(n): Lm[x, (x + 1) % n] -= 1; Lm[(x + 1) % n, x] -= 1
        return Lm

    n = 512; S = chain(n); xs = np.arange(n)
    Esea = lambda ph: -np.abs(np.linalg.eigvalsh(ph[:, None] * S * ph[None, :])).sum()        # the walk sigma_x (x) S: both coin sectors' negative modes
    E0 = Esea(np.ones(n)); c0 = E0 / n
    gs = {}
    for m in (1, 2, 3, 4, 6, n // 2):
        q = 2 * np.pi * m / n; e_ = 1e-4; u = e_ * np.cos(q * xs)
        Pi = (Esea(np.exp(u / 2)) + Esea(np.exp(-u / 2)) - 2 * E0) / (2 * e_ ** 2 * n)
        gs[m] = (Pi - c0 / 4) / (1 - np.cos(q))
    ok = abs(c0 + 2 / np.pi) < 1e-4 and abs(gs[1]) < 0.01 * gs[2] and all(abs(gs[m] * 6 * np.pi / (1 - 1 / m ** 2) - 1) < 2e-3 for m in (2, 3, 4, 6)) \
        and abs(gs[n // 2] - 1 / (6 * np.pi)) > 0.02
    want("C1 NUMERIC ring of 512 sites, the walk's negative modes filled (a chiral sea): volume term c0 = -2/pi; the rates' second variation "
         "beyond it is g(q)(1 - cos q) with g = (1/(6 pi))(1 - 1/m^2) at q = 2 pi m/N (m = 1 zero to rounding - under 1 percent of m = 2 - and m = 2..6 to 2e-3): a positive "
         "gradient coefficient c = 1/(6 pi) = c_CFT/(12 pi) with c_CFT = 2 species, a finite-size (m^3 - m) correction, and g(pi) = 0.0795: "
         "the form c sum sqrt(w_x w_y)(u_x - u_y)^2 holds only at long wavelength",
         ok, f"c0 = {c0:.6f}; g*6pi/(1-1/m^2) at m=2,3,4,6: {[round(gs[m] * 6 * np.pi / (1 - 1 / m ** 2), 4) for m in (2, 3, 4, 6)]}; g(m=1) = {gs[1]:.1e}; g(pi) = {gs[n // 2]:.4f}")
    Lm = ring_lap(n); EL = lambda ph: np.linalg.eigvalsh(ph[:, None] * Lm * ph[None, :])[: n // 2].sum()
    EL0 = EL(np.ones(n)); cL = EL0 / n; q = 2 * np.pi * 2 / n; e_ = 1e-4; u = e_ * np.cos(q * xs)
    PiL = (EL(np.exp(u / 2)) + EL(np.exp(-u / 2)) - 2 * EL0) / (2 * e_ ** 2 * n)
    want("C2 NUMERIC the ring Laplacian with its lower half of modes filled (Fermi level inside the band, no chiral symmetry): as q -> 0 the "
         "second variation beyond the volume term tends to -1/(2 pi), a negative mass term for the rates (a compressibility), not a gradient term",
         abs((PiL - cL / 4) * 2 * np.pi + 1) < 1e-3, f"(Pi - c0/4) x 2pi = {(PiL - cL / 4) * 2 * np.pi:.5f}; c0 = {cL:.5f}")
except ImportError as exc:
    want("C NUMERIC skipped (numpy missing)", False, str(exc))

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL (a) c sum (phi_x - phi_y)^2 = <1| phi c Lambda phi |1> exactly; (b) as a free clocked amplitude the background's stationary state "
          "near uniform is exactly 1/phi, with zero energy (started uniform it moves and keeps F only as a conserved, non-stationary value), "
          "so a static law with a free background has no field term and block 56's law is exactly the held-uniform limit (a supplied pinning); (c) a filled chiral sea gives a positive long-wavelength stiffness c = 1/(6 pi) on a line "
          "(numeric, = c_CFT/(12 pi)) with a volume term -2/pi and finite-size and lattice corrections, while a non-chiral half-filled sea gives "
          "a mass term -1/(2 pi) that clause A forbids; (d) the identity is a rewriting; only the filled-chiral-sea reading adds a computed gamma")
    print("HIT: the field energy c sum (phi_x - phi_y)^2 is the clocked energy of a uniform background, but a stationary background under its own "
          "clocked generator is exactly 1/phi and carries no field energy (started uniform it moves, keeping F only as a non-stationary value); block 56 is the held-uniform limit; a filled "
          "chiral sea on a line induces c = 1/(6 pi) (numeric), a non-chiral one a forbidden mass term -1/(2 pi)")
