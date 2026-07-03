"""Doublet field-space metric scope repair.

The runner verifies the finite metric calculation on (a, Re b, Im b), the
conditional det_R/det_C arithmetic, and two route-pruning checks. It does not
prove that A1 uniquely defaults to det_R or that every admissible field-space
complex structure is excluded.
"""
from pathlib import Path

import numpy as np


def check(name, cond, detail=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    return bool(cond)


C = np.array([[0, 0, 1.0], [1, 0, 0], [0, 1, 0]])
I3 = np.eye(3)


def hs(A, B):
    return np.trace(A.conj().T @ B)


def main():
    passed = []

    da, dx, dy = I3, C + C @ C, 1j * (C - C @ C)
    G = np.array([[hs(u, v) for v in (da, dx, dy)] for u in (da, dx, dy)]).real
    passed.append(check(
        "M1 HS/coherent-state field-space metric on (a,Re b,Im b) is diag(3,6,6)",
        np.allclose(G, np.diag([3, 6, 6])),
        f"metric={np.round(G, 3).tolist()}; metric value is reading-neutral"))

    def hlin(b):
        return b * C + np.conj(b) * C.conj().T

    viol = np.linalg.norm(hlin(1j) - 1j * hlin(1.0))
    iH = 1j * hlin(1.0)
    passed.append(check(
        "M2 operator-symbol route is R-linear not C-linear; multiplying by i exits Hermitian observables",
        viol > 1e-9 and np.allclose(iH.conj().T, -iH),
        f"||H_lin(ib)-iH_lin(b)||={viol:.4f}; i*H_lin(1) is anti-Hermitian"))

    q = lambda r: 1 / 3 + 2 / 3 * r
    passed.append(check(
        "M3 conditional det_R arithmetic: per-real-direction reading gives r=1 and Q=1",
        abs(q(1.0) - 1.0) < 1e-12,
        f"Q(r=1)={q(1.0):.4f}"))
    passed.append(check(
        "M4 conditional det_C arithmetic: equal-complex-block reading gives r=1/2 and Q=2/3",
        abs(q(0.5) - 2 / 3) < 1e-12,
        f"Q(r=1/2)={q(0.5):.4f}"))

    lam = lambda dl: np.array([1 + 2 * 0.7 * np.cos(dl + 2 * np.pi * k / 3) for k in range(3)])
    m0, m60 = np.round(lam(0) ** 2, 3), np.round(lam(np.pi / 3) ** 2, 3)
    passed.append(check(
        "M5 without a continuous U(1)_b gauge, delta=arg(b) is spectrum-observable in this family",
        not np.allclose(sorted(m0), sorted(m60)),
        f"masses delta=0 {sorted(m0.tolist())}; delta=60deg {sorted(m60.tolist())}"))

    allowed = [0.0, 2 * np.pi / 3, 4 * np.pi / 3]
    continuous_probe = 0.37
    passed.append(check(
        "M6 C^3=I permits only discrete rephasings C->exp(i alpha)C, not a continuous U(1)_b",
        all(abs(np.exp(1j * alpha) ** 3 - 1) < 1e-12 for alpha in allowed)
        and abs(np.exp(1j * continuous_probe) ** 3 - 1) > 1e-3,
        "allowed alpha are 0, 2pi/3, 4pi/3; generic alpha fails order three"))

    root = Path(__file__).resolve().parents[1]
    note = (root / "docs" / "FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md").read_text()
    banned = [
        "A1 default is det_R",
        "Q=1 is selected by the framework",
        "maximal hierarchy",
    ]
    required = [
        "reading-neutral",
        "These are conditional readings.",
        "No new axiom is introduced.",
    ]
    passed.append(check(
        "M7 source boundary guard: no det_R default or full-J-exclusion conclusion is promoted",
        all(term not in note for term in banned) and all(term in note for term in required),
        "the packet leaves physical doublet counting open"))

    print(f"\nSCORECARD PASS={sum(passed)} FAIL={len(passed)-sum(passed)}")
    print("VERDICT: bounded-support finite metric packet.")
    print("The HS/coherent-state metric is diag(3,6,6) and reading-neutral. The det_R")
    print("and det_C r/Q values are conditional arithmetic readings. The operator-symbol")
    print("complex-linearity route and continuous U(1)_b route are pruned, but this runner")
    print("does not select the physical doublet count.")
    return 0 if all(passed) else 1


if __name__ == "__main__":
    raise SystemExit(main())
