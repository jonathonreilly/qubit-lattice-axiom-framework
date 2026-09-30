#!/usr/bin/env python3
"""The walker's sea feels the shape of a constant metric under the natural coupling.

Question: a spatially constant, volume-preserving change of the metric (a
shear) is a relabelling of coordinates in the continuum, so a covariant
vacuum's energy cannot depend on it. On a fixed lattice the Brillouin zone is
fixed in coordinate momentum. Does the matter's vacuum energy then depend on
the shape of a constant metric? If it does, and the dependence is the
long-wavelength limit of the static kernel, the member's transverse-traceless
(TT) modes get a zero-wavelength term of the size of the lattice vacuum
energy: a mass for one sign, a growth rate for the other.

Supplied comparator coupling (not fixed by the axioms or by the campaign):
the walker's hop along axis j carries sigma_a e_a^j instead of sigma_j, with a
constant inverse vielbein e and inverse metric g^{ij} = (e e^T)^{ij}; a shear is
e = expm(eps/2), eps symmetric and traceless, so g^{-1} = expm(eps) and the
proper volume per cell is unchanged. The sea (lower band filled) has energy
per cell E(e) = -<|e^T s(k)|>_BZ, s(k) = (sin k_1, sin k_2, sin k_3).

Shape coefficient: E(expm(t eps/2)) = E_0 + (1/2) c t^2 + O(t^3) for unit eps
(tr eps^2 = 1). Cubic symmetry allows two values: c_E for the axis shears
(eps diagonal) and c_T for the face shears (eps off-diagonal). c > 0 means
the flat shape is a minimum, c < 0 a maximum.

Checks:
A. Covariant comparator: with a cutoff on the proper momentum, |e^T k| < pi,
   the sea energy is independent of shear (change of variables; checked on
   a direct k-grid).
B. Coordinate-fixed ball comparator: with the cutoff |k| < pi fixed in
   coordinate momentum (rotation-invariant but not covariant), the shape
   stiffness is isotropic and nonzero: c = 2 E_0/15 exactly.
C. The walker's sea on Z^3: c_E = -0.1779, c_T = -0.1467 per cell (lattice
   units), converged; both negative (the flat shape is a maximum) and unequal
   (cubic, not isotropic). Under a face shear the natural coupling gives the
   doublers with cos K_1 cos K_2 = -1 the mirrored metric; a taste-universal
   local coupling (adding the range-2 hops cos k_a sin k_j cos k_j, j != a)
   gives all 8 nodes one metric and c_T = -0.1088 (c_E unchanged).
D. Real space: the vielbein-coupled walker on a periodic 8^3 lattice,
   diagonalised directly, has the k-space sea energy at every shape, and a
   sheared lattice's spectrum differs from the unsheared one, so no unitary
   relabelling of the matter maps one onto the other.
E. Only the shape matters: rotating the frame index (e -> e R) leaves the sea
   energy unchanged; with the taste-universal coupling, turning an axis shear
   by 45 degrees into a face shear changes its cost from c_E/2 to c_T/2.
F. The hypercubic tick surface (Euclidean) does not remove it: a free lattice
   scalar on Euclidean Z^4 has shape coefficients c_3 (diagonal) and c_6
   (off-diagonal, including Euclidean time-space shears), unequal and of order
   0.1 per site, converged, for two site-local metric couplings: the
   forward-difference form C_{mu nu} = Re[(e^{i k_mu} - 1)(e^{-i k_nu} - 1)], and
   a mixed form with forward differences on the diagonal and central
   differences off it (C_{mu mu} = 4 sin^2(k_mu/2), C_{mu nu} = sin k_mu sin k_nu).
   They move with the mass. (The symbol 4 sin(k_mu/2) sin(k_nu/2) is not used:
   it is not periodic, so it is not a site-local coupling.)
G. Cancelling needs matched dispersions: a complex boson with the walker's
   own dispersion cancels the sea's shape energy at every shape. One REAL
   forward-difference scalar (one degree of freedom) cancels the sea's
   energy and axis coefficient exactly at q = 0 (sin k and sin(k/2) take the
   same values with the same weights) and leaves a face coefficient +0.060
   with the taste-universal walker coupling (+0.022 with the natural one).
O. The signs are general: for a fermion sea -<|e^T v(k)|> with any real
   symbol v, the energy is concave along every volume-keeping shear path
   (Cauchy-Schwarz), so c <= 0; for a boson (1/2)<log(tr(g C) + m^2)> with C
   positive semidefinite it is convex, so c >= 0; checked on random symbols.
   The fermion sea's energy is unbounded below along such paths.
P. Dressing: the sea's zero-wavelength response depends on frequency as
   chi(omega) = chi0 + omega^2 chi2 + ..., which adds chi2/4 to the member's
   inertia (0.0069 axis, 0.0016 face; finite, converged). At the Planck
   spacing the q = 0 growth rate is solved exactly on the imaginary frequency
   axis from the one-loop (exact, free) kernel: 3.57/a (axis), 3.20/a (face).
Q. The exactly conserved crystal momentum is not a sum of local densities:
   its symbol k is a sawtooth on the zone, whose real-space kernel decays
   only as 1/r; a local shift coupling cannot use it.
I. A designed coupling removes it for free matter: relabel the zone by the
   time-1 flow phi of a divergence-free trigonometric vector field that fixes
   the 8 nodes (v = curl(A e_3), A = (lam/4) sin 2k_1 sin 2k_2 for an axis
   shear, A = -(lam/4) cos k_1 cos 3k_2 for a face shear) and use the symbol
   sigma . s(phi(k)). The flow keeps volume, so the sea energy is exactly
   unchanged; every node sees one common sheared metric (J^T J compared
   directly); the hoppings decay exponentially with range. The face flow is
   v = (lam/2)(sin 2k_2, sin 2k_1, 0), whose Jacobian is the same symmetric
   face shear at every node.
J. Interactions bring it back: with the designed coupling, the first-order
   energy of a nearest-neighbour density interaction V sum n_x n_{x+e_j}
   (its exchange part) depends on the shear (axis and face; values printed). The on-site density matrix is
   unchanged, so on-site interactions stay blind at first order.
K. Why: a relabelling that kept every momentum-conserving two-body vertex
   momentum-conserving would satisfy phi(a) + phi(b) = phi(a+b) + phi(0), so
   phi - phi(0) would be a continuous homomorphism of the torus, an integer
   matrix; no small shear is one. The designed phi violates momentum addition
   at order lam.
L. The zero-wavelength coefficient is the long-wavelength limit of the static
   kernel: for a static modulation cos(q x) of the vielbein along a cube axis,
   the TT coefficients (h_yy - h_zz and h_yz for q along x) computed from the
   second-order energy c(q) = -tau/4 - chi(q)/2 (per mean-square cosine
   amplitude; vielbein at the hop's midpoint) go smoothly (at order q^2) to
   c_E and to the taste-universal c_T; for q along an axis these two
   polarisations are in their own irreps of the little group, so they do not
   mix with lapse, shift or trace. Read as the whole static TT kernel of a
   member induced from this sea, c(q) = c0 + kappa q^2 has range
   sqrt(kappa/|c0|) of 0.23 (axis) and 0.15 (face) lattice spacings.
M. The clock is protected; a shift coupled to the hopping current is not
   (continuous time; a spin-1/2
   chain of 12 sites at zero magnetisation as a comparator for interacting
   lattice matter): a constant lapse multiplies H, so the vacuum energy is
   exactly linear in it (zero curvature, any matter); a constant shift
   couples to a momentum operator, here the hopping current, whose vacuum
   curvature is zero for free matter and nonzero with interactions; and a
   search over all translation-invariant, magnetisation-conserving local
   charges of range <= 3 finds a conserved parity-odd charge (a candidate
   local momentum density) for the free chain and for the integrable XXZ
   chain (its energy current), but none once a next-nearest-neighbour
   interaction breaks integrability. (The exactly conserved crystal momentum
   is not local: check Q.)
N. Matching must be exact: a complex boson with the walker's dispersion but a
   mass M leaves c_E = -0.044 (M a)^2 (M below about 0.2 per lattice unit),
   so a boson-fermion splitting M gives the member a mass of about
   2 M l_P / a; a TeV splitting would need a lattice coarser than a metre to
   pass the gravitational-wave bound.
R. Dressed second order (2D walker sigma_x sin k_x + sigma_y sin k_y, designed
   face coupling): rescale a nearest-neighbour density interaction as
   V (1 + beta t^2) with beta chosen so its first-order shape dependence
   cancels; the second-order (Moller-Plesset) energy is still
   shape-dependent, about +0.0025 V^2 per unit shear (24^2, 32^2 within
   10 %). An on-site interaction, blind at first order, gives about
   +9e-5 U^2 at second order.
H. Size (arithmetic, observational bound as reference input): with block
   101's member, the constant TT mode has omega^2 = c wbar / (2 alpha); in
   GR's normalisation m^2 = 32 pi G c / a^4 (units hbar = c = 1), with the
   added bridge that a hop costs hbar c / a. With |c| = 0.109 (the smaller
   taste-universal coefficient), |m| is about 3.3 M_P at the Planck spacing
   and about 1e-3 eV at an illustrative a = 1e-19 m, 8e19 times the
   LIGO-Virgo-KAGRA dispersion bound 1.27e-23 eV; the coefficient would have
   to be about 1e-40 of its natural size there (1e-103 at the Planck
   spacing). A negative c means growth, not oscillation; for growth the
   yardstick is the Hubble rate (1.5e-33 eV), giving about 1e-60 at 1e-19 m
   and 1e-123 at the Planck spacing.

Prints one line per check and `TOTAL: PASS=N FAIL=M`. Runtime about 2 minutes.
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


AUDIT_TIMEOUT_SEC = 900

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


def u_symbols(K):  # taste-universal coupling: u[n, j, a], u_aa = sin k_a, u_ja = cos k_a sin k_j cos k_j (j != a)
    s_, c_ = np.sin(K), np.cos(K); u = np.zeros((K.shape[0], 3, 3))
    for j in range(3):
        for a in range(3):
            u[:, j, a] = s_[:, a] if j == a else c_[:, a] * s_[:, j] * c_[:, j]
    return u


def sea_u(e, u):
    return -np.mean(np.linalg.norm(np.einsum('nja,ja->na', u, e), axis=1))


U128 = u_symbols(kgrid(128, 3))
cTu = stiffness(lambda t: sea_u(expm(t * EPS_T / 2), U128)); cEu = stiffness(lambda t: sea_u(expm(t * EPS_E / 2), U128))


def node_metric(fun, K0, d=1e-6):
    J = np.zeros((3, 3))
    for j in range(3):
        ej = np.zeros(3); ej[j] = d; J[:, j] = (fun(K0 + ej) - fun(K0 - ej)) / (2 * d)
    return J.T @ J


NODES8 = [np.array(n, float) for n in __import__('itertools').product((0, np.pi), repeat=3)]
e_face = expm(0.2 * EPS_T / 2)
nat_off = [node_metric(lambda k: np.sin(k)[None] @ e_face, K0)[0, 1] if False else node_metric(lambda k: (np.sin(k)[None] @ e_face)[0], K0)[0, 1] for K0 in NODES8]
uni_off = [node_metric(lambda k: np.einsum('nja,ja->na', u_symbols(k[None]), e_face)[0], K0)[0, 1] for K0 in NODES8]
check("C: the walker's sea on Z^3 feels shear: unequal, negative shape coefficients (the flat shape is a maximum); the natural coupling mirrors a face shear "
      "at half the nodes, a taste-universal local coupling does not",
      cE < -0.1 and cT < -0.1 and abs(cE / cT - 1) > 0.1 and conv < 1e-4 and abs(cEu - cE) < 1e-9 and cTu < -0.05
      and min(nat_off) < -0.1 < 0.1 < max(nat_off) and min(uni_off) > 0.1 and max(uni_off) - min(uni_off) < 1e-6,
      f"E_0 = {E0:.5f}; natural c_E = {cE:.5f}, c_T = {cT:.5f}; taste-universal c_E = {cEu:.5f}, c_T = {cTu:.5f} per cell; grid change 64->128: {conv:.1e}; "
      f"face-shear node metric (0,1) entries, natural {sorted(set(round(x, 4) for x in nat_off))}, universal {sorted(set(round(x, 4) for x in uni_off))}")

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
S = np.sin(kgrid(96, 3)); U96 = u_symbols(kgrid(96, 3)); rng = np.random.default_rng(3)
Q, _ = np.linalg.qr(rng.normal(size=(3, 3))); Q *= np.sign(np.linalg.det(Q))
e1 = expm(0.3 * (EPS_E + 0.5 * EPS_T) / 2)
Rz = np.array([[np.cos(np.pi / 4), -np.sin(np.pi / 4), 0], [np.sin(np.pi / 4), np.cos(np.pi / 4), 0], [0, 0, 1]])
t = 0.02
axis_cost = sea_u(expm(t * EPS_E / 2), U96) - sea_u(np.eye(3), U96)
turned = Rz @ EPS_E @ Rz.T
face_cost = sea_u(expm(t * turned / 2), U96) - sea_u(np.eye(3), U96)
check("E: rotating the frame index changes nothing; turning an axis shear by 45 degrees (into a face shear) changes its cost",
      abs(sea(e1 @ Q, S) - sea(e1, S)) < 1e-13 and np.allclose(np.abs(turned), np.abs(EPS_T), atol=1e-12)
      and abs(axis_cost / (0.5 * cE * t ** 2) - 1) < 0.02 and abs(face_cost / (0.5 * cTu * t ** 2) - 1) < 0.02,
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


def mixed_symbol(K):  # forward differences on the diagonal, central differences off it
    d = K.shape[1]; S_ = np.sin(K)
    C = np.einsum('ni,nj->nij', S_, S_)
    for i in range(d):
        C[:, i, i] = 4 * np.sin(K[:, i] / 2) ** 2
    return C


rows = {}
for n in (24, 36):
    K4 = kgrid(n, 4); C4 = forward_symbol(K4); M4 = mixed_symbol(K4)
    for m2 in (0.5, 0.1):
        rows[(n, 'forward', m2)] = [stiffness(lambda t, eps=eps: free_energy_fwd(expm(t * eps), C4, m2), d=2e-3) for eps in (E3, E6)]
        rows[(n, 'mixed', m2)] = [stiffness(lambda t, eps=eps: free_energy_fwd(expm(t * eps), M4, m2), d=2e-3) for eps in (E3, E6)]
conv4 = max(abs(a - b) for key in rows if key[0] == 36 for a, b in zip(rows[key], rows[(24,) + key[1:]]))
vals = {key[1:]: [round(v, 4) for v in rows[key]] for key in rows if key[0] == 36}
check("F: on the hypercubic tick surface (Euclidean Z^4 free scalar, two site-local couplings) the free energy also depends on shape, time-space shears included; two unequal coefficients that move with the mass",
      all(v[0] > 0.05 and v[1] > 0.05 and abs(v[0] / v[1] - 1) > 0.05 for v in rows.values()) and conv4 < 1e-5
      and abs(rows[(36, 'forward', 0.1)][0] - rows[(36, 'forward', 0.5)][0]) > 1e-3,
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
U64 = u_symbols(K3)
real_fwd = [stiffness(lambda t, eps=eps: sea(expm(t * eps / 2), S3) + 0.5 * boson_fwd(expm(t * eps / 2))) for eps in (EPS_E, EPS_T)]
real_fwd_u = stiffness(lambda t: sea_u(expm(t * EPS_T / 2), U64) + 0.5 * boson_fwd(expm(t * EPS_T / 2)))
e0_real = sea(np.eye(3), S3) + 0.5 * boson_fwd(np.eye(3))
check("G: a boson with the walker's own dispersion cancels the sea's shape energy at every shape; one real forward-difference scalar cancels the energy and "
      "the axis coefficient exactly and leaves a face coefficient",
      max(abs(m) for m in matched) < 1e-13 and abs(e0_real) < 1e-6 and abs(real_fwd[0]) < 1e-5 and real_fwd_u > 0.05,
      f"matched total at four shapes: {max(abs(m) for m in matched):.1e}; walker + one real forward scalar: energy {e0_real:.1e}, "
      f"axis {real_fwd[0]:.1e}, face {real_fwd_u:+.4f} (taste-universal walker; {real_fwd[1]:+.4f} with the natural one); walker + complex forward scalar (two degrees of freedom): {[round(s, 4) for s in std]}")

# ---------------------------------------------------------------- I designed coupling (free matter)
def v_axis(K, lam):  # curl(A e_3), A = (lam/4) sin 2k_1 sin 2k_2
    k1, k2 = K[:, 0], K[:, 1]
    return np.stack([lam / 2 * np.sin(2 * k1) * np.cos(2 * k2), -lam / 2 * np.cos(2 * k1) * np.sin(2 * k2), 0 * k1], -1)


def v_face(K, lam):  # curl(A e_3), A = (lam/2)(sin^2 k_2 - sin^2 k_1): v = (lam/2)(sin 2k_2, sin 2k_1, 0)
    return np.stack([lam / 2 * np.sin(2 * K[:, 1]), lam / 2 * np.sin(2 * K[:, 0]), 0 * K[:, 0]], -1)


def flow(K, vf, lam, steps=100):
    h = 1.0 / steps; X = K.copy()
    for _ in range(steps):
        a = vf(X, lam); b = vf(X + h / 2 * a, lam); c_ = vf(X + h / 2 * b, lam); d_ = vf(X + h * c_, lam)
        X = X + h / 6 * (a + 2 * b + 2 * c_ + d_)
    return X


from scipy.linalg import polar
lam = 0.1
K96 = kgrid(96, 3); E096 = sea(np.eye(3), np.sin(K96))
NODES = [np.array(n, float) for n in __import__('itertools').product((0, np.pi), repeat=3)]
designed = {}
for name, vf in (('axis', v_axis), ('face', v_face)):
    dE = -np.mean(np.linalg.norm(np.sin(flow(K96, vf, lam)), axis=1)) - E096
    metrics = [node_metric(lambda k, vf=vf: np.sin(flow(k[None], vf, lam))[0], K0) for K0 in NODES]
    spread = max(np.max(np.abs(m - metrics[0])) for m in metrics)
    Ng = 48; kg = 2 * np.pi * np.arange(Ng) / Ng
    Kg = np.stack(np.meshgrid(kg, kg, kg, indexing='ij'), -1).reshape(-1, 3)
    F = np.abs(np.fft.fftn(np.sin(flow(Kg, vf, lam)).reshape(Ng, Ng, Ng, 3), axes=(0, 1, 2))) / Ng ** 3
    rr = np.minimum(np.arange(Ng), Ng - np.arange(Ng)); Rng = np.maximum.reduce(np.meshgrid(rr, rr, rr, indexing='ij'))
    designed[name] = (dE, spread, metrics[0], F[Rng == 10].max(), F[Rng == 20].max())
vb = sea(expm(lam * np.diag([1.0, -1.0, 0.0])), np.sin(K96)) - E096
check("I: a designed coupling (a volume-keeping relabelling of the zone, linear at the nodes) makes the free sea exactly blind to shear; "
      "every node sees one sheared metric; hoppings decay exponentially",
      all(abs(d[0]) < 1e-7 and d[1] < 1e-8 and d[4] < 1e-12 for d in designed.values()) and abs(vb) > 5e-3
      and abs(designed['axis'][2][0, 0] - np.exp(2 * lam)) < 1e-7 and abs(designed['face'][2][0, 1] - np.sinh(2 * lam)) < 1e-6,
      "; ".join(f"{n}: energy change {d[0]:.1e}, node-metric spread {d[1]:.1e}, largest hop at range 10 / 20: {d[3]:.0e} / {d[4]:.0e}"
                for n, d in designed.items()) + f"; natural coupling at the same axis metric: {vb:.2e}")

# ---------------------------------------------------------------- J interactions bring it back
PA = np.array(PAULI)


def exchange(svec, K):  # first-order exchange energy per site of V sum_{x,j} n_x n_{x+e_j}, V = 1; and the on-site density matrix
    sh = svec / np.linalg.norm(svec, axis=1)[:, None]
    P = 0.5 * (np.eye(2)[None] - np.einsum('na,aij->nij', sh, PA))
    G = [np.mean(P * np.exp(1j * K[:, j])[:, None, None], axis=0) for j in range(3)]
    return -sum(np.real(np.trace(g @ g.conj().T)) for g in G), np.mean(P, axis=0)


cJ = {}
for name, vf in (('axis', v_axis), ('face', v_face)):
    f = lambda l: exchange(np.sin(flow(K96, vf, l) if l else K96), K96)[0]
    cJ[name] = stiffness(f, d=0.05) / 8  # unit shear t = 2 sqrt 2 lam
G0flat = exchange(np.sin(K96), K96)[1]
G0sh = exchange(np.sin(flow(K96, v_face, lam)), K96)[1]
check("J: with the designed coupling, a nearest-neighbour density interaction's first-order energy depends on shear again; on-site interactions stay blind at first order",
      cJ['axis'] > 1e-3 and cJ['face'] > 1e-3 and np.max(np.abs(G0flat - G0sh)) < 1e-12,
      f"stiffness per unit shear, in units of V: axis {cJ['axis']:.4f}, face {cJ['face']:.4f}; on-site density-matrix change {np.max(np.abs(G0flat - G0sh)):.1e}")

# ---------------------------------------------------------------- K momentum addition
rngK = np.random.default_rng(5); A_ = rngK.uniform(-np.pi, np.pi, (2000, 3)); B_ = rngK.uniform(-np.pi, np.pi, (2000, 3))
wrap = lambda x: (x + np.pi) % (2 * np.pi) - np.pi
viol = np.max(np.abs(wrap(flow(A_, v_axis, lam) + flow(B_, v_axis, lam) - flow(wrap(A_ + B_), v_axis, lam) - flow(np.zeros((1, 3)), v_axis, lam))))
check("K: the designed relabelling does not respect momentum addition (it cannot: a map that did would be an integer matrix), so it cannot carry a momentum-conserving interaction along",
      viol > 0.5 * lam, f"largest |phi(a) + phi(b) - phi(a+b) - phi(0)| over 2000 random pairs at lam = {lam}: {viol:.3f}")

# ---------------------------------------------------------------- L long-wavelength limit
def bands(K):
    w, v = np.linalg.eigh(np.einsum('nj,jab->nab', np.sin(K), PA)); return w, v


def link_symbol(eps, K, qv, universal):  # vielbein at each hop's midpoint: the k -> k+q element is M(k + q/2)
    Km = K + qv / 2
    u = u_symbols(Km) if universal else None
    M = 0
    for j in range(3):
        for a in range(3):
            if eps[j, a] != 0:
                f = u[:, j, a] if universal else np.sin(Km[:, j])
                M = M + eps[j, a] * f[:, None, None] * PA[a][None]
    return M


def chi(eps, qv, K, universal=False):  # second-order energy lowering per unit <delta e^2> (interband, lower band k -> upper band k+q)
    w0, v0 = bands(K); out = []
    for sgn in ((1, -1) if np.any(qv) else (1,)):
        w1, v1 = bands(K + sgn * qv)
        me = np.einsum('na,nab,nb->n', v1[:, :, 1].conj(), link_symbol(eps, K, sgn * qv, universal), v0[:, :, 0])
        out.append(np.mean(np.abs(me) ** 2 / (w1[:, 1] - w0[:, 0])))
    return float(np.mean(out))


KL = kgrid(96, 3); tau = float(np.mean(np.sin(KL[:, 0]) ** 2 / np.linalg.norm(np.sin(KL), axis=1)))
EPS_Ex = np.diag([0.0, 1.0, -1.0]) / np.sqrt(2); EPS_Tx = np.zeros((3, 3)); EPS_Tx[1, 2] = EPS_Tx[2, 1] = 1 / np.sqrt(2)
cq = {}
for name, eps, uni in (('yy-zz', EPS_Ex, False), ('yz (taste-universal)', EPS_Tx, True)):
    cq[name] = [-tau / 4 - chi(eps, np.array([2 * np.pi * m / 96, 0, 0]), KL, uni) / 2 for m in (0, 1, 2, 4)]
fitrange = {}
for name, v in cq.items():
    qs_ = np.array([2 * np.pi * m / 96 for m in (0, 1, 2, 4)])
    A_ = np.stack([np.ones(4), qs_ ** 2, qs_ ** 4], 1); c0_, kap_, _ = np.linalg.lstsq(A_, np.array(v), rcond=None)[0]
    fitrange[name] = (kap_, np.sqrt(abs(kap_ / c0_)))
check("L: the zero-wavelength coefficient is the long-wavelength limit of the static kernel: for q along x the two TT polarisations' "
      "coefficients go smoothly to c_E and the taste-universal c_T (differences shrink like q^2)",
      abs(cq['yy-zz'][0] - cE) < 1e-4 and abs(cq['yz (taste-universal)'][0] - cTu) < 1e-4
      and all(abs(v[1] - v[0]) < 1e-4 and abs(v[3] - v[0]) / abs(v[2] - v[0]) > 3 for v in cq.values()),
      "; ".join(f"{n}: c(q) at q = 0, 0.065, 0.131, 0.262: {[round(x, 5) for x in v]}" for n, v in cq.items())
      + "; as an induced static kernel c0 + kappa q^2: " + ", ".join(f"{n}: kappa {k_:.4f}, range {r_:.3f} spacings" for n, (k_, r_) in fitrange.items()))

# ---------------------------------------------------------------- M clock protected, shift not
import itertools as _it
import scipy.sparse as sps
import scipy.sparse.linalg as spla
Lc = 12
I2s = sps.identity(2, format='csr'); Zs = sps.csr_matrix([[1, 0], [0, -1]]); Sps = sps.csr_matrix([[0, 1], [0, 0]]); Sms = sps.csr_matrix([[0, 0], [1, 0]])
OPS = {'Z': Zs, '+': Sps, '-': Sms}


def site_op(ops):
    M = sps.identity(1, format='csr')
    for x in range(Lc):
        M = sps.kron(M, ops.get(x, I2s), format='csr')
    return M


def tsum(word):
    return sum(site_op({(s0 + i) % Lc: OPS[c] for i, c in enumerate(word) if c != 'I'}) for s0 in range(Lc))


SEL = np.where(np.array([bin(i).count('1') for i in range(2 ** Lc)]) == Lc // 2)[0]
restrict = lambda M: M[SEL][:, SEL]
HOP, ZZ1, ZZ2 = restrict(-0.5 * (tsum('+-') + tsum('-+'))), restrict(0.25 * tsum('ZZ')), restrict(0.25 * tsum('ZIZ'))
CUR = restrict((1 / 2j) * (tsum('+-') - tsum('-+')))
ground = lambda M: spla.eigsh(M, k=1, which='SA')[0][0]


def curvature(Hm, Op, d=0.02):
    return (ground(Hm - d * Op) - 2 * ground(Hm) + ground(Hm + d * Op)) / d ** 2 / Lc


words = sorted({''.join(w) for r_ in (1, 2, 3) for w in _it.product('IZ+-', repeat=r_)
                if w[0] != 'I' and w[-1] != 'I' and w.count('+') == w.count('-')})
BASIS = [restrict(tsum(w)) for w in words]
widx = {w_: i for i, w_ in enumerate(words)}
PAR = np.zeros((len(words), len(words)))
for i, w_ in enumerate(words):
    PAR[widx[w_[::-1]], i] = 1
Dsec = BASIS[0].shape[0]
NORM = np.array([[(bi.conj().multiply(bj)).sum() for bj in BASIS] for bi in BASIS])
TR = np.array([b.diagonal().sum() for b in BASIS]); NORM = NORM - np.outer(TR.conj(), TR) / Dsec


def sector(sign):  # coordinates of the parity-even (+1) or parity-odd (-1) local operators, orthonormal in the traceless norm
    Pj = (np.eye(len(words)) + sign * PAR) / 2
    Nn = Pj.T @ NORM @ Pj; sN, UN = np.linalg.eigh(Nn); keep = sN > 1e-8 * sN.max()
    return Pj @ UN[:, keep] / np.sqrt(sN[keep])


T_EVEN, T_ODD = sector(+1), sector(-1)


def charges(Hm):  # smallest ||[H,Q]||^2/||Q||^2 in each parity sector, and the number of conserved even charges
    C = [Hm @ b - b @ Hm for b in BASIS]
    G = np.array([[(ci.conj().multiply(cj)).sum() for cj in C] for ci in C])
    ev = np.linalg.eigvalsh(T_EVEN.conj().T @ G @ T_EVEN); od = np.linalg.eigvalsh(T_ODD.conj().T @ G @ T_ODD)
    return ev, od


mrows = {}
for label, V1, V2 in (('free', 0.0, 0.0), ('XXZ', 1.0, 0.0), ('XXZ + next-nearest', 1.0, 0.6)):
    Hm = HOP + V1 * ZZ1 + V2 * ZZ2
    ev, od = charges(Hm)
    mrows[label] = (abs((ground((1 + 0.02) * Hm) - 2 * ground(Hm) + ground((1 - 0.02) * Hm)) / 0.02 ** 2 / Lc),
                    curvature(Hm, CUR), int(np.sum(ev < 1e-10) + np.sum(od < 1e-10)), bool(od.min() < 1e-10), float(od.min()))
check("M: the clock is protected; a shift coupled to the hopping current is not: lapse curvature zero for any matter; hopping-current shift curvature zero only without interactions; "
      "a local conserved parity-odd charge (range <= 3) exists for the free and integrable chains, none for the non-integrable one",
      all(v[0] < 1e-8 for v in mrows.values()) and abs(mrows['free'][1]) < 1e-8 and abs(mrows['XXZ + next-nearest'][1]) > 1e-3
      and mrows['free'][3] and mrows['XXZ'][3] and (not mrows['XXZ + next-nearest'][3]) and mrows['XXZ + next-nearest'][4] > 0.1,
      "; ".join(f"{k}: lapse curvature {v[0]:.0e}, shift curvature {v[1]:+.4f} per site, conserved local charges {v[2]}, "
                f"momentum-like one {'yes' if v[3] else 'no'} (best odd candidate {v[4]:.3f})" for k, v in mrows.items()))

# ---------------------------------------------------------------- N split matching
def split_total(e, M, S_):
    w_ = np.linalg.norm(S_ @ e, axis=1)
    return -np.mean(w_) + np.mean(np.sqrt(w_ ** 2 + M ** 2))


Ssp = np.sin(kgrid(96, 3))
split = {M: stiffness(lambda t, M=M: split_total(expm(t * EPS_E / 2), M, Ssp), d=2e-3) for M in (0.02, 0.05, 0.1, 0.2)}
ratios = [c_ / M ** 2 for M, c_ in split.items()]
coef = float(np.mean(ratios))
m_over = np.sqrt(32 * np.pi * abs(coef))  # member mass / (M l_P / a)
a_needed = m_over * 1e12 * 1.616255e-35 / 1.27e-23  # metres, for a 1 TeV splitting
check("N: boson-fermion matching must be exact: a mass splitting M leaves c ~ -0.044 (M a)^2, so a TeV splitting needs a lattice coarser than a metre",
      max(ratios) - min(ratios) < 0.002 and -0.05 < coef < -0.04 and a_needed > 1,
      f"c_E / (M a)^2 at M a = {list(split)}: {[round(x, 4) for x in ratios]}; member mass about {m_over:.1f} M l_P / a; "
      f"a TeV splitting passes the 1.27e-23 eV bound only for a > {a_needed:.1f} m")

# ---------------------------------------------------------------- O signs
rngO = np.random.default_rng(12); KO = kgrid(48, 3); sgn_ok = True; worst = []
for trial in range(6):
    coef = rngO.normal(size=(3, 3, 3))  # random real symbol v_a(k) = sum_j coef[a, j, m] sin((m+1) k_j) ... (odd, real)
    V_ = np.stack([sum(coef[a, j, m] * np.sin((m + 1) * KO[:, j]) for j in range(3) for m in range(3)) for a in range(3)], -1)
    eps_r = rngO.normal(size=(3, 3)); eps_r = eps_r + eps_r.T; eps_r -= np.trace(eps_r) / 3 * np.eye(3); eps_r /= np.linalg.norm(eps_r)
    cf = stiffness(lambda t: -np.mean(np.linalg.norm(V_ @ expm(t * eps_r / 2), axis=1)))
    Cb = np.einsum('na,nb->nab', V_, V_)
    cb = stiffness(lambda t: 0.5 * np.mean(np.log(np.einsum('nab,ab->n', Cb, expm(t * eps_r)) + 0.3)), d=2e-3)
    worst.append((cf, cb)); sgn_ok &= (cf < 0) and (cb > 0)
unb = sea(expm(8 * EPS_E / 2), np.sin(kgrid(64, 3)))
check("O: the signs are general: every fermion sea -<|e^T v|> is concave along volume-keeping shears (c < 0), every boson log-det is convex (c > 0); "
      "the fermion sea is unbounded below along such paths",
      sgn_ok and unb < -10, f"fermion, boson coefficients for 6 random real symbols and shears: {[(round(a_, 4), round(b_, 4)) for a_, b_ in worst]}; "
      f"walker sea energy at axis shear 8: {unb:.2f} (flat {E0:.2f})")

# ---------------------------------------------------------------- P dressing
dress = {}
for n in (96, 144):
    Kd = kgrid(n, 3); wd, vd = bands(Kd); Dd = wd[:, 1] - wd[:, 0]
    for name, eps, uni in (('axis', EPS_E, False), ('face', EPS_T, True)):
        me2 = np.abs(np.einsum('na,nab,nb->n', vd[:, :, 1].conj(), link_symbol(eps, Kd, np.zeros(3), uni), vd[:, :, 0])) ** 2
        dress[(n, name)] = (float(np.mean(me2 / Dd)), float(np.mean(me2 / Dd ** 3)))
alpha_gr = 1 / (64 * np.pi)  # alpha/wbar at a = l_P in lattice units
from scipy.optimize import brentq
Kd = kgrid(144, 3); wd, vd = bands(Kd); Dd = wd[:, 1] - wd[:, 0]
dressed, bare = {}, {}
for name, eps, uni, cc in (('axis', EPS_E, False, cE), ('face', EPS_T, True, cTu)):
    me2 = np.abs(np.einsum('na,nab,nb->n', vd[:, :, 1].conj(), link_symbol(eps, Kd, np.zeros(3), uni), vd[:, :, 0])) ** 2
    chi_im = lambda G, me2=me2: np.mean(me2 * Dd / (Dd ** 2 + G ** 2))  # exact one-loop response on the imaginary axis
    dressed[name] = brentq(lambda G: 2 * alpha_gr * G ** 2 - (tau / 4 + chi_im(G) / 2), 1e-6, 50)
    bare[name] = np.sqrt(abs(cc / (2 * alpha_gr)))
check("P: dressing by the sea's frequency dependence is finite: it adds chi2/4 to the member's inertia at low frequency (relative corrections (l_P/a)^2 for a >> l_P); "
      "at the Planck spacing the q = 0 growth rate solved exactly on the imaginary frequency axis is still cutoff-sized",
      all(abs(dress[(96, nm)][1] - dress[(144, nm)][1]) < 1e-4 for nm in ('axis', 'face')) and all(dressed[nm] < bare[nm] for nm in dressed),
      "; ".join(f"{nm}: chi2/4 = {dress[(144, nm)][1] / 4:.5f}, growth rate x a: static-only {bare[nm]:.2f}, exact {dressed[nm]:.3f}" for nm in ('axis', 'face'))
      + f"; alpha/wbar at a = l_P: {alpha_gr:.5f}")

# ---------------------------------------------------------------- Q crystal momentum is not local
Nq = 256; kq = 2 * np.pi * (np.arange(Nq) - Nq // 2) / Nq
ker = np.abs(np.fft.fft(np.fft.ifftshift(kq))) / Nq
rq = np.arange(1, 40)
check("Q: the exactly conserved crystal momentum has the sawtooth symbol k, whose real-space kernel decays only as 1/r (not a sum of local densities)",
      np.allclose(ker[rq] * rq, 1.0, rtol=0.05), f"|kernel(r)| * r at r = 1, 5, 20, 39: {[round(float(ker[r_] * r_), 3) for r_ in (1, 5, 20, 39)]}")

# ---------------------------------------------------------------- R dressed second order (2D walker, designed face coupling)
SX2 = np.array([[0, 1], [1, 0]], complex); SY2 = np.array([[0, -1j], [1j, 0]])


def grid2(L):
    k = (np.arange(L) + 0.5) * 2 * np.pi / L - np.pi
    return np.stack(np.meshgrid(k, k, indexing='ij'), -1).reshape(-1, 2)


def flow2(K, lam, steps=100):
    vf = lambda X: np.stack([lam / 2 * np.sin(2 * X[:, 1]), lam / 2 * np.sin(2 * X[:, 0])], -1)
    h = 1 / steps; X = K.copy()
    for _ in range(steps):
        a = vf(X); b = vf(X + h / 2 * a); c_ = vf(X + h / 2 * b); d_ = vf(X + h * c_); X = X + h / 6 * (a + 2 * b + 2 * c_ + d_)
    return X


def mp2_energies(L, lam, onsite):
    K = grid2(L); N = L * L; Kp = flow2(K, lam) if lam else K
    w, v = np.linalg.eigh(np.sin(Kp[:, 0])[:, None, None] * SX2 + np.sin(Kp[:, 1])[:, None, None] * SY2)
    lo, up, elo, eup = v[:, :, 0], v[:, :, 1], w[:, 0], w[:, 1]
    P = np.einsum('na,nb->nab', lo, lo.conj())
    if onsite:
        G = np.mean(P, axis=0); E1 = 0.5 * (1 - np.real(np.trace(G @ G.conj().T)))
        Wf = lambda dk: 0.5 + 0 * dk[..., 0]
    else:
        E1 = sum(1 - np.real(np.trace(G @ G.conj().T)) for G in [np.mean(P * np.exp(1j * K[:, j])[:, None, None], axis=0) for j in range(2)])
        Wf = lambda dk: np.cos(dk[..., 0]) + np.cos(dk[..., 1])
    idx = np.arange(N).reshape(L, L); ii, jj = np.unravel_index(np.arange(N), (L, L))
    O = np.einsum('ma,na->mn', up.conj(), lo); E2 = 0.0
    n2 = np.arange(N)[:, None]; n3 = np.arange(N)[None, :]
    for n1 in range(N):
        n4 = idx[(ii[n1] + ii[n2] - ii[n3]) % L, (jj[n1] + jj[n2] - jj[n3]) % L]
        A = Wf(K[n1] - K[n3]) * O[n3, n1] * O[n4, n2] - Wf(K[n2] - K[n3]) * O[n3, n2] * O[n4, n1]
        E2 += np.sum(np.abs(A) ** 2 / (eup[n3] + eup[n4] - elo[n1] - elo[n2]))
    return E1, -0.25 * (2 / N) ** 2 * E2 / N


def dressed_second(L, onsite, d=0.05):
    r = {lam: mp2_energies(L, lam, onsite) for lam in (-d, 0.0, d)}
    cv = lambda i: (r[-d][i] - 2 * r[0.0][i] + r[d][i]) / d ** 2 / 8
    c1, c2 = cv(0), cv(1)
    return c1, (c2 - 2 * c1 * r[0.0][1] / r[0.0][0]) if abs(c1) > 1e-12 else c2


dsec = {(nm, L): dressed_second(L, nm == 'on-site') for nm in ('nearest-neighbour', 'on-site') for L in (24, 32)}
nn24, nn32 = dsec[('nearest-neighbour', 24)][1], dsec[('nearest-neighbour', 32)][1]
os24, os32 = dsec[('on-site', 24)][1], dsec[('on-site', 32)][1]
check("R: after the first-order shape dependence of a nearest-neighbour interaction is cancelled by rescaling V with the shear, the second order brings it back "
      "(2D walker, designed face coupling; pre-registered: at least 1e-4 per V^2 with grids within 10 %); an on-site interaction, blind at first order, "
      "is shape-dependent at second order",
      nn32 > 1e-4 and abs(nn24 / nn32 - 1) < 0.1 and abs(dsec[('on-site', 32)][0]) < 1e-9 and os32 > 5e-5 and abs(os24 / os32 - 1) < 0.1,
      "; ".join(f"{nm} L={L}: first-order {v_[0]:+.6f}, dressed second-order {v_[1]:+.6f} per unit shear" for (nm, L), v_ in dsec.items()))

# ---------------------------------------------------------------- H size
hbar_c = 1.973269804e-7  # eV m
l_P = 1.616255e-35       # m
M_P = hbar_c / l_P       # eV (non-reduced Planck mass)
m_bound = 1.27e-23       # eV, LIGO-Virgo-KAGRA GWTC-3 (reference input)
c = min(abs(cE), abs(cTu))  # the smaller of the walker's two taste-universal coefficients


def mass(a):  # eV: m = sqrt(32 pi c) l_P / a^2, times hbar c
    return np.sqrt(32 * np.pi * c) * l_P / a ** 2 * hbar_c


m_planck, m_lhc = mass(l_P), mass(1e-19)
H0 = 1.5e-33  # eV, the Hubble rate (reference input)
tune_hubble_lhc, tune_hubble_planck = (H0 / m_lhc) ** 2, (H0 / m_planck) ** 2
tune_lhc = (m_bound / m_lhc) ** 2; tune_planck = (m_bound / m_planck) ** 2
check("H: size: an untuned coefficient gives the member's long-wavelength TT modes a Planck-size mass (or growth rate) at the Planck spacing, "
      "and still far above the gravitational-wave dispersion bound at an illustrative a = 1e-19 m",
      2.5 < m_planck / M_P < 5 and m_lhc / m_bound > 1e19,
      f"|m| = {m_planck / M_P:.2f} M_P at a = l_P; {m_lhc:.2e} eV at a = 1e-19 m ({m_lhc / m_bound:.1e} x the bound); "
      f"required tuning of c: {tune_lhc:.0e} (a = 1e-19 m), {tune_planck:.0e} (a = l_P) against the dispersion bound; for c < 0 (growth) against the Hubble rate: "
      f"{tune_hubble_lhc:.0e} (a = 1e-19 m, growth time {6.582e-16 / m_lhc:.1e} s), {tune_hubble_planck:.0e} (a = l_P)")

print("per_element: the sea energy's shear dependence is checked on explicit 2x2 Bloch symbols and on node Jacobians (J^T J) at all 8 nodes.")
print("per_site: an 8^3 real-space diagonalisation reproduces the k-space sea energy at three shapes; the designed hoppings' range decay is measured.")
print('per_mode: shape coefficients are Brillouin-zone quadratures converged on 64^3-144^3 grids; the static TT kernel is computed at finite q.')
print('per_block: checked and not executed - no finite interacting block of the walker is diagonalised; the interacting shift comparator is a 12-site spin chain.')
print('lattice_wide: checked and not executed - interactions only at first order (walker) and in a 1D comparator; no gauge fields, no dressed pole, no 3D charge search.')
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
