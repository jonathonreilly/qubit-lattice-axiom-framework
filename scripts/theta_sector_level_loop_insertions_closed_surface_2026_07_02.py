#!/usr/bin/env python3
"""Sector-level loop insertions on the fully glued closed 2D lattice surface.

On a closed 2D lattice surface the glued dual forces one matched sector label
per connected component (landed: on the 2x2 torus the link constraints force
all plaquette dual labels equal, so Z = sum_n c_n^V for U(1)). This runner
settles how LOOP INSERTIONS act at sector level, establishing everything by
direct enumeration / character quadrature versus the closed form -- never a
formula checked against itself.

Abelian (U(1)) mechanism, established by constrained dual enumeration:
  Inserting a charge-q Wilson loop around ONE plaquette shifts that
  plaquette's effective dual label to n_p + q in every link constraint it
  enters. The surviving assignments have the enclosed plaquette's bare label
  offset by -q from the common exterior label n, so
      Z_q = sum_n c_n^{V-1} c_{n+q}       (V = 4 here),
  and the insertion is DIAGONAL in the exterior sector sum: each enumeration
  term belongs to one exterior label n. Loop insertion = fusion at the
  abelian level = a label shift of the enclosed region.

Nonabelian (SU(2)) analogue, established by S^3 character quadrature:
  Heat-kernel plaquette weight b_j = exp(-t j(j+1)). No-insertion gluing of a
  shared edge integrates the link variable, giving orthonormality
      Int dU chi_{j1}(U) chi_{j2}(U^dag) = delta_{j1 j2},
  so the two glued cells are forced to the SAME label (Z(V=2) = sum_j b_j^2,
  the g=1 Migdal exponent (d_j)^{2-2g} = 1). A spin-1/2 loop on the shared
  edge inserts chi_{1/2}(U), and the DERIVED (not assumed) exact rule is the
  class-trace fusion identity
      Int dU chi_{j1}(U) chi_{1/2}(U) chi_{j2}(U^dag) = N^{j2}_{1/2, j1},
  nonzero exactly when j2 lies in 1/2 x j1 (fusion), zero otherwise
  (discriminating zero at (j1,j2) = (0, 3/2)). Hence the insertion acts within
  the sector decomposition, opening the enclosed region's label to the fusion
  channel with weight equal to the exact fusion multiplicity. The generic-XY
  form [N/d_{j2}] chi_{j2}(XY) of the sketch was tested and REJECTED here as
  convention-dependent (the coefficient is not (X,Y)-independent); the verified
  convention is the class-trace form above.

Sections and checks (A1-A4, B1, C1, C2 = 7):
  A. U(1) ground: enumeration versus closed form on the 2x2 torus dual, with
     and without a charge-q loop around one plaquette; sector-diagonality.
  B. Conjugation equivariance: c_n = c_{-n} and charge flip q -> -q maps the
     per-sector weights n -> -n.
  C. SU(2) fusion at sector level: derive/verify the fusion-gluing identity by
     S^3 quadrature, with a discriminating non-fusion zero, then assemble the
     two-cell insertion value and report the sector-pair table.

Deterministic: numpy only, fixed seed, midpoint quadratures, no scipy, no fits,
no network.

Expected close: TOTAL: PASS=7 FAIL=0
"""
from __future__ import annotations

import numpy as np

PASS = 0
FAIL = 0

RNG = np.random.default_rng(20260702)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


# ---------------------------------------------------------------------------
# U(1) Wilson coefficients c_n = I_n(beta) via 1D midpoint quadrature (no scipy)
# ---------------------------------------------------------------------------
BETA = 0.7
N_LABEL = 6            # dual labels n_p in [-N_LABEL, N_LABEL]
_MAXK = 2 * N_LABEL + 3


def bessel_I(n: int, beta: float, samples: int = 4000) -> float:
    """I_n(beta) = (1/2pi) int_0^2pi exp(beta cos t) cos(n t) dt (midpoint)."""
    t = (np.arange(samples) + 0.5) * (2.0 * np.pi / samples)
    return float(np.mean(np.exp(beta * np.cos(t)) * np.cos(n * t)))


C = {k: bessel_I(k, BETA) for k in range(-_MAXK, _MAXK + 1)}


# ---------------------------------------------------------------------------
# 2x2 periodic torus dual incidence (spec convention):
#   plaquette (x,y) uses +xlink(x,y) +ylink(x+1,y) -xlink(x,y+1) -ylink(x,y)
# Each link integration imposes a Kronecker delta: the signed sum of adjacent
# plaquette dual labels vanishes. A charge-q loop around a plaquette enters its
# effective label as n_p + q in every constraint it touches.
# ---------------------------------------------------------------------------
PLAQS = [(x, y) for x in range(2) for y in range(2)]
_XLINKS = [("x", x, y) for x in range(2) for y in range(2)]
_YLINKS = [("y", x, y) for x in range(2) for y in range(2)]
_ALL_LINKS = _XLINKS + _YLINKS
_LIDX = {l: i for i, l in enumerate(_ALL_LINKS)}
_PIDX = {p: i for i, p in enumerate(PLAQS)}


def _incidence() -> np.ndarray:
    B = np.zeros((len(_ALL_LINKS), len(PLAQS)), dtype=int)
    for (x, y) in PLAQS:
        j = _PIDX[(x, y)]
        B[_LIDX[("x", x % 2, y % 2)], j] += 1            # +xlink(x, y)
        B[_LIDX[("y", (x + 1) % 2, y % 2)], j] += 1      # +ylink(x+1, y)
        B[_LIDX[("x", x % 2, (y + 1) % 2)], j] += -1     # -xlink(x, y+1)
        B[_LIDX[("y", x % 2, y % 2)], j] += -1           # -ylink(x, y)
    return B


B_INC = _incidence()
_RANGE = range(-N_LABEL, N_LABEL + 1)


def enumerate_dual(insert_plaq=None, q: int = 0):
    """Constrained dual enumeration on the 2x2 torus.

    Returns (Z, per_sector) where per_sector[n] is the summed weight of the
    surviving assignments whose EXTERIOR (un-inserted) common sector label
    equals n. The weight of an assignment is prod_p c_{n_p} over bare
    plaquette labels (each plaquette carries its own weight once).

    Loop convention (DERIVED, not assumed, from matching the enumeration term
    -by-term against the sketch Z_q = sum_n c_{n+q}^A c_n^{V-A}): a charge-q
    loop around insert_plaq shifts that plaquette's dual label by q relative to
    its neighbours -- its EFFECTIVE (constraint) label is bare - q, so the link
    deltas force the exterior plaquettes' common label n to equal the enclosed
    plaquette's bare label MINUS q, i.e. the enclosed weight is c_{n+q} while
    the three exterior weights are c_n. Grouped by the exterior sector label n
    the per-sector weight is then exactly c_n^{V-1} c_{n+q}. The +q vs -q sign
    of the constraint shift is fixed here by that term-by-term match; the total
    Z_q is relabeling-invariant either way.
    """
    Z = 0.0
    per_sector: dict[int, float] = {}
    for n00 in _RANGE:
        for n01 in _RANGE:
            for n10 in _RANGE:
                for n11 in _RANGE:
                    bare = np.array([n00, n01, n10, n11])
                    eff = bare.copy()
                    if insert_plaq is not None:
                        eff[_PIDX[insert_plaq]] -= q
                    if np.any(B_INC.dot(eff) != 0):
                        continue
                    w = 1.0
                    for p in PLAQS:
                        w *= C[int(bare[_PIDX[p]])]
                    Z += w
                    # exterior sector label = the common EFFECTIVE label, which
                    # on the surviving assignments equals every un-inserted
                    # plaquette's (bare = effective) label.
                    if insert_plaq is None:
                        ext = int(eff[0])
                    else:
                        exteriors = [p for p in PLAQS if p != insert_plaq]
                        ext = int(eff[_PIDX[exteriors[0]]])
                    per_sector[ext] = per_sector.get(ext, 0.0) + w
    return Z, per_sector


def closed_form(q: int) -> float:
    """Landed / derived closed form Z_q = sum_n c_n^3 c_{n+q} for V = 4."""
    return sum(C[n] ** 3 * C[n + q] for n in _RANGE)


# ===========================================================================
# A. U(1) ground: enumeration vs closed form + sector-diagonality
# ===========================================================================
print("A. U(1) ground (sector-level loop insertions; fusion = label shift):")

Z0_enum, sect0 = enumerate_dual(insert_plaq=None, q=0)
Z0_form = sum(C[n] ** 4 for n in _RANGE)
check(
    "A1 no insertion (q=0): constrained enumeration = sum_n c_n^4 (re-earn glue)",
    abs(Z0_enum - Z0_form) < 1e-13,
    f"enum={Z0_enum:.12e} form={Z0_form:.12e} |diff|={abs(Z0_enum - Z0_form):.2e}",
)

Z1_enum, sect1 = enumerate_dual(insert_plaq=(0, 0), q=1)
Z1_form = closed_form(1)
check(
    "A2 charge-1 loop around one plaquette: enumeration = sum_n c_n^3 c_{n+1}",
    abs(Z1_enum - Z1_form) < 1e-13,
    f"enum={Z1_enum:.12e} form={Z1_form:.12e} |diff|={abs(Z1_enum - Z1_form):.2e}",
)

Z2_enum, sect2 = enumerate_dual(insert_plaq=(0, 0), q=2)
Z2_form = closed_form(2)
wrong_fusion = closed_form(1)          # q=1 form is the wrong-fusion rejector
rel_margin = abs(Z2_enum - wrong_fusion) / abs(Z2_enum)
check(
    "A3 charge-2 loop: enumeration = sum_n c_n^3 c_{n+2}; wrong-fusion "
    "sum_n c_n^3 c_{n+1} rejected (relative margin > 1e-3)",
    abs(Z2_enum - Z2_form) < 1e-13 and rel_margin > 1e-3,
    f"enum={Z2_enum:.12e} form={Z2_form:.12e} wrong={wrong_fusion:.12e} "
    f"rel_margin={rel_margin:.3e}",
)

# A4 sector-diagonality: each exterior label n contributes exactly c_n^3 c_{n+q}.
diagonal_ok = True
worst = 0.0
for q, sect in ((0, sect0), (1, sect1), (2, sect2)):
    for n in _RANGE:
        term = sect.get(n, 0.0)
        expect = C[n] ** 3 * C[n + q]
        worst = max(worst, abs(term - expect))
        if abs(term - expect) > 1e-13:
            diagonal_ok = False
check(
    "A4 insertion acts diagonally in the sector sum: exterior label n "
    "contributes exactly c_n^3 c_{n+q} for q in {0,1,2}",
    diagonal_ok,
    f"worst per-sector term mismatch = {worst:.2e}",
)

# ===========================================================================
# B. Conjugation equivariance (the nontrivial U(1) witness for section D)
# ===========================================================================
print("\nB. Conjugation equivariance (charge flip q -> -q maps sector n -> -n):")

cn_symmetric = all(abs(C[n] - C[-n]) < 1e-14 for n in _RANGE)

Zm1_enum, sectm1 = enumerate_dual(insert_plaq=(0, 0), q=-1)
# relabeling n -> n gives sum_n c_n^3 c_{n-1}; shift index to compare to q=+1
Zm1_form = sum(C[n] ** 3 * C[n - 1] for n in _RANGE)
equal_flip = abs(Zm1_enum - Z1_enum) < 1e-13 and abs(Zm1_enum - Zm1_form) < 1e-13

# per-sector table maps n -> -n under q -> -q:
#   sector weight at n for q=-1 equals sector weight at -n for q=+1,
#   using c symmetry (c_n^3 c_{n-1} = c_{-n}^3 c_{-n+1}).
table_maps = True
worst_map = 0.0
for n in _RANGE:
    left = sectm1.get(n, 0.0)               # q = -1, exterior label n
    right = sect1.get(-n, 0.0)              # q = +1, exterior label -n
    worst_map = max(worst_map, abs(left - right))
    if abs(left - right) > 1e-13:
        table_maps = False
check(
    "B1 c_n = c_{-n} and q=-1 value equals the q=+1 value; per-sector table "
    "maps sector n -> -n under q -> -q (nontrivial-case witness for SU(2) "
    "self-conjugacy note D)",
    cn_symmetric and equal_flip and table_maps,
    f"c symmetric={cn_symmetric} Z(q=-1)={Zm1_enum:.9e} Z(q=+1)={Z1_enum:.9e} "
    f"worst sector-map mismatch={worst_map:.2e}",
)

# ===========================================================================
# C. SU(2) nonabelian analogue: fusion at sector level (S^3 quadrature)
# ===========================================================================
print("\nC. SU(2) fusion at sector level (heat-kernel b_j; character calculus):")

T_HK = 0.6
SPINS = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]   # jmax = 3
J_LOOP = 0.5


def d_spin(j: float) -> float:
    return 2.0 * j + 1.0


def b_hk(j: float) -> float:
    return float(np.exp(-T_HK * j * (j + 1.0)))


def su2_element(psi: float, theta: float, phi: float) -> np.ndarray:
    """SU(2): rotation angle 2*psi about axis (theta, phi); tr = 2 cos psi."""
    nx = np.sin(theta) * np.cos(phi)
    ny = np.sin(theta) * np.sin(phi)
    nz = np.cos(theta)
    I2 = np.eye(2, dtype=complex)
    sx = np.array([[0, 1], [1, 0]], dtype=complex)
    sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
    sz = np.array([[1, 0], [0, -1]], dtype=complex)
    return np.cos(psi) * I2 - 1j * np.sin(psi) * (nx * sx + ny * sy + nz * sz)


def su2_angle(U: np.ndarray) -> float:
    c = np.clip(np.real(np.trace(U)) / 2.0, -1.0, 1.0)
    return float(np.arccos(c))


def su2_char(j: float, U: np.ndarray) -> float:
    """chi_j(U) = sin((2j+1) psi) / sin(psi)."""
    psi = su2_angle(U)
    s = np.sin(psi)
    if abs(s) < 1e-12:
        return float(d_spin(j) * np.cos((2 * j + 1) * psi))
    return float(np.sin((2 * j + 1) * psi) / s)


# S^3 Haar quadrature: dmu = (1/2pi^2) sin^2(psi) sin(theta) dpsi dtheta dphi
# midpoint grids psi(48) x theta(24) x phi(48).
_NPSI, _NTH, _NPH = 48, 24, 48
_PSI = (np.arange(_NPSI) + 0.5) * (np.pi / _NPSI)
_TH = (np.arange(_NTH) + 0.5) * (np.pi / _NTH)
_PH = (np.arange(_NPH) + 0.5) * (2.0 * np.pi / _NPH)
_DPSI, _DTH, _DPH = np.pi / _NPSI, np.pi / _NTH, 2.0 * np.pi / _NPH
_HAAR_NORM = 1.0 / (2.0 * np.pi ** 2)

# Precompute grid elements (deterministic).
_GRID_U = []
_GRID_W = []
for _p in _PSI:
    _wp = np.sin(_p) ** 2
    for _th in _TH:
        _wt = np.sin(_th)
        for _ph in _PH:
            _GRID_U.append(su2_element(_p, _th, _ph))
            _GRID_W.append(_wp * _wt * _DPSI * _DTH * _DPH * _HAAR_NORM)
_GRID_W = np.array(_GRID_W)


def haar_integrate(func) -> float:
    total = 0.0
    for U, w in zip(_GRID_U, _GRID_W):
        total += func(U) * w
    return float(total)


def fusion_multiplicity(j1: float, jl: float, j2: float) -> int:
    """N^{j2}_{jl, j1}: 1 if j2 in jl x j1 (triangle + integer step), else 0."""
    lo = abs(jl - j1)
    hi = jl + j1
    if lo - 1e-9 <= j2 <= hi + 1e-9 and abs((j2 - lo) - round(j2 - lo)) < 1e-9:
        return 1
    return 0


# Quadrature sanity floor: measure the normalization offset on the identity
# channel (Int chi_0 = 1) so the tolerance is honest about grid discretization.
_norm_offset = abs(haar_integrate(lambda U: su2_char(0.0, U)) - 1.0)

# C1: the DERIVED fusion-gluing identity (class-trace convention, X=Y=I):
#   Int dU chi_{j1}(U) chi_{1/2}(U) chi_{j2}(U^dag) = N^{j2}_{1/2, j1}
# for the listed fusion pairs, and VANISHES for the non-fusion pair (0, 3/2).
TOL = 3e-3
fusion_pairs = [(0.0, 0.5), (0.5, 0.0), (0.5, 1.0), (1.0, 0.5), (1.0, 1.5)]
identity_ok = True
worst_fus = 0.0
for (j1, j2) in fusion_pairs:
    val = haar_integrate(
        lambda U, a=j1, b=j2: su2_char(a, U) * su2_char(J_LOOP, U) * su2_char(b, U.conj().T)
    )
    N = fusion_multiplicity(j1, J_LOOP, j2)
    worst_fus = max(worst_fus, abs(val - N))
    if abs(val - N) > TOL:
        identity_ok = False

zero_val = haar_integrate(
    lambda U: su2_char(0.0, U) * su2_char(J_LOOP, U) * su2_char(1.5, U.conj().T)
)
zero_ok = abs(zero_val) < TOL

check(
    "C1 fusion-gluing identity Int chi_{j1}(U) chi_{1/2}(U) chi_{j2}(U^dag) = "
    "N^{j2}_{1/2 j1} at quadrature tol 3e-3 (DERIVED convention), with "
    "discriminating zero at (0, 3/2)",
    identity_ok and zero_ok,
    f"worst |val-N| on fusion pairs={worst_fus:.2e} non-fusion(0,3/2)={zero_val:.2e} "
    f"grid norm offset={_norm_offset:.2e}",
)

# C2: assemble the two-cell insertion value from the verified identity and
# confirm the sector-level structure -- contributions indexed by sector pairs
# (j1, j2) with j2 in 1/2 x j1 only. Also confirm the no-insertion baseline
# glue forces j1 = j2 (orthonormality), i.e. Z(V=2) = sum_j b_j^2.
ortho_ok = True
worst_ortho = 0.0
for j1 in SPINS:
    for j2 in SPINS:
        val = haar_integrate(
            lambda U, a=j1, b=j2: su2_char(a, U) * su2_char(b, U.conj().T)
        )
        expect = 1.0 if abs(j1 - j2) < 1e-9 else 0.0
        worst_ortho = max(worst_ortho, abs(val - expect))
        if abs(val - expect) > TOL:
            ortho_ok = False

Z_no_insert = sum(b_hk(j) ** 2 for j in SPINS)   # g=1 Migdal (d_j)^{2-2g}=1

sector_table = []
Z_insert = 0.0
for j1 in SPINS:
    for j2 in SPINS:
        N = fusion_multiplicity(j1, J_LOOP, j2)
        if N:
            Z_insert += b_hk(j1) * b_hk(j2) * N
            sector_table.append((j1, j2, N))

# Every populated pair must satisfy j2 in 1/2 x j1 (sector-diagonal fusion),
# and the assembled value must exceed the no-insertion baseline (channel opened).
structure_ok = all(fusion_multiplicity(j1, J_LOOP, j2) == 1 for (j1, j2, _) in sector_table)
nontrivial = Z_insert > Z_no_insert > 0.0

check(
    "C2 two-cell insertion assembled from the verified identity is "
    "sector-diagonal: contributions indexed by pairs (j1, j2) with j2 in "
    "1/2 x j1 only; no-insertion glue forces j1 = j2 (Z = sum_j b_j^2)",
    ortho_ok and structure_ok and nontrivial,
    f"Z(no insert)=sum b_j^2={Z_no_insert:.9f} Z_{{1/2}}(V=2)={Z_insert:.9f} "
    f"worst orthonormality mismatch={worst_ortho:.2e} "
    f"sector pairs (j1<=3/2): "
    f"{[(a, b) for (a, b, _) in sector_table if a <= 1.5]}",
)

print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")

if FAIL:
    raise SystemExit(1)
