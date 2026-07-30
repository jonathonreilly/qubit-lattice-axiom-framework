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
from fractions import Fraction
from hashlib import sha256
import importlib.abc
import json
from math import gcd, lcm
from pathlib import Path
import sys
from time import monotonic


class _CountingStdout:
    def __init__(self, target):
        self.target = target
        self.bytes_written = 0

    def write(self, value: str) -> int:
        self.bytes_written += len(value.encode("utf-8"))
        return self.target.write(value)

    def flush(self) -> None:
        self.target.flush()

    def __getattr__(self, name: str):
        return getattr(self.target, name)


COUNTING_STDOUT = _CountingStdout(sys.stdout)
sys.stdout = COUNTING_STDOUT
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
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
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
    literal_dynamic_imports = []
    for node in ast.walk(own_tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.append(node.module or "")
        elif (
            isinstance(node, ast.Call)
            and node.args
            and isinstance(node.args[0], ast.Constant)
            and isinstance(node.args[0].value, str)
            and (
                (
                    isinstance(node.func, ast.Name)
                    and node.func.id == "__import__"
                )
                or (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr == "import_module"
                )
            )
        ):
            literal_dynamic_imports.append(node.args[0].value)
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
    primary_assignments = top_level_assignments(
        trees[AUDIT_INPUT_PATHS[0]]
    )
    source_layer_choices = tuple(
        ast.literal_eval(primary_assignments["LAYER_CHOICES"])
    )
    supply_node = primary_assignments["SUPPLY_CHOICES"]
    if not isinstance(supply_node, ast.Dict):
        raise AssertionError("Cycle-805 SUPPLY_CHOICES is not a dict")
    supply_values = {
        str(ast.literal_eval(key)): value
        for key, value in zip(
            supply_node.keys, supply_node.values, strict=True
        )
    }
    source_supply_choices = {
        "inherited_1": tuple(
            ast.literal_eval(supply_values["inherited_1"])
        ),
        "inherited_2": tuple(
            ast.literal_eval(supply_values["inherited_2"])
        ),
        "inherited_3": tuple(
            f"layers={layer};Q_order={order}"
            for layer, order in source_layer_choices
        ),
    }
    source_alternatives = tuple(
        (supply, choice)
        for supply in ("inherited_1", "inherited_2", "inherited_3")
        for choice in source_supply_choices[supply][1:]
    )
    reimplemented_alternatives = tuple(
        (str(spec["supply"]), str(spec["choice"]))
        for spec in generator_specs()
    )
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
        "cycle805_declared_layer_choices_AST_exact": (
            source_layer_choices
            == (
                ("Q_then_R", "ascending"),
                ("Q_then_R", "descending"),
                ("Q_then_R", "even_then_odd"),
                ("R_then_Q", "ascending"),
                ("R_then_Q", "descending"),
                ("R_then_Q", "even_then_odd"),
            )
        ),
        "cycle805_nine_alternatives_AST_equal_reimplementation": (
            len(source_alternatives) == 9
            and source_alternatives == reimplemented_alternatives
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
        "blocklisted_not_AST_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in imported
        ),
        "blocklisted_not_literal_dynamic_imported": not any(
            name.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES
            for name in literal_dynamic_imports
        ),
        "blocklisted_not_loaded": all(
            loaded.rsplit(".", 1)[-1] not in BLOCKLISTED_MODULES
            for loaded in sys.modules
        ),
        "runtime_blocker_installed": PACKAGE_BLOCKER in sys.meta_path,
        "runtime_attempts": runtime_attempts,
        "source_alternatives": source_alternatives,
        "reimplemented_alternatives": reimplemented_alternatives,
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


def rotate_left(values: tuple, amount: int) -> tuple:
    amount %= len(values)
    return values[amount:] + values[:amount]


def q_order(stations: int, mode: str) -> tuple[int, ...]:
    if mode == "ascending":
        return tuple(range(stations))
    if mode == "descending":
        return tuple(reversed(range(stations)))
    if mode == "even_then_odd":
        return tuple(range(0, stations, 2)) + tuple(range(1, stations, 2))
    raise ValueError(mode)


def advance_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in range(len(a)):
        a[station], b[station] = b[station], a[station]
    for station in range(len(a)):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    return tuple(a), tuple(b)


def retreat_rails(
    a_tokens: tuple[int, ...],
    b_tokens: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    a = list(a_tokens)
    b = list(b_tokens)
    for station in reversed(range(len(a))):
        target = (station + 1) % len(a)
        b[station], a[target] = a[target], b[station]
    for station in reversed(range(len(a))):
        a[station], b[station] = b[station], a[station]
    return tuple(a), tuple(b)


def apply_live_macro(
    data: tuple[int, ...],
    program: tuple,
    a_tokens: tuple[int, ...],
    *,
    reverse: bool,
    order_mode: str,
) -> tuple[int, ...]:
    output = data
    for station in q_order(len(program), order_mode):
        if a_tokens[station]:
            word = K719.mapped_macro(program[station])
            if reverse:
                word = tuple(reversed(word))
            output = K719.A.apply_semantic(output, word)
    return output


def run_orbit(
    data: tuple[int, ...],
    program: tuple,
    *,
    token_position: int,
    reverse: bool,
    layer_order: str,
    order_mode: str,
    checkpoints: bool,
) -> tuple[
    tuple[int, ...],
    tuple[int, ...],
    tuple[int, ...],
    tuple[tuple[tuple[int, ...], tuple[int, ...], tuple[int, ...]], ...],
]:
    stations = len(program)
    a = tuple(int(index == token_position) for index in range(stations))
    b = (0,) * stations
    output = data
    trace = []
    for _step in range(stations):
        if not reverse and layer_order == "Q_then_R":
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
            a, b = advance_rails(a, b)
        elif not reverse and layer_order == "R_then_Q":
            a, b = advance_rails(a, b)
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=False,
                order_mode=order_mode,
            )
        elif reverse and layer_order == "Q_then_R":
            a, b = retreat_rails(a, b)
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
        elif reverse and layer_order == "R_then_Q":
            output = apply_live_macro(
                output,
                program,
                a,
                reverse=True,
                order_mode=order_mode,
            )
            a, b = retreat_rails(a, b)
        else:
            raise ValueError((reverse, layer_order))
        if checkpoints:
            trace.append((output, a, b))
    return output, a, b, tuple(trace)


def epoch_fixtures(
    bank_count: int,
) -> tuple[dict[str, object], ...]:
    banks, links = K719.B.chain_genesis(bank_count)
    state = K719.M.pack_state(banks, links)
    allocator = K719.M.global_allocator_word(bank_count)
    rows = []
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = K719.M.prepare_endpoint(state, direction)
        expected = K719.A.apply_semantic(before, allocator)
        rows.append(
            {
                "event": event,
                "direction": direction,
                "before": before,
                "expected": expected,
            }
        )
        state = expected
    return tuple(rows)


def relabeled_program(
    base_program: tuple,
    mapping: tuple[int, ...],
) -> tuple:
    output = [None] * len(base_program)
    for source, target in enumerate(mapping):
        output[target] = base_program[source]
    if any(row is None for row in output):
        raise AssertionError("incomplete relabeled program")
    return tuple(output)


def spec_station_shift(spec: dict[str, object], stations: int) -> int:
    return (
        -int(spec["rotation"])
        - int(spec["layer_order"] == "R_then_Q")
    ) % stations


def symbolic_commutation(
    bank_count: int,
    spec: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    stations = len(base_program)
    shift = spec_station_shift(spec, stations)
    mapping = tuple(
        (station + shift) % stations for station in range(stations)
    )
    relabeled = relabeled_program(base_program, mapping)
    alternative = rotate_left(base_program, int(spec["rotation"]))
    order = q_order(stations, str(spec["order_mode"]))
    failures = []
    comparisons = 0
    phase = int(spec["layer_order"] == "R_then_Q")
    for base_start in range(stations):
        alternative_start = mapping[base_start]
        for step in range(stations):
            landed_q_station = (alternative_start + step) % stations
            alternative_q_station = (
                alternative_start + step + phase
            ) % stations
            expected_row = base_program[(base_start + step) % stations]
            forward_ok = (
                relabeled[landed_q_station] == expected_row
                and alternative[alternative_q_station] == expected_row
                and (alternative_start + step + 1) % stations
                == mapping[(base_start + step + 1) % stations]
            )
            landed_inverse_q_station = (
                alternative_start - step - 1
            ) % stations
            alternative_inverse_q_station = (
                alternative_start
                - step
                - int(spec["layer_order"] == "Q_then_R")
            ) % stations
            expected_inverse_row = base_program[
                (base_start - step - 1) % stations
            ]
            inverse_ok = (
                relabeled[landed_inverse_q_station]
                == expected_inverse_row
                and alternative[alternative_inverse_q_station]
                == expected_inverse_row
                and (alternative_start - step - 1) % stations
                == mapping[(base_start - step - 1) % stations]
            )
            comparisons += 2
            if not forward_ok or not inverse_ok:
                failures.append(
                    {
                        "base_start": base_start,
                        "step": step,
                        "forward_ok": forward_ok,
                        "inverse_ok": inverse_ok,
                    }
                )
                break
        if failures:
            break
    return {
        "bank": bank_count,
        "generator": spec["name"],
        "station_positions_exhausted": stations,
        "steps_per_orbit": stations,
        "forward_inverse_operator_comparisons": comparisons,
        "q_order_is_permutation": (
            len(set(order)) == stations
            and set(order) == set(range(stations))
        ),
        "failure": failures[:1],
        "commutes_for_arbitrary_data_state": (
            not failures
            and len(set(order)) == stations
            and set(order) == set(range(stations))
        ),
    }


def checkpoint_commutation(
    bank_count: int,
    spec: dict[str, object],
) -> dict[str, object]:
    base_program = K719.interleaved_program(bank_count)
    stations = len(base_program)
    shift = spec_station_shift(spec, stations)
    mapping = tuple(
        (station + shift) % stations for station in range(stations)
    )
    relabeled = relabeled_program(base_program, mapping)
    alternative = rotate_left(base_program, int(spec["rotation"]))
    checkpoint_count = 0
    failures = []
    for fixture in epoch_fixtures(bank_count):
        landed_after, landed_a, landed_b, landed_trace = run_orbit(
            fixture["before"],
            relabeled,
            token_position=mapping[0],
            reverse=False,
            layer_order="Q_then_R",
            order_mode="ascending",
            checkpoints=True,
        )
        varied_after, varied_a, varied_b, varied_trace = run_orbit(
            fixture["before"],
            alternative,
            token_position=mapping[0],
            reverse=False,
            layer_order=str(spec["layer_order"]),
            order_mode=str(spec["order_mode"]),
            checkpoints=True,
        )
        landed_restored, landed_ia, landed_ib, landed_inverse = run_orbit(
            landed_after,
            relabeled,
            token_position=mapping[0],
            reverse=True,
            layer_order="Q_then_R",
            order_mode="ascending",
            checkpoints=True,
        )
        varied_restored, varied_ia, varied_ib, varied_inverse = run_orbit(
            varied_after,
            alternative,
            token_position=mapping[0],
            reverse=True,
            layer_order=str(spec["layer_order"]),
            order_mode=str(spec["order_mode"]),
            checkpoints=True,
        )
        forward_equal = (
            landed_after == varied_after
            and landed_a == varied_a
            and landed_b == varied_b
            and landed_trace == varied_trace
        )
        inverse_equal = (
            landed_restored == varied_restored
            and landed_ia == varied_ia
            and landed_ib == varied_ib
            and landed_inverse == varied_inverse
        )
        checkpoint_count += len(landed_trace) + len(landed_inverse)
        if not forward_equal or not inverse_equal:
            failures.append(
                {
                    "event": fixture["event"],
                    "forward_equal": forward_equal,
                    "inverse_equal": inverse_equal,
                }
            )
    return {
        "bank": bank_count,
        "generator": spec["name"],
        "declared_checkpoints":
            "after every complete controller step, forward and inverse",
        "checkpoint_count": checkpoint_count,
        "events": 2 * bank_count,
        "all_checkpoint_states_equal": not failures,
        "failure": failures[:1],
    }


def construction_commutation_certificate(
    stations: dict[int, int],
    group: dict[str, object],
) -> dict[str, object]:
    specs = generator_specs()
    map_checks = []
    for spec in specs:
        for bank in ALL_BANKS:
            size = stations[bank]
            maps = spec_bank_maps(spec, size)
            domains = {
                "station": set(maps["station"]) == set(range(size)),
                "physical": set(maps["physical"]) == set(range(2 * size)),
                "q_slots": set(maps["q_slots"]) == set(range(size)),
                "layer": set(maps["layer"]) == {0, 1},
                "epochs_fixed": maps["epochs"] == tuple(range(2 * bank)),
                "orientations_fixed": maps["orientations"] == (-1, 1),
            }
            map_checks.append(
                {
                    "bank": bank,
                    "generator": spec["name"],
                    "domains": domains,
                    "all_domains_bijective": all(domains.values()),
                }
            )
    symbolic = tuple(
        symbolic_commutation(bank, spec)
        for bank in ALL_BANKS
        for spec in specs
    )
    checkpoint = tuple(
        checkpoint_commutation(3, spec) for spec in specs
    )
    original_sample_names = {
        "I1_SOURCE_1",
        "I2_ROTATE_1",
        "I3_R_THEN_Q_DESCENDING",
    }
    original_sample_checkpoint_count = sum(
        row["checkpoint_count"]
        for row in checkpoint
        if row["generator"] in original_sample_names
    )
    generator_word_basis = tuple(
        (str(spec["name"]), 1) for spec in specs
    ) + tuple(
        (str(spec["name"]), -1) for spec in specs
    )
    closure_lemma = all(
        (
            bool(group["exact_closure_and_inverse"]),
            all(row["all_domains_bijective"] for row in map_checks),
            all(row["commutes_for_arbitrary_data_state"] for row in symbolic),
            all(row["all_checkpoint_states_equal"] for row in checkpoint),
        )
    )
    return {
        "verified_generator_count": len(specs),
        "complete_generator_word_basis": generator_word_basis,
        "map_cases": len(map_checks),
        "primary_bank_mapping_cases": sum(
            row["bank"] in (1, 2, 3) for row in map_checks
        ),
        "extension_bank_mapping_cases": sum(
            row["bank"] in (5, 12) for row in map_checks
        ),
        "all_mapping_domains_bijective": all(
            row["all_domains_bijective"] for row in map_checks
        ),
        "symbolic_cases": len(symbolic),
        "full_family_symbolic_event_transport_consequences":
            len(specs) * sum(2 * bank for bank in ALL_BANKS),
        "symbolic_operator_comparisons": sum(
            row["forward_inverse_operator_comparisons"] for row in symbolic
        ),
        "all_symbolic_constructions_commute": all(
            row["commutes_for_arbitrary_data_state"] for row in symbolic
        ),
        "checkpoint_bank": 3,
        "checkpoint_generator_cases": len(checkpoint),
        "checkpoint_count": sum(
            row["checkpoint_count"] for row in checkpoint
        ),
        "cycle805_sample_checkpoint_count":
            original_sample_checkpoint_count,
        "same_checkpoint_discipline": (
            original_sample_checkpoint_count == 684
            and all(
                row["declared_checkpoints"]
                == "after every complete controller step, forward and inverse"
                for row in checkpoint
            )
        ),
        "all_checkpoint_states_equal": all(
            row["all_checkpoint_states_equal"] for row in checkpoint
        ),
        "first_mapping_failure": next(
            (row for row in map_checks if not row["all_domains_bijective"]),
            None,
        ),
        "first_symbolic_failure": next(
            (
                row for row in symbolic
                if not row["commutes_for_arbitrary_data_state"]
            ),
            None,
        ),
        "first_checkpoint_failure": next(
            (
                row for row in checkpoint
                if not row["all_checkpoint_states_equal"]
            ),
            None,
        ),
        "composition_inverse_closure_lemma": closure_lemma,
        "all_group_elements_commute_with_construction": closure_lemma,
        "closure_reason":
            "bijections intertwining the construction are closed under "
            "composition and inverse; the exact normal forms cover every "
            "generated element",
    }


def landed_occurrence_rows(
    stations: dict[int, int],
) -> tuple[dict[str, object], ...]:
    rows = []
    for bank in ALL_BANKS:
        program = K719.interleaved_program(bank)
        if len(program) != stations[bank]:
            raise AssertionError(("station drift", bank))
        for fixture in epoch_fixtures(bank):
            selected = S750.enforcement_lineage_selector(
                program,
                fixture["before"],
                fixture["expected"],
                bank,
                tuple(range(len(program))),
            )
            after_banks, after_links = K719.M.unpack_state(
                fixture["expected"], bank
            )
            chain, decode_order = K719.B.decode_local_graph(
                after_banks, after_links
            )
            cell = chain.cells[int(fixture["event"])]
            rows.append(
                {
                    "bank": bank,
                    "epoch": int(fixture["event"]),
                    "direction": tuple(fixture["direction"]),
                    "orientation": int(cell.orientation),
                    "cell_identity": int(cell.identity),
                    "selected": tuple(int(value) for value in selected),
                    "program_stations": len(program),
                    "decode_node": tuple(decode_order[int(fixture["event"])]),
                }
            )
    return tuple(rows)


def orientation_counts(
    rows: tuple[dict[str, object], ...],
) -> dict[str, int]:
    counts = Counter(int(row["orientation"]) for row in rows)
    return {
        "+1": counts[1],
        "-1": counts[-1],
        "other": sum(
            count
            for orientation, count in counts.items()
            if orientation not in (-1, 1)
        ),
        "total": len(rows),
    }


def occurrence_key(row: dict[str, object]) -> tuple[object, ...]:
    return (
        int(row["bank"]),
        int(row["epoch"]),
        tuple(row["direction"]),
        int(row["orientation"]),
        tuple(row["selected"]),
    )


def orientation_candidate_certificate(
    rows: tuple[dict[str, object], ...],
) -> dict[str, object]:
    indexed = {
        (int(row["bank"]), int(row["epoch"])): row for row in rows
    }
    occurrence_transport_checks = []
    for row in rows:
        bank = int(row["bank"])
        epoch = int(row["epoch"])
        direction = tuple(row["direction"])
        mapped_direction = {
            (1, 0): (0, 1),
            (0, 1): (1, 0),
        }[direction]
        mapped = (
            bank,
            epoch ^ 1,
            mapped_direction,
            -int(row["orientation"]),
            tuple(row["selected"]),
        )
        occurrence_transport_checks.append(
            {
                "bank": bank,
                "source_epoch": epoch,
                "target_epoch": epoch ^ 1,
                "maps_exactly":
                    mapped == occurrence_key(indexed[(bank, epoch ^ 1)]),
                "involution_exact": ((epoch ^ 1) ^ 1) == epoch,
            }
        )
    occurrence_pair_checks = []
    for bank in ALL_BANKS:
        for pair in range(bank):
            left = indexed[(bank, 2 * pair)]
            right = indexed[(bank, 2 * pair + 1)]
            mapped_left = (
                bank,
                2 * pair + 1,
                (0, 1),
                -int(left["orientation"]),
                tuple(left["selected"]),
            )
            occurrence_pair_checks.append(
                {
                    "bank": bank,
                    "pair": pair,
                    "epochs": (2 * pair, 2 * pair + 1),
                    "maps_exactly": mapped_left == occurrence_key(right),
                }
            )

    checkpoint_count = 0
    equal_checkpoint_count = 0
    construction_pairs = []
    for bank in ALL_BANKS:
        program = K719.interleaved_program(bank)
        fixtures = epoch_fixtures(bank)
        for pair in range(bank):
            left = fixtures[2 * pair]
            right = fixtures[2 * pair + 1]
            left_after, left_a, left_b, left_forward = run_orbit(
                left["before"],
                program,
                token_position=0,
                reverse=False,
                layer_order="Q_then_R",
                order_mode="ascending",
                checkpoints=True,
            )
            right_after, right_a, right_b, right_forward = run_orbit(
                right["before"],
                program,
                token_position=0,
                reverse=False,
                layer_order="Q_then_R",
                order_mode="ascending",
                checkpoints=True,
            )
            (
                left_restored,
                left_ia,
                left_ib,
                left_inverse,
            ) = run_orbit(
                left_after,
                program,
                token_position=0,
                reverse=True,
                layer_order="Q_then_R",
                order_mode="ascending",
                checkpoints=True,
            )
            (
                right_restored,
                right_ia,
                right_ib,
                right_inverse,
            ) = run_orbit(
                right_after,
                program,
                token_position=0,
                reverse=True,
                layer_order="Q_then_R",
                order_mode="ascending",
                checkpoints=True,
            )
            comparisons = tuple(
                left_row == right_row
                for left_row, right_row in zip(
                    left_forward + left_inverse,
                    right_forward + right_inverse,
                    strict=True,
                )
            )
            checkpoint_count += len(comparisons)
            equal_checkpoint_count += sum(comparisons)
            construction_equal = all(
                (
                    left_after == right_after,
                    left_a == right_a,
                    left_b == right_b,
                    left_forward == right_forward,
                    left_restored == right_restored,
                    left_ia == right_ia,
                    left_ib == right_ib,
                    left_inverse == right_inverse,
                )
            )
            construction_pairs.append(
                {
                    "bank": bank,
                    "pair": pair,
                    "checkpoint_count": len(comparisons),
                    "equal_checkpoint_count": sum(comparisons),
                    "commutes": construction_equal,
                    "left_forward_sha256": digest(left_forward),
                    "right_forward_sha256": digest(right_forward),
                }
            )

    orientation_fixed_by_every_805_generator = all(
        maps["orientations"] == (-1, 1)
        for spec in generator_specs()
        for bank in ALL_BANKS
        for maps in (spec_bank_maps(spec, EXPECTED_STATIONS[bank]),)
    )
    epochs_fixed_by_every_805_generator = all(
        maps["epochs"] == tuple(range(2 * bank))
        for spec in generator_specs()
        for bank in ALL_BANKS
        for maps in (spec_bank_maps(spec, EXPECTED_STATIONS[bank]),)
    )
    in_generated_group = not all(
        (
            orientation_fixed_by_every_805_generator,
            epochs_fixed_by_every_805_generator,
        )
    )
    occurrence_projection_pairs = all(
        row["maps_exactly"] for row in occurrence_transport_checks
    )
    candidate_involution = all(
        row["involution_exact"] for row in occurrence_transport_checks
    )
    construction_commutes = all(
        row["commutes"] for row in construction_pairs
    )
    verified_commuting_extension = construction_commutes
    admitted = in_generated_group or verified_commuting_extension
    return {
        "candidate":
            "(bank,epoch,direction,orientation,station) -> "
            "(bank,epoch xor 1,swapped_direction,-orientation,station)",
        "pair_count": len(occurrence_pair_checks),
        "event_transport_count": len(occurrence_transport_checks),
        "occurrence_projection_pairs_exact": occurrence_projection_pairs,
        "candidate_involution_exact": candidate_involution,
        "orientation_fixed_by_every_805_generator":
            orientation_fixed_by_every_805_generator,
        "epochs_fixed_by_every_805_generator":
            epochs_fixed_by_every_805_generator,
        "in_generated_group": in_generated_group,
        "same_evidence_state_action":
            "identity on constructor data state, as in the Cycle-805 maps",
        "constructor_checkpoint_count": checkpoint_count,
        "equal_constructor_checkpoint_count": equal_checkpoint_count,
        "construction_commutes": construction_commutes,
        "verified_commuting_extension": verified_commuting_extension,
        "first_construction_failure": next(
            (row for row in construction_pairs if not row["commutes"]),
            None,
        ),
        "admitted_to_group": admitted,
        "outcome": (
            "IN_G"
            if in_generated_group
            else (
                "VERIFIED_COMMUTING_EXTENSION"
                if verified_commuting_extension
                else "NOT_IN_G_NO_VERIFIED_COMMUTING_EXTENSION"
            )
        ),
        "nontrivial_constructor_state_lifts_exhausted": False,
        "honest_boundary":
            "the parity map is an exact occurrence-level pairing but fails "
            "with the Cycle-805 identity action on constructor data state; "
            "no nontrivial constructor-state lift is claimed excluded",
    }


def push_occurrence_counter(
    counter: Counter[tuple[object, ...]],
    spec: dict[str, object],
    stations: dict[int, int],
) -> Counter[tuple[object, ...]]:
    output: Counter[tuple[object, ...]] = Counter()
    for key, multiplicity in counter.items():
        bank, epoch, direction, orientation, selected = key
        station_map = spec_bank_maps(spec, stations[int(bank)])["station"]
        mapped_selected = tuple(
            sorted(station_map[int(value)] for value in selected)
        )
        output[
            (
                bank,
                epoch,
                direction,
                orientation,
                mapped_selected,
            )
        ] += multiplicity
    return output


def universal_orbit_lemma(
    points: tuple[int, ...],
    generators: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    """Certify the arbitrary-count implication by generator-edge closure."""
    parent = {point: point for point in points}

    def find(point: int) -> int:
        while parent[point] != point:
            parent[point] = parent[parent[point]]
            point = parent[point]
        return point

    def union(left: int, right: int) -> None:
        left_root = find(left)
        right_root = find(right)
        if left_root != right_root:
            parent[right_root] = left_root

    all_generators_bijective = all(
        set(permutation) == set(points) for permutation in generators
    )
    for permutation in generators:
        for point in points:
            union(point, permutation[point])
    components: dict[int, set[int]] = {}
    for point in points:
        components.setdefault(find(point), set()).add(point)
    edge_components = tuple(
        sorted(tuple(sorted(component)) for component in components.values())
    )
    computed_orbits = tuple(sorted(permutation_orbits(points, generators)))
    return {
        "all_generators_bijective": all_generators_bijective,
        "generator_edge_components": edge_components,
        "computed_orbits": computed_orbits,
        "edge_components_equal_orbits":
            edge_components == computed_orbits,
        "arbitrary_count_implication_exact": (
            all_generators_bijective
            and edge_components == computed_orbits
        ),
        "statement":
            "for every integer-valued occurrence multiplicity c, "
            "c(x)=c(gx) for every generator edge implies c is constant "
            "on every generated orbit",
    }


def finite_orbit_implication(
    counts: Counter[int],
    points: tuple[int, ...],
    generators: tuple[tuple[int, ...], ...],
) -> dict[str, object]:
    invariant_generators = []
    for permutation in generators:
        pushed = Counter(
            {
                permutation[point]: counts[point]
                for point in points
            }
        )
        invariant_generators.append(pushed == counts)
    orbits = permutation_orbits(points, generators)
    orbit_uniform = tuple(
        len({counts[point] for point in orbit}) == 1 for orbit in orbits
    )
    invariant = all(invariant_generators)
    universal = universal_orbit_lemma(points, generators)
    return {
        "generator_invariant": invariant,
        "orbits": orbits,
        "orbit_uniform": orbit_uniform,
        "universal_lemma": universal,
        "implication_exact": (
            universal["arbitrary_count_implication_exact"]
            and ((not invariant) or all(orbit_uniform))
        ),
        "proof_kernel":
            "generator equality propagates along each finite orbit word",
    }


def corollary_certificate(
    rows: tuple[dict[str, object], ...],
    stations: dict[int, int],
    candidate: dict[str, object],
) -> dict[str, object]:
    occurrence_counter = Counter(occurrence_key(row) for row in rows)
    generator_transport = {}
    for spec in generator_specs():
        pushed = push_occurrence_counter(occurrence_counter, spec, stations)
        generator_transport[str(spec["name"])] = pushed == occurrence_counter
    occurrence_g_invariant = all(generator_transport.values())

    station_implications = {}
    for bank in ALL_BANKS:
        size = stations[bank]
        bank_counts = Counter(
            {
                station: sum(
                    1
                    for row in rows
                    if int(row["bank"]) == bank
                    and station in tuple(row["selected"])
                )
                for station in range(size)
            }
        )
        generators = tuple(
            tuple(spec_bank_maps(spec, size)["station"])
            for spec in generator_specs()
        )
        station_implications[bank] = finite_orbit_implication(
            bank_counts, tuple(range(size)), generators
        )

    counted = orientation_counts(rows)
    orientation_orbits = ((-1,), (1,))
    orientation_universal_lemma = universal_orbit_lemma(
        (0, 1),
        tuple((0, 1) for _spec in generator_specs()),
    )
    orientation_nontrivial_orbit = any(
        len(orbit) > 1 for orbit in orientation_orbits
    )
    parity_counterfactual = {
        "orientation_orbit_if_admitted": ((-1, 1),),
        "occurrence_projection_invariant":
            candidate["occurrence_projection_pairs_exact"],
        "would_predict_each":
            Fraction(counted["total"], 2),
        "would_match_counted": (
            counted["+1"] == counted["-1"] == counted["total"] // 2
        ),
        "usable": candidate["admitted_to_group"],
    }
    finite_implications_exact = all(
        row["implication_exact"] for row in station_implications.values()
    )
    zero_counting_orientation_derivation = all(
        (
            occurrence_g_invariant,
            orientation_nontrivial_orbit,
            candidate["admitted_to_group"],
        )
    )
    return {
        "finite_invariance_implies_orbit_uniformity":
            finite_implications_exact,
        "generator_transport": generator_transport,
        "occurrence_multiset_G_invariant": occurrence_g_invariant,
        "first_invariance_failure": next(
            (
                name for name, passed in generator_transport.items()
                if not passed
            ),
            None,
        ),
        "station_implications": station_implications,
        "orientation_G_orbits": orientation_orbits,
        "orientation_universal_orbit_lemma": orientation_universal_lemma,
        "orientation_nontrivial_G_orbit": orientation_nontrivial_orbit,
        "counted_orientation": counted,
        "derived_orientation_prediction": (
            {"+1": 23, "-1": 23}
            if zero_counting_orientation_derivation
            else None
        ),
        "zero_counting_orientation_derivation":
            zero_counting_orientation_derivation,
        "parity_counterfactual_not_admitted": parity_counterfactual,
        "count_comparison": (
            "DERIVED_23_23_MATCHES_COUNT"
            if zero_counting_orientation_derivation
            else "COUNTED_23_23_NOT_A_G_COROLLARY"
        ),
        "corollary_status": (
            "PROVED"
            if zero_counting_orientation_derivation
            else "DERIVATION_FAILS"
        ),
    }


def uniformity_law_certificate(
    rows: tuple[dict[str, object], ...],
    stations: dict[int, int],
    orbit_rows: tuple[dict[str, object], ...],
    corollary: dict[str, object],
) -> dict[str, object]:
    laws = []
    for orbit_row in orbit_rows:
        domain = str(orbit_row["domain"])
        bank = orbit_row["bank"]
        for orbit in orbit_row["orbits"]:
            if len(orbit) <= 1:
                continue
            if domain == "station":
                observed = {
                    int(label): sum(
                        1
                        for row in rows
                        if int(row["bank"]) == int(bank)
                        and int(label) in tuple(row["selected"])
                    )
                    for label in orbit
                }
                total = sum(observed.values())
                predicted = Fraction(total, len(orbit))
                verified = (
                    bool(corollary["occurrence_multiset_G_invariant"])
                    and all(Fraction(value) == predicted for value in observed.values())
                )
                status = (
                    "DERIVED_AND_VERIFIED"
                    if verified
                    else "NOT_DERIVABLE_OCCURRENCE_NOT_G_INVARIANT"
                )
                marginal = f"selected_station_at_bank_{bank}"
            else:
                observed = None
                predicted = None
                verified = False
                status = "NO_TYPED_OCCURRENCE_MARGINAL"
                marginal = None
            laws.append(
                {
                    "domain": domain,
                    "bank": bank,
                    "orbit": orbit,
                    "marginal": marginal,
                    "predicted_exact_uniformity": predicted,
                    "observed_counts": observed,
                    "verified": verified,
                    "status": status,
                }
            )
    verified = tuple(row for row in laws if row["verified"])
    return {
        "nontrivial_label_orbits": len(laws),
        "candidate_laws": tuple(laws),
        "derived_and_verified_laws": len(verified),
        "new_derived_and_verified_laws": len(verified),
        "orientation_excluded_from_new_count": True,
        "status": (
            "UNIFORMITY_LAWS_DERIVED"
            if verified
            else "NO_UNIFORMITY_LAWS_DERIVABLE_FROM_G_ON_LANDED_OCCURRENCES"
        ),
    }


def build_core() -> dict[str, object]:
    stations = {
        bank: len(K719.interleaved_program(bank)) for bank in ALL_BANKS
    }
    group = exact_group_certificate(stations)
    commutation = construction_commutation_certificate(stations, group)
    rows = landed_occurrence_rows(stations)
    candidate = orientation_candidate_certificate(rows)
    corollary = corollary_certificate(rows, stations, candidate)
    orbit_rows = all_label_orbits(stations)
    laws = uniformity_law_certificate(
        rows, stations, orbit_rows, corollary
    )
    return {
        "stations": stations,
        "group": group,
        "commutation": commutation,
        "landed_occurrence_rows_sha256": digest(rows),
        "landed_occurrence_count": len(rows),
        "landed_selected_exact": all(
            tuple(row["selected"]) == (0,) for row in rows
        ),
        "landed_cell_identity_exact": all(
            int(row["cell_identity"]) == int(row["epoch"]) for row in rows
        ),
        "orientation_candidate": candidate,
        "corollary": corollary,
        "label_orbits": orbit_rows,
        "uniformity_laws": laws,
    }


def main() -> int:
    input_sha_before = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    controls = package_text_audit()
    first = build_core()

    group = first["group"]
    commutation = first["commutation"]
    certificate_a = all(
        (
            first["stations"] == EXPECTED_STATIONS,
            group["station_modulus"] == 285285,
            group["group_order"] == 58599022482000,
            group["exact_closure_and_inverse"],
            commutation["verified_generator_count"] == 9,
            commutation["primary_bank_mapping_cases"] == 27,
            commutation["extension_bank_mapping_cases"] == 18,
            commutation["all_mapping_domains_bijective"],
            commutation["symbolic_cases"] == 45,
            commutation[
                "full_family_symbolic_event_transport_consequences"
            ] == 414,
            commutation["all_symbolic_constructions_commute"],
            commutation["checkpoint_count"] == 2052,
            commutation["same_checkpoint_discipline"],
            commutation["all_checkpoint_states_equal"],
            commutation["all_group_elements_commute_with_construction"],
        )
    )
    emit("GROUP_ORDER", group["group_order"])
    emit("GROUP_PRESENTATION", group["presentation"])
    emit("GROUP_NORMAL_FORM", group["normal_form"])
    for name, row in group["raw_generators"].items():
        emit("GROUP_GENERATOR", name, "::", compact(row))
    check(
        "CERTIFICATE_A_EXACT_GAUGE_GROUP_AND_COMMUTATION",
        certificate_a,
        {
            "group_order": group["group_order"],
            "station_modulus": group["station_modulus"],
            "multiplier_group_order": group["multiplier_group_order"],
            "presentation": group["presentation"],
            "normal_form": group["normal_form"],
            "exact_closure_and_inverse": group["exact_closure_and_inverse"],
            "canonical_basis":
                group["canonical_basis_derived_from_verified_generators"],
            "presentation_relations": group["presentation_relations"],
            "commutation": commutation,
        },
    )

    candidate = first["orientation_candidate"]
    certificate_b = all(
        (
            first["landed_occurrence_count"] == 46,
            first["landed_selected_exact"],
            first["landed_cell_identity_exact"],
            candidate["pair_count"] == 23,
            candidate["event_transport_count"] == 46,
            candidate["occurrence_projection_pairs_exact"],
            candidate["candidate_involution_exact"],
            candidate["orientation_fixed_by_every_805_generator"],
            candidate["epochs_fixed_by_every_805_generator"],
            not candidate["in_generated_group"],
            candidate["constructor_checkpoint_count"] == 2698,
            candidate["equal_constructor_checkpoint_count"] == 0,
            not candidate["construction_commutes"],
            not candidate["verified_commuting_extension"],
            not candidate["admitted_to_group"],
            candidate["outcome"]
            == "NOT_IN_G_NO_VERIFIED_COMMUTING_EXTENSION",
            not candidate["nontrivial_constructor_state_lifts_exhausted"],
        )
    )
    emit("ORIENTATION_ELEMENT_OUTCOME", candidate["outcome"])
    check(
        "CERTIFICATE_B_ORIENTATION_ELEMENT_EVIDENCE_BAR",
        certificate_b,
        candidate,
    )

    corollary = first["corollary"]
    certificate_c = all(
        (
            corollary["finite_invariance_implies_orbit_uniformity"],
            not corollary["occurrence_multiset_G_invariant"],
            corollary["orientation_G_orbits"] == ((-1,), (1,)),
            corollary["orientation_universal_orbit_lemma"][
                "arbitrary_count_implication_exact"
            ],
            not corollary["orientation_nontrivial_G_orbit"],
            corollary["counted_orientation"]
            == {"+1": 23, "-1": 23, "other": 0, "total": 46},
            corollary["derived_orientation_prediction"] is None,
            not corollary["zero_counting_orientation_derivation"],
            corollary["count_comparison"]
            == "COUNTED_23_23_NOT_A_G_COROLLARY",
            corollary["corollary_status"] == "DERIVATION_FAILS",
        )
    )
    emit("COROLLARY_STATUS", corollary["corollary_status"])
    check(
        "CERTIFICATE_C_FINITE_COROLLARY_AND_FAILED_ANTECEDENT",
        certificate_c,
        corollary,
    )

    for row in first["label_orbits"]:
        for orbit in row["orbits"]:
            emit(
                "LABEL_ORBIT",
                f"domain={row['domain']}",
                f"bank={row['bank']}",
                "::",
                compact(orbit),
            )
    laws = first["uniformity_laws"]
    for law in laws["candidate_laws"]:
        emit("UNIFORMITY_LAW", "::", compact(law))
    certificate_d = all(
        (
            laws["nontrivial_label_orbits"] == 21,
            laws["derived_and_verified_laws"] == 0,
            laws["new_derived_and_verified_laws"] == 0,
            laws["orientation_excluded_from_new_count"],
            laws["status"]
            == "NO_UNIFORMITY_LAWS_DERIVABLE_FROM_G_ON_LANDED_OCCURRENCES",
            all(
                not row["verified"] for row in laws["candidate_laws"]
            ),
        )
    )
    check(
        "CERTIFICATE_D_COMPLETE_ORBITS_AND_UNIFORMITY_LAWS",
        certificate_d,
        laws,
    )

    scope = (
        "46-epoch landed occurrence family at banks 1/2/3/5/12, under "
        "the nine censused lawful Cycle-805 selecting-supply variations "
        "and their generated relabeling closure; occurrence counts only"
    )
    scope_basis = {
        "banks_exact": tuple(first["stations"]) == ALL_BANKS,
        "landed_epoch_count_exact": first["landed_occurrence_count"] == 46,
        "censused_variation_count_exact":
            commutation["verified_generator_count"] == 9,
        "primary_bijection_count_exact":
            commutation["primary_bank_mapping_cases"] == 27,
        "extension_bijection_count_exact":
            commutation["extension_bank_mapping_cases"] == 18,
        "full_family_symbolic_event_transport_count_exact":
            commutation[
                "full_family_symbolic_event_transport_consequences"
            ] == 414,
        "generated_closure_is_not_an_additional_census": True,
        "occurrence_rows_rebuilt_from_landed_machinery":
            first["landed_selected_exact"]
            and first["landed_cell_identity_exact"],
    }
    certificate_e = all(scope_basis.values())
    check(
        "CERTIFICATE_E_SCOPE_HONESTY",
        certificate_e,
        {
            "scope": scope,
            "scope_basis": scope_basis,
            "occurrence_counts_only": True,
        },
    )

    second = build_core()
    input_sha_after = {
        path: file_sha256(path) for path in AUDIT_INPUT_PATHS
    }
    deterministic = first == second
    elapsed = monotonic() - START
    direct_control_keys = (
        "literal_AUDIT_INPUT_PATHS",
        "DECLARED_INPUT_PATHS_alias",
        "paths_worktree_relative",
        "all_paths_exist",
        "blocklisted_not_AST_imported",
        "blocklisted_not_literal_dynamic_imported",
        "blocklisted_not_loaded",
        "runtime_blocker_installed",
    )
    controls_pass = all(
        (
            all(bool(controls[key]) for key in direct_control_keys),
            all(controls["runtime_attempts"].values()),
            all(controls["source_anchors"].values()),
            input_sha_before == input_sha_after == EXPECTED_INPUT_SHA256,
            deterministic,
            elapsed < AUDIT_TIMEOUT_SEC,
        )
    )
    for path in AUDIT_INPUT_PATHS:
        emit("AUDIT_INPUT_SHA256", path, input_sha_after[path])
    stdout_before_f = len(
        ("\n".join(OUTPUT_LINES) + "\n").encode("utf-8")
    )
    early_stdout_bytes = COUNTING_STDOUT.bytes_written
    certificate_f = (
        controls_pass
        and early_stdout_bytes + stdout_before_f + 16 * 1024
        < STDOUT_LIMIT_BYTES
    )
    check(
        "CERTIFICATE_F_CONTROLS_DETERMINISM_AND_BOUNDS",
        certificate_f,
        {
            "text_AST_only_blocklist": controls,
            "input_sha256_before": input_sha_before,
            "input_sha256_after": input_sha_after,
            "expected_input_sha256": EXPECTED_INPUT_SHA256,
            "input_stability": input_sha_before == input_sha_after,
            "deterministic": deterministic,
            "first_core_sha256": digest(first),
            "repeat_core_sha256": digest(second),
            "runtime_seconds": round(elapsed, 6),
            "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
            "stdout_bytes_before_buffered_output": early_stdout_bytes,
            "stdout_bytes_before_certificate_F": stdout_before_f,
            "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        },
    )

    stable_report = {
        "cycle": 808,
        "runner_certificates_pass": all(CHECKS.values()),
        "scientific_outcome": "NEGATIVE_DERIVATION_RESULT",
        "certificates": dict(CHECKS),
        "group_order": group["group_order"],
        "orientation_element_outcome": candidate["outcome"],
        "corollary_status": corollary["corollary_status"],
        "counted_orientation": corollary["counted_orientation"],
        "new_uniformity_laws_derived_and_verified":
            laws["new_derived_and_verified_laws"],
        "scope": scope,
    }
    report = {
        **stable_report,
        "runtime_seconds": round(elapsed, 6),
    }
    report["stable_report_sha256"] = digest(stable_report)
    emit("SUMMARY_JSON", compact(report))
    emit(
        "CYCLE808_NEGATIVE_DERIVATION_RESULT_CERTIFIED"
        if report["runner_certificates_pass"]
        else "CYCLE808_CERTIFICATE_FAILURE"
    )
    output = "\n".join(OUTPUT_LINES) + "\n"
    output_bytes = len(output.encode("utf-8"))
    if early_stdout_bytes + output_bytes >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            (
                "stdout bound",
                early_stdout_bytes + output_bytes,
                STDOUT_LIMIT_BYTES,
            )
        )
    sys.stdout.write(output)
    return 0 if report["runner_certificates_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
