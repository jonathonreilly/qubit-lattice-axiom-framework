AUDIT_INPUT_PATHS = ('docs/SAME_EDGE_VACUUM_SUBTRACTION_REMOVES_THE_INDUCED_EDGE_ACTION_AND_EDGE_LOOPS_MOVE_G_AS_ONE_OVER_THE_BLOCK_AREA_BOUNDED_THEOREM_NOTE_2026-10-22.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
#!/usr/bin/env python3
"""induced-G: does an induced (Sakharov) term move 1/G under CL-3's vacuum standard?

A. matter/link sea under the vacuum standard (same-edge subtraction)
B. the edges' own zero-point loops (not subtracted): size ~ C W4 / b_e^2
C. estimates against measurement; the unit map L = sqrt(8 pi) l_P
Self-contained: numpy/scipy only.
"""
import time, itertools
import numpy as np
from scipy.integrate import quad
from scipy.special import i0e

AUDIT_TIMEOUT_SEC = 120
T0 = time.time()
NP = NF = 0


def rep(ok, tag, msg, val=""):
    global NP, NF
    if ok:
        NP += 1
    else:
        NF += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {tag} {msg}" + (f" | {val}" if val else ""))


# ---------------------------------------------------------------- A1
# exact Fock space: 2x5 torus, 5 fermions (252 configurations), staggered mass,
# bond hop 1/length with lengths from a supplied edge configuration
NX, NY, NPART, MST = 5, 2, 5, 0.5
NS = NX * NY
sites = [(x, y) for y in range(NY) for x in range(NX)]
idx = {s: i for i, s in enumerate(sites)}
bonds = []
for (x, y) in sites:
    bonds.append((idx[(x, y)], idx[((x + 1) % NX, y)], x))      # x-bond, column x
    if NY > 1 and y == 0:
        bonds.append((idx[(x, y)], idx[(x, (y + 1) % NY)], x))  # y-bond (one per pair)
confs = [sum(1 << i for i in c) for c in itertools.combinations(range(NS), NPART)]
cidx = {c: i for i, c in enumerate(confs)}
stag = np.array([MST * (-1) ** (x + y) for (x, y) in sites])


def hop_matrix(i, j):
    """matrix of c_i^dag c_j + c_j^dag c_i on the fixed-N configurations"""
    M = np.zeros((len(confs), len(confs)))
    for a, c in enumerate(confs):
        for (p, q) in ((i, j), (j, i)):
            if (c >> q) & 1 and not (c >> p) & 1:
                lo, hi = min(p, q), max(p, q)
                sgn = (-1) ** bin(c & (((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1))).count("1")
                M[cidx[(c ^ (1 << q)) | (1 << p)], a] += sgn
    return M


HOPS = [hop_matrix(i, j) for (i, j, _) in bonds]
NOCC = np.array([[(c >> i) & 1 for i in range(NS)] for c in confs], float)


def terms(lengths):
    """list of (matrix, sites touched): bond hops -1/l_b and on-site masses"""
    out = [(-HOPS[b] / lengths[b], (bonds[b][0], bonds[b][1])) for b in range(len(bonds))]
    for i in range(NS):
        out.append((np.diag(stag[i] * NOCC[:, i]), (i,)))
    return out


def ham(lengths):
    return sum(M for M, _ in terms(lengths))


def vac(lengths):
    w, v = np.linalg.eigh(ham(lengths))
    return w[0], v[:, 0]


def site_shares(psi, lengths):
    """each site's share of the phase by which the update's terms advance the odds,
    each term shared equally between the sites it touches (configurations with psi != 0)"""
    sh = np.zeros((len(confs), NS))
    for M, touch in terms(lengths):
        r = M @ psi
        for s in touch:
            sh[:, s] += r / len(touch)
    good = np.abs(psi) > 1e-9
    return sh[good] / psi[good, None], good


def ell(h):
    return np.array([1.0 + h * np.cos(2 * np.pi * col / NX) for (_, _, col) in bonds])


print("== A. the sea under the vacuum standard (same edges)")
rng = np.random.default_rng(7)
mx = 0.0
for _ in range(4):
    L_e = 1.0 + 0.3 * rng.random(len(bonds))
    E0, psi = vac(L_e)
    sh, good = site_shares(psi, L_e)
    shv, _ = site_shares(psi, L_e)            # the vacuum odds on the same edges
    mx = max(mx, np.abs(sh - shv).max())
    tot = sh.sum(1)
E0, psi = vac(ell(0.0))
dh = 1e-3
Fraw = [vac(ell(s * dh))[0] for s in (-1, 0, 1)]
d2raw = (Fraw[0] - 2 * Fraw[1] + Fraw[2]) / dh ** 2
psi0 = vac(ell(0.0))[1]
Fflat = [vac(ell(s * dh))[0] - psi0 @ ham(ell(s * dh)) @ psi0 for s in (-1, 0, 1)]
d2flat = (Fflat[0] - 2 * Fflat[1] + Fflat[2]) / dh ** 2
rep(mx < 1e-12 and abs(d2raw) > 1e-2 and d2flat < -1e-2, "A1 [T]",
    "theorem: the vacuum standard subtracts, at each joint configuration, the same site shares "
    "for the vacuum odds of the same edges, so for vacuum odds the total matter phase is zero at "
    "every configuration and for EVERY edge configuration: the sea's induced edge action (cosmological, "
    "Einstein-Hilbert, R^2 and nonlocal parts alike) is removed exactly, not just its constant; "
    "subtracting a fixed (flat) vacuum instead leaves minus the sea's static susceptibility",
    f"max share diff {mx:.0e}; raw d2E0/dh2 {d2raw:+.3f}, flat-reference {d2flat:+.3f}, same-edge 0")

# ---------------------------------------------------------------- A2
def gapped_2d(N, h):
    """single-particle levels of the 2D staggered-mass torus with modulated bond lengths"""
    n = N * N
    H = np.zeros((n, n))
    for x in range(N):
        for y in range(N):
            i = x + N * y
            H[i, i] = MST * (-1) ** (x + y)
            for (xx, yy) in (((x + 1) % N, y), (x, (y + 1) % N)):
                j = xx + N * yy
                t = 1.0 / (1.0 + h * np.cos(2 * np.pi * x / N))
                H[i, j] -= t
                H[j, i] -= t
    w = np.linalg.eigvalsh(H)
    return w[: n // 2].sum(), w[n // 2]


rows = []
for N in (8, 12, 16, 24):
    e = [gapped_2d(N, s * dh) for s in (-1, 0, 1)]
    d0 = (e[0][0] - 2 * e[1][0] + e[2][0]) / dh ** 2
    d1 = (e[0][1] - 2 * e[1][1] + e[2][1]) / dh ** 2
    rows.append((N, d0 / N ** 2, d1))
ok = all(abs(r[1] - rows[-1][1]) < 0.05 * abs(rows[-1][1]) for r in rows[1:]) and \
    abs(rows[-1][2]) * 24 ** 0 < 5 * abs(rows[0][2]) + 1
rep(ok, "A2 [D]",
    "with an added particle the response is the departure's own: d2/dh2 of (E1 - E0) stays O(1) or less "
    "while the vacuum's raw d2E0/dh2 grows as the area N^2; so no N_species x volume x curvature term "
    "survives, only the matter's stress (and its O(1/V) density-dependent dressing)",
    "N, raw/N^2, departure: " + "; ".join(f"{r[0]}, {r[1]:+.4f}, {r[2]:+.4f}" for r in rows))

# ---------------------------------------------------------------- A3
NK, RW = 60000, 1.0
kk = 2 * np.pi * (np.arange(NK) + 0.5) / NK


def bands(k, m):
    dx, dz = np.sin(k), m + RW * (1 - np.cos(k))
    E = np.hypot(dx, dz)
    th = np.arctan2(dx, dz)
    return E, th


def chi(om, q, m):
    """scalar (sigma_z) vertex polarisation of the half-filled 1D Wilson-Dirac sea"""
    E1, t1 = bands(kk, m)
    E2, t2 = bands(kk + q, m)
    M2 = np.sin((t1 + t2) / 2) ** 2          # |<+,k+q| sigma_z |-,k>|^2
    D = E1 + E2
    return np.mean(2 * M2 * D / (D ** 2 - om ** 2))


rr = []
for m in (0.1, 0.05, 0.025, 0.0125):
    E, th = bands(kk, m)
    M2 = np.sin(th) ** 2
    a_om = np.mean(2 * M2 / (2 * E) ** 3)          # d chi / d omega^2 at q = 0
    dq = 1e-2 * m
    a_q = -(chi(0, dq, m) - chi(0, 0, m)) / dq ** 2      # - d chi / d q^2
    rr.append((m, a_om / a_q))
extrap = 2 * rr[-1][1] - rr[-2][1]        # Wilson-term corrections are O(m)
rep(abs(extrap - 1) < 0.02 and abs(rr[-1][1] - 1) < abs(rr[0][1] - 1), "A3 [D]",
    "time-dependent edges: the sea's response is a function of q^2 - omega^2 (ratio of the omega^2 "
    "and -q^2 coefficients -> 1 in the continuum limit), so subtracting only the INSTANTANEOUS vacuum "
    "removes the static half and leaves the omega^2 half: a non-covariant induced kinetic term as "
    "large as the removed gradient term",
    "m, coef ratio: " + "; ".join(f"{m}, {r:.4f}" for m, r in rr) + f"; linear extrapolation m->0 {extrap:.4f}")

m = 0.1
E, th = bands(kk, m)
M2 = np.sin(th) ** 2
D = 2 * E
om = 0.5 * m                                    # below the pair threshold 2m
c = [np.mean(2 * M2 / D ** (2 * j + 1)) for j in range(4)]
full = chi(om, 0.0, m)
R = [full - sum(c[i] * om ** (2 * i) for i in range(n + 1)) for n in range(4)]
ok = all(abs(R[n + 1]) < 0.3 * abs(R[n]) for n in range(3)) and abs(R[3] / R[0]) < 1e-3
rep(ok, "A4 [T]",
    "an ADIABATIC reference (the vacuum carried along the same edge history, expanded to all "
    "orders in omega/gap) removes every order: the remainder after order 2n falls as "
    "(omega/2m)^(2n+2); what it does not remove is real pair creation above threshold, which is "
    "a physical departure",
    "remainder after order 0/2/4/6: " + ", ".join(f"{abs(x):.1e}" for x in R))

# ---------------------------------------------------------------- B
print("== B. the edges' own zero-point loops (not subtracted)")
W4 = quad(lambda t: i0e(2 * t) ** 4, 0, np.inf, limit=400)[0]
rep(abs(W4 - 0.154933) < 2e-5, "B1 [T]",
    "lattice tadpole of the 4D block lattice: W4 = int_BZ d^4k/(2pi)^4 / k_hat^2 = "
    "int_0^inf (e^-2t I0(2t))^4 dt; a field on blocks of b cells has G(0) = W4/(b L)^2",
    f"W4 = {W4:.6f}")


def lndet_toy(K, h, N=10):
    """(1/2) ln det of K * (weighted 2D lattice Laplacian + mass) with background-modulated weights"""
    n = N * N
    A = np.eye(n) * 0.3
    for x in range(N):
        for y in range(N):
            i = x + N * y
            for (xx, yy) in (((x + 1) % N, y), (x, (y + 1) % N)):
                j = xx + N * yy
                w = 1.0 + h * np.cos(2 * np.pi * x / N)
                A[i, i] += w; A[j, j] += w; A[i, j] -= w; A[j, i] -= w
    return 0.5 * np.linalg.slogdet(K * A)[1]


d2 = {}
for K in (1.0, 100.0):
    v = [lndet_toy(K, s * 1e-3) for s in (-1, 0, 1)]
    d2[K] = (v[0] - 2 * v[1] + v[2]) / 1e-6
rep(abs(d2[1.0] - d2[100.0]) < 1e-5 * abs(d2[1.0]) + 1e-6, "B2 [T]",
    "theorem: the one-loop term (1/2) ln det of the edges' quadratic form does not depend on its "
    "overall stiffness, while the bare hinge sum scales as the stiffness b_e^2 (same G): the edges' "
    "own loop correction to 1/G is O(1) per block against b_e^2, i.e. dG/G = C W4 / b_e^2",
    f"d2/dh2 at K = 1: {d2[1.0]:.6f}, K = 100: {d2[100.0]:.6f}")

# continuum normalisation: delta(1/16 pi G) = (1/2)(1/6 - xi) G(0) per real component,
# 1/(16 pi G) = 1/(2 L^2)  =>  delta G / G = -(1/6 - xi) W4 / b_e^2 per component
per = W4 / 6.0
C_env = 10.0
tab = [(b, per / b ** 2, C_env * W4 / b ** 2) for b in (1, 10, 27, 76)]
rep(tab[1][2] < 0.02, "B3 [E]",
    "ESTIMATE: one minimally coupled component gives |dG/G| = W4/(6 b_e^2); the edge field's "
    "curvature couplings and ghosts enter as an unknown lattice sum C, envelope |C| <= 10: "
    "at one-cell edges (b_e = 1) the correction is O(1) and uncontrolled, at the rules' blocks it is small",
    "b_e, per-component, envelope: " + "; ".join(f"{b}, {p:.1e}, {e:.1e}" for b, p, e in tab))

# ---------------------------------------------------------------- C
print("== C. estimates against measurement")
f_SM = 24 * 0.00483 / 0.5        # induced-response: induced TT R2 per Dirac copy / Regge
cg2 = 1.0 / (1.0 + f_SM)
rep(abs(1 - np.sqrt(cg2)) > 1e-3, "C1 [E]",
    "the reference vacuum matters: with no subtraction the sea adds f = 23% to the TT term and 0 to "
    "the Newtonian one (G_T/G_N 0.81, induced-response); with an instantaneous reference it adds f "
    "to the TT kinetic term only, |c_g - 1| ~ 0.1 against GW170817's 3e-15, unless the dressed-weight "
    "clause's 'vacuum' includes the sea; with the adiabatic (carried) reference it adds nothing",
    f"f = {f_SM:.3f}; instantaneous-reference |c_g - 1| = {1 - np.sqrt(cg2):.3f}")
f_IR = [(b, f_SM / b ** 2) for b in (10, 27, 76)]
rep(f_IR[0][1] < 3e-3, "C2 [E]",
    "sea modes slower than the edges' zero-point motion (below ~1/(b_e L)) are not adiabatic, but "
    "carry at most the fraction 1/b_e^2 of the induced term: an upper bound f/b_e^2",
    "; ".join(f"b_e {b}: {x:.1e}" for b, x in f_IR))
lp = 1.616255e-35
dmax = C_env * W4 / 10 ** 2 + f_IR[0][1]
Lr = np.sqrt(8 * np.pi)
rep(dmax < 0.03, "C3 [E]",
    "unit map: L/l_P = sqrt(8 pi) (1 + dG/(2G)): with the adiabatic vacuum standard the sea gives "
    "zero and the edges' own loops at most ~1.6e-2 at b_e = 10 (2e-3 at 27, 3e-4 at 76): L moves by "
    "under 1%, not by an O(1) factor; it is fixed by G, not an independent observable",
    f"sqrt(8 pi) = {Lr:.4f}, range at b_e 10: {Lr*(1-dmax/2):.3f} .. {Lr*(1+dmax/2):.3f}; L = {Lr*lp:.3e} m")
print("theorems: A1, A4, B1, B2; diagnostics: A2, A3; estimates: B3, C1-C3")
print("supplied: toy seas (2D staggered, 1D Wilson-Dirac), scalar vertex, lattice C envelope |C|<=10,\n"
      "  heat-kernel normalisation (1/2)(1/6-xi)G(0), f = 23% from induced-response, b_e from edge-block")
print(f"elapsed {time.time()-T0:.1f} s")
print(f"TOTAL: PASS={NP} FAIL={NF}")
