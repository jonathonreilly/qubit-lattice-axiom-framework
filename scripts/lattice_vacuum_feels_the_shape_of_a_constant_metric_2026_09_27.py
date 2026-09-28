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
   (cubic, not isotropic).
D. Real space: the vielbein-coupled walker on a periodic 8^3 lattice,
   diagonalised directly, has the k-space sea energy at every shape, and a
   sheared lattice's spectrum differs from the unsheared one, so no unitary
   relabelling of the matter maps one onto the other.
E. Only the shape matters: rotating the frame index (e -> e R) leaves the sea
   energy unchanged; turning an axis shear by 45 degrees into a face shear
   changes its cost from c_E/2 to c_T/2.
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
   own dispersion cancels the sea's shape energy at every shape; the
   standard forward-difference lattice scalar does not.
I. A designed coupling removes it for free matter: relabel the zone by the
   time-1 flow phi of a divergence-free trigonometric vector field that fixes
   the 8 nodes (v = curl(A e_3), A = (lam/4) sin 2k_1 sin 2k_2 for an axis
   shear, A = -(lam/4) cos k_1 cos 3k_2 for a face shear) and use the symbol
   sigma . s(phi(k)). The flow keeps volume, so the sea energy is exactly
   unchanged; every node sees one common sheared metric; the hoppings decay
   exponentially with range.
J. Interactions bring it back: with the designed coupling, the first-order
   energy of a nearest-neighbour density interaction V sum n_x n_{x+e_j}
   (its exchange part) depends on the shear, stiffness about 0.0019 V (axis)
   and 0.0049 V (face) per unit shear. The on-site density matrix is
   unchanged, so on-site interactions stay blind at first order.
K. Why: a relabelling that kept every momentum-conserving two-body vertex
   momentum-conserving would satisfy phi(a) + phi(b) = phi(a+b) + phi(0), so
   phi - phi(0) would be a continuous homomorphism of the torus, an integer
   matrix; no small shear is one. The designed phi violates momentum addition
   at order lam.
L. The zero-wavelength coefficient is the long-wavelength limit of the static
   kernel: for a static modulation cos(q x) of the vielbein along a cube axis,
   the TT coefficients (h_yy - h_zz and h_yz for q along x) computed from the
   second-order energy c(q) = -tau/4 - chi(q)/2 go smoothly (at order q^2) to
   c_E and c_T; for q along an axis these two polarisations are in their own
   irreps of the little group, so they do not mix with lapse, shift or trace.
H. Size (arithmetic, observational bound as reference input): with block
   101's member, the constant TT mode has omega^2 = c wbar / (2 alpha); in
   GR's normalisation m^2 = 32 pi G c / a^4 (units hbar = c = 1), with the
   added bridge that a hop costs hbar c / a. At the Planck spacing |m| is
   about 4 M_P; at an illustrative a = 1e-19 m it is about 1e-3 eV, 1e20
   times the LIGO-Virgo-KAGRA dispersion bound 1.27e-23 eV. The coefficient
   would have to be about 1e-40 of its natural size at that spacing (1e-104
   at the Planck spacing).

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
check("C: the walker's sea on Z^3 feels shear: two unequal, negative shape coefficients (the flat shape is a maximum of its energy)",
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
check("G: a boson with the walker's own dispersion cancels the sea's shape energy at every shape; the standard forward-difference scalar does not",
      max(abs(m) for m in matched) < 1e-13 and min(abs(s) for s in std) > 0.02,
      f"matched total at four shapes: {max(abs(m) for m in matched):.1e}; walker + forward-difference complex scalar stiffnesses {[round(s, 4) for s in std]}")

# ---------------------------------------------------------------- I designed coupling (free matter)
def v_axis(K, lam):  # curl(A e_3), A = (lam/4) sin 2k_1 sin 2k_2
    k1, k2 = K[:, 0], K[:, 1]
    return np.stack([lam / 2 * np.sin(2 * k1) * np.cos(2 * k2), -lam / 2 * np.cos(2 * k1) * np.sin(2 * k2), 0 * k1], -1)


def v_face(K, lam):  # curl(A e_3), A = -(lam/4) cos k_1 cos 3k_2
    k1, k2 = K[:, 0], K[:, 1]; c = -lam / 4
    return np.stack([-3 * c * np.cos(k1) * np.sin(3 * k2), c * np.sin(k1) * np.cos(3 * k2), 0 * k1], -1)


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
    metrics = []
    for K0 in NODES:
        J = np.zeros((3, 3)); dd = 1e-5
        for j in range(3):
            ej = np.zeros(3); ej[j] = dd
            J[:, j] = (flow((K0 + ej)[None], vf, lam)[0] - flow((K0 - ej)[None], vf, lam)[0]) / (2 * dd)
        D = np.diag(np.cos(K0)); _, P = polar(D @ J, side='right'); metrics.append(D @ P @ D)
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
      and abs(designed['axis'][2][0, 0] - np.exp(lam)) < 1e-8 and abs(designed['face'][2][0, 1]) > 0.09,
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
check("J: with the designed coupling, a nearest-neighbour density interaction's first-order energy is stiff to shear again; on-site interactions stay blind at first order",
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


def link_symbol(eps, K, qv):  # symbol of sum_x eps_{ja} e^{i q.x} [psi_x^dag (sigma_a/2i) psi_{x+j} + h.c.], k -> k+q
    M = 0
    for j in range(3):
        for a in range(3):
            if eps[j, a] != 0:
                A = PA[a] / (2j)
                M = M + eps[j, a] * (A[None] * np.exp(1j * K[:, j])[:, None, None]
                                     + A.conj().T[None] * np.exp(-1j * (K[:, j] + qv[j]))[:, None, None])
    return M


def chi(eps, qv, K):  # second-order energy lowering per unit <delta e^2> (interband, lower band k -> upper band k+q)
    w0, v0 = bands(K); out = []
    for sgn in ((1, -1) if np.any(qv) else (1,)):
        w1, v1 = bands(K + sgn * qv)
        me = np.einsum('na,nab,nb->n', v1[:, :, 1].conj(), link_symbol(eps, K, sgn * qv), v0[:, :, 0])
        out.append(np.mean(np.abs(me) ** 2 / (w1[:, 1] - w0[:, 0])))
    return float(np.mean(out))


KL = kgrid(96, 3); tau = float(np.mean(np.sin(KL[:, 0]) ** 2 / np.linalg.norm(np.sin(KL), axis=1)))
EPS_Ex = np.diag([0.0, 1.0, -1.0]) / np.sqrt(2); EPS_Tx = np.zeros((3, 3)); EPS_Tx[1, 2] = EPS_Tx[2, 1] = 1 / np.sqrt(2)
cq = {}
for name, eps in (('yy-zz', EPS_Ex), ('yz', EPS_Tx)):
    cq[name] = [-tau / 4 - chi(eps, np.array([2 * np.pi * m / 96, 0, 0]), KL) / 2 for m in (0, 1, 2, 4)]
check("L: the zero-wavelength coefficient is the long-wavelength limit of the static kernel: for q along x the two TT polarisations' "
      "coefficients go smoothly to c_E and c_T (differences shrink like q^2)",
      abs(cq['yy-zz'][0] - cE) < 1e-4 and abs(cq['yz'][0] - cT) < 1e-4
      and all(abs(v[1] - v[0]) < 1e-4 and abs(v[3] - v[0]) / abs(v[2] - v[0]) > 3 for v in cq.values()),
      "; ".join(f"{n}: c(q) at q = 0, 0.065, 0.131, 0.262: {[round(x, 5) for x in v]}" for n, v in cq.items()))

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
check("H: size: an untuned coefficient gives the member's long-wavelength TT modes a Planck-size mass (or growth rate) at the Planck spacing, "
      "and still far above the gravitational-wave dispersion bound at an illustrative a = 1e-19 m",
      3 < m_planck / M_P < 5 and m_lhc / m_bound > 1e19,
      f"|m| = {m_planck / M_P:.2f} M_P at a = l_P; {m_lhc:.2e} eV at a = 1e-19 m ({m_lhc / m_bound:.1e} x the bound); "
      f"required tuning of c: {tune_lhc:.0e} (a = 1e-19 m), {tune_planck:.0e} (a = l_P)")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
