#!/usr/bin/env python3
"""Check released rational witnesses against an independent sector-Gram Q.

No root Python source is imported or executed. Root discovery is not rerun.
The witness coefficients are inputs; integer-scaled polynomial identities,
all sign ranks, and the matrix itself are independently checked.
"""
from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import math
import time


ROOT = Path(__file__).resolve().parent
ZERO = (0, 0, 0, 0, 0)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(name, value):
    path = ROOT / name
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    return digest(path)


def recheck_inputs():
    manifest = json.loads((ROOT / "POST_INPUTS.json").read_text())
    assert digest(ROOT / "PRE_SEAL.json") == manifest["pre_seal_sha256"]
    for name, expected in json.loads((ROOT / "PRE_SEAL.json").read_text())["files"].items():
        assert digest(ROOT / name) == expected, name
    for entry in manifest["sources"]:
        assert digest(entry["snapshot"]) == entry["sha256"], entry["snapshot"]
    return manifest


def independently_build_Q():
    # Enumerate charge words in a different state space, then apply the
    # specified occupied-set/negative-position ordering only for comparison.
    even = tuple(v for v in range(8) if v.bit_count() % 2 == 0)
    odd = tuple(v for v in range(8) if v.bit_count() % 2 == 1)
    edges = sorted((a, a ^ (1 << axis)) for a in even for axis in range(3))
    assert even == (0, 3, 5, 6) and odd == (1, 2, 4, 7)
    assert edges == [(0, 1), (0, 2), (0, 4), (3, 1), (3, 2), (3, 7),
                     (5, 1), (5, 4), (5, 7), (6, 2), (6, 4), (6, 7)]
    chords = (0, 5, 7, 8, 10)
    chord_number = {edge: k for k, edge in enumerate(chords)}
    words = [word for word in product((-1, 0, 1), repeat=8)
             if word.count(1) == 5 and word.count(-1) == 1 and word.count(0) == 2]
    words.sort(key=lambda word: (tuple(v for v in range(8) if word[v] != 0), word.index(-1)))
    sectors = {w: [word for word in words if sum(word[a] == 0 for a in even) == w]
               for w in range(3)}
    assert len(words) == 168 and [len(sectors[w]) for w in range(3)] == [36, 96, 36]
    indices = {w: {word: j for j, word in enumerate(sectors[w])} for w in range(3)}
    middle = sectors[1]
    dark = []
    bright = []
    for j, word in enumerate(middle):
        empty_a = next(a for a in even if word[a] == 0)
        empty_b = next(b for b in odd if word[b] == 0)
        (dark if empty_a ^ empty_b == 7 else bright).append(j)
    assert len(dark) == 24 and len(bright) == 72

    # Construct F from single outward transitions, never by paired dark paths.
    transition = {0: [], 1: []}
    for w in range(2):
        for source, word in enumerate(sectors[w]):
            for edge_number, (a, b) in enumerate(edges):
                if word[a] == 0 or word[b] != 0:
                    continue
                charge = word[a]
                destination = list(word)
                destination[a], destination[b] = 0, charge
                destination = tuple(destination)
                exponent = [0] * 5
                if edge_number in chord_number:
                    exponent[chord_number[edge_number]] = -charge
                target = indices[w + 1][destination]
                transition[w].append((target, source, tuple(exponent)))

    # G_11 = F_10 F_10* - F_21* F_21, using Laurent conjugation z^n -> z^-n.
    positive_columns = defaultdict(list)
    negative_rows = defaultdict(list)
    for target, source, exponent in transition[0]:
        positive_columns[source].append((target, exponent))
    for target, source, exponent in transition[1]:
        negative_rows[target].append((source, exponent))
    gram_difference = defaultdict(int)
    for column in positive_columns.values():
        for row, row_exponent in column:
            for col, col_exponent in column:
                exponent = tuple(a - b for a, b in zip(row_exponent, col_exponent))
                gram_difference[row, col, exponent] += 1
    for row_data in negative_rows.values():
        for row, row_exponent in row_data:
            for col, col_exponent in row_data:
                exponent = tuple(b - a for a, b in zip(row_exponent, col_exponent))
                gram_difference[row, col, exponent] -= 1
    gram_difference = {key: coefficient for key, coefficient in gram_difference.items() if coefficient}
    assert all(gram_difference.get((col, row, tuple(-x for x in exponent))) == coefficient
               for (row, col, exponent), coefficient in gram_difference.items())
    dark_set = set(dark)
    assert not any(row in dark_set and col in dark_set for row, col, exponent in gram_difference)
    bright_index = {middle_index: k for k, middle_index in enumerate(bright)}
    dark_index = {middle_index: k for k, middle_index in enumerate(dark)}
    q = {(bright_index[row], dark_index[col], exponent): coefficient
         for (row, col, exponent), coefficient in gram_difference.items()
         if row in bright_index and col in dark_index}
    rows = [[] for _ in range(72)]
    for (row, col, exponent), coefficient in sorted(q.items()):
        rows[row].append((col, exponent, coefficient))
    record = {
        "construction": "Single-hop outward F matrices, then F_10 F_10* minus F_21* F_21.",
        "charge_enumeration": "All ternary eight-site words filtered by populations; canonical order imposed afterwards.",
        "edges": edges, "chords": chords,
        "sector_dimensions": {str(w): len(sectors[w]) for w in range(3)},
        "outward_transition_counts": {str(w): len(transition[w]) for w in range(2)},
        "G_Laurent_Hermitian": True, "dark_dark_block_identically_zero": True,
        "dark_charge_words": [middle[j] for j in dark],
        "bright_charge_words": [middle[j] for j in bright],
        "Q_coefficient_count": len(q),
        "Q_coefficients": [[row, col, list(exponent), coefficient]
                           for (row, col, exponent), coefficient in sorted(q.items())],
    }
    return q, rows, record


def read_supplied_Q(data):
    result = defaultdict(int)
    assert len(data["rows"]) == 72
    for row, cells in enumerate(data["rows"]):
        for cell in cells:
            col = cell["column"]
            assert type(col) is int and 0 <= col < 24
            for term in cell["terms"]:
                exponent, coefficient = term["exponent"], term["coefficient"]
                assert len(exponent) == 5 and all(type(x) is int for x in exponent)
                assert type(coefficient) is int
                result[row, col, tuple(exponent)] += coefficient
    return {key: value for key, value in result.items() if value}


def combine_with_integer_denominator(certificate, shifts, rows, override_phase=None):
    combination = certificate["row_combination"]
    denominator = math.lcm(*(entry[2] for entry in combination))
    accumulated = defaultdict(int)
    total_absolute = 0
    for number, numerator, divisor in combination:
        weight = numerator * (denominator // divisor)
        total_absolute += abs(weight)
        shift = shifts[number // 72]
        for col, exponent, coefficient in rows[number % 72]:
            total_exponent = tuple(a + b for a, b in zip(shift, exponent))
            accumulated[col, total_exponent] += weight * coefficient
    phase = certificate["phase"] if override_phase is None else override_phase
    unit = tuple(int(j == phase) for j in range(5))
    accumulated[certificate["column"], unit] -= denominator
    accumulated[certificate["column"], tuple(-x for x in unit)] += denominator
    residual = {key: value for key, value in accumulated.items() if value}
    return residual, Fraction(total_absolute, denominator)


def verify_certificates(witness, rows):
    # Recreate and compare the entire multiplier set; do not trust row labels.
    shifts = sorted((e for e in product(range(-3, 4), repeat=5) if sum(abs(x) for x in e) <= 3),
                    key=lambda e: (sum(abs(x) for x in e), e))
    assert len(shifts) == 231 and [list(e) for e in shifts] == witness["shifts"]
    assert witness["degree"] == 3
    certificates = witness["certificates"]
    assert len(certificates) == 120
    assert {(c["phase"], c["column"]) for c in certificates} == set(product(range(5), range(24)))
    records = []
    for certificate in certificates:
        assert type(certificate["phase"]) is int and type(certificate["column"]) is int
        combination = certificate["row_combination"]
        assert combination and len({entry[0] for entry in combination}) == len(combination)
        for entry in combination:
            assert len(entry) == 3 and all(type(x) is int for x in entry)
            number, numerator, denominator = entry
            assert 0 <= number < 72 * len(shifts)
            assert numerator != 0 and denominator > 0 and math.gcd(numerator, denominator) == 1
        residual, total_absolute = combine_with_integer_denominator(certificate, shifts, rows)
        assert not residual, (certificate["phase"], certificate["column"], "nonzero exact Laurent residual")
        ceiling = math.ceil(total_absolute)
        assert total_absolute <= 68891
        records.append({"phase": certificate["phase"], "column": certificate["column"],
                        "combination_terms": len(combination), "residual_coefficient_count": len(residual),
                        "row_coefficient_L1": [total_absolute.numerator, total_absolute.denominator],
                        "row_coefficient_L1_ceiling": ceiling})
        if certificate["column"] == 23:
            print(json.dumps({"phase": certificate["phase"], "independent_exact_identities_verified": 24}), flush=True)
    first = certificates[0]
    altered = dict(first)
    altered["row_combination"] = [entry[:] for entry in first["row_combination"]]
    altered["row_combination"][0][1] += altered["row_combination"][0][2]
    altered_residual, _ = combine_with_integer_denominator(altered, shifts, rows)
    reversed_rows = [[(col, exponent, -coefficient) for col, exponent, coefficient in row] for row in rows]
    reversed_residual, _ = combine_with_integer_denominator(first, shifts, reversed_rows)
    missing_rows = [row[:] for row in rows]
    missing_rows[0] = missing_rows[0][1:]
    missing_residual, _ = combine_with_integer_denominator(first, shifts, missing_rows)
    wrong_target_residual, _ = combine_with_integer_denominator(first, shifts, rows, override_phase=1)
    mutations = {"one_witness_coefficient_changed": len(altered_residual),
                 "commutator_sign_reversed": len(reversed_residual),
                 "one_primitive_monomial_removed": len(missing_residual),
                 "target_phase_changed": len(wrong_target_residual)}
    assert all(count > 0 for count in mutations.values())
    return {"arithmetic": "Each rational witness scaled by its exact common denominator, then accumulated over integers.",
            "identities": records, "maximum_L1_ceiling": max(r["row_coefficient_L1_ceiling"] for r in records),
            "declared_uniform_L1_bound": 68891, "M_P": 120 * 68891**2,
            "mutation_residual_coefficient_counts": mutations}


def integer_determinant(matrix):
    # Independent fraction-free verification of each lower-rank witness minor.
    n = len(matrix)
    if n == 0:
        return 1
    work = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(n - 1):
        if work[k][k] == 0:
            target = next((i for i in range(k + 1, n) if work[i][k] != 0), None)
            if target is None:
                return 0
            work[k], work[target] = work[target], work[k]
            sign = -sign
        pivot = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                value = pivot * work[i][j] - work[i][k] * work[k][j]
                quotient, remainder = divmod(value, previous)
                assert remainder == 0, "Bareiss exact division failed"
                work[i][j] = quotient
            work[i][k] = 0
        previous = pivot
    return sign * work[-1][-1]


def exact_rank_certificate(matrix):
    work = [[Fraction(value) for value in row] for row in matrix]
    m, n = len(work), len(work[0])
    original_rows = list(range(m))
    pivot_columns = []
    rank = 0
    for column in range(n):
        eligible = [i for i in range(rank, m) if work[i][column]]
        if not eligible:
            continue
        selected = min(eligible, key=lambda i: (abs(work[i][column]), original_rows[i]))
        work[rank], work[selected] = work[selected], work[rank]
        original_rows[rank], original_rows[selected] = original_rows[selected], original_rows[rank]
        pivot = work[rank][column]
        for i in range(rank + 1, m):
            if work[i][column] == 0:
                continue
            scale = work[i][column] / pivot
            for j in range(column + 1, n):
                work[i][j] -= scale * work[rank][j]
            work[i][column] = Fraction(0)
        pivot_columns.append(column)
        rank += 1
    assert all(all(value == 0 for value in row) for row in work[rank:])
    free_columns = [j for j in range(n) if j not in pivot_columns]
    kernel = []
    for free in free_columns:
        vector = [Fraction(0) for _ in range(n)]
        vector[free] = Fraction(1)
        for i in range(rank - 1, -1, -1):
            pivot_column = pivot_columns[i]
            vector[pivot_column] = -sum((work[i][j] * vector[j] for j in range(pivot_column + 1, n)), Fraction(0)) / work[i][pivot_column]
        assert all(sum((a * b for a, b in zip(row, vector)), Fraction(0)) == 0 for row in matrix)
        assert [vector[j] for j in free_columns] == [Fraction(int(j == free)) for j in free_columns]
        kernel.append(vector)
    minor_rows = original_rows[:rank]
    minor = [[matrix[i][j] for j in pivot_columns] for i in minor_rows]
    determinant = integer_determinant(minor)
    assert determinant != 0
    assert len(kernel) == n - rank
    return {"rank": rank, "minor_rows": minor_rows, "minor_columns": pivot_columns,
            "integer_minor_determinant": determinant,
            "kernel_vectors": [[[v.numerator, v.denominator] for v in vector] for vector in kernel],
            "kernel_vectors_exactly_annihilated": True}


def all_sign_ranks(q):
    results = []
    for bits in product((0, 1), repeat=5):
        matrix = [[0 for _ in range(24)] for _ in range(72)]
        for (row, column, exponent), coefficient in q.items():
            parity = sum(b * e for b, e in zip(bits, exponent)) % 2
            matrix[row][column] += coefficient if parity == 0 else -coefficient
        certificate = exact_rank_certificate(matrix)
        certificate["pi_bits"] = list(bits)
        certificate["integer_matrix"] = matrix
        results.append(certificate)
    # Compare only after deriving all ranks and independently witnessing each.
    claimed = {"00000": 23, "00011": 23, "01101": 22, "01110": 23,
               "10100": 23, "10111": 22, "11001": 20, "11010": 22}
    computed = {"".join(map(str, row["pi_bits"])): row["rank"] for row in results if row["rank"] < 24}
    assert computed == claimed
    return {"method": "Rational echelon calculation; each rank then certified by a nonzero integer minor and exact independent kernel vectors.",
            "ranks": results, "rank_deficient_phases": computed}


def main():
    started = time.monotonic()
    manifest = recheck_inputs()
    print(json.dumps({"inputs_and_PRE_hashes_verified": True,
                      "released_source_hashes": {Path(x["snapshot"]).name: x["sha256"] for x in manifest["sources"]}}), flush=True)
    q, rows, primitive = independently_build_Q()
    supplied_data = json.loads((ROOT / "released_sources/INCIDENCE_PROBE.json").read_text())
    assert q == read_supplied_Q(supplied_data), "Independent primitive matrix differs from supplied incidence matrix"
    primitive["exact_match_to_supplied_primitive_coefficients"] = True
    primitive_hash = write_json("INDEPENDENT_PRIMITIVE_Q.json", primitive)
    print(json.dumps({"independent_primitive_Q_verified": True, "coefficient_count": len(q),
                      "sector_dimensions": primitive["sector_dimensions"],
                      "outward_transition_counts": primitive["outward_transition_counts"]}), flush=True)
    witness = json.loads((ROOT / "released_sources/MODULE_EXACT_CERTIFICATES_ALL.json").read_text())
    assert witness["source_sha256"] == digest(ROOT / "released_sources/INCIDENCE_PROBE.json")
    identity_results = verify_certificates(witness, rows)
    identities_hash = write_json("INDEPENDENT_IDENTITY_RESULTS.json", identity_results)
    rank_results = all_sign_ranks(q)
    ranks_hash = write_json("INDEPENDENT_SIGN_RANKS.json", rank_results)
    recheck_inputs()
    summary = {"independent_primitive_Q_verified": True,
               "exact_identity_count": len(identity_results["identities"]),
               "maximum_L1_ceiling": identity_results["maximum_L1_ceiling"],
               "M_P": identity_results["M_P"],
               "exact_sign_ranks_count": len(rank_results["ranks"]),
               "rank_deficient_phases": rank_results["rank_deficient_phases"],
               "mutation_residual_coefficient_counts": identity_results["mutation_residual_coefficient_counts"],
               "output_sha256": {"INDEPENDENT_PRIMITIVE_Q.json": primitive_hash,
                                 "INDEPENDENT_IDENTITY_RESULTS.json": identities_hash,
                                 "INDEPENDENT_SIGN_RANKS.json": ranks_hash},
               "independent_verifier_sha256": digest(Path(__file__)),
               "scope": "All identities and ranks verified against an independent exact primitive-hop reconstruction. No root builder imported, modular search rerun, publication runtime certified, or audit status applied."}
    write_json("POST_CHECK_RESULTS.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True), flush=True)
    print(json.dumps({"verification_elapsed_seconds": time.monotonic() - started}), flush=True)


if __name__ == "__main__":
    main()
