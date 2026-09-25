#!/usr/bin/env python3
"""Gauging the composite-site charge: the Yao-Lee matter of composite sites minimally coupled to the spin-1/2 link
field, with the Z2 gauge partner intact and a staggered background charge.

Setting (all supplied, none adopted): doubled coordinates with one role per site class (D-roles): vertex sites carry
the matter qubit sigma, link sites the U(1) link qubit with E_l = s^z_l / 2 along the link's orientation (open PR
9066), cube sites the Z2 gauge partner tau of the vertex below them (D-comp: the composite site is (v, v + (1,1,1))),
plaquette sites are free. Between composite sites two lattice steps apart along axis e, with link l between the
vertices and bond type lambda(e) = e, the dressed bond term is
  J (tau^lambda_c tau^lambda_c') [ sigma^z_v sigma^z_v' + 2 (sigma^+_v s^+_l sigma^-_v' + sigma^-_v s^-_l sigma^+_v') ],
the Yao-Lee bond of open PR 9144 with its charged part carrying one unit of link flux. The Gauss law is
  G_v = sum_out E_l - n_v + rho_v,  n_v = (1 + sigma^z_v)/2,  rho_v = 1 on odd vertices and 0 on even ones,
the staggered background without which a closed lattice has no charged gauge-invariant state. The link field moves
by the covariant ring -g (U + U^dag) of open PR 9072. Supplied model, finite certificates, no physical reading.

Cluster: one plaquette of four composite sites (4 matter, 4 partner and 4 link qubits, 4096 states), bond types
x, y, x, y.
1. Geometry: the five-site support of a dressed bond fits a 4 x 2 x 2 block and no closed star; cube sites are
   adjacent at distance two along every axis; the four site classes take four roles.
2. Gauge invariance: [G_v, H] = 0 exactly for every vertex with the link dressing and not without it (norm
   reported); the total matter charge commutes with H and the matter SU(2) is broken to U(1) by the dressing.
3. The Z2 structure survives: the plaquette product of the partner qubits commutes with H, so the Z2 flux sector
   is conserved, as in the undressed Yao-Lee model.
4. The gauge sector: its dimension, the fixed total charge N_f = 2 (the number of odd vertices), and the support
   condition: in every gauge-invariant basis state the matter record at a vertex equals the outward link flux plus
   the background, so the matter records are functions of the link records (and not conversely: the number of link
   patterns per matter pattern is reported). The spectrum in the gauge sector at g = 0 and g = 1/2, by Z2 flux.
5. The odd three-dimer term of open PR 9144, kappa (tau^x tau^z tau^y)(sigma . sigma) on the path v1 - v2 - v3, with its
   charged part dressed by the two link raising operators along the path: it commutes with every Gauss operator (the
   undressed one does not), with the matter charge and with the Z2 flux; under complex conjugation in the record basis,
   the anti-unitary symmetry of the gauged model, it flips sign while the bonds and the ring are even; the spin-flip
   time reversal of the ungauged model is broken by the dressing (it flips the charge but not the flux). It shifts the
   gauge-sector spectrum.

Prints one line per check and TOTAL: PASS=N FAIL=M.
"""
import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "1")

import itertools
import sys

import numpy as np
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 300

RESULTS = []


def check(label, ok, detail=""):
    RESULTS.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {label}" + (f" :: {detail}" if detail else ""))


I2 = sp.identity(2, format="csr", dtype=complex)
X = sp.csr_matrix(np.array([[0, 1], [1, 0]], dtype=complex))
Y = sp.csr_matrix(np.array([[0, -1j], [1j, 0]]))
Z = sp.csr_matrix(np.diag([1.0 + 0j, -1.0]))
SP = sp.csr_matrix(np.array([[0, 1], [0, 0]], dtype=complex))     # raises |1> (down, -1) to |0> (up, +1) in the Z basis
SM = SP.T.tocsr()
PAULI = {"x": X, "y": Y, "z": Z}

# qubits: 0-3 matter sigma at vertices v1..v4, 4-7 partner tau at cubes c1..c4, 8-11 links l12, l23, l43, l14
NQ = 12
DIM = 2 ** NQ


def op(i, M):
    mats = [I2] * NQ
    mats[i] = M
    out = mats[0]
    for m in mats[1:]:
        out = sp.kron(out, m, format="csr")
    return out


def prod(*ops):
    out = ops[0]
    for o in ops[1:]:
        out = out @ o
    return out


# ------------------------------------------------ 1. geometry in doubled coordinates
def role(site):
    odd = sum(c % 2 for c in site)
    return ["vertex", "link", "plaquette", "cube"][odd]


v, e = (0, 0, 0), (1, 0, 0)
c = tuple(v[i] + 1 for i in range(3))
vp = tuple(v[i] + 2 * e[i] for i in range(3))
cp = tuple(c[i] + 2 * e[i] for i in range(3))
l = tuple(v[i] + e[i] for i in range(3))
support = [v, vp, l, c, cp]
roles = [role(s) for s in support]
box = [max(s[i] for s in support) - min(s[i] for s in support) + 1 for i in range(3)]
stars = 0
for s in itertools.product(range(-2, 5), repeat=3):
    star = {s} | {tuple(np.add(s, d)) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]}
    stars += all(p in star for p in support)
cube_nbrs = sorted({tuple(np.add(c, 2 * np.array(d))) for d in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]})
check("geometry: a dressed bond spans two vertices, one link and two cubes in a 4 x 2 x 2 block, in no closed star; one role per site class",
      roles == ["vertex", "vertex", "link", "cube", "cube"] and box == [4, 2, 2] and stars == 0
      and all(role(n) == "cube" for n in cube_nbrs) and len(cube_nbrs) == 6,
      f"support roles {roles}; bounding box {box[0]}x{box[1]}x{box[2]}; closed stars containing it: {stars}; "
      f"a cube site's six neighbours at distance two are cube sites; plaquette sites stay free")

# ------------------------------------------------ the cluster Hamiltonian
# vertices v1=(0,0,0), v2=(2,0,0), v3=(2,2,0), v4=(0,2,0); links oriented l12: v1->v2 (x), l23: v2->v3 (y), l43: v4->v3 (x), l14: v1->v4 (y)
SIG = lambda i, a: op(i, PAULI[a])
TAU = lambda i, a: op(4 + i, PAULI[a])
LINK = {"12": 8, "23": 9, "43": 10, "14": 11}
E = {k: 0.5 * op(q, Z) for k, q in LINK.items()}                  # E_l = s^z_l / 2 along the link orientation
splus = {k: op(q, SP) for k, q in LINK.items()}
sminus = {k: op(q, SM) for k, q in LINK.items()}
n = [0.5 * (sp.identity(DIM, format="csr", dtype=complex) + SIG(i, "z")) for i in range(4)]
rho = [0, 1, 0, 1]                                                  # staggered background: odd vertices v2, v4
# outward flux: v1: +E12 +E14; v2: -E12 +E23; v3: -E23 -E43; v4: +E43 -E14
flux_out = [E["12"] + E["14"], -E["12"] + E["23"], -E["23"] - E["43"], E["43"] - E["14"]]
G = [flux_out[i] - n[i] + rho[i] * sp.identity(DIM, format="csr", dtype=complex) for i in range(4)]
BONDS = [(0, 1, "x", "12"), (1, 2, "y", "23"), (3, 2, "x", "43"), (0, 3, "y", "14")]    # (I, J, type, link), link oriented I -> J
J = 1.0


def bond(i, j, lam, link, dressed=True):
    zz = SIG(i, "z") @ SIG(j, "z")
    if dressed:
        hop = op(i, SP) @ splus[link] @ op(j, SM) + op(i, SM) @ sminus[link] @ op(j, SP)
    else:
        hop = op(i, SP) @ op(j, SM) + op(i, SM) @ op(j, SP)
    return J * (TAU(i, lam) @ TAU(j, lam)) @ (zz + 2 * hop)


H_matter = sum(bond(*b) for b in BONDS)
H_bare = sum(bond(*b, dressed=False) for b in BONDS)
U = splus["12"] @ splus["23"] @ sminus["43"] @ sminus["14"]        # circulation v1 -> v2 -> v3 -> v4 -> v1
ring = -(U + U.conj().T)


def cnorm(A, B):
    C = (A @ B - B @ A)
    return float(abs(C).max()) if C.nnz else 0.0


# ------------------------------------------------ 2. gauge invariance
comm_dressed = max(cnorm(G[i], H_matter) for i in range(4))
comm_ring = max(cnorm(G[i], ring) for i in range(4))
comm_bare = max(cnorm(G[i], H_bare) for i in range(4))
Sz = 0.5 * sum(SIG(i, "z") for i in range(4))
Sx = 0.5 * sum(SIG(i, "x") for i in range(4))
check("gauge invariance: the dressed bonds and the ring commute with every Gauss operator; the bare Yao-Lee bonds do not; SU(2) breaks to U(1)",
      comm_dressed == 0.0 and comm_ring == 0.0 and comm_bare > 0.5 and cnorm(Sz, H_matter) == 0.0 and cnorm(Sx, H_matter) > 0.5
      and cnorm(Sx, H_bare) == 0.0,
      f"|[G_v, H_dressed]| = {comm_dressed:.0e}, |[G_v, ring]| = {comm_ring:.0e}, |[G_v, H_bare]| = {comm_bare:.1f}; "
      f"|[S^z, H]| = {cnorm(Sz, H_matter):.0e}, |[S^x, H_dressed]| = {cnorm(Sx, H_matter):.1f}, |[S^x, H_bare]| = {cnorm(Sx, H_bare):.0e}")

# ------------------------------------------------ 3. the Z2 structure survives
W = prod(*[TAU(i, "z") for i in range(4)])
Wprod = prod(*[TAU(i, lam) @ TAU(j, lam) for (i, j, lam, _) in BONDS])
check("the Z2 flux of the partner qubits commutes with the dressed Hamiltonian and the ring",
      cnorm(W, H_matter) == 0.0 and cnorm(W, ring) == 0.0 and abs(Wprod + W).max() < 1e-12,
      f"|[W, H]| = {cnorm(W, H_matter):.0e}; the product of the four bond factors equals -W exactly")

# ------------------------------------------------ 4. the gauge sector
bits = ((np.arange(DIM)[:, None] >> np.arange(NQ)[::-1]) & 1)          # bit k of the basis index = qubit k (0 = up = +1)
zval = 1 - 2 * bits                                                   # sigma^z / s^z eigenvalues
nval = (1 + zval[:, :4]) / 2
Eval = zval[:, 8:] / 2                                                # E12, E23, E43, E14
fout = np.stack([Eval[:, 0] + Eval[:, 3], -Eval[:, 0] + Eval[:, 1], -Eval[:, 1] - Eval[:, 2], Eval[:, 2] - Eval[:, 3]], axis=1)
gauss = np.all(fout - nval + np.array(rho) == 0, axis=1)
idx = np.flatnonzero(gauss)
dG = len(idx)
Nf = nval[idx].sum(axis=1)
matter_patterns = {tuple(nval[i]) for i in idx}
link_per_matter = {m: len({tuple(Eval[i]) for i in idx if tuple(nval[i]) == m}) for m in matter_patterns}
P = sp.csr_matrix((np.ones(dG), (idx, np.arange(dG))), shape=(DIM, dG))
HG = (P.T @ (H_matter + 0.0 * ring) @ P).toarray()
HG_ring = (P.T @ (H_matter + 0.5 * ring) @ P).toarray()
WG = (P.T @ W @ P).toarray().real
herm = max(np.abs(HG - HG.conj().T).max(), np.abs(HG_ring - HG_ring.conj().T).max())
# check the sector is invariant: H maps it into itself
leak = float(abs(((sp.identity(DIM, format="csr") - P @ P.T) @ (H_matter + 0.5 * ring) @ P)).max())
spec0, spec1 = np.linalg.eigvalsh(HG), np.linalg.eigvalsh(HG_ring)
wdiag = np.round(np.diag(WG)).astype(int)
e_by_w = {w: (np.linalg.eigvalsh(HG_ring[np.ix_(wdiag == w, wdiag == w)])[:3]) for w in (1, -1)}
check("the gauge sector: fixed total charge 2, matter records determined by link records, invariant under H; spectra by Z2 flux",
      dG > 0 and set(Nf) == {2.0} and leak < 1e-12 and herm < 1e-12 and all(v_ >= 1 for v_ in link_per_matter.values())
      and abs(np.diag(WG)).min() > 1 - 1e-12,
      f"gauge-sector dimension {dG} of 4096; N_f = 2 in every state; {len(matter_patterns)} matter patterns with "
      f"{sorted(link_per_matter.values())} link patterns each; leakage of H out of the sector {leak:.0e}; W diagonal on the sector; "
      f"g = 0: lowest levels {np.round(spec0[:4], 4).tolist()}; g = 1/2: {np.round(spec1[:4], 4).tolist()}; "
      f"g = 1/2 by Z2 flux W = +1: {np.round(e_by_w[1], 4).tolist()}, W = -1: {np.round(e_by_w[-1], 4).tolist()}")

# ------------------------------------------------ 5. the time-reversal-odd term, dressed along its two-link path
# path v1 - v2 - v3 through the corner v2 (bond types x then y): kappa (tau^x_1 tau^z_2 tau^y_3)(sigma_1 . sigma_3), with the
# charged part hopping the fermion from v3 to v1: the outward flux at v1 must rise by one (s^+_12), the flux through v2 must
# pass (s^+_23 keeps -E12 + E23 fixed), and the outward flux at v3 then falls by one.
kappa = 0.35
odd_tau = TAU(0, "x") @ TAU(1, "z") @ TAU(2, "y")
odd_dressed = kappa * odd_tau @ (SIG(0, "z") @ SIG(2, "z") + 2 * (op(0, SP) @ splus["12"] @ splus["23"] @ op(2, SM)
                                                                 + op(0, SM) @ sminus["12"] @ sminus["23"] @ op(2, SP)))
odd_bare = kappa * odd_tau @ (SIG(0, "z") @ SIG(2, "z") + 2 * (op(0, SP) @ op(2, SM) + op(0, SM) @ op(2, SP)))
# anti-unitary symmetries: K = complex conjugation in the record basis (fixes every record and link value); the spin-flip
# time reversal Y..Y K of the ungauged model flips the charge but not the flux, so the dressed hops break it
T_odd = odd_dressed.conj()
T_even = (H_matter + ring).conj()
Yall = op(0, Y)
for q_ in range(1, NQ):
    Yall = Yall @ op(q_, Y)
spinflip_break = float(abs(Yall @ H_matter.conj() @ Yall - H_matter).max())
spinflip_bare = float(abs(Yall @ H_bare.conj() @ Yall - H_bare).max())
comm_odd = max(cnorm(G[i], odd_dressed) for i in range(4))
comm_odd_bare = max(cnorm(G[i], odd_bare) for i in range(4))
HG_odd = (P.T @ (H_matter + 0.5 * ring + odd_dressed) @ P).toarray()
leak_odd = float(abs(((sp.identity(DIM, format="csr") - P @ P.T) @ (H_matter + 0.5 * ring + odd_dressed) @ P)).max())
spec_odd = np.linalg.eigvalsh(HG_odd)
check("the odd three-dimer term dressed along its two-link path keeps gauge invariance, the charge and the Z2 flux; it is odd under record-basis conjugation, under which the bonds and ring are even",
      comm_odd == 0.0 and comm_odd_bare > 0.5 and cnorm(Sz, odd_dressed) == 0.0 and cnorm(W, odd_dressed) == 0.0
      and abs(T_odd + odd_dressed).max() < 1e-12 and abs(T_even - (H_matter + ring)).max() < 1e-12 and leak_odd < 1e-12
      and abs(spec_odd - spec1).max() > 1e-6 and spinflip_break > 0.5 and spinflip_bare < 1e-12,
      f"|[G_v, odd_dressed]| = {comm_odd:.0e}, |[G_v, odd_bare]| = {comm_odd_bare:.1f}; |[S^z, odd]| = {cnorm(Sz, odd_dressed):.0e}; "
      f"|[W, odd]| = {cnorm(W, odd_dressed):.0e}; under record-basis conjugation K the odd term flips sign ({abs(T_odd + odd_dressed).max():.0e}) "
      f"while the bonds and ring are even ({abs(T_even - (H_matter + ring)).max():.0e}); the spin-flip time reversal of the ungauged model "
      f"is broken by the dressing (|Y K H Y - H| = {spinflip_break:.1f}, bare {spinflip_bare:.0e}); leakage {leak_odd:.0e}; lowest levels "
      f"with the odd term at kappa = {kappa}: {np.round(spec_odd[:4], 4).tolist()}")

print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
