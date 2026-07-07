"""
Sections:
S/A - nonemptiness and the free-orbit reduction.
B - the J2 channel and one-step closure / propagation tests.
C - spontaneous registration under the achiral toy rule.

Expected close: TOTAL: PASS=12 FAIL=0
"""

import itertools

import numpy as np


rng = np.random.default_rng(8)

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        prefix = "PASS"
    else:
        FAIL += 1
        prefix = "FAIL"
    print(f"{prefix}: {name}" + (f" | {detail}" if detail else ""))


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
DIRS = AX.copy()


def axis_index(vec):
    v = tuple(int(x) for x in np.asarray(vec, dtype=int))
    for i, a in enumerate(AX):
        if v == tuple(int(x) for x in a):
            return i
    raise ValueError(f"not an axis vector: {v}")


NEG = tuple(axis_index(-AX[i]) for i in range(len(AX)))


def det_int(M):
    return int(round(float(np.linalg.det(M))))


def mat_key(M):
    return tuple(int(x) for x in M.reshape(-1))


def signed_permutation_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            M = np.zeros((3, 3), dtype=int)
            for row, col in enumerate(perm):
                M[row, col] = signs[row]
            mats.append(M)
    mats.sort(key=mat_key)
    return mats


GROUP = signed_permutation_group()
PROPER = [M for M in GROUP if det_int(M) == 1]
IMPROPER = [M for M in GROUP if det_int(M) == -1]
IDENTITY = np.eye(3, dtype=int)


def point_key(v):
    return tuple(int(x) for x in np.asarray(v, dtype=int))


def proper_orbit_int(point):
    p = np.asarray(point, dtype=int)
    return {point_key(M @ p) for M in PROPER}


def inverted_point_set(points):
    return {tuple(-x for x in p) for p in points}


def is_inversion_invariant(points):
    return inverted_point_set(points) == set(points)


def orbit_float(v):
    return {tuple(float(x) for x in np.round(M @ v, 12)) for M in PROPER}


def has_nontrivial_stabilizer(v):
    return any(
        not np.array_equal(M, IDENTITY) and np.allclose(M @ v, v, atol=1e-10)
        for M in PROPER
    )


def inversion_in_float_orbit(v):
    return any(np.allclose(M @ v, -v, atol=1e-10) for M in PROPER)


def triple(a, b, c):
    return int(np.dot(np.cross(a, b), c))


def j2(slots):
    total = 0
    for d in slots:
        for e in slots:
            if d != e:
                total += triple(DIRS[d], DIRS[e], AX[slots[e]])
    return int(total)


def flip_slots(slots):
    return {NEG[d]: NEG[c] for d, c in slots.items()}


def transform_slots(slots, M):
    return {axis_index(M @ DIRS[d]): axis_index(M @ AX[c]) for d, c in slots.items()}


def all_sites(L):
    return tuple(itertools.product(range(L), repeat=3))


def neighbor_site(site, direction, L):
    raw = np.asarray(site, dtype=int) + DIRS[direction]
    return tuple(int(x) for x in np.mod(raw, L))


def slot_pattern(config, L, site):
    slots = {}
    for d in range(len(DIRS)):
        nb = neighbor_site(site, d, L)
        if nb in config:
            slots[d] = config[nb]
    return slots


def available(config, L, site, odd_channel):
    slots = slot_pattern(config, L, site)
    threshold = 0.0
    if odd_channel and len(slots) >= 2 and j2(slots) < -1e-9:
        threshold = 1.0

    out = []
    for cand in range(len(AX)):
        base = sum(int(np.dot(AX[cand], AX[c])) for c in slots.values())
        if float(base) >= threshold:
            out.append(cand)
    return tuple(out)


def flip_config(config):
    return {site: NEG[c] for site, c in config.items()}


def flip_availability(candidates):
    return tuple(sorted(NEG[c] for c in candidates))


def random_slot_pattern():
    slots = {}
    for d in range(len(DIRS)):
        if rng.random() < 0.55:
            slots[d] = int(rng.integers(0, len(AX)))
    return slots


def random_config_with_empty_target(L, max_records):
    sites = all_sites(L)
    target = sites[int(rng.integers(0, len(sites)))]
    pool = [i for i, s in enumerate(sites) if s != target]
    nrec = int(rng.integers(1, max_records + 1))
    chosen = rng.choice(pool, size=nrec, replace=False)
    config = {
        sites[int(i)]: int(rng.integers(0, len(AX)))
        for i in chosen
    }
    return config, target


def state_to_config(state, sites):
    return {sites[i]: c for i, c in enumerate(state) if c >= 0}


def flip_state(state):
    return tuple(-1 if c < 0 else NEG[c] for c in state)


def transform_site(site, M, L):
    raw = M @ np.asarray(site, dtype=int)
    return tuple(int(x) for x in np.mod(raw, L))


def transform_config(config, M, L):
    return {
        transform_site(site, M, L): axis_index(M @ AX[c])
        for site, c in config.items()
    }


def transformed_candidates(candidates, M):
    return tuple(sorted(axis_index(M @ AX[c]) for c in candidates))


def history_reachable(history, L, odd_channel):
    config = {}
    trace = []
    ok = True
    for site, content in history:
        avail = available(config, L, site, odd_channel)
        trace.append((site, content, avail))
        if site in config or content not in avail:
            ok = False
            break
        config = dict(config)
        config[site] = content
    return ok, config, trace


# Section S/A.
axis_rep = np.array([1, 0, 0], dtype=int)
corner_rep = np.array([1, 1, 1], dtype=int)
edge_rep = np.array([1, 1, 0], dtype=int)
mirror_rep = np.array([2, 1, 0], dtype=int)
generic_rep = np.array([3, 2, 1], dtype=int)

orbit_reps = (axis_rep, corner_rep, edge_rep, mirror_rep, generic_rep)
orbit_sizes = tuple(len(proper_orbit_int(p)) for p in orbit_reps)
det_counts = (len(PROPER), len(IMPROPER))
check(
    "S0 computed cubic group machinery",
    len(GROUP) == 48 and det_counts == (24, 24) and orbit_sizes == (6, 8, 12, 24, 24),
    f"group={len(GROUP)} det_split={det_counts} orbit_sizes={orbit_sizes}",
)

axis_orbit = proper_orbit_int(axis_rep)
corner_orbit = proper_orbit_int(corner_rep)
edge_orbit = proper_orbit_int(edge_rep)
mirror_orbit = proper_orbit_int(mirror_rep)
generic_orbit = proper_orbit_int(generic_rep)
model_sets = (
    axis_orbit,
    axis_orbit | corner_orbit,
    axis_orbit | generic_orbit,
)
a1_ok = all(
    proper_orbit_int(np.array(p, dtype=int)).issubset(model_set)
    for model_set in model_sets
    for p in model_set
)
check(
    "A1 proper nonempty orbit containment",
    a1_ok,
    f"model_sizes={tuple(len(s) for s in model_sets)}",
)

axis_count = 0
axis_residual_ok = True
for M in PROPER:
    if np.array_equal(M, IDENTITY):
        continue
    vals, vecs = np.linalg.eig(M.astype(float))
    idx = int(np.argmin(np.abs(vals - 1.0)))
    axis = np.real(vecs[:, idx])
    axis = axis / np.linalg.norm(axis)
    axis_residual_ok = axis_residual_ok and np.allclose(M @ axis, axis, atol=1e-8)
    if any(np.allclose(H @ axis, axis, atol=1e-8) for H in IMPROPER):
        axis_count += 1
check(
    "A2 rotation axes improper stabilized",
    axis_residual_ok and axis_count == len(PROPER) - 1,
    f"improper_fixed_axes={axis_count} nonidentity_proper={len(PROPER) - 1}",
)

samples = [p.astype(float) for p in orbit_reps]
for _ in range(20):
    v = rng.normal(size=3)
    samples.append(v / np.linalg.norm(v))

a3_small = 0
a3_ok = True
for v in samples:
    size = len(orbit_float(v))
    nontrivial = has_nontrivial_stabilizer(v)
    inv = inversion_in_float_orbit(v)
    a3_ok = a3_ok and ((size < len(PROPER)) == nontrivial)
    a3_ok = a3_ok and (size == len(PROPER) or inv)
    if size < len(PROPER):
        a3_small += 1
check(
    "A3 small proper orbits and inversion",
    a3_ok,
    f"samples={len(samples)} small_orbits={a3_small}",
)

base_union = axis_orbit | corner_orbit | edge_orbit | mirror_orbit
with_generic = base_union | generic_orbit
generic_twin = proper_orbit_int(-generic_rep)
restored = with_generic | generic_twin
a4_ok = (
    is_inversion_invariant(base_union)
    and not is_inversion_invariant(with_generic)
    and is_inversion_invariant(restored)
)
check(
    "A4 free orbit reduction by inversion",
    a4_ok,
    f"base={len(base_union)} plus_one_free={len(with_generic)} restored={len(restored)}",
)


# Section B.
b1_flip_ok = True
b1_nonzero = False
for _ in range(200):
    slots = random_slot_pattern()
    val = j2(slots)
    b1_nonzero = b1_nonzero or (val != 0)
    b1_flip_ok = b1_flip_ok and (j2(flip_slots(slots)) == -val)

b1_cov_ok = True
for M in PROPER:
    for _ in range(5):
        slots = random_slot_pattern()
        b1_cov_ok = b1_cov_ok and (j2(transform_slots(slots, M)) == j2(slots))
check(
    "B1 J2 flip odd and proper covariant",
    b1_flip_ok and b1_nonzero and b1_cov_ok,
    f"nonzero_observed={b1_nonzero} proper_tests={len(PROPER) * 5}",
)

pair_reps = tuple(i for i in range(len(AX)) if i < NEG[i])
b2_values = []
for _ in range(50):
    slots = {}
    for d in pair_reps:
        if rng.random() < 0.85:
            c = int(rng.integers(0, len(AX)))
            slots[d] = c
            slots[NEG[d]] = c
    b2_values.append(j2(slots))
check(
    "B2 L2 duplicated slots zero J2",
    all(v == 0 for v in b2_values),
    f"patterns={len(b2_values)} values={tuple(sorted(set(b2_values)))}",
)

b3_ok = True
for _ in range(200):
    config, target = random_config_with_empty_target(3, 4)
    lhs = tuple(sorted(available(flip_config(config), 3, target, False)))
    rhs = flip_availability(available(config, 3, target, False))
    b3_ok = b3_ok and (lhs == rhs)
check(
    "B3 achiral toy one-step closure under flip",
    b3_ok,
    "trials=200",
)

sites2 = all_sites(2)
empty_state = tuple(-1 for _ in sites2)
layers = [set([empty_state])]
for _depth in range(3):
    next_layer = set()
    for state in layers[-1]:
        config = state_to_config(state, sites2)
        for i, site in enumerate(sites2):
            if state[i] >= 0:
                continue
            for content in available(config, 2, site, False):
                new_state = list(state)
                new_state[i] = content
                next_layer.add(tuple(new_state))
    layers.append(next_layer)
layer_sizes = tuple(len(layer) for layer in layers)
b4_flip_ok = all(flip_state(state) in layer for layer in layers for state in layer)
check(
    "B4 achiral toy BFS endpoint flip closure",
    b4_flip_ok and layer_sizes[0] == 1,
    f"layer_sizes={layer_sizes}",
)

witness_first = ((1, 1, 0), 2)
witness_second = ((0, 1, 1), 3)
witness_target = (0, 1, 0)
first_avail = available({}, 3, witness_first[0], True)
config_after_first = {witness_first[0]: witness_first[1]}
second_avail = available(config_after_first, 3, witness_second[0], True)
witness_config = {
    witness_first[0]: witness_first[1],
    witness_second[0]: witness_second[1],
}
witness_slots = slot_pattern(witness_config, 3, witness_target)
flipped_witness = flip_config(witness_config)
flipped_witness_slots = slot_pattern(flipped_witness, 3, witness_target)
witness_j2 = j2(witness_slots)
flipped_witness_j2 = j2(flipped_witness_slots)
witness_avail = available(witness_config, 3, witness_target, True)
flipped_witness_avail = available(flipped_witness, 3, witness_target, True)
all_candidates = tuple(range(len(AX)))
b5_ok = (
    witness_first[1] in first_avail
    and witness_second[1] in second_avail
    and witness_j2 == 2
    and flipped_witness_j2 == -2
    and witness_avail == all_candidates
    and flipped_witness_avail == tuple()
    and tuple(sorted(flipped_witness_avail)) != flip_availability(witness_avail)
)
check(
    "B5 chiral toy one-step closure violation witness",
    b5_ok,
    (
        f"J2={witness_j2} flip_J2={flipped_witness_j2} "
        f"avail={witness_avail} flip_avail={flipped_witness_avail} "
        f"reachable=({witness_first[1] in first_avail},{witness_second[1] in second_avail})"
    ),
)

b6_ok = True
sites3 = all_sites(3)
for M in PROPER:
    for _ in range(3):
        target = sites3[int(rng.integers(0, len(sites3)))]
        pool = [i for i, s in enumerate(sites3) if s != target]
        nrec = int(rng.integers(0, 6))
        chosen = rng.choice(pool, size=nrec, replace=False)
        config = {
            sites3[int(i)]: int(rng.integers(0, len(AX)))
            for i in chosen
        }
        moved_config = transform_config(config, M, 3)
        moved_target = transform_site(target, M, 3)
        lhs = available(moved_config, 3, moved_target, True)
        rhs = transformed_candidates(available(config, 3, target, True), M)
        b6_ok = b6_ok and (tuple(sorted(lhs)) == rhs)
check(
    "B6 chiral toy proper torus covariance",
    b6_ok,
    f"proper_elements={len(PROPER)} random_configs_each=3",
)


# Section C.
history = (
    witness_first,
    witness_second,
    (witness_target, 0),
)
history_ok, history_config, history_trace = history_reachable(history, 3, False)
flipped_history = tuple((site, NEG[content]) for site, content in history)
flipped_history_ok, flipped_history_config, flipped_trace = history_reachable(
    flipped_history, 3, False
)
nonzero_sites = []
for site in sites3:
    val = j2(slot_pattern(history_config, 3, site))
    if val != 0:
        nonzero_sites.append((site, val))
c1_ok = history_ok and flipped_history_ok and bool(nonzero_sites)
check(
    "C1 achiral toy spontaneous J2 registration",
    c1_ok,
    (
        f"history_available={[content in avail for _, content, avail in history_trace]} "
        f"flip_history_available={[content in avail for _, content, avail in flipped_trace]} "
        f"first_nonzero={nonzero_sites[0] if nonzero_sites else None}"
    ),
)


print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
