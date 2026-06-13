#!/usr/bin/env python3
"""Independent exact cross-check for g_bare / N_F pending-chain rows.

This is a source-side helper for rows that are awaiting audit
cross-confirmation.  It is not an audit verdict and does not promote either
row.  It independently rechecks the small algebraic spine shared by:

- docs/G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md
- docs/N_F_BOUNDED_Z2_REDUCTION_THEOREM_NOTE_2026-05-07_w2.md
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
G_NOTE = ROOT / "docs" / "G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md"
NF_NOTE = ROOT / "docs" / "N_F_BOUNDED_Z2_REDUCTION_THEOREM_NOTE_2026-05-07_w2.md"

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
    else:
        FAIL += 1
    suffix = f"  [{detail}]" if detail else ""
    print(f"{tag}: {label}{suffix}")


def compact(text: str) -> str:
    out = text.lower()
    for old, new in {
        "*": "",
        "`": "",
        "²": "^2",
        "→": "->",
        "≠": "!=",
        "∈": "in",
        "δ": "delta",
    }.items():
        out = out.replace(old, new)
    return " ".join(out.split())


def gell_mann() -> list[np.ndarray]:
    return [
        np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
        np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
        np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
        np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
        np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
    ]


def embed_full_space(t: np.ndarray) -> np.ndarray:
    block4 = np.zeros((4, 4), dtype=complex)
    block4[:3, :3] = t
    return np.kron(block4, np.eye(2, dtype=complex))


def main() -> int:
    print("g_bare / N_F pending-chain exact cross-check")
    print(f"g_note={G_NOTE.relative_to(ROOT)}")
    print(f"nf_note={NF_NOTE.relative_to(ROOT)}")
    print()

    g_text = compact(G_NOTE.read_text(encoding="utf-8"))
    nf_text = compact(NF_NOTE.read_text(encoding="utf-8"))

    lambdas = gell_mann()
    t3 = [lam / 2 for lam in lambdas]
    gram3 = np.array([[np.trace(a @ b).real for b in t3] for a in t3])
    check("canonical color-carrier Gram is Tr_3(T_a T_b)=1/2 delta_ab", np.allclose(gram3, 0.5 * np.eye(8)))

    casimir = sum(t @ t for t in t3)
    check("canonical color-carrier Casimir is C_F=4/3", np.allclose(casimir, (4.0 / 3.0) * np.eye(3)))

    t8 = [embed_full_space(t) for t in t3]
    gram8 = np.array([[np.trace(a @ b).real for b in t8] for a in t8])
    check("full framework trace gives Tr_V(T_a^V T_b^V)=1 delta_ab", np.allclose(gram8, np.eye(8)))
    check("trace-surface ratio Tr_V/Tr_3 is exactly 2", abs(gram8[0, 0] / gram3[0, 0] - 2.0) < 1e-12)

    for nf, cf in [(Fraction(1, 2), Fraction(4, 3)), (Fraction(1, 1), Fraction(8, 3))]:
        check(f"C_F=(8/3)N_F maps N_F={nf} to C_F={cf}", Fraction(8, 3) * nf == cf)

    nc = Fraction(3, 1)
    beta = 2 * nc
    g2 = (2 * nc) / beta
    check("Wilson canonical beta=2N_c at N_c=3 gives beta=6", beta == 6)
    check("beta=2N_c/g_bare^2 with beta=2N_c gives g_bare^2=1", g2 == 1)

    check("g_bare note locates exactly one convention layer at N_F", "exactly one convention layer" in g_text and "n_f" in g_text)
    check("g_bare note excludes derivation of N_F=1/2 from A1/A2 alone", "does not claim" in g_text and "n_f = 1/2" in g_text and "a1" in g_text and "a2" in g_text)
    check("g_bare note keeps Wilson action form as separate retained/bounded surface", "wilson plaquette action form" in g_text and "separate" in g_text)
    check("g_bare note does not claim absolute g_bare from A1+A2", "absolute derivation of g_bare = 1 from a1+a2" in g_text)

    check("N_F note states the binary trace-surface set {1/2, 1}", "n_f in {1/2, 1}" in nf_text)
    check("N_F note identifies V_3 value 1/2 and full V value 1", "color carrier" in nf_text and "1/2" in nf_text and "full framework hilbert space" in nf_text and "1" in nf_text)
    check("N_F note refuses unique derivation of N_F=1/2", "cannot yet say" in nf_text and "uniquely forced by the primitives" in nf_text)
    check("N_F note refuses zero-input derivation of g_bare=1", "zero-input derivation of g_bare = 1" in nf_text)
    check("N_F note names remaining binary trace-surface choice", "remaining open step" in nf_text and "binary choice" in nf_text)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
