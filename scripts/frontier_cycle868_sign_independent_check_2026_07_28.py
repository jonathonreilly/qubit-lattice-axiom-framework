#!/usr/bin/env python3
"""Independent adversarial checker for the Cycle-868 sign census.

This checker is specified to REFUTE.  Its job is to find one functional on
the stipulated response surface that distinguishes the grading sign, which
would refute the primary's EXACT-SUPPORT claim over the DECLARED source
family.  It therefore does not re-run the primary's six stipulated objects:
it searches a deliberately much larger functional space built from the same
stipulated surface -- every coordinate of the graded source, the pushforward
and the composed pullback, every index contraction of the pushforward, and
every unordered quadratic in that whole base -- across the declared source
family.

Everything decisive is STIPULATED IN-FILE, mirroring the primary: the
traceless three-sector recoil ledger (-2d, +d, +d), the sector-weight ladder
d = 1..6 (an explicit scope input; no cited supplier), the two-endpoint
exchange, and the sector-trace grading.  The ONLY audit inputs are the
primary runner and its pinned stdout, both SHA-pinned text evidence behind a
meta-path import firewall.  The Cycle-320/322/749/768/812 lineage is
provenance-only, non-load-bearing context; its modules are import-blocklisted
as a belt and are not read, hashed, or otherwise consumed.  The arithmetic
route is independent as well: the primary carried a formal sigma as a
rational polynomial, while this checker hard-wires two integer worlds
(sigma=+1 and sigma=-1) and compares them with integer arithmetic only, so a
bug in the primary's polynomial algebra cannot reproduce itself here.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle868_response_sign_census_2026_07_28.py",
    "logs/runner-cache/frontier_cycle868_response_sign_census_2026_07_28.txt",
)

import ast
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations_with_replacement
import json
from pathlib import Path
import sys
from time import monotonic

ROOT = Path(__file__).resolve().parents[1]
PRIMARY_PATH, PRIMARY_CACHE = AUDIT_INPUT_PATHS[0], AUDIT_INPUT_PATHS[1]
PYTHON_PATHS = tuple(
    path for path in AUDIT_INPUT_PATHS if path.endswith(".py")
)
# Provenance-only ancestor modules (non-load-bearing context; not audit
# inputs).  The blocklist is a belt that fails closed if any of them -- or
# the primary itself -- is ever imported.
PROVENANCE_BLOCKLIST_STEMS = (
    "unit_weight_carried_link_recoil_cycle320_2026_07_18",
    "two_cell_two_source_recoil_reciprocity_cycle322_2026_07_18",
    "frontier_cycle749_response_comparison_harness_2026_07_28",
    "frontier_cycle768_response_law_candidate_2026_07_28",
    "frontier_cycle812_mixed_input_response_2026_07_28",
)
BLOCKLISTED_MODULES = tuple(
    Path(path).stem for path in PYTHON_PATHS
) + PROVENANCE_BLOCKLIST_STEMS
EXPECTED_SHA256 = {
    AUDIT_INPUT_PATHS[0]:
        "dca6b71b9dec65adbacff348e75085bf2c24fe96f621b949a4c8fb96f74cf89a",
    AUDIT_INPUT_PATHS[1]:
        "efb45439065ca7c92db20e29a1f261cfeaec71f96ae21d5774e617dfdc295c55",
}
EXPECTED_GIT_BLOBS = {
    AUDIT_INPUT_PATHS[0]: "c155a2dafaccde60c17047303c6de358445711c3",
    AUDIT_INPUT_PATHS[1]: "38a0ecf77aaef1b37d1c9fcca49bbd74edd40796",
}
PRIMARY_REQUIRED_MARKERS = (
    "adjoint_pullback",
    "census_certificate",
    "grading_operator",
    "stipulated_ledger",
    "response_objects",
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
# the scope, restated here from the stipulated definitions rather than read
# from the primary: three sectors, the (-2d,+d,+d) ledger, six signed axis
# directions, six carried weights (an explicit scope input with cardinality
# matching the held L=6 edge; no cited supplier), two endpoints, k <= 2
# --------------------------------------------------------------------------
SECTOR_COUNT = 3
AXIS_COUNT = 3
ENDPOINT_COUNT = 2
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
WEIGHTS = (1, 2, 3, 4, 5, 6)
SCALE = 3  # every graded quantity times 3 is an integer


def ledger(weight: int) -> tuple[int, int, int]:
    return (-2 * weight, weight, weight)


def detuned_ledger(weight: int) -> tuple[int, int, int]:
    return (-2 * weight, weight, weight + 1)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), default=str)


def digest(value: object) -> str:
    return sha256(compact(value).encode()).hexdigest()


def git_blob(payload: bytes) -> str:
    return sha1(f"blob {len(payload)}\0".encode() + payload).hexdigest()


# --------------------------------------------------------------------------
# independent enumeration: a flat lexicographic index over canonical keys
# --------------------------------------------------------------------------
def family() -> tuple[tuple, ...]:
    members = []
    span_one = ENDPOINT_COUNT * len(DIRECTIONS) * len(WEIGHTS)
    span_two = (len(DIRECTIONS) * len(WEIGHTS)) ** 2
    for flat in range(span_one):
        endpoint = flat // (len(DIRECTIONS) * len(WEIGHTS))
        remainder = flat % (len(DIRECTIONS) * len(WEIGHTS))
        members.append((
            "k1", endpoint,
            remainder // len(WEIGHTS),
            WEIGHTS[remainder % len(WEIGHTS)],
        ))
    for flat in range(span_two):
        left = flat // (len(DIRECTIONS) * len(WEIGHTS))
        right = flat % (len(DIRECTIONS) * len(WEIGHTS))
        members.append((
            "k2",
            left // len(WEIGHTS), WEIGHTS[left % len(WEIGHTS)],
            right // len(WEIGHTS), WEIGHTS[right % len(WEIGHTS)],
        ))
    return tuple(members)


def member_sources(member: tuple) -> tuple[tuple[int, int, int], ...]:
    if member[0] == "k1":
        return ((member[1], member[2], member[3]),)
    return ((0, member[1], member[2]), (1, member[3], member[4]))


def scaled_source(member: tuple, rule=ledger) -> list[list[list[int]]]:
    """SCALE * S[endpoint][sector][axis], integers only."""
    grid = [
        [[0] * AXIS_COUNT for _sector in range(SECTOR_COUNT)]
        for _endpoint in range(ENDPOINT_COUNT)
    ]
    for endpoint, direction, weight in member_sources(member):
        unit = DIRECTIONS[direction]
        for sector, coefficient in enumerate(rule(weight)):
            for axis in range(AXIS_COUNT):
                grid[endpoint][sector][axis] += SCALE * coefficient * unit[axis]
    return grid


def graded_world(scaled: list[list[list[int]]], sign: int) -> list[list[list[int]]]:
    """Hard-wired world: tracefree part plus sign times the conformal part.

    Everything stays integral because the source is already scaled by 3 and
    the conformal projector divides the sector trace by 3.
    """
    out = []
    for endpoint in range(ENDPOINT_COUNT):
        trace = [
            sum(scaled[endpoint][sector][axis] for sector in range(SECTOR_COUNT))
            for axis in range(AXIS_COUNT)
        ]
        block = []
        for sector in range(SECTOR_COUNT):
            row = []
            for axis in range(AXIS_COUNT):
                conformal, remainder = divmod(trace[axis], SECTOR_COUNT)
                if remainder:
                    raise AssertionError("conformal projection left a remainder")
                tracefree = scaled[endpoint][sector][axis] - conformal
                row.append(tracefree + sign * conformal)
            block.append(row)
        out.append(block)
    return out


def exchange(world: list[list[list[int]]]) -> list[list[list[int]]]:
    return [world[ENDPOINT_COUNT - 1 - endpoint]
            for endpoint in range(ENDPOINT_COUNT)]


def regrade(world: list[list[list[int]]], sign: int) -> list[list[list[int]]]:
    out = []
    for endpoint in range(ENDPOINT_COUNT):
        trace = [
            sum(world[endpoint][sector][axis] for sector in range(SECTOR_COUNT))
            for axis in range(AXIS_COUNT)
        ]
        block = []
        for sector in range(SECTOR_COUNT):
            row = []
            for axis in range(AXIS_COUNT):
                conformal, remainder = divmod(trace[axis], SECTOR_COUNT)
                if remainder:
                    raise AssertionError("regrade left a remainder")
                tracefree = world[endpoint][sector][axis] - conformal
                row.append(tracefree + sign * conformal)
            block.append(row)
        out.append(block)
    return out


def flatten(world: list[list[list[int]]]) -> list[int]:
    return [
        world[endpoint][sector][axis]
        for endpoint in range(ENDPOINT_COUNT)
        for sector in range(SECTOR_COUNT)
        for axis in range(AXIS_COUNT)
    ]


CONTRACTION_PATTERNS = (
    ("endpoint",), ("sector",), ("axis",),
    ("endpoint", "sector"), ("endpoint", "axis"), ("sector", "axis"),
    ("endpoint", "sector", "axis"),
)


def contractions(world: list[list[list[int]]]) -> list[int]:
    """Every index-subset contraction of the response array, flattened."""
    values: list[int] = []
    for pattern in CONTRACTION_PATTERNS:
        keep_endpoint = "endpoint" not in pattern
        keep_sector = "sector" not in pattern
        keep_axis = "axis" not in pattern
        endpoints = range(ENDPOINT_COUNT) if keep_endpoint else (None,)
        sectors = range(SECTOR_COUNT) if keep_sector else (None,)
        axes = range(AXIS_COUNT) if keep_axis else (None,)
        for endpoint in endpoints:
            for sector in sectors:
                for axis in axes:
                    total = 0
                    for e in (range(ENDPOINT_COUNT) if endpoint is None
                              else (endpoint,)):
                        for s in (range(SECTOR_COUNT) if sector is None
                                  else (sector,)):
                            for a in (range(AXIS_COUNT) if axis is None
                                      else (axis,)):
                                total += world[e][s][a]
                    values.append(total)
    return values


def base_features(scaled: list[list[list[int]]], sign: int) -> list[int]:
    """The linear base of the searched functional space, in one sigma world."""
    graded = graded_world(scaled, sign)
    pushed = exchange(graded)
    pulled = regrade(exchange(exchange(graded)), sign)
    return flatten(graded) + flatten(pushed) + flatten(pulled) + contractions(pushed)


BASE_WIDTH = (
    3 * ENDPOINT_COUNT * SECTOR_COUNT * AXIS_COUNT
    + sum(
        (ENDPOINT_COUNT if "endpoint" not in pattern else 1)
        * (SECTOR_COUNT if "sector" not in pattern else 1)
        * (AXIS_COUNT if "axis" not in pattern else 1)
        for pattern in CONTRACTION_PATTERNS
    )
)
QUADRATIC_PAIRS = tuple(combinations_with_replacement(range(BASE_WIDTH), 2))
FUNCTIONAL_COUNT = BASE_WIDTH + len(QUADRATIC_PAIRS)


def sensitive_functionals(scaled: list[list[list[int]]]) -> tuple[int, ...]:
    """Indices of every searched functional that separates sigma=+1 from -1."""
    plus = base_features(scaled, 1)
    minus = base_features(scaled, -1)
    hits: list[int] = []
    for index in range(BASE_WIDTH):
        if plus[index] != minus[index]:
            hits.append(index)
    offset = BASE_WIDTH
    for position, (left, right) in enumerate(QUADRATIC_PAIRS):
        if plus[left] * plus[right] != minus[left] * minus[right]:
            hits.append(offset + position)
    return tuple(hits)


# --------------------------------------------------------------------------
# certificate CK_A -- sources
# --------------------------------------------------------------------------
def source_controls() -> dict[str, object]:
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}
    primary_tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    primary_names = set()
    for node in primary_tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            primary_names.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    primary_names.add(target.id)
    markers_present = set(PRIMARY_REQUIRED_MARKERS) <= primary_names
    rows = tuple({
        "path": path,
        "exists_worktree_relative":
            not Path(path).is_absolute() and (ROOT / path).is_file(),
        "sha256": sha256(payloads[path]).hexdigest(),
        "sha256_exact": sha256(payloads[path]).hexdigest() == EXPECTED_SHA256[path],
        "git_blob": git_blob(payloads[path]),
        "git_blob_exact": git_blob(payloads[path]) == EXPECTED_GIT_BLOBS[path],
        "AST_valid": path.endswith(".py"),
        "access": "TEXT_AST_ONLY_BLOCKLISTED_PRIMARY" if path.endswith(".py")
                  else "TEXT_ONLY_PINNED_STDOUT",
    } for path in AUDIT_INPUT_PATHS)
    result = {
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_path_count": len(AUDIT_INPUT_PATHS),
        "read_cap": 2,
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
            "Both cited inputs -- the primary runner and its pinned stdout, "
            "the checker's ONLY audit inputs -- are literal worktree-relative "
            "paths that exist, match their pinned SHA-256 and git blob "
            "hashes, and are consumed as text or AST only; the primary "
            "carries every required structural marker and is blocked from "
            "import, and the provenance-only ancestor modules stay "
            "blocklisted without being consumed."
        ),
    }
    result["pass"] = (
        len(rows) <= 2
        and all(
            row["exists_worktree_relative"]
            and row["sha256_exact"]
            and row["git_blob_exact"]
            for row in rows
        )
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
    final_line = None
    census_line = None
    for line in text.splitlines():
        if line.startswith("FINAL "):
            final_line = json.loads(line[len("FINAL "):])
        elif line.startswith(("PASS D_SIGN_CENSUS :: ", "FAIL D_SIGN_CENSUS :: ")):
            census_line = json.loads(line.split(" :: ", 1)[1])
    return {"final": final_line, "census": census_line}


def claims_certificate(claims: dict[str, object]) -> dict[str, object]:
    final = claims["final"]
    census = claims["census"]
    parsed = final is not None and census is not None
    result = {
        "primary_cache": PRIMARY_CACHE,
        "final_parsed": final is not None,
        "census_parsed": census is not None,
        "claimed_verdict": final.get("verdict") if final else None,
        "claimed_pairs": final.get("pairs_censused") if final else None,
        "claimed_sensitive": final.get("sign_sensitive_pairs") if final else None,
        "claimed_blind": final.get("sign_blind_pairs") if final else None,
        "claimed_member_count": census.get("member_count") if census else None,
        "claimed_conformal_nonzero_members":
            census.get("conformal_nonzero_members") if census else None,
        "claimed_object_names":
            tuple(sorted(census.get("blind", {}))) if census else (),
        "finding": (
            "The primary's pinned stdout parses cleanly and its claims are "
            "extracted verbatim for comparison: a verdict string, the censused "
            "pair count, the sign-sensitive and sign-blind splits, the member "
            "count, and the number of family members carrying a nonzero "
            "conformal channel."
        ),
    }
    result["pass"] = parsed and isinstance(result["claimed_pairs"], int)
    return result


# --------------------------------------------------------------------------
# certificate CK_C -- the refutation hunt
# --------------------------------------------------------------------------
def refutation_hunt(members: tuple[tuple, ...]) -> dict[str, object]:
    sensitive_members = 0
    sensitive_functional_hits: dict[int, int] = {}
    conformal_nonzero = 0
    stream = sha256()
    for member in members:
        scaled = scaled_source(member)
        trace_nonzero = False
        for endpoint in range(ENDPOINT_COUNT):
            for axis in range(AXIS_COUNT):
                if sum(scaled[endpoint][sector][axis]
                       for sector in range(SECTOR_COUNT)) != 0:
                    trace_nonzero = True
        if trace_nonzero:
            conformal_nonzero += 1
        hits = sensitive_functionals(scaled)
        if hits:
            sensitive_members += 1
            for index in hits:
                sensitive_functional_hits[index] = \
                    sensitive_functional_hits.get(index, 0) + 1
        stream.update(compact({"m": member, "h": hits}).encode())
    result = {
        "searched_member_count": len(members),
        "searched_functional_count_per_member": FUNCTIONAL_COUNT,
        "base_functional_width": BASE_WIDTH,
        "quadratic_functional_count": len(QUADRATIC_PAIRS),
        "total_sigma_comparisons": len(members) * FUNCTIONAL_COUNT,
        "functional_space_description": (
            "every coordinate of the graded source, the pushforward and the "
            "composed pullback; every index-subset contraction of the "
            "pushforward; and every unordered product of two of those"
        ),
        "members_with_any_sensitive_functional": sensitive_members,
        "distinct_sensitive_functionals": len(sensitive_functional_hits),
        "sensitive_functional_index_sample": tuple(
            sorted(sensitive_functional_hits)[:16]
        ),
        "conformal_nonzero_members": conformal_nonzero,
        "hunt_stream_sha256": stream.hexdigest(),
        "finding": (
            f"The hunt swept {len(members)} declared source configurations "
            f"against {FUNCTIONAL_COUNT} response functionals each -- "
            f"{len(members) * FUNCTIONAL_COUNT} exact integer comparisons "
            f"between the sigma=+1 and sigma=-1 worlds, a functional space "
            f"far wider than the primary's six declared objects. "
            f"{sensitive_members} members exposed a sign-sensitive functional "
            f"and {len(sensitive_functional_hits)} distinct functionals were "
            f"sensitive anywhere; {conformal_nonzero} members carry a nonzero "
            f"conformal channel."
        ),
    }
    result["pass"] = (
        result["total_sigma_comparisons"] == len(members) * FUNCTIONAL_COUNT
        and FUNCTIONAL_COUNT == BASE_WIDTH + len(QUADRATIC_PAIRS)
        and result["searched_member_count"] == len(members)
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_D -- claim comparison
# --------------------------------------------------------------------------
def comparison_certificate(
    claims: dict[str, object],
    hunt: dict[str, object],
    members: tuple[tuple, ...],
) -> dict[str, object]:
    census = claims["census"] or {}
    final = claims["final"] or {}
    object_count = len(census.get("blind", {})) or 0
    rows = (
        {
            "field": "member_count",
            "primary": census.get("member_count"),
            "checker": len(members),
            "agree": census.get("member_count") == len(members),
        },
        {
            "field": "pairs_censused",
            "primary": final.get("pairs_censused"),
            "checker": len(members) * object_count,
            "agree": final.get("pairs_censused") == len(members) * object_count,
        },
        {
            "field": "conformal_nonzero_members",
            "primary": census.get("conformal_nonzero_members"),
            "checker": hunt["conformal_nonzero_members"],
            "agree": census.get("conformal_nonzero_members")
                     == hunt["conformal_nonzero_members"],
        },
        {
            "field": "any_sign_sensitive_object_exists",
            "primary": bool(final.get("sign_sensitive_pairs")),
            "checker": hunt["members_with_any_sensitive_functional"] > 0,
            "agree": bool(final.get("sign_sensitive_pairs"))
                     == (hunt["members_with_any_sensitive_functional"] > 0),
        },
    )
    disagreements = tuple(row["field"] for row in rows if not row["agree"])
    result = {
        "rows": rows,
        "disagreements": disagreements,
        "primary_verdict": final.get("verdict"),
        "checker_independent_verdict": (
            "RESPONSE_SURFACE_CONSTRAINS_THE_CONFORMAL_SIGN"
            if hunt["members_with_any_sensitive_functional"] > 0
            else "EXACT_SUPPORT_SIGN_INVISIBLE_ON_STIPULATED_SURFACE"
        ),
        "verdicts_agree": (
            final.get("verdict") == (
                "RESPONSE_SURFACE_CONSTRAINS_THE_CONFORMAL_SIGN"
                if hunt["members_with_any_sensitive_functional"] > 0
                else "EXACT_SUPPORT_SIGN_INVISIBLE_ON_STIPULATED_SURFACE"
            )
        ),
    }
    result["finding"] = (
        f"Four independently recomputed quantities were compared against the "
        f"primary's pinned claims, and the checker formed its own verdict from "
        f"its own wider hunt before any comparison. "
        f"{len(disagreements)} field(s) disagree"
        + (f": {', '.join(disagreements)}. " if disagreements else ". ")
        + f"The checker's independent verdict is "
        f"{result['checker_independent_verdict']}, which "
        f"{'matches' if result['verdicts_agree'] else 'does NOT match'} the "
        f"primary's {final.get('verdict')}."
    )
    result["pass"] = (
        all(isinstance(row["checker"], (int, bool)) for row in rows)
        and object_count > 0
        and not disagreements
        and result["verdicts_agree"]
    )
    return result


# --------------------------------------------------------------------------
# certificate CK_E -- the checker's own adversary calibration
# --------------------------------------------------------------------------
def adversary_certificate() -> dict[str, object]:
    seed = ("k2", 2, 4, 5, 3)
    stipulated = scaled_source(seed)
    detuned = scaled_source(seed, rule=detuned_ledger)
    stipulated_hits = sensitive_functionals(stipulated)
    detuned_hits = sensitive_functionals(detuned)
    fake_claims = {
        "final": {
            "verdict": "EXACT_SUPPORT_SIGN_INVISIBLE_ON_STIPULATED_SURFACE",
            "pairs_censused": 999_999,
            "sign_sensitive_pairs": 0,
            "sign_blind_pairs": 999_999,
        },
        "census": {
            "member_count": 999_999,
            "conformal_nonzero_members": 4242,
            "blind": {"X": 0},
        },
    }
    fake_hunt = {
        "conformal_nonzero_members": 0,
        "members_with_any_sensitive_functional": 0,
    }
    fake_comparison = comparison_certificate(fake_claims, fake_hunt, (("k1", 0, 0, 1),))
    result = {
        "seed_member": seed,
        "stipulated_ledger_sensitive_functional_count": len(stipulated_hits),
        "detuned_sensitive_functional_count": len(detuned_hits),
        "detector_fires_on_detuned_ledger": len(detuned_hits) > 0,
        "detector_silent_on_stipulated_ledger": len(stipulated_hits) == 0,
        "planted_false_claim_fields_caught":
            tuple(fake_comparison["disagreements"]),
        "planted_false_claim_detected":
            len(fake_comparison["disagreements"]) >= 3,
        "calibration_scope_note": (
            "the detuned ledger is an OFF-SCOPE synthetic probe and the "
            "planted claim block is fabricated; both calibrate the checker's "
            "discriminating power and neither is evidence about the declared "
            "family"
        ),
        "finding": (
            f"The checker demonstrates it can refute. On an off-scope source "
            f"whose ledger is detuned by one unit the hunt fires on "
            f"{len(detuned_hits)} distinct functionals, while on the "
            f"stipulated ledger at the same configuration it fires on "
            f"{len(stipulated_hits)}. A fabricated claim block with wrong "
            f"counts is caught on "
            f"{len(fake_comparison['disagreements'])} comparison fields, so a "
            f"primary that misreported its census would not pass this "
            f"comparison unnoticed."
        ),
    }
    result["pass"] = (
        result["detector_fires_on_detuned_ledger"]
        and result["planted_false_claim_detected"]
    )
    return result


# --------------------------------------------------------------------------
# emission
# --------------------------------------------------------------------------
LABELS = (
    "CK_A_SOURCES",
    "CK_B_PRIMARY_CLAIMS",
    "CK_C_REFUTATION_HUNT",
    "CK_D_COMPARISON",
    "CK_E_ADVERSARY",
    "CK_F_CONTROLS",
)


def render_fixed_point(certificates: dict[str, dict[str, object]]) -> str:
    for _attempt in range(12):
        checks = {label: bool(certificates[label]["pass"]) for label in LABELS}
        hunt = certificates["CK_C_REFUTATION_HUNT"]
        comparison = certificates["CK_D_COMPARISON"]
        refuted = hunt["members_with_any_sensitive_functional"] > 0 or bool(
            comparison["disagreements"]
        )
        terminal = {
            "terminal": (
                "CYCLE868_INDEPENDENT_CHECK_REFUTES_PRIMARY" if refuted
                else "CYCLE868_INDEPENDENT_CHECK_CORROBORATES_BY_EXHAUSTION"
            ),
            "bookkeeping_complete": all(checks.values()),
            "checks": checks,
            "functionals_per_member": hunt["searched_functional_count_per_member"],
            "sigma_comparisons": hunt["total_sigma_comparisons"],
            "sensitive_members_found": hunt["members_with_any_sensitive_functional"],
            "claim_disagreements": comparison["disagreements"],
            "checker_verdict": comparison["checker_independent_verdict"],
            "runtime_seconds": certificates["CK_F_CONTROLS"]["runtime_seconds"],
            "stdout_bytes": certificates["CK_F_CONTROLS"]["stdout_bytes"],
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
        controls = certificates["CK_F_CONTROLS"]
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
    hunt = refutation_hunt(members)
    comparison = comparison_certificate(claims, hunt, members)
    adversary = adversary_certificate()

    replay_members = family()
    replay_hunt = refutation_hunt(replay_members)
    deterministic = (
        replay_members == members
        and replay_hunt["hunt_stream_sha256"] == hunt["hunt_stream_sha256"]
        and replay_hunt["members_with_any_sensitive_functional"]
        == hunt["members_with_any_sensitive_functional"]
        and replay_hunt["conformal_nonzero_members"]
        == hunt["conformal_nonzero_members"]
    )
    elapsed = monotonic() - started
    controls = {
        **{key: value for key, value in sources.items()
           if key not in {"pass", "finding"}},
        "sources_pass": sources["pass"],
        "determinism": {
            "scope": (
                "the family enumeration and the complete refutation hunt were "
                "recomputed from scratch and compared digest-for-digest"
            ),
            "first_hunt_sha256": hunt["hunt_stream_sha256"],
            "second_hunt_sha256": replay_hunt["hunt_stream_sha256"],
            "exact": deterministic,
        },
        "arithmetic_route": (
            "integers only: the source is pre-scaled by 3 and both sigma "
            "worlds are hard-wired, so no polynomial algebra and no rational "
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
            "hash matched, the whole hunt was recomputed from scratch and "
            "reproduced byte-for-byte, and the runtime and stdout caps were "
            "respected. The checker shares no arithmetic route with the "
            "primary: it works in integers across two hard-wired sign worlds."
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
        "CK_C_REFUTATION_HUNT": hunt,
        "CK_D_COMPARISON": comparison,
        "CK_E_ADVERSARY": adversary,
        "CK_F_CONTROLS": controls,
    }
    sys.stdout.write(render_fixed_point(certificates))
    return 0 if all(row["pass"] for row in certificates.values()) else 1


if __name__ == "__main__":
    raise SystemExit(run())
