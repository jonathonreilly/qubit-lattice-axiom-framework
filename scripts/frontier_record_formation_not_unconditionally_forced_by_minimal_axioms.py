#!/usr/bin/env python3
"""Finite unitary controls and current axiom-quotation consistency.

Four model calculations plus two documentary checks; not full framework
countermodels or a universal formation-rule nonderivability theorem.
"""

from __future__ import annotations
from pathlib import Path
import numpy as np
from scipy.linalg import expm

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ("docs/MINIMAL_AXIOMS_2026-06-29.md",)

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
LIVE_MINIMAL_AXIOMS = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"


def check(name, condition, detail=""):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok); FAIL += int(not ok)
    print(f"  [{tag(ok)}] {name}" + (f"  ({detail})" if detail else ""))


def tag(ok):
    return "PASS" if ok else "FAIL"


SX = np.array([[0, 1], [1, 0]], complex)
SY = np.array([[0, -1j], [1j, 0]], complex)
SZ = np.array([[1, 0], [0, -1]], complex)
I2 = np.eye(2, dtype=complex)


def emb(op, k, n):
    m = np.array([[1]], complex)
    for i in range(n):
        m = np.kron(m, op if i == k else I2)
    return m


def coherence(state):
    r = state.reshape(2, -1)
    rho = r @ r.conj().T
    return abs(rho[0, 1])


def rounded(values):
    return [round(float(v), 3) for v in values]


def main() -> int:
    memo = LIVE_MINIMAL_AXIOMS.read_text(encoding="utf-8")
    operative = memo.split("## The Four Framework Axioms", 1)[1].split("## Qualification", 1)[0]
    print("=" * 78)
    print("Finite unitary controls and current-premise inventory; no general no-go")
    print("=" * 78)
    n = 4
    psi0 = np.array([1, 1], complex) / np.sqrt(2)
    for _ in range(n - 1):
        psi0 = np.kron(psi0, np.array([1, 0], complex))

    # ---- (0) live Record occurrence sentence ----
    print("\n-- live axiom-surface check --")
    check('(0) live MINIMAL_AXIOMS_2026-06-29.md contains the exact Record occurrence sentence "Records form."',
          "Records form." in operative)

    # ---- (1) H=0: no formation process/rate is read off from unitary dynamics ----
    print("\n-- unitary surfaces that do not supply the formation rule/process/state --")
    cohs0 = [coherence(expm(-1j * np.zeros((2 ** n, 2 ** n)) * t) @ psi0) for t in (1, 5, 20)]
    check("(1) H=0 (trivial dynamics): pointer coherence preserved (finite samples of the exact identity evolution)",
          all(abs(c - 0.5) < 1e-9 for c in cohs0), detail=f"coh(t=1,5,20) = {rounded(cohs0)}")

    # ---- (2) decoupled H != 0: no coupling/write rule is forced ----
    HS = emb(SX, 0, n)
    HE = sum(emb(SZ, k, n) for k in range(1, n))
    Hdec = HS + HE                                    # no S-E coupling term
    cohs_dec = [coherence(expm(-1j * Hdec * t) @ psi0) for t in (1, 5, 20)]
    check("(2) decoupled H = H_S(x)I + I(x)H_E with H != 0 (no coupling): coherence preserved for this supplied local eigenstate => "
          "no fragment writing in this finite fixture", all(abs(c - 0.5) < 1e-9 for c in cohs_dec),
          detail=f"coh(t=1,5,20) = {rounded(cohs_dec)}")

    # ---- (3) a coupled-H EIGENSTATE: stationary, no state-trigger rule ----
    Hc = HS + sum(emb(SZ, 0, n) @ emb(SX, k, n) for k in range(1, n))   # coupled H
    w, V = np.linalg.eigh(Hc)
    eig = V[:, 0]
    cohs_eig = [coherence(expm(-1j * Hc * t) @ eig) for t in (1, 5, 20)]
    check("(3) an eigenstate of any (even coupled) H is stationary => coherence frozen in the supplied unitary model",
          max(cohs_eig) - min(cohs_eig) < 1e-9)

    # ---- (4) contrast: a generic coupled H + non-eigenstate can decohere ----
    print("\n-- contrast: coupled non-eigenstate dynamics can decohere --")
    coh_coupled = coherence(expm(-1j * Hc * 3.0) @ psi0)
    check("(4) supplied coupled H reduces pointer coherence at this tested time; no asymptotic or framework formation claim",
          coh_coupled < 0.4, detail=f"coupled-H coherence = {coh_coupled:.3f}")

    # ---- (5) documentary consistency, not a logical independence proof ----
    normalized = " ".join(operative.split())
    distribution_clause = (
        "For each site, the probability distribution over the possibilities is "
        "determined by, and varies with, the nearest-neighbor conditions."
    )
    check("(5) documentary: Admissibility supplies a local distribution; unrecorded sites cannot be read",
          distribution_clause in normalized and "A site with no record cannot be read." in normalized)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: finite control or source-consistency check failed.")
        return 1
    print("Scope: four finite unitary controls and two documentary checks pass. "
          "These are not full framework countermodels or a physical formation theorem.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
