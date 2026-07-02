#!/usr/bin/env python3
"""
Source-side runner for the informative-step fraction occupancy residual packet.

Q1: enumerate the proper cubic rotation group, its six-neighbor slot action,
    and the binary-pattern orbit inventory.
Q2: enumerate exact subset sums, including the optional value-flip refinement.
Q3: recompute p* from the SU(3) Haar Weyl-grid integral, using the zero-sum
    minimal logarithm branch and the 1600-point centered grid in each angle.
Q4: build the occupancy polynomials from the enumerated orbit inventory and
    locate any interior q roots by sign-change bracketing and bisection.

The runner checks source boundaries and prints an honest TOTAL line. It does
not assign an audit verdict, a downstream status, or a selected rule.
"""

import itertools
from fractions import Fraction
from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]


def check(label, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {label}" + (f" - {detail}" if detail else ""))
        return True
    FAIL += 1
    print(f"FAIL: {label}" + (f" - {detail}" if detail else ""))
    return False


def require(label, ok, detail=""):
    return check(label, ok, detail)


def parity_of_perm(perm):
    inv = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            inv += int(perm[i] > perm[j])
    return -1 if inv % 2 else 1


def matmul(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def transpose(a):
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))


def signed_permutation_matrices(det_wanted=None):
    mats = []
    for perm in itertools.permutations(range(3)):
        perm_sign = parity_of_perm(perm)
        for signs in itertools.product((-1, 1), repeat=3):
            det = perm_sign * signs[0] * signs[1] * signs[2]
            if det_wanted is not None and det != det_wanted:
                continue
            rows = [[0, 0, 0] for _ in range(3)]
            for col, row in enumerate(perm):
                rows[row][col] = signs[col]
            mats.append(tuple(tuple(row) for row in rows))
    return tuple(sorted(set(mats)))


SLOTS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
SLOT_INDEX = {slot: i for i, slot in enumerate(SLOTS)}
IDENTITY = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
INVERSION = ((-1, 0, 0), (0, -1, 0), (0, 0, -1))


def matvec(m, v):
    return tuple(sum(m[i][j] * v[j] for j in range(3)) for i in range(3))


def slot_permutation(m):
    return tuple(SLOT_INDEX[matvec(m, slot)] for slot in SLOTS)


def permute_pattern(pattern, perm):
    out = [0] * 6
    for i, j in enumerate(perm):
        out[j] = pattern[i]
    return tuple(out)


def complement_pattern(pattern):
    return tuple(1 - bit for bit in pattern)


def pattern_int(pattern):
    return sum(bit << i for i, bit in enumerate(pattern))


def all_patterns():
    return tuple(tuple((n >> i) & 1 for i in range(6)) for n in range(64))


def orbit_decomposition(perms, include_value_flip=False):
    unvisited = set(all_patterns())
    orbits = []
    while unvisited:
        start = min(unvisited, key=pattern_int)
        orbit = set()
        frontier = [start]
        while frontier:
            pattern = frontier.pop()
            if pattern in orbit:
                continue
            orbit.add(pattern)
            for perm in perms:
                image = permute_pattern(pattern, perm)
                if image not in orbit:
                    frontier.append(image)
                if include_value_flip:
                    flipped = complement_pattern(image)
                    if flipped not in orbit:
                        frontier.append(flipped)
        orbits.append(frozenset(orbit))
        unvisited -= orbit
    return tuple(sorted(orbits, key=lambda o: (sum(next(iter(o))), len(o), min(pattern_int(p) for p in o))))


def cycle_count(perm):
    seen = [False] * len(perm)
    cycles = 0
    for start in range(len(perm)):
        if seen[start]:
            continue
        cycles += 1
        here = start
        while not seen[here]:
            seen[here] = True
            here = perm[here]
    return cycles


def antipodal_pair_count(pattern):
    return int(pattern[0] and pattern[1]) + int(pattern[2] and pattern[3]) + int(pattern[4] and pattern[5])


def describe_pattern_orbit(orbit):
    rep = min(orbit, key=pattern_int)
    weight = sum(rep)
    size = len(orbit)
    pairs = antipodal_pair_count(rep)
    if weight == 0:
        desc = "empty"
    elif weight == 1:
        desc = "single occupied neighbor"
    elif weight == 2:
        desc = "antipodal pair" if pairs == 1 else "adjacent pair"
    elif weight == 3:
        desc = "octant triple" if pairs == 0 else "axial triple"
    elif weight == 4:
        comp_pairs = antipodal_pair_count(complement_pattern(rep))
        desc = "complement of antipodal pair" if comp_pairs == 1 else "complement of adjacent pair"
    elif weight == 5:
        desc = "single vacancy"
    else:
        desc = "full"
    return (size, weight, desc)


def subset_sums(sizes):
    sums = {0}
    for size in sizes:
        sums |= {old + size for old in tuple(sums)}
    return sums


def choose(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    out = 1
    for i in range(1, k + 1):
        out = out * (n - k + i) // i
    return out


def occupancy_polynomial(terms):
    coeffs = [Fraction(0, 1) for _ in range(7)]
    for size, weight in terms:
        for j in range(6 - weight + 1):
            sign = -1 if j % 2 else 1
            coeffs[weight + j] += Fraction(size * sign * choose(6 - weight, j), 1)
    return tuple(coeffs)


def eval_poly_fraction(coeffs, q):
    total = Fraction(0, 1)
    power = Fraction(1, 1)
    for coeff in coeffs:
        total += coeff * power
        power *= q
    return total


def eval_poly_float(coeffs, q):
    total = 0.0
    for coeff in reversed(coeffs):
        total = total * q + float(coeff)
    return total


def poly_string(coeffs):
    pieces = []
    for power, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        if power == 0:
            term = f"{abs(coeff)}"
        elif power == 1:
            term = "q" if abs(coeff) == 1 else f"{abs(coeff)}q"
        else:
            term = f"q^{power}" if abs(coeff) == 1 else f"{abs(coeff)}q^{power}"
        if not pieces:
            pieces.append(term if coeff > 0 else f"-{term}")
        else:
            pieces.append((" + " if coeff > 0 else " - ") + term)
    return "".join(pieces) if pieces else "0"


def recompute_p_star():
    m = 1600
    twopi = 2.0 * np.pi
    step = twopi / m
    angles = -np.pi + (np.arange(m, dtype=float) + 0.5) * step
    density_total = 0.0
    weighted_s2 = 0.0

    for a in angles:
        b = angles
        c_raw = -(a + b)
        c = ((c_raw + np.pi) % twopi) - np.pi

        base = a * a + b * b + c * c
        branch_sum = a + b + c
        s2 = base.copy()

        high = branch_sum > np.pi
        if np.any(high):
            cand_a = (a - twopi) * (a - twopi) + b * b + c * c
            cand_b = a * a + (b - twopi) * (b - twopi) + c * c
            cand_c = a * a + b * b + (c - twopi) * (c - twopi)
            s2[high] = np.minimum(np.minimum(cand_a[high], cand_b[high]), cand_c[high])

        low = branch_sum < -np.pi
        if np.any(low):
            cand_a = (a + twopi) * (a + twopi) + b * b + c * c
            cand_b = a * a + (b + twopi) * (b + twopi) + c * c
            cand_c = a * a + b * b + (c + twopi) * (c + twopi)
            s2[low] = np.minimum(np.minimum(cand_a[low], cand_b[low]), cand_c[low])

        d12 = 2.0 - 2.0 * np.cos(a - b)
        d13 = 2.0 - 2.0 * np.cos(a - c_raw)
        d23 = 2.0 - 2.0 * np.cos(b - c_raw)
        density = (d12 * d13 * d23) / 6.0
        density_total += float(np.sum(density))
        weighted_s2 += float(np.sum(density * s2))

    density_mean = density_total / (m * m)
    s2_mean = weighted_s2 / density_total
    p_star = 4.0 / (s2_mean + 8.0 / 27.0)
    return density_mean, s2_mean, p_star


def sign_change_roots(coeffs, target):
    intervals = []
    q_prev = 0.01
    f_prev = eval_poly_float(coeffs, q_prev) - target
    for i in range(1, 981):
        q = 0.01 + i * (0.98 / 980.0)
        f = eval_poly_float(coeffs, q) - target
        if f_prev == 0.0:
            intervals.append((q_prev, q_prev))
        elif f == 0.0:
            intervals.append((q, q))
        elif f_prev * f < 0.0:
            intervals.append((q_prev, q))
        q_prev = q
        f_prev = f

    roots = []
    for lo, hi in intervals:
        if lo == hi:
            roots.append(lo)
            continue
        flo = eval_poly_float(coeffs, lo) - target
        for _ in range(80):
            mid = 0.5 * (lo + hi)
            fmid = eval_poly_float(coeffs, mid) - target
            if hi - lo < 1.0e-10:
                break
            if flo * fmid <= 0.0:
                hi = mid
            else:
                lo = mid
                flo = fmid
        roots.append(0.5 * (lo + hi))
    return tuple(roots)


def run_group_and_orbit_checks():
    print("\nSECTION A - group and orbit classification")
    proper = signed_permutation_matrices(det_wanted=1)
    all_signed = signed_permutation_matrices(det_wanted=None)
    proper_set = set(proper)

    require("A1 proper cubic rotation group has 24 elements", len(proper) == 24, f"count={len(proper)}")
    closure_ok = all(matmul(a, b) in proper_set for a in proper for b in proper)
    require("A1 proper group is closed under multiplication", closure_ok)
    inverse_ok = all(transpose(a) in proper_set and matmul(a, transpose(a)) == IDENTITY for a in proper)
    require("A1 every proper element has its inverse in the group", inverse_ok)

    proper_perms = tuple(slot_permutation(m) for m in proper)
    proper_perm_set = set(proper_perms)
    require("A2 proper rotations induce 24 distinct six-slot permutations", len(proper_perm_set) == 24)

    orbits = orbit_decomposition(proper_perms)
    sizes = sorted(len(o) for o in orbits)
    weights_single = all(len({sum(p) for p in orbit}) == 1 for orbit in orbits)
    inventory = sorted(describe_pattern_orbit(o) for o in orbits)
    expected_inventory = sorted(
        (
            (1, 0, "empty"),
            (6, 1, "single occupied neighbor"),
            (3, 2, "antipodal pair"),
            (12, 2, "adjacent pair"),
            (8, 3, "octant triple"),
            (12, 3, "axial triple"),
            (3, 4, "complement of antipodal pair"),
            (12, 4, "complement of adjacent pair"),
            (6, 5, "single vacancy"),
            (1, 6, "full"),
        )
    )
    require("A3 binary neighbor patterns have exactly 10 proper-rotation orbits", len(orbits) == 10)
    require("A3 orbit sizes match the validated inventory", sizes == [1, 1, 3, 3, 6, 6, 8, 12, 12, 12], str(sizes))
    require("A3 orbit sizes sum to 64", sum(sizes) == 64)
    require("A3 every orbit has a single Hamming weight", weights_single)
    require("A3 size/weight/description inventory matches anchors", inventory == expected_inventory, str(inventory))

    burnside_sum = sum(2 ** cycle_count(perm) for perm in proper_perms)
    require("A4 Burnside cross-check gives 10 orbits exactly", burnside_sum % 24 == 0 and burnside_sum // 24 == 10, f"sum={burnside_sum}")

    inversion_perm = slot_permutation(INVERSION)
    require("A5 inversion slot permutation is absent from the proper rotation action", inversion_perm not in proper_perm_set, str(inversion_perm))
    require("A5 inversion slot permutation is odd on the six slots", parity_of_perm(inversion_perm) == -1)
    all_slot_perms = {slot_permutation(m) for m in all_signed}
    print(f"  improper-extension slot permutations: {len(all_slot_perms)}; inversion={inversion_perm}")

    flip_orbits = orbit_decomposition(proper_perms, include_value_flip=True)
    flip_sizes = sorted(len(o) for o in flip_orbits)
    require("A6 value-flip refinement has 6 combined orbits", len(flip_orbits) == 6)
    require("A6 value-flip orbit sizes are [2, 6, 8, 12, 12, 24]", flip_sizes == [2, 6, 8, 12, 12, 24], str(flip_sizes))
    return inventory, sizes, flip_sizes


def run_attainable_set_checks(sizes, flip_sizes):
    print("\nSECTION B - attainable sets")
    sums = subset_sums(sizes)
    missing = sorted(set(range(65)) - sums)
    require("B1 rotation-covariant subset sums miss no k in 0..64", missing == [], f"missing={missing}")
    require("B1 rotation-covariant attainable set has 65 values", len(sums) == 65)

    flip_sums = subset_sums(flip_sizes)
    require("B2 value-flip attainable k are even only", all(k % 2 == 0 for k in flip_sums), f"count={len(flip_sums)}")
    require("B2 value-flip k=26 is attainable", 26 in flip_sums)
    require("B2 value-flip k=27 is not attainable", 27 not in flip_sums)
    require("B2 value-flip k=28 is attainable", 28 in flip_sums)


def run_p_star_checks():
    print("\nSECTION C - p* recomputed in-packet")
    density_mean, s2_mean, p_star = recompute_p_star()
    require("C1 Haar density mean equals 1 on the centered Weyl grid", abs(density_mean - 1.0) < 1.0e-9, f"mean={density_mean:.15f}")
    require("C2 <s2_min>_Haar matches the validated value", abs(s2_mean - 9.466227112) < 1.0e-8, f"s2={s2_mean:.12f}")
    require("C3 p* matches 0.409731 within 5e-6", abs(p_star - 0.409731) < 5.0e-6, f"p*={p_star:.9f}")
    scaled = 64.0 * p_star
    nearest_distance = abs(scaled - round(scaled))
    require("C4 64 p* is separated from the nearest integer by more than 0.2", nearest_distance > 0.2, f"64p*={scaled:.6f}")
    low = Fraction(26, 64)
    high = Fraction(27, 64)
    require("C5 p* is bracketed by 26/64 and 27/64", float(low) < p_star < float(high))
    require("C5 bracket gaps are positive and printed", p_star - float(low) > 0 and float(high) - p_star > 0, f"p*-26/64={p_star - float(low):.9f}; 27/64-p*={float(high) - p_star:.9f}")
    return p_star


def run_occupancy_checks(inventory, p_star):
    print("\nSECTION D - occupancy residual")
    by_desc = {desc: (size, weight) for size, weight, desc in inventory}
    r26_terms = (
        by_desc["empty"],
        by_desc["adjacent pair"],
        by_desc["axial triple"],
        by_desc["full"],
    )
    r27_terms = (
        by_desc["antipodal pair"],
        by_desc["adjacent pair"],
        by_desc["axial triple"],
    )
    rules = (("R26", r26_terms, Fraction(26, 64)), ("R27", r27_terms, Fraction(27, 64)))
    all_roots = []
    rules_with_roots = 0
    for name, terms, half_target in rules:
        coeffs = occupancy_polynomial(terms)
        at_half = eval_poly_fraction(coeffs, Fraction(1, 2))
        require(f"D1 {name} polynomial evaluates exactly to {half_target} at q=1/2", at_half == half_target, f"value={at_half}")
        require(f"D1 {name} polynomial has degree at most 6", len(coeffs) == 7 and coeffs[-1] != 0, poly_string(coeffs))
        print(f"  {name}(q) = {poly_string(coeffs)}")

        roots = sign_change_roots(coeffs, p_star)
        if roots:
            rules_with_roots += 1
            print(f"  {name} q* roots: " + ", ".join(f"{root:.12f}" for root in roots))
        else:
            print(f"  {name} has no sign-change root in the scanned interior interval")
        for root in roots:
            all_roots.append((name, root, coeffs))

    require("D2 at least one exhibited rule has an interior sign-change root", rules_with_roots >= 1, f"rules_with_roots={rules_with_roots}")
    require("D2 both fixed exhibited rules are scanned without silent replacement", rules_with_roots <= 2)
    roots_inside = all(0.0 < root < 1.0 for _, root, _ in all_roots)
    require("D2 every found q* lies in (0,1)", roots_inside, f"count={len(all_roots)}")
    residuals_ok = all(abs(eval_poly_float(coeffs, root) - p_star) < 1.0e-8 for _, root, coeffs in all_roots)
    require("D2 every found q* reproduces p* within 1e-8", residuals_ok)
    not_uniform = all(abs(root - 0.5) >= 1.0e-3 for _, root, _ in all_roots)
    require("D3 no found q* equals the uniform baseline within 1e-3", not_uniform)
    print("  Dial discipline: q* is located, not forced; no rule or occupancy law is selected here.")


def flat_text(path):
    if not path.is_file():
        return ""
    return " ".join(path.read_text(encoding="utf-8").split())


def run_source_boundary_guards():
    print("\nSECTION F - source-boundary guards")
    note = ROOT / "docs" / "INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY_RESIDUAL_THEOREM_NOTE_2026-07-02.md"
    runner = ROOT / "scripts" / "informative_fraction_covariant_rule_quantization_occupancy_residual_2026_07_02.py"
    axioms = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
    rigidity = ROOT / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md"
    semigroup = ROOT / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md"

    paths = (
        ("note", note),
        ("runner", runner),
        ("axioms", axioms),
        ("rigidity", rigidity),
        ("semigroup", semigroup),
    )
    for label, path in paths:
        check(f"F files exist: {label}", path.is_file(), str(path.relative_to(ROOT)))

    note_text = flat_text(note)
    runner_text = flat_text(runner)
    axioms_text = flat_text(axioms)
    rigidity_text = flat_text(rigidity)
    semigroup_text = flat_text(semigroup)

    dep_markers = (
        ("F dep marker axioms covariance", axioms_text, "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations."),
        ("F dep marker axioms available-subset clause", axioms_text, "For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions."),
        ("F dep marker axioms no weights", axioms_text, "transition probabilities or weights"),
        ("F dep marker rigidity normalization", rigidity_text, "no independent scalar-normalization freedom"),
        ("F dep marker semigroup boundary", semigroup_text, "continuous Markov semigroups live on the probability/ensemble"),
    )
    for label, text, needle in dep_markers:
        check(label, needle in text)

    preserve_markers = (
        "set only by the independent audit lane",
        "recorded-neighborhood baseline",
        "quantized",
        "k/64",
        "off-lattice",
        "occupancy residual",
        "located, never forced",
        "not a citation-graph dependency",
        "does not claim:",
        "an audit verdict or any effective-status promotion",
        "does not derive the admissibility rule",
        "does not derive occupancy statistics",
    )
    for marker in preserve_markers:
        check(f"F note preserve marker: {marker}", marker in note_text)

    forbidden = (
        "audit_" + "status:",
        "effective_" + "status:",
        "only" + " route",
        "exhaust" + "ed",
        "closes" + " the route",
    )
    for needle in forbidden:
        check(f"F forbidden absent from note: {needle}", needle not in note_text)
        check(f"F forbidden absent from runner: {needle}", needle not in runner_text)


def main():
    inventory, sizes, flip_sizes = run_group_and_orbit_checks()
    run_attainable_set_checks(sizes, flip_sizes)
    p_star = run_p_star_checks()
    run_occupancy_checks(inventory, p_star)
    run_source_boundary_guards()
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
