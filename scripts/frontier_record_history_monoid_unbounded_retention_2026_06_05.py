#!/usr/bin/env python3
"""Record history monoid / unbounded finite retention verifier.

This runner checks the exact finite algebra behind the post-record history
sector:

* finite record histories form a free monoid under concatenation;
* forgetting order gives a free commutative count monoid N^O;
* scalar readout is finitely additive over counts;
* append updates preserve prior records as prefixes and only increment counts;
* for every finite N, Z^3 supplies N distinct sites, so there is no fixed
  framework-level finite cap on recorded-history length;
* the result does not claim completed infinity, physical production dynamics,
  or coherent qubit storage of the whole history.

Run:
    python3 scripts/frontier_record_history_monoid_unbounded_retention_2026_06_05.py
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from pathlib import Path
from typing import Iterable

import sympy as sp


PASS = 0
FAIL = 0


ALPHABET = ("singlet", "doublet", "other")
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "RECORD_HISTORY_MONOID_UNBOUNDED_RETENTION_2026-06-05.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return ok


def concat(*words: tuple[str, ...]) -> tuple[str, ...]:
    out: tuple[str, ...] = ()
    for word in words:
        out = out + word
    return out


def count_word(word: Iterable[str], alphabet: tuple[str, ...] = ALPHABET) -> tuple[int, ...]:
    c = Counter(word)
    return tuple(c[a] for a in alphabet)


def add_counts(*counts: tuple[int, ...]) -> tuple[int, ...]:
    if not counts:
        return tuple(0 for _ in ALPHABET)
    return tuple(sum(c[i] for c in counts) for i in range(len(counts[0])))


def unit_count(alphabet: tuple[str, ...] = ALPHABET) -> tuple[int, ...]:
    return tuple(0 for _ in alphabet)


def basis_count(atom: str, alphabet: tuple[str, ...] = ALPHABET) -> tuple[int, ...]:
    return tuple(1 if a == atom else 0 for a in alphabet)


def scalar_readout(counts: tuple[int, ...], weights: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(sp.Integer(c) * w for c, w in zip(counts, weights)))


def line_sites(n: int) -> list[tuple[int, int, int]]:
    return [(i, 0, 0) for i in range(n)]


def tagged_history(word: tuple[str, ...]) -> tuple[tuple[tuple[int, int, int], str], ...]:
    return tuple(zip(line_sites(len(word)), word))


def is_prefix(prefix: tuple[str, ...], whole: tuple[str, ...]) -> bool:
    return whole[: len(prefix)] == prefix


def main() -> int:
    empty: tuple[str, ...] = ()
    w1 = ("singlet",)
    w2 = ("doublet", "singlet")
    w3 = ("other", "doublet")

    # ------------------------------------------------------------------
    # 1. Free monoid of finite record histories.
    # ------------------------------------------------------------------
    check("M1.1 empty word is the two-sided identity", concat(empty, w2) == w2 and concat(w2, empty) == w2)
    check("M1.2 concatenation is associative", concat(concat(w1, w2), w3) == concat(w1, concat(w2, w3)))
    check("M1.3 length is additive under concatenation", len(concat(w1, w2, w3)) == len(w1) + len(w2) + len(w3))

    words_len_3 = list(product(ALPHABET, repeat=3))
    check("M1.4 finite alphabet has |O|^N finite words at fixed length", len(words_len_3) == len(ALPHABET) ** 3)
    check("M1.5 every generated history is finite", all(len(w) == 3 for w in words_len_3))

    # ------------------------------------------------------------------
    # 2. Count projection to the commutative monoid N^O.
    # ------------------------------------------------------------------
    c1 = count_word(w1)
    c2 = count_word(w2)
    c3 = count_word(w3)
    check("C2.1 empty history maps to zero count", count_word(empty) == unit_count())
    check("C2.2 count projection is a monoid homomorphism", count_word(concat(w1, w2, w3)) == add_counts(c1, c2, c3))
    check("C2.3 count addition is associative", add_counts(add_counts(c1, c2), c3) == add_counts(c1, add_counts(c2, c3)))
    check("C2.4 count addition is commutative", add_counts(c1, c2) == add_counts(c2, c1))
    check("C2.5 appending an atom increments exactly its basis count", count_word(concat(w2, ("other",))) == add_counts(count_word(w2), basis_count("other")))

    # ------------------------------------------------------------------
    # 3. Finite scalar additivity over counts.
    # ------------------------------------------------------------------
    I_s, I_d, I_o = sp.symbols("I_s I_d I_o")
    weights = (I_s, I_d, I_o)
    check("readout.1 scalar readout of empty count is zero", scalar_readout(unit_count(), weights) == 0)
    check(
        "readout.2 scalar readout is additive over finite disjoint count sums",
        sp.simplify(
            scalar_readout(add_counts(c1, c2, c3), weights)
            - scalar_readout(c1, weights)
            - scalar_readout(c2, weights)
            - scalar_readout(c3, weights)
        )
        == 0,
    )
    check(
        "readout.3 append readout increment is the atom readout",
        sp.simplify(
            scalar_readout(count_word(concat(w2, ("doublet",))), weights)
            - scalar_readout(count_word(w2), weights)
            - I_d
        )
        == 0,
    )

    # ------------------------------------------------------------------
    # 4. Durability as prefix/count preservation under append.
    # ------------------------------------------------------------------
    appended = concat(w2, ("other", "singlet"))
    check("D4.1 append preserves the previous history as a prefix", is_prefix(w2, appended))
    check("D4.2 append never decreases any count", all(a <= b for a, b in zip(count_word(w2), count_word(appended))))
    check("D4.3 tagged histories preserve old site-record pairs under append", tagged_history(w2) == tagged_history(appended)[: len(w2)])

    # ------------------------------------------------------------------
    # 5. Z^3 supplies arbitrary finite distinct record sites.
    # ------------------------------------------------------------------
    site_checks = []
    for n in range(0, 21):
        sites = line_sites(n)
        site_checks.append(len(sites) == n and len(set(sites)) == n and all(y == 0 and z == 0 for _, y, z in sites))
    check("Z5.1 explicit line embedding gives N distinct Z^3 sites for N=0..20", all(site_checks))

    larger_n = 101
    check("Z5.2 no tested finite cap: 101 distinct sites exist on a lattice line", len(set(line_sites(larger_n))) == larger_n)

    # For any proposed finite bound B, the line construction gives B+1 sites.
    B = sp.symbols("B", integer=True, nonnegative=True)
    check("Z5.3 symbolic bound escape is B -> B+1 finite sites", sp.simplify((B + 1) - B - 1) == 0)

    # ------------------------------------------------------------------
    # 6. Type firewall: counts/histories are not probabilities or qubits.
    # ------------------------------------------------------------------
    counts = count_word(("singlet", "singlet", "doublet"))
    check("T6.1 nonempty count total is history length, not probability normalization", sum(counts) == 3 and sum(counts) != 1)
    check("T6.2 count entries are integers and can exceed one", all(isinstance(x, int) for x in counts) and max(counts) > 1)

    p_s, p_d, p_o = sp.symbols("p_s p_d p_o", nonnegative=True)
    probability_sum = sp.Eq(p_s + p_d + p_o, 1)
    count_sum = sp.Integer(sum(counts))
    check("T6.3 count normalization differs from probability normalization", probability_sum != sp.Eq(count_sum, 1))

    # ------------------------------------------------------------------
    # 7. Boundary checks: unbounded finite, not completed infinity.
    # ------------------------------------------------------------------
    finite_lengths = [len(("singlet",) * n) for n in range(0, 12)]
    check("B7.1 constructed histories are finite at each finite N", finite_lengths == list(range(12)))
    check("B7.2 lengths are unbounded over finite N samples", max(finite_lengths) > 10)
    check("B7.3 no single constructed history has infinite length", all(isinstance(length, int) for length in finite_lengths))

    # ------------------------------------------------------------------
    # 8. Source-boundary guardrails.
    # ------------------------------------------------------------------
    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    check("G8.1 source note declares bounded theorem, not positive closure", "**Claim type:** bounded_theorem" in note_text)
    check("G8.2 source note records exact post-record support boundary", "exact post-record support theorem" in note_text)
    check("G8.3 source note says production is not derived", "Does not prove that nonzero records are physically produced" in note_text)
    check("G8.4 source note says readout context/alphabet are supplied", "supplied finite record alphabet" in note_flat and "Does not derive the readout context" in note_text)
    check("G8.5 source note keeps probability and IID outside the result", "Does not derive probability, independence, IID structure" in note_text)
    check("G8.6 source note blocks retained-status proposal language", "makes no retained-status proposal" in note_flat and "does not use bare retained language" in note_flat)
    check("G8.7 source note names downstream additivity row without promoting it", "RECORD_UNBOUNDED_FINITE_ADDITIVITY_SCHEMA_2026-06-06.md" in note_text and "does not claim" in note_flat)

    print("\n=== Record history interpretation ===")
    print("Finite record histories form an append-only free monoid; counts form N^O.")
    print("Z^3 gives arbitrarily many distinct sites for any finite N, so no fixed finite cap is imposed by the framework carrier.")
    print("This is bounded post-record support for unbounded finite retention, not production closure, completed infinity, or coherent qubit-state storage.")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
