"""Empty-state bootstrap runner.

Sections:
S/A - bootstrap setup and orbit dichotomy.
B - model availability sets and the pair.
C - the degree-nine detection wall.
D - the selector and the readout face.

Expected close: TOTAL: PASS=13 FAIL=0
"""

import itertools

import numpy as np


PASS = 0
FAIL = 0
TOL = 1e-9
rng = np.random.default_rng(4)


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def det_int(m):
    return int(round(float(np.linalg.det(m))))


def signed_permutation_matrices():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            m = np.zeros((3, 3))
            for i, j in enumerate(perm):
                m[i, j] = signs[i]
            out.append(m)

    unique = []
    for m in out:
        if not any(np.array_equal(m, n) for n in unique):
            unique.append(m)
    return unique


mats = signed_permutation_matrices()
dets = [det_int(m) for m in mats]
proper = [m for m, d in zip(mats, dets) if d == 1]
improper = [m for m, d in zip(mats, dets) if d == -1]
P = -np.eye(3)


def unit(v):
    v = np.array(v, dtype=float)
    return v / np.linalg.norm(v)


def add_unique(points, v, tol=TOL):
    v = np.array(v, dtype=float)
    if not any(np.linalg.norm(v - w) <= tol for w in points):
        points.append(v)


def unique_points(points, tol=TOL):
    out = []
    for p in points:
        add_unique(out, p, tol)
    return out


def orbit(v):
    return unique_points([r @ v for r in proper])


def transform_set(points, m):
    return unique_points([m @ p for p in points])


def union_sets(*sets):
    out = []
    for s in sets:
        for p in s:
            add_unique(out, p)
    return out


def sets_equal(a, b, tol=TOL):
    if len(a) != len(b):
        return False
    used = [False] * len(b)
    for x in a:
        hit = False
        for i, y in enumerate(b):
            if not used[i] and np.linalg.norm(x - y) <= tol:
                used[i] = True
                hit = True
                break
        if not hit:
            return False
    return True


def sets_disjoint(a, b, tol=TOL):
    return all(np.linalg.norm(x - y) > tol for x in a for y in b)


def proper_invariant(points):
    return all(sets_equal(transform_set(points, r), points) for r in proper)


def p_invariant(points):
    return sets_equal(transform_set(points, P), points)


def improper_stabilized(v):
    return any(np.linalg.norm(m @ v - v) <= TOL for m in improper)


def psi9(v):
    x, y, z = v
    return x * y * z * (x * x - y * y) * (y * y - z * z) * (z * z - x * x)


axis = unit((0.0, 0.0, 1.0))
corner = unit((1.0, 1.0, 1.0))
edge = unit((1.0, 1.0, 0.0))
mirror_plane = unit((0.3, 0.3, np.sqrt(1.0 - 0.18)))
generic = unit((0.2, 0.5, np.sqrt(1.0 - 0.29)))
reps = [axis, corner, edge, mirror_plane, generic]
rep_names = ["axis", "corner", "edge", "mirror", "generic"]


# Section S/A - bootstrap setup and orbit dichotomy.
orbit_sizes = [len(orbit(v)) for v in reps]
check(
    "S0 group machinery and orbit sizes",
    len(mats) == 48
    and len(proper) == 24
    and len(improper) == 24
    and orbit_sizes == [6, 8, 12, 24, 24],
    f"unique={len(mats)} proper={len(proper)} improper={len(improper)} "
    f"orbit_sizes={dict(zip(rep_names, orbit_sizes))}",
)

directions = [
    np.array((1.0, 0.0, 0.0)),
    np.array((-1.0, 0.0, 0.0)),
    np.array((0.0, 1.0, 0.0)),
    np.array((0.0, -1.0, 0.0)),
    np.array((0.0, 0.0, 1.0)),
    np.array((0.0, 0.0, -1.0)),
]
all_open = tuple(["open"] * len(directions))
pattern_fixed = True
for m in mats:
    perm = []
    for d in directions:
        image = m @ d
        matches = [i for i, base in enumerate(directions) if np.array_equal(image, base)]
        if len(matches) != 1:
            pattern_fixed = False
            break
        perm.append(matches[0])
    if tuple(all_open[i] for i in perm) != all_open:
        pattern_fixed = False
        break
check(
    "A1 all-open pattern invariant under full cubic direction action",
    pattern_fixed,
    "constant all-open six-direction coloring is fixed by all 48 direction "
    "permutations; this is the checkable empty-state symmetry input for "
    "proper-covariant availability-set transport",
)

a2_points = reps + [unit(rng.normal(size=3)) for _ in range(30)]
a2_results = []
for v in a2_points:
    orbit_p_invariant = sets_equal(orbit(v), orbit(P @ v))
    stab = improper_stabilized(v)
    a2_results.append(orbit_p_invariant == stab)
check(
    "A2 orbit dichotomy equals improper stabilizer criterion",
    all(a2_results),
    f"cases={len(a2_points)} mismatches={a2_results.count(False)}",
)

generic_orbit = orbit(generic)
p_generic_orbit = orbit(P @ generic)
a3_equal = [sets_equal(orbit(v), orbit(P @ v)) for v in reps[:4]]
a3_disjoint = sets_disjoint(generic_orbit, p_generic_orbit)
check(
    "A3 mirror twins equal exactly on improper-stabilized representatives",
    a3_disjoint and all(a3_equal),
    f"generic_disjoint={a3_disjoint} "
    f"equal={{axis:{a3_equal[0]}, corner:{a3_equal[1]}, edge:{a3_equal[2]}, "
    f"mirror:{a3_equal[3]}}}",
)


# Section B - model availability sets and the pair.
axis_orbit = orbit(axis)
corner_orbit = orbit(corner)
s_chiral = union_sets(axis_orbit, generic_orbit)
p_s_chiral = transform_set(s_chiral, P)
s_paired = union_sets(axis_orbit, generic_orbit, p_generic_orbit)
s_special = union_sets(axis_orbit, corner_orbit)
b1_chiral_not_p = not p_invariant(s_chiral)
b1_paired_p = p_invariant(s_paired)
b1_special_p = p_invariant(s_special)
check(
    "B1 model availability sets under P pairing",
    b1_chiral_not_p and b1_paired_p and b1_special_p,
    f"sizes={{S_chiral:{len(s_chiral)}, S_paired:{len(s_paired)}, "
    f"S_special:{len(s_special)}}} P_flags={{S_chiral:{not b1_chiral_not_p}, "
    f"S_paired:{b1_paired_p}, S_special:{b1_special_p}}}",
)

b2_proper_each = proper_invariant(s_chiral) and proper_invariant(p_s_chiral)
b2_distinct = not sets_equal(s_chiral, p_s_chiral)
b2_no_proper_map = all(not sets_equal(transform_set(s_chiral, r), p_s_chiral) for r in proper)
check(
    "B2 chiral model pair is not related by proper transport",
    b2_proper_each and b2_distinct and b2_no_proper_map,
    f"proper_invariant={b2_proper_each} distinct={b2_distinct} "
    f"proper_maps_to_twin={not b2_no_proper_map}",
)


# Section C - the degree-nine detection wall.
def chi_so3(l, r):
    cos_theta = np.clip((float(np.trace(r)) - 1.0) / 2.0, -1.0, 1.0)
    if abs(cos_theta - 1.0) < 1e-12:
        return float(2 * l + 1)
    theta = np.arccos(cos_theta)
    return float(np.sin((l + 0.5) * theta) / np.sin(0.5 * theta))


def chi_o3(l, m, d):
    if d == 1:
        return chi_so3(l, m)
    proper_part = P @ m
    return ((-1.0) ** l) * chi_so3(l, proper_part)


multiplicities = []
for l in range(11):
    total = sum(d * chi_o3(l, m, d) for m, d in zip(mats, dets)) / len(mats)
    multiplicities.append(total)
c1_low_zero = all(abs(multiplicities[l]) < 1e-9 for l in range(9))
c1_nine_one = abs(multiplicities[9] - 1.0) < 1e-9
check(
    "C1 degree wall by det-character multiplicities",
    c1_low_zero and c1_nine_one,
    "m_l(0..10)=" + "[" + ", ".join(f"{m:.12g}" for m in multiplicities) + "]",
)

c2_ok = True
c2_max_err = 0.0
for m, d in zip(mats, dets):
    for _ in range(3):
        v = rng.normal(size=3)
        lhs = psi9(m @ v)
        rhs = d * psi9(v)
        err = abs(lhs - rhs)
        c2_max_err = max(c2_max_err, err)
        if err > 1e-9 * max(1.0, abs(lhs), abs(rhs)):
            c2_ok = False
check(
    "C2 Psi9 follows det character",
    c2_ok,
    f"group_elements={len(mats)} samples_per_element=3 max_err={c2_max_err:.3e}",
)


def exact_degree_exponents(degree):
    exps = []
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            exps.append((i, j, degree - i - j))
    return exps


def up_to_degree_exponents(degree):
    exps = []
    for total in range(degree + 1):
        exps.extend(exact_degree_exponents(total))
    return exps


def eval_poly(coeffs, exps, v):
    x, y, z = v
    total = 0.0
    for c, (i, j, k) in zip(coeffs, exps):
        total += c * (x ** i) * (y ** j) * (z ** k)
    return total


def det_project_value(coeffs, exps, v):
    total = 0.0
    for m, d in zip(mats, dets):
        total += d * eval_poly(coeffs, exps, m.T @ v)
    return total / len(mats)


c3_zero_checks = []
c3_zero_details = []
for degree in (7, 8):
    exps = exact_degree_exponents(degree)
    coeffs = rng.normal(size=len(exps))
    points = [unit(rng.normal(size=3)) for _ in range(20)]
    input_scale = max(1.0, max(abs(eval_poly(coeffs, exps, v)) for v in points))
    max_projected = max(abs(det_project_value(coeffs, exps, v)) for v in points)
    ok = max_projected < 1e-9 * input_scale
    c3_zero_checks.append(ok)
    c3_zero_details.append(
        f"d{degree}:monomials={len(exps)},max_projected={max_projected:.3e},"
        f"scale={input_scale:.3e}"
    )

exps9 = exact_degree_exponents(9)
coeffs9 = rng.normal(size=len(exps9))
c3_points9 = []
while len(c3_points9) < 20:
    v = unit(rng.normal(size=3))
    if abs(psi9(v)) > 1e-8:
        c3_points9.append(v)
ratios = np.array([det_project_value(coeffs9, exps9, v) / psi9(v) for v in c3_points9])
ratio0 = float(np.mean(ratios))
ratio_spread = float(np.max(np.abs(ratios - ratio0)))
c3_ratio_ok = (
    abs(ratio0) > 1e-10
    and ratio_spread <= 1e-6 * max(1.0, abs(ratio0))
)
check(
    "C3 degree wall by polynomial projection",
    all(c3_zero_checks) and c3_ratio_ok,
    "; ".join(c3_zero_details)
    + f"; d9:monomials={len(exps9)},ratio={ratio0:.12g},spread={ratio_spread:.3e}",
)


def constructed_mirror_points(count):
    points = []
    while len(points) < count:
        a, b = rng.normal(size=2)
        if abs(a) + abs(b) < 1e-12:
            continue
        mode = len(points) % 3
        if mode == 0:
            raw = (a, a, b)
        elif mode == 1:
            raw = (a, -a, b)
        else:
            raw = (0.0, a, b)
        points.append(unit(raw))
    return points


mirror_points = constructed_mirror_points(10)
zero_locus_points = [axis, corner, edge, mirror_plane] + mirror_points
zero_values = [abs(psi9(v)) for v in zero_locus_points]
c4_random_values = []
c4_skipped = 0
for _ in range(20):
    v = unit(rng.normal(size=3))
    value = abs(psi9(v))
    if value <= 1e-8:
        c4_skipped += 1
    else:
        c4_random_values.append(value)
c4_ok = (
    max(zero_values) < 1e-12
    and abs(psi9(generic)) > 1e-8
    and all(v > 1e-8 for v in c4_random_values)
)
check(
    "C4 mirror zero locus and generic nonzero locus",
    c4_ok,
    f"zero_points={len(zero_locus_points)} max_zero={max(zero_values):.3e} "
    f"generic_abs={abs(psi9(generic)):.3e} rng_nonzero={len(c4_random_values)} "
    f"skipped={c4_skipped}",
)

c5_points = reps + mirror_points + [unit(rng.normal(size=3)) for _ in range(40)]
c5_mismatches = 0
for v in c5_points:
    psi_zero = abs(psi9(v)) < 1e-10
    stab = improper_stabilized(v)
    if psi_zero != stab:
        c5_mismatches += 1
check(
    "C5 pointwise Psi9-zero iff improper-stabilized",
    c5_mismatches == 0,
    f"cases={len(c5_points)} mismatches={c5_mismatches}",
)


# Section D - the selector and the readout face.
selector = 1.0 if psi9(generic) > 0.0 else -1.0
d1_transport_ok = True
d1_nonzero_d = 0
for _ in range(20):
    draw = rng.integers(-9, 10, size=6)
    e = draw[:3].astype(float)
    b = np.array((draw[5], -draw[4], draw[3]), dtype=float)
    density = float(e @ b)
    if density != 0.0:
        d1_nonzero_d += 1
    base = selector * density
    simultaneous = (-selector) * (-density)
    content_flip = (-selector) * density
    frame_flip = selector * (-density)
    if simultaneous != base or content_flip != -base or frame_flip != -base:
        d1_transport_ok = False

sum_chiral = float(sum(psi9(v) for v in s_chiral))
sum_paired = float(sum(psi9(v) for v in s_paired))
sum_special = float(sum(psi9(v) for v in s_special))
d1_orbit_sums_ok = (
    abs(sum_paired) < 1e-12
    and abs(sum_special) < 1e-12
    and abs(sum_chiral) > 1e-8
)
check(
    "D1 one-bit selector transport and orbit sums",
    d1_transport_ok and d1_nonzero_d >= 15 and d1_orbit_sums_ok,
    f"nonzero_D={d1_nonzero_d}/20 orbit_sums={{S_chiral:{sum_chiral:.12g}, "
    f"S_paired:{sum_paired:.12g}, S_special:{sum_special:.12g}}}",
)

config = [unit(rng.normal(size=3)) for _ in range(6)]
q_exps = up_to_degree_exponents(3)
q_coeffs = rng.normal(size=len(q_exps))


def q_poly(v):
    return eval_poly(q_coeffs, q_exps, v)


def even_f(v):
    return q_poly(v) + q_poly(-v)


readout = float(sum(even_f(v) for v in config))
flipped_readout = float(sum(even_f(-v) for v in config))
psi_sum = float(sum(psi9(v) for v in config))
flipped_psi_sum = float(sum(psi9(-v) for v in config))
d2_ok = (
    abs(readout - flipped_readout) < 1e-12
    and abs(psi_sum + flipped_psi_sum) < 1e-12
    and abs(psi_sum) > 1e-8
)
check(
    "D2 readout face: even additive scalar vs Psi9",
    d2_ok,
    f"readout={readout:.12g} flipped_readout={flipped_readout:.12g} "
    f"Psi9_sum={psi_sum:.12g} flipped_Psi9_sum={flipped_psi_sum:.12g}",
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
