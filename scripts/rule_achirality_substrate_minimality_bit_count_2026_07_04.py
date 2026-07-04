"""
Rule achirality substrate runner.

Sections:
A - reflection symmetry of the supplied substrate
B - achiral and chiral rules in the proper-covariant rule space
C - mirror pair and one bit count
D - reflection-odd selecting datum
E - odd non-sourcing and spontaneous-state escape

Expected close: TOTAL: PASS=14 FAIL=0
"""

import itertools

import numpy as np


PASS = 0
FAIL = 0

AX = np.array(
    [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1],
    ],
    dtype=int,
)
AXIS_INDEX = {tuple(int(x) for x in AX[i]): i for i in range(6)}
NEG = tuple(AXIS_INDEX[tuple(int(x) for x in -AX[i])] for i in range(6))
SIGMA = np.diag((-1, 1, 1)).astype(int)
MINUS_I = -np.eye(3, dtype=int)
rng = np.random.default_rng(5)


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def mat_key(m):
    return tuple(int(x) for x in np.asarray(m, dtype=int).reshape(-1))


def det_int(m):
    return int(round(float(np.linalg.det(m))))


def aidx(v):
    return AXIS_INDEX[tuple(int(x) for x in np.asarray(v, dtype=int))]


def sorted_cond(cond):
    return {int(k): int(cond[k]) for k in sorted(cond)}


def cond_key(cond):
    return tuple((int(d), int(c)) for d, c in sorted(cond.items()))


def signed_permutation_group():
    mats = {}
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            m = np.zeros((3, 3), dtype=int)
            for row, col in enumerate(perm):
                m[row, col] = signs[row]
            mats[mat_key(m)] = m
    return [mats[k] for k in sorted(mats)]


def axis_sign_flips():
    return [np.diag(signs).astype(int) for signs in itertools.product((-1, 1), repeat=3)]


def transform_condition(m, cond):
    out = {}
    for d, c in cond.items():
        out[aidx(m @ AX[d])] = aidx(m @ AX[c])
    return sorted_cond(out)


def transform_output(m, out):
    return frozenset(aidx(m @ AX[x]) for x in out)


def transform_site(m, site, n):
    v = np.array(site, dtype=int)
    return tuple(int(x % n) for x in (m @ v))


def base_value(m, cond):
    return sum(int(np.dot(AX[m], AX[c])) for c in cond.values())


def base_multiset(cond):
    return tuple(sorted(base_value(m, cond) for m in range(6)))


def J2(cond):
    total = 0
    slots = list(cond)
    for d, e in itertools.permutations(slots, 2):
        total += int(np.dot(np.cross(AX[d], AX[e]), AX[cond[e]]))
    return total


def R_align(cond):
    return frozenset(m for m in range(6) if base_value(m, cond) >= 0)


def R_J2(cond):
    thr = 1 if len(cond) >= 2 and J2(cond) < 0 else 0
    return frozenset(m for m in range(6) if base_value(m, cond) >= thr)


def R_J2bar(cond):
    thr = 1 if len(cond) >= 2 and J2(cond) > 0 else 0
    return frozenset(m for m in range(6) if base_value(m, cond) >= thr)


def covariance_pair(rule, m, cond):
    left = rule(transform_condition(m, cond))
    right = transform_output(m, rule(cond))
    return left, right


def covariance_holds(rule, m, cond):
    left, right = covariance_pair(rule, m, cond)
    return left == right


def conjugated_output(m, rule, cond):
    return transform_output(m, rule(transform_condition(m.T, cond)))


def has_zero_base(cond):
    return any(base_value(m, cond) == 0 for m in range(6))


def random_condition():
    k = int(rng.integers(3, 6))
    slots = rng.choice(6, size=k, replace=False)
    contents = rng.integers(0, 6, size=k)
    return sorted_cond({int(d): int(c) for d, c in zip(slots, contents)})


def make_sample():
    conds = []
    seen = set()
    attempts = 0
    while len(conds) < 60:
        attempts += 1
        cond = random_condition()
        key = cond_key(cond)
        if key in seen:
            continue
        chiral = J2(cond) != 0
        if len(conds) < 36:
            accept = chiral and has_zero_base(cond)
        else:
            accept = (not chiral) or has_zero_base(cond)
        if accept:
            conds.append(cond)
            seen.add(key)
    return conds, attempts


def first_covariance_failure(rule, mats, conds):
    for m in mats:
        for cond in conds:
            left, right = covariance_pair(rule, m, cond)
            if left != right:
                return m, cond, left, right
    return None


def torus_edges(n):
    sites = list(itertools.product(range(n), repeat=3))
    edges = set()
    for site in sites:
        for d in (0, 2, 4):
            nbr = tuple(int((site[i] + AX[d][i]) % n) for i in range(3))
            edges.add(tuple(sorted((tuple(site), nbr))))
    return edges


def transform_edges(m, edges, n):
    return {tuple(sorted((transform_site(m, a, n), transform_site(m, b, n)))) for a, b in edges}


def difference_within_chiral(conds):
    # The twins agree whenever J2 == 0 (identical threshold), so the difference
    # set is a SUBSET of the chiral set: a difference REQUIRES J2 != 0, i.e. the
    # distinguishing datum lives in the reflection-odd channel. Equality does NOT
    # hold in general -- a chiral condition with no content exactly at the
    # threshold has R_J2 == R_J2bar -- so we test only the load-bearing subset
    # direction (differences imply chirality), on an unbiased sample.
    diff = [cond for cond in conds if R_J2(cond) != R_J2bar(cond)]
    chiral = [cond for cond in conds if J2(cond) != 0]
    subset = all(J2(cond) != 0 for cond in diff)
    return subset, len(diff), len(chiral)


rng_ub = np.random.default_rng(11)


def random_condition_unbiased():
    k = int(rng_ub.integers(3, 6))
    slots = rng_ub.choice(6, size=k, replace=False)
    contents = rng_ub.integers(0, 6, size=k)
    return sorted_cond({int(d): int(c) for d, c in zip(slots, contents)})


def canonical_pair_key(cond):
    mate = transform_condition(SIGMA, cond)
    return min(cond_key(cond), cond_key(mate))


def chiral_transversal(conds):
    reps = []
    seen = set()
    for cond in conds:
        if J2(cond) == 0:
            continue
        pos = cond if J2(cond) > 0 else transform_condition(SIGMA, cond)
        key = canonical_pair_key(pos)
        if key not in seen:
            reps.append(pos)
            seen.add(key)
    return reps


def handedness(rule, positive_cond):
    # Size asymmetry of the rule's OWN output across a chiral pair
    # {cond, sigma.cond}, using only the rule's outputs (no R_align reference).
    # An achiral rule commutes with sigma, so |rule(cond)| = |rule(sigma.cond)|
    # and this is 0 by a MEASURED symmetry, not by construction. A chiral rule
    # can prefer one handedness (nonzero) -- on pairs where its threshold bites.
    negative_cond = transform_condition(SIGMA, positive_cond)
    d = len(rule(positive_cond)) - len(rule(negative_cond))
    return (d > 0) - (d < 0)


def Omega(rule, conds):
    return sum(
        1
        for cond in conds
        if rule(transform_condition(SIGMA, cond)) != transform_output(SIGMA, rule(cond))
    )


def su3_diag(phi, psi):
    return np.diag(
        np.array(
            [
                np.exp(1j * phi),
                np.exp(1j * psi),
                np.exp(-1j * (phi + psi)),
            ],
            dtype=complex,
        )
    )


def theta_seed_odd_part(u):
    c = 0.37
    alpha = 0.71
    return float(-2.0 * c * np.sin(alpha) * np.imag(np.trace(u)))


def find_reachable_chiral_history():
    site = (0, 0, 0)
    for length in range(3, 7):
        for slots in itertools.permutations(range(6), length):
            for contents in itertools.product(range(6), repeat=length):
                cond = {}
                history = []
                ok = True
                for d, c in zip(slots, contents):
                    if c not in R_align(cond):
                        ok = False
                        break
                    cond[d] = c
                    history.append((site, d, c))
                if ok and J2(cond) != 0:
                    return history, sorted_cond(cond)
    return None, None


def replay_history(history, rule, n):
    records = {}
    for site, d, c in history:
        site = tuple(site)
        cond = records.setdefault(site, {})
        if d in cond:
            return False, records
        _neighbor = tuple(int((site[i] + AX[d][i]) % n) for i in range(3))
        if c not in rule(cond):
            return False, records
        cond[d] = c
    return True, {site: sorted_cond(cond) for site, cond in records.items()}


def mirror_history(history):
    return [
        (transform_site(SIGMA, site, 3), aidx(SIGMA @ AX[d]), aidx(SIGMA @ AX[c]))
        for site, d, c in history
    ]


GROUP = signed_permutation_group()
GPROPER = [m for m in GROUP if det_int(m) == 1]
GIMPROPER = [m for m in GROUP if det_int(m) == -1]
FLIPS = axis_sign_flips()
SAMPLE, SAMPLE_ATTEMPTS = make_sample()


product_keys = {mat_key(r @ f) for r in GPROPER for f in FLIPS}
group_keys = {mat_key(m) for m in GROUP}
proper_flip_intersection = {mat_key(m) for m in GPROPER} & {mat_key(f) for f in FLIPS}
check(
    "A1 substrate reflection generated by proper rotations and sign flips",
    len(GROUP) == 48
    and len(GPROPER) == 24
    and len(FLIPS) == 8
    and product_keys == group_keys
    and len(proper_flip_intersection) == 4
    and det_int(SIGMA) == -1
    and mat_key(SIGMA) in product_keys
    and all(NEG[NEG[i]] == i for i in range(6)),
    f"|O_h|={len(GROUP)} |G+|={len(GPROPER)} |Z2^3|={len(FLIPS)} intersection={len(proper_flip_intersection)}",
)

edges5 = torus_edges(5)
check(
    "A2 torus nearest-neighbor adjacency reflection symmetry",
    transform_edges(SIGMA, edges5, 5) == edges5 and transform_edges(MINUS_I, edges5, 5) == edges5,
    f"|E(Z5^3)|={len(edges5)} sigma_equal={transform_edges(SIGMA, edges5, 5) == edges5} inversion_equal={transform_edges(MINUS_I, edges5, 5) == edges5}",
)

check(
    "B1 R_align achiral O_h covariance",
    first_covariance_failure(R_align, GROUP, SAMPLE) is None,
    f"checked={len(GROUP) * len(SAMPLE)} sample={len(SAMPLE)}",
)

b2_failure = first_covariance_failure(R_J2, GPROPER, SAMPLE)
b2_witness = first_covariance_failure(R_J2, GIMPROPER, SAMPLE)
if b2_witness is None:
    b2_detail = f"proper_failure={b2_failure is not None} improper_witness=None"
else:
    wm, wc, wl, wr = b2_witness
    b2_detail = (
        f"proper_checked={len(GPROPER) * len(SAMPLE)} "
        f"improper_g={mat_key(wm)} cond={cond_key(wc)} J2={J2(wc)} "
        f"lhs={tuple(sorted(wl))} rhs={tuple(sorted(wr))}"
    )
check(
    "B2 R_J2 proper covariance with improper witness",
    b2_failure is None and b2_witness is not None,
    b2_detail,
)

chiral_count = sum(1 for cond in SAMPLE if J2(cond) != 0)
check(
    "B3 chiral condition count is non-vacuous",
    chiral_count >= 30,
    f"chiral={chiral_count}/{len(SAMPLE)} sample_attempts={SAMPLE_ATTEMPTS}",
)

c1_sigma_to_bar = all(conjugated_output(SIGMA, R_J2, cond) == R_J2bar(cond) for cond in SAMPLE)
c1_distinct = any(R_J2(cond) != R_J2bar(cond) for cond in SAMPLE)
c1_bar_cov = first_covariance_failure(R_J2bar, GPROPER, SAMPLE) is None
check(
    "C1 mirror pair under reflection conjugation",
    c1_sigma_to_bar and c1_distinct and c1_bar_cov,
    f"sigma_to_bar={c1_sigma_to_bar} mirror_distinct={c1_distinct} R_J2bar_Gplus={c1_bar_cov}",
)

c2_witnesses = []
for m in GPROPER:
    witness = None
    for cond in SAMPLE:
        if conjugated_output(m, R_J2, cond) != R_J2bar(cond):
            witness = cond
            break
    if witness is not None:
        c2_witnesses.append((m, witness))
check(
    "C2 no proper element connects mirror pair",
    len(c2_witnesses) == len(GPROPER),
    f"proper_elements_with_witness={len(c2_witnesses)}/{len(GPROPER)} first_cond={cond_key(c2_witnesses[0][1]) if c2_witnesses else None}",
)

c3_align_fixed = all(conjugated_output(SIGMA, R_align, cond) == R_align(cond) for cond in SAMPLE)
c3_j2_to_bar = all(conjugated_output(SIGMA, R_J2, cond) == R_J2bar(cond) for cond in SAMPLE)
c3_bar_to_j2 = all(conjugated_output(SIGMA, R_J2bar, cond) == R_J2(cond) for cond in SAMPLE)
c3_pair_distinct = any(R_J2(cond) != R_J2bar(cond) for cond in SAMPLE)
c3_sigma_involution = np.array_equal(SIGMA @ SIGMA, np.eye(3, dtype=int))
check(
    "C3 reflection orbit sizes give zero or one bit",
    c3_align_fixed and c3_j2_to_bar and c3_bar_to_j2 and c3_pair_distinct and c3_sigma_involution,
    f"R_align_orbit=1 R_J2_orbit=2 sigma_involution={c3_sigma_involution}",
)

UNBIASED = [random_condition_unbiased() for _ in range(400)]
d1_subset, d1_diff_count, d1_chiral_count = difference_within_chiral(UNBIASED)
# The subset (twins differ => J2 != 0) holds BY CONSTRUCTION (identical
# thresholds when J2 == 0), so it is reported, not gated. The gate rests on
# the genuinely computed facts: J2 is reflection-odd, and the even base-value
# multiset is reflection-invariant -- so the distinguishing datum lives in the
# reflection-odd channel and no even summary recovers it.
d1_odd = all(J2(transform_condition(SIGMA, cond)) == -J2(cond) for cond in UNBIASED)
d1_base_even = all(base_multiset(transform_condition(SIGMA, cond)) == base_multiset(cond) for cond in UNBIASED)
check(
    "D1 selecting datum is reflection-odd",
    d1_odd and d1_base_even and d1_diff_count > 0 and d1_subset,
    f"unbiased={len(UNBIASED)}: J2 reflection-odd={d1_odd}, base-multiset reflection-invariant={d1_base_even}; "
    f"twins differ on {d1_diff_count} conds, all chiral (subset of {d1_chiral_count}; the subset holds by construction of the thresholds)",
)

# Unbiased chiral transversal (one representative per {cond, sigma.cond} pair).
transversal = chiral_transversal(UNBIASED)
d2_align = [handedness(R_align, cond) for cond in transversal]
d2_j2 = [handedness(R_J2, cond) for cond in transversal]
d2_bar = [handedness(R_J2bar, cond) for cond in transversal]
d2_active = sum(1 for x in d2_j2 if x != 0)
check(
    "D2 handedness selector carries one bit",
    len(transversal) > 0
    and all(x == 0 for x in d2_align)          # achiral rule: measured symmetry, 0
    and all(x in (-1, 0, 1) for x in d2_j2)
    and all(a == -b for a, b in zip(d2_j2, d2_bar))  # mirror pair: exact negation
    and d2_active > 0,                          # non-vacuity: some pair is decided
    f"pairs={len(transversal)} achiral_selector={set(d2_align)} "
    f"mirror_pair_opposite={all(a == -b for a, b in zip(d2_j2, d2_bar))} "
    f"active(chiral rule decides)={d2_active}/{len(transversal)} (0 where no content sits at the threshold)",
)

omega_align = Omega(R_align, SAMPLE)
omega_j2 = Omega(R_J2, SAMPLE)
check(
    "E1a achiral Omega sources nothing",
    omega_align == 0,
    f"Omega(R_align)={omega_align}",
)
check(
    "E1b chiral Omega positive control",
    omega_j2 > 0,
    f"Omega(R_J2)={omega_j2}",
)

phase_pairs = [(float(rng.uniform(-np.pi, np.pi)), float(rng.uniform(-np.pi, np.pi))) for _ in range(5)]
us = [su3_diag(phi, psi) for phi, psi in phase_pairs]
e2_flip = all(abs(theta_seed_odd_part(u.conj().T) + theta_seed_odd_part(u)) < 1e-12 for u in us)
e2_swap_sum = sum(theta_seed_odd_part(u) + theta_seed_odd_part(u.conj().T) for u in us)
e2_frame_sum = sum(theta_seed_odd_part(u) for u in us)
check(
    "E2 theta-seed projection is reflection-odd",
    e2_flip and abs(e2_swap_sum) < 1e-12 and abs(e2_frame_sum) > 1e-9,
    f"flip={e2_flip} swap_sum={e2_swap_sum:.3e} imported_orientation_sum={e2_frame_sum:.3e}",
)

history, final_cond = find_reachable_chiral_history()
hist_ok, records = replay_history(history, R_align, 3) if history is not None else (False, {})
mhist = mirror_history(history) if history is not None else []
mirror_ok, mirror_records = replay_history(mhist, R_align, 3) if mhist else (False, {})
site = (0, 0, 0)
state_j2 = J2(records.get(site, {})) if hist_ok else 0
mirror_j2 = J2(mirror_records.get(site, {})) if mirror_ok else 0
check(
    "E3 chiral state survives achiral law",
    hist_ok and mirror_ok and state_j2 != 0 and mirror_j2 == -state_j2,
    f"history_len={len(history) if history else 0} J2={state_j2} mirror_J2={mirror_j2} cond={cond_key(final_cond) if final_cond else None}",
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
