#!/usr/bin/env python3
"""Class-A verifier (narrow no-go): the current minimal axioms force generic
record occurrence through the Record sentence "Records form.", but they do not
force the formation rule/process/state/site/weight/rate.

MINIMAL_AXIOMS_2026-06-29, Record (verbatim): "Records form." The same memo
keeps record-production process and formation rules (which admissible
possibility a new record locks, at which site, with what weight, or at what
rate) outside axiom content.

Verifies the narrowed target:
  (0) the live memo contains the exact occurrence sentence "Records form.";
  (1) H=0 (trivial dynamics): pointer coherence is preserved for all times, so
      this unitary surface supplies no formation process/rate;
  (2) a decoupled H = H_S (x) I + I (x) H_E with H!=0 (no system-environment
      coupling): coherence is preserved, so no coupling/write rule is forced;
  (3) a Hamiltonian eigenstate is stationary, so no state-trigger rule is fixed
      by the Hamiltonian surface alone;
  (4) CONTRAST: a coupled H on a non-eigenstate decoheres in the toy model;
  (5) the logical reduction: occurrence is axiom content, but the concrete
      rule/process/state/site/weight/rate remains downstream.

No new axiom: Lattice, Qubit, Admissibility, and Record plus standard
finite-dimensional unitary evolution for the witness models. This no-go is
only on forcing the formation rule/process/state/site/weight/rate from the
minimal axioms.
"""

from __future__ import annotations
from pathlib import Path
import numpy as np
from scipy.linalg import expm

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
    print("=" * 78)
    print("NARROW NO-GO: occurrence is axiom content; formation rule/process/state/site/weight/rate is not  [class A]")
    print("=" * 78)
    n = 4
    psi0 = np.array([1, 1], complex) / np.sqrt(2)
    for _ in range(n - 1):
        psi0 = np.kron(psi0, np.array([1, 0], complex))

    # ---- (0) live Record occurrence sentence ----
    print("\n-- live axiom-surface check --")
    check('(0) live MINIMAL_AXIOMS_2026-06-29.md contains the exact Record occurrence sentence "Records form."',
          "Records form." in memo)

    # ---- (1) H=0: no formation process/rate is read off from unitary dynamics ----
    print("\n-- unitary surfaces that do not supply the formation rule/process/state --")
    cohs0 = [coherence(expm(-1j * np.zeros((2 ** n, 2 ** n)) * t) @ psi0) for t in (1, 5, 20)]
    check("(1) H=0 (trivial dynamics): pointer coherence preserved for all t => no formation process/rate is supplied by this unitary surface",
          all(abs(c - 0.5) < 1e-9 for c in cohs0), detail=f"coh(t=1,5,20) = {rounded(cohs0)}")

    # ---- (2) decoupled H != 0: no coupling/write rule is forced ----
    HS = emb(SX, 0, n)
    HE = sum(emb(SZ, k, n) for k in range(1, n))
    Hdec = HS + HE                                    # no S-E coupling term
    cohs_dec = [coherence(expm(-1j * Hdec * t) @ psi0) for t in (1, 5, 20)]
    check("(2) decoupled H = H_S(x)I + I(x)H_E with H != 0 (no coupling): coherence preserved => "
          "no site/write coupling rule is forced by non-trivial dynamics alone", all(abs(c - 0.5) < 1e-9 for c in cohs_dec),
          detail=f"coh(t=1,5,20) = {rounded(cohs_dec)}")

    # ---- (3) a coupled-H EIGENSTATE: stationary, no state-trigger rule ----
    Hc = HS + sum(emb(SZ, 0, n) @ emb(SX, k, n) for k in range(1, n))   # coupled H
    w, V = np.linalg.eigh(Hc)
    eig = V[:, 0]
    cohs_eig = [coherence(expm(-1j * Hc * t) @ eig) for t in (1, 5, 20)]
    check("(3) an eigenstate of any (even coupled) H is stationary => coherence frozen => no state-trigger formation rule is fixed by H alone",
          max(cohs_eig) - min(cohs_eig) < 1e-9)

    # ---- (4) contrast: a generic coupled H + non-eigenstate can decohere ----
    print("\n-- contrast: coupled non-eigenstate dynamics can decohere --")
    coh_coupled = coherence(expm(-1j * Hc * 3.0) @ psi0)
    check("(4) a generic coupled H on a non-eigenstate decoheres (companion contrast); (1)-(3) show the concrete formation mechanism is not forced by unitary structure alone",
          coh_coupled < 0.4, detail=f"coupled-H coherence = {coh_coupled:.3f}")

    # ---- (5) the reduction: occurrence is present; formation details remain downstream ----
    print("\n-- the no-go reduction --")
    occurrence_is_axiom_content = "Records form." in memo
    formation_rule_surface_outside = all(needle in memo for needle in (
        "formation rules (which",
        "which admissible possibility",
        "at which site",
        "with what weight",
        "at what rate",
    ))
    process_outside = "record-production process" in memo
    state_not_privileged = "A law privileges no states." in memo
    check("(5) current memo supplies occurrence but leaves formation rule/process/state/site/weight/rate outside axiom content",
          occurrence_is_axiom_content and formation_rule_surface_outside and process_outside and state_not_privileged)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: narrowed formation-rule no-go FAILED.")
        return 1
    print("VERDICT: the live Record axiom supplies generic occurrence via \"Records form.\", while "
          "formation rule/process/state/site/weight/rate remains unforced by the minimal axiom "
          "surface. The unitary checks preserve the old computations as process/rule negative "
          "controls, and the coupled non-eigenstate case remains contrast only.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
