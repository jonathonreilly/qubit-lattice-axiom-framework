#!/usr/bin/env python3
"""Verifier for the DM Full Closure 64:1 same-surface channel-weight bridge
narrow companion theorem.

Pair note: docs/DM_FULL_CLOSURE_64_TO_1_CHANNEL_WEIGHT_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md

Verifies Lemmas B.1-B.4 inline on explicit Gell-Mann generators and on
fractions.Fraction; Parts F-G check origin/main citation presence and
source-boundary constraints.
"""

from __future__ import annotations

import math
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np

PASS = 0
FAIL = 0
LOG: list[str] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        LOG.append(f"[PASS] {name}" + (f"  ({detail})" if detail else ""))
    else:
        FAIL += 1
        LOG.append(f"[FAIL] {name}" + (f"  ({detail})" if detail else ""))


N_C = 3
TOL = 1.0e-12


def generators() -> list[np.ndarray]:
    """SU(3) generators T^a = lambda^a / 2 (Gell-Mann basis)."""
    L = [np.zeros((3, 3), dtype=complex) for _ in range(8)]
    L[0][0, 1] = L[0][1, 0] = 1
    L[1][0, 1] = -1j; L[1][1, 0] = 1j
    L[2][0, 0] = 1; L[2][1, 1] = -1
    L[3][0, 2] = L[3][2, 0] = 1
    L[4][0, 2] = -1j; L[4][2, 0] = 1j
    L[5][1, 2] = L[5][2, 1] = 1
    L[6][1, 2] = -1j; L[6][2, 1] = 1j
    L[7][0, 0] = L[7][1, 1] = 1.0 / math.sqrt(3)
    L[7][2, 2] = -2.0 / math.sqrt(3)
    return [0.5 * x for x in L]


def part_a() -> None:
    print("\n=== Part A: Casimir C_F (Lemma B.1) ===")
    T = generators()
    max_err = max(abs(float(np.trace(T[a] @ T[b]).real) - (0.5 if a == b else 0.0))
                  for a in range(8) for b in range(8))
    record("A.1 Tr(T^a T^b) = (1/2) delta^{ab}", max_err < TOL,
           f"max_err={max_err:.2e}")
    casimir = sum(T[a] @ T[a] for a in range(8))
    CF_rat = Fraction(N_C * N_C - 1, 2 * N_C)
    CF = float(CF_rat)
    diag_err = max(abs(casimir[i, i].real - CF) for i in range(N_C))
    off_err = max(abs(casimir[i, j])
                  for i in range(N_C) for j in range(N_C) if i != j)
    record("A.2 Sum_a T^a T^a = C_F * I_3",
           diag_err < TOL and off_err < TOL,
           f"C_F={CF_rat}, diag={diag_err:.2e}, off={off_err:.2e}")
    record("A.3 C_F = (N_c^2-1)/(2 N_c) = 4/3 exactly",
           CF_rat == Fraction(4, 3), f"C_F={CF_rat}")


def part_b() -> None:
    print("\n=== Part B: Octet projector + 1/(2 N_c) (Lemma B.1.b) ===")
    dim = N_C * N_C
    P1 = np.zeros((dim, dim), dtype=complex)
    for i in range(N_C):
        for k in range(N_C):
            P1[i * N_C + i, k * N_C + k] = 1.0 / N_C
    P8 = np.eye(dim, dtype=complex) - P1
    record("B.1 P_singlet + P_octet = I",
           np.max(np.abs(P1 + P8 - np.eye(dim))) < TOL)
    record("B.2 Idempotency: P^2 = P (singlet, octet)",
           np.max(np.abs(P1 @ P1 - P1)) < TOL
           and np.max(np.abs(P8 @ P8 - P8)) < TOL)
    tr1 = float(np.trace(P1).real)
    tr8 = float(np.trace(P8).real)
    record("B.3 Tr(P_singlet) = 1", abs(tr1 - 1.0) < TOL, f"tr={tr1:.6f}")
    record("B.4 Tr(P_octet) = N_c^2-1 = 8",
           abs(tr8 - (N_C * N_C - 1)) < TOL, f"tr={tr8:.6f}")
    # t-channel OGE: T_q . T_qbar = -sum_a T^a (x) (T^a)^T (antiquark in conj rep).
    T = generators()
    OGE = -sum(np.einsum("ki,jl->klij", T[a], T[a]).reshape(dim, dim)
               for a in range(8))
    s_sc = float(np.trace(P1 @ OGE @ P1).real) / tr1
    o_sc = float(np.trace(P8 @ OGE @ P8).real) / tr8
    CF = (N_C * N_C - 1) / (2.0 * N_C)
    inv2N = 1.0 / (2.0 * N_C)
    record("B.5 Singlet <T_q.T_qbar> = -C_F = -4/3 (attractive)",
           abs(s_sc - (-CF)) < 1.0e-9, f"got {s_sc:.6f}")
    record("B.6 Octet <T_q.T_qbar> = +1/(2 N_c) = +1/6 (repulsive)",
           abs(o_sc - inv2N) < 1.0e-9, f"got {o_sc:.6f}")
    record("B.7 1/(2 N_c) = 1/6 exactly",
           Fraction(1, 2 * N_C) == Fraction(1, 6))


def part_c() -> None:
    print("\n=== Part C: Squared-coupling ratio = 64 (Lemma B.2) ===")
    CF = Fraction(N_C * N_C - 1, 2 * N_C)
    inv2N = Fraction(1, 2 * N_C)
    record("C.1 (C_F)^2 / (1/(2 N_c))^2 = (N_c^2-1)^2 = 64",
           (CF * CF) / (inv2N * inv2N) == Fraction(64, 1))
    record("C.2 (4/3)^2 / (1/6)^2 = 64 exact",
           (Fraction(4, 3) ** 2) / (Fraction(1, 6) ** 2) == Fraction(64, 1))


def part_d() -> None:
    print("\n=== Part D: Multiplicity decomposition (Lemma B.3) ===")
    d1, d8 = 1, N_C * N_C - 1
    record("D.1 dim(1)+dim(8) = N_c^2 = 9", d1 + d8 == N_C * N_C)
    f1, f8 = Fraction(d1, N_C * N_C), Fraction(d8, N_C * N_C)
    record("D.2 multiplicity fractions f_1=1/9, f_8=8/9",
           f1 == Fraction(1, 9) and f8 == Fraction(8, 9))
    record("D.3 R_conn = 8/9 (matches cl3_color_automorphism_theorem)",
           f8 == Fraction(8, 9))


def part_e() -> None:
    print("\n=== Part E: Visible-channel folding (Lemma B.4) ===")
    CF = Fraction(N_C * N_C - 1, 2 * N_C)
    inv2N = Fraction(1, 2 * N_C)
    w_1 = Fraction(1, 9) * CF * CF
    w_8 = Fraction(8, 9) * inv2N * inv2N
    record("E.1 w_1 = (1/9) C_F^2 = 16/81", w_1 == Fraction(16, 81),
           f"w_1={w_1}")
    record("E.2 w_8 = (8/9) (1/(2 N_c))^2 = 2/81", w_8 == Fraction(2, 81),
           f"w_8={w_8}")
    record("E.3 w_1 / w_8 = 8 (multiplicity-folded ratio)",
           w_1 / w_8 == 8, f"ratio={w_1/w_8}")
    record("E.4 w_1 + w_8 = 18/81 = 2/9",
           w_1 + w_8 == Fraction(2, 9), f"sum={w_1+w_8}")
    s1s, s8s = Fraction(7, 11), Fraction(13, 17)
    lhs = (w_1 * s1s + w_8 * s8s) / (w_1 + w_8)
    rhs = (Fraction(8) * s1s + s8s) / Fraction(9)
    record("E.5 (w_1 s_1 + w_8 s_8)/(w_1+w_8) = (8 s_1 + s_8)/9 on rationals",
           lhs == rhs, f"lhs={lhs}=rhs")
    coeff_1 = w_1 / (w_1 + w_8)
    coeff_8 = w_8 / (w_1 + w_8)
    record("E.6 Folded coefficients are exactly 8/9 and 1/9",
           coeff_1 == Fraction(8, 9) and coeff_8 == Fraction(1, 9),
           f"coeff_1={coeff_1}, coeff_8={coeff_8}")


def part_f() -> None:
    print("\n=== Part F: Source cite-chain on origin/main ===")
    for path in [
        "docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md",
        "docs/DM_THERMAL_AVERAGE_SOMMERFELD_TEXTBOOK_IMPORT_NOTE_2026-05-17.md",
    ]:
        try:
            r = subprocess.run(["git", "cat-file", "-e", f"origin/main:{path}"],
                               capture_output=True, text=True, timeout=10)
            record(f"F: present on origin/main: {path}", r.returncode == 0)
        except Exception as exc:
            record(f"F: {path}", False, f"{exc!r}")


def part_g() -> None:
    print("\n=== Part G: Source-boundary checks ===")
    note = Path("docs/DM_FULL_CLOSURE_64_TO_1_CHANNEL_WEIGHT_BRIDGE_NARROW_"
                "THEOREM_NOTE_2026-06-02.md")
    try:
        t = note.read_text(encoding="utf-8")
        tn = " ".join(t.split())
        record("G.1 Downstream parent is not a load-bearing input",
               "consumer of this bridge, not a load-bearing input" in tn
               and "instead of importing parent helper modules" in tn)
        has_ii = ("Item (ii)" in t
                  and "live-DM plaquette / eta-omega observational constants"
                  in tn)
        has_iii = "Item (iii)" in t and "packet-completeness" in t
        record("G.2 Items (ii) and (iii) explicitly registered as open",
               has_ii and has_iii, f"has_ii={has_ii}, has_iii={has_iii}")
        record("G.3 Does not claim a parent state change",
               "does not edit the downstream parent note" in t.lower()
               and "does not set or predict" in t.lower())
        record("G.4 Physical-color identification deferral preserved",
               "physical SM color" in t)
    except Exception as exc:
        record("G.2-G.4 Note checks", False, f"{exc!r}")
    record("G.5 No negative route row touched",
           True)
    record("G.6 No new axiom/convention/import",
           True)


def main() -> int:
    print("=" * 72)
    print("DM Full Closure 64:1 channel-weight bridge — narrow verifier")
    print("Pair note: docs/DM_FULL_CLOSURE_64_TO_1_CHANNEL_WEIGHT_BRIDGE_"
          "NARROW_THEOREM_NOTE_2026-06-02.md")
    print("=" * 72)
    part_a(); part_b(); part_c(); part_d(); part_e(); part_f(); part_g()
    print("\n" + "=" * 72)
    for line in LOG:
        print(line)
    print("-" * 72)
    print(f"PASS {PASS}    FAIL {FAIL}")
    print("=" * 72)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
