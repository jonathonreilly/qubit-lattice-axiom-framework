"""Class-A runner for admissibility-rule covariance-extension classification.

Sections:
A. group structure
B. Burnside classification of condition patterns
C. sign channel on the chiral orbit
D. antilinear value twist and pairing law
E. dichotomy and theta-seed transport

Expected close: TOTAL: PASS=20 FAIL=0
"""

import itertools
import numpy as np


PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if bool(cond):
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def det3(M):
    return int(
        M[0, 0] * (M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
        - M[0, 1] * (M[1, 0] * M[2, 2] - M[1, 2] * M[2, 0])
        + M[0, 2] * (M[1, 0] * M[2, 1] - M[1, 1] * M[2, 0])
    )


def mat_key(M):
    return tuple(int(x) for x in M.reshape(-1))


DIRS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
DIR_INDEX = {d: i for i, d in enumerate(DIRS)}


def dperm(M):
    perm = []
    for d in DIRS:
        image = tuple(int(x) for x in M @ np.array(d, dtype=int))
        perm.append(DIR_INDEX[image])
    return tuple(perm)


def act_col(perm, col):
    out = [None] * len(col)
    for i, j in enumerate(perm):
        out[j] = col[i]
    return tuple(out)


def inv_perm(perm):
    out = [None] * len(perm)
    for i, j in enumerate(perm):
        out[j] = i
    return tuple(out)


records = []
seen_mats = set()
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((-1, 1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for row, col in enumerate(perm):
            M[row, col] = signs[row]
        key = mat_key(M)
        if key not in seen_mats:
            seen_mats.add(key)
            records.append({"M": M, "key": key, "det": det3(M), "perm": dperm(M)})

mats = [r["M"] for r in records]
proper_records = [r for r in records if r["det"] == 1]
full_perms = [r["perm"] for r in records]
proper_perms = [r["perm"] for r in proper_records]
I = np.eye(3, dtype=int)
P = -I
P_key = mat_key(P)
P_perm = dperm(P)


def cycle_count(perm):
    seen = [False] * len(perm)
    cycles = 0
    for start in range(len(perm)):
        if not seen[start]:
            cycles += 1
            here = start
            while not seen[here]:
                seen[here] = True
                here = perm[here]
    return cycles


def burnside_orbits(perms, k):
    total = sum(k ** cycle_count(perm) for perm in perms)
    assert total % len(perms) == 0
    return total // len(perms)


def all_colorings(k):
    return list(itertools.product(range(k), repeat=len(DIRS)))


def direct_orbits(perms, k):
    unseen = set(all_colorings(k))
    orbits = []
    while unseen:
        seed = min(unseen)
        orbit = {act_col(perm, seed) for perm in perms}
        orbits.append(orbit)
        unseen -= orbit
    return orbits


def orbit_ids(orbits):
    return {col: i for i, orbit in enumerate(orbits) for col in orbit}


def proper_equiv_to_p_image(col):
    p_col = act_col(P_perm, col)
    return any(act_col(perm, col) == p_col for perm in proper_perms)


def chiral_pairs(proper_orbits):
    ids = orbit_ids(proper_orbits)
    pairs = []
    seen = set()
    for i, orbit in enumerate(proper_orbits):
        image_id = ids[act_col(P_perm, next(iter(orbit)))]
        if image_id != i:
            pair = tuple(sorted((i, image_id)))
            if pair not in seen:
                seen.add(pair)
                pairs.append(pair)
    return pairs


def frame_sign(col):
    rows = []
    for color in (1, 2, 3):
        positions = [i for i, value in enumerate(col) if value == color]
        if len(positions) != 1:
            return 0
        rows.append(DIRS[positions[0]])
    return det3(np.array(rows, dtype=int))


def frame_from_col(col):
    rows = []
    for color in (1, 2, 3):
        positions = [i for i, value in enumerate(col) if value == color]
        assert len(positions) == 1
        rows.append(DIRS[positions[0]])
    return tuple(rows)


def transform_value(R, perm, det, col, twisted=True):
    value = R(act_col(inv_perm(perm), col))
    if twisted and det == -1:
        value = np.conjugate(value)
    return value


central = all(np.array_equal(P @ M, M @ P) for M in mats)
check(
    "A1 inversion central",
    len(records) == len(seen_mats) and P_key in seen_mats and central,
    f"generated={len(records)}; det(P)={det3(P)}",
)

check(
    "A2 direction action faithful",
    len(set(full_perms)) == len(records),
    f"distinct direction permutations={len(set(full_perms))}",
)

check(
    "A3 inversion outside proper image",
    P_perm not in set(proper_perms),
    f"proper image size={len(set(proper_perms))}; P_perm={P_perm}",
)

factorizations = {}
for g_plus in proper_records:
    for eps in (0, 1):
        factor = g_plus["M"] @ (P if eps else I)
        key = mat_key(factor)
        if key not in factorizations:
            factorizations[key] = []
        factorizations[key].append((g_plus["key"], eps))

check(
    "A4 proper-times-inversion factorization",
    set(factorizations) == seen_mats and all(len(v) == 1 for v in factorizations.values()),
    f"factorized={len(factorizations)}; proper={len(proper_records)}",
)

b2_proper = burnside_orbits(proper_perms, 2)
b2_full = burnside_orbits(full_perms, 2)
d2_proper = direct_orbits(proper_perms, 2)
d2_full = direct_orbits(full_perms, 2)
all_binary_p_related = all(proper_equiv_to_p_image(col) for col in all_colorings(2))
check(
    "B1 openness patterns achiral",
    b2_proper == b2_full
    and len(d2_proper) == b2_proper
    and len(d2_full) == b2_full
    and all_binary_p_related,
    (
        f"Burnside proper/full={b2_proper}/{b2_full}; "
        f"direct proper/full={len(d2_proper)}/{len(d2_full)}; "
        f"p-related={sum(1 for col in all_colorings(2) if proper_equiv_to_p_image(col))}"
    ),
)

b3_proper = burnside_orbits(proper_perms, 3)
b3_full = burnside_orbits(full_perms, 3)
diff3 = b3_proper - b3_full
d3_proper = direct_orbits(proper_perms, 3)
d3_full = direct_orbits(full_perms, 3)
ids3 = orbit_ids(d3_proper)
not_p_related3 = [col for col in all_colorings(3) if not proper_equiv_to_p_image(col)]
not_p_orbits3 = sorted({ids3[col] for col in not_p_related3})
pairs3 = chiral_pairs(d3_proper)
sizes3 = [len(d3_proper[i]) for i in not_p_orbits3]
rep3 = min(d3_proper[not_p_orbits3[0]])
rep3_axis_mixed = all(rep3[2 * axis] != rep3[2 * axis + 1] for axis in range(3))
rep3_color_counts = sorted(rep3.count(color) for color in range(3))
check(
    "B2 ternary chiral pair count",
    diff3 == 1
    and len(d3_proper) == b3_proper
    and len(d3_full) == b3_full
    and len(not_p_related3) > 0
    and len(not_p_orbits3) == 2
    and len(pairs3) == diff3
    and rep3_axis_mixed
    and rep3_color_counts == [2, 2, 2],
    (
        f"Burnside proper/full={b3_proper}/{b3_full}; "
        f"difference={diff3}; direct chiral orbit sizes={sizes3}; "
        f"representative={rep3} (every axis bi-colored, every color used twice)"
    ),
)

b4_proper = burnside_orbits(proper_perms, 4)
b4_full = burnside_orbits(full_perms, 4)
diff4 = b4_proper - b4_full
d4_proper = direct_orbits(proper_perms, 4)
d4_full = direct_orbits(full_perms, 4)
ids4 = orbit_ids(d4_proper)
pairs4 = chiral_pairs(d4_proper)
check(
    "B3 quaternary chiral pair count",
    diff4 > 1
    and len(d4_proper) == b4_proper
    and len(d4_full) == b4_full
    and len(pairs4) == diff4,
    (
        f"Burnside proper/full={b4_proper}/{b4_full}; "
        f"difference={diff4}; direct chiral pairs={len(pairs4)}"
    ),
)

witness = (1, 0, 2, 0, 3, 0)
p_witness = act_col(P_perm, witness)
witness_orbit_id = ids4[witness]
witness_pair = [pair for pair in pairs4 if witness_orbit_id in pair]
check(
    "B4 oriented frame witness membership",
    len(witness_pair) == 1 and frame_sign(witness) == 1,
    f"witness={witness}; k=4 orbit pair={witness_pair[0] if witness_pair else None}",
)

proper_maps_witness_to_p = [perm for perm in proper_perms if act_col(perm, witness) == p_witness]
check(
    "B5 witness P-image separation",
    len(proper_maps_witness_to_p) == 0,
    f"proper maps found={len(proper_maps_witness_to_p)}",
)

full_witness_orbit = {act_col(perm, witness) for perm in full_perms}
proper_witness_orbit = {act_col(perm, witness) for perm in proper_perms}
proper_p_witness_orbit = {act_col(perm, p_witness) for perm in proper_perms}
frame_sign_proper_fixed = all(
    frame_sign(act_col(perm, col)) == frame_sign(col)
    for perm in proper_perms
    for col in full_witness_orbit
)
check(
    "C1 frame_sign proper split",
    len(full_witness_orbit) == len(full_perms)
    and proper_witness_orbit.isdisjoint(proper_p_witness_orbit)
    and proper_witness_orbit | proper_p_witness_orbit == full_witness_orbit
    and all(frame_sign(col) == 1 for col in proper_witness_orbit)
    and all(frame_sign(col) == -1 for col in proper_p_witness_orbit)
    and frame_sign_proper_fixed,
    (
        f"full orbit={len(full_witness_orbit)}; "
        f"proper split={len(proper_witness_orbit)}/{len(proper_p_witness_orbit)}"
    ),
)

orbit_list = sorted(full_witness_orbit)
orbit_index = {col: i for i, col in enumerate(orbit_list)}


def transform_function_vector(vec, perm):
    inv = inv_perm(perm)
    return np.array([vec[orbit_index[act_col(inv, col)]] for col in orbit_list], dtype=float)


def average_under_proper(vec):
    out = np.zeros(len(orbit_list), dtype=float)
    for perm in proper_perms:
        out += transform_function_vector(vec, perm)
    return out / len(proper_perms)


projector_columns = []
for col_index in range(len(orbit_list)):
    basis = np.zeros(len(orbit_list), dtype=float)
    basis[col_index] = 1.0
    projector_columns.append(average_under_proper(basis))
proper_projector = np.column_stack(projector_columns)
projector_rank = np.linalg.matrix_rank(proper_projector, tol=1e-9)
ind_witness = np.array([1.0 if col in proper_witness_orbit else 0.0 for col in orbit_list])
ind_p_witness = np.array([1.0 if col in proper_p_witness_orbit else 0.0 for col in orbit_list])
sign_vec = np.array([float(frame_sign(col)) for col in orbit_list])
odd_witness = 0.5 * (ind_witness - transform_function_vector(ind_witness, P_perm))
odd_p_witness = 0.5 * (ind_p_witness - transform_function_vector(ind_p_witness, P_perm))
avg_odd_witness = average_under_proper(odd_witness)
avg_odd_p_witness = average_under_proper(odd_p_witness)
sign_norm = float(np.dot(sign_vec, sign_vec))
factor_witness = float(np.dot(avg_odd_witness, sign_vec) / sign_norm)
factor_p_witness = float(np.dot(avg_odd_p_witness, sign_vec) / sign_norm)
check(
    "C2 chiral orbit odd channel dimension",
    projector_rank == 2
    and np.allclose(average_under_proper(ind_witness), ind_witness)
    and np.allclose(average_under_proper(ind_p_witness), ind_p_witness)
    and np.allclose(avg_odd_witness, factor_witness * sign_vec)
    and np.allclose(avg_odd_p_witness, factor_p_witness * sign_vec)
    and factor_witness != 0.0
    and factor_witness == -factor_p_witness,
    f"proper-invariant rank={projector_rank}; P-odd factors={factor_witness},{factor_p_witness}",
)

sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)


def spin_flip(X):
    return sigma2 @ np.conjugate(X) @ sigma2


alpha = 1 + 2j
beta = -3 + 1j
X = sigma1 + 2 * sigma2
Y = sigma3 - sigma1
check(
    "D0 antilinear value premise",
    all(np.allclose(spin_flip(sigma), -sigma) for sigma in (sigma1, sigma2, sigma3))
    and np.allclose(spin_flip(alpha * X + beta * Y), np.conjugate(alpha) * spin_flip(X) + np.conjugate(beta) * spin_flip(Y)),
    "Pauli generators map to their negatives; scalar coefficients conjugate",
)


def R0(col):
    return 1j * frame_sign(col)


def R1(col):
    return frame_sign(col)


check(
    "D1 twisted imaginary sign invariant",
    all(
        np.allclose(transform_value(R0, rec["perm"], rec["det"], col, twisted=True), R0(col))
        for rec in records
        for col in full_witness_orbit
    ),
    f"group elements checked={len(records)}; orbit size={len(full_witness_orbit)}",
)

check(
    "D2 real sign determinant character",
    all(
        np.allclose(transform_value(R1, rec["perm"], rec["det"], col, twisted=True), rec["det"] * R1(col))
        for rec in records
        for col in full_witness_orbit
    ),
    f"group elements checked={len(records)}; orbit size={len(full_witness_orbit)}",
)

r0_real_zero = all(np.real(R0(col)) == 0 for col in full_witness_orbit)
r0_imag_nonzero = [col for col in orbit_list if np.imag(R0(col)) != 0]
check(
    "D3 achiral scalar readout zero",
    r0_real_zero and len(r0_imag_nonzero) > 0,
    f"nonzero imaginary example={r0_imag_nonzero[0] if r0_imag_nonzero else None}",
)

check(
    "D4 twist load-bearing",
    all(np.allclose(transform_value(R0, P_perm, det3(P), col, twisted=False), -R0(col)) for col in full_witness_orbit)
    and any(not np.allclose(transform_value(R0, P_perm, det3(P), col, twisted=False), R0(col)) for col in full_witness_orbit),
    f"P under untwisted action sends R0 to -R0 on {len(full_witness_orbit)} colorings",
)


def P_R1(col):
    return transform_value(R1, P_perm, det3(P), col, twisted=True)


check(
    "E1 chiral rule pair exchange",
    all(
        np.allclose(transform_value(R1, rec["perm"], rec["det"], col, twisted=True), R1(col))
        for rec in proper_records
        for col in full_witness_orbit
    )
    and all(
        np.allclose(transform_value(P_R1, rec["perm"], rec["det"], col, twisted=True), P_R1(col))
        for rec in proper_records
        for col in full_witness_orbit
    )
    and any(not np.allclose(R1(col), P_R1(col)) for col in full_witness_orbit)
    and all(np.allclose(P_R1(col), -R1(col)) for col in full_witness_orbit)
    and all(
        np.allclose(transform_value(P_R1, P_perm, det3(P), col, twisted=True), R1(col))
        for col in full_witness_orbit
    ),
    "proper-fixed pair is distinct and exchanged by inversion",
)


def frame_orientation(frame):
    return det3(np.array(frame, dtype=int))


def density_for_frame(draw, frame):
    e = np.array(draw[:3], dtype=int)
    raw_b = np.array(draw[3:], dtype=int)
    b_frame = frame_orientation(frame) * raw_b
    return int(np.dot(e, b_frame))


witness_frame = frame_from_col(witness)
p_witness_frame = frame_from_col(p_witness)
s_witness = R1(witness)
s_p_witness = R1(p_witness)
rng = np.random.default_rng(3)
draws50 = rng.integers(-5, 6, size=(50, 6))
base_D50 = [density_for_frame(draw, witness_frame) for draw in draws50]
p_D50 = [density_for_frame(draw, p_witness_frame) for draw in draws50]
nonzero_D50 = sum(1 for value in base_D50 if value != 0)
check(
    "E2 theta seed transport",
    frame_orientation(witness_frame) == s_witness
    and frame_orientation(p_witness_frame) == s_p_witness
    and all(s_witness * d0 == s_p_witness * d1 for d0, d1 in zip(base_D50, p_D50))
    and nonzero_D50 >= 35,
    f"draws={len(draws50)}; nonzero D={nonzero_D50}; signs={s_witness}/{s_p_witness}",
)

check(
    "E3 scalar and pair cancellation",
    R1(witness) + R1(p_witness) == 0 and r0_real_zero,
    f"pair sum={R1(witness) + R1(p_witness)}; readable real zero={r0_real_zero}",
)

draws20 = rng.integers(-5, 6, size=(20, 6))
four_way_ok = True
for draw in draws20:
    d_base = density_for_frame(draw, witness_frame)
    d_frame_flip = density_for_frame(draw, p_witness_frame)
    prod_base = s_witness * d_base
    prod_frame_flip = s_witness * d_frame_flip
    prod_witness_flip = s_p_witness * d_base
    prod_both_flip = s_p_witness * d_frame_flip
    four_way_ok = four_way_ok and d_frame_flip == -d_base
    four_way_ok = four_way_ok and s_p_witness == -s_witness
    four_way_ok = four_way_ok and prod_frame_flip == -prod_base
    four_way_ok = four_way_ok and prod_witness_flip == -prod_base
    four_way_ok = four_way_ok and prod_both_flip == prod_base

check(
    "E4 one orientation bit",
    four_way_ok,
    f"draws={len(draws20)}; base sign={s_witness}; flipped sign={s_p_witness}",
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
