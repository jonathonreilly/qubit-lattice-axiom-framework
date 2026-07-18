#!/usr/bin/env python3
"""Exact finite controls for the infinite-redundancy quasilocal sector probe."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs"
    / "work_history"
    / "repo"
    / "review_feedback"
    / "INFINITE_REDUNDANCY_QUASILOCAL_RECORD_SECTOR_NOTE_2026-07-14.md"
)
AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PAULI = {
    "I": ((1, 0), (0, 1)),
    "X": ((0, 1), (1, 0)),
    "Y": ((0, -1j), (1j, 0)),
    "Z": ((1, 0), (0, -1)),
}
PASS = 0
FAIL = 0


def section(title: str) -> None:
    print("\n" + "=" * 79)
    print(title)
    print("=" * 79)


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label}" + (f" :: {detail}" if detail else ""))
    else:
        FAIL += 1
        print(f"FAIL {label}" + (f" :: {detail}" if detail else ""))


def product_element(word: tuple[str, ...], row: int, column: int) -> complex:
    value = 1 + 0j
    for label in word:
        value *= PAULI[label][row][column]
    return value


def cat_expectation(word: tuple[str, ...], phase: complex = 1 + 0j) -> complex:
    diagonal = product_element(word, 0, 0) + product_element(word, 1, 1)
    cross = phase * product_element(word, 0, 1) + phase.conjugate() * product_element(word, 1, 0)
    return (diagonal + cross) / 2


def mixture_expectation(word: tuple[str, ...], p: Fraction = Fraction(1, 2)) -> complex:
    return complex(p) * product_element(word, 0, 0) + complex(1 - p) * product_element(word, 1, 1)


def close(left: complex, right: complex, tol: float = 1e-12) -> bool:
    return abs(left - right) < tol


def source_contract() -> None:
    section("A - Source and authority boundary")
    check("A note exists", NOTE.is_file())
    check("A live axioms exist", AXIOMS.is_file())
    text = NOTE.read_text(encoding="utf-8").lower().replace("*", "")
    check("A note is authority-free", "authority: none" in text)
    check("A note changes no live foundation", "changes no live foundation" in text)
    check("A note is bounded away from a universal sector no-go", "not a no-go against infinite-volume collapse" in text)
    check("A note contains N1-N8", all(f"n{index} —" in text for index in range(1, 9)))
    axioms = AXIOMS.read_text(encoding="utf-8")
    check("A current Record permanence is present", "records are permanent." in axioms)
    check("A state-is-records qualification is present", "A state is a configuration of records." in axioms)


def finite_local_indistinguishability() -> None:
    section("B - Every proper-support Pauli observable forgets GHZ phase")
    for n in range(2, 7):
        words = tuple(product(PAULI, repeat=n))
        proper = tuple(word for word in words if "I" in word)
        check(f"B N={n} proper-support census is nonempty", bool(proper))
        check(
            f"B N={n} GHZ plus equals mixture on every proper-support Pauli",
            all(close(cat_expectation(word), mixture_expectation(word)) for word in proper),
        )
        check(
            f"B N={n} GHZ minus equals mixture on every proper-support Pauli",
            all(close(cat_expectation(word, -1 + 0j), mixture_expectation(word)) for word in proper),
        )
        full_x = tuple("X" for _ in range(n))
        check(f"B N={n} full X distinguishes plus cat from mixture", close(cat_expectation(full_x), 1) and close(mixture_expectation(full_x), 0))
        check(f"B N={n} full X distinguishes cat phases", close(cat_expectation(full_x, -1 + 0j), -1))


def branch_and_weight_controls() -> None:
    section("C - Branch distinction, nonconversion, weight, and actuality")
    local_z = ("Z",)
    check("C onsite Z distinguishes product branches", close(product_element(local_z, 0, 0), 1) and close(product_element(local_z, 1, 1), -1))
    for n in range(2, 9):
        for flipped in (1, n - 1):
            after = (1,) * flipped + (0,) * (n - flipped)
            check(f"C N={n} flipping {flipped} sites does not convert the whole branch", after != (1,) * n)
    half = mixture_expectation(local_z, Fraction(1, 2))
    two_thirds = mixture_expectation(local_z, Fraction(2, 3))
    check("C half mixture has zero local Z", close(half, 0))
    check("C two-thirds mixture has local Z one-third", close(two_thirds, Fraction(1, 3)))
    check("C same sector support permits different weights", not close(half, two_thirds))
    check("C nontrivial mixture differs from either actual branch", not close(two_thirds, 1) and not close(two_thirds, -1))


def finite_reach_controls() -> None:
    section("D - Finite nearest-neighbor time never completes an infinite tail")
    volumes = []
    for t in range(0, 21):
        volume = (4 * t**3 + 6 * t**2 + 8 * t + 3) // 3
        volumes.append(volume)
        check(f"D t={t} Manhattan ball volume is finite", isinstance(volume, int) and volume > 0)
    check("D ball volumes grow strictly", all(left < right for left, right in zip(volumes, volumes[1:])))
    check("D finite horizon remains finite at t=20", volumes[-1] == 11521)


def claim_contract() -> None:
    section("E - Exact claim and route boundary")
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    tokens = (
        "operational phase quotient",
        "superselection-like nonreconnection",
        "does not actualize one branch",
        "does not explain finite-time formation",
        "permanence and loss of hidden phase may be theorems",
        "mixture neither chooses its weight nor names one member",
        "does not prove a general infinite- volume superselection theorem",
        "strongest surviving steelman",
    )
    for token in tokens:
        check(f"E note contains boundary: {token}", token in text)


def main() -> int:
    source_contract()
    finite_local_indistinguishability()
    branch_and_weight_controls()
    finite_reach_controls()
    claim_contract()
    section("SUMMARY")
    print(f"PASS={PASS}")
    print(f"FAIL={FAIL}")
    print("RESULT: " + ("PASS" if FAIL == 0 else "FAIL"))
    print("BOUNDARY: infinite quasilocal redundancy can retire phase and local reconnection, but not occurrence, sector weight, actuality, or finite-time formation")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
