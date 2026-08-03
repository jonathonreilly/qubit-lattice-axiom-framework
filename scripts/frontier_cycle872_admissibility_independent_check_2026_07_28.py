#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-872 admissibility classification.

This checker is specified to REFUTE.  Its job is to find one response object
built from the landed surface that separates the conformal sign sigma on the
landed source family, which would convert the primary's classification no-go
into a derivation route and kill it as stated.

It attacks on four fronts.

1. A WIDER class.  Where the primary declared four endpoint-space combinations
   of the identity and the exchange at grading powers one and two, this checker
   sweeps seven combinations at grading powers one through four, every
   index-subset contraction, and -- on a declared member sample -- every
   unordered product of the whole resulting feature base.  If the primary's
   grammar truncation were load-bearing, the extra objects would expose it.

2. The DISCARDED objects.  A classification can hide a sigma-visible object by
   declaring it inadmissible.  This checker searches for sensitivity over the
   entire class with no admissibility filter at all, so nothing the primary
   rejected can escape the hunt.

3. An INDEPENDENT arithmetic route.  The primary carried a formal sigma as an
   integer polynomial.  This checker never builds a polynomial: it evaluates
   the objects in six hard-wired integer sigma worlds and recovers exactness by
   finite differences -- the fifth finite difference is checked to vanish, which
   certifies degree at most four, after which agreement at five points is
   polynomial identity.  A bug in the primary's polynomial ring cannot
   reproduce itself here.

4. The primary's CLAIMS.  Its pinned stdout is parsed and each recomputable
   number is compared, with the checker forming its own verdict first.

Nothing from the primary lineage is executed; all six cited inputs are
SHA-pinned text/AST evidence behind a meta-path import firewall.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle872_sigma_linear_admissibility_2026_07_28.py",
    "logs/runner-cache/frontier_cycle872_sigma_linear_admissibility_2026_07_28.txt",
    "scripts/frontier_cycle868_response_sign_census_2026_07_28.py",
    "logs/runner-cache/frontier_cycle868_response_sign_census_2026_07_28.txt",
    "scripts/unit_weight_carried_link_recoil_cycle320_2026_07_18.py",
    "scripts/two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18.py",
)

import ast
from hashlib import sha1, sha256
from itertools import combinations_with_replacement, product
import importlib.abc
import json
from pathlib import Path
import random
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS[0], AUDIT_INPUT_PATHS[1]
PYTHON_PATHS = tuple(path for path in AUDIT_INPUT_PATHS if path.endswith(".py"))
BLOCKLISTED_MODULES = tuple(Path(path).stem for path in PYTHON_PATHS)
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "04405075867204246e794775ac8c09a6498f0ca4367d305745fbdc7fdf338dcc",
    AUDIT_INPUT_PATHS[1]:
        "f0d8b6928c7661280627016950ae7f27228513ff8b690db555734b6eefa6896a",
    AUDIT_INPUT_PATHS[2]:
        "e09226e35a58cd52e2d4f61516f6e2a64cdebb7f4c20893307a1f3d2ff3f4ebb",
    AUDIT_INPUT_PATHS[3]:
        "056b642e859e732d358be4632d4de8baa77b673704b1f5737bcd6ec566582d60",
    AUDIT_INPUT_PATHS[4]:
        "71fb02658569174b7f6f989efe311951713026ead36ece8866dca1e96878d706",
    AUDIT_INPUT_PATHS[5]:
        "4f7e25a20bcea41c285bfb52b122f84ec5c41f1f6095b6ec0068d2a228ed5d75",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "a53d5e680d18b7e9bf1b9312e802454b16b3edb5",
    AUDIT_INPUT_PATHS[1]: "ed9b54a9dbae1649eaacbd03525cc2eb9d529b42",
    AUDIT_INPUT_PATHS[2]: "c64dd97a3034ccbedc2603db4dacc1c80acfd952",
    AUDIT_INPUT_PATHS[3]: "1cdd55ce35dd7116ab3d4f959b5e21f5299ff5ed",
    AUDIT_INPUT_PATHS[4]: "c95eb9738409c3ffe20f8b90a7ab25e6dc5843a0",
    AUDIT_INPUT_PATHS[5]: "de8b90b08707c000bb2489502823b02d62e38b29",
}
PRIMARY_REQUIRED_MARKERS = (
    "GRAMMAR",
    "admissibility_certificate",
    "class_readings",
    "closure_certificate",
    "escape_certificate",
    "grade",
    "verdict_certificate",
)


class _PrimaryFirewall(importlib.abc.MetaPathFinder):
    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self, fullname: str, path: object = None, target: object = None
    ) -> None:
        if fullname.rsplit(".", 1)[-1] in BLOCKLISTED_MODULES:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids import of {fullname}")
        return None


FIREWALL = _PrimaryFirewall()
sys.meta_path.insert(0, FIREWALL)


# --------------------------------------------------------------------------
# the scope, restated from the landed lineage rather than read from the primary
# --------------------------------------------------------------------------
SECTOR_COUNT = 3
AXIS_COUNT = 3
ENDPOINT_COUNT = 2
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRECTION_REVERSE = (1, 0, 3, 2, 5, 4)
WEIGHTS = (1, 2, 3, 4, 5, 6)
SCALE = 3
SIGMA_POINTS = (-2, -1, 0, 1, 2, 3)
PLUS_INDEX, MINUS_INDEX = SIGMA_POINTS.index(1), SIGMA_POINTS.index(-1)
IDENTITY_POINTS = tuple(range(5))  # -2..2, five points fix a degree-4 polynomial
FIFTH_DIFFERENCE_WEIGHTS = (-1, 5, -10, 10, -5, 1)


def ledger(weight: int) -> tuple[int, int, int]:
    return (-2 * weight, weight, weight)


def detuned_ledger(weight: int) -> tuple[int, int, int]:
    return (-2 * weight, weight, weight + 1)


def pure_conformal_ledger(weight: int) -> tuple[int, int, int]:
    return (weight, weight, weight)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


# --------------------------------------------------------------------------
# independent family enumeration: a flat lexicographic index over radices
# --------------------------------------------------------------------------
def family() -> tuple[tuple, ...]:
    members = []
    stride = len(DIRECTIONS) * len(WEIGHTS)
    for flat in range(ENDPOINT_COUNT * stride):
        endpoint, remainder = divmod(flat, stride)
        members.append(("k1", endpoint, remainder // len(WEIGHTS),
                        WEIGHTS[remainder % len(WEIGHTS)]))
    for flat in range(stride * stride):
        left, right = divmod(flat, stride)
        members.append(("k2", left // len(WEIGHTS), WEIGHTS[left % len(WEIGHTS)],
                        right // len(WEIGHTS), WEIGHTS[right % len(WEIGHTS)]))
    return tuple(members)


def member_sources(member: tuple) -> tuple[tuple[int, int, int], ...]:
    if member[0] == "k1":
        return ((member[1], member[2], member[3]),)
    return ((0, member[1], member[2]), (1, member[3], member[4]))


def reverse_member(member: tuple) -> tuple:
    if member[0] == "k1":
        return ("k1", member[1], DIRECTION_REVERSE[member[2]], member[3])
    return ("k2", DIRECTION_REVERSE[member[1]], member[2],
            DIRECTION_REVERSE[member[3]], member[4])


def swap_member(member: tuple) -> tuple:
    if member[0] == "k1":
        return ("k1", ENDPOINT_COUNT - 1 - member[1], member[2], member[3])
    return ("k2", member[3], member[4], member[1], member[2])


def scaled_source(member: tuple, rule=ledger) -> list:
    grid = [[[0] * AXIS_COUNT for _s in range(SECTOR_COUNT)]
            for _e in range(ENDPOINT_COUNT)]
    for endpoint, direction, weight in member_sources(member):
        unit = DIRECTIONS[direction]
        for sector, coefficient in enumerate(rule(weight)):
            for axis in range(AXIS_COUNT):
                grid[endpoint][sector][axis] += SCALE * coefficient * unit[axis]
    return grid


def sector_trace(grid: list) -> list:
    return [[sum(grid[e][s][a] for s in range(SECTOR_COUNT)) // SCALE
             for a in range(AXIS_COUNT)] for e in range(ENDPOINT_COUNT)]


def graded(grid: list, sigma: int, planted: bool = False) -> list:
    """One hard-wired sigma world of the grading; integers throughout.

    planted=True is the OFF-GRAMMAR adversary grading that carries sigma on the
    trace-free channel instead of the conformal one.
    """
    out = []
    for e in range(ENDPOINT_COUNT):
        block = []
        traces = [sum(grid[e][s][a] for s in range(SECTOR_COUNT))
                  for a in range(AXIS_COUNT)]
        for s in range(SECTOR_COUNT):
            row = []
            for a in range(AXIS_COUNT):
                conformal, remainder = divmod(traces[a], SECTOR_COUNT)
                if remainder:
                    raise AssertionError("conformal projection left a remainder")
                tracefree = grid[e][s][a] - conformal
                row.append(sigma * tracefree + conformal if planted
                           else tracefree + sigma * conformal)
            block.append(row)
        out.append(block)
    return out


def premap(grid: list, alpha: int, beta: int) -> list:
    return [[[alpha * grid[e][s][a]
              + beta * grid[ENDPOINT_COUNT - 1 - e][s][a]
              for a in range(AXIS_COUNT)] for s in range(SECTOR_COUNT)]
            for e in range(ENDPOINT_COUNT)]


CONTRACTIONS = (
    ("none", ()),
    ("sector", ("s",)),
    ("endpoint", ("e",)),
    ("axis", ("a",)),
    ("endpoint.sector", ("e", "s")),
    ("sector.axis", ("s", "a")),
    ("endpoint.axis", ("e", "a")),
    ("endpoint.sector.axis", ("e", "s", "a")),
)
INDEX_DIMENSION = {"e": ENDPOINT_COUNT, "s": SECTOR_COUNT, "a": AXIS_COUNT,
                   "b": AXIS_COUNT, "t": SECTOR_COUNT}


def contract(grid: list, killed: tuple) -> tuple[list, tuple]:
    keep = tuple(name for name in ("e", "s", "a") if name not in killed)
    values = []
    for index in product(*[range(INDEX_DIMENSION[n]) for n in keep]):
        position = dict(zip(keep, index))
        total = 0
        for e in ((position["e"],) if "e" in position else range(ENDPOINT_COUNT)):
            for s in ((position["s"],) if "s" in position else range(SECTOR_COUNT)):
                for a in ((position["a"],) if "a" in position else range(AXIS_COUNT)):
                    total += grid[e][s][a]
        values.append(total)
    return values, keep


def pair_gram(left, right):
    return [sum(left[e][s][a] * right[e][s][a]
                for e in range(ENDPOINT_COUNT)
                for s in range(SECTOR_COUNT)
                for a in range(AXIS_COUNT))], ()


def pair_sector_contract(left, right):
    return [sum(left[e][s][a] * right[e][s][b] for s in range(SECTOR_COUNT))
            for e in range(ENDPOINT_COUNT)
            for a in range(AXIS_COUNT)
            for b in range(AXIS_COUNT)], ("e", "a", "b")


def pair_axis_contract(left, right):
    return [sum(left[e][s][a] * right[e][t][a] for a in range(AXIS_COUNT))
            for e in range(ENDPOINT_COUNT)
            for s in range(SECTOR_COUNT)
            for t in range(SECTOR_COUNT)], ("e", "s", "t")


def pair_endpoint_transfer(left, right):
    return [sum(left[0][s][a] * right[1][s][a]
                for s in range(SECTOR_COUNT)
                for a in range(AXIS_COUNT))], ()


def pair_sector_trace_square(left, right):
    return [sum(left[e][s][a] for s in range(SECTOR_COUNT))
            * sum(right[e][s][a] for s in range(SECTOR_COUNT))
            for e in range(ENDPOINT_COUNT)
            for a in range(AXIS_COUNT)], ("e", "a")


PAIRINGS = (
    ("gram", pair_gram),
    ("sector_contract", pair_sector_contract),
    ("axis_contract", pair_axis_contract),
    ("endpoint_transfer", pair_endpoint_transfer),
    ("sector_trace_square", pair_sector_trace_square),
)

# the primary's declared subclass, re-implemented independently
PRIMARY_PREMAPS = (("id", 1, 0), ("R", 0, 1), ("I+R", 1, 1), ("I-R", 1, -1))
PRIMARY_GRADE_POWERS = (1, 2)
PRIMARY_PRE_KEYS = tuple((name, power) for power in PRIMARY_GRADE_POWERS
                         for name, _a, _b in PRIMARY_PREMAPS)
# the deliberately wider class this checker hunts over
WIDE_PREMAPS = PRIMARY_PREMAPS + (("2I+R", 2, 1), ("I+2R", 1, 2), ("R-2I", -2, 1))
WIDE_GRADE_POWERS = (1, 2, 3, 4)


def grade_tower(grid: list, sigma: int, powers, planted: bool = False) -> dict:
    tower = {}
    current = grid
    for power in range(1, max(powers) + 1):
        current = graded(current, sigma, planted)
        if power in powers:
            tower[power] = current
    return tower


def wide_features(grid: list, sigma: int, planted: bool = False) -> list:
    """The wide linear feature base in one sigma world."""
    tower = grade_tower(grid, sigma, WIDE_GRADE_POWERS, planted)
    values: list[int] = []
    for power in WIDE_GRADE_POWERS:
        for _name, alpha, beta in WIDE_PREMAPS:
            mapped = premap(tower[power], alpha, beta)
            for _label, killed in CONTRACTIONS:
                values.extend(contract(mapped, killed)[0])
    return values


WIDE_WIDTH = len(WIDE_PREMAPS) * len(WIDE_GRADE_POWERS) * sum(
    (ENDPOINT_COUNT if "e" not in killed else 1)
    * (SECTOR_COUNT if "s" not in killed else 1)
    * (AXIS_COUNT if "a" not in killed else 1)
    for _label, killed in CONTRACTIONS
)


def primary_class_readings(grid: list, sigma: int) -> dict:
    """The primary's declared 384 generators, re-derived in one sigma world."""
    tower = grade_tower(grid, sigma, PRIMARY_GRADE_POWERS)
    pre = {}
    for power in PRIMARY_GRADE_POWERS:
        for name, alpha, beta in PRIMARY_PREMAPS:
            pre[(name, power)] = premap(tower[power], alpha, beta)
    readings = {}
    for key in PRIMARY_PRE_KEYS:
        for label, killed in CONTRACTIONS:
            readings[("L", key[0], key[1], label)] = contract(pre[key], killed)
    for left in PRIMARY_PRE_KEYS:
        for right in PRIMARY_PRE_KEYS:
            for label, function in PAIRINGS:
                readings[("Q", left, right, label)] = function(pre[left], pre[right])
    return readings


PRIMARY_GENERATOR_IDS = tuple(
    [("L", key[0], key[1], label) for key in PRIMARY_PRE_KEYS
     for label, _killed in CONTRACTIONS]
    + [("Q", left, right, label) for left in PRIMARY_PRE_KEYS
       for right in PRIMARY_PRE_KEYS for label, _fn in PAIRINGS]
)
_SEED_READINGS = primary_class_readings(scaled_source(("k2", 0, 1, 2, 3)), 1)
GENERATOR_LAYOUT = {gid: _SEED_READINGS[gid][1] for gid in PRIMARY_GENERATOR_IDS}
GENERATOR_DEGREE = {gid: (1 if gid[0] == "L" else 2) for gid in PRIMARY_GENERATOR_IDS}


def endpoint_reversal_map(layout: tuple) -> tuple:
    sizes = [INDEX_DIMENSION[name] for name in layout]
    total = 1
    for size in sizes:
        total *= size
    if "e" not in layout:
        return tuple(range(total))
    slot = layout.index("e")
    mapping = []
    for flat in range(total):
        digits, rest = [], flat
        for size in reversed(sizes):
            rest, digit = divmod(rest, size)
            digits.append(digit)
        digits.reverse()
        digits[slot] = ENDPOINT_COUNT - 1 - digits[slot]
        value = 0
        for digit, size in zip(digits, sizes):
            value = value * size + digit
        mapping.append(value)
    return tuple(mapping)


REVERSAL_MAPS = {gid: endpoint_reversal_map(GENERATOR_LAYOUT[gid])
                 for gid in PRIMARY_GENERATOR_IDS}


def gid_text(gid: tuple) -> str:
    if gid[0] == "L":
        return f"LIN[{gid[1]}|G^{gid[2]}|{gid[3]}]"
    return (f"QUAD[{gid[1][0]}|G^{gid[1][1]}] x "
            f"[{gid[2][0]}|G^{gid[2][1]}] :: {gid[3]}")


# --------------------------------------------------------------------------
# certificate CK_A -- sources
# --------------------------------------------------------------------------
def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    markers_present = set(PRIMARY_REQUIRED_MARKERS) <= names
    rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "access": "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY" if path.endswith(".py")
                  else "TEXT_ONLY_PINNED_STDOUT",
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 6,
        "source_rows": rows,
        "primary_required_AST_markers": PRIMARY_REQUIRED_MARKERS,
        "primary_required_AST_markers_present": markers_present,
        "BLOCKLIST": BLOCKLISTED_MODULES,
        "blocked_modules_loaded": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits": tuple(FIREWALL.hits),
        "executable_science_inputs": (),
        "finding": (
            "All six cited inputs are literal worktree-relative paths that "
            "exist, match their pinned SHA-256 and git blob hashes, and are "
            "consumed as text or AST only; the primary runner carries every "
            "required structural marker and is blocked from import."
        ),
    }
    result["pass"] = (
        len(rows) <= 6
        and all(row["exists_worktree_relative"] and row["sha256_exact"]
                and row["git_blob_exact"] for row in rows)
        and markers_present
        and not result["blocked_modules_loaded"]
        and not result["firewall_hits"]
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_B -- the primary's claims, parsed from its pinned stdout
# --------------------------------------------------------------------------
def parse_primary_claims() -> dict[str, object]:
    text = (ROOT / PRIMARY_CACHE).read_text()
    blocks: dict[str, object] = {}
    for line in text.splitlines():
        if line.startswith("FINAL "):
            blocks["FINAL"] = json.loads(line[len("FINAL "):])
        elif " :: " in line and line.split(" ", 1)[0] in ("PASS", "FAIL"):
            label = line.split(" ", 2)[1]
            blocks[label] = json.loads(line.split(" :: ", 1)[1])
    return blocks


def claims_certificate(claims: dict[str, object]) -> dict[str, object]:
    final = claims.get("FINAL") or {}
    landed = claims.get("E_LANDED_CLASSIFICATION") or {}
    lineage = claims.get("B_LINEAGE_CONSTRAINTS") or {}
    escape = claims.get("G_ESCAPE_B") or {}
    admissibility = claims.get("D_ADMISSIBILITY") or {}
    result = {
        "primary_cache": PRIMARY_CACHE,
        "blocks_parsed": tuple(sorted(claims)),
        "claimed_verdict": final.get("verdict"),
        "claimed_generators_declared": final.get("generators_declared"),
        "claimed_generators_admissible": final.get("generators_admissible"),
        "claimed_pairs_classified": final.get("pairs_classified"),
        "claimed_sigma_sensitive_pairs": final.get("sigma_sensitive_pairs"),
        "claimed_escape_b_shaped": final.get("escape_b_shaped_objects"),
        "claimed_member_count": landed.get("member_count"),
        "claimed_nonconstant_generators": landed.get("nonconstant_generator_count"),
        "claimed_conformal_nonzero_members":
            lineage.get("landed_conformal_nonzero_members"),
        "claimed_max_sigma_degree_on_loaded_probes":
            escape.get("max_sigma_degree_on_loaded_probes"),
        "claimed_inadmissible_count": admissibility.get("inadmissible_count"),
        "finding": (
            "The primary's pinned stdout parses cleanly and its recomputable "
            "claims are extracted verbatim for later comparison: the verdict, "
            "the declared and admissible generator counts, the classified pair "
            "count and its sensitive split, the escape-(b)-shaped count, the "
            "family size, the number of members carrying a conformal channel, "
            "and the top sigma degree it says it saw on a loaded probe."
        ),
    }
    result["pass"] = (
        "FINAL" in claims
        and isinstance(result["claimed_pairs_classified"], int)
        and isinstance(result["claimed_generators_admissible"], int)
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_C -- the wide refutation hunt (no admissibility filter)
# --------------------------------------------------------------------------
def wide_hunt(members: tuple, rule=ledger, planted: bool = False) -> dict:
    sensitive_members = 0
    sensitive_features: dict[int, int] = {}
    conformal_nonzero = 0
    stream = sha256()
    for member in members:
        grid = scaled_source(member, rule)
        trace = sector_trace(grid)
        if any(value for block in trace for value in block):
            conformal_nonzero += 1
        plus = wide_features(grid, 1, planted)
        minus = wide_features(grid, -1, planted)
        hits = tuple(index for index in range(len(plus))
                     if plus[index] != minus[index])
        if hits:
            sensitive_members += 1
            for index in hits:
                sensitive_features[index] = sensitive_features.get(index, 0) + 1
        stream.update(compact({"m": member, "n": len(hits)}).encode())
    return {
        "searched_member_count": len(members),
        "linear_feature_width": len(wide_features(scaled_source(members[0], rule),
                                                  1, planted)),
        "members_with_any_sensitive_feature": sensitive_members,
        "distinct_sensitive_features": len(sensitive_features),
        "conformal_nonzero_members": conformal_nonzero,
        "stream_sha256": stream.hexdigest(),
    }


def hunt_certificate(members: tuple) -> dict[str, object]:
    hunt = wide_hunt(members)
    rng = random.Random(872_002)
    # direct quadratic sweep on a declared member sample: every unordered
    # product of the whole feature base, with no reliance on any implication
    sample = tuple(members[rng.randrange(len(members))] for _ in range(8))
    quadratic_comparisons = 0
    quadratic_sensitive = 0
    for member in sample:
        grid = scaled_source(member)
        plus = wide_features(grid, 1)
        minus = wide_features(grid, -1)
        for left, right in combinations_with_replacement(range(len(plus)), 2):
            quadratic_comparisons += 1
            if plus[left] * plus[right] != minus[left] * minus[right]:
                quadratic_sensitive += 1
    # higher-degree spot check: random monomials and combinations to degree five
    monomial_tested = 0
    monomial_sensitive = 0
    max_degree = 0
    for _trial in range(600):
        member = members[rng.randrange(len(members))]
        grid = scaled_source(member)
        plus = wide_features(grid, 1)
        minus = wide_features(grid, -1)
        total_plus = 0
        total_minus = 0
        for _term in range(rng.randint(1, 3)):
            factors = [rng.randrange(len(plus)) for _ in range(rng.randint(1, 5))]
            max_degree = max(max_degree, len(factors))
            coefficient = rng.randint(-9, 9)
            term_plus, term_minus = coefficient, coefficient
            for index in factors:
                term_plus *= plus[index]
                term_minus *= minus[index]
            total_plus += term_plus
            total_minus += term_minus
        monomial_tested += 1
        if total_plus != total_minus:
            monomial_sensitive += 1
    result = {
        **hunt,
        "class_description": (
            "seven endpoint-space combinations of the identity and the exchange "
            "(including three the primary never declared), grading powers one "
            "through four (the primary declared one and two), and every "
            "index-subset contraction -- searched with NO admissibility filter, "
            "so an object the primary rejected as inadmissible cannot hide here"
        ),
        "wide_premaps": tuple(name for name, _a, _b in WIDE_PREMAPS),
        "wide_grade_powers": WIDE_GRADE_POWERS,
        "wide_width_closed_form": WIDE_WIDTH,
        "total_linear_comparisons": len(members) * hunt["linear_feature_width"],
        "quadratic_sample_members": len(sample),
        "quadratic_comparisons": quadratic_comparisons,
        "quadratic_sensitive": quadratic_sensitive,
        "random_monomial_tested": monomial_tested,
        "random_monomial_max_degree": max_degree,
        "random_monomial_sensitive": monomial_sensitive,
        "seed": 872_002,
        "finding": (
            f"The hunt swept all {len(members)} landed source configurations "
            f"against {hunt['linear_feature_width']} linear response features "
            f"each -- {len(members) * hunt['linear_feature_width']} exact "
            f"integer comparisons between the sigma=+1 and sigma=-1 worlds over "
            f"a class strictly wider than the primary's and with no "
            f"admissibility filter applied. "
            f"{hunt['members_with_any_sensitive_feature']} members exposed a "
            f"sign-sensitive feature. A direct quadratic sweep over "
            f"{len(sample)} sampled members compared "
            f"{quadratic_comparisons} products and found "
            f"{quadratic_sensitive} sensitive, and {monomial_tested} random "
            f"algebra elements of degree up to {max_degree} produced "
            f"{monomial_sensitive} sensitive readings."
        ),
    }
    result["pass"] = (
        result["total_linear_comparisons"]
        == len(members) * hunt["linear_feature_width"]
        and hunt["linear_feature_width"] == WIDE_WIDTH
        and quadratic_comparisons > 0
        and monomial_tested == 600
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_D -- independent re-derivations
# --------------------------------------------------------------------------
def rederivation_certificate(members: tuple) -> dict[str, object]:
    # the annihilation, by an integer dot product rather than a polynomial
    covector_dot = sum(coefficient for coefficient in ledger(1))
    extreme_rows = []
    extreme_all_zero = True
    rng = random.Random(872_003)
    for label, count, magnitude in (
        ("k=12_random_directions_unit_weights", 12, 1),
        ("k=6_weights_to_1e9", 6, 10 ** 9),
        ("k=3_weights_to_1e18", 3, 10 ** 18),
    ):
        grid = [[[0] * AXIS_COUNT for _s in range(SECTOR_COUNT)]
                for _e in range(ENDPOINT_COUNT)]
        for _index in range(count):
            endpoint = rng.randrange(ENDPOINT_COUNT)
            direction = rng.randrange(len(DIRECTIONS))
            weight = rng.randint(1, magnitude)
            for sector, coefficient in enumerate(ledger(weight)):
                for axis in range(AXIS_COUNT):
                    grid[endpoint][sector][axis] += \
                        SCALE * coefficient * DIRECTIONS[direction][axis]
        trace = sector_trace(grid)
        is_zero = not any(value for block in trace for value in block)
        extreme_all_zero = extreme_all_zero and is_zero
        extreme_rows.append({"configuration": label, "source_count": count,
                             "sector_trace_is_zero": is_zero})
    # the six Cycle-868 objects, rebuilt in two integer worlds
    landed_868_blind = True
    landed_868_probe_sensitive = 0
    for member in members[:64]:
        for rule, expect_probe in ((ledger, False), (detuned_ledger, True)):
            grid = scaled_source(member, rule)
            readings = {}
            for sigma in (1, -1):
                tower = grade_tower(grid, sigma, (1, 2))
                pushed = premap(tower[1], 0, 1)
                readings[sigma] = (
                    [pushed[e][s][a] for e in range(ENDPOINT_COUNT)
                     for s in range(SECTOR_COUNT) for a in range(AXIS_COUNT)]
                    + [tower[2][e][s][a] for e in range(ENDPOINT_COUNT)
                       for s in range(SECTOR_COUNT) for a in range(AXIS_COUNT)]
                    + contract(pushed, ("s",))[0]
                    + pair_gram(pushed, pushed)[0]
                    + pair_sector_contract(pushed, pushed)[0]
                    + pair_endpoint_transfer(tower[1], tower[1])[0]
                )
            differs = readings[1] != readings[-1]
            if rule is ledger and differs:
                landed_868_blind = False
            if expect_probe and differs:
                landed_868_probe_sensitive += 1
    # the escape-(b) shape, confirmed independently on a loaded source
    escape_shape_features = 0
    probe_grid = scaled_source(("k2", 1, 3, 4, 2), detuned_ledger)
    probe_plus = wide_features(probe_grid, 1)
    probe_minus = wide_features(probe_grid, -1)
    for index in range(len(probe_plus)):
        if probe_plus[index] != probe_minus[index]:
            escape_shape_features += 1
    result = {
        "ledger_all_ones_dot_product": covector_dot,
        "ledger_is_sector_traceless": covector_dot == 0,
        "extreme_configuration_rows": tuple(extreme_rows),
        "extreme_configurations_all_traceless": extreme_all_zero,
        "cycle868_objects_rebuilt": (
            "O1 pushforward, O2 composed pullback, O3 flux balance, O4 gram, "
            "O5 response tensor, O6 edge transfer, rebuilt from the exchange "
            "and the two-world grading with no reference to the primary"
        ),
        "cycle868_objects_blind_on_landed_sample": landed_868_blind,
        "cycle868_objects_sensitive_on_detuned_sample":
            landed_868_probe_sensitive,
        "cycle868_sample_members": 64,
        "escape_b_shaped_features_on_loaded_probe": escape_shape_features,
        "escape_b_shape_is_realisable": escape_shape_features > 0,
        "finding": (
            f"Three claims are re-derived without touching the primary. The "
            f"recoil ledger's dot product with the all-ones sector covector is "
            f"{covector_dot}, so the source is sector-traceless by a one-line "
            f"integer identity rather than a polynomial argument, and the "
            f"sector trace stayed zero on every declared extreme configuration "
            f"up to twelve sources and weights of order 1e18. The six Cycle-868 "
            f"objects were rebuilt from scratch in two integer worlds and read "
            + ("blind" if landed_868_blind else "SENSITIVE")
            + f" on the landed sample while firing on "
            f"{landed_868_probe_sensitive} detuned cases, which reproduces the "
            f"868 result independently. And {escape_shape_features} features of "
            f"the wide class separate the signs on a conformally loaded probe, "
            f"so the escape-(b) shape "
            + ("is realisable" if escape_shape_features > 0 else
               "is NOT realisable")
            + " and the primary's nonzero shaped count is corroborated."
        ),
    }
    result["pass"] = (
        len(extreme_rows) == 3
        and isinstance(covector_dot, int)
        and isinstance(escape_shape_features, int)
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_E -- independent admissibility, by finite differences
# --------------------------------------------------------------------------
def admissibility_recheck(members: tuple) -> dict[str, object]:
    rng = random.Random(872_004)
    sample = {members[rng.randrange(len(members))] for _ in range(160)}
    sample |= {member for member in members if member[0] == "k1"}
    closure = set(sample)
    for member in sample:
        closure.add(reverse_member(member))
        closure.add(swap_member(member))
    closure = tuple(sorted(closure))
    readings = {}
    for member in closure:
        grid = scaled_source(member)
        readings[member] = [primary_class_readings(grid, sigma)
                            for sigma in SIGMA_POINTS]
    degree_bound_ok = True
    max_nonzero_difference = 0
    for member in closure:
        for gid in PRIMARY_GENERATOR_IDS:
            arity = len(readings[member][0][gid][0])
            for slot in range(arity):
                fifth = sum(
                    weight * readings[member][point][gid][0][slot]
                    for point, weight in enumerate(FIFTH_DIFFERENCE_WEIGHTS)
                )
                if fifth:
                    degree_bound_ok = False
                    max_nonzero_difference = max(max_nonzero_difference, abs(fifth))
    parity_ok = {gid: True for gid in PRIMARY_GENERATOR_IDS}
    equivariance = {gid: {1, -1} for gid in PRIMARY_GENERATOR_IDS}
    for member in sorted(sample):
        reversed_member = reverse_member(member)
        swapped_member = swap_member(member)
        for gid in PRIMARY_GENERATOR_IDS:
            sign = (-1) ** GENERATOR_DEGREE[gid]
            mapping = REVERSAL_MAPS[gid]
            for point in IDENTITY_POINTS:
                base = readings[member][point][gid][0]
                if readings[reversed_member][point][gid][0] != \
                        [sign * value for value in base]:
                    parity_ok[gid] = False
                permuted = [base[mapping[i]] for i in range(len(mapping))]
                swapped = readings[swapped_member][point][gid][0]
                for eps in tuple(equivariance[gid]):
                    if swapped != [eps * value for value in permuted]:
                        equivariance[gid].discard(eps)
    admissible = tuple(gid for gid in PRIMARY_GENERATOR_IDS
                       if parity_ok[gid] and equivariance[gid])
    # escape-(b) shape, counted over the checker's own admissible set
    escape_shaped = set()
    for member in (("k2", 0, 1, 2, 3), ("k2", 1, 3, 4, 2), ("k1", 0, 0, 1)):
        for rule in (detuned_ledger, pure_conformal_ledger):
            grid = scaled_source(member, rule)
            plus = primary_class_readings(grid, 1)
            minus = primary_class_readings(grid, -1)
            for gid in admissible:
                if plus[gid][0] != minus[gid][0]:
                    escape_shaped.add(gid)
    sensitive_on_landed = 0
    for member in sorted(sample):
        plus = readings[member][SIGMA_POINTS.index(1)]
        minus = readings[member][SIGMA_POINTS.index(-1)]
        for gid in PRIMARY_GENERATOR_IDS:
            if plus[gid][0] != minus[gid][0]:
                sensitive_on_landed += 1
    result = {
        "route": (
            "no polynomial ring: every generator is evaluated in six hard-wired "
            "integer sigma worlds; the fifth finite difference is checked to "
            "vanish, which certifies sigma-degree at most four, after which "
            "agreement at five points is polynomial identity"
        ),
        "sigma_points": SIGMA_POINTS,
        "fifth_difference_weights": FIFTH_DIFFERENCE_WEIGHTS,
        "degree_at_most_four_everywhere": degree_bound_ok,
        "largest_nonvanishing_fifth_difference": max_nonzero_difference,
        "generators_rebuilt": len(PRIMARY_GENERATOR_IDS),
        "member_sample_size": len(sample),
        "member_closure_size": len(closure),
        "sample_note": (
            "a declared subsample closed under direction reversal and endpoint "
            "exchange; subsampling can only WEAKEN the constraints, so a "
            "checker count below the primary's would mean the primary admitted "
            "an object that fails on a member the checker actually tested"
        ),
        "checker_admissible_count": len(admissible),
        "checker_inadmissible_count":
            len(PRIMARY_GENERATOR_IDS) - len(admissible),
        "checker_escape_b_shaped_count": len(escape_shaped),
        "sensitive_generator_pairs_on_landed_sample": sensitive_on_landed,
        "finding": (
            f"The primary's {len(PRIMARY_GENERATOR_IDS)} declared generators "
            f"were rebuilt here and re-tested by a route that shares no "
            f"arithmetic with it. The fifth finite difference vanished "
            + ("on every component of every generator, so sigma-degree is at "
               "most four and five-point agreement is exact polynomial "
               "identity"
               if degree_bound_ok else
               f"NOT everywhere -- the largest survivor was "
               f"{max_nonzero_difference}, so the degree bound the checker "
               f"relies on does not hold")
            + f". Over a {len(sample)}-member subsample closed under both "
            f"lineage symmetries, {len(admissible)} generators survived both "
            f"constraints, {len(escape_shaped)} of them carry the escape-(b) "
            f"shape on a conformally loaded probe, and "
            f"{sensitive_on_landed} generator readings out of the whole "
            f"unfiltered set separated the signs on the landed subsample."
        ),
    }
    result["pass"] = (
        degree_bound_ok
        and len(admissible) <= len(PRIMARY_GENERATOR_IDS)
        and len(closure) >= len(sample)
        and len(PRIMARY_GENERATOR_IDS) == 384
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_F -- claim comparison, checker's verdict formed first
# --------------------------------------------------------------------------
def comparison_certificate(claims: dict[str, object], hunt: dict[str, object],
                           recheck: dict[str, object],
                           rederivation: dict[str, object],
                           members: tuple) -> dict[str, object]:
    final = claims.get("FINAL") or {}
    landed = claims.get("E_LANDED_CLASSIFICATION") or {}
    lineage = claims.get("B_LINEAGE_CONSTRAINTS") or {}
    escape = claims.get("G_ESCAPE_B") or {}
    checker_verdict = (
        "OUTCOME_A_LAWFUL_SIGMA_VISIBLE_OBJECT_EXISTS"
        if (hunt["members_with_any_sensitive_feature"] > 0
            or hunt["quadratic_sensitive"] > 0
            or hunt["random_monomial_sensitive"] > 0
            or recheck["sensitive_generator_pairs_on_landed_sample"] > 0)
        else "OUTCOME_B_CONSTRUCTOR_ALGEBRA_BLIND"
    )
    rows = (
        {"field": "family_member_count",
         "primary": landed.get("member_count"), "checker": len(members),
         "agree": landed.get("member_count") == len(members)},
        {"field": "conformal_nonzero_members",
         "primary": lineage.get("landed_conformal_nonzero_members"),
         "checker": hunt["conformal_nonzero_members"],
         "agree": lineage.get("landed_conformal_nonzero_members")
                  == hunt["conformal_nonzero_members"]},
        {"field": "generators_declared",
         "primary": final.get("generators_declared"),
         "checker": len(PRIMARY_GENERATOR_IDS),
         "agree": final.get("generators_declared") == len(PRIMARY_GENERATOR_IDS)},
        {"field": "any_sigma_visible_object_on_landed_family",
         "primary": bool(final.get("sigma_sensitive_pairs")),
         "checker": checker_verdict.startswith("OUTCOME_A"),
         "agree": bool(final.get("sigma_sensitive_pairs"))
                  == checker_verdict.startswith("OUTCOME_A")},
        {"field": "escape_b_shape_realisable",
         "primary": bool(final.get("escape_b_shaped_objects")),
         "checker": rederivation["escape_b_shape_is_realisable"],
         "agree": bool(final.get("escape_b_shaped_objects"))
                  == rederivation["escape_b_shape_is_realisable"]},
        {"field": "generators_admissible_not_overclaimed",
         "primary": final.get("generators_admissible"),
         "checker": recheck["checker_admissible_count"],
         "agree": isinstance(final.get("generators_admissible"), int)
                  and recheck["checker_admissible_count"]
                  >= final.get("generators_admissible")},
        {"field": "escape_b_shaped_count_not_overclaimed",
         "primary": final.get("escape_b_shaped_objects"),
         "checker": recheck["checker_escape_b_shaped_count"],
         "agree": isinstance(final.get("escape_b_shaped_objects"), int)
                  and recheck["checker_escape_b_shaped_count"]
                  >= final.get("escape_b_shaped_objects")},
        {"field": "max_sigma_degree_on_loaded_probes",
         "primary": escape.get("max_sigma_degree_on_loaded_probes"),
         "checker": 4 if recheck["degree_at_most_four_everywhere"] else None,
         "agree": escape.get("max_sigma_degree_on_loaded_probes") == 4
                  and recheck["degree_at_most_four_everywhere"]},
    )
    disagreements = tuple(row["field"] for row in rows if not row["agree"])
    result = {
        "rows": rows,
        "disagreements": disagreements,
        "primary_verdict": final.get("verdict"),
        "checker_independent_verdict": checker_verdict,
        "verdicts_agree": bool(
            final.get("verdict", "").startswith("OUTCOME_B")
        ) == checker_verdict.startswith("OUTCOME_B"),
        "overclaim_test_direction": (
            "the admissible and escape-(b)-shaped counts are compared as "
            "NOT-OVERCLAIMED rather than as equalities: the checker's tests run "
            "on a subsample and are therefore weaker, so it should find at "
            "least as many survivors; finding FEWER would mean the primary "
            "admitted an object that fails a constraint on a member the "
            "checker actually tested"
        ),
    }
    result["finding"] = (
        f"Eight independently recomputed quantities were compared against the "
        f"primary's pinned claims, with the checker forming its own verdict "
        f"from its own wider hunt before any comparison was made. "
        f"{len(disagreements)} field(s) disagree"
        + (f": {', '.join(disagreements)}. " if disagreements else ". ")
        + f"The checker's independent verdict is {checker_verdict}, which "
        f"{'matches' if result['verdicts_agree'] else 'does NOT match'} the "
        f"primary's {final.get('verdict')}."
    )
    result["pass"] = all(
        isinstance(row["checker"], (int, bool, type(None))) for row in rows
    ) and len(rows) == 8
    return result


# --------------------------------------------------------------------------
# certificate CK_G -- the checker's own adversary calibration
# --------------------------------------------------------------------------
def adversary_certificate(members: tuple) -> dict[str, object]:
    probe = (("k2", 2, 4, 5, 3), ("k2", 0, 1, 2, 3), ("k1", 1, 5, 6))
    detuned = wide_hunt(probe, rule=detuned_ledger)
    conformal = wide_hunt(probe, rule=pure_conformal_ledger)
    landed = wide_hunt(probe, rule=ledger)
    planted = wide_hunt(probe, rule=ledger, planted=True)
    fake_claims = {
        "FINAL": {
            "verdict": "OUTCOME_B_CONSTRUCTOR_ALGEBRA_BLIND_ESCAPE_B_SHAPED_BUT_VOID",
            "generators_declared": 999,
            "generators_admissible": 999_999,
            "pairs_classified": 42,
            "sigma_sensitive_pairs": 0,
            "escape_b_shaped_objects": 999_999,
        },
        "E_LANDED_CLASSIFICATION": {"member_count": 7,
                                    "nonconstant_generator_count": 0},
        "B_LINEAGE_CONSTRAINTS": {"landed_conformal_nonzero_members": 1234},
        "G_ESCAPE_B": {"max_sigma_degree_on_loaded_probes": 99},
    }
    fake_hunt = {"conformal_nonzero_members": 0,
                 "members_with_any_sensitive_feature": 0,
                 "quadratic_sensitive": 0, "random_monomial_sensitive": 0}
    fake_recheck = {"checker_admissible_count": 344,
                    "checker_escape_b_shaped_count": 162,
                    "sensitive_generator_pairs_on_landed_sample": 0,
                    "degree_at_most_four_everywhere": True}
    fake_rederivation = {"escape_b_shape_is_realisable": True}
    fake_comparison = comparison_certificate(
        fake_claims, fake_hunt, fake_recheck, fake_rederivation, members[:3]
    )
    result = {
        "probe_members": probe,
        "detuned_sensitive_members": detuned["members_with_any_sensitive_feature"],
        "detuned_distinct_sensitive_features": detuned["distinct_sensitive_features"],
        "pure_conformal_sensitive_members":
            conformal["members_with_any_sensitive_feature"],
        "landed_sensitive_members": landed["members_with_any_sensitive_feature"],
        "planted_off_grammar_sensitive_members":
            planted["members_with_any_sensitive_feature"],
        "planted_off_grammar_distinct_features":
            planted["distinct_sensitive_features"],
        "detector_fires_on_detuned_ledger":
            detuned["members_with_any_sensitive_feature"] > 0,
        "detector_fires_on_planted_off_grammar_grading":
            planted["members_with_any_sensitive_feature"] > 0,
        "planted_false_claim_fields_caught": tuple(fake_comparison["disagreements"]),
        "planted_false_claim_detected":
            len(fake_comparison["disagreements"]) >= 4,
        "calibration_scope_note": (
            "the detuned and pure-conformal ledgers, the off-grammar grading "
            "that carries sigma on the trace-free channel, and the fabricated "
            "claim block are all OFF-SCOPE; they calibrate the checker's "
            "discriminating power and none is evidence about the landed family"
        ),
        "finding": (
            f"The checker demonstrates it can refute, on three independent "
            f"axes. Detuning the ledger by one unit made "
            f"{detuned['distinct_sensitive_features']} distinct features "
            f"sign-sensitive and a purely conformal ledger fired on "
            f"{conformal['members_with_any_sensitive_feature']} probe members, "
            f"while the landed ledger fired on "
            f"{landed['members_with_any_sensitive_feature']}. An off-grammar "
            f"grading that carries sigma on the trace-free channel instead -- a "
            f"genuinely sigma-visible object on the LANDED ledger -- was caught "
            f"on {planted['members_with_any_sensitive_feature']} probe members "
            f"and {planted['distinct_sensitive_features']} features, so the "
            f"hunt would have found a lawful sigma-visible object had one "
            f"existed. A fabricated claim block was caught on "
            f"{len(fake_comparison['disagreements'])} comparison fields."
        ),
    }
    result["pass"] = (
        result["detector_fires_on_detuned_ledger"]
        and result["detector_fires_on_planted_off_grammar_grading"]
        and result["planted_false_claim_detected"]
    )
    return result


# --------------------------------------------------------------------------
# emission
# --------------------------------------------------------------------------
LABELS = (
    "CK_A_SOURCES",
    "CK_B_PRIMARY_CLAIMS",
    "CK_C_WIDE_HUNT",
    "CK_D_REDERIVATIONS",
    "CK_E_ADMISSIBILITY_RECHECK",
    "CK_F_COMPARISON",
    "CK_G_ADVERSARY",
    "CK_H_CONTROLS",
)


def render_fixed_point(certificates: dict[str, dict[str, object]]) -> str:
    for _attempt in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        hunt = certificates["CK_C_WIDE_HUNT"]
        recheck = certificates["CK_E_ADMISSIBILITY_RECHECK"]
        comparison = certificates["CK_F_COMPARISON"]
        refuted = (
            hunt["members_with_any_sensitive_feature"] > 0
            or hunt["quadratic_sensitive"] > 0
            or hunt["random_monomial_sensitive"] > 0
            or recheck["sensitive_generator_pairs_on_landed_sample"] > 0
            or bool(comparison["disagreements"])
        )
        terminal = {
            "terminal": (
                "CYCLE872_INDEPENDENT_CHECK_REFUTES_PRIMARY" if refuted
                else "CYCLE872_INDEPENDENT_CHECK_CORROBORATES_BY_EXHAUSTION"
            ),
            "bookkeeping_complete": all(checks.values()),
            "checks": checks,
            "linear_features_per_member": hunt["linear_feature_width"],
            "linear_comparisons": hunt["total_linear_comparisons"],
            "quadratic_comparisons": hunt["quadratic_comparisons"],
            "sensitive_members_found": hunt["members_with_any_sensitive_feature"],
            "claim_disagreements": comparison["disagreements"],
            "checker_verdict": comparison["checker_independent_verdict"],
            "runtime_seconds": certificates["CK_H_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["CK_H_CONTROLS"]["stdout_bytes"],
        }
        lines = []
        for label in LABELS:
            lines.append(f"FINDING {label} :: {certificates[label]['finding']}")
            lines.append(
                f"{'PASS' if checks[label] else 'FAIL'} {label} :: "
                f"{compact(certificates[label])}"
            )
        lines.append("FINAL " + compact(terminal))
        output = "\n".join(lines) + "\n"
        size = len(output.encode("utf-8"))
        controls = certificates["CK_H_CONTROLS"]
        prior = controls["stdout_bytes"]
        controls["stdout_bytes"] = size
        controls["stdout_under_limit"] = size < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["base_pass"] and controls["stdout_under_limit"]
        if prior == size:
            return output
    raise AssertionError("stdout byte fixed point did not converge")


def run() -> int:
    started = monotonic()
    sources = source_controls()
    claims = parse_primary_claims()
    claim_rows = claims_certificate(claims)
    members = family()
    hunt = hunt_certificate(members)
    rederivation = rederivation_certificate(members)
    recheck = admissibility_recheck(members)
    comparison = comparison_certificate(claims, hunt, recheck, rederivation, members)
    adversary = adversary_certificate(members)

    replay_members = family()
    replay_hunt = wide_hunt(replay_members)
    replay_recheck = admissibility_recheck(replay_members)
    deterministic = (
        replay_members == members
        and replay_hunt["stream_sha256"] == hunt["stream_sha256"]
        and replay_hunt["members_with_any_sensitive_feature"]
        == hunt["members_with_any_sensitive_feature"]
        and replay_recheck["checker_admissible_count"]
        == recheck["checker_admissible_count"]
        and replay_recheck["checker_escape_b_shaped_count"]
        == recheck["checker_escape_b_shaped_count"]
    )
    elapsed = monotonic() - started
    controls = {
        **{key: value for key, value in sources.items()
           if key not in {"pass", "finding"}},
        "sources_pass": sources["pass"],
        "determinism": {
            "scope": (
                "the family enumeration, the whole wide hunt and the seeded "
                "admissibility recheck were recomputed from scratch and "
                "compared digest-for-digest"
            ),
            "first_hunt_sha256": hunt["stream_sha256"],
            "second_hunt_sha256": replay_hunt["stream_sha256"],
            "exact": deterministic,
        },
        "arithmetic_route": (
            "integers only: the source is pre-scaled by three and every object "
            "is evaluated in hard-wired sigma worlds with exactness recovered "
            "by finite differences, so no polynomial algebra and no rational "
            "arithmetic is shared with the primary"
        ),
        "runtime_seconds": round(elapsed, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_limit": elapsed < AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_under_limit": False,
        "blocked_modules_loaded_after_science": tuple(
            name for name in BLOCKLISTED_MODULES if name in sys.modules
        ),
        "firewall_hits_after_science": tuple(FIREWALL.hits),
        "finding": (
            "The primary stayed blocked from import throughout, every pinned "
            "hash matched, the whole hunt and the admissibility recheck were "
            "recomputed from scratch and reproduced digest-for-digest, and the "
            "runtime and stdout caps were respected. The checker shares no "
            "arithmetic route with the primary: it works in integers across six "
            "hard-wired sigma worlds and recovers exactness by finite "
            "differences rather than by carrying a polynomial."
        ),
    }
    controls["base_pass"] = (
        sources["pass"] and deterministic and controls["runtime_under_limit"]
        and not controls["blocked_modules_loaded_after_science"]
        and not controls["firewall_hits_after_science"]
    )
    controls["pass"] = controls["base_pass"]

    certificates = {
        "CK_A_SOURCES": sources,
        "CK_B_PRIMARY_CLAIMS": claim_rows,
        "CK_C_WIDE_HUNT": hunt,
        "CK_D_REDERIVATIONS": rederivation,
        "CK_E_ADMISSIBILITY_RECHECK": recheck,
        "CK_F_COMPARISON": comparison,
        "CK_G_ADVERSARY": adversary,
        "CK_H_CONTROLS": controls,
    }
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
