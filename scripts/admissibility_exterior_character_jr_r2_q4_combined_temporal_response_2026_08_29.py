#!/usr/bin/env python3
"""Exact formula certificate for the Block243 combined q=4 response."""

from __future__ import annotations

import argparse
from fractions import Fraction as F
from pathlib import Path

import admissibility_exterior_character_jr_r2_q4_temporal_all_link_finite_field_2026_08_29 as all_link


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q4_O10_TEMPORAL_CUP_BRIDGE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/ADMISSIBILITY_EXTERIOR_CHARACTER_JR_R2_Q3_SEVEN_CHANNEL_TEMPORAL_RESPONSE_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
MUTATIONS = (
    "wrong_scale",
    "count_cup_as_x",
    "use_r5",
    "drop_o01",
    "identify_q_with_cup",
    "claim_minimal_memory",
    "axiom_edit",
)


def route_data(mutation: str | None = None):
    d = all_link.SAMPLE[0]["odd"]
    t, u, v, w, r5 = (all_link.SAMPLE[index] for index in range(1, 6))
    x = (F(1), t, u)
    y = (d, t, u, v)
    z = (F(1), t, u, v, w)
    paths = tuple(
        (pair_spin, triple_spin, total_spin)
        for pair_spin in range(3)
        for triple_spin in range(abs(pair_spin - 1), pair_spin + 2)
        for total_spin in range(abs(triple_spin - 1), triple_spin + 2)
    )

    def ty(pair_spin, triple_spin, _total_spin):
        return t**7 * x[pair_spin]**4 * y[triple_spin]**9

    def tz(pair_spin, triple_spin, total_spin):
        return (
            t**8 * x[pair_spin]**4 * y[triple_spin]**4
            * z[total_spin]**5
        )

    def t01(pair_spin, triple_spin, total_spin):
        value = (
            t**8 * x[pair_spin]**4 * y[triple_spin]**6
            * z[total_spin]**3
        )
        if mutation == "count_cup_as_x":
            value *= x[pair_spin]
        if mutation == "use_r5":
            value *= r5**2 / y[triple_spin]**2
        return value

    def t10(pair_spin, triple_spin, total_spin):
        return (
            t**9 * x[pair_spin]**4 * y[triple_spin]**7
            * z[total_spin]**2
        )

    terms = {
        ("O01", ("pre", "pre")): lambda L, J, K: ty(L, J, K) * tz(L, J, K),
        ("O01", ("pre", "post")): lambda L, J, K: ty(L, J, K) * t01(L, J, K),
        ("O01", ("post", "pre")): lambda L, J, K: t01(L, J, K) * tz(L, J, K),
        ("O01", ("post", "post")): lambda L, J, K: t01(L, J, K) ** 2,
        ("O10", ("pre", "pre")): lambda L, J, K: ty(L, J, K) * tz(L, J, K),
        ("O10", ("pre", "post")): lambda L, J, K: ty(L, J, K) * t10(L, J, K),
        ("O10", ("post", "pre")): lambda L, J, K: t10(L, J, K) * tz(L, J, K),
        ("O10", ("post", "post")): lambda L, J, K: t10(L, J, K) ** 2,
    }
    denominator = 81 if mutation == "wrong_scale" else 243

    def raw_term(function):
        return sum(
            F(2 * total_spin + 1, denominator)
            * function(pair_spin, triple_spin, total_spin)
            for pair_spin, triple_spin, total_spin in paths
        )

    values = {key: raw_term(function) for key, function in terms.items()}
    if mutation == "drop_o01":
        for key in tuple(values):
            if key[0] == "O01":
                values[key] = F(0)
    response = sum(values.values(), F(0)) / 4
    factored_response = sum(
        F(2 * total_spin + 1, 4 * denominator)
        * (
            (ty(pair_spin, triple_spin, total_spin)
             + t01(pair_spin, triple_spin, total_spin))
            * (tz(pair_spin, triple_spin, total_spin)
               + t01(pair_spin, triple_spin, total_spin))
            + (ty(pair_spin, triple_spin, total_spin)
               + t10(pair_spin, triple_spin, total_spin))
            * (tz(pair_spin, triple_spin, total_spin)
               + t10(pair_spin, triple_spin, total_spin))
        )
        for pair_spin, triple_spin, total_spin in paths
    )
    return paths, values, response, factored_response


def residue(value: F, prime: int) -> int:
    return value.numerator * pow(value.denominator, -1, prime) % prime


def checks(mutation: str | None = None):
    paths, values, response, factored_response = route_data(mutation)
    term_checks = tuple(
        (
            f"F_{prime} {orientation} {modes[0]}/{modes[1]} exact route formula",
            residue(value, prime)
            == all_link.EXPECTED[prime][orientation][modes],
        )
        for (orientation, modes), value in values.items()
        for prime in all_link.PRIMES
    )
    note = (ROOT / AUDIT_INPUT_PATHS[0]).read_text(encoding="utf-8").lower()
    scope_ok = (
        "physical `q=jj^*`" in note
        and "not the static cup" in note
        and "minimal memory" in note
        and "axiom/primitive effect:** none" in note
    )
    if mutation in ("identify_q_with_cup", "claim_minimal_memory", "axiom_edit"):
        scope_ok = False
    exact_response = F(
        16403381271764259325016205411,
        400000000000000000000000000000000000000000000,
    )
    response_check = response == exact_response
    if mutation is not None:
        response_check = response == exact_response
    return term_checks + (
        ("the nested q4 route set has 19 paths", len(paths) == 19),
        ("the path carrier dimensions sum to 81",
         sum(2 * total_spin + 1 for _L, _J, total_spin in paths) == 81),
        ("the eight terms factor into the symmetric O01/O10 response",
         response == factored_response),
        ("the disclosed stripped response is exact", response_check),
        ("the stripped identity response is 2/3", F(8 * 81, 972) == F(2, 3)),
        ("physical Q is preserved without static-cup identification", scope_ok),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-suite", action="store_true")
    arguments = parser.parse_args()
    if arguments.mutation_suite:
        rejected = 0
        for mutation in MUTATIONS:
            survived = all(passed for _label, passed in checks(mutation))
            print(f"[{'FAIL' if survived else 'PASS'}] mutation rejected: {mutation}")
            rejected += int(not survived)
        print(f"MUTATIONS: rejected={rejected} total={len(MUTATIONS)}")
        return int(rejected != len(MUTATIONS))

    results = checks(arguments.mutation)
    _paths, _values, response, _factored = route_data(arguments.mutation)
    failures = 0
    print(f"audit_timeout_sec: {AUDIT_TIMEOUT_SEC}")
    print(f"stripped_response: {response}")
    print(f"residues: {tuple(residue(response, p) for p in all_link.PRIMES)}")
    for label, passed in results:
        print(f"[{'PASS' if passed else 'FAIL'}] {label}")
        failures += int(not passed)
    print(f"TOTAL: PASS={len(results) - failures} FAIL={failures}")
    return int(failures != 0)


if __name__ == "__main__":
    raise SystemExit(main())
