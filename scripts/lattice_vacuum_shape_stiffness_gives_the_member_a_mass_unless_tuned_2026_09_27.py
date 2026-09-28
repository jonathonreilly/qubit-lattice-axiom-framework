#!/usr/bin/env python3
"""The lattice vacuum resists shear: a member coupled to lattice matter gets a mass unless tuned.

Question: a spatially constant, volume-preserving change of the metric (a
shear) is a relabelling of coordinates in the continuum, so a covariant
vacuum's energy cannot depend on it. On a fixed lattice the Brillouin zone is
fixed in coordinate momentum. Does the matter's vacuum energy then depend on
the shape of a constant metric? If it does, the member's constant
transverse-traceless (TT) modes feel a restoring force (a mass) or an
anti-restoring one (an instability) of the size of the lattice vacuum energy.

Supplied comparator coupling (not fixed by the axioms or by the campaign):
the walker's hop along axis j carries sigma_a e_a^j instead of sigma_j, with a
constant inverse vielbein e and inverse metric g^{ij} = (e e^T)^{ij}; a shear is
e = expm(eps/2), eps symmetric and traceless, so g^{-1} = expm(eps) and the
proper volume per cell is unchanged. The sea (lower band filled) has energy
per cell E(e) = -<|e^T s(k)|>_BZ, s(k) = (sin k_1, sin k_2, sin k_3).

Shape stiffness: E(expm(t eps/2)) = E_0 + (1/2) c t^2 + O(t^3) for unit eps
(tr eps^2 = 1). Cubic symmetry allows two values: c_E for the axis shears
(eps diagonal) and c_T for the face shears (eps off-diagonal).

Checks:
A. Covariant comparator: with a cutoff on the proper momentum, |e^T k| < pi,
   the sea energy is independent of shear (change of variables; checked on
   a direct k-grid).
B. Coordinate-fixed ball comparator: with the cutoff |k| < pi fixed in
   coordinate momentum (rotation-invariant but not covariant), the shape
   stiffness is isotropic and nonzero: c = 2 E_0/15 exactly.
C. The walker's sea on Z^3: c_E = -0.1779, c_T = -0.1467 per cell (lattice
   units), converged; both negative and unequal (cubic, not isotropic).
D. Real space: the vielbein-coupled walker on a periodic 8^3 lattice,
   diagonalised directly, has the k-space sea energy at every shape, and a
   sheared lattice's spectrum differs from the unsheared one, so no unitary
   relabelling of the matter maps one onto the other.
E. Only the shape matters: rotating the frame index (e -> e R) leaves the sea
   energy unchanged; turning an axis shear by 45 degrees into a face shear
   changes its cost from c_E/2 to c_T/2.
F. The hypercubic tick surface does not remove it: a free lattice scalar on
   Euclidean Z^4 has shape stiffnesses c_3 (diagonal) and c_6 (off-diagonal,
   including time-space shears), unequal and of order 0.1 per site,
   converged, for two metric couplings: the symmetric-difference form
   g^{mu nu} phat_mu phat_nu with phat = 2 sin(k/2), and the forward-difference
   form g^{mu nu} Re[(e^{i k_mu} - 1)(e^{-i k_nu} - 1)]. They move with the mass.
   (sin k is not used as a second dispersion: over the zone sin k and
   sin(k/2) take the same values with the same weights, so it would repeat
   the first test at a rescaled mass.)
G. Cancelling needs matched dispersions: a complex boson with the walker's
   own dispersion cancels the sea's shape energy at every shape; the
   standard forward-difference lattice scalar does not.
H. Size (arithmetic, observational bound as reference input): with block
   101's member, the constant TT mode has omega^2 = c wbar / (2 alpha); in
   GR's normalisation m^2 = 32 pi G c / a^4 (units hbar = c = 1). At the
   Planck spacing |m| is about 4 M_P; at a = 1e-19 m it is about 1e-3 eV,
   1e20 times the LIGO-Virgo-KAGRA bound 1.27e-23 eV. The stiffness must be
   tuned to about 1e-40 of its natural size at that spacing (1e-104 at the
   Planck spacing).

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import numpy as np
from scipy.linalg import expm

PASS = FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}", flush=True)


PAULI = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]
EPS_E = np.diag([1.0, -1.0, 0.0]) / np.sqrt(2)
EPS_T = np.zeros((3, 3)); EPS_T[0, 1] = EPS_T[1, 0] = 1 / np.sqrt(2)


def kgrid(N, d):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    return np.stack(np.meshgrid(*([k] * d), indexing='ij'), -1).reshape(-1, d)


def sea(e, S):
    return -np.mean(np.linalg.norm(S @ e, axis=1))


def stiffness(f, d=1e-3):
    return (f(d) - 2 * f(0.0) + f(-d)) / d ** 2


# ---------------------------------------------------------------- A covariant comparator
N = 200
kk = (np.arange(N) + 0.5) * (2 * 1.6 * np.pi / N) - 1.6 * np.pi
KB = np.stack(np.meshgrid(kk, kk, kk, indexing='ij'), -1).reshape(-1, 3); dv = (2 * 1.6 * np.pi / N) ** 3 / (2 * np.pi) ** 3


def e_cov(e):
    q = np.linalg.norm(KB @ e, axis=1)
    return -np.sum(q * (q < np.pi)) * dv


covs = [e_cov(expm(t * eps / 2)) for eps in (EPS_E, EPS_T) for t in (0.0, 0.3)]
exact = -np.pi ** 4 / (8 * np.pi ** 3) * 4 * np.pi / 4 / np.pi  # -(1/(2pi)^3) * 4 pi * pi^4/4
exact = -(4 * np.pi) * np.pi ** 4 / 4 / (2 * np.pi) ** 3
check("A: covariant comparator (cutoff on the proper momentum): the sea energy does not depend on the shear",
      max(abs(c - exact) for c in covs) < 2e-3 * abs(exact),
      f"energy at shear 0 and 0.3 (axis, face): {[round(c, 4) for c in covs]}; exact {exact:.4f}")

# ---------------------------------------------------------------- B coordinate-fixed ball
nth, nph = 400, 800
th = (np.arange(nth) + 0.5) * np.pi / nth; ph = (np.arange(nph) + 0.5) * 2 * np.pi / nph
TH, PH = np.meshgrid(th, ph, indexing='ij')
U = np.stack([np.sin(TH) * np.cos(PH), np.sin(TH) * np.sin(PH), np.cos(TH)], -1).reshape(-1, 3)
W = (np.sin(TH).reshape(-1)) * (np.pi / nth) * (2 * np.pi / nph)
radial = np.pi ** 4 / 4 / (2 * np.pi) ** 3


def e_ball(e):
    return -radial * np.sum(W * np.linalg.norm(U @ e, axis=1))


E0b = e_ball(np.eye(3))
cb = [stiffness(lambda t, eps=eps: e_ball(expm(t * eps / 2))) for eps in (EPS_E, EPS_T)]
check("B: coordinate-fixed ball (rotation-invariant, not covariant): the stiffness is isotropic and equals 2 E_0 / 15",
      all(abs(c - 2 * E0b / 15) < 1e-4 * abs(E0b) for c in cb),
      f"E_0 = {E0b:.5f}; c_E, c_T = {cb[0]:.5f}, {cb[1]:.5f}; 2 E_0/15 = {2 * E0b / 15:.5f}")

# ---------------------------------------------------------------- C the walker's sea on Z^3
res = {}
for n in (64, 128):
    S = np.sin(kgrid(n, 3))
    res[n] = (sea(np.eye(3), S), [stiffness(lambda t, eps=eps: sea(expm(t * eps / 2), S)) for eps in (EPS_E, EPS_T)])
E0, (cE, cT) = res[128]
conv = max(abs(a - b) for a, b in zip(res[64][1], res[128][1]))
check("C: the walker's sea on Z^3 resists shear with two unequal, negative stiffnesses (the flat shape is a maximum of its energy)",
      cE < -0.1 and cT < -0.1 and abs(cE / cT - 1) > 0.1 and conv < 1e-4,
      f"E_0 = {E0:.5f}; c_E = {cE:.5f}, c_T = {cT:.5f} per cell; ratio {cE / cT:.3f}; grid change 64->128: {conv:.1e}")

# ---------------------------------------------------------------- D real space
L = 8


def real_space_sea(e):
    n = L ** 3; H = np.zeros((2 * n, 2 * n), complex)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                i = (x * L + y) * L + z
                for j, (dx, dy, dz) in enumerate(((1, 0, 0), (0, 1, 0), (0, 0, 1))):
                    k = (((x + dx) % L) * L + (y + dy) % L) * L + (z + dz) % L
                    A = sum(PAULI[a] * e[j, a] for a in range(3)) / (2j)
                    H[2 * i:2 * i + 2, 2 * k:2 * k + 2] += A; H[2 * k:2 * k + 2, 2 * i:2 * i + 2] += A.conj().T
    w = np.linalg.eigvalsh(H)
    return np.sum(w[w < 0]) / n, w


kp = 2 * np.pi * np.arange(L) / L
SP = np.sin(np.stack(np.meshgrid(kp, kp, kp, indexing='ij'), -1).reshape(-1, 3))
shapes = [np.eye(3), expm(0.4 * EPS_E / 2), expm(0.4 * EPS_T / 2)]
rs = [real_space_sea(e) for e in shapes]
ks = [sea(e, SP) for e in shapes]
spec_diff = min(np.max(np.abs(np.sort(rs[0][1]) - np.sort(r[1]))) for r in rs[1:])
check("D: real space (periodic 8^3): the direct sea energy equals the k-space formula at every shape, and shearing changes the spectrum",
      max(abs(r[0] - k) for r, k in zip(rs, ks)) < 1e-12 and spec_diff > 1e-3 and abs(rs[1][0] - rs[0][0]) > 1e-3,
      f"sea per site (flat, axis, face): {[round(r[0], 6) for r in rs]}; k-space: {[round(k, 6) for k in ks]}; "
      f"smallest largest-eigenvalue shift {spec_diff:.3f}")

# ---------------------------------------------------------------- E only the shape matters
S = np.sin(kgrid(96, 3)); rng = np.random.default_rng(3)
Q, _ = np.linalg.qr(rng.normal(size=(3, 3))); Q *= np.sign(np.linalg.det(Q))
e1 = expm(0.3 * (EPS_E + 0.5 * EPS_T) / 2)
Rz = np.array([[np.cos(np.pi / 4), -np.sin(np.pi / 4), 0], [np.sin(np.pi / 4), np.cos(np.pi / 4), 0], [0, 0, 1]])
t = 0.02
axis_cost = sea(expm(t * EPS_E / 2), S) - sea(np.eye(3), S)
turned = Rz @ EPS_E @ Rz.T
face_cost = sea(expm(t * turned / 2), S) - sea(np.eye(3), S)
check("E: rotating the frame index changes nothing; turning an axis shear by 45 degrees (into a face shear) changes its cost",
      abs(sea(e1 @ Q, S) - sea(e1, S)) < 1e-13 and np.allclose(np.abs(turned), np.abs(EPS_T), atol=1e-12)
      and abs(axis_cost / (0.5 * cE * t ** 2) - 1) < 0.02 and abs(face_cost / (0.5 * cT * t ** 2) - 1) < 0.02,
      f"frame-rotation change {abs(sea(e1 @ Q, S) - sea(e1, S)):.1e}; cost of shear 0.02 along axes {axis_cost:.3e}, "
      f"turned 45 degrees {face_cost:.3e}")

# ---------------------------------------------------------------- F the hypercubic tick surface
E3 = np.zeros((4, 4)); E3[0, 0], E3[1, 1] = 1 / np.sqrt(2), -1 / np.sqrt(2)
E6 = np.zeros((4, 4)); E6[0, 1] = E6[1, 0] = 1 / np.sqrt(2)


def free_energy(ginv, P, m2):
    return 0.5 * np.mean(np.log(np.einsum('ni,ij,nj->n', P, ginv, P) + m2))


def forward_symbol(K):  # Re[(e^{ik_i}-1)(e^{-ik_j}-1)] for all i, j
    d = K.shape[1]
    return np.stack([np.stack([np.cos(K[:, i] - K[:, j]) - np.cos(K[:, i]) - np.cos(K[:, j]) + 1 for j in range(d)], -1)
                     for i in range(d)], -2)


def free_energy_fwd(ginv, C, m2):
    return 0.5 * np.mean(np.log(np.einsum('nij,ij->n', C, ginv) + m2))


rows = {}
for n in (24, 36):
    K4 = kgrid(n, 4); P = 2 * np.sin(K4 / 2); C4 = forward_symbol(K4)
    for m2 in (0.5, 0.1):
        rows[(n, 'symmetric', m2)] = [stiffness(lambda t, eps=eps: free_energy(expm(t * eps), P, m2), d=2e-3) for eps in (E3, E6)]
        rows[(n, 'forward', m2)] = [stiffness(lambda t, eps=eps: free_energy_fwd(expm(t * eps), C4, m2), d=2e-3) for eps in (E3, E6)]
conv4 = max(abs(a - b) for key in rows if key[0] == 36 for a, b in zip(rows[key], rows[(24,) + key[1:]]))
vals = {key[1:]: [round(v, 4) for v in rows[key]] for key in rows if key[0] == 36}
check("F: the hypercubic tick surface (Euclidean Z^4 free scalar) also resists shear, time-space shears included; two unequal stiffnesses that move with the mass",
      all(v[0] > 0.05 and v[1] > 0.05 and abs(v[0] / v[1] - 1) > 0.05 for v in rows.values()) and conv4 < 1e-5
      and abs(rows[(36, 'symmetric', 0.1)][0] - rows[(36, 'symmetric', 0.5)][0]) > 1e-3,
      f"(c_3, c_6) per site: {vals}; grid change 24->36: {conv4:.1e}")

# ---------------------------------------------------------------- G cancelling needs matched dispersions
S3 = np.sin(kgrid(64, 3)); K3 = kgrid(64, 3)


def boson(e, P):  # complex scalar zero-point energy per cell: 2 x (1/2) <omega>, omega = |e^T P|
    return np.mean(np.linalg.norm(P @ e, axis=1))


C3 = forward_symbol(K3)


def boson_fwd(e):  # complex forward-difference scalar: omega^2 = g^{ij} Re[(e^{ik_i}-1)(e^{-ik_j}-1)], g^{-1} = e e^T
    return np.mean(np.sqrt(np.maximum(np.einsum('nij,ij->n', C3, e @ e.T), 0)))


es = [np.eye(3), expm(0.3 * EPS_E / 2), expm(0.3 * EPS_T / 2), expm(0.2 * (EPS_E - EPS_T) / 2)]
matched = [sea(e, S3) + boson(e, S3) for e in es]
std = [stiffness(lambda t, eps=eps: sea(expm(t * eps / 2), S3) + boson_fwd(expm(t * eps / 2))) for eps in (EPS_E, EPS_T)]
check("G: a boson with the walker's own dispersion cancels the sea's shape energy at every shape; the standard forward-difference scalar does not",
      max(abs(m) for m in matched) < 1e-13 and min(abs(s) for s in std) > 0.02,
      f"matched total at four shapes: {max(abs(m) for m in matched):.1e}; walker + forward-difference complex scalar stiffnesses {[round(s, 4) for s in std]}")

# ---------------------------------------------------------------- H size
hbar_c = 1.973269804e-7  # eV m
l_P = 1.616255e-35       # m
M_P = hbar_c / l_P       # eV (non-reduced Planck mass)
m_bound = 1.27e-23       # eV, LIGO-Virgo-KAGRA GWTC-3 (reference input)
c = abs(cT)              # the smaller of the walker's two stiffnesses


def mass(a):  # eV: m = sqrt(32 pi c) l_P / a^2, times hbar c
    return np.sqrt(32 * np.pi * c) * l_P / a ** 2 * hbar_c


m_planck, m_lhc = mass(l_P), mass(1e-19)
tune_lhc = (m_bound / m_lhc) ** 2; tune_planck = (m_bound / m_planck) ** 2
check("H: size: an untuned stiffness gives the member's constant TT modes a Planck-size mass (or growth rate) at the Planck spacing, "
      "and still far above the gravitational-wave bound at the largest spacing colliders allow",
      3 < m_planck / M_P < 5 and m_lhc / m_bound > 1e19,
      f"|m| = {m_planck / M_P:.2f} M_P at a = l_P; {m_lhc:.2e} eV at a = 1e-19 m ({m_lhc / m_bound:.1e} x the bound); "
      f"required tuning of c: {tune_lhc:.0e} (a = 1e-19 m), {tune_planck:.0e} (a = l_P)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
