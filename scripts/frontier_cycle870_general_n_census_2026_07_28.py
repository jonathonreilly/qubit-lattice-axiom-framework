#!/usr/bin/env python3
"""Cycle 870: the general-n census law and the composite-ring (n=12) test.

Wave-1 of Campaign 5.  The landed Cycle-857 census fixed n=11 and reported
N_k = C(10-k, k-1) * 4 * 11 / k.  This runner derives the law for general n
(transfer matrix / eigenvalue expansion, plus an origin-marking double
count), reproduces the landed n=11 row exactly, builds the composite
falsification table at n=12 from a native orbit computation, and prices the
selection no-go at composite n.

Self-contained: no declared repo inputs, no imports of other cycle runners,
no writes.  Every reported number is derived in-process; the external n=12
prediction is carried only as a comparator and is scored, not assumed.
"""
from __future__ import annotations

import ast
from collections import Counter
from hashlib import sha1, sha256
import importlib.abc
from itertools import combinations
import json
from math import comb, gcd
from pathlib import Path
import subprocess
import sys
from time import monotonic

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150_000
EXPECTED_BRANCH = "physics-loop/toe-time-blockN1-20260802"
SELF_PATH = "scripts/frontier_cycle870_general_n_census_2026_07_28.py"

# No repo file is read as evidence: the census is derived from scratch.
DECLARED_INPUT_PATHS: tuple[str, ...] = ()
BLOCKLISTED_MODULE_PREFIXES = ("frontier_", "kcpt_", "final_", "full_law_")

PHASE_COUNT = 4
LANDED_CYCLE857_N = 11
# Landed Cycle-857 phased census row, k = 1..5 (comparator, not an input).
LANDED_CYCLE857_PHASED = {1: 44, 2: 176, 3: 308, 4: 220, 5: 44}
LANDED_CYCLE857_QUOTED_SUBROW = (176, 308, 220, 44)

COMPOSITE_N = 12
# External Cycle-870 prediction, carried verbatim as a comparator.  It is
# stated in the brief as the spectrum of "unphased k=2 placements"; this
# runner re-derives every candidate scope natively and scores the claim.
EXTERNAL_UNPHASED_SPECTRUM = {2: 1, 3: 1, 4: 1, 6: 2, 12: 24}
EXTERNAL_PHASED_ROW = (4, 4, 4, 8, 96)
EXTERNAL_DECLARED_SCOPE = "K_EQ_2"

BRUTE_N_MAX = 18
LAW_SPOT_N_MAX = 14
EXTENDED_N_MAX = 36


class _RunnerBlocker(importlib.abc.MetaPathFinder):
    """Fail closed if any other cycle runner is imported."""

    def __init__(self) -> None:
        self.hits: list[str] = []

    def find_spec(
        self,
        fullname: str,
        path: object = None,
        target: object = None,
    ) -> None:
        stem = fullname.split(".")[-1]
        if stem == Path(SELF_PATH).stem:
            return None
        if stem.startswith(BLOCKLISTED_MODULE_PREFIXES):
            self.hits.append(fullname)
            raise ImportError(f"BLOCKLIST forbids runner import: {fullname}")
        return None


RUNNER_BLOCKER = _RunnerBlocker()
sys.meta_path.insert(0, RUNNER_BLOCKER)


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


def literal_assignment(tree: ast.Module, name: str) -> object | None:
    for node in tree.body:
        if isinstance(node, ast.AnnAssign):
            if (
                isinstance(node.target, ast.Name)
                and node.target.id == name
                and node.value is not None
            ):
                try:
                    return ast.literal_eval(node.value)
                except ValueError:
                    return None
            continue
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == name:
                try:
                    return ast.literal_eval(node.value)
                except ValueError:
                    return None
    return None


def key_str(mapping: dict[int, int]) -> dict[str, int]:
    return {str(key): int(value) for key, value in sorted(mapping.items())}


# ---------------------------------------------------------------------------
# Ground truth: brute-force enumeration of cyclically independent placements
# ---------------------------------------------------------------------------


def brute_placements(n: int) -> tuple[frozenset[int], ...]:
    """Every S subset of Z_n with no two cyclically adjacent members."""
    found: list[frozenset[int]] = []
    for size in range(0, n // 2 + 1):
        for candidate in combinations(range(n), size):
            chosen = set(candidate)
            if all(((site + 1) % n) not in chosen for site in chosen):
                found.append(frozenset(chosen))
    return tuple(found)


def brute_profile(n: int) -> dict[int, int]:
    counts = Counter(len(placement) for placement in brute_placements(n))
    return {size: counts.get(size, 0) for size in range(0, n // 2 + 1)}


def kaplansky_closed_form(n: int, k: int) -> int:
    """I(n,k) = (n/k) C(n-k-1, k-1), the origin-marked closed form."""
    if k == 0:
        return 1
    numerator = n * comb(n - k - 1, k - 1)
    if numerator % k:
        raise AssertionError(("non-integral closed form", n, k))
    return numerator // k


def kaplansky_alt_form(n: int, k: int) -> int:
    """I(n,k) = n/(n-k) C(n-k, k), the eigenvalue-expansion closed form."""
    if k == 0:
        return 1
    numerator = n * comb(n - k, k)
    if numerator % (n - k):
        raise AssertionError(("non-integral alt form", n, k))
    return numerator // (n - k)


def path_independent_count(vertices: int, chosen: int) -> int:
    """j-subsets of a path on m vertices, no two adjacent: C(m-j+1, j)."""
    if chosen < 0 or vertices < 0:
        return 0
    return comb(vertices - chosen + 1, chosen)


def lucas(n: int) -> int:
    """Total cyclically independent sets in C_n; L_1 = 1, L_2 = 3."""
    if n <= 0:
        raise AssertionError(("lucas index", n))
    previous, current = 2, 1
    for _step in range(n - 1):
        previous, current = current, previous + current
    return current


def smallest_prime_factor(n: int) -> int:
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return n


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


# ---------------------------------------------------------------------------
# Certificate A: the general-n law
# ---------------------------------------------------------------------------


def certificate_a_general_law() -> dict[str, object]:
    x = sp.Symbol("x")
    transfer = sp.Matrix([[1, x], [1, 0]])

    # S1: transfer-matrix generating function against brute enumeration.
    s1_rows = []
    s1_ok = True
    for n in range(3, LAW_SPOT_N_MAX + 1):
        trace_poly = sp.Poly(sp.expand((transfer**n).trace()), x)
        brute = brute_profile(n)
        transfer_profile = {
            k: int(trace_poly.coeff_monomial(x**k))
            for k in range(0, n // 2 + 1)
        }
        matched = transfer_profile == brute
        s1_ok = s1_ok and matched and int(trace_poly.degree()) == n // 2
        s1_rows.append({"n": n, "trace_equals_brute": matched})

    # S2: the eigenvalue expansion, proved by the shared recurrence.
    root_plus = (1 + sp.sqrt(1 + 4 * x)) / 2
    root_minus = (1 - sp.sqrt(1 + 4 * x)) / 2
    char_residual = tuple(
        sp.simplify(root**2 - root - x) for root in (root_plus, root_minus)
    )
    n_sym = sp.Symbol("m", integer=True, positive=True)
    power_sum = root_plus**n_sym + root_minus**n_sym
    recurrence_residual = sp.simplify(
        power_sum.subs(n_sym, n_sym + 2)
        - power_sum.subs(n_sym, n_sym + 1)
        - x * power_sum
    )
    lucas_poly_residual = []
    s2_ok = True
    for n in range(3, LAW_SPOT_N_MAX + 1):
        expansion = sp.Poly(sp.expand(sp.simplify(root_plus**n + root_minus**n)), x)
        closed = {
            k: sp.Rational(n, n - k) * sp.binomial(n - k, k)
            for k in range(0, n // 2 + 1)
        }
        matched = all(
            sp.simplify(expansion.coeff_monomial(x**k) - closed[k]) == 0
            for k in range(0, n // 2 + 1)
        )
        s2_ok = s2_ok and matched
        lucas_poly_residual.append({"n": n, "eigen_expansion_is_lucas": matched})

    # S3: origin-marking double count k*I(n,k) = n*C(n-k-1, k-1).
    s3_rows = []
    s3_ok = True
    for n in range(3, BRUTE_N_MAX + 1):
        placements = brute_placements(n)
        for k in range(1, n // 2 + 1):
            sized = [p for p in placements if len(p) == k]
            marked_pairs = sum(len(p) for p in sized)
            through_origin = sum(1 for p in sized if 0 in p)
            path_form = path_independent_count(n - 3, k - 1)
            row_ok = (
                marked_pairs == k * len(sized)
                and marked_pairs == n * through_origin
                and through_origin == comb(n - k - 1, k - 1)
                and through_origin == path_form
                and len(sized) == kaplansky_closed_form(n, k)
                and len(sized) == kaplansky_alt_form(n, k)
            )
            s3_ok = s3_ok and row_ok
            if not row_ok:
                s3_rows.append({"n": n, "k": k, "ok": False})

    # S4: the two closed forms are one identity, symbolically.
    n_free, k_free = sp.symbols("n k", positive=True, integer=True)
    form_alt = n_free / (n_free - k_free) * sp.binomial(n_free - k_free, k_free)
    form_origin = (
        n_free / k_free * sp.binomial(n_free - k_free - 1, k_free - 1)
    )
    identity_residual = sp.simplify(
        sp.expand_func(form_alt) - sp.expand_func(form_origin)
    )

    # S5: the phase label is a free Z_4 factor.
    phase_rows = []
    phase_ok = True
    for n in range(3, BRUTE_N_MAX + 1):
        profile = brute_profile(n)
        for k, count in profile.items():
            expected = PHASE_COUNT * count
            got = PHASE_COUNT * kaplansky_closed_form(n, k)
            phase_ok = phase_ok and expected == got
        total = sum(profile.values())
        lucas_ok = total == lucas(n)
        phase_ok = phase_ok and lucas_ok
        phase_rows.append({"n": n, "total_is_lucas": lucas_ok, "L_n": total})

    theorem = (
        "N(n,k) = 4 * (n/k) * C(n-k-1, k-1) = 4 * n/(n-k) * C(n-k, k) "
        "for 3 <= n and 1 <= k <= floor(n/2); N(n,0) = 4."
    )
    proof_steps = (
        "S1 TRANSFER_MATRIX :: with T(x) = [[1,x],[1,0]] on the "
        "unoccupied/occupied state pair, tr T(x)^n is the generating "
        "function sum_k I(n,k) x^k of cyclically independent placements; "
        "verified against brute enumeration for n = 3..%d." % LAW_SPOT_N_MAX,
        "S2 EIGENVALUE_EXPANSION :: T(x) has char. polynomial L^2 - L - x, "
        "roots L_pm = (1 +- sqrt(1+4x))/2, so tr T^n = L_+^n + L_-^n.  That "
        "power sum obeys P_{n+2} = P_{n+1} + x P_n (residual 0 symbolically) "
        "with P_1 = 1, P_2 = 1 + 2x, whose solution is the Lucas polynomial "
        "sum_k n/(n-k) C(n-k,k) x^k; coefficient equality re-checked "
        "term-by-term for n = 3..%d." % LAW_SPOT_N_MAX,
        "S3 ORIGIN_MARKING :: double count pairs (S, s in S).  By S this is "
        "k*I(n,k); by s, Z_n transitivity gives n*A(n,k) with A(n,k) the "
        "placements containing site 0.  Cutting the ring at a selected 0 "
        "forbids sites 1 and n-1 and leaves a path on n-3 sites carrying "
        "k-1 non-adjacent selections: A(n,k) = C((n-3)-(k-1)+1, k-1) = "
        "C(n-k-1, k-1).  Hence I(n,k) = (n/k) C(n-k-1, k-1) -- this is the "
        "'x n origins / k labels' step.",
        "S4 FORM_IDENTITY :: n/(n-k) C(n-k,k) - n/k C(n-k-1,k-1) simplifies "
        "to 0 for symbolic n,k, so the eigenvalue route and the "
        "origin-marking route are the same law, not two coincident tables.",
        "S5 PHASE_FACTOR :: the phase label is a free Z_4 factor attached to "
        "the whole placement, independent of which sites are selected, so "
        "N(n,k) = 4 * I(n,k); the unphased totals sum_k I(n,k) reproduce the "
        "Lucas numbers L_n as an independent check.",
    )

    result = {
        "certificate": "A_GENERAL_LAW",
        "finding": "GENERAL_N_LAW_DERIVED",
        "theorem": theorem,
        "proof_steps": proof_steps,
        "s1_transfer_matrix_matches_brute": s1_ok,
        "s1_rows_checked": len(s1_rows),
        "s2_char_poly_residuals_zero": all(
            residual == 0 for residual in char_residual
        ),
        "s2_recurrence_residual_zero": recurrence_residual == 0,
        "s2_eigen_expansion_is_lucas_polynomial": s2_ok,
        "s2_rows_checked": len(lucas_poly_residual),
        "s3_origin_marking_double_count": s3_ok,
        "s3_failures": tuple(s3_rows),
        "s4_symbolic_form_identity_residual": str(identity_residual),
        "s4_forms_identical": identity_residual == 0,
        "s5_phase_factor_and_lucas_totals": phase_ok,
        "s5_lucas_totals": tuple(
            (row["n"], row["L_n"]) for row in phase_rows
        ),
        "brute_range": (3, BRUTE_N_MAX),
        "symbolic_range": (3, LAW_SPOT_N_MAX),
    }
    result["pass"] = (
        result["s1_transfer_matrix_matches_brute"]
        and result["s2_char_poly_residuals_zero"]
        and result["s2_recurrence_residual_zero"]
        and result["s2_eigen_expansion_is_lucas_polynomial"]
        and result["s3_origin_marking_double_count"]
        and not result["s3_failures"]
        and result["s4_forms_identical"]
        and result["s5_phase_factor_and_lucas_totals"]
    )
    return result


# ---------------------------------------------------------------------------
# Certificate B: n = 11 reproduction
# ---------------------------------------------------------------------------


def certificate_b_n11() -> dict[str, object]:
    n = LANDED_CYCLE857_N
    brute = brute_profile(n)
    closed = {k: kaplansky_closed_form(n, k) for k in brute}
    alt = {k: kaplansky_alt_form(n, k) for k in brute}
    cycle857_form = {
        k: comb(10 - k, k - 1) * PHASE_COUNT * 11 // k
        for k in range(1, n // 2 + 1)
    }
    phased = {k: PHASE_COUNT * brute[k] for k in brute}
    landed_rows = {k: phased[k] for k in LANDED_CYCLE857_PHASED}
    subrow = tuple(phased[k] for k in (2, 3, 4, 5))

    result = {
        "certificate": "B_N11_REPRODUCTION",
        "finding": "LANDED_N11_ROW_REPRODUCED",
        "n": n,
        "brute_unphased": key_str(brute),
        "closed_form_unphased": key_str(closed),
        "phased_census": key_str(phased),
        "brute_equals_closed_form": brute == closed,
        "brute_equals_alt_form": brute == alt,
        "cycle857_literal_form_agrees": cycle857_form == {
            k: phased[k] for k in cycle857_form
        },
        "landed_row_reproduced": landed_rows == LANDED_CYCLE857_PHASED,
        "quoted_subrow": subrow,
        "quoted_subrow_reproduced": subrow == LANDED_CYCLE857_QUOTED_SUBROW,
        "unphased_total": sum(brute.values()),
        "unphased_total_is_lucas_11": sum(brute.values()) == lucas(11),
        "phased_total": sum(phased.values()),
    }
    result["pass"] = (
        result["brute_equals_closed_form"]
        and result["brute_equals_alt_form"]
        and result["cycle857_literal_form_agrees"]
        and result["landed_row_reproduced"]
        and result["quoted_subrow_reproduced"]
        and result["unphased_total_is_lucas_11"]
    )
    return result


# ---------------------------------------------------------------------------
# Certificate C: the composite (n = 12) falsification table
# ---------------------------------------------------------------------------


def rotate(placement: frozenset[int], shift: int, n: int) -> frozenset[int]:
    return frozenset((site + shift) % n for site in placement)


def orbit_table(n: int) -> tuple[dict[str, object], ...]:
    placements = brute_placements(n)
    seen: set[frozenset[int]] = set()
    orbits: list[dict[str, object]] = []
    for placement in placements:
        if placement in seen:
            continue
        orbit = {rotate(placement, shift, n) for shift in range(n)}
        seen.update(orbit)
        representative = tuple(sorted(min(orbit, key=lambda s: sorted(s))))
        orbits.append({
            "representative": representative,
            "k": len(placement),
            "orbit_size": len(orbit),
            "stabilizer_order": n // len(orbit),
        })
    orbits.sort(key=lambda row: (row["k"], row["orbit_size"],
                                 row["representative"]))
    return tuple(orbits)


def spectrum_for(orbits: tuple[dict[str, object], ...],
                 predicate) -> dict[int, int]:
    counts = Counter(
        int(row["orbit_size"]) for row in orbits if predicate(row)
    )
    return dict(sorted(counts.items()))


def certificate_c_composite() -> dict[str, object]:
    n = COMPOSITE_N
    orbits = orbit_table(n)
    brute = brute_profile(n)
    closed = {k: kaplansky_closed_form(n, k) for k in brute}
    phased = {k: PHASE_COUNT * brute[k] for k in brute}

    scopes = {
        "K_EQ_2": lambda row: row["k"] == 2,
        "K_GE_2": lambda row: row["k"] >= 2,
        "K_GE_1": lambda row: row["k"] >= 1,
        "ALL_K": lambda row: True,
    }
    native = {
        name: spectrum_for(orbits, predicate)
        for name, predicate in scopes.items()
    }
    native_elements = {
        name: sum(size * count for size, count in spectrum.items())
        for name, spectrum in native.items()
    }
    # The phase label is a free Z_4 factor untouched by rotation, so each
    # unphased orbit splits into 4 phased orbits of the same size.
    phased_spectrum = {
        name: {size: PHASE_COUNT * count for size, count in spectrum.items()}
        for name, spectrum in native.items()
    }

    matching_scopes = tuple(
        name for name, spectrum in native.items()
        if spectrum == EXTERNAL_UNPHASED_SPECTRUM
    )
    declared_scope_matches = (
        native[EXTERNAL_DECLARED_SCOPE] == EXTERNAL_UNPHASED_SPECTRUM
    )
    external_row_sizes = tuple(sorted(EXTERNAL_UNPHASED_SPECTRUM))
    phased_as_multiplicities = tuple(
        phased_spectrum["K_GE_2"][size] for size in external_row_sizes
    )
    phased_as_orbit_sizes = tuple(
        PHASE_COUNT * size for size in external_row_sizes
    )

    # Burnside cross-check of the orbit count: fixed sets under rotation j
    # are the independent sets of C_gcd(j,n), counted by the Lucas numbers.
    burnside_total = sum(lucas(gcd(j, n)) for j in range(1, n + 1))
    burnside_orbits = burnside_total // n

    result = {
        "certificate": "C_COMPOSITE_TABLE",
        "finding": "COMPOSITE_TABLE_BUILT_EXTERNAL_SCOPE_REFUTED",
        "n": n,
        "unphased_census": key_str(brute),
        "unphased_matches_general_law": brute == closed,
        "phased_census": key_str(phased),
        "orbit_count_total": len(orbits),
        "native_spectra": {
            name: key_str(spectrum) for name, spectrum in native.items()
        },
        "native_spectrum_element_totals": native_elements,
        "phased_orbit_multiplicities": {
            name: key_str(spectrum)
            for name, spectrum in phased_spectrum.items()
        },
        "non_free_orbits": tuple(
            {
                "representative": row["representative"],
                "k": row["k"],
                "orbit_size": row["orbit_size"],
                "stabilizer_order": row["stabilizer_order"],
            }
            for row in orbits if row["orbit_size"] < n
        ),
        "external_unphased_spectrum": key_str(EXTERNAL_UNPHASED_SPECTRUM),
        "external_declared_scope": EXTERNAL_DECLARED_SCOPE,
        "external_declared_scope_native_spectrum":
            key_str(native[EXTERNAL_DECLARED_SCOPE]),
        "external_declared_scope_matches": declared_scope_matches,
        "external_scope_refuted": not declared_scope_matches,
        "external_spectrum_matching_scopes": matching_scopes,
        "external_spectrum_correct_under_scope":
            matching_scopes == ("K_GE_2",),
        "external_phased_row": EXTERNAL_PHASED_ROW,
        "phased_row_as_multiplicities": phased_as_multiplicities,
        "phased_row_as_orbit_sizes": phased_as_orbit_sizes,
        "external_phased_row_is_multiplicities":
            phased_as_multiplicities == EXTERNAL_PHASED_ROW,
        "external_phased_row_is_orbit_sizes":
            phased_as_orbit_sizes == EXTERNAL_PHASED_ROW,
        "burnside_fixed_point_total": burnside_total,
        "burnside_orbit_count": burnside_orbits,
        "burnside_agrees_with_enumeration": burnside_orbits == len(orbits),
        "verdict": (
            "external numbers are the K_GE_2 spectrum (all placements with "
            "k >= 2), NOT the k = 2 spectrum the brief labels them with; the "
            "native k = 2 spectrum is {6:1, 12:4} on 54 placements.  The "
            "phased row 4/4/4/8/96 is correct read as orbit MULTIPLICITIES "
            "(x4 free phase label), and false read as orbit sizes."
        ),
    }
    result["pass"] = (
        result["unphased_matches_general_law"]
        and result["burnside_agrees_with_enumeration"]
        and result["external_spectrum_correct_under_scope"]
        and result["external_scope_refuted"]
        and result["external_phased_row_is_multiplicities"]
        and not result["external_phased_row_is_orbit_sizes"]
    )
    return result


# ---------------------------------------------------------------------------
# Certificate D: the selection no-go at composite n
# ---------------------------------------------------------------------------


def invariant_placement_count(n: int, g: int) -> int:
    """Independent sets of C_n invariant under the subgroup <g>."""
    return lucas(g)


def exact_stabilizer_counts(n: int) -> dict[int, int]:
    """Elements whose stabilizer is exactly <g>, indexed by orbit size g."""
    return {
        g: sum(
            mobius(g // h) * invariant_placement_count(n, h)
            for h in divisors_of(g)
        )
        for g in divisors_of(n)
    }


def certificate_d_selection_scope() -> dict[str, object]:
    n = COMPOSITE_N
    orbits = orbit_table(n)
    nonempty = tuple(row for row in orbits if row["k"] >= 1)
    min_orbit_size = min(int(row["orbit_size"]) for row in nonempty)
    minimisers = tuple(
        row["representative"] for row in nonempty
        if int(row["orbit_size"]) == min_orbit_size
    )

    # Möbius/Lucas route to the same spectrum, and the spf law at scale.
    spf_rows = []
    spf_ok = True
    for m in range(3, EXTENDED_N_MAX + 1):
        exact = exact_stabilizer_counts(m)
        # g = 1 is the fully invariant class: only the empty placement.
        predicted_min = min(
            g for g, count in exact.items() if g > 1 and count > 0
        )
        spf = smallest_prime_factor(m)
        row_ok = predicted_min == spf and exact[1] == 1
        spf_ok = spf_ok and row_ok
        spf_rows.append({"n": m, "min_nonempty_orbit": predicted_min,
                         "spf": spf, "ok": row_ok})

    brute_spf_ok = True
    brute_spf_rows = []
    for m in range(3, BRUTE_N_MAX + 1):
        table = orbit_table(m)
        sizes = [int(row["orbit_size"]) for row in table if row["k"] >= 1]
        row_ok = min(sizes) == smallest_prime_factor(m)
        brute_spf_ok = brute_spf_ok and row_ok
        brute_spf_rows.append((m, min(sizes), smallest_prime_factor(m)))

    exact_12 = exact_stabilizer_counts(n)
    mobius_spectrum = {
        g: count // g for g, count in exact_12.items() if count
    }
    enumerated_spectrum = spectrum_for(orbits, lambda row: True)
    enumerated_spectrum = {
        int(size): int(count) for size, count in enumerated_spectrum.items()
    }

    prime_case = orbit_table(LANDED_CYCLE857_N)
    prime_sizes = {
        int(row["orbit_size"]) for row in prime_case if row["k"] >= 1
    }

    lemma = (
        "STABILIZER_LEMMA :: S subset Z_n is fixed by <g> iff S is a union "
        "of <g>-cosets, i.e. S = {y : y mod g in T} for some T subset Z_g; "
        "S is cyclically independent iff T is cyclically independent in "
        "C_g.  A nonempty independent S therefore forces g >= 2, so the "
        "largest possible stabilizer order is n/spf(n) and the SMALLEST "
        "possible orbit is spf(n), realised by the coset S = {0, spf(n), "
        "2 spf(n), ...} and its rotations."
    )
    consequence = (
        "SELECTION_SCOPE :: a C_n-covariant selection is a nonempty "
        "C_n-invariant set of placements, so its size is a sum of orbit "
        "sizes and its minimum is spf(n).  At prime n every nonempty orbit "
        "is free of size n -- that is the landed free-C_11 no-go, and it "
        "rides primality exactly here.  At n = 12 the floor drops to 2, "
        "realised by {evens, odds}.  Size 1 remains impossible for every "
        "n >= 3: the only C_n-fixed subsets are the empty set and Z_n, and "
        "Z_n is not independent, so no canonical single placement exists at "
        "any n.  Under the full C_n x Z_4 phase symmetry the free phase "
        "factor multiplies the floor to 4 * spf(n) = 8 at n = 12 and 44 at "
        "n = 11."
    )

    result = {
        "certificate": "D_SELECTION_SCOPE",
        "finding": "NOGO_SCOPE_PRICED_SPF_FLOOR",
        "lemma": lemma,
        "consequence": consequence,
        "n": n,
        "min_nonempty_orbit_size_n12": min_orbit_size,
        "min_orbit_realisers_n12": minimisers,
        "smallest_covariant_selection_rotation_only": min_orbit_size,
        "smallest_covariant_selection_with_phase":
            PHASE_COUNT * min_orbit_size,
        "single_placement_selection_possible": False,
        "stabilised_placements_n12": tuple(
            {
                "representative": row["representative"],
                "k": row["k"],
                "stabilizer_order": row["stabilizer_order"],
                "orbit_size": row["orbit_size"],
            }
            for row in orbits if row["stabilizer_order"] > 1 and row["k"] >= 1
        ),
        "mobius_spectrum_n12": key_str(mobius_spectrum),
        "enumerated_spectrum_n12": key_str(enumerated_spectrum),
        "mobius_agrees_with_enumeration":
            mobius_spectrum == enumerated_spectrum,
        "spf_law_extended_range": (3, EXTENDED_N_MAX),
        "spf_law_holds_extended": spf_ok,
        "spf_law_brute_range": (3, BRUTE_N_MAX),
        "spf_law_holds_brute": brute_spf_ok,
        "spf_brute_rows": tuple(brute_spf_rows),
        "prime_n11_orbit_sizes": tuple(sorted(prime_sizes)),
        "prime_n11_all_orbits_free": prime_sizes == {LANDED_CYCLE857_N},
        "n12_free_orbit_premise_fails": min_orbit_size < n,
    }
    result["pass"] = (
        result["mobius_agrees_with_enumeration"]
        and result["spf_law_holds_extended"]
        and result["spf_law_holds_brute"]
        and result["prime_n11_all_orbits_free"]
        and result["n12_free_orbit_premise_fails"]
        and result["min_nonempty_orbit_size_n12"]
        == smallest_prime_factor(n)
    )
    return result


# ---------------------------------------------------------------------------
# Certificate E: controls (integrity gates + falsification probes)
# ---------------------------------------------------------------------------


def falsification_probes() -> dict[str, object]:
    """Mutants that MUST be refuted by the derived tables."""
    n11 = brute_profile(LANDED_CYCLE857_N)
    n12_orbits = orbit_table(COMPOSITE_N)

    mutant_binomial = {
        k: PHASE_COUNT * LANDED_CYCLE857_N * comb(11 - k, k - 1) // k
        for k in range(1, 6)
        if (PHASE_COUNT * LANDED_CYCLE857_N * comb(11 - k, k - 1)) % k == 0
    }
    mutant_no_label_division = {
        k: PHASE_COUNT * LANDED_CYCLE857_N * comb(10 - k, k - 1)
        for k in range(1, 6)
    }
    mutant_phase_power = {
        k: PHASE_COUNT**k * n11[k] for k in range(1, 6)
    }
    landed = LANDED_CYCLE857_PHASED
    k2_spectrum = spectrum_for(n12_orbits, lambda row: row["k"] == 2)
    n11_orbit_sizes = {
        int(row["orbit_size"]) for row in orbit_table(LANDED_CYCLE857_N)
        if row["k"] >= 1
    }
    n12_min_orbit = min(
        int(row["orbit_size"]) for row in n12_orbits if row["k"] >= 1
    )

    probes = {
        "NC1_shifted_binomial_law": mutant_binomial != landed,
        "NC2_law_without_label_division": mutant_no_label_division != landed,
        "NC3_phase_factor_4_to_the_k": mutant_phase_power != landed,
        "NC4_external_spectrum_is_k_eq_2":
            k2_spectrum != EXTERNAL_UNPHASED_SPECTRUM,
        "NC5_n12_admits_single_placement_selection": n12_min_orbit != 1,
        "NC6_n11_has_a_stabilised_placement":
            n11_orbit_sizes == {LANDED_CYCLE857_N},
        "NC7_kaplansky_equals_plain_binomial": any(
            kaplansky_closed_form(12, k) != comb(12, k) for k in (2, 3, 4)
        ),
    }
    return {
        "probes": probes,
        "mutant_k2_spectrum": key_str(k2_spectrum),
        "all_refuted": all(probes.values()),
    }


def certificate_e_controls(
    fingerprint_first: str,
    fingerprint_repeat: str,
    self_payload_before: bytes,
    self_payload_after: bytes,
    runtime_seconds: float,
) -> dict[str, object]:
    self_tree = ast.parse(self_payload_before, filename=Path(SELF_PATH).name)
    imported = {
        alias.name
        for node in ast.walk(self_tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    }
    imported.update(
        node.module
        for node in ast.walk(self_tree)
        if isinstance(node, ast.ImportFrom) and node.module
    )
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
    probes = falsification_probes()

    result = {
        "certificate": "E_CONTROLS",
        "finding": "CONTROLS_CLEAN",
        "declared_input_paths": DECLARED_INPUT_PATHS,
        "literal_declared_input_paths":
            literal_assignment(self_tree, "DECLARED_INPUT_PATHS") == list(
                DECLARED_INPUT_PATHS
            )
            or literal_assignment(self_tree, "DECLARED_INPUT_PATHS")
            == DECLARED_INPUT_PATHS,
        "self_contained_no_repo_inputs": DECLARED_INPUT_PATHS == (),
        "literal_phase_count":
            literal_assignment(self_tree, "PHASE_COUNT") == PHASE_COUNT,
        "literal_external_spectrum":
            literal_assignment(self_tree, "EXTERNAL_UNPHASED_SPECTRUM")
            == EXTERNAL_UNPHASED_SPECTRUM,
        "literal_external_phased_row":
            literal_assignment(self_tree, "EXTERNAL_PHASED_ROW")
            == list(EXTERNAL_PHASED_ROW)
            or literal_assignment(self_tree, "EXTERNAL_PHASED_ROW")
            == EXTERNAL_PHASED_ROW,
        "literal_landed_row":
            literal_assignment(self_tree, "LANDED_CYCLE857_PHASED")
            == LANDED_CYCLE857_PHASED,
        "self_sha256": sha256(self_payload_before).hexdigest(),
        "self_git_blob": git_blob_sha(self_payload_before),
        "self_unchanged_by_run": self_payload_before == self_payload_after,
        "no_write_calls_in_source": not write_calls,
        "write_calls_found": write_calls,
        "blocked_runner_import_hits": tuple(RUNNER_BLOCKER.hits),
        "foreign_runner_modules_loaded": tuple(sorted(
            name for name in sys.modules
            if name.split(".")[-1].startswith(BLOCKLISTED_MODULE_PREFIXES)
            and name.split(".")[-1] != Path(SELF_PATH).stem
        )),
        "imported_modules": tuple(sorted(imported)),
        "sympy_version": sp.__version__,
        "running_branch": git_text("rev-parse", "--abbrev-ref", "HEAD"),
        "expected_branch": EXPECTED_BRANCH,
        "execution_head_sha": git_text("rev-parse", "HEAD"),
        "determinism_replay": fingerprint_first == fingerprint_repeat,
        "falsification_probes": probes["probes"],
        "mutant_k2_spectrum": probes["mutant_k2_spectrum"],
        "all_falsification_probes_refuted": probes["all_refuted"],
        "runtime_seconds": round(runtime_seconds, 6),
        "runtime_limit_seconds": AUDIT_TIMEOUT_SEC,
        "stdout_bytes": 0,
        "stdout_limit_bytes": STDOUT_LIMIT_BYTES,
        "stdout_within_limit": False,
    }
    result["pass"] = (
        result["literal_declared_input_paths"]
        and result["self_contained_no_repo_inputs"]
        and result["literal_phase_count"]
        and result["literal_external_spectrum"]
        and result["literal_external_phased_row"]
        and result["literal_landed_row"]
        and result["self_unchanged_by_run"]
        and result["no_write_calls_in_source"]
        and not result["blocked_runner_import_hits"]
        and not result["foreign_runner_modules_loaded"]
        and result["running_branch"] == EXPECTED_BRANCH
        and result["determinism_replay"]
        and result["all_falsification_probes_refuted"]
        and runtime_seconds < AUDIT_TIMEOUT_SEC
    )
    return result


# ---------------------------------------------------------------------------
# Assembly
# ---------------------------------------------------------------------------


def build_tables() -> dict[str, object]:
    return {
        "A_GENERAL_LAW": certificate_a_general_law(),
        "B_N11_REPRODUCTION": certificate_b_n11(),
        "C_COMPOSITE_TABLE": certificate_c_composite(),
        "D_SELECTION_SCOPE": certificate_d_selection_scope(),
    }


def fingerprint(tables: dict[str, object]) -> str:
    return digest({
        label: compact(certificate)
        for label, certificate in tables.items()
    })


def render(
    tables: dict[str, object],
    controls: dict[str, object],
) -> str:
    law = tables["A_GENERAL_LAW"]
    composite = tables["C_COMPOSITE_TABLE"]
    scope = tables["D_SELECTION_SCOPE"]
    lines = [
        "CYCLE870_GENERAL_N_CENSUS_LAW",
        "SCOPE :: general-n census law + composite-ring (n=12) test; "
        "self-contained derivation, no repo inputs",
        "THEOREM :: " + str(law["theorem"]),
    ]
    for step in law["proof_steps"]:
        lines.append("PROOF_STEP :: " + str(step))
    lines.append("LEMMA :: " + str(scope["lemma"]))
    lines.append("COROLLARY :: " + str(scope["consequence"]))
    for label in ("A_GENERAL_LAW", "B_N11_REPRODUCTION",
                  "C_COMPOSITE_TABLE", "D_SELECTION_SCOPE"):
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
    lines.append("COMPARATOR_VERDICT :: " + str(composite["verdict"]))
    lines.append("FINAL :: " + compact({
        "general_law": law["theorem"],
        "n11_phased_census": tables["B_N11_REPRODUCTION"]["phased_census"],
        "n11_quoted_subrow_reproduced":
            tables["B_N11_REPRODUCTION"]["quoted_subrow_reproduced"],
        "n12_phased_census": composite["phased_census"],
        "n12_native_spectra": composite["native_spectra"],
        "external_spectrum_matching_scopes":
            composite["external_spectrum_matching_scopes"],
        "external_declared_scope_matches":
            composite["external_declared_scope_matches"],
        "external_phased_row_is_multiplicities":
            composite["external_phased_row_is_multiplicities"],
        "min_covariant_selection_n12":
            scope["smallest_covariant_selection_rotation_only"],
        "min_covariant_selection_n12_with_phase":
            scope["smallest_covariant_selection_with_phase"],
        "selection_floor_law": "min covariant selection size = spf(n)",
        "runtime_seconds": controls["runtime_seconds"],
        "pass": all(value["pass"] for value in tables.values())
            and controls["pass"],
    }))
    lines.append(
        "CYCLE870_GENERAL_N_CENSUS_LAW_PASS"
        if all(value["pass"] for value in tables.values()) and controls["pass"]
        else "CYCLE870_GENERAL_N_CENSUS_LAW_FAIL"
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    started = monotonic()
    self_payload_before = Path(__file__).read_bytes()
    tables = build_tables()
    repeat = build_tables()
    self_payload_after = Path(__file__).read_bytes()
    runtime_seconds = monotonic() - started
    controls = certificate_e_controls(
        fingerprint(tables),
        fingerprint(repeat),
        self_payload_before,
        self_payload_after,
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
