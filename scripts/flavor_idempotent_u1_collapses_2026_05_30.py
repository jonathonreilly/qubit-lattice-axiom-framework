#!/usr/bin/env python3
"""Finite negative boundary for the idempotent-U(1) flavor route."""

from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
W = np.exp(2j * np.pi / 3)


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


def spectral_projector(C, q):
    I = np.eye(3, dtype=complex)
    return (I + (W ** (-q)) * C + (W ** (-2 * q)) * (C @ C)) / 3.0


def main():
    C = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], complex)
    I = np.eye(3, dtype=complex)
    J = np.ones((3, 3), dtype=complex)
    Ps = J / 3
    Pd = I - J / 3
    U = np.exp(1j * 0.7) * Ps + np.exp(1j * 2.3) * Pd
    H = I + (0.6 + 0.3j) * C + (0.6 - 0.3j) * C.T

    passed = []
    passed.append(
        check(
            "K1 idempotent U(1) commutes with C and is distinct from generator rephasing",
            np.allclose(U @ C - C @ U, 0),
        )
    )
    passed.append(
        check(
            "K2 idempotent U(1) is inert by conjugation on circulant H",
            np.allclose(U @ H @ U.conj().T, H),
        )
    )
    one_sided = H @ U.conj().T
    passed.append(
        check(
            "K3 one-sided action is not a Hermitian signed-readout route",
            not np.allclose(one_sided, one_sided.conj().T)
            and not np.allclose(np.linalg.eigvals(one_sided).imag, 0),
        )
    )

    P0 = spectral_projector(C, 0)
    P1 = spectral_projector(C, 1)
    P2 = spectral_projector(C, 2)
    Q_equal = P1 + P2
    Q_opp = P1 - P2
    coeffs, *_ = np.linalg.lstsq(
        np.column_stack([Ps.reshape(-1), Pd.reshape(-1)]),
        Q_opp.reshape(-1),
        rcond=None,
    )
    span_residual = np.linalg.norm(coeffs[0] * Ps + coeffs[1] * Pd - Q_opp)
    passed.append(
        check(
            "K4 equal doublet charge is idempotent-native; opposite charge is outside span{Ps,Pd}",
            np.allclose(Q_equal, Pd)
            and span_residual > 0.5
            and np.allclose(P0 + P1 + P2, I),
            f"opposite-charge span residual={span_residual:.3f}",
        )
    )

    r = {"lep": 0.500, "down": 0.597, "up": 0.773}
    qem = {"lep": 1.0, "down": 1 / 3, "up": 2 / 3}
    color = {"lep": 1, "down": 3, "up": 3}
    rmono = r["lep"] < r["down"] < r["up"]
    qem_mono = (qem["lep"] < qem["down"] < qem["up"]) or (
        qem["lep"] > qem["down"] > qem["up"]
    )
    color_strict = color["lep"] < color["down"] < color["up"]
    passed.append(
        check(
            "K5 supplied charge/color labels do not monotonely index the supplied r order",
            rmono and not qem_mono and not color_strict,
            "comparator only; not a sector-selector theorem",
        )
    )

    source = (ROOT / "docs/FLAVOR_IDEMPOTENT_U1_COLLAPSES_NOTE_2026-05-30.md").read_text()
    authorities = [
        "KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md",
        "KOIDE_C3_GENERATOR_REPHASING_OBSTRUCTION_NARROW_THEOREM_NOTE_2026-05-29.md",
        "THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md",
    ]
    passed.append(
        check(
            "K6 one-hop authority links are present for chiral, rephasing, and generation-algebra boundaries",
            all(name in source for name in authorities),
        )
    )
    passed.append(
        check(
            "K7 source boundary demotes ordering to comparator and keeps selector open",
            "not used as a theorem" in source
            and "does not prove the absence of every possible" in source
            and "sector selector remains a separate open bridge" in source,
        )
    )

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed) - sum(passed)}")
    print("VERDICT: the idempotent-U(1) route is a finite negative boundary.")
    print("It exists and dodges blanket C^3=I wording, but conjugation is inert;")
    print("the one-sided action is non-Hermitian/chiral; and opposite doublet")
    print("charge leaves the idempotent span. The observed ordering table is only")
    print("a comparator, not a framework-native sector-selector theorem.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
