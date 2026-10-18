"""Exact finite controls for the conditional contact-source pump.

Only standard-library modules and SymPy are imported. No artifact reads, writes,
random inputs, top-level execution, cache production, or audit verdicts occur.
The infinite-volume/all-time statements require the source note's analytic
proofs; finitely many H powers and channel incidences are corroborating fixtures.
"""
from collections import defaultdict
from itertools import combinations, permutations, product
import sympy as s

_COORDS = tuple((x, y, 0) for x in (-2, -1, 1, 2) for y in (0, 1))
_STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))


def _pair(a, b):
    return tuple(sorted((a, b)))


def _add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _adjacent(a, b):
    return sum(abs(x - y) for x, y in zip(a, b)) == 1


def _clean(values):
    return {key: value for key, value in values.items() if value}


def _states(mutation):
    a, b, c, d = (1, 0, 0), (2, 0, 0), (2, 1, 0), (1, 1, 0)
    chi = {_pair(a, b): s.Rational(1, 2), _pair(b, c): -s.Rational(1, 2),
           _pair(c, d): s.Rational(1, 2), _pair(d, a): -s.Rational(1, 2)}
    if mutation == "scale_source":
        chi = {key: 2 * value for key, value in chi.items()}

    def odd(n, x):
        return int(x == n) - int(x == -n)

    # p=sqrt(2)*psi: rational coefficients retain exact normalized-wedge math.
    p = {}
    for u, v in combinations(_COORDS, 2):
        dx = odd(1, u[0]) * odd(2, v[0]) - odd(2, u[0]) * odd(1, v[0])
        dy = int(u[1] == 0 and v[1] == 1) - int(u[1] == 1 and v[1] == 0)
        value = s.Rational(dx * dy, 2)
        if value:
            p[_pair(u, v)] = value
    if mutation == "add_contact_to_target":
        p[_pair(a, b)] = s.Rational(1, 2)
    return chi, p


def _hamiltonian(state, mutation=None, free=False):
    """Configuration formula at j=1; hard-core collisions are excluded."""
    out = defaultdict(lambda: s.Rational(0))
    contact_coefficient = 0 if mutation == "omit_contact_energy" else 4
    hopping = 2 if mutation == "reverse_hopping" else -2
    for (a, b), value in state.items():
        out[(a, b)] += (24 if free else 24 - contact_coefficient * _adjacent(a, b)) * value
        for moving, fixed in ((a, b), (b, a)):
            for delta in _STEPS:
                dest = _add(moving, delta)
                if dest != fixed:
                    out[_pair(dest, fixed)] += hopping * value
    return _clean(out)


def _bond_action(state):
    """Independent implementation: sum each crossing bond's 2(I-SWAP)."""
    out = defaultdict(lambda: s.Rational(0))
    for positions, value in state.items():
        for occupied in positions:
            for delta in _STEPS:
                dest = _add(occupied, delta)
                if dest in positions:
                    continue
                remaining = set(positions) - {occupied}
                out[positions] += 2 * value
                out[tuple(sorted(remaining | {dest}))] -= 2 * value
    return _clean(out)


def _inner(left, right):
    return sum(s.conjugate(value) * right.get(key, 0) for key, value in left.items())


def _rotations():
    result = []
    for permutation in permutations(range(3)):
        parity = (-1) ** sum(permutation[i] > permutation[j] for i in range(3) for j in range(i + 1, 3))
        for signs in product((-1, 1), repeat=3):
            if parity * signs[0] * signs[1] * signs[2] == 1:
                result.append((permutation, signs))
    return result


def _incidence(chi, rotations, axis):
    def rotate(point, rotation):
        permutation, signs = rotation
        return tuple(signs[i] * point[permutation[i]] for i in range(3))

    endpoint = tuple(int(i == axis) for i in range(3))
    edge = _pair((0, 0, 0), endpoint)
    labels = []
    for index, rotation in enumerate(rotations):
        rotated = {_pair(rotate(a, rotation), rotate(b, rotation)): value for (a, b), value in chi.items()}
        shifts = {tuple(x - y for x, y in zip(dest, point))
                  for pair in rotated for point in pair for dest in edge}
        for shift in shifts:
            translated = {_pair(_add(a, shift), _add(b, shift)): value for (a, b), value in rotated.items()}
            if edge in translated:
                labels.append((index, shift, translated[edge]))
    return labels


def _evaluate(mutation=None):
    chi, p = _states(mutation)
    index = {point: i for i, point in enumerate(_COORDS)}
    dimension = 2 ** len(_COORDS)

    def bit(pair):
        return sum(1 << index[point] for point in pair)

    vc = s.SparseMatrix(dimension, 1, {(bit(pair), 0): value for pair, value in chi.items()})
    vp = s.SparseMatrix(dimension, 1, {(bit(pair), 0): value for pair, value in p.items()})
    jm = s.SparseMatrix(dimension, dimension,
                        {(b | (1 << i), b): 1 for b in range(dimension)
                         for i in range(8) if not b & (1 << i)})
    jp = jm.T
    jz = s.diag(*[4 - b.bit_count() for b in range(dimension)])
    zero = s.zeros(dimension, 1)
    checks = {
        "source_norm": (vc.T * vc)[0] == 1,
        "target_norm": (vp.T * vp)[0] == 2,
        "source_highest_weight": jp * vc == zero,
        "target_highest_weight": jp * vp == zero,
        "source_target_orthogonal": (vc.T * vp)[0] == 0,
        "source_contact_support": all(_adjacent(*pair) for pair in chi),
    }
    # W=sqrt(2)*V is rational; no floating-point matrix normalization.
    w = s.SparseMatrix(dimension, dimension, {})
    sources, targets, norms = [], [], []
    for r in range(5):
        norm = s.factorial(r) * s.factorial(4) / s.factorial(4 - r)
        checks[f"multiplet_norm_{r}"] = (vc.T * vc)[0] == norm and (vp.T * vp)[0] == 2 * norm
        sources.append(vc)
        targets.append(vp)
        norms.append(norm)
        if not (mutation == "omit_last_multiplet" and r == 4):
            w += vp * vc.T / norm
        vc, vp = jm * vc, jm * vp
    checks.update({
        "multiplets_end": vc == zero and vp == zero,
        "scalar_Jplus": w * jp == jp * w,
        "scalar_Jminus": w * jm == jm * w,
        "scalar_Jz": w * jz == jz * w,
        "partial_isometry_sources": all(w * sources[r] == targets[r] for r in range(5)),
        "partial_isometry_adjoint": all(w.T * targets[r] == 2 * sources[r] for r in range(5)),
        "two_flip_restriction": all(w[:, b] == (targets[0] * sources[0][b] if b.bit_count() == 2 else zero)
                                    for b in range(dimension) if b.bit_count() <= 2),
    })
    seed = _pair((1, 0, 0), (2, 0, 0))
    if mutation == "wrong_first_seed":
        seed = _pair((-2, 0, 0), (-1, 0, 0))
    image = w[:, bit(seed)]
    first_rate = (image.T * image)[0] / 2
    checks["selected_first_seed_rate"] = first_rate == s.Rational(1, 4)

    energy_source = _inner(chi, _hamiltonian(chi, mutation))
    energy_target = _inner(p, _hamiltonian(p, mutation)) / 2
    checks["source_energy"] = energy_source == 20
    checks["target_energy"] = energy_target == 24
    checks["source_bond_action"] = _hamiltonian(chi, mutation) == _bond_action(chi)
    rows, state = [], p
    for power in range(7):
        action = _hamiltonian(state, mutation)
        rows.append({
            "power": power, "support_configurations": len(state),
            "zero_contact": all(not _adjacent(*pair) for pair in state),
            "zero_x0_plane": all(a[0] != 0 and b[0] != 0 for a, b in state),
            "full_free_action_agrees": action == _hamiltonian(state, mutation, free=True),
            "independent_bond_action_agrees": action == _bond_action(state),
        })
        state = action
    checks["dark_orbit_fixtures"] = all(row["zero_contact"] and row["zero_x0_plane"] for row in rows)
    checks["full_H_fixtures"] = all(row["full_free_action_agrees"] and row["independent_bond_action_agrees"] for row in rows)

    rotations = _rotations()
    if mutation == "remove_rotation":
        rotations = rotations[:-1]
    incidence_rows = []
    for axis in range(3):
        labels = _incidence(chi, rotations, axis)
        rate = sum(value * value for _, _, value in labels)
        incidence_rows.append({"axis": axis, "source_support_count": len(labels), "total_initial_rate_over_gamma": str(rate)})
    checks["rotation_group_size"] = len(rotations) == 24
    checks["edge_incidence_32"] = all(row["source_support_count"] == 32 for row in incidence_rows)
    checks["total_initial_rate_8"] = all(row["total_initial_rate_over_gamma"] == "8" for row in incidence_rows)
    checks = {name: bool(value) for name, value in checks.items()}
    family_members = {
        "normalization": ("source_norm", "target_norm"),
        "scalar_intertwiner": ("source_highest_weight", "target_highest_weight", "source_target_orthogonal", "multiplets_end",
                               "scalar_Jplus", "scalar_Jminus", "scalar_Jz", "partial_isometry_sources", "partial_isometry_adjoint",
                               "two_flip_restriction") + tuple(f"multiplet_norm_{r}" for r in range(5)),
        "full_H": ("source_bond_action", "full_H_fixtures"),
        "dark_contact_and_plane": ("source_contact_support", "dark_orbit_fixtures"),
        "incidence": ("rotation_group_size", "edge_incidence_32", "total_initial_rate_8"),
        "energy": ("source_energy", "target_energy"),
        "selected_first_event": ("selected_first_seed_rate",),
    }
    families = {name: all(checks[key] for key in members) for name, members in family_members.items()}
    return {
        "kind": "exact finite conditional controls; no audit verdict",
        "sympy": s.__version__, "local_dimension": dimension,
        "checks": checks, "families": families,
        "source_support_size": len(chi), "target_support_size": len(p),
        "multiplet_raw_norms": [str(value) for value in norms],
        "source_energy_over_j": str(energy_source), "target_energy_over_j": str(energy_target),
        "selected_first_seed_rate_over_gamma": str(first_rate),
        "H_power_controls": rows, "incidence_controls": incidence_rows,
        "all_checks": all(checks.values()),
        "scope": "Exact 256-state local algebra, actual-Z3 finite-support H powers 0..6 and three representative edge incidences. All-time persistence, countable CP convergence and positive-time first-event bounds require analytic proofs; no native physical instrument or registration is derived.",
    }


class CheckFailure(RuntimeError):
    """Failed finite controls, with JSON-compatible diagnostic summary."""

    def __init__(self, summary):
        self.summary = summary
        failed = [name for name, ok in summary["checks"].items() if not ok]
        super().__init__("contact-source controls failed: " + ", ".join(failed))


def _checked(mutation=None):
    summary = _evaluate(mutation)
    if not summary["all_checks"]:
        raise CheckFailure(summary)
    return summary


def run_checks():
    """Return exact finite evidence; raise CheckFailure on any failed check."""
    return _checked()


def run_mutation_checks():
    """Run in-memory perturbed constructions, one per load-bearing family.

    Each uses the same fail-closed checks as baseline, without modifying files.
    Multiple detected failures are retained; there is no forced-green predicate.
    """
    mutations = (
        ("scale_source", "normalization"),
        ("omit_last_multiplet", "scalar_intertwiner"),
        ("reverse_hopping", "full_H"),
        ("add_contact_to_target", "dark_contact_and_plane"),
        ("remove_rotation", "incidence"),
        ("omit_contact_energy", "energy"),
        ("wrong_first_seed", "selected_first_event"),
    )
    rows = []
    for mutation, family in mutations:
        try:
            _checked(mutation)
        except CheckFailure as error:
            summary = error.summary
            if summary["families"][family]:
                raise RuntimeError(f"Mutation {mutation} did not fail intended family {family}") from error
            rows.append({"mutation": mutation, "intended_family": family,
                         "failed_checks": [name for name, ok in summary["checks"].items() if not ok],
                         "failed_families": [name for name, ok in summary["families"].items() if not ok],
                         "rejected_by_checks": not summary["all_checks"]})
        else:
            raise RuntimeError(f"Mutation {mutation} was not detected")
    return {"mutations": rows, "all_rejected": all(row["rejected_by_checks"] for row in rows),
            "scope": "Seven explicit in-memory construction mutations; not exhaustive defect coverage."}
