#!/usr/bin/env python3
"""L1/L2 determinant-positivity checks plus an L3 readout-bridge firewall.

Bounded theorem checked here:

* L1: for finite real antisymmetric D and positive real diagonal S,
  det(S + D) is strictly positive real.
* L2: for invertible real antisymmetric D and real diagonal J satisfying
  ||D^{-1}J|| < 1, det(D+tJ) stays positive for t in [0,1].

The legacy claim ID contains ``and_log_readout``, but no log-readout theorem is
claimed. The runner supplies two decisive guards against that scope drift:

* an exact countermodel shows that continuity and direct-sum additivity do not
  force a determinant-only readout; and
* source-text checks require the theorem block to remain free of Record/readout
  claims while the separate open boundary names both missing bridges.

No framework code and no empirical/fitted/literature numerical input are used.
"""
from __future__ import annotations

from pathlib import Path

import numpy as np


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/REAL_DIAGONAL_SOURCE_DET_POSITIVITY_AND_LOG_READOUT_LEMMA_NOTE_2026-06-08.md"


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def rand_antisym(n: int, rng: np.random.Generator) -> np.ndarray:
    a = rng.standard_normal((n, n))
    return a - a.T


def main() -> int:
    print("REAL-DIAGONAL-SOURCE DETERMINANT POSITIVITY + READOUT-BRIDGE FIREWALL")
    print("=" * 76)
    rng = np.random.default_rng(0)

    # L1: det(S + D) > 0 for S positive diagonal and D real antisymmetric.
    ok1 = True
    worst = np.inf
    for _ in range(400):
        n = int(rng.integers(2, 7))
        dmat = rand_antisym(n, rng)
        smat = np.diag(rng.uniform(0.05, 3.0, size=n))
        determinant = float(np.linalg.det(smat + dmat))
        worst = min(worst, determinant)
        complex_det = np.linalg.det((smat + dmat).astype(complex))
        ok1 = ok1 and determinant > 0 and abs(np.imag(complex_det)) < 1e-9
    check(
        "L1: det(S+D)>0 is real on positive-diagonal S + real antisymmetric D",
        ok1,
        f"400 deterministic-seed cases; minimum determinant={worst:.4f}",
    )

    # L1 structural mechanism on both odd and even dimensions.
    structure_ok = True
    details = []
    for n in (5, 6):
        bmat = rand_antisym(n, rng)
        eigenvalues = np.linalg.eigvals(bmat)
        real_parts_zero = np.allclose(np.real(eigenvalues), 0, atol=1e-9)
        det_positive = float(np.linalg.det(np.eye(n) + bmat)) >= 1.0 - 1e-9
        structure_ok = structure_ok and real_parts_zero and det_positive
        details.append(
            f"n={n}: max|Re eig|={np.max(np.abs(np.real(eigenvalues))):.1e}, "
            f"det(I+B)={np.linalg.det(np.eye(n)+bmat):.6f}"
        )
    check(
        "L1 mechanism: real antisymmetric spectrum is imaginary-paired and det(I+B)>=1",
        structure_ok,
        "; ".join(details),
    )

    # L2: Neumann sign constancy on the derivative patch.
    ok2 = True
    tested = 0
    for _ in range(200):
        n = int(rng.integers(2, 6)) * 2
        dmat = rand_antisym(n, rng)
        if abs(np.linalg.det(dmat)) < 1e-6:
            continue
        jmat = np.diag(rng.standard_normal(n))
        scale = 0.5 / (np.linalg.norm(np.linalg.inv(dmat) @ jmat) + 1e-12)
        jmat = scale * jmat
        neumann_norm = np.linalg.norm(np.linalg.inv(dmat) @ jmat)
        determinants = [float(np.linalg.det(dmat + t * jmat)) for t in np.linspace(0, 1, 25)]
        ok2 = ok2 and neumann_norm < 1 and all(value > 0 for value in determinants)
        tested += 1
    check(
        "L2: ||D^{-1}J||<1 keeps det(D+tJ)>0 on t in [0,1]",
        ok2 and tested > 0,
        f"{tested} deterministic-seed invertible patches",
    )

    # Open-L3 firewall: determinant algebra remains true in the countermodel.
    s1 = np.diag([4.0, 1.0])
    s2 = np.diag([2.0, 2.0])
    direct_sum = np.block([[s1, np.zeros((2, 2))], [np.zeros((2, 2)), s2]])
    multiplicative = np.isclose(np.linalg.det(direct_sum), np.linalg.det(s1) * np.linalg.det(s2))
    check(
        "L3 firewall premise check: determinant remains multiplicative on direct sums",
        bool(multiplicative),
        f"det(S1 direct_sum S2)={np.linalg.det(direct_sum):.1f}",
    )

    # W_epsilon = log det + epsilon Tr is continuous and direct-sum additive,
    # yet distinguishes equal-determinant blocks. Thus determinant-only readout
    # cannot be inferred from determinant multiplicativity plus additivity.
    epsilon = 0.25

    def w_eps(matrix: np.ndarray) -> float:
        return float(np.log(np.linalg.det(matrix)) + epsilon * np.trace(matrix))

    additive = np.isclose(w_eps(direct_sum), w_eps(s1) + w_eps(s2))
    same_det = np.isclose(np.linalg.det(s1), np.linalg.det(s2))
    different_readout = not np.isclose(w_eps(s1), w_eps(s2))
    check(
        "L3 firewall countermodel: continuous block-additive readout need not be determinant-only",
        bool(additive and same_det and different_readout),
        (
            f"det(S1)=det(S2)={np.linalg.det(s1):.1f}; "
            f"Tr(S1)={np.trace(s1):.1f}, Tr(S2)={np.trace(s2):.1f}; "
            f"W_eps(S1)={w_eps(s1):.6f}, W_eps(S2)={w_eps(s2):.6f}"
        ),
    )

    note_text = NOTE.read_text(encoding="utf-8")
    theorem_start = note_text.index("## Theorem statement: determinant positivity only")
    boundary_start = note_text.index("## Open L3 boundary")
    theorem_block = note_text[theorem_start:boundary_start]
    theorem_scope_clean = all(
        token not in theorem_block
        for token in ("Record", "determinant-only readout", "source-block-to-disjoint-record", "c log det")
    )
    check(
        "Scope guard: the bounded-theorem block contains only L1/L2 determinant positivity",
        theorem_scope_clean and "complete bounded-theorem target" in theorem_block,
        "Record/readout bridge vocabulary is confined to the separate open boundary",
    )

    required_boundary_strings = (
        "conditional readout classification, not a theorem claim",
        "determinant-only readout bridge",
        "source-block-to-disjoint-record bridge",
        "Only **if a separate future premise or theorem supplies both bridges**",
        "Choosing `c = 1` is a",
        "further normalization convention",
        "Consumers must **not** cite this claim",
    )
    missing_boundary_strings = [text for text in required_boundary_strings if text not in note_text]
    check(
        "Scope guard: the note explicitly leaves both L3 bridges conditional/open",
        not missing_boundary_strings,
        (
            "required determinant-only, source-to-record, and normalization firewalls are present"
            if not missing_boundary_strings
            else f"missing strings: {missing_boundary_strings}"
        ),
    )

    print(f"\nSCORECARD PASS={PASS} FAIL={FAIL}")
    print(
        "RESULT: L1/L2 determinant positivity checks pass. The exact countermodel and source-scope "
        "guards prevent this runner or note from licensing a determinant-only readout, a "
        "source-block-to-record bridge, or c log det. Independent audit lane owns status."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
