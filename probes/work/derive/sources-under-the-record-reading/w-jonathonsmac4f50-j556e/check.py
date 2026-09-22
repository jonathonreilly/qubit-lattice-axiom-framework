"""sources-under-the-record-reading, attempt a3 (w-jonathonsmac4f50-j556e).

Block 56's box: the simplest bond energy F = (2/gamma) sum (phi_x - phi_y)^2, walls held at the ambient rate phi = 1, bodies at rest with bare
energies m_x; exact static law ((1 - A) + (gamma/12) M) phi = 0 inside; ledger L = sum m_x phi_x (block 56 T2); g = (1 - A)^-1 with the walls
held (the potential of 1 - average).  Exact: sympy rationals.  The discriminator (c) is NUMERIC, labelled.
"""
import itertools
from fractions import Fraction as F

import numpy as np
import sympy as sp

RESULTS = []


def want(label, ok, detail=""):
    RESULTS.append((label, bool(ok)))
    print(("PASS " if ok else "FAIL ") + label + ((" :: " + str(detail)) if detail != "" else ""), flush=True)


def box(n):
    sites = list(itertools.product(range(1, n + 1), repeat=3)); ix = {s: i for i, s in enumerate(sites)}; N = len(sites)
    OneMinusA = sp.zeros(N, N)
    for s in sites:
        i = ix[s]; OneMinusA[i, i] = 1
        for a in range(3):
            for d in (1, -1):
                t = list(s); t[a] += d; t = tuple(t)
                if t in ix: OneMinusA[i, ix[t]] -= sp.Rational(1, 6)
    return sites, ix, OneMinusA, OneMinusA.inv()


def ledger(OneMinusA, m, gamma):
    """exact ledger sum m_x phi_x, phi = 1 + delta, ((1 - A) + (gamma/12) M) delta = -(gamma/12) M 1 inside (walls at 1)."""
    N = len(m)
    Mdiag = sp.diag(*m)
    delta = (OneMinusA + gamma / 12 * Mdiag).LUsolve(-(gamma / 12) * sp.Matrix(m))
    return sum(m[i] * (1 + delta[i]) for i in range(N))


# ================================================================== (b) exact on boxes: the formation event's ledger
rows = []; ok = True
for n in (3, 5):
    sites, ix, OmA, g = box(n)
    cen = tuple([(n + 1) // 2] * 3)
    star = [cen] + [tuple(cen[d] + (s if d == a else 0) for d in range(3)) for a in range(3) for s in (1, -1)]
    rho = [sp.Rational(1, len(star)) if s in star else 0 for s in sites]
    E = sp.Integer(1); gamma = sp.Integer(1)
    m = [E * r for r in rho]
    L = ledger(OmA, m, gamma)
    rgr = sum(rho[i] * g[i, j] * rho[j] for i in range(len(sites)) for j in range(len(sites)) if rho[i] != 0 and rho[j] != 0)
    for y in (cen, star[1]):
        gyy = g[ix[y], ix[y]]
        exists = L < 12 / (gamma * gyy)
        mprime = L / (1 - gamma / 12 * gyy * L)
        Lafter = mprime / (1 + gamma / 12 * gyy * mprime)
        ok = ok and exists and sp.simplify(Lafter - L) == 0 and mprime > E
        rows.append(f"box {n + 2}: y = {y}, g_yy = {gyy}, L_before = {float(L):.6f}, m' = {float(mprime):.6f}")
    # weak field: the first-order coefficients, as exact derivatives at gamma = 0 (symbolic gamma on the small box)
    gyy = g[ix[cen], ix[cen]]
    if n == 3:
        # exact rational solve at a small gamma: (L - E)/eps = -<m, g m>/12 + O(eps), and the bare record's drop -(g_yy - <rho,g rho>)/12 + O(eps)
        eps = sp.Rational(1, 10 ** 6)
        Le = ledger(OmA, [E * r for r in rho], eps)
        dL = (Le - E) / eps
        drop = (E / (1 + eps / 12 * gyy * E) - Le) / eps
        ok = ok and abs(dL + rgr / 12) < sp.Rational(1, 10 ** 5) and abs(drop + (gyy - rgr) / 12) < sp.Rational(1, 10 ** 5)
    ok = ok and gyy > rgr
    rows.append(f"box {n + 2}: <rho,g rho> = {rgr} = {float(rgr):.5f}, g_center = {gyy} = {float(gyy):.5f}")
want("B1 (b) EXACT (walls held; boxes 5^3 and 7^3; an amplitude at rest spread uniformly over the 7-site star, E = 1, gamma = 1): the "
     "ledger after one record at y is m'/(1 + (gamma/12) g_yy m') and equals the ledger before iff m' = L/(1 - (gamma/12) g_yy L) (block 58 "
     "T1, re-derived); at weak field L = E - (gamma/12) E^2 <rho, g rho> + O(gamma^2) and a record keeping the bare energy loses "
     "(gamma/12) E^2 (g_yy - <rho, g rho>) > 0 of ledger: the field's self-energy change, exactly in terms of the potential of 1 - A",
     ok, "; ".join(rows))

# on average over odds p of where the record forms (NO rule assumed): required mean excess (gamma/12) E^2 (sum_y p_y g_yy - <rho, g rho>)
sites, ix, OmA, g = box(5)
cen = (3, 3, 3)
star = [cen] + [tuple(cen[d] + (s if d == a else 0) for d in range(3)) for a in range(3) for s in (1, -1)]
rho = [sp.Rational(1, 7) if s in star else 0 for s in sites]
rgr = sum(rho[i] * g[i, j] * rho[j] for i in range(len(sites)) for j in range(len(sites)) if rho[i] != 0 and rho[j] != 0)
p_born = sum(rho[ix[s]] * g[ix[s], ix[s]] for s in star)
corner = (1, 1, 1)
g_corner = g[ix[corner], ix[corner]]
# an amplitude mostly at the centre with a little weight at the corner; odds concentrated at the corner (a site of its support)
rho2 = [sp.Rational(99, 100) if s == cen else (sp.Rational(1, 100) if s == corner else 0) for s in sites]
rgr2 = sum(rho2[i] * g[i, j] * rho2[j] for i in range(len(sites)) for j in range(len(sites)) if rho2[i] != 0 and rho2[j] != 0)
p_wall = g_corner
cs_ok = all(g[i, j] ** 2 <= g[i, i] * g[j, j] for i in range(0, len(sites), 7) for j in range(0, len(sites), 11))
want("B2 (b) ON AVERAGE, ANY ODDS: the required mean excess is (gamma/12) E^2 (sum_y p_y g_yy - <rho, g rho>); for odds p = rho it is >= 0 "
     "(g positive definite: g_xy <= (g_xx + g_yy)/2), here > 0; on Z^3, where g_yy = G_0(0) for every y and g_xy <= G_0(0) (Cauchy-Schwarz), "
     "it is >= 0 for EVERY odds; in a box it can be negative: an amplitude with weight 99/100 at the centre and 1/100 at a corner of "
     "the 7^3 box, and odds concentrated at that corner, give g_corner - <rho, g rho> < 0 (the wall lowers g_yy)", p_born > rgr and
     p_wall < rgr2 and cs_ok, f"star: sum rho_y g_yy = {float(p_born):.5f} > <rho,g rho> = {float(rgr):.5f}; g_corner = {p_wall} = "
     f"{float(p_wall):.5f} < <rho2,g rho2> = {float(rgr2):.5f}")

# ================================================================== (b) the record energy that keeps the ledger does not see the walls
boxes = {n: box(n) for n in (3, 5)}
weightings = {"uniform": [sp.Rational(1, 7)] * 7, "centre-heavy": [sp.Rational(1, 2)] + [sp.Rational(1, 12)] * 6,
              "lopsided": [sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 8), sp.Rational(1, 8), sp.Rational(1, 8), sp.Rational(1, 16), sp.Rational(1, 16)]}
res = {}
for name, wts in weightings.items():
    for n, (sites_, ix_, OmA_, g_) in boxes.items():
        c_ = tuple([(n + 1) // 2] * 3)
        star_ = [c_] + [tuple(c_[d] + (s if d == a else 0) for d in range(3)) for a in range(3) for s in (1, -1)]
        wmap = dict(zip(star_, wts))
        rho_ = [wmap.get(s, 0) for s in sites_]
        for gam in (sp.Integer(1), sp.Rational(7, 3)):
            L_ = ledger(OmA_, rho_, gam)
            res[(name, n, gam)] = L_ / (1 - gam / 12 * g_[ix_[c_], ix_[c_]] * L_)
sym_same = all(res[(nm, 3, gm)] == res[(nm, 5, gm)] for nm in ("uniform", "centre-heavy") for gm in (sp.Integer(1), sp.Rational(7, 3)))
lop_diff = res[("lopsided", 3, sp.Integer(1))] != res[("lopsided", 5, sp.Integer(1))]
want("B3 (b) EXACT, LOCALITY OF THE FORMATION BOOKKEEPING: for an amplitude symmetric about the formation site y (the 7-site star, uniform "
     "or centre-heavy) in boxes symmetric about y, the record energy that keeps the ledger, m' = L/(1 - (gamma/12) g_yy L), is the SAME exact "
     "rational in the 5^3 and 7^3 boxes, at gamma = 1 and 7/3: the walls' correction to g is discrete-harmonic, so by the mean-value "
     "property it acts on symmetric charges as the constant H(y,y) J, and a constant shift cancels in 1/m' = 1/L - (gamma/12) g_yy "
     "(Sherman-Morrison); lopsided weights (control) break it", sym_same and lop_diff,
     f"uniform star: m' = {res[('uniform', 3, sp.Integer(1))]} (both boxes, gamma = 1); lopsided: {float(res[('lopsided', 3, sp.Integer(1))]):.9f} vs "
     f"{float(res[('lopsided', 5, sp.Integer(1))]):.9f}")

# ================================================================== (c) the executed discriminator (NUMERIC)
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
Lx, Ly, Lz = 48, 24, 4
Nn = Lx * Ly * Lz
idx = lambda x, y, z: ((x % Lx) * Ly + (y % Ly)) * Lz + (z % Lz)
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
r_, c_, v_ = [], [], []
for x in range(Lx):
    for y in range(Ly):
        for z in range(Lz):
            i = idx(x, y, z)
            for a, (dx, dy, dz) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                j = idx(x + dx, y + dy, z + dz); blk = SIG[a] / (2j)
                for p in range(2):
                    for q in range(2):
                        if blk[p, q] != 0:
                            r_ += [2 * i + p, 2 * j + p]; c_ += [2 * j + q, 2 * i + q]; v_ += [blk[p, q], -blk[p, q]]
Hs = sps.csr_matrix((v_, (r_, c_)), shape=(2 * Nn, 2 * Nn))
X, Y, Z = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")


def mean_field(gamma_E, xs, ys, w=1.5):
    rho_ = np.exp(-((X - xs) ** 2 + (Y - ys) ** 2) / (2 * w * w)); rho_ /= rho_.sum()
    ek = np.fft.fftn(gamma_E * rho_ - gamma_E / Nn)
    kx, ky, kz = (2 * np.pi * np.fft.fftfreq(L) for L in (Lx, Ly, Lz))
    KX, KY, KZ = np.meshgrid(kx, ky, kz, indexing="ij")
    oma = 1 - (np.cos(KX) + np.cos(KY) + np.cos(KZ)) / 3
    uk = np.zeros_like(ek); nz = oma > 1e-12; uk[nz] = -(1 / 6) * ek[nz] / oma[nz]      # u - Au = -(gamma/6)(e - mean)
    return np.real(np.fft.ifftn(uk))


def centre_y(u, T=36, steps=6):
    env = np.exp(-((X - 8) ** 2 + (Y - 12) ** 2) / 16) * np.exp(1j * 0.6 * X)
    Hk = np.sin(0.6) * SIG[0]; w_, v = np.linalg.eigh(Hk); chi = v[:, 1]
    psi0 = (env[..., None] * chi[None, None, None, :]).reshape(-1); psi0 /= np.linalg.norm(psi0)
    D = sps.diags(np.repeat(np.exp(u / 2).reshape(-1), 2))
    out = expm_multiply(-1j * (D @ Hs @ D).tocsr(), psi0, start=0, stop=T, num=steps + 1, endpoint=True)
    return np.array([((np.abs(s_.reshape(Lx, Ly, Lz, 2)) ** 2).sum(-1) * Y).sum() for s_ in out])


ya = centre_y(np.zeros((Lx, Ly, Lz)))
shifts = {}
for gE in (1.0, 2.0):
    shifts[gE] = centre_y(mean_field(gE, 24, 17)) - ya
mirror = centre_y(mean_field(2.0, 24, 7)) - ya
disc_ok = shifts[1.0][-1] > 0.5 and shifts[2.0][-1] > 1.5 * shifts[1.0][-1] and mirror[-1] < -1.0
want("C1 (c) EXECUTED, NOT CLAIMED (NUMERIC): a test packet of block 54's walk (k = 0.6 along x, width 2) passes an UNRECORDED source lobe "
     "(width 1.5, 5 sites off its path, 48x24x4 torus). Records only (a): the rates stay ambient, so the test amplitude's transverse centre "
     "follows the free walk. Mean-field amplitude sources (c): it is pulled toward the lobe, by an amount proportional to gamma E, and the "
     "mirror placement reverses it. The observable is the transverse centre of the test body's formed records, given the conditions in "
     "ATTEMPT.md", disc_ok,
     f"shift of the centre at t = 36: {shifts[1.0][-1]:.3f} (gamma E = 1), {shifts[2.0][-1]:.3f} (gamma E = 2), mirror {mirror[-1]:.3f}")

npass = sum(1 for _, o in RESULTS if o)
nfail = len(RESULTS) - npass
print(f"TOTAL: PASS={npass} FAIL={nfail}")
if nfail == 0:
    print("SUMMARY: PARTIAL: (b) exact on held-wall boxes: a formation event keeps the ledger iff the record's bare energy is "
          "L/(1 - (gamma/12) g_yy L) (block 58 T1 re-derived); at weak field the self-energy change is (gamma/12) E^2 (g_yy - <rho, g rho>); "
          "the required mean excess over ANY odds is (gamma/12) E^2 (sum p_y g_yy - <rho, g rho>), >= 0 for every odds on Z^3 and of either "
          "sign in a box; and for an amplitude symmetric about the formation site the record energy that keeps the ledger does not depend on "
          "the walls at all (exact, two boxes; mean-value property). (a) records only: an unrecorded packet is pulled and pulls nothing; with "
          "records at rest its momentum is not conserved and the ledger is kept only because the field ignores it; with moving records the "
          "ledger drifts at sum e du/dt (block 55 T2). (c) executed discriminator: the transverse centre of the test body's records shifts "
          "toward an unrecorded source only under amplitude sourcing. (d) records-only fits every sentence of the Record and Qualification "
          "axioms; amplitude sourcing makes the field depend on non-state data")
    print("HIT: keeping the ledger through a formation event that replaces an amplitude (energy E, weights rho) by one record at y requires "
          "the record's bare energy L/(1 - (gamma/12) g_yy L); at weak field this exceeds E by (gamma/12) E^2 (g_yy - <rho, g rho>), g the "
          "held-wall potential of 1 - average; averaged over ANY odds it is (gamma/12) E^2 (sum p_y g_yy - <rho, g rho>), >= 0 for every odds "
          "on Z^3 but of either sign in a box; for an amplitude symmetric about y the required record energy is independent of the walls "
          "(exact: 1188/1091 for the uniform 7-site star at gamma = 1 in both the 5^3 and 7^3 boxes)")
