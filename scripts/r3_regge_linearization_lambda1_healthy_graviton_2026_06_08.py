"""R3 target-operator algebra certificate.

This runner checks the continuum linearized Einstein tensor target operator.
It does not compute the second variation of a cubic-Coxeter Regge action and
does not derive the framework's edge-length metric degrees of freedom.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


ETA = np.diag([-1.0, 1.0, 1.0, 1.0])
PASS = 0
FAIL = 0


def check(name: str, cond: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(cond)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(ok)
    FAIL += int(not ok)
    return ok


def raise_idx(v: np.ndarray) -> np.ndarray:
    return ETA @ v


def trace_h(h: np.ndarray) -> float:
    return float(np.trace(ETA @ h))


def G_lin(h: np.ndarray, k: np.ndarray) -> np.ndarray:
    """Linearized Einstein tensor in momentum space for covariant h and k."""
    ku = raise_idx(k)
    k2 = float(k @ ku)
    htr = trace_h(h)
    kh = h @ ku
    kkh = float(ku @ h @ ku)
    term = (
        -k2 * h
        - np.outer(k, k) * htr
        + np.outer(k, kh)
        + np.outer(kh, k)
        + ETA * (k2 * htr - kkh)
    )
    return -0.5 * term


def source_guardrail() -> tuple[bool, str]:
    note = Path(
        "docs/R3_GEOMETRIC_REGGE_LINEARIZATION_GIVES_HEALTHY_LAMBDA1_GRAVITON_NARROW_THEOREM_NOTE_2026-06-08.md"
    )
    text = note.read_text(encoding="utf-8")
    required = [
        "target continuum operator",
        "does not compute the second",
        "does not derive edge-length metric",
        "not landed",
        "kinetic-isotropy primitive supplies a dynamical metric",
    ]
    missing = [marker for marker in required if marker not in text]
    return not missing, f"missing={missing}"


def main() -> int:
    print("R3 target operator: linearized Einstein tensor lambda-one algebra")
    print("=" * 76)

    k = np.array([0.0, 0.0, 0.0, 1.7])
    ku = raise_idx(k)
    k2 = float(k @ ku)
    rng = np.random.default_rng(11)

    max_gauge = 0.0
    for _ in range(500):
        xi = rng.standard_normal(4)
        h_gauge = np.outer(k, xi) + np.outer(xi, k)
        max_gauge = max(max_gauge, float(np.max(np.abs(G_lin(h_gauge, k)))))
    check(
        "R3a gauge modes are zero modes of G_lin",
        max_gauge < 1e-12,
        f"max |G_lin(k xi + xi k)| over 500 samples = {max_gauge:.2e}",
    )

    h_tt = np.zeros((4, 4))
    h_tt[1, 1] = 1.0
    h_tt[2, 2] = -1.0
    trans = float(np.max(np.abs(h_tt @ ku)))
    tr = abs(trace_h(h_tt))
    G_tt = G_lin(h_tt, k)
    expected = 0.5 * k2 * h_tt
    tt_error = float(np.max(np.abs(G_tt - expected)))
    check(
        "R3b supplied TT sample has nonzero two-derivative response",
        trans < 1e-12 and tr < 1e-12 and tt_error < 1e-12 and np.max(np.abs(G_tt)) > 1e-9,
        f"k.h={trans:.2e}; trace={tr:.2e}; max |G-(1/2 k^2 h)|={tt_error:.2e}; k2={k2:.3f}",
    )

    h_conf = ETA.copy()
    G_conf = G_lin(h_conf, k)
    conf_like_tt = np.allclose(G_conf, 0.5 * k2 * h_conf, atol=1e-12)
    check(
        "R3c conformal sample is distinct from the TT response",
        np.max(np.abs(G_conf)) > 1e-12 and not conf_like_tt,
        f"max |G_conf|={np.max(np.abs(G_conf)):.3e}; TT-like={conf_like_tt}",
    )

    guard_ok, guard_detail = source_guardrail()
    check(
        "R3d source note keeps Regge/metric guardrails",
        guard_ok,
        guard_detail,
    )

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print("Boundary: target-operator algebra only; no Regge second variation,")
    print("no emergent edge-length metric, and no physical graviton closure.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
