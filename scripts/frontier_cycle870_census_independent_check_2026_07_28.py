#!/usr/bin/env python3
"""Cycle 870 independent check of the general-n census law and n=12 table.

The primary is source evidence only: this checker reads and parses it, and
reads its pinned run cache, but never imports or executes it.  Every number
is recomputed by a deliberately different route:

  * placement counts by integer-polynomial transfer-matrix powers and by a
    path/ring conditioning DP -- no closed form, no sympy;
  * orbit structure by minimal-period canonical forms and, independently, by
    Burnside/Moebius inversion over the divisor lattice with fixed-point
    counts read off the C_gcd sub-ring -- not by rotating sets;
  * the invariant-subset floor from that Moebius spectrum alone.

The harness is spec'd to REFUTE.  Each primary claim gets a refutation
attempt; the checker also runs its refuter against deliberately wrong
mutants and fails if the refuter cannot kill them.

Demoted surfaces (review iteration 1, 2026-08-08, FIX_THEN_PROCEED): the
factor-four phased values re-checked here are CONDITIONAL on the
primary's SUPPLIED free Cartesian Z_4 phase premise, which neither
script derives; the n=12 comparator tuple is a stipulated in-file
literal with no source artifact, so its comparison is local and
attributes nothing to any external document; "selection" means exactly
a nonempty C_n-invariant subset of the finite placement set; and the
running branch and HEAD are recorded as provenance only, with no PASS
authority.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
import json
from pathlib import Path
import subprocess
import sys
from time import monotonic


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000

AUDIT_INPUT_PATHS = (
    "scripts/frontier_cycle870_general_n_census_2026_07_28.py",
    "logs/runner-cache/frontier_cycle870_general_n_census_2026_07_28.txt",
)
PRIMARY_PATH, PRIMARY_CACHE_PATH = AUDIT_INPUT_PATHS
PRIMARY_MODULE = Path(PRIMARY_PATH).stem
EXPECTED_SHA256 = {
    PRIMARY_PATH:
        "3b497c65a6a29dd7ec1b07294366d687559f1b57a45a93ee7e1b662b152f5e2a",
    PRIMARY_CACHE_PATH:
        "74e2b80c57a52548e44b359e6824bc95e59c1fa30bb9634c32f1d97fcdf9f99d",
}
EXPECTED_GIT_BLOBS = {
    PRIMARY_PATH: "4d8eb188db6372a7e61bad846118cee612b9aeab",
    PRIMARY_CACHE_PATH: "3232bf367c76e9a87d54ec1f05914c7aea92a59d",
}

PHASE_COUNT = 4
COMPOSITE_N = 12
PRIME_N = 11
CHECK_N_MAX = 24
MOEBIUS_N_MAX = 40
# Values the primary reports but must not be able to smuggle in as literals.
NON_LITERAL_WITNESSES = (
    448, 420, 144, 216, 54, 112, 105, 36, 77, 55, 199, 322, 309,
)
ALLOWED_PRIMARY_PATH_STRINGS = (PRIMARY_PATH,)


class _PrimaryBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if the Cycle-870 primary is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        if fullname.split(".")[-1] == PRIMARY_MODULE:
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids primary import: {fullname}")
        return None


PRIMARY_BLOCKER = _PrimaryBlocker()
sys.meta_path.insert(0, PRIMARY_BLOCKER)


def compact(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value: object) -> str:
    return sha256(compact(value).encode("utf-8")).hexdigest()


def git_blob_sha(payload: bytes) -> str:
    header = f"blob {len(payload)}\0".encode("ascii")
    return sha1(header + payload).hexdigest()


def git_text(*arguments: str) -> str:
    return subprocess.run(
        ("git", *arguments),
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8").strip()


def key_str(mapping: dict[int, int]) -> dict[str, int]:
    return {str(key): int(value) for key, value in sorted(mapping.items())}


# ---------------------------------------------------------------------------
# Independent route 1: conditioning DP (paths and rings), pure integers
# ---------------------------------------------------------------------------


def path_profile(vertices: int) -> dict[int, int]:
    """j-subsets of a path on `vertices` vertices with no two adjacent."""
    if vertices < 0:
        return {}
    table: list[dict[int, int]] = [{0: 1}, {0: 1, 1: 1}]
    if vertices == 0:
        return dict(table[0])
    for size in range(2, vertices + 1):
        current = dict(table[size - 1])
        for chosen, count in table[size - 2].items():
            current[chosen + 1] = current.get(chosen + 1, 0) + count
        table.append(current)
    return dict(table[vertices])


def ring_profile_dp(n: int) -> dict[int, int]:
    """I(n,k) by conditioning on site 0: unselected -> path(n-1);
    selected -> sites 1 and n-1 forbidden, path(n-3) carries k-1."""
    if n == 1:
        return {0: 1}
    if n == 2:
        return {0: 1, 1: 2}
    unselected = path_profile(n - 1)
    selected = path_profile(n - 3)
    profile = dict(unselected)
    for chosen, count in selected.items():
        profile[chosen + 1] = profile.get(chosen + 1, 0) + count
    return {k: v for k, v in sorted(profile.items()) if v}


# ---------------------------------------------------------------------------
# Independent route 2: integer polynomial transfer matrix (no sympy)
# ---------------------------------------------------------------------------


def poly_add(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    width = max(len(left), len(right))
    return tuple(
        (left[i] if i < len(left) else 0) + (right[i] if i < len(right) else 0)
        for i in range(width)
    )


def poly_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    if not left or not right:
        return ()
    out = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if not a:
            continue
        for j, b in enumerate(right):
            out[i + j] += a * b
    return tuple(out)


def matrix_mul(
    left: tuple[tuple[tuple[int, ...], ...], ...],
    right: tuple[tuple[tuple[int, ...], ...], ...],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    return tuple(
        tuple(
            poly_add(
                poly_mul(left[row][0], right[0][col]),
                poly_mul(left[row][1], right[1][col]),
            )
            for col in range(2)
        )
        for row in range(2)
    )


def ring_profile_transfer(n: int) -> dict[int, int]:
    """I(n,k) from tr T(x)^n with T(x) = [[1,x],[1,0]] over Z[x]."""
    base = (((1,), (0, 1)), ((1,), ()))
    power = base
    for _step in range(n - 1):
        power = matrix_mul(power, base)
    trace = poly_add(power[0][0], power[1][1])
    return {k: c for k, c in enumerate(trace) if c}


# ---------------------------------------------------------------------------
# Independent route 3: minimal-period canonical forms (orbit structure)
# ---------------------------------------------------------------------------


def independent_masks(n: int) -> tuple[int, ...]:
    masks = []
    full = (1 << n) - 1
    for mask in range(1 << n):
        rotated = ((mask << 1) | (mask >> (n - 1))) & full
        if not (mask & rotated):
            masks.append(mask)
    return tuple(masks)


def rotate_mask(mask: int, shift: int, n: int) -> int:
    full = (1 << n) - 1
    shift %= n
    return ((mask << shift) | (mask >> (n - shift))) & full if shift else mask


def canonical_orbits(n: int) -> tuple[dict[str, object], ...]:
    """Orbits keyed by minimal rotation; orbit size = minimal period."""
    rows: dict[int, dict[str, object]] = {}
    for mask in independent_masks(n):
        rotations = [rotate_mask(mask, shift, n) for shift in range(n)]
        canonical = min(rotations)
        if canonical in rows:
            continue
        period = next(
            p for p in range(1, n + 1)
            if n % p == 0 and rotate_mask(mask, p, n) == mask
        )
        rows[canonical] = {
            "k": bin(mask).count("1"),
            "orbit_size": period,
            "distinct_rotations": len(set(rotations)),
        }
    return tuple(rows.values())


# ---------------------------------------------------------------------------
# Independent route 4: Burnside / Moebius over the divisor lattice
# ---------------------------------------------------------------------------


def divisors_of(n: int) -> tuple[int, ...]:
    return tuple(d for d in range(1, n + 1) if n % d == 0)


def mobius(n: int) -> int:
    result = 1
    remaining = n
    factor = 2
    while factor * factor <= remaining:
        if remaining % factor == 0:
            remaining //= factor
            if remaining % factor == 0:
                return 0
            result = -result
        factor += 1
    if remaining > 1:
        result = -result
    return result


def subring_profile(g: int) -> dict[int, int]:
    """Independent sets of the quotient ring C_g, by size."""
    if g == 1:
        return {0: 1}
    if g == 2:
        return {0: 1, 1: 2}
    return ring_profile_dp(g)


def invariant_profile(n: int, g: int) -> dict[int, int]:
    """Size profile of placements in C_n fixed by the subgroup <g>."""
    block = n // g
    return {
        size * block: count for size, count in subring_profile(g).items()
    }


def moebius_spectrum(n: int) -> dict[tuple[int, int], int]:
    """(orbit_size, k) -> orbit count, by exact-stabilizer Moebius inversion."""
    spectrum: dict[tuple[int, int], int] = {}
    for g in divisors_of(n):
        exact: Counter[int] = Counter()
        for h in divisors_of(g):
            coefficient = mobius(g // h)
            if not coefficient:
                continue
            for size, count in invariant_profile(n, h).items():
                exact[size] += coefficient * count
        for size, count in exact.items():
            if count:
                if count % g:
                    raise AssertionError(("non-integral orbit count", n, g, size))
                spectrum[(g, size)] = count // g
    return spectrum


def spectrum_by_scope(
    spectrum: dict[tuple[int, int], int], k_min: int
) -> dict[int, int]:
    counts: Counter[int] = Counter()
    for (orbit_size, k), count in spectrum.items():
        if k >= k_min:
            counts[orbit_size] += count
    return dict(sorted(counts.items()))


def min_invariant_subset(n: int) -> int:
    """Minimum size of a nonempty C_n-invariant subset of placements."""
    return min(
        orbit_size for (orbit_size, k) in moebius_spectrum(n) if k >= 1
    )


def smallest_prime_factor(n: int) -> int:
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n


# ---------------------------------------------------------------------------
# Primary evidence: source and pinned cache, parsed never imported
# ---------------------------------------------------------------------------


def read_inputs() -> dict[str, bytes]:
    return {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}


def parse_cache(text: str) -> dict[str, object]:
    header: dict[str, str] = {}
    body_lines: list[str] = []
    in_stdout = False
    for line in text.splitlines():
        if line.startswith("----- stdout -----"):
            in_stdout = True
            continue
        if line.startswith("----- stderr -----"):
            in_stdout = False
            continue
        if in_stdout:
            body_lines.append(line)
        elif ":" in line and not line.startswith("====="):
            key, _sep, value = line.partition(":")
            header[key.strip()] = value.strip()
    certificates: dict[str, object] = {}
    final: object = None
    terminal = ""
    for line in body_lines:
        if line.startswith(("PASS ", "FAIL ")) and " FINDING=" in line:
            label = line.split(" ", 2)[1]
            certificates[label] = json.loads(line.split(" :: ", 1)[1])
        elif line.startswith("FINAL :: "):
            final = json.loads(line.split(" :: ", 1)[1])
        elif line.startswith("CYCLE870_"):
            terminal = line.strip()
    return {
        "header": header,
        "certificates": certificates,
        "final": final,
        "terminal": terminal,
        "stdout_lines": len(body_lines),
    }


# ---------------------------------------------------------------------------
# The refuter
# ---------------------------------------------------------------------------


def refute(claim: str, holds: bool) -> dict[str, object]:
    return {"claim": claim, "verdict": "SURVIVED" if holds else "REFUTED"}


def run_refuter(claims: dict[str, bool]) -> dict[str, str]:
    return {
        name: refute(name, holds)["verdict"] for name, holds in claims.items()
    }


def certificate_a_independent_counts() -> dict[str, object]:
    dp_rows = {}
    agreement = True
    for n in range(3, CHECK_N_MAX + 1):
        dp = ring_profile_dp(n)
        transfer = ring_profile_transfer(n)
        agreement = agreement and dp == transfer
        dp_rows[n] = dp
    brute_agreement = True
    for n in range(3, 17):
        masks = independent_masks(n)
        brute = Counter(bin(mask).count("1") for mask in masks)
        brute_agreement = brute_agreement and dict(sorted(brute.items())) == {
            k: v for k, v in sorted(ring_profile_dp(n).items())
        }
    lucas_rows = {n: sum(dp_rows[n].values()) for n in dp_rows}
    lucas_recurrence = all(
        lucas_rows[n] == lucas_rows[n - 1] + lucas_rows[n - 2]
        for n in range(5, CHECK_N_MAX + 1)
    )
    result = {
        "certificate": "A_INDEPENDENT_COUNTS",
        "finding": "TWO_INDEPENDENT_ROUTES_AGREE",
        "range": (3, CHECK_N_MAX),
        "dp_equals_transfer_matrix": agreement,
        "dp_equals_bitmask_brute_force": brute_agreement,
        "totals_obey_lucas_recurrence": lucas_recurrence,
        "n11_profile": key_str(dp_rows[11]),
        "n12_profile": key_str(dp_rows[12]),
        "n11_total": lucas_rows[11],
        "n12_total": lucas_rows[12],
    }
    result["pass"] = (
        agreement and brute_agreement and lucas_recurrence
    )
    return result


def certificate_b_independent_orbits() -> dict[str, object]:
    canonical = canonical_orbits(COMPOSITE_N)
    canonical_spectrum = {
        (int(row["orbit_size"]), int(row["k"])): 0 for row in canonical
    }
    for row in canonical:
        canonical_spectrum[(int(row["orbit_size"]), int(row["k"]))] += 1
    moebius = moebius_spectrum(COMPOSITE_N)
    periods_consistent = all(
        int(row["orbit_size"]) == int(row["distinct_rotations"])
        for row in canonical
    )
    scopes = {
        "K_EQ_2": {
            size: count
            for size, count in sorted(Counter({
                orbit_size: total
                for (orbit_size, k), total in moebius.items() if k == 2
            }).items())
        },
        "K_GE_2": spectrum_by_scope(moebius, 2),
        "K_GE_1": spectrum_by_scope(moebius, 1),
        "ALL_K": spectrum_by_scope(moebius, 0),
    }
    element_totals = {
        name: sum(size * count for size, count in spectrum.items())
        for name, spectrum in scopes.items()
    }
    profile = ring_profile_dp(COMPOSITE_N)
    result = {
        "certificate": "B_INDEPENDENT_ORBITS",
        "finding": "CANONICAL_FORM_AND_MOEBIUS_ROUTES_AGREE",
        "n": COMPOSITE_N,
        "canonical_equals_moebius": canonical_spectrum == moebius,
        "orbit_size_equals_minimal_period": periods_consistent,
        "canonical_orbit_count": len(canonical),
        "moebius_orbit_count": sum(moebius.values()),
        "scoped_spectra": {
            name: key_str(spectrum) for name, spectrum in scopes.items()
        },
        "scoped_element_totals": element_totals,
        "all_k_elements_equal_census_total":
            element_totals["ALL_K"] == sum(profile.values()),
        "phased_orbit_multiplicities_k_ge_2": key_str({
            size: PHASE_COUNT * count
            for size, count in scopes["K_GE_2"].items()
        }),
    }
    result["pass"] = (
        result["canonical_equals_moebius"]
        and result["orbit_size_equals_minimal_period"]
        and result["all_k_elements_equal_census_total"]
        and result["canonical_orbit_count"] == result["moebius_orbit_count"]
    )
    return result


def certificate_c_refutation(cache: dict[str, object]) -> dict[str, object]:
    certificates = cache["certificates"]
    final = cache["final"]
    law = certificates["A_GENERAL_LAW"]
    n11 = certificates["B_N11_REPRODUCTION"]
    n12 = certificates["C_COMPOSITE_TABLE"]
    scope = certificates["D_SELECTION_SCOPE"]

    independent_n11 = {
        str(k): PHASE_COUNT * v
        for k, v in ring_profile_dp(PRIME_N).items()
    }
    independent_n12 = {
        str(k): PHASE_COUNT * v
        for k, v in ring_profile_dp(COMPOSITE_N).items()
    }
    moebius = moebius_spectrum(COMPOSITE_N)
    k_eq_2 = {
        orbit_size: total
        for (orbit_size, k), total in moebius.items() if k == 2
    }
    k_ge_2 = spectrum_by_scope(moebius, 2)
    comparator = {
        int(k): v
        for k, v in n12["supplied_comparator_spectrum"].items()
    }
    comparator_row = tuple(n12["supplied_comparator_phased_row"])
    phased_multiplicities = tuple(
        PHASE_COUNT * k_ge_2[size] for size in sorted(comparator)
    )

    # The law as the primary states it, re-evaluated from independent counts.
    law_rows_ok = True
    for n in range(3, CHECK_N_MAX + 1):
        profile = ring_profile_dp(n)
        for k in range(1, n // 2 + 1):
            numerator = n * _binomial(n - k - 1, k - 1)
            alt = n * _binomial(n - k, k)
            law_rows_ok = law_rows_ok and numerator % k == 0
            law_rows_ok = law_rows_ok and alt % (n - k) == 0
            law_rows_ok = (
                law_rows_ok
                and numerator // k == profile.get(k, 0)
                and alt // (n - k) == profile.get(k, 0)
            )

    spf_rows_ok = all(
        min_invariant_subset(n) == smallest_prime_factor(n)
        for n in range(3, MOEBIUS_N_MAX + 1)
    )
    no_singleton_subset = all(
        min_invariant_subset(n) > 1 for n in range(3, MOEBIUS_N_MAX + 1)
    )

    claims = {
        "R1_general_law_matches_independent_counts": law_rows_ok,
        "R2_n11_phased_row": n11["phased_census"] == independent_n11,
        "R3_n11_quoted_subrow": tuple(n11["quoted_subrow"]) == (
            independent_n11["2"], independent_n11["3"],
            independent_n11["4"], independent_n11["5"],
        ),
        "R4_n12_phased_census": n12["phased_census"] == independent_n12,
        "R5_n12_k_eq_2_spectrum": {
            str(size): count for size, count in sorted(k_eq_2.items())
        } == n12["native_spectra"]["K_EQ_2"],
        "R6_n12_k_ge_2_spectrum": {
            str(size): count for size, count in sorted(k_ge_2.items())
        } == n12["native_spectra"]["K_GE_2"],
        "R7_comparator_declared_scope_mismatch": (
            k_eq_2 != comparator
            and n12["comparator_scope_label_mismatch"] is True
        ),
        "R8_comparator_numbers_are_k_ge_2": (
            k_ge_2 == comparator
            and tuple(n12["comparator_spectrum_matching_scopes"])
            == ("K_GE_2",)
        ),
        "R9_phased_row_is_multiplicities": (
            phased_multiplicities == comparator_row
            and n12["comparator_phased_row_is_multiplicities"] is True
        ),
        "R10_phased_row_is_not_orbit_sizes": (
            tuple(PHASE_COUNT * size for size in sorted(comparator))
            != comparator_row
        ),
        "R11_min_invariant_subset_n12": (
            scope["min_nonempty_orbit_size_n12"]
            == min_invariant_subset(COMPOSITE_N) == 2
        ),
        "R12_invariant_subset_floor_is_spf": spf_rows_ok,
        "R13_no_singleton_invariant_subset": no_singleton_subset,
        "R14_prime_n11_orbits_all_free": (
            min_invariant_subset(PRIME_N) == PRIME_N
            and tuple(scope["prime_n11_orbit_sizes"]) == (PRIME_N,)
        ),
        "R15_primary_theorem_string_matches_law": (
            "(n/k) * C(n-k-1, k-1)" in str(law["theorem"])
            and "n/(n-k) * C(n-k, k)" in str(law["theorem"])
            and "Conditional on the supplied phase premise"
            in str(law["theorem"])
            and "supplied, not derived" in str(law["theorem"])
        ),
        "R16_final_block_consistent": (
            final is not None
            and final["min_invariant_subset_n12"] == 2
            and final["min_invariant_subset_n12_with_phase_conditional"]
            == PHASE_COUNT * 2
            and final["phase_values_conditional_on_supplied_premise"] is True
            and final["pass"] is True
        ),
    }
    verdicts = run_refuter(claims)

    # Harness teeth: the same refuter applied to deliberately wrong claims.
    # M5 is the per-source-phase census model N(n,k) = 4^k * I(n,k): the
    # mutant keeps the placement multiplicity I(n,k) on its own side, so it
    # AGREES with the correct model at k = 1 and must fail at some k >= 2.
    n11_unphased = ring_profile_dp(PRIME_N)
    m5_mutant_agrees_at_k1 = (
        PHASE_COUNT * n11_unphased[1] == PHASE_COUNT**1 * n11_unphased[1]
    )
    m5_mutant_fails_beyond_k1 = any(
        PHASE_COUNT * v != PHASE_COUNT**k * v
        for k, v in n11_unphased.items() if k >= 2
    )
    mutant_claims = {
        "M1_n11_row_off_by_one": independent_n11 == dict(
            independent_n11, **{"5": independent_n11["5"] + 1}
        ),
        "M2_comparator_is_k_eq_2": k_eq_2 == comparator,
        "M3_min_invariant_subset_is_one": min_invariant_subset(COMPOSITE_N) == 1,
        "M4_floor_is_largest_prime_factor": all(
            min_invariant_subset(n) == max(
                p for p in range(2, n + 1)
                if n % p == 0 and smallest_prime_factor(p) == p
            )
            for n in range(3, 25)
        ),
        "M5_phase_factor_is_4_to_the_k": all(
            PHASE_COUNT * v == PHASE_COUNT**k * v
            for k, v in n11_unphased.items() if k
        ),
        "M6_counts_are_plain_binomials": all(
            ring_profile_dp(12).get(k, 0) == _binomial(12, k)
            for k in (2, 3, 4)
        ),
        "M7_orbit_sizes_all_equal_n": all(
            orbit_size == COMPOSITE_N
            for (orbit_size, k) in moebius_spectrum(COMPOSITE_N) if k >= 1
        ),
    }
    mutant_verdicts = run_refuter(mutant_claims)

    result = {
        "certificate": "C_REFUTATION_HARNESS",
        "finding": "ALL_PRIMARY_CLAIMS_SURVIVE_ALL_MUTANTS_REFUTED",
        "primary_claim_verdicts": verdicts,
        "primary_claims_surviving": sum(
            1 for verdict in verdicts.values() if verdict == "SURVIVED"
        ),
        "primary_claims_refuted": tuple(sorted(
            name for name, verdict in verdicts.items() if verdict == "REFUTED"
        )),
        "mutant_verdicts": mutant_verdicts,
        "mutants_refuted": sum(
            1 for verdict in mutant_verdicts.values() if verdict == "REFUTED"
        ),
        "mutants_surviving": tuple(sorted(
            name for name, verdict in mutant_verdicts.items()
            if verdict == "SURVIVED"
        )),
        "independent_n11_phased": independent_n11,
        "independent_n12_phased": independent_n12,
        "independent_k_eq_2_spectrum": key_str(k_eq_2),
        "independent_k_ge_2_spectrum": key_str(k_ge_2),
        "independent_phased_multiplicities": phased_multiplicities,
        "phase_values_conditional_on_supplied_premise": True,
        "m5_mutant_agrees_at_k1": m5_mutant_agrees_at_k1,
        "m5_mutant_fails_beyond_k1": m5_mutant_fails_beyond_k1,
        "invariant_subset_floor_range": (3, MOEBIUS_N_MAX),
    }
    result["pass"] = (
        not result["primary_claims_refuted"]
        and not result["mutants_surviving"]
        and result["mutants_refuted"] == len(mutant_claims)
        and result["m5_mutant_agrees_at_k1"]
        and result["m5_mutant_fails_beyond_k1"]
    )
    return result


def _binomial(n: int, k: int) -> int:
    if k < 0 or n < 0 or k > n:
        return 0
    value = 1
    for step in range(k):
        value = value * (n - step) // (step + 1)
    return value


def certificate_d_primary_hygiene(
    payloads: dict[str, bytes], cache: dict[str, object]
) -> dict[str, object]:
    tree = ast.parse(payloads[PRIMARY_PATH], filename=PRIMARY_PATH)
    int_literals = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, int)
        and not isinstance(node.value, bool)
    }
    string_constants = {
        node.value
        for node in ast.walk(tree)
        if isinstance(node, ast.Constant) and isinstance(node.value, str)
    }
    repo_path_strings = tuple(sorted(
        value for value in string_constants
        if value.startswith(("scripts/", "docs/", "logs/", "outputs/"))
    ))
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import) for alias in node.names
    }
    imports.update(
        node.module for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    smuggled = tuple(sorted(
        value for value in NON_LITERAL_WITNESSES if value in int_literals
    ))
    header = cache["header"]
    result = {
        "certificate": "D_PRIMARY_HYGIENE",
        "finding": "PRIMARY_DERIVES_ITS_NUMBERS",
        "primary_access_mode": "read_bytes + ast.parse; never import/execute",
        "blocker_hits": tuple(PRIMARY_BLOCKER.hits),
        "primary_module_loaded": PRIMARY_MODULE in sys.modules,
        "smuggled_answer_literals": smuggled,
        "no_smuggled_answer_literals": not smuggled,
        "primary_repo_path_strings": repo_path_strings,
        "primary_reads_only_itself":
            repo_path_strings == ALLOWED_PRIMARY_PATH_STRINGS,
        "primary_imports": tuple(sorted(imports)),
        "primary_imports_no_sibling_runner": not any(
            name.split(".")[-1].startswith(("frontier_", "kcpt_"))
            for name in imports
        ),
        "cache_exit_code": header.get("exit_code"),
        "cache_status": header.get("status"),
        "cache_runner": header.get("runner"),
        "cache_runner_sha256": header.get("runner_sha256"),
        "cache_sha_matches_pinned_primary":
            header.get("runner_sha256") == EXPECTED_SHA256[PRIMARY_PATH],
        "cache_terminal_line": cache["terminal"],
        "cache_terminal_is_pass":
            cache["terminal"] == "CYCLE870_GENERAL_N_CENSUS_LAW_PASS",
        "cache_certificate_labels": tuple(sorted(cache["certificates"])),
    }
    result["pass"] = (
        not result["blocker_hits"]
        and not result["primary_module_loaded"]
        and result["no_smuggled_answer_literals"]
        and result["primary_reads_only_itself"]
        and result["primary_imports_no_sibling_runner"]
        and result["cache_exit_code"] == "0"
        and result["cache_status"] == "ok"
        and result["cache_runner"] == PRIMARY_PATH
        and result["cache_sha_matches_pinned_primary"]
        and result["cache_terminal_is_pass"]
        and result["cache_certificate_labels"] == (
            "A_GENERAL_LAW", "B_N11_REPRODUCTION", "C_COMPOSITE_TABLE",
            "D_SELECTION_SCOPE", "E_CONTROLS",
        )
    )
    return result


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    for node in tree.body:
        targets: list[ast.expr] = []
        if isinstance(node, ast.AnnAssign):
            targets = [node.target]
            value = node.value
        elif isinstance(node, ast.Assign):
            targets = list(node.targets)
            value = node.value
        else:
            continue
        if value is None:
            continue
        if any(isinstance(t, ast.Name) and t.id == name for t in targets):
            try:
                return ast.literal_eval(value)
            except ValueError:
                return None
    return None


def certificate_e_controls(
    fingerprint_first: str,
    fingerprint_repeat: str,
    payloads_before: dict[str, bytes],
    payloads_after: dict[str, bytes],
    runtime_seconds: float,
) -> dict[str, object]:
    self_payload = Path(__file__).read_bytes()
    self_tree = ast.parse(self_payload, filename=Path(__file__).name)
    actual_sha = {
        path: sha256(payload).hexdigest()
        for path, payload in payloads_before.items()
    }
    actual_blobs = {
        path: git_blob_sha(payload)
        for path, payload in payloads_before.items()
    }
    write_calls = tuple(sorted({
        node.func.attr
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {
            "write_text", "write_bytes", "mkdir", "unlink", "rename",
            "touch", "rmdir", "replace",
        }
    }))
    imported = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import) for alias in node.names
    }
    imported.update(
        node.module for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
    result = {
        "certificate": "E_CONTROLS",
        "finding": "CONTROLS_CLEAN",
        "AUDIT_INPUT_PATHS": AUDIT_INPUT_PATHS,
        "literal_audit_input_paths":
            tuple(literal_assignment(self_tree, "AUDIT_INPUT_PATHS") or ())
            == AUDIT_INPUT_PATHS,
        "inputs_existing_worktree_relative": all(
            not Path(path).is_absolute()
            and ".." not in Path(path).parts
            and (ROOT / path).is_file()
            for path in AUDIT_INPUT_PATHS
        ),
        "input_sha256_pins": actual_sha,
        "input_sha256_pins_match": actual_sha == EXPECTED_SHA256,
        "input_git_blob_pins_match": actual_blobs == EXPECTED_GIT_BLOBS,
        "inputs_unchanged": payloads_before == payloads_after,
        "checker_uses_no_symbolic_algebra": "sympy" not in imported,
        "imported_modules": tuple(sorted(imported)),
        "no_write_calls_in_source": not write_calls,
        "write_calls_found": write_calls,
        "blocker_hits": tuple(PRIMARY_BLOCKER.hits),
        "primary_module_never_loaded": PRIMARY_MODULE not in sys.modules,
        # Branch and HEAD are provenance only: they never gate PASS, so
        # the checker is portable to main, detached, and audit worktrees.
        "running_branch_provenance_only":
            git_text("rev-parse", "--abbrev-ref", "HEAD"),
        "execution_head_sha_provenance_only": git_text("rev-parse", "HEAD"),
        "primary_is_tracked_at_head": PRIMARY_PATH in git_text(
            "ls-tree", "--name-only", "HEAD", "scripts/"
        ),
        "determinism_replay": fingerprint_first == fingerprint_repeat,
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": False,
    }
    result["pass"] = (
        result["literal_audit_input_paths"]
        and result["inputs_existing_worktree_relative"]
        and result["input_sha256_pins_match"]
        and result["input_git_blob_pins_match"]
        and result["inputs_unchanged"]
        and result["checker_uses_no_symbolic_algebra"]
        and result["no_write_calls_in_source"]
        and not result["blocker_hits"]
        and result["primary_module_never_loaded"]
        and result["primary_is_tracked_at_head"]
        and result["determinism_replay"]
        and runtime_seconds < AUDIT_TIMEOUT_SEC
    )
    return result


def build_tables(payloads: dict[str, bytes]) -> dict[str, object]:
    cache = parse_cache(payloads[PRIMARY_CACHE_PATH].decode("utf-8"))
    return {
        "A_INDEPENDENT_COUNTS": certificate_a_independent_counts(),
        "B_INDEPENDENT_ORBITS": certificate_b_independent_orbits(),
        "C_REFUTATION_HARNESS": certificate_c_refutation(cache),
        "D_PRIMARY_HYGIENE": certificate_d_primary_hygiene(payloads, cache),
    }


def fingerprint(tables: dict[str, object]) -> str:
    return digest({
        label: compact(certificate) for label, certificate in tables.items()
    })


def render(
    tables: dict[str, object], controls: dict[str, object]
) -> str:
    refutation = tables["C_REFUTATION_HARNESS"]
    lines = [
        "CYCLE870_CENSUS_INDEPENDENT_CHECK",
        "DESIGN :: conditioning DP + integer transfer matrix + minimal-period "
        "canonical forms + Burnside/Moebius; primary read as text and cache "
        "only, never imported",
        "SPEC :: this checker is built to REFUTE -- every primary claim is a "
        "refutation target and the refuter is itself tested against mutants",
    ]
    for label in ("A_INDEPENDENT_COUNTS", "B_INDEPENDENT_ORBITS",
                  "C_REFUTATION_HARNESS", "D_PRIMARY_HYGIENE"):
        certificate = tables[label]
        lines.append(
            ("PASS " if certificate["pass"] else "FAIL ")
            + label + " FINDING=" + str(certificate["finding"])
            + " :: " + compact(certificate)
        )
    lines.append(
        ("PASS " if controls["pass"] else "FAIL ")
        + "E_CONTROLS FINDING=" + str(controls["finding"])
        + " :: " + compact(controls)
    )
    for name, verdict in sorted(refutation["primary_claim_verdicts"].items()):
        lines.append(f"REFUTATION_ATTEMPT :: {name} :: {verdict}")
    for name, verdict in sorted(refutation["mutant_verdicts"].items()):
        lines.append(f"MUTANT_PROBE :: {name} :: {verdict}")
    lines.append("FINAL :: " + compact({
        "primary_claims_tested": len(refutation["primary_claim_verdicts"]),
        "primary_claims_refuted": refutation["primary_claims_refuted"],
        "mutants_tested": len(refutation["mutant_verdicts"]),
        "mutants_surviving": refutation["mutants_surviving"],
        "independent_n11_phased": refutation["independent_n11_phased"],
        "independent_n12_phased": refutation["independent_n12_phased"],
        "independent_k_eq_2_spectrum":
            refutation["independent_k_eq_2_spectrum"],
        "independent_k_ge_2_spectrum":
            refutation["independent_k_ge_2_spectrum"],
        "comparator_scope_verdict":
            "MISMATCH_UNDER_DECLARED_K_EQ_2_EXACT_AS_K_GE_2",
        "phase_values_conditional_on_supplied_premise": True,
        "invariant_subset_floor_law": (
            "min nonempty C_n-invariant subset of placements has size "
            "spf(n); the x4 phase lift is conditional on the supplied "
            "Z_4 premise"
        ),
        "runtime_seconds": controls["runtime_seconds"],
        "pass": all(value["pass"] for value in tables.values())
            and controls["pass"],
    }))
    lines.append(
        "CYCLE870_CENSUS_INDEPENDENT_CHECK_PASS"
        if all(value["pass"] for value in tables.values()) and controls["pass"]
        else "CYCLE870_CENSUS_INDEPENDENT_CHECK_FAIL"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    payloads_before = read_inputs()
    tables = build_tables(payloads_before)
    repeat = build_tables(payloads_before)
    payloads_after = read_inputs()
    runtime_seconds = monotonic() - started
    controls = certificate_e_controls(
        fingerprint(tables),
        fingerprint(repeat),
        payloads_before,
        payloads_after,
        runtime_seconds,
    )
    output = render(tables, controls)
    for _attempt in range(3):
        output_bytes = len(output.encode("utf-8"))
        controls["stdout_bytes"] = output_bytes
        controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
        controls["pass"] = controls["pass"] and controls["stdout_within_limit"]
        updated = render(tables, controls)
        if len(updated.encode("utf-8")) == output_bytes:
            output = updated
            break
        output = updated
    output_bytes = len(output.encode("utf-8"))
    controls["stdout_bytes"] = output_bytes
    controls["stdout_within_limit"] = output_bytes < STDOUT_LIMIT_BYTES
    output = render(tables, controls)
    if len(output.encode("utf-8")) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(
            ("stdout bound", len(output.encode("utf-8")), STDOUT_LIMIT_BYTES)
        )
    sys.stdout.write(output)
    passed = all(value["pass"] for value in tables.values()) and controls["pass"]
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
