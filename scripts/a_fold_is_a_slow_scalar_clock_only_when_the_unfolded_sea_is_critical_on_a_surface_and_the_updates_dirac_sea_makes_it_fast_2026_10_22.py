AUDIT_INPUT_PATHS = ('docs/A_FOLD_IS_A_SLOW_SCALAR_CLOCK_ONLY_WHEN_THE_UNFOLDED_SEA_IS_CRITICAL_ON_A_SURFACE_AND_THE_UPDATES_DIRAC_SEA_MAKES_IT_FAST_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""Fold order parameter as the scalar clock (finite runner, seeded).

Asks whether the grid folding (unfolded odds -> star-rule pair fold) gives a
slow scalar clock, with V(phi) and the stiffness computed, not chosen.
  A  funnel ends: star rule = Majumdar-Ghosh form; uniform odds sit at the top
     as an exact eigenstate; the sea sits on a downhill funnel; fold weight
  B  speed: stiffness Z of a fold order parameter of a gapless sea,
     Z ~ m^(d-3) (d = codimension of the gapless set); 1D, 3D nested, 3D Dirac
  C  1D toy with the pole: exact V_star(delta), z(delta) on the dimer path;
     slow roll, n_s, r, exit, A_s; split re-seeding arithmetic
  D  3D Dirac sea (the update's light band): fast roll at every allowed rung
  E  reheating into misfolds
Supplied numbers are named in the output. Measured numbers enter only C/D/E.
"""
import time
import itertools
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

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
x, d = sp.symbols("x d", positive=True)
I1 = sp.integrate(x ** 2 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, sp.oo))
I2 = sp.integrate(x ** 3 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, sp.oo))
Lam = sp.symbols("Lambda", positive=True)
I3 = sp.limit(sp.integrate(x ** 4 / (1 + x ** 2) ** sp.Rational(5, 2), (x, 0, Lam)) - sp.log(Lam), Lam, sp.oo)
check(I1 == sp.Rational(1, 3) and I2 == sp.Rational(2, 3) and I3.is_finite,
      "B1 [T]", "adiabatic stiffness of a gap-opening fold order parameter m on a sea with gapless-set codimension d: "
      "Z(m) = int rho(e) e^2/(4(e^2+m^2)^(5/2)) de, rho ~ e^(d-1), so Z = c_d m^(d-3): d=1 (a surface of gapless modes) a "
      "pole m^-2, d=3 (Dirac points) only log(1/m); the unfolded point is at infinite field distance iff d = 1",
      f"c_1 = {I1}, c_2 = {I2}, d=3: log + {sp.nsimplify(I3)}")


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
    dsum = -qint(lambda q: np.sin(q / 2) ** 2 / f(q) - np.sin(q / 2), dl) / np.pi
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
      "D1 [T+D]", "with the stiffness only logarithmic, the plateau curvature is eta ~ -sqrt(c2/(V0 zeta^2 z1 N)) "
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
print(f"elapsed {time.time()-T0:.1f}s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
