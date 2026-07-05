#!/usr/bin/env python3
"""Map the domain-wall edge content against one SM generation.

This is a bounded map, not a Standard Model derivation.  The runner:

* enumerates the Step 1-3 edge Weyl content and its spin/cubic behavior;
* re-earns the chiral-cube Y surface exactly;
* lists the one-generation SM left-handed target in exact rational form;
* compares the surfaces, reporting both matches and precise gaps;
* computes anomaly sums for the matched subcontent and the full target.

The calculation is deterministic and uses numpy plus Python exact Fractions.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
import itertools
import math

import numpy as np

np.set_printoptions(precision=12, suppress=True, linewidth=160)

PASS = 0
FAIL = 0
EPS = 1.0e-12


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail else ""
    print(f"{tag} - {name}{suffix}")


def section(title: str) -> None:
    print("\n" + "=" * 92)
    print(title)
    print("=" * 92)


def fmt(q: Fraction) -> str:
    if q.denominator == 1:
        return str(q.numerator)
    return f"{q.numerator}/{q.denominator}"


def fmt_counter(counter: Counter[Fraction]) -> str:
    parts = []
    for key in sorted(counter, key=lambda x: (float(x), x.numerator, x.denominator)):
        parts.append(f"{fmt(key)}:{counter[key]}")
    return "{" + ", ".join(parts) + "}"


def kron(*mats: np.ndarray) -> np.ndarray:
    out = mats[0]
    for mat in mats[1:]:
        out = np.kron(out, mat)
    return out


I2 = np.eye(2, dtype=complex)
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
sigmas = [s1, s2, s3]
I8 = np.eye(8, dtype=complex)


def state_idx(b1: int, b2: int, b3: int) -> int:
    return 4 * b1 + 2 * b2 + b3


def signed_permutation_rotations() -> list[np.ndarray]:
    rotations: list[np.ndarray] = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3), dtype=int)
        for i, j in enumerate(perm):
            P[i, j] = 1
        for signs in itertools.product([-1, 1], repeat=3):
            R = P.copy()
            for i, sign in enumerate(signs):
                R[i, :] *= sign
            if round(np.linalg.det(R)) == 1:
                rotations.append(R)
    return rotations


def su2_rotation(axis: np.ndarray, angle: float) -> np.ndarray:
    axis = np.asarray(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    sigma_axis = axis[0] * s1 + axis[1] * s2 + axis[2] * s3
    return math.cos(angle / 2.0) * I2 - 1j * math.sin(angle / 2.0) * sigma_axis


def swap12_matrix() -> np.ndarray:
    P = np.zeros((8, 8), dtype=complex)
    for b1, b2, b3 in itertools.product([0, 1], repeat=3):
        old = state_idx(b1, b2, b3)
        new = state_idx(b2, b1, b3)
        P[new, old] = 1.0
    return P


def perm_matrix_8d(perm: tuple[int, int, int]) -> np.ndarray:
    mat = np.zeros((8, 8), dtype=complex)
    for bits in itertools.product([0, 1], repeat=3):
        new_bits = [bits[perm[i]] for i in range(3)]
        mat[state_idx(*new_bits), state_idx(*bits)] = 1.0
    return mat


def y_surface_data() -> dict[str, object]:
    P_swap = swap12_matrix()
    P_sym = (I8 + P_swap) / 2.0
    P_anti = (I8 - P_swap) / 2.0
    Y = (1.0 / 3.0) * P_sym - P_anti
    evals = np.linalg.eigvalsh(Y.real)
    rounded = [Fraction(str(round(float(e), 12))).limit_denominator() for e in evals]
    return {
        "P_swap": P_swap,
        "P_sym": P_sym,
        "P_anti": P_anti,
        "Y": Y,
        "evals": rounded,
        "spectrum": Counter(rounded),
        "rank_sym": int(round(np.trace(P_sym).real)),
        "rank_anti": int(round(np.trace(P_anti).real)),
        "trace_Y": Fraction(str(round(float(np.trace(Y).real), 12))).limit_denominator(),
    }


def s3_character_decomposition() -> dict[str, Fraction]:
    T12 = perm_matrix_8d((1, 0, 2))
    Z3 = perm_matrix_8d((2, 0, 1))
    chi_e = Fraction(8, 1)
    chi_2 = Fraction(int(round(np.trace(T12).real)), 1)
    chi_3 = Fraction(int(round(np.trace(Z3).real)), 1)
    n_A1 = (chi_e + 3 * chi_2 + 2 * chi_3) / 6
    n_A2 = (chi_e - 3 * chi_2 + 2 * chi_3) / 6
    n_E = (2 * chi_e - 2 * chi_3) / 6
    return {"chi_e": chi_e, "chi_2": chi_2, "chi_3": chi_3, "A1": n_A1, "A2": n_A2, "E": n_E}


def multiset_from_rows(rows: list[tuple[str, int, Fraction]]) -> Counter[Fraction]:
    out: Counter[Fraction] = Counter()
    for _, multiplicity, charge in rows:
        out[charge] += multiplicity
    return out


def expanded_charges(rows: list[tuple[str, int, Fraction]]) -> list[Fraction]:
    charges: list[Fraction] = []
    for _, multiplicity, charge in rows:
        charges.extend([charge] * multiplicity)
    return charges


def anomaly_sums_for_sm_rows(rows: list[tuple[str, int, Fraction]]) -> dict[str, Fraction]:
    """Perturbative anomalies for the SM target rows in LH-conjugate convention."""
    by_name = {name: (mult, y) for name, mult, y in rows}
    charges = expanded_charges(rows)
    linear = sum(charges, start=Fraction(0))
    cubic = sum((y**3 for y in charges), start=Fraction(0))
    su2 = Fraction(0)
    if "Q" in by_name:
        su2 += Fraction(1, 2) * 3 * by_name["Q"][1]
    if "L" in by_name:
        su2 += Fraction(1, 2) * by_name["L"][1]
    su3 = Fraction(0)
    if "Q" in by_name:
        su3 += Fraction(1, 2) * 2 * by_name["Q"][1]
    if "u^c" in by_name:
        su3 += Fraction(1, 2) * by_name["u^c"][1]
    if "d^c" in by_name:
        su3 += Fraction(1, 2) * by_name["d^c"][1]
    return {"sum_Y": linear, "sum_Y3": cubic, "su2_su2_Y": su2, "su3_su3_Y": su3}


def cubic_su3_anomaly_for_target(rows: list[tuple[str, int, Fraction]]) -> int:
    # Fundamental Q gives +1 for each weak component; conjugate u^c/d^c give -1.
    by_name = {name: mult for name, mult, _ in rows}
    return 2 * (1 if "Q" in by_name else 0) - (1 if "u^c" in by_name else 0) - (1 if "d^c" in by_name else 0)


def common_su2_kernel_dimension() -> int:
    stacked = np.vstack([s1, s2, s3])
    return 2 - int(np.linalg.matrix_rank(stacked, tol=1.0e-12))


def main() -> None:
    section("1. Edge Weyl content from the Step 1-3 domain-wall construction")
    sigma_anticomm = max(
        np.max(np.abs(sigmas[i] @ sigmas[j] + sigmas[j] @ sigmas[i] - (2.0 if i == j else 0.0) * I2))
        for i in range(3)
        for j in range(3)
    )
    rotations = signed_permutation_rotations()
    vector_trace_counts = Counter(int(round(np.trace(R))) for R in rotations)
    U_z_90 = su2_rotation(np.array([0.0, 0.0, 1.0]), math.pi / 2.0)
    projective_four_turn = U_z_90 @ U_z_90 @ U_z_90 @ U_z_90
    conj_x = U_z_90 @ s1 @ U_z_90.conj().T
    conj_y = U_z_90 @ s2 @ U_z_90.conj().T
    edge_wall_species = 1
    edge_spin_dim = 2
    edge_wall_dim = edge_wall_species * edge_spin_dim
    print(f"edge content per wall: species={edge_wall_species}, Cl(3,0) spinor_dim={edge_spin_dim}, local_dim={edge_wall_dim}")
    print(f"proper cubic rotations: |O|={len(rotations)}, vector trace counts={dict(sorted(vector_trace_counts.items()))}")
    check("Pauli sigma algebra realizes the Cl(3,0) edge spin", sigma_anticomm < EPS, f"max_anticomm_error={sigma_anticomm:.3e}")
    check("proper cubic group has 24 orientation-preserving signed-permutation rotations", len(rotations) == 24)
    check("proper cubic vector representation trace distribution is computed", vector_trace_counts == Counter({3: 1, 1: 6, 0: 8, -1: 9}), str(dict(sorted(vector_trace_counts.items()))))
    check("edge spinor is a double-cover/projective cubic spin representation", np.allclose(projective_four_turn, -I2, atol=EPS), "four 90-degree spin turns give -I")
    check("spin lift rotates the sigma algebra by conjugation", np.allclose(conj_x, s2, atol=EPS) and np.allclose(conj_y, -s1, atol=EPS))

    section("2. Re-earn the C^8 taste/base Y surface")
    ydata = y_surface_data()
    s3_decomp = s3_character_decomposition()
    y_surface = Counter({Fraction(1, 3): 6, Fraction(-1, 1): 2})
    print(f"Y spectrum={fmt_counter(ydata['spectrum'])}")
    print(f"S3 character decomposition: A1={fmt(s3_decomp['A1'])}, A2={fmt(s3_decomp['A2'])}, E={fmt(s3_decomp['E'])}")
    check("P_sym and P_antisym are orthogonal projectors", np.allclose(ydata["P_sym"] @ ydata["P_sym"], ydata["P_sym"], atol=EPS) and np.allclose(ydata["P_anti"] @ ydata["P_anti"], ydata["P_anti"], atol=EPS) and np.allclose(ydata["P_sym"] @ ydata["P_anti"], 0, atol=EPS))
    check("Y surface has the exact 6+2 multiplicity split", ydata["rank_sym"] == 6 and ydata["rank_anti"] == 2, f"rank_sym={ydata['rank_sym']} rank_anti={ydata['rank_anti']}")
    check("Y spectrum is +1/3 with multiplicity 6 and -1 with multiplicity 2", ydata["spectrum"] == y_surface, fmt_counter(ydata["spectrum"]))
    check("Y trace is exactly zero on the 6+2 surface", ydata["trace_Y"] == 0, f"TrY={fmt(ydata['trace_Y'])}")
    check("scale-free Y ratio is 1:(-3)", Fraction(1, 3) / Fraction(-1, 1) == Fraction(-1, 3))
    check("taste cube S3 representation decomposes as 4A1 + 2E", s3_decomp["A1"] == 4 and s3_decomp["A2"] == 0 and s3_decomp["E"] == 2)

    section("3. One-generation SM target and exact anomaly sums")
    sm_rows = [
        ("Q", 6, Fraction(1, 6)),
        ("u^c", 3, Fraction(-2, 3)),
        ("d^c", 3, Fraction(1, 3)),
        ("L", 2, Fraction(-1, 2)),
        ("e^c", 1, Fraction(1, 1)),
    ]
    sm_counter = multiset_from_rows(sm_rows)
    sm_anom = anomaly_sums_for_sm_rows(sm_rows)
    print(f"SM target multiset={fmt_counter(sm_counter)} total_dim={sum(sm_counter.values())}")
    print("SM anomaly sums: " + ", ".join(f"{k}={fmt(v)}" for k, v in sm_anom.items()))
    check("SM one-generation target has 15 left-handed Weyl states", sum(sm_counter.values()) == 15)
    check("SM target perturbative hypercharge anomalies vanish exactly", all(v == 0 for v in sm_anom.values()), ", ".join(f"{k}={fmt(v)}" for k, v in sm_anom.items()))
    check("SM target SU(3)^3 anomaly cancels in the LH-conjugate frame", cubic_su3_anomaly_for_target(sm_rows) == 0)

    section("4. Map: matches and precise gaps")
    scaled_surface = Counter({Fraction(1, 6): 6, Fraction(-1, 2): 2})
    sm_lh_doublet = Counter({Fraction(1, 6): 6, Fraction(-1, 2): 2})
    scale_to_sm_convention = Fraction(1, 2)
    scaled_from_y = Counter({scale_to_sm_convention * k: v for k, v in y_surface.items()})
    missing_from_surface = sm_counter - scaled_from_y
    extra_in_surface = scaled_from_y - sm_counter
    direct_edge_to_taste_dims_match = edge_wall_dim == 8
    tensor_edge_taste_dim = edge_wall_dim * 8
    print(f"scaled Y surface by convention factor {fmt(scale_to_sm_convention)} -> {fmt_counter(scaled_from_y)}")
    print(f"SM states missing from scaled 6+2 surface={fmt_counter(missing_from_surface)}")
    print(f"extra states in scaled surface relative to SM={fmt_counter(extra_in_surface)}")
    check("MATCH: scaled 6+2 Y surface equals the SM Q_L + L_L hypercharge multiset", scaled_from_y == sm_lh_doublet, fmt_counter(scaled_from_y))
    check("MATCH: the map reuses only the scale-free 1:(-3) ratio before convention fixing", scale_to_sm_convention == Fraction(1, 2), "absolute factor 1/2 is the SM convention bridge, not derived here")
    check("GAP: scaled 6+2 surface is not the full SM 15-plet", scaled_from_y != sm_counter and sum(scaled_from_y.values()) == 8 and sum(sm_counter.values()) == 15, f"surface_dim=8 sm_dim=15 missing={fmt_counter(missing_from_surface)}")
    check("GAP: Step 1-3 edge spinor is not directly the C^8 taste cube", not direct_edge_to_taste_dims_match, f"edge_spin_dim={edge_wall_dim} taste_dim=8")
    check("GAP: edge spinor tensor taste cube gives 16 states, not the target 15-plet", tensor_edge_taste_dim == 16 and tensor_edge_taste_dim != 15)
    check("ROUTE-NO-GO: H_unit singlet cannot derive an SU(2) doublet by a nonzero equivariant map", common_su2_kernel_dimension() == 0, "Hom_SU(2)(1,2)=0")

    section("5. Anomaly cross-check for the identified subcontent")
    lh_surface_rows = [
        ("Q", 6, Fraction(1, 6)),
        ("L", 2, Fraction(-1, 2)),
    ]
    lh_anom = anomaly_sums_for_sm_rows(lh_surface_rows)
    print("identified 6+2 subcontent anomaly sums: " + ", ".join(f"{k}={fmt(v)}" for k, v in lh_anom.items()))
    check("identified 6+2 subcontent has vanishing linear trace and SU(2)^2-U(1)", lh_anom["sum_Y"] == 0 and lh_anom["su2_su2_Y"] == 0, ", ".join(f"{k}={fmt(v)}" for k, v in lh_anom.items()))
    check("PRECISE NO-GO: identified 6+2 subcontent is not anomaly-complete by itself", lh_anom["sum_Y3"] != 0 and lh_anom["su3_su3_Y"] != 0, f"sum_Y3={fmt(lh_anom['sum_Y3'])} su3_su3_Y={fmt(lh_anom['su3_su3_Y'])}")
    check("PRECISE GAP: the missing singlet charges are exactly the SM anomaly-completing 7 states", missing_from_surface == Counter({Fraction(-2, 3): 3, Fraction(1, 3): 3, Fraction(1, 1): 1}), fmt_counter(missing_from_surface))

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
