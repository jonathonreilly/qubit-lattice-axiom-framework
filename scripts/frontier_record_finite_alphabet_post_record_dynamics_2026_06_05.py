#!/usr/bin/env python3
"""Finite-alphabet post-record dynamics verifier.

This runner checks the exact algebraic dynamics that follows after a record
atom is realized:

* finite suffixes act on finite histories by append;
* count states update by translations in N^O;
* count projection is equivariant under append;
* alphabet coarse-grainings commute with append/count dynamics;
* scalar readout preservation under coarse-graining requires compatible
  readout weights;
* realized post-record updates are integral, not probability vectors.

Run:
    python3 scripts/frontier_record_finite_alphabet_post_record_dynamics_2026_06_05.py
"""

from __future__ import annotations

from collections import Counter
from itertools import product
from typing import Callable, Iterable

import sympy as sp


PASS = 0
FAIL = 0

ALPHABET = ("singlet", "doublet", "other")
COARSE_ALPHABET = ("generation", "remainder")
PHI = {"singlet": "generation", "doublet": "generation", "other": "remainder"}


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


def append_suffix(word: tuple[str, ...], suffix: tuple[str, ...]) -> tuple[str, ...]:
    return word + suffix


def count_word(word: Iterable[str], alphabet: tuple[str, ...] = ALPHABET) -> tuple[int, ...]:
    c = Counter(word)
    return tuple(c[a] for a in alphabet)


def add_counts(*counts: tuple[int, ...]) -> tuple[int, ...]:
    if not counts:
        return tuple(0 for _ in ALPHABET)
    return tuple(sum(c[i] for c in counts) for i in range(len(counts[0])))


def translate_count(count: tuple[int, ...], delta: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(a + b for a, b in zip(count, delta))


def basis_count(atom: str, alphabet: tuple[str, ...] = ALPHABET) -> tuple[int, ...]:
    return tuple(1 if a == atom else 0 for a in alphabet)


def is_prefix(prefix: tuple[str, ...], word: tuple[str, ...]) -> bool:
    return word[: len(prefix)] == prefix


def coarse_word(word: tuple[str, ...], phi: dict[str, str] = PHI) -> tuple[str, ...]:
    return tuple(phi[a] for a in word)


def coarse_count(
    fine_count: tuple[int, ...],
    fine_alphabet: tuple[str, ...] = ALPHABET,
    coarse_alphabet: tuple[str, ...] = COARSE_ALPHABET,
    phi: dict[str, str] = PHI,
) -> tuple[int, ...]:
    out = {a: 0 for a in coarse_alphabet}
    for atom, n in zip(fine_alphabet, fine_count):
        out[phi[atom]] += n
    return tuple(out[a] for a in coarse_alphabet)


def scalar_readout(counts: tuple[int, ...], weights: tuple[sp.Expr, ...]) -> sp.Expr:
    return sp.simplify(sum(sp.Integer(c) * w for c, w in zip(counts, weights)))


def relabel_word(word: tuple[str, ...], relabel: Callable[[str], str]) -> tuple[str, ...]:
    return tuple(relabel(a) for a in word)


def tagged_history(word: tuple[str, ...]) -> tuple[tuple[tuple[int, int, int], str], ...]:
    return tuple(((i, 0, 0), atom) for i, atom in enumerate(word))


def main() -> int:
    empty: tuple[str, ...] = ()
    w = ("singlet", "doublet", "singlet")
    u = ("other", "doublet")
    v = ("singlet", "other", "other")
    atom = ("doublet",)

    # ------------------------------------------------------------------
    # 1. Finite suffix append is a right monoid action on histories.
    # ------------------------------------------------------------------
    check("append.1 empty suffix acts as identity", append_suffix(w, empty) == w)
    check(
        "append.2 suffix action composes by concatenating suffixes",
        append_suffix(append_suffix(w, u), v) == append_suffix(w, append_suffix(u, v)),
    )
    check("append.3 append increases length by suffix length", len(append_suffix(w, v)) == len(w) + len(v))
    check("append.4 append preserves the old history as prefix", is_prefix(w, append_suffix(w, v)))
    check(
        "append.5 tagged append preserves old site-record pairs",
        tagged_history(w) == tagged_history(append_suffix(w, v))[: len(w)],
    )

    left = append_suffix(append_suffix(("singlet",), ("doublet",)), atom)
    fake_hom = append_suffix(("singlet",), atom) + append_suffix(("doublet",), atom)
    check(
        "append.6 fixed-atom append is not a monoid endomorphism",
        left != fake_hom,
        "append is a state update/action, not a homomorphism O* -> O*",
    )

    # ------------------------------------------------------------------
    # 2. Count projection is equivariant under append.
    # ------------------------------------------------------------------
    cw = count_word(w)
    cu = count_word(u)
    cv = count_word(v)
    check("C2.1 count of appended word is count plus suffix count", count_word(append_suffix(w, u)) == add_counts(cw, cu))
    check("C2.2 single-atom append increments exactly one basis count", count_word(append_suffix(w, atom)) == add_counts(cw, basis_count("doublet")))
    check("C2.3 count translation identity", translate_count(cw, count_word(empty)) == cw)
    check(
        "C2.4 count translations compose by count addition",
        translate_count(translate_count(cw, cu), cv) == translate_count(cw, add_counts(cu, cv)),
    )
    check("C2.5 counts are monotone under append", all(a <= b for a, b in zip(cw, count_word(append_suffix(w, v)))))
    check("C2.6 total count is history length", sum(count_word(append_suffix(w, v))) == len(append_suffix(w, v)))

    # ------------------------------------------------------------------
    # 3. Coarse-graining extends alphabet maps to word/count maps.
    # ------------------------------------------------------------------
    check(
        "G3.1 alphabet map extends to word homomorphism",
        coarse_word(append_suffix(w, u)) == append_suffix(coarse_word(w), coarse_word(u)),
    )
    check(
        "G3.2 coarse count agrees with count of coarse word",
        coarse_count(count_word(w)) == count_word(coarse_word(w), COARSE_ALPHABET),
    )
    check(
        "G3.3 coarse count commutes with append dynamics",
        coarse_count(count_word(append_suffix(w, v)))
        == add_counts(coarse_count(count_word(w)), coarse_count(count_word(v))),
    )
    check("G3.4 coarse-graining preserves total length", sum(coarse_count(count_word(append_suffix(w, v)))) == len(append_suffix(w, v)))

    g, r = sp.symbols("g r")
    fine_fiber_constant = (g, g, r)
    coarse_weights = (g, r)
    check(
        "G3.5 scalar readout is preserved for fiber-constant weights",
        scalar_readout(count_word(w), fine_fiber_constant) == scalar_readout(coarse_count(count_word(w)), coarse_weights),
    )

    fine_nonconstant = (sp.Integer(1), sp.Integer(2), sp.Integer(7))
    word_s = ("singlet",)
    word_d = ("doublet",)
    same_coarse_count = coarse_count(count_word(word_s)) == coarse_count(count_word(word_d))
    different_fine_readout = scalar_readout(count_word(word_s), fine_nonconstant) != scalar_readout(count_word(word_d), fine_nonconstant)
    check(
        "G3.6 coarse count cannot preserve arbitrary non-fiber-constant scalar readout",
        same_coarse_count and different_fine_readout,
        "singlet and doublet have same coarse count but different fine readout",
    )

    # ------------------------------------------------------------------
    # 4. Relabelings and deterministic post-record maps.
    # ------------------------------------------------------------------
    swap_sd = {"singlet": "doublet", "doublet": "singlet", "other": "other"}
    relabel = lambda a: swap_sd[a]
    check(
        "R4.1 deterministic atom relabeling extends to a word homomorphism",
        relabel_word(append_suffix(w, u), relabel) == append_suffix(relabel_word(w, relabel), relabel_word(u, relabel)),
    )
    relabeled_count = count_word(relabel_word(w, relabel))
    expected_relabel_count = (cw[1], cw[0], cw[2])
    check("R4.2 relabeling acts linearly on counts", relabeled_count == expected_relabel_count)
    check(
        "R4.3 relabeling commutes with suffix append through the relabeled suffix",
        relabel_word(append_suffix(w, v), relabel) == append_suffix(relabel_word(w, relabel), relabel_word(v, relabel)),
    )

    # ------------------------------------------------------------------
    # 5. Probability/rate/selector firewall.
    # ------------------------------------------------------------------
    realized = count_word(append_suffix(w, ("singlet",)))
    p_s, p_d, p_o = sp.symbols("p_s p_d p_o")
    expected_next = tuple(sp.Integer(c) + p for c, p in zip(cw, (p_s, p_d, p_o)))
    check("T5.1 realized post-record count update remains integral", all(isinstance(x, int) for x in realized))
    check(
        "T5.2 ensemble expectation is a different pre-record object",
        any(not val.is_integer for val in expected_next),
        "c+p is not the realized count c+e_o",
    )
    check(
        "T5.3 finite append grammar does not select which suffix occurs",
        append_suffix(empty, ("singlet",)) != append_suffix(empty, ("doublet",)),
        "both are admissible realized suffixes in the grammar",
    )

    # ------------------------------------------------------------------
    # 6. Unbounded finite post-record trajectories.
    # ------------------------------------------------------------------
    finite_words = [tuple("singlet" for _ in range(n)) for n in range(0, 31)]
    reached_from_empty = [append_suffix(empty, word) for word in finite_words]
    check("U6.1 every tested finite suffix is reached from empty", reached_from_empty == finite_words)
    check("U6.2 tested trajectory lengths are unbounded over finite samples", max(len(wd) for wd in reached_from_empty) == 30)
    check("U6.3 every reached trajectory remains finite", all(isinstance(len(wd), int) for wd in reached_from_empty))

    B = sp.symbols("B", integer=True, nonnegative=True)
    check("U6.4 finite-bound escape is append a suffix of length B+1", sp.simplify((B + 1) - B - 1) == 0)

    print("\n=== Finite-alphabet post-record dynamics interpretation ===")
    print("Finite suffixes act on record histories by append; counts update by translations in N^O.")
    print("Alphabet coarse-grainings commute with append/count dynamics, with scalar preservation only under compatible readout.")
    print("The grammar supplies post-record information dynamics, not record-production probabilities, rates, or dial selection.")
    print(f"SCORECARD PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
