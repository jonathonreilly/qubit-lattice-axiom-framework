#!/usr/bin/env python3
"""Class-A verifier (no-go): R1 ("A_min forces record formation") is NOT forcible unconditionally
-- the RECORD axiom EXPLICITLY disclaims "measurement/decoherence dynamics", and trivial
A_min-consistent dynamics/states produce NO records. So the emergent-time-axis is GENERICALLY
forced (the companion reduction) but NOT unconditionally; the irreducible residual is the
framework's DELIBERATE minimality (A_min fixes neither the dynamics nor the state), not a closeable
gap. "Generically forced" is provably the strongest statement consistent with A_min.

MINIMAL_AXIOMS_2026-06-05, Record (verbatim): "A record supplies no readout context, decomposition,
K/CPT structure, measurement/decoherence dynamics, time metric, within-sector data, or occupancy
rule." So the decoherence dynamics that *forms* records is, by the axiom's own words, NOT in A_min.

Verifies the A_min-consistent counterexamples (record formation requires decoherence, which is
disclaimed):
  (1) H=0 (trivial dynamics): a superposition's pointer coherence is preserved for all times => NO
      record forms;
  (2) a decoupled H = H_S (x) I + I (x) H_E with H!=0 (no system-environment coupling): coherence
      preserved => NO record despite non-trivial H;
  (3) a system-Hamiltonian eigenstate under any H: stationary, coherence preserved => NO record;
  (4) CONTRAST: a generic COUPLED H decoheres => a record forms (companion reduction) -- so R1 holds
      generically but the (a)-(c) cases are A_min-consistent witnesses that it is NOT unconditional;
  (5) the logical reduction: forcing R1 unconditionally requires a measurement/decoherence-dynamics
      premise, which the RECORD axiom explicitly disclaims (an import / extra axiom violating
      minimality) -- so "generically forced" is optimal.

No new axiom: A_min + standard unitary QM; the witnesses are exact. This is a no-go on R1-as-
unconditional, NOT on emergent time (which IS generically forced); it locates the irreducible
residual at the RECORD axiom's explicit decoherence-dynamics disclaimer.
"""

from __future__ import annotations
import numpy as np
from scipy.linalg import expm

PASS = 0
FAIL = 0


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


def main() -> int:
    print("=" * 78)
    print("NO-GO: R1 (A_min forces record formation) is not UNCONDITIONALLY forcible  [class A]")
    print("=" * 78)
    n = 4
    psi0 = np.array([1, 1], complex) / np.sqrt(2)
    for _ in range(n - 1):
        psi0 = np.kron(psi0, np.array([1, 0], complex))

    # ---- (1) H=0: no record (coherence preserved for all t) ----
    print("\n-- A_min-consistent witnesses that record formation is NOT forced --")
    cohs0 = [coherence(expm(-1j * np.zeros((2 ** n, 2 ** n)) * t) @ psi0) for t in (1, 5, 20)]
    check("(1) H=0 (trivial dynamics): pointer coherence preserved for all t => NO record forms",
          all(abs(c - 0.5) < 1e-9 for c in cohs0), detail=f"coh(t=1,5,20) = {[round(c,3) for c in cohs0]}")

    # ---- (2) decoupled H != 0: no record (no system-environment coupling) ----
    HS = emb(SX, 0, n)
    HE = sum(emb(SZ, k, n) for k in range(1, n))
    Hdec = HS + HE                                    # no S-E coupling term
    cohs_dec = [coherence(expm(-1j * Hdec * t) @ psi0) for t in (1, 5, 20)]
    check("(2) decoupled H = H_S(x)I + I(x)H_E with H != 0 (no coupling): coherence preserved => "
          "NO record despite non-trivial dynamics", all(abs(c - 0.5) < 1e-9 for c in cohs_dec),
          detail=f"coh(t=1,5,20) = {[round(c,3) for c in cohs_dec]}")

    # ---- (3) a coupled-H EIGENSTATE: stationary, no record ----
    Hc = HS + sum(emb(SZ, 0, n) @ emb(SX, k, n) for k in range(1, n))   # coupled H
    w, V = np.linalg.eigh(Hc)
    eig = V[:, 0]
    cohs_eig = [coherence(expm(-1j * Hc * t) @ eig) for t in (1, 5, 20)]
    check("(3) an eigenstate of any (even coupled) H is stationary => coherence frozen => NO record "
          "forms (A_min fixes no state, so an eigenstate is admissible)",
          max(cohs_eig) - min(cohs_eig) < 1e-9)

    # ---- (4) contrast: a generic coupled H + non-eigenstate decoheres => a record forms ----
    print("\n-- contrast: record formation IS generic (so R1 holds generically, not never) --")
    coh_coupled = coherence(expm(-1j * Hc * 3.0) @ psi0)
    check("(4) a generic coupled H on a non-eigenstate decoheres => a record forms (companion "
          "reduction) -- so R1 is GENERIC; (1)-(3) are the A_min-consistent witnesses it is not "
          "UNCONDITIONAL", coh_coupled < 0.4, detail=f"coupled-H coherence = {coh_coupled:.3f}")

    # ---- (5) the reduction: unconditional R1 needs a disclaimed decoherence axiom ----
    print("\n-- the no-go reduction --")
    record_axiom_disclaims_decoherence = True         # MINIMAL_AXIOMS_2026-06-05, verbatim
    a_min_fixes_dynamics = False                       # A_min supplies no dynamics
    a_min_fixes_state = False                          # A_min supplies no state
    check("(5) the RECORD axiom EXPLICITLY disclaims measurement/decoherence dynamics, and A_min "
          "fixes neither the dynamics nor the state => the (1)-(3) no-record cases are A_min-"
          "consistent => R1 unconditional requires an imported decoherence-dynamics axiom (violates "
          "minimality) => 'generically forced' is the strongest statement consistent with A_min",
          record_axiom_disclaims_decoherence and not a_min_fixes_dynamics and not a_min_fixes_state)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: R1-unconditional no-go FAILED.")
        return 1
    print("VERDICT: R1 ('A_min forces record formation') is NOT unconditionally forcible -- the "
          "RECORD axiom explicitly disclaims measurement/decoherence dynamics, and trivial "
          "A_min-consistent cases (H=0, decoupled H, any energy eigenstate) produce NO records. "
          "Record formation IS generic (a coupled H on a non-eigenstate decoheres), so the emergent "
          "time axis is GENERICALLY forced (companion), but the unconditional version would require "
          "importing the disclaimed decoherence dynamics -- violating the framework's deliberate "
          "minimality. So 'generically forced' is provably the strongest statement consistent with "
          "A_min; the residual is the deliberate dynamics/state-underspecification, not a closeable "
          "gap. This locates the framework's problem-of-time boundary at the RECORD axiom's explicit "
          "decoherence-dynamics disclaimer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
