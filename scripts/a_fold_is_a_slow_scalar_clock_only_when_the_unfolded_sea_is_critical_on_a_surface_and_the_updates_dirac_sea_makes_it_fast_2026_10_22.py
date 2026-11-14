AUDIT_INPUT_PATHS = ('docs/A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Fold order parameter as the scalar clock (finite runner, seeded).

Asks whether the grid folding (unfolded odds -> star-rule pair fold) gives a
slow scalar clock, with V(phi) and the stiffness computed, not chosen.
  A  funnel ends: star rule = Majumdar-Ghosh form; uniform odds sit at the top
     as an exact eigenstate; the sea sits on a downhill funnel; fold weight
  B  speed: stiffness Z of a fold order parameter of a gapless two-band sea: Z = (A/4) I(alpha) m^(alpha-3)
     asymptotically for rho(e) ~ A e^(alpha-1); alpha = d (codimension) only for linear transverse dispersion
     (normalization and nonlinear-dispersion controls added 2026-11-14); lattice ratios 1D, 3D nested, 3D Dirac
  C  1D toy with the pole: exact V_star(delta), z(delta) on the dimer path;
     slow roll, n_s, r, exit, A_s; split re-seeding arithmetic
  D  3D Dirac sea (the update's light band): fast roll at every allowed rung
  E  reheating into misfolds
Supplied numbers are named in the output. Measured numbers enter only C/D/E.
"""
import sys
import time
import itertools
import warnings
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

IW = []   # every warning raised by the run is recorded here and reported once (2026-11-14), not printed inline
warnings.showwarning = lambda msg, cat, *a, **k: IW.append((cat.__name__, str(msg).split('.')[0][:60]))

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
RNG = np.random.default_rng(20261022)
NP = NF = 0


def check(ok, tag, text, vals=""):
    global NP, NF
    NP += bool(ok)
    NF += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {text}  {vals}")


A_S, NS_PL, NS_ACT, R_MAX = 2.1e-9, 0.9649, 0.974, 0.036

# ---------------------------------------------------------------- ED helpers
def sector(N):
    st = [s for s in range(1 << N) if bin(s).count("1") == N // 2]
    return np.array(st), {s: i for i, s in enumerate(st)}


def swap_op(st, idx, i, j):
    D = len(st)
    M = np.zeros((D, D))
    for a, s in enumerate(st):
        bi, bj = (s >> i) & 1, (s >> j) & 1
        t = s if bi == bj else s ^ ((1 << i) | (1 << j))
        M[idx[t], a] += 1.0
    return M


def SS(st, idx, i, j):            # S_i.S_j = swap/2 - 1/4
    return 0.5 * swap_op(st, idx, i, j) - 0.25 * np.eye(len(st))


def flip_op(st, idx, i, j):       # S+S- + h.c. (XX hop, spin language)
    D = len(st)
    M = np.zeros((D, D))
    for a, s in enumerate(st):
        if ((s >> i) & 1) != ((s >> j) & 1):
            M[idx[s ^ ((1 << i) | (1 << j))], a] += 1.0
    return M


def star_rule(N, st, idx):
    H = np.zeros((len(st), len(st)))
    for x in range(N):
        a, b, c = (x - 1) % N, x, (x + 1) % N
        H += 0.5 * np.eye(len(st)) + (2 / 3) * (SS(st, idx, a, b) + SS(st, idx, b, c) + SS(st, idx, a, c))
    return H


print("== A. the funnel's ends")
# A1: P_3/2 on one star is a rank-4 projector; star rule = MG form
st3, id3 = np.arange(8), {s: s for s in range(8)}
P = 0.5 * np.eye(8) + (2 / 3) * (SS(st3, id3, 0, 1) + SS(st3, id3, 1, 2) + SS(st3, id3, 0, 2))
proj = np.abs(P @ P - P).max()
rank = int(round(np.trace(P)))
gaps, zero = {}, {}
EDS = {}
for N in (8, 10, 12):
    st, idx = sector(N)
    H = star_rule(N, st, idx)
    MG = N / 2 * np.eye(len(st)) + sum((4 / 3) * SS(st, idx, x, (x + 1) % N) + (2 / 3) * SS(st, idx, x, (x + 2) % N) for x in range(N))
    w, v = np.linalg.eigh(H)
    zero[N] = int(np.sum(np.abs(w) < 1e-9))
    gaps[N] = w[zero[N]]
    EDS[N] = (st, idx, H, w, v, np.abs(H - MG).max())
check(proj < 1e-14 and rank == 4 and all(zero[N] == 2 for N in zero) and max(EDS[N][5] for N in EDS) < 1e-12,
      "A1 [T+D]", "the star rule sum_x P_3/2(x-1,x,x+1) is a sum of rank-4 projectors and equals the Majumdar-Ghosh form "
      "N/2 + (4/3) sum S.S(x,x+1) + (2/3) sum S.S(x,x+2) (literature: Majumdar-Ghosh 1969); two zero-phase folds, gapped",
      f"|P^2-P| {proj:.0e}; zero modes {zero[8]},{zero[10]},{zero[12]}; gaps " + ", ".join(f"{gaps[N]:.3f}" for N in gaps))

# A2: uniform odds (equal amplitude on every half-filled configuration) = funnel top, exact eigenstate
N = 12
st, idx, H, w, v, _ = EDS[N]
dk = np.ones(len(st)) / np.sqrt(len(st))
res = np.linalg.norm(H @ dk - N * dk)
Hhop = sum(flip_op(st, idx, x, (x + 1) % N) for x in range(N))
wh, vh = np.linalg.eigh(Hhop)
ch = vh.T @ dk
fid = [abs(np.sum(ch ** 2 * np.exp(-1j * wh * t))) ** 2 for t in (0.25, 0.5, 1.0, 2.0)]
check(res < 1e-10 and w.max() <= N + 1e-9 and fid[2] < 0.5,
      "A2 [T+D]", "uniform odds are the funnel TOP: every star is spin-3/2 (energy 1 per site, the maximum), an exact eigenstate "
      "of the star rule and of any SU(2)-blind rule, so the fold never starts from it; the update's hop breaks SU(2) and "
      "moves it off the top within about one tick (fidelity under the N=12 XX hop at t=0.25,0.5,1,2)",
      f"|H psi - N psi| {res:.0e}; E_max/N {w.max()/N:.4f}; fid " + ", ".join(f"{f:.3f}" for f in fid))

# A3: the sea (XX ground state) on the funnel: star energy per site; conserved fold weight
seaE, wfold = {}, {}
for N in (8, 10, 12):
    st, idx, H, w, v, _ = EDS[N]
    Hx = sum(flip_op(st, idx, x, (x + 1) % N) for x in range(N))
    ws, vs = np.linalg.eigh(Hx)
    sea = vs[:, 0]
    seaE[N] = float(sea @ H @ sea) / N
    P0 = v[:, :2] @ v[:, :2].T
    wfold[N] = float(sea @ P0 @ sea)
check(all(0 < seaE[N] < 0.2 for N in seaE) and wfold[8] > wfold[10] > wfold[12],
      "A3 [T+D]", "the update's sea sits low on the funnel (star energy per site, infinite chain 0.0756 in C1); under the "
      "fold rule's own unitary its weight on the fold manifold is conserved exactly ([H, P_fold] = 0) and falls with N (~0.91 per site): "
      "unitary odds never complete a fold, an energy sink is needed (records cannot be one: they never condition the odds)",
      "e_sea N=8,10,12: " + ", ".join(f"{seaE[N]:.4f}" for N in seaE) + "; fold weight " + ", ".join(f"{wfold[N]:.4f}" for N in wfold))

print("== B. what sets the fold's speed: the stiffness of a fold order parameter")
# B1 (narrowed 2026-11-14). Hypotheses: a two-band (or Clifford) sea whose gap term anticommutes with the kinetic term, so
# E = sqrt(e^2 + m^2) and Z(m) = int rho(e) e^2/(4 (e^2+m^2)^(5/2)) de; and a density of kinetic energies
# rho(e) = A e^(alpha-1) (1 + o(1)) as e -> 0 with 0 < alpha < 3, bounded by a multiple of e^(alpha-1) up to the cutoff.
# Substituting e = m x and dominated convergence give Z(m) = (A/4) I(alpha) m^(alpha-3) (1 + o(1)) as m -> 0, with the
# NORMALIZED integral I(alpha) = int_0^oo x^(alpha+1)/(1+x^2)^(5/2) dx = Gamma((alpha+2)/2) Gamma((3-alpha)/2)/(2 Gamma(5/2)).
# alpha equals the codimension d only for smooth nonzero LINEAR transverse dispersion; e ~ |k_perp|^z gives alpha = d/z.
x, d = sp.symbols("x d", positive=True)
al_, A_, m_, e_ = sp.symbols("alpha A m e", positive=True)
I1 = sp.integrate(x ** 2 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, sp.oo))
I2 = sp.integrate(x ** 3 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, sp.oo))
Lam = sp.symbols("Lambda", positive=True)
I3 = sp.limit(sp.integrate(x ** 4 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, Lam)) - sp.log(Lam), Lam, sp.oo)
Igen = sp.gamma((al_ + 2) / 2) * sp.gamma((3 - al_) / 2) / (2 * sp.gamma(sp.Rational(5, 2)))
Ihalf = quad(lambda t: t ** 1.5 / (1 + t * t) ** 2.5, 0, np.inf)[0]
# exact prefactor for a pure power density rho = A e^(d-1) (no cutoff): the coefficient carries A/4
Zpow = {dd: sp.simplify(sp.integrate(A_ * e_ ** (dd - 1) * e_ ** 2 / (4 * (e_ ** 2 + m_ ** 2) ** sp.Rational(5, 2)), (e_, 0, sp.oo)))
        for dd in (1, 2)}
okB1 = (I1 == sp.Rational(1, 3) and I2 == sp.Rational(2, 3) and I3.is_finite
        and sp.simplify(Igen.subs(al_, 1) - I1) == 0 and sp.simplify(Igen.subs(al_, 2) - I2) == 0
        and abs(float(Igen.subs(al_, sp.Rational(1, 2))) - Ihalf) < 1e-10
        and sp.simplify(Zpow[1] - A_ / (12 * m_ ** 2)) == 0 and sp.simplify(Zpow[2] - A_ / (6 * m_)) == 0)
# control: the held reading 'c_1 = 1/3, c_2 = 2/3' as absolute coefficients holds only at the single value A = 4
held_A = [sp.solve(sp.Eq(Zpow[1], m_ ** -2 / 3), A_), sp.solve(sp.Eq(Zpow[2], 2 / (3 * m_)), A_)]
okB1 = okB1 and held_A == [[4], [4]]
check(okB1, "B1 [T]", "stiffness of a gap-opening fold order parameter m on a two-band (Clifford) sea, Z(m) = int rho(e) e^2/(4(e^2+m^2)^(5/2)) de: "
      "if rho(e) = A e^(alpha-1)(1 + o(1)) as e -> 0 (0 < alpha < 3), then Z = (A/4) I(alpha) m^(alpha-3)(1 + o(1)) as m -> 0, with the "
      "normalized integral I(alpha) = Gamma((alpha+2)/2) Gamma((3-alpha)/2)/(2 Gamma(5/2)); alpha = d (codimension of the gapless set) "
      "only for smooth nonzero linear transverse dispersion, so then d=1 gives a pole (A/12) m^-2, d=2 gives (A/6) m^-1, d=3 only "
      "(A/4) ln(1/m); a pure power rho = A e^(d-1) gives these exactly; control: the held absolute c_1 = 1/3, c_2 = 2/3 need A = 4",
      f"normalized I_1 = {I1}, I_2 = {I2}, I(1/2) = {float(Igen.subs(al_, sp.Rational(1, 2))):.6f} (quad {Ihalf:.6f}), d=3: log + {sp.nsimplify(I3)}; "
      f"Z(d=1) = {Zpow[1]}, Z(d=2) = {Zpow[2]}; held coefficients need A = {held_A[0][0]}, {held_A[1][0]}")


def zk_radial(m, D, disp, cut=np.inf):
    """B1 stiffness computed in k-space for an isotropic two-band model: int d^Dk/(2pi)^D e(k)^2/(4 E^5), E^2 = e^2 + m^2."""
    meas = {1: lambda k: 2 / (2 * np.pi), 2: lambda k: 2 * np.pi * k / (2 * np.pi) ** 2}[D]   # both signs of k in 1D
    f = lambda k: meas(k) * disp(k) ** 2 / (4 * (disp(k) ** 2 + m * m) ** 2.5)
    edges = sorted({0.0, cut, *[p for p in (m, np.sqrt(m), 10 * m, 10 * np.sqrt(m)) if p < cut]})
    return sum(quad(f, a_, b_, limit=400, epsabs=0, epsrel=1e-11)[0] for a_, b_ in zip(edges[:-1], edges[1:]))


def sz_matrix_element(Hk):
    """|<+|sigma_z|->|^2 / (e^2/E^2) for a 2x2 Hermitian H(k) = dx sx + dy sy + m sz (1 when the derivation's per-k step holds)."""
    w_, v_ = np.linalg.eigh(Hk); me = abs(v_[:, 1].conj() @ np.diag([1, -1]) @ v_[:, 0]) ** 2
    E_ = w_[1]; e2 = E_ ** 2 - np.real(Hk[0, 0]) ** 2
    return me / (e2 / E_ ** 2)


sx_, sy_, sz_ = np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.diag([1.0, -1.0])
vD, mB = 0.7, (1e-2, 1e-3)
# B1b (added 2026-11-14): normalization on explicit linear models, computed in k-space (a different route from the e-integral)
A1D, A2D = 2 / (2 * np.pi * vD), 2 * np.pi / ((2 * np.pi) ** 2 * vD ** 2)          # DOS prefactors from the k-measure
Z1D = [zk_radial(mm, 1, lambda k: vD * k) for mm in mB]
Z2D = [zk_radial(mm, 2, lambda k: vD * k) for mm in mB]
rel1 = max(abs(z_ * mm ** 2 / (A1D / 12) - 1) for z_, mm in zip(Z1D, mB))
rel2 = max(abs(z_ * mm / (A2D / 6) - 1) for z_, mm in zip(Z2D, mB))
cutdev = [abs(zk_radial(mm, 1, lambda k: vD * k, cut=1.0) * mm ** 2 / (A1D / 12) - 1) for mm in (0.3, 0.03, 0.003)]
me_lin = max(abs(sz_matrix_element(vD * (kx_ * sx_ + ky_ * sy_) + 0.1 * sz_) - 1) for kx_, ky_ in ((0.3, 0.1), (-1.2, 0.7), (0.05, -2.0)))


def zsum_1d(m, v):
    """the plain sum of the claim scope, sum_k |<+|dH/dm|->|^2/(E_+ - E_-)^3, from diagonalising H(k) = v k sigma_x + m sigma_z"""
    def f(k):
        w_, V_ = np.linalg.eigh(v * k * sx_ + m * sz_)
        return abs(V_[:, 1].conj() @ sz_ @ V_[:, 0]) ** 2 / (w_[1] - w_[0]) ** 3
    edges = [0.0, m / v, 10 * m / v, 100 * m / v, np.inf]
    return 2 * sum(quad(f, a_, b_, limit=400, epsabs=0, epsrel=1e-10)[0] for a_, b_ in zip(edges[:-1], edges[1:])) / (2 * np.pi)


relsum = abs(zsum_1d(mB[0], vD) / (Z1D[0] / 2) - 1)
check(rel1 < 1e-8 and rel2 < 1e-8 and cutdev[0] > cutdev[1] > cutdev[2] and cutdev[0] > 1e-3 and me_lin < 1e-10 and relsum < 1e-7
      and abs(Z1D[0] * mB[0] ** 2 - 1 / 3) > 0.1,
      "B1b [T+D]", "normalization on explicit linear Dirac models H = v k.sigma + m sigma_z (v = 0.7), computed in k-space: Z m^(3-d) equals "
      "(A/4) I_d with A the k-mode density-of-states prefactor (1D: A = 1/(pi v), 2D: A = 1/(2 pi v^2)); with a momentum cutoff "
      "the law is asymptotic (relative deviation falls as m -> 0); the per-k matrix element |<+|sigma_z|->|^2 = e^2/E^2 is checked; the "
      "scope's plain sum sum |<+|dH|->|^2/(E_+ - E_-)^3, from diagonalisation, is half the B1 integral with rho = the k-mode density "
      "(B1's e^2/(4 E^5) per mode is the Inglis cranking form, twice the plain sum); control: the held absolute c_1 = 1/3 misses the 1D value",
      f"rel. error 1D {rel1:.1e}, 2D {rel2:.1e}; cutoff 1: deviation {', '.join(f'{c_:.1e}' for c_ in cutdev)} at m = 0.3, 0.03, 0.003; "
      f"matrix element {me_lin:.0e}; plain sum / (B1 integral / 2) - 1 = {relsum:.1e}; 1D Z m^2 = {Z1D[0]*mB[0]**2:.5f} = A/12 vs held 1/3")
# B1c (added 2026-11-14): nonlinear transverse dispersion in the same two-band family; the codimension-only exponent d - 3 fails
quadx = lambda k: k * k                                          # 1D quadratic crossing H = k^2 sigma_x + m sigma_z (d = 1, z = 2)
Zq = [zk_radial(mm, 1, quadx) for mm in mB]
pq = np.log(Zq[0] / Zq[1]) / np.log(mB[0] / mB[1])
Aq = 1 / (2 * np.pi)                                             # rho(e) = 2 (dk/de)/(2 pi) = e^(-1/2)/(2 pi): alpha = 1/2
relq = abs(Zq[0] * mB[0] ** 2.5 / (Aq / 4 * float(Igen.subs(al_, sp.Rational(1, 2)))) - 1)
qbt = lambda kx_, ky_: (kx_ ** 2 - ky_ ** 2) * sx_ + 2 * kx_ * ky_ * sy_   # 2D quadratic band touching (d = 2, z = 2)
iso = max(abs(np.linalg.eigvalsh(qbt(np.cos(t_), np.sin(t_)))[1] - 1) for t_ in np.linspace(0, np.pi, 17))
Zb = [zk_radial(mm, 2, quadx) for mm in mB + (1e-4,)]
pb = np.log(Zb[0] / Zb[1]) / np.log(mB[0] / mB[1])
Ab = 1 / (4 * np.pi)                                             # rho(e) = (d/de)(pi e/(2 pi)^2) = 1/(4 pi): alpha = 1
relb = abs(Zb[0] * mB[0] ** 2 / (Ab / 12) - 1)
dist_b = [np.sqrt(z_) * mm for z_, mm in zip(Zb, mB + (1e-4,))]  # sqrt(Z) m constant: canonical distance ~ ln(1/m), divergent
me_nl = max(abs(sz_matrix_element(H_ + 0.1 * sz_) - 1) for H_ in (qbt(0.4, -0.9), qbt(1.1, 0.2), 0.7 ** 2 * sx_))
okB1c = (abs(pq + 2.5) < 1e-6 and relq < 1e-8 and abs(pb + 2) < 1e-6 and relb < 1e-8 and iso < 1e-12 and me_nl < 1e-10
         and max(dist_b) / min(dist_b) - 1 < 1e-8 and abs(pq - (1 - 3)) > 0.4 and abs(pb - (2 - 3)) > 0.9)
check(okB1c, "B1c [T+D]", "nonlinear transverse dispersion (two-band, gap term sigma_z): a codimension-1 quadratic crossing H = k^2 sigma_x + m sigma_z "
      "has rho ~ e^(-1/2) and Z ~ m^(-5/2), and the 2D quadratic band touching H = (kx^2-ky^2) sigma_x + 2 kx ky sigma_y + m sigma_z "
      "(d = 2, z = 2) has Z ~ m^-2 and an infinite canonical distance; both follow the B1 law with alpha = d/z and its prefactor; "
      "control: the codimension-only exponent d - 3 (-2 and -1) is rejected in both, so d = 1 is not necessary for a pole outside linear dispersion",
      f"exponents {pq:+.6f} (alpha 1/2), {pb:+.6f} (alpha 1); prefactor rel. error {relq:.1e}, {relb:.1e}; QBT isotropy {iso:.0e}; "
      f"sqrt(Z) m at m = 1e-2, 1e-3, 1e-4: {', '.join(f'{x_:.6f}' for x_ in dist_b)}; matrix element {me_nl:.0e}")


def z_ratio(fun):
    zz = [fun(m) for m in (0.4, 0.2, 0.1)]
    return (zz[2] - zz[1]) / (zz[1] - zz[0])


def z1d(m):            # dimerised chain with gap 2*delta = m
    dd = m / 2
    return 0.5 * quad(lambda q: np.sin(q) ** 2 / (2 * np.sqrt(dd * dd + (1 - dd * dd) * np.sin(q / 2) ** 2)) ** 5,
                      0, np.pi, points=[dd], limit=500)[0] / np.pi


kx = (np.arange(1600) + 0.5) * 2 * np.pi / 1600
kp = (np.arange(160) + 0.5) * 2 * np.pi / 160


def z3d(m, kind):
    tot = 0.0
    cx, sx = np.cos(kx), np.sin(kx) ** 2
    for ky in kp:
        if kind == "nested":
            e2 = (-2 * (cx[None, :] + np.cos(ky) + np.cos(kp)[:, None])) ** 2
        else:
            e2 = sx[None, :] + np.sin(ky) ** 2 + np.sin(kp)[:, None] ** 2
        tot += np.sum(e2 / (4 * (e2 + m * m) ** 2.5))
    return tot / (1600 * 160 * 160)


R1, Rn, Rd = z_ratio(z1d), z_ratio(lambda m: z3d(m, "nested")), z_ratio(lambda m: z3d(m, "dirac"))
check(abs(R1 - 4) < 0.3 and abs(Rn - 4) < 0.6 and Rd < 1.6,
      "B2 [D]", "lattice check of the pole order, ratio [Z(0.1)-Z(0.2)]/[Z(0.2)-Z(0.4)] (4 for m^-2, 1 for log): 1D dimer "
      "chain and the 3D half-filled nearest-neighbour cubic sea (nested Fermi surface, fold = staggered gap) have the pole; "
      "a 3D lattice Dirac sea (point nodes, the update's light-band type) does not",
      f"1D {R1:.2f}, 3D nested {Rn:.2f}, 3D Dirac {Rd:.2f}")

print("== C. 1D star-rule toy (pole present): V and z computed on the dimer path")


def qint(fn, dl):      # integral over [0, pi] with geometric breakpoints at the gap scale
    e = [0.0] + [b for b in dl * 10.0 ** np.arange(0, 12) if b < np.pi] + [np.pi]
    return sum(quad(fn, e[i], e[i + 1], limit=200, epsabs=0, epsrel=1e-12)[0] for i in range(len(e) - 1))


def path(dl):          # exact infinite-chain correlators of the dimerised sea, t = 1 +- delta
    f = lambda q: np.sqrt(dl * dl + (1 - dl * dl) * np.sin(q / 2) ** 2)
    # sin^2/f - sin = -delta^2 cos^2 sin/(f (sin + f)) for these half-angles: the cancellation-free form (2026-11-14; the
    # subtracted form lost ~3e-3 of W at delta = 1e-9 to roundoff, the source of the quadrature warnings in the earlier cache)
    dsum = -qint(lambda q: -dl * dl * np.cos(q / 2) ** 2 * np.sin(q / 2) / (f(q) * (np.sin(q / 2) + f(q))), dl) / np.pi
    ddif = -dl * qint(lambda q: np.cos(q / 2) ** 2 / f(q), dl) / np.pi
    g_s = -1 / np.pi + dsum / 2 + ddif / 2
    g_w = -1 / np.pi + dsum / 2 - ddif / 2
    W = -(2 / 3) * dsum + (2 / 3) * (g_s - g_w) ** 2      # V0 - V_star
    z = qint(lambda q: np.sin(q) ** 2 / (2 * f(q)) ** 5, dl) / (2 * np.pi)
    return g_s, g_w, W, z


# real-space open-chain check of the correlators (delta = 0.3)
Nr, dl = 400, 0.3
h = np.zeros((Nr, Nr))
for i in range(Nr - 1):
    h[i, i + 1] = h[i + 1, i] = 1 + dl if i % 2 == 0 else 1 - dl
ev, evec = np.linalg.eigh(h)
G = evec[:, :Nr // 2] @ evec[:, :Nr // 2].T
gs3, gw3, W3, _ = path(0.3)
V0 = 0.5 + (4 / 3) * (-1 / np.pi - 1 / np.pi ** 2) + (2 / 3) * (2 / np.pi ** 2)
# ED check of the Wick reduction: Slater state of a 10-site open chain, bulk star energies
Ne = 10
he = np.zeros((Ne, Ne))
for i in range(Ne - 1):
    he[i, i + 1] = he[i + 1, i] = 1 + dl if i % 2 == 0 else 1 - dl
e_, U_ = np.linalg.eigh(he)
Phi = U_[:, :Ne // 2]
st, idx = sector(Ne)
amp = np.array([np.linalg.det(Phi[[j for j in range(Ne) if (s >> j) & 1], :]) for s in st])
Ge = Phi @ Phi.T
ok_w = True
for c in (3, 4):
    Pst = 0.5 * np.eye(len(st)) + (2 / 3) * (SS(st, idx, c - 1, c) + SS(st, idx, c, c + 1) + SS(st, idx, c - 1, c + 1))
    ed = amp @ Pst @ amp
    ga, gb = Ge[c - 1, c], Ge[c, c + 1]
    wick = 0.5 + (2 / 3) * ((ga - ga ** 2) + (gb - gb ** 2) + 2 * ga * gb)
    ok_w &= abs(ed - wick) < 1e-12
grid = np.concatenate([np.logspace(-9, -0.05, 260), 1 - np.logspace(-1.0, -6, 40)])
Wv, zv = np.zeros(len(grid)), np.zeros(len(grid))
for i, dl in enumerate(grid):
    _, _, Wv[i], zv[i] = path(dl)
mono = np.all(np.diff(Wv) > 0)
check(abs(G[200, 201] - gs3) < 1e-9 and abs(G[201, 202] - gw3) < 1e-9 and ok_w and mono and abs(Wv[-1] - V0) < 1e-5
      and abs(zv[0] * grid[0] ** 2 - 1 / (24 * np.pi)) < 1e-4,
      "C1 [T+D]", "on the dimer path (hop 1 +- delta; delta = 0 the sea, delta = 1 the fold) the star energy is a "
      "monotone funnel from V0 to 0, V0 - V ~ delta^2 ln^2(1/delta), and the one-loop stiffness has the pole "
      "z = 1/(24 pi delta^2); Wick reduction checked against a 10-site Slater state, correlators against a 400-site chain",
      f"V0 {V0:.5f}; V(0.1) {V0-path(0.1)[2]:.5f}; z delta^2 at 1e-9: {zv[0]*grid[0]**2:.6f} (1/24pi {1/(24*np.pi):.6f})")

# C1b (added 2026-11-14): convergence of the dimer-path quadratures against an independent implementation (mpmath tanh-sinh,
# 30 digits, same breakpoints) at seven delta, plus a control showing the comparison catches the old subtracted integrand.
mp.mp.dps = 30
def path_mp(dl):
    d_ = mp.mpf(dl); f_ = lambda q: mp.sqrt(d_ * d_ + (1 - d_ * d_) * mp.sin(q / 2) ** 2)
    pts = [mp.mpf(0)] + [d_ * mp.mpf(10) ** j for j in range(12) if d_ * mp.mpf(10) ** j < mp.pi] + [mp.pi]
    ds_ = -mp.quad(lambda q: -d_ * d_ * mp.cos(q / 2) ** 2 * mp.sin(q / 2) / (f_(q) * (mp.sin(q / 2) + f_(q))), pts) / mp.pi
    dd_ = -d_ * mp.quad(lambda q: mp.cos(q / 2) ** 2 / f_(q), pts) / mp.pi
    W_ = -(mp.mpf(2) / 3) * ds_ + (mp.mpf(2) / 3) * dd_ ** 2
    return float(W_), float(mp.quad(lambda q: mp.sin(q) ** 2 / (2 * f_(q)) ** 5, pts) / (2 * mp.pi))
def W_subtracted(dl):      # the pre-2026-11-14 form, for the control only
    f = lambda q: np.sqrt(dl * dl + (1 - dl * dl) * np.sin(q / 2) ** 2)
    ds_ = -qint(lambda q: np.sin(q / 2) ** 2 / f(q) - np.sin(q / 2), dl) / np.pi; dd_ = -dl * qint(lambda q: np.cos(q / 2) ** 2 / f(q), dl) / np.pi
    return -(2 / 3) * ds_ + (2 / 3) * dd_ ** 2
nIW = len(IW)
cmp_ = []
for dl in (1e-9, 1e-6, 1e-3, 0.05, 0.3, 0.9, 1 - 1e-6):
    a_, b_ = path(dl)[2:], path_mp(dl); cmp_.append((abs(a_[0] / b_[0] - 1), abs(a_[1] / b_[1] - 1)))
nIW_cmp = len(IW) - nIW
ctl = abs(W_subtracted(1e-9) / path_mp(1e-9)[0] - 1); nIW_ctl = len(IW) - nIW - nIW_cmp
check(max(c[0] for c in cmp_) < 1e-7 and max(c[1] for c in cmp_) < 1e-12 and nIW == 0 and nIW_cmp == 0 and ctl > 1e-4,
      "C1b [D]", "quadrature convergence: the dimer-path V and z used for C1-C2 agree with an independent 30-digit mpmath quadrature at "
      "delta = 1e-9 .. 1 - 1e-6, with no integration warning over the 300-point grid; control: the earlier subtracted integrand is off "
      "by > 1e-4 at delta = 1e-9 and raises the warnings the earlier cache showed",
      f"max rel diff W {max(c[0] for c in cmp_):.1e}, z {max(c[1] for c in cmp_):.1e}; warnings on the grid {nIW}; control rel err {ctl:.1e} with {nIW_ctl} warnings")
u = np.log(grid)
sW, sz = CubicSpline(u, np.log(Wv)), CubicSpline(u, np.log(zv))


def slowroll(sW, sz, V0, ulo, uhi, zeta, Nstar=55.0):
    """slow roll on lnW(u), lnz(u), u = ln(order parameter); W = V0 - V; chi = zeta int sqrt(z) e^u du (M_P units)"""
    uu = np.linspace(ulo, uhi, 40000)
    lW, l1, l2, lz1 = sW(uu), sW(uu, 1), sW(uu, 2), sz(uu, 1)
    lp = np.log(zeta) + uu + 0.5 * sz(uu)
    V = V0 - np.exp(lW)
    rat = np.exp(lW - 2 * lp)                       # W / p^2
    eps = 0.5 * l1 ** 2 * np.exp(2 * (lW - lp)) / V ** 2
    eta = -(rat / V) * ((l2 + l1 ** 2) - l1 * (1 + 0.5 * lz1))
    dN = V / (rat * l1)
    Ncum = np.concatenate([[0], np.cumsum(0.5 * (dN[1:] + dN[:-1]) * np.diff(uu))])
    iend = np.argmax(eps >= 1.0) if np.any(eps >= 1.0) else len(uu) - 1
    Nfrom = Ncum[iend] - Ncum
    j = np.argmin(np.abs(Nfrom - Nstar))
    return 1 - 6 * eps[j] + 2 * eta[j], 16 * eps[j], uu[j], uu[iend], eta[j], Nfrom[0]


JA = np.sqrt(3.0)          # supplied: hop scale J = sqrt(3)/a (eps0/tick, tied lapse)
rows = []
for r in (0, 2, 4):
    zeta = JA ** -0.5 * 2.0 ** -r      # M_P a = 1 at the flat cell rung (unit map); coarser rung r
    ns, rr, us, ue, et, _ = slowroll(sW, sz, V0, u[0], u[-1], zeta)
    rows.append((r, zeta, ns, rr, np.exp(us), np.exp(ue)))
ok = all(abs(ns - (1 - 2 / 55)) < 0.012 and dend < 1 for (_, _, ns, _, _, dend) in rows)
check(ok, "C2 [D]", "slow roll on the computed V_star and z (canonical chi = zeta int sqrt(z) d delta, zeta = (J a)^-1/2 "
      "/(M_P a_r), M_P a = 1 at the flat rung): the fold is critically slowed near the sea, V(chi) is an exponential "
      "plateau, n_s ~ 1 - 2/N independent of the coupling and the rung, r ~ 2 zeta^2 z0/N^2; the plateau ends (eps = 1) "
      "before the fold completes (graceful exit)",
      "; ".join(f"rung {r}: n_s {ns:.4f} r {rr:.1e} delta* {ds:.0e} end {de:.2f}" for (r, z_, ns, rr, ds, de) in rows))

z0 = 1 / (24 * np.pi)
lam55 = 2 ** (-2 / 55)
Nact = 2 / (1 - NS_ACT)
check(abs(lam55 - 0.9751) < 1e-3 and 0.9731 < lam55 < 0.9788,
      "C3 [T]", "per-split factor of this clock: lam = 2^(n_s-1) = 2^(-2/N), not constant (running -2/N^2); Planck's "
      "range is met at N* = 55, ACT's 0.974 needs N* = 77 (same as every exponential plateau, act-tilt)",
      f"lam(55) {lam55:.4f}; running {-2/55**2:.1e}; N for ACT {Nact:.0f}")

# A_s: V0/M_P^4 = gamma V0 sqrt3 2^-4r, eps = s^2/(8N^2), s^2 = z0 2^-2r/sqrt3 -> A_s = gamma V0 N^2 2^-2r/(pi^2 z0)
gamma = 1.0
two_m2r = np.pi ** 2 * z0 * A_S / (gamma * V0 * 55 ** 2)
rung = -0.5 * np.log2(two_m2r)
HoverMP = np.sqrt(gamma * V0 * JA / 3) * two_m2r
r_t = 2 * (two_m2r / JA) * z0 / 55 ** 2
check(18 < rung < 22 and r_t < R_MAX,
      "C4 [T+E]", "amplitude: A_s = gamma V0 N^2 2^(-2r)/(pi^2 z0) fixes the fold rung, ~20 rungs above the cell for "
      "fold coupling gamma = 1 (gamma supplied; rung = 19.8 + log2(gamma)/2); then H/M_P and r are tiny",
      f"2^-2r {two_m2r:.2e}, rung {rung:.1f}, H/M_P {HoverMP:.1e}, r {r_t:.0e}")

# split re-seeding: children born unfolded with share x -> per-split energy factor q = 1/8 + 7x/8
q_need = 2 ** (-2 * 0.0175)
x_need = (8 * q_need - 1) / 7
check(abs((1 / 8 + 7 * 1 / 8) - 1) < 1e-15 and abs(16 * 0.0175 - 0.28) < 1e-12,
      "C5 [T]", "if the split births children unfolded (share x), the per-split vacuum-energy factor is q = 1/8 + 7x/8: "
      "x = 1 is exact de Sitter with no exit, constant x < 1 is power-law (r = 16 eps, inflaton-design B1): the "
      "re-seeded unfolded share is not a clock; the clock needs the split to carry the fold order (children inherit)",
      f"x for q = {q_need:.4f}: {x_need:.4f}; r = {16*0.0175:.2f}")

print("== D. the update's sea: an isotropic Dirac band (point node), d = 3")
Lc = (6 * np.pi ** 2) ** (1 / 3)        # supplied: ball cutoff with one mode per cell volume
mf = 1.0                                # supplied: fold gap in cell units


def zd(m):
    return quad(lambda k: k ** 4 / (2 * (k * k + m * m) ** 2.5), 0, Lc, points=[m], limit=200)[0] / (2 * np.pi ** 2)


z1 = 1 / (4 * np.pi ** 2)
c2 = Lc ** 2 / (4 * np.pi ** 2)
mg = np.logspace(-6, 0, 200)
Wd = np.array([quad(lambda k: k * k * (np.sqrt(k * k + m * m) - k), 0, Lc, points=[m], limit=200)[0] / np.pi ** 2 for m in mg])
V0d = Wd[-1]
zdv = np.array([zd(m) for m in mg])
ua = np.linspace(-4000, np.log(mg[0]), 400)[:-1]          # small-m asymptotics (B1): W = c2 m^2, z = z1 (ln(2L/m) - 4/3)
lWa = np.log(c2) + 2 * ua
lza = np.log(z1 * (np.log(2 * Lc) - ua - 4 / 3))
cont = (abs(np.log(Wd[0]) - (np.log(c2) + 2 * np.log(mg[0]))), abs(np.log(zdv[0]) - np.log(z1 * (np.log(2 * Lc / mg[0]) - 4 / 3))))
ud = np.concatenate([ua, np.log(mg)])
sWd = CubicSpline(ud, np.concatenate([lWa, np.log(Wd)]))
szd = CubicSpline(ud, np.concatenate([lza, np.log(zdv)]))
zeta_need = np.sqrt(4 / ((1 - NS_PL) ** 2 * 55) * c2 / (V0d * z1))
etas = [slowroll(sWd, szd, V0d, ud[0], ud[-1], 2.0 ** -r) for r in (0, 4)]
check(all(abs(e[4]) > 0.3 for e in etas) and zeta_need > 10 and max(cont) < 1e-3,
      "D1 [T+D]", "linear point node (d = 3, B1 with A = 1/pi^2 in this model's normalization, so z1 = A/4 = 1/(4 pi^2)): "
      "with the stiffness only logarithmic, the plateau curvature is eta ~ -sqrt(c2/(V0 zeta^2 z1 N)) "
      "(log asymptotics): at N* = 55 the fold is fast at the flat rung and worse at coarser rungs (zeta = 2^-r); "
      "n_s = 0.965 would need zeta ~ 50, a cell far below the Planck length, against M_P a = 1 (unit map)",
      "; ".join(f"rung {r}: eta {e[4]:.2f} n_s {e[0]:.2f} at ln m* {e[2]:.0f}" for r, e in zip((0, 4), etas)) + f"; zeta needed {zeta_need:.0f}")

Hta = 1.93e-5          # r < 0.036 bound on H a (cell scale), cites inflaton A1
gap = gaps[12]
ticks_gen = np.log(2) / Hta
check(ticks_gen * gap > 1e4,
      "D2 [E]", "fold speed in ticks: a gapped local fold relaxes in ~1/gap ticks, a split takes >= ln2/(H a) cell times, "
      "so without the pole the fold finishes 1e4 times within one split: no clock (the lattice eta problem, inflaton-design C1)",
      f"gap {gap:.3f}; cell times per split >= {ticks_gen:.1e}; folds per split >= {ticks_gen*gap:.0e}")

print("== E. reheating: misfolds")
pair = gaps[12]
nmis = 2 * V0 / pair
check(0 < nmis < 1,
      "E1 [T+E]", "the fold rule is >= 0 and vanishes only on folds, so all plateau energy that leaves the coherent mode "
      "sits in misfolds (domain walls: free sites, matter in the neighbourhood reading); full conversion of V0 gives a dense "
      "misfold gas (walls per site <= 2 V0/gap_pair), reheating at the fold scale, then diluted by splits as matter",
      f"V0 {V0:.4f}; pair gap (N=12) {pair:.3f}; walls/site <= {nmis:.2f}")

print("supplied: star rule; dimer path (one-loop mean field); J a = sqrt3; M_P a = 1 at the flat rung (unit map); fold "
      "rung; gamma = 1; N* = 55; Dirac ball cutoff; fold gap m_f = 1; semiclassical FRW with Hubble friction")
print(f"warnings raised in this run: {len(IW)} (all from the C1b control's subtracted integrand: {nIW + nIW_cmp == 0 and len(IW) == nIW_ctl}); kinds: {sorted(set(c for c, _ in IW))}")
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
sys.exit(0 if NF == 0 else 1)
