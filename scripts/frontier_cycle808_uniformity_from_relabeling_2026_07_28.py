#!/usr/bin/env python3
"""Cycle 808: test uniformity as a corollary of the Cycle-805 relabelings.

The Cycle-805 pair and the carried Cycle-793 package are SHA-pinned,
text/AST-only, and runtime-blocklisted.  Their finite constructions are
reimplemented below against the landed Cycle-719/750 machinery.

This runner distinguishes an isomorphism between convention presentations
from an automorphism of one labeled occurrence multiset.  That distinction is
load-bearing for the requested symmetry-to-uniformity implication.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1500
STDOUT_LIMIT_BYTES = 200 * 1024
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle805_supply_relabeling_tournament_2026_07_28.py",
    "scripts/frontier_cycle805_relabeling_independent_check_2026_07_28.py",
    "scripts/frontier_cycle793_enlarged_orientation_census_2026_07_28.py",
    "scripts/frontier_cycle793_balance_independent_check_2026_07_28.py",
    "scripts/frontier_cycle750_actual_selector_stretch_2026_07_28.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

import ast
from collections import Counter, deque
from hashlib import sha256
import importlib.abc
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
START = monotonic()
ALL_BANKS = (1, 2, 3, 5, 12)
EXPECTED_STATIONS = {1: 3, 2: 11, 3: 19, 5: 35, 12: 91}
BLOCKLISTED_MODULES = (
    "frontier_cycle805_supply_relabeling_tournament_2026_07_28",
    "frontier_cycle805_relabeling_independent_check_2026_07_28",
    "frontier_cycle793_enlarged_orientation_census_2026_07_28",
    "frontier_cycle793_balance_independent_check_2026_07_28",
)
EXPECTED_INPUT_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "04432816e3844043b419de8d91001003cd7fb8de76635658c3367574c3e44b9a",
    AUDIT_INPUT_PATHS[1]:
        "dca858db349bddeb2e4e800bf68a0be2f9fabf076529decf7f3700c26a45655f",
    AUDIT_INPUT_PATHS[2]:
        "aff8222437aac85443df6770cd11bef136b7698f6be0d4a65caa7771f1bf31c5",
    AUDIT_INPUT_PATHS[3]:
        "4f96f4b862dce8d0221ff47c9f9b4e761d55ee5285cd6c8de984d22d70463399",
    AUDIT_INPUT_PATHS[4]:
        "a74c7e5bbc297c57d317af7fd85d0b9e01d078625f5d4689daf2ebbdbc1cee0a",
    AUDIT_INPUT_PATHS[5]:
        "0c0417912f35c369113513823edd2221d446ecdcae7ff039c50fb7c322e791c4",
}


class _PackageBlocker(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path=None, target=None):
        if fullname in BLOCKLISTED_MODULES:
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


PACKAGE_BLOCKER = _PackageBlocker()
sys.meta_path.insert(0, PACKAGE_BLOCKER)
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle750_actual_selector_stretch_2026_07_28 as S750
import frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26 as K719


Normal = tuple[int, int, int, int]
CHECKS: dict[str, bool] = {}
OUTPUT_LINES: list[str] = []


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def emit(*parts: object) -> None:
    OUTPUT_LINES.append(" ".join(str(part) for part in parts))


def check(label: str, condition: bool, detail: object) -> None:
    if label in CHECKS:
        raise AssertionError(("duplicate certificate", label))
    CHECKS[label] = bool(condition)
    emit("PASS" if condition else "FAIL", label, "::", compact(detail))


def file_sha256(path: str) -> str:
    return sha256((ROOT / path).read_bytes()).hexdigest()


def top_level_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    assignments = {}
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        for target in targets:
            if isinstance(target, ast.Name):
                assignments[target.id] = node.value
    return assignments


def package_text_audit() -> dict[str, object]:
    sources = {
        path: (ROOT / path).read_text(encoding="utf-8")
        for path in AUDIT_INPUT_PATHS[:4]
    }
    trees = {
        path: ast.parse(source, filename=path)
        for path, source in sources.items()
    }
    imported = []
    own_tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))
    own_assignments = top_level_assignments(own_tree)
    for node in own_tree.body:
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
    runtime_attempts = {}
    for module in BLOCKLISTED_MODULES:
        try:
            __import__(module)
        except ImportError as exc:
            runtime_attempts[module] = (
                str(exc) == f"BLOCKLIST forbids import of {module}"
            )
        else:
            runtime_attempts[module] = False
    audit_node = own_assignments["AUDIT_INPUT_PATHS"]
    declared_node = own_assignments["DECLARED_INPUT_PATHS"]
    normalized = {
        path: " ".join(source.split()) for path, source in sources.items()
    }
    anchors = {
        "cycle805_primary_has_station_cyclic_map": (
            "def cyclic_map(stations: int, shift: int)" in
            sources[AUDIT_INPUT_PATHS[0]]
            and '"station_labels": [' in sources[AUDIT_INPUT_PATHS[0]]
        ),
        "cycle805_primary_extends_declared_domains": all(
            token in sources[AUDIT_INPUT_PATHS[0]]
            for token in (
                '"physical_track_site_slots"',
                '"logical_bank_indices"',
                '"epochs"',
                '"layer_slots"',
                '"q_traversal_slots"',
            )
        ),
        "cycle805_checker_shift_formula": (
            '-int(row["program_rotation"]) - phase_offset(row)'
            in normalized[AUDIT_INPUT_PATHS[1]]
        ),
        "cycle805_checker_checkpoint_discipline": (
            "after every complete controller step, forward and inverse"
            in sources[AUDIT_INPUT_PATHS[1]]
            and 'attack_2["checkpoint_count"] == 684'
            in sources[AUDIT_INPUT_PATHS[1]]
        ),
        "cycle793_primary_count_anchor": (
            'enlarged_counts == {"+1": 23, "-1": 23, "total": 46}'
            in sources[AUDIT_INPUT_PATHS[2]]
        ),
        "cycle793_checker_pair_anchor": (
            "2j -> 2j+1 is a 1:1 constructor-level pairing"
            in sources[AUDIT_INPUT_PATHS[3]]
            and '"orientation_conjugates_exact"' in sources[AUDIT_INPUT_PATHS[3]]
        ),
        "all_texts_parse": all(
            isinstance(tree, ast.Module) for tree in trees.values()
        ),
    }
    return {
        "literal_AUDIT_INPUT_PATHS": (
            isinstance(audit_node, ast.Tuple)
            and all(
                isinstance(item, ast.Constant) and isinstance(item.value, str)
                for item in audit_node.elts
            )
            and tuple(ast.literal_eval(audit_node)) == AUDIT_INPUT_PATHS
        ),
        "DECLARED_INPUT_PATHS_alias": (
            isinstance(declared_node, ast.Name)
            and declared_node.id == "AUDIT_INPUT_PATHS"
        ),
        "paths_worktree_relative": all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
        "all_paths_exist": all(
            (ROOT / path).is_file() for path in AUDIT_INPUT_PATHS
        ),
        "blocklisted_not_AST_imported": not set(imported).intersection(
            BLOCKLISTED_MODULES
        ),
        "blocklisted_not_loaded": all(
            module not in sys.modules for module in BLOCKLISTED_MODULES
        ),
        "runtime_blocker_installed": PACKAGE_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "source_anchors": anchors,
    }


def multiplicative_order(value: int, modulus: int) -> int:
    if gcd(value, modulus) != 1:
        raise ValueError((value, modulus))
    current = 1
    for exponent in range(1, modulus + 1):
        current = current * value % modulus
        if current == 1:
            return exponent
    raise AssertionError(("order bound failed", value, modulus))


def compose(left: Normal, right: Normal, modulus: int) -> Normal:
    """Return left after right for (station, layer, q multiplier, q shift)."""
    lt, ll, la, lb = left
    rt, rl, ra, rb = right
    return (
        (lt + rt) % modulus,
        ll ^ rl,
        la * ra % modulus,
        (la * rb + lb) % modulus,
    )


def inverse(row: Normal, modulus: int) -> Normal:
    station, layer, multiplier, shift = row
    multiplier_inverse = pow(multiplier, -1, modulus)
    return (
        -station % modulus,
        layer,
        multiplier_inverse,
        -multiplier_inverse * shift % modulus,
    )


def power(row: Normal, exponent: int, modulus: int) -> Normal:
    if exponent < 0:
        return power(inverse(row, modulus), -exponent, modulus)
    result: Normal = (0, 0, 1, 0)
    factor = row
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = compose(result, factor, modulus)
        factor = compose(factor, factor, modulus)
        remaining //= 2
    return result


def q_positions(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        order = tuple(range(stations))
    elif mode == "descending":
        order = tuple(reversed(range(stations)))
    elif mode == "even_then_odd":
        order = tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    else:
        raise ValueError(mode)
    positions = [0] * stations
    for slot, station in enumerate(order):
        positions[station] = slot
    return tuple(positions)


def generator_specs() -> tuple[dict[str, object], ...]:
    """The nine non-landed Cycle-805 choices, in independent normal form."""
    return (
        {
            "name": "I1_SOURCE_1",
            "supply": "inherited_1",
            "choice": "source_index=1",
            "rotation": -1,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        },
        {
            "name": "I1_SOURCE_LAST",
            "supply": "inherited_1",
            "choice": "source_index=stations-1",
            "rotation": 1,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        },
        {
            "name": "I2_ROTATE_1",
            "supply": "inherited_2",
            "choice": "left_rotation=1",
            "rotation": 1,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        },
        {
            "name": "I2_ROTATE_LAST",
            "supply": "inherited_2",
            "choice": "left_rotation=stations-1",
            "rotation": -1,
            "layer_order": "Q_then_R",
            "order_mode": "ascending",
        },
        *(
            {
                "name": f"I3_{layer}_{order}".upper(),
                "supply": "inherited_3",
                "choice": f"layers={layer};Q_order={order}",
                "rotation": 0,
                "layer_order": layer,
                "order_mode": order,
            }
            for layer, order in (
                ("Q_then_R", "descending"),
                ("Q_then_R", "even_then_odd"),
                ("R_then_Q", "ascending"),
                ("R_then_Q", "descending"),
                ("R_then_Q", "even_then_odd"),
            )
        ),
    )


def spec_normal(spec: dict[str, object], modulus: int) -> Normal:
    rotation = int(spec["rotation"])
    phase = int(spec["layer_order"] == "R_then_Q")
    mode = str(spec["order_mode"])
    if mode == "ascending":
        multiplier = 1
        shift = -rotation
    elif mode == "descending":
        multiplier = -1
        shift = rotation - 1
    elif mode == "even_then_odd":
        multiplier = pow(2, -1, modulus)
        shift = -rotation * multiplier
    else:
        raise ValueError(mode)
    return (
        (-rotation - phase) % modulus,
        phase,
        multiplier % modulus,
        shift % modulus,
    )


def spec_bank_maps(
    spec: dict[str, object],
    stations: int,
) -> dict[str, tuple[int, ...] | tuple[tuple[int, int], ...]]:
    rotation = int(spec["rotation"]) % stations
    phase = int(spec["layer_order"] == "R_then_Q")
    station_shift = (-rotation - phase) % stations
    station = tuple(
        (value + station_shift) % stations for value in range(stations)
    )
    q_position = q_positions(stations, str(spec["order_mode"]))
    q_slots = tuple(
        q_position[(value - rotation) % stations]
        for value in range(stations)
    )
    physical = tuple(
        2 * ((site // 2 + station_shift) % stations) + site % 2
        for site in range(2 * stations)
    )
    return {
        "station": station,
        "physical": physical,
        "q_slots": q_slots,
        "layer": (phase, 1 ^ phase),
        "epochs": tuple(range(2 * ((stations + 5) // 8))),
        "orientations": (-1, 1),
    }


def exact_group_certificate(stations: dict[int, int]) -> dict[str, object]:
    modulus = lcm(*stations.values())
    order_two = multiplicative_order(2, modulus)
    powers_two = {pow(2, exponent, modulus) for exponent in range(order_two)}
    multipliers = {
        sign * residue % modulus
        for sign in (1, -1)
        for residue in powers_two
    }
    multiplier_closure = all(
        left * right % modulus in multipliers
        for left in multipliers
        for right in multipliers
    )
    multiplier_inverse_closure = all(
        pow(value, -1, modulus) in multipliers for value in multipliers
    )

    specs = generator_specs()
    raw = {str(spec["name"]): spec_normal(spec, modulus) for spec in specs}
    identity: Normal = (0, 0, 1, 0)
    r: Normal = (1, 0, 1, 0)
    s: Normal = (0, 1, 1, 0)
    tau: Normal = (0, 0, 1, 1)
    mu: Normal = (0, 0, 2, 0)
    nu: Normal = (0, 0, -1 % modulus, 0)

    raw_a = raw["I1_SOURCE_1"]
    raw_d = raw["I3_Q_THEN_R_DESCENDING"]
    raw_e = raw["I3_Q_THEN_R_EVEN_THEN_ODD"]
    raw_r = raw["I3_R_THEN_Q_ASCENDING"]
    half_word = pow(-2, -1, modulus)
    derived_r = power(raw_r, 2 * half_word, modulus)
    derived_s = compose(raw_r, derived_r, modulus)
    derived_tau = compose(raw_a, inverse(derived_r, modulus), modulus)
    derived_mu = inverse(raw_e, modulus)
    derived_nu = compose(derived_tau, raw_d, modulus)

    multiplier_words = {}
    for epsilon in (0, 1):
        for exponent in range(order_two):
            value = (-1 if epsilon else 1) * pow(2, exponent, modulus) % modulus
            multiplier_words.setdefault(value, (epsilon, exponent))

    decompositions = {}
    for name, element in raw.items():
        station_shift, layer, multiplier, shift = element
        epsilon, exponent = multiplier_words[multiplier]
        rebuilt = compose(
            power(r, station_shift, modulus),
            compose(
                power(s, layer, modulus),
                compose(
                    power(tau, shift, modulus),
                    compose(
                        power(mu, exponent, modulus),
                        power(nu, epsilon, modulus),
                        modulus,
                    ),
                    modulus,
                ),
                modulus,
            ),
            modulus,
        )
        decompositions[name] = {
            "normal": element,
            "basis_word": {
                "r": station_shift,
                "s": layer,
                "tau": shift,
                "mu": exponent,
                "nu": epsilon,
            },
            "rebuilds": rebuilt == element,
            "inverse_normal": inverse(element, modulus),
        }

    presentation_relations = {
        "r^L": power(r, modulus, modulus) == identity,
        "s^2": power(s, 2, modulus) == identity,
        "tau^L": power(tau, modulus, modulus) == identity,
        "mu^ord2": power(mu, order_two, modulus) == identity,
        "nu^2": power(nu, 2, modulus) == identity,
        "mu_nu_commute": (
            compose(mu, nu, modulus) == compose(nu, mu, modulus)
        ),
        "mu_tau_mu_inverse=tau^2": (
            compose(
                compose(mu, tau, modulus),
                inverse(mu, modulus),
                modulus,
            )
            == power(tau, 2, modulus)
        ),
        "nu_tau_nu_inverse=tau^-1": (
            compose(
                compose(nu, tau, modulus),
                inverse(nu, modulus),
                modulus,
            )
            == inverse(tau, modulus)
        ),
        "r_and_s_central": all(
            compose(left, right, modulus) == compose(right, left, modulus)
            for left in (r, s)
            for right in (r, s, tau, mu, nu)
        ),
    }
    canonical_basis_derived = {
        "r": derived_r == r,
        "s": derived_s == s,
        "tau": derived_tau == tau,
        "mu": derived_mu == mu,
        "nu": derived_nu == nu,
    }
    group_order = modulus * 2 * modulus * len(multipliers)
    return {
        "station_modulus": modulus,
        "station_sizes": stations,
        "multiplier_order_of_2": order_two,
        "minus_one_in_powers_of_2": (-1 % modulus) in powers_two,
        "multiplier_group_order": len(multipliers),
        "multiplier_closure_exhaustive": multiplier_closure,
        "multiplier_inverse_closure_exhaustive": multiplier_inverse_closure,
        "affine_translation_domain_complete": len(range(modulus)) == modulus,
        "affine_inverse_well_defined": all(
            gcd(value, modulus) == 1 for value in multipliers
        ),
        "normal_form":
            "(r^i,s^j,tau^b,mu^k,nu^e), "
            "0<=i,b<L; 0<=j,e<2; 0<=k<ord_L(2)",
        "normal_form_unique_count": group_order,
        "group_order": group_order,
        "presentation": (
            f"<r,s,tau,mu,nu | r^{modulus}=s^2=tau^{modulus}="
            f"mu^{order_two}=nu^2=1; r,s central; [mu,nu]=1; "
            "mu*tau*mu^-1=tau^2; nu*tau*nu^-1=tau^-1>"
        ),
        "canonical_basis_derived_from_verified_generators":
            canonical_basis_derived,
        "presentation_relations": presentation_relations,
        "raw_generators": decompositions,
        "all_raw_generators_rebuilt": all(
            row["rebuilds"] for row in decompositions.values()
        ),
        "exact_closure_and_inverse": all(
            (
                multiplier_closure,
                multiplier_inverse_closure,
                all(gcd(value, modulus) == 1 for value in multipliers),
                all(canonical_basis_derived.values()),
                all(presentation_relations.values()),
                all(row["rebuilds"] for row in decompositions.values()),
            )
        ),
    }


def permutation_orbits(
    points: tuple[int, ...],
    generators: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    remaining = set(points)
    orbits = []
    while remaining:
        start = min(remaining)
        orbit = {start}
        queue = deque((start,))
        while queue:
            point = queue.popleft()
            for permutation in generators:
                target = permutation[point]
                if target not in orbit:
                    orbit.add(target)
                    queue.append(target)
        ordered = tuple(sorted(orbit))
        orbits.append(ordered)
        remaining.difference_update(orbit)
    return tuple(orbits)


def all_label_orbits(stations: dict[int, int]) -> tuple[dict[str, object], ...]:
    specs = generator_specs()
    rows = []
    for bank in ALL_BANKS:
        size = stations[bank]
        maps = tuple(spec_bank_maps(spec, size) for spec in specs)
        for domain, point_count in (
            ("station", size),
            ("physical_track_site", 2 * size),
            ("q_traversal_slot", size),
            ("epoch", 2 * bank),
            ("logical_bank_index", bank),
        ):
            mapping_key = {
                "physical_track_site": "physical",
                "q_traversal_slot": "q_slots",
                "epoch": "epochs",
                "logical_bank_index": "epochs",
            }.get(domain, domain)
            generators = tuple(
                tuple(
                    int(value)
                    for value in mapping[mapping_key][:point_count]
                )
                if domain != "logical_bank_index"
                else tuple(range(bank))
                for mapping in maps
            )
            orbits = permutation_orbits(tuple(range(point_count)), generators)
            rows.append(
                {
                    "domain": domain,
                    "bank": bank,
                    "points": point_count,
                    "orbits": orbits,
                    "nontrivial_orbits": sum(len(orbit) > 1 for orbit in orbits),
                }
            )
    layer_generators = tuple(
        tuple(int(value) for value in spec_bank_maps(spec, 3)["layer"])
        for spec in specs
    )
    rows.extend(
        (
            {
                "domain": "layer_slot",
                "bank": None,
                "points": 2,
                "orbits": permutation_orbits((0, 1), layer_generators),
                "nontrivial_orbits": 1,
            },
            {
                "domain": "orientation",
                "bank": None,
                "points": 2,
                "labels": (-1, 1),
                "orbits": ((-1,), (1,)),
                "nontrivial_orbits": 0,
            },
            {
                "domain": "direction",
                "bank": None,
                "points": 2,
                "labels": ((1, 0), (0, 1)),
                "orbits": (((1, 0),), ((0, 1),)),
                "nontrivial_orbits": 0,
            },
            {
                "domain": "layer_kind",
                "bank": None,
                "points": 2,
                "labels": ("Q", "R"),
                "orbits": (("Q",), ("R",)),
                "nontrivial_orbits": 0,
            },
        )
    )
    return tuple(rows)
