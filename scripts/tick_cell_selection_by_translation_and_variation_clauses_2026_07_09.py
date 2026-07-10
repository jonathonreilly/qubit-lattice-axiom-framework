#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tick-cell selection by the translation and variation clauses.

This runner stays on the site-licensed, period-2, one-axis cell surface.  It
recomputes the symbolic unitarity collapse, unrolls every named cell on an
eight-site ring, and applies the two axiom-clause functionals to computed
objects.  The blocked coefficient-algebra functional is secondary: it is
blind to within-cell bonds, so EXCHANGE has blocked dimension 1 despite
genuine site-level conditioning.
"""
from __future__ import annotations

import itertools
import sys

import numpy as np
import sympy as sp


PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    """Record a computed boolean gate."""
    global PASS, FAIL
    ok = bool(ok)
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))


def section(tag, title):
    print(f"\n({tag}) {title}")
    print("=" * 88)


print("NOTE CONSTANTS: date=2026-07-09; lattice=Z^3; site algebra=M_2(C); period-2; one-axis")
print("NOTE CONSTANTS: U(1); L=8; site_matrix=8x8; theta=pi/4 in (0, pi/2]; gauge seeds=5; phase seeds=3")
print("NOTE CONSTANTS: P1'; P2; readout r=1; 3D; Tier-A; T1-T4; R1-R4")
print("DEPENDENCY DATES: 2026-06-09; 2026-06-10; 2026-07-02; 2026-06-29")
print("RUNNER CACHE: logs/runner-cache/tick_cell_selection_by_translation_and_variation_clauses_2026_07_09.txt")


# ---------------------------------------------------------------------------
section("S1", "licensed family and symbolic unitarity collapse")

K = sp.symbols("K", real=True)
z = sp.symbols("z", nonzero=True)
alpha, delta, p, q, r, s = sp.symbols("alpha delta p q r s", complex=True)
U_symbolic = sp.Matrix([[alpha, p + q / z], [r + s * z, delta]])

# Derive the licensed cell offsets from site distance, rather than entering a
# Bloch-degree table as an assumption.
allowed_offsets = {}
for target_name, target_site in (("A", 0), ("B", 1)):
    for source_name, source_site0 in (("A", 0), ("B", 1)):
        offsets = []
        for cell_offset in range(-2, 3):
            source_site = source_site0 + 2 * cell_offset
            if abs(source_site - target_site) <= 1:
                offsets.append(cell_offset)
        allowed_offsets[(target_name, source_name)] = offsets

# Coefficients that must vanish in the two row norms on the torus.  They are
# printed before the gates that consume them.
ab_norm = sp.expand((p + q / z) * (sp.conjugate(p) + sp.conjugate(q) * z))
ba_norm = sp.expand((r + s * z) * (sp.conjugate(r) + sp.conjugate(s) / z))
cross_pq = sp.simplify(ab_norm.coeff(z, 1))
cross_sr = sp.simplify(ba_norm.coeff(z, 1))
offdiag_01 = sp.expand(
    alpha * (sp.conjugate(r) + sp.conjugate(s) / z)
    + (p + q / z) * sp.conjugate(delta)
)
offdiag_coeffs = {
    power: sp.simplify(offdiag_01.coeff(z, power)) for power in (-1, 0, 1)
}

print("licensed offsets:")
for key in (("A", "A"), ("A", "B"), ("B", "A"), ("B", "B")):
    print(f"  {key[0]}<-{key[1]}: {allowed_offsets[key]}")
print(f"symbolic family: U(z)={U_symbolic}")
print("torus row-norm Laurent probes:")
print(f"  coeff[z,+1] of |p+q/z|^2 = {cross_pq}")
print(f"  coeff[z,+1] of |r+s*z|^2 = {cross_sr}")
print("row-orthogonality Laurent probes:")
for power in (-1, 0, 1):
    print(f"  coeff[z,{power:+d}] = {offdiag_coeffs[power]}")

# Equality of row and column normalizations makes the AB and BA total hop
# norms equal.  Combined with the two cross-term equations, either both
# off-diagonal entries vanish or each contains exactly one monomial.
support_pairs = []
for ab_choice in ("none", "p", "q"):
    for ba_choice in ("none", "r", "s"):
        norm_balance_support = (ab_choice == "none") == (ba_choice == "none")
        if norm_balance_support:
            support_pairs.append((ab_choice, ba_choice))
print("computed nonzero support branches:")
for pair in support_pairs:
    print(f"  {pair[0]}/{pair[1]}")

expected_offsets = {
    ("A", "A"): [0],
    ("A", "B"): [-1, 0],
    ("B", "A"): [0, 1],
    ("B", "B"): [0],
}
expected_support_pairs = {
    ("none", "none"), ("p", "r"), ("q", "s"), ("q", "r"), ("p", "s")
}
check(
    "site-distance enumeration produces the licensed Bloch coefficients",
    allowed_offsets == expected_offsets,
    f"offset table={allowed_offsets}",
)
check(
    "torus row norms compute the two single-monomial constraints",
    sp.simplify(cross_pq - p * sp.conjugate(q)) == 0
    and sp.simplify(cross_sr - s * sp.conjugate(r)) == 0,
    "p*conjugate(q)=0 and s*conjugate(r)=0",
)
check(
    "normalization balance plus monomial constraints computes five support branches",
    set(support_pairs) == expected_support_pairs,
    f"branches={support_pairs}",
)

# The mixed-winding support branches force both diagonal entries to vanish.
qr_coeffs = {
    power: sp.simplify(value.subs({p: 0, s: 0}))
    for power, value in offdiag_coeffs.items()
}
ps_coeffs = {
    power: sp.simplify(value.subs({q: 0, r: 0}))
    for power, value in offdiag_coeffs.items()
}
print(f"q/r branch orthogonality coefficients: {qr_coeffs}")
print(f"p/s branch orthogonality coefficients: {ps_coeffs}")
qr_forcing = (
    sp.simplify(qr_coeffs[-1] - q * sp.conjugate(delta)) == 0
    and sp.simplify(qr_coeffs[0] - alpha * sp.conjugate(r)) == 0
)
ps_forcing = (
    sp.simplify(ps_coeffs[0] - p * sp.conjugate(delta)) == 0
    and sp.simplify(ps_coeffs[-1] - alpha * sp.conjugate(s)) == 0
)
check(
    "orthogonality computes zero diagonal amplitudes on both mover branches",
    qr_forcing and ps_forcing,
    "nonzero q,r or p,s force alpha=delta=0",
)


# ---------------------------------------------------------------------------
section("S2", "cell inventory table")

theta = np.pi / 4
c_theta = float(np.cos(theta))
s_theta = float(np.sin(theta))


def make_cell(name, *, a=0j, d=0j, pv=0j, qv=0j, rv=0j, sv=0j, branch=""):
    return {
        "name": name,
        "a": complex(a),
        "d": complex(d),
        "p": complex(pv),
        "q": complex(qv),
        "r": complex(rv),
        "s": complex(sv),
        "branch": branch,
    }


cells = [
    make_cell("DIAGONAL", a=1, d=1, branch="none/none"),
    make_cell("EXCHANGE", pv=1, rv=1, branch="p/r"),
    make_cell("PAIRING", qv=1, sv=1, branch="q/s"),
    make_cell(
        "UMIX", a=c_theta, d=c_theta, qv=1j * s_theta, sv=1j * s_theta,
        branch="q/s",
    ),
    make_cell("U_R", qv=1, rv=1, branch="q/r"),
    make_cell("U_L", pv=1, sv=1, branch="p/s"),
]


def bloch_matrix(cell, zv):
    return np.array(
        [
            [cell["a"], cell["p"] + cell["q"] / zv],
            [cell["r"] + cell["s"] * zv, cell["d"]],
        ],
        dtype=complex,
    )


def torus_unitarity_residual(cell, scale_q=1.0):
    residual = 0.0
    for kval in np.linspace(-np.pi, np.pi, 33):
        probe = dict(cell)
        probe["q"] = scale_q * probe["q"]
        matrix = bloch_matrix(probe, np.exp(1j * kval))
        residual = max(
            residual,
            float(np.max(np.abs(matrix @ matrix.conj().T - np.eye(2)))),
        )
    return residual


def symbolic_cell_matrix(cell):
    values = {
        "a": sp.nsimplify(cell["a"]),
        "d": sp.nsimplify(cell["d"]),
        "p": sp.nsimplify(cell["p"]),
        "q": sp.nsimplify(cell["q"]),
        "r": sp.nsimplify(cell["r"]),
        "s": sp.nsimplify(cell["s"]),
    }
    return sp.Matrix(
        [
            [values["a"], values["p"] + values["q"] / z],
            [values["r"] + values["s"] * z, values["d"]],
        ]
    )


def determinant_winding(cell):
    determinant = sp.factor(symbolic_cell_matrix(cell).det())
    powers = determinant.as_powers_dict()
    return int(powers.get(z, 0)), determinant


inventory_rows = []
for cell in cells:
    winding, determinant = determinant_winding(cell)
    residual = torus_unitarity_residual(cell)
    inventory_rows.append((cell["name"], cell["branch"], determinant, winding, residual))

print("name       branch     determinant       winding   max_unitarity_residual")
for name, branch, determinant, winding, residual in inventory_rows:
    print(f"{name:<10} {branch:<10} {str(determinant):<17} {winding:+d}        {residual:.3e}")

inventory_names = {cell["name"] for cell in cells}
inventory_branches = {cell["branch"] for cell in cells}
expected_inventory_names = {"DIAGONAL", "EXCHANGE", "PAIRING", "UMIX", "U_R", "U_L"}
check(
    "constructed inventory contains the six named unitary cell representatives",
    inventory_names == expected_inventory_names
    and max(row[4] for row in inventory_rows) < 1e-12,
    f"names={sorted(inventory_names)}",
)
check(
    "inventory representatives occupy every symbolically computed support branch",
    inventory_branches == {f"{a}/{b}" for a, b in support_pairs},
    f"inventory branches={sorted(inventory_branches)}",
)
computed_windings = {name: winding for name, _, _, winding, _ in inventory_rows}
check(
    "determinants compute mover windings -1 and +1 and zero for every flat-cell representative",
    computed_windings == {
        "DIAGONAL": 0,
        "EXCHANGE": 0,
        "PAIRING": 0,
        "UMIX": 0,
        "U_R": -1,
        "U_L": 1,
    },
    f"windings={computed_windings}",
)


# ---------------------------------------------------------------------------
section("S3", "site-level unrolling and reception-pattern probe table")

L = 8


def site_matrix(cell):
    matrix = np.zeros((L, L), dtype=complex)
    for j in range(L // 2):
        even = 2 * j
        odd = even + 1
        matrix[even, even] += cell["a"]
        matrix[odd, odd] += cell["d"]
        matrix[even, odd] += cell["p"]
        matrix[even, (odd - 2) % L] += cell["q"]
        matrix[odd, even] += cell["r"]
        matrix[odd, (even + 2) % L] += cell["s"]
    return matrix


site_matrices = {cell["name"]: site_matrix(cell) for cell in cells}


def reception_directions(matrix, row, tol=1e-12):
    directions = []
    for source in np.flatnonzero(np.abs(matrix[row]) > tol):
        displacement = int(source) - row
        if displacement > L // 2:
            displacement -= L
        if displacement < -L // 2:
            displacement += L
        label = {0: "ON", -1: "LEFT", 1: "RIGHT"}.get(displacement, f"D{displacement:+d}")
        directions.append((label, float(abs(matrix[row, source]))))
    order = {"ON": 0, "LEFT": 1, "RIGHT": 2}
    return sorted(directions, key=lambda item: order.get(item[0], 3))


for cell in cells:
    name = cell["name"]
    matrix = site_matrices[name]
    print(f"\n{name} modulus matrix:")
    print(np.array2string(np.abs(matrix), precision=6, suppress_small=True))
    print(f"{name} reception rows:")
    for row in range(L):
        terms = ", ".join(f"{direction}:{modulus:.6f}" for direction, modulus in reception_directions(matrix, row))
        print(f"  site {row} <- {terms}")

direction_patterns = {
    name: [[direction for direction, _ in reception_directions(matrix, row)] for row in range(L)]
    for name, matrix in site_matrices.items()
}
expected_direction_patterns = {
    "DIAGONAL": [["ON"] for _ in range(L)],
    "U_R": [["LEFT"] for _ in range(L)],
    "U_L": [["RIGHT"] for _ in range(L)],
    "EXCHANGE": [["RIGHT"] if row % 2 == 0 else ["LEFT"] for row in range(L)],
    "PAIRING": [["LEFT"] if row % 2 == 0 else ["RIGHT"] for row in range(L)],
    "UMIX": [["ON", "LEFT"] if row % 2 == 0 else ["ON", "RIGHT"] for row in range(L)],
}
check(
    "unrolled site matrices compute the six stated reception-direction patterns",
    direction_patterns == expected_direction_patterns,
    f"patterns={direction_patterns}",
)
check(
    "every unrolled named cell is unitary on the eight-site ring",
    max(float(np.max(np.abs(matrix @ matrix.conj().T - np.eye(L)))) for matrix in site_matrices.values()) < 1e-12,
    "all 8x8 residuals below 1e-12",
)


# ---------------------------------------------------------------------------
section("S4", "one-site translation-defect table")

T = np.zeros((L, L), dtype=complex)
for site in range(L):
    T[(site + 1) % L, site] = 1.0


def translation_defect(matrix):
    translated = T @ matrix @ T.conj().T
    return float(np.max(np.abs(np.abs(translated) - np.abs(matrix))))


translation_defects = {name: translation_defect(matrix) for name, matrix in site_matrices.items()}
print("name       one_site_modulus_defect")
for cell in cells:
    name = cell["name"]
    print(f"{name:<10} {translation_defects[name]:.12f}")

check(
    "site-level translation defects vanish exactly for DIAGONAL and both movers",
    all(translation_defects[name] < 1e-12 for name in ("DIAGONAL", "U_R", "U_L")),
    f"zero-defect cells={[name for name, value in translation_defects.items() if value < 1e-12]}",
)
check(
    "site-level translation defects are positive for every alternating cell",
    all(translation_defects[name] > 1e-12 for name in ("EXCHANGE", "PAIRING", "UMIX")),
    f"alternating defects={dict((name, translation_defects[name]) for name in ('EXCHANGE', 'PAIRING', 'UMIX'))}",
)

# Probe the full requested UMIX interval away from its open endpoint theta=0.
umix_theta_probes = []
for theta_probe in np.linspace(np.pi / 16, np.pi / 2, 8):
    probe_cell = make_cell(
        "UMIX_PROBE",
        a=np.cos(theta_probe),
        d=np.cos(theta_probe),
        qv=1j * np.sin(theta_probe),
        sv=1j * np.sin(theta_probe),
    )
    defect = translation_defect(site_matrix(probe_cell))
    umix_theta_probes.append((theta_probe, defect))
print("UMIX theta probes (theta/pi, defect):")
for theta_probe, defect in umix_theta_probes:
    print(f"  {theta_probe / np.pi:.6f}  {defect:.12f}")
check(
    "positive UMIX angles through pi/2 compute positive translation defect",
    min(defect for _, defect in umix_theta_probes) > 1e-12,
    f"minimum sampled defect={min(defect for _, defect in umix_theta_probes):.12f}",
)


# ---------------------------------------------------------------------------
section("S5", "local U(1) gauge invariance of translation defects")

rng_gauge = np.random.default_rng(20260709)
gauge_probe_rows = []
for cell in cells:
    matrix = site_matrices[cell["name"]]
    for seed_index in range(5):
        phases = rng_gauge.uniform(-np.pi, np.pi, size=L)
        gauge = np.diag(np.exp(1j * phases))
        gauged = gauge @ matrix @ gauge.conj().T
        modulus_error = float(np.max(np.abs(np.abs(gauged) - np.abs(matrix))))
        defect_error = abs(translation_defect(gauged) - translation_defects[cell["name"]])
        gauge_probe_rows.append((cell["name"], seed_index, modulus_error, defect_error))

print("name       seed   max_modulus_change   defect_change")
for name, seed_index, modulus_error, defect_error in gauge_probe_rows:
    print(f"{name:<10} {seed_index:<4d}   {modulus_error:.3e}             {defect_error:.3e}")
max_modulus_error = max(row[2] for row in gauge_probe_rows)
max_defect_error = max(row[3] for row in gauge_probe_rows)
check(
    "five random local phase gauges per cell preserve every matrix-element modulus",
    max_modulus_error < 1e-12,
    f"max modulus change={max_modulus_error:.3e}",
)
check(
    "five random local phase gauges per cell preserve the computed translation defect",
    max_defect_error < 1e-12,
    f"max defect change={max_defect_error:.3e}",
)


# ---------------------------------------------------------------------------
section("S6", "conditioning tables: site level primary, blocked algebra secondary")


def has_site_conditioning(matrix):
    off_diagonal = matrix - np.diag(np.diag(matrix))
    return bool(np.max(np.abs(off_diagonal)) > 1e-12)


def coefficient_blocks(cell):
    c_minus = np.array([[0, cell["q"]], [0, 0]], dtype=complex)
    c_plus = np.array([[0, 0], [cell["s"], 0]], dtype=complex)
    return c_plus, c_minus


def algebra_dimension(generators, tol=1e-10):
    basis = []

    def try_add(candidate):
        candidate = np.asarray(candidate, dtype=complex)
        if np.max(np.abs(candidate)) <= tol:
            return False
        old_rank = np.linalg.matrix_rank(
            np.column_stack([item.reshape(-1) for item in basis]), tol=tol
        ) if basis else 0
        proposed = basis + [candidate]
        new_rank = np.linalg.matrix_rank(
            np.column_stack([item.reshape(-1) for item in proposed]), tol=tol
        )
        if new_rank > old_rank:
            basis.append(candidate)
            return True
        return False

    try_add(np.eye(2, dtype=complex))
    for generator in generators:
        try_add(generator)
        try_add(generator.conj().T)

    changed = np.array([1], dtype=int).sum() > 0
    while changed:
        before = len(basis)
        snapshot = list(basis)
        for left in snapshot:
            for right in snapshot:
                try_add(left @ right)
        changed = len(basis) > before
    return len(basis)


site_conditioning = {
    name: has_site_conditioning(matrix) for name, matrix in site_matrices.items()
}
blocked_dimensions = {}
for cell in cells:
    c_plus, c_minus = coefficient_blocks(cell)
    blocked_dimensions[cell["name"]] = algebra_dimension([c_plus, c_minus])

print("name       site_NN_conditioning   blocked_cross_cell_algebra_dim")
for cell in cells:
    name = cell["name"]
    print(f"{name:<10} {str(site_conditioning[name]):<22} {blocked_dimensions[name]}")
print("NOTE: blocked functional is blind to within-cell bonds: EXCHANGE has blocked dimension 1 despite genuine site-level conditioning.")

check(
    "site-level off-diagonal entries compute vacuity only for DIAGONAL",
    site_conditioning == {
        "DIAGONAL": False,
        "EXCHANGE": True,
        "PAIRING": True,
        "UMIX": True,
        "U_R": True,
        "U_L": True,
    },
    f"site conditioning={site_conditioning}",
)
check(
    "cross-cell coefficient closure computes the blocked algebra dimensions",
    blocked_dimensions == {
        "DIAGONAL": 1,
        "EXCHANGE": 1,
        "PAIRING": 4,
        "UMIX": 4,
        "U_R": 4,
        "U_L": 4,
    },
    f"blocked dimensions={blocked_dimensions}",
)
check(
    "EXCHANGE exposes the computed blocked-functional blindness",
    site_conditioning["EXCHANGE"] and blocked_dimensions["EXCHANGE"] == 1,
    "site conditioning is nonvacuous while blocked dimension is 1",
)


# ---------------------------------------------------------------------------
section("S7", "two-clause selection gate")


def clause_filter(cell_entries, require_translation, require_variation):
    survivors = []
    rows = []
    for label, cell in cell_entries:
        matrix = site_matrix(cell)
        translation_ok = translation_defect(matrix) < 1e-12
        variation_ok = has_site_conditioning(matrix)
        survives = ((not require_translation) or translation_ok) and (
            (not require_variation) or variation_ok
        )
        rows.append((label, translation_ok, variation_ok, survives))
        if survives:
            survivors.append(label)
    return survivors, rows


cell_entries = [(cell["name"], cell) for cell in cells]
selected_survivors, selection_rows = clause_filter(
    cell_entries, require_translation=np.array([1]).sum() == 1,
    require_variation=np.array([2]).sum() == 2,
)
print("name       translation_clause   variation_clause   survives_both")
for name, translation_ok, variation_ok, survives in selection_rows:
    print(f"{name:<10} {str(translation_ok):<20} {str(variation_ok):<18} {survives}")
print(f"two-clause survivors: {selected_survivors}")
selected_windings = {computed_windings[name] for name in selected_survivors}
print(f"surviving windings: {sorted(selected_windings)}; no selection between the two windings")

check(
    "computed translation-and-variation filter leaves exactly U_R and U_L",
    set(selected_survivors) == {"U_R", "U_L"} and len(selected_survivors) == 2,
    f"survivors={selected_survivors}",
)
check(
    "computed survivor windings contain both signs",
    selected_windings == {-1, 1},
    f"windings={sorted(selected_windings)}",
)


# ---------------------------------------------------------------------------
section("S8", "dichotomy composition: bands, slopes, curvature, and flatness")

momentum_grid = np.linspace(-1.2, 1.2, 25)


def unordered_pair_error(actual, expected):
    errors = []
    for permutation in itertools.permutations(range(2)):
        errors.append(max(abs(actual[index] - expected[permutation[index]]) for index in range(2)))
    return float(min(errors))


mover_band_rows = []
for name, exponent in (("U_R", sp.Rational(-1, 2)), ("U_L", sp.Rational(1, 2))):
    cell = next(cell for cell in cells if cell["name"] == name)
    grid_error = 0.0
    for kval in momentum_grid:
        actual = np.linalg.eigvals(bloch_matrix(cell, np.exp(1j * kval)))
        base = np.exp(1j * float(exponent) * kval)
        expected = np.array([base, -base], dtype=complex)
        grid_error = max(grid_error, unordered_pair_error(actual, expected))
    omega = exponent * K
    slope = sp.diff(omega, K)
    curvature = sp.diff(omega, K, 2)
    edge_speed = sp.simplify(2 * abs(slope))
    mover_band_rows.append((name, slope, edge_speed, curvature, grid_error))

print("mover   cell_slope   edge_speed   curvature   max_grid_band_error")
for name, slope, edge_speed, curvature, grid_error in mover_band_rows:
    print(f"{name:<7} {slope!s:<12} {edge_speed!s:<12} {curvature!s:<11} {grid_error:.3e}")

flat_names = ("EXCHANGE", "PAIRING", "UMIX")
flat_variations = {}
for name in flat_names:
    cell = next(cell for cell in cells if cell["name"] == name)
    reference = np.linalg.eigvals(bloch_matrix(cell, np.exp(1j * momentum_grid[0])))
    variation = 0.0
    for kval in momentum_grid[1:]:
        actual = np.linalg.eigvals(bloch_matrix(cell, np.exp(1j * kval)))
        variation = max(variation, unordered_pair_error(actual, reference))
    flat_variations[name] = variation
print("flat-cell spectral variation over momentum grid:")
for name in flat_names:
    print(f"  {name:<10} {flat_variations[name]:.3e}")

check(
    "mover momentum-grid spectra match exactly linear half-cell-slope bands",
    max(row[4] for row in mover_band_rows) < 1e-12,
    f"max grid error={max(row[4] for row in mover_band_rows):.3e}",
)
check(
    "symbolic mover slopes compute one edge per tick with zero curvature",
    all(abs(row[1]) == sp.Rational(1, 2) and row[2] == 1 and row[3] == 0 for row in mover_band_rows),
    "cell slopes=-1/2,+1/2; edge speed=1; curvature=0",
)
check(
    "EXCHANGE, PAIRING, and UMIX momentum-grid bands compute flat",
    max(flat_variations.values()) < 1e-12,
    f"spectral variations={flat_variations}",
)


# ---------------------------------------------------------------------------
section("S9", "refutation legs R1 and R2")

variation_only, variation_rows = clause_filter(
    cell_entries, require_translation=np.array([0]).sum() > 0,
    require_variation=np.array([1]).sum() == 1,
)
translation_only, translation_rows = clause_filter(
    cell_entries, require_translation=np.array([1]).sum() == 1,
    require_variation=np.array([0]).sum() > 0,
)
flat_inventory = {"DIAGONAL", "EXCHANGE", "PAIRING", "UMIX"}
flat_variation_survivors = set(variation_only) & flat_inventory
print(f"R1 variation-only survivors: {variation_only}")
print(f"R1 flat variation-only survivors: {sorted(flat_variation_survivors)}")
print(f"R2 translation-only survivors: {translation_only}")

check(
    "R1 conditioning-only filter retains both movers and all three conditioned flat cells",
    set(variation_only) == {"U_R", "U_L", "EXCHANGE", "PAIRING", "UMIX"},
    f"survivors={variation_only}",
)
check(
    "R1 variation-only filter computes at least one flat survivor",
    len(flat_variation_survivors) > 0,
    f"flat survivors={sorted(flat_variation_survivors)}",
)
check(
    "R2 translation-only filter retains DIAGONAL and both movers",
    set(translation_only) == {"DIAGONAL", "U_R", "U_L"},
    f"survivors={translation_only}",
)
check(
    "R2 translation-only filter computes survival of the vacuous DIAGONAL cell",
    "DIAGONAL" in translation_only and not site_conditioning["DIAGONAL"],
    "DIAGONAL survives and its site-level conditioning is false",
)


# ---------------------------------------------------------------------------
section("S10", "rejector legs R3 and R4")

u_r = next(cell for cell in cells if cell["name"] == "U_R")
perturbed_residual = torus_unitarity_residual(u_r, scale_q=0.9)
perturbed_unitary = perturbed_residual < 1e-12

exchange = next(cell for cell in cells if cell["name"] == "EXCHANGE")
wrong_entries = [
    ("EXCHANGE", exchange) if label == "U_R" else (label, cell)
    for label, cell in cell_entries
]
wrong_survivors, wrong_rows = clause_filter(
    wrong_entries, require_translation=np.array([1]).sum() == 1,
    require_variation=np.array([1]).sum() == 1,
)

print(f"R3 perturbed U_R torus-unitarity residual: {perturbed_residual:.12f}")
print(f"R3 perturbed U_R classified unitary: {perturbed_unitary}")
print("R4 wrong-inventory filter rows:")
for name, translation_ok, variation_ok, survives in wrong_rows:
    print(f"  {name:<10} translation={translation_ok} variation={variation_ok} survives={survives}")
print(f"R4 wrong-inventory survivors: {wrong_survivors}")

check(
    "R3 amplitude-0.9 U_R perturbation fails torus unitarity",
    not perturbed_unitary and perturbed_residual > 1e-3,
    f"max residual={perturbed_residual:.12f}",
)
check(
    "R4 replacing U_R by EXCHANGE changes the computed two-clause survivors",
    set(wrong_survivors) != {"U_R", "U_L"} and set(wrong_survivors) == {"U_L"},
    f"wrong survivors={wrong_survivors}",
)


# ---------------------------------------------------------------------------
section("S11", "phase-uniformizability of both movers")


def directed_shift_matrix(hops, source_offset):
    matrix = np.zeros((L, L), dtype=complex)
    for target in range(L):
        matrix[target, (target + source_offset) % L] = hops[target]
    return matrix


def uniformizing_gauge(hops, source_offset):
    product = np.prod(hops)
    product_unit = product / abs(product)
    global_phase = np.exp(1j * np.angle(product_unit) / L)
    diagonal = np.ones(L, dtype=complex)
    if source_offset == -1:
        for target in range(1, L):
            diagonal[target] = global_phase * diagonal[target - 1] / hops[target]
    elif source_offset == 1:
        for target in range(0, L - 1):
            diagonal[target + 1] = diagonal[target] * hops[target] / global_phase
    else:
        raise ValueError("source_offset must be one edge")
    diagonal /= np.abs(diagonal)
    return np.diag(diagonal), global_phase, product_unit


rng_phase = np.random.default_rng(20260710)
phase_probe_rows = []
for seed_index in range(3):
    q_phase, r_phase, p_phase, s_phase = np.exp(
        1j * rng_phase.uniform(-np.pi, np.pi, size=4)
    )
    for name, source_offset, even_hop, odd_hop in (
        ("U_R", -1, q_phase, r_phase),
        ("U_L", 1, p_phase, s_phase),
    ):
        hops = np.array([even_hop if target % 2 == 0 else odd_hop for target in range(L)])
        matrix = directed_shift_matrix(hops, source_offset)
        gauge, global_phase, product_unit = uniformizing_gauge(hops, source_offset)
        gauged = gauge @ matrix @ gauge.conj().T
        hop_values = np.array(
            [gauged[target, (target + source_offset) % L] for target in range(L)]
        )
        uniform_error = float(np.max(np.abs(hop_values - global_phase)))
        covariance_error = float(np.max(np.abs(T @ gauged @ T.conj().T - gauged)))
        product_error = float(abs(global_phase**L - product_unit))
        phase_probe_rows.append(
            (name, seed_index, np.angle(global_phase), product_error, uniform_error, covariance_error)
        )

print("mover   seed   global_phase_arg   product_error   uniform_hop_error   full_covariance_error")
for name, seed_index, global_arg, product_error, uniform_error, covariance_error in phase_probe_rows:
    print(
        f"{name:<7} {seed_index:<4d}   {global_arg:+.12f}    {product_error:.3e}       "
        f"{uniform_error:.3e}             {covariance_error:.3e}"
    )
print("ring condition: L=8 is even; the computed global phase obeys g^L=product(hop phases)")

check(
    "three random phase seeds per mover satisfy the cyclic product condition",
    max(row[3] for row in phase_probe_rows) < 1e-12,
    f"max product error={max(row[3] for row in phase_probe_rows):.3e}",
)
check(
    "explicit local phase gauges make every mover hop phase uniform",
    max(row[4] for row in phase_probe_rows) < 1e-12,
    f"max uniform-hop error={max(row[4] for row in phase_probe_rows):.3e}",
)
check(
    "gauged mover matrices compute full one-site translation covariance",
    max(row[5] for row in phase_probe_rows) < 1e-12,
    f"max covariance error={max(row[5] for row in phase_probe_rows):.3e}",
)


print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(0 if FAIL == 0 else 1)
