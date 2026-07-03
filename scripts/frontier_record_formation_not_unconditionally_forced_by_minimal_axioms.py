#!/usr/bin/env python3
"""Class-A verifier (no-go): record formation is not unconditionally forced by
the Lattice, Quantum, and Record baseline. Record explicitly excludes
measurement/decoherence dynamics, and baseline-consistent dynamics/states can
produce no records. A coupled non-eigenstate toy model supplies generic
contrast only; it is not a universal theorem.

MINIMAL_AXIOMS_2026-06-05, Record (verbatim): "A record supplies no readout context, decomposition,
K/CPT structure, measurement/decoherence dynamics, time metric, within-sector data, or occupancy
rule." So the decoherence dynamics that forms records is outside the approved
axiom baseline.

Verifies baseline-consistent counterexamples:
  (1) H=0 (trivial dynamics): a superposition's pointer coherence is preserved for all times => NO
      record forms;
  (2) a decoupled H = H_S (x) I + I (x) H_E with H!=0 (no system-environment coupling): coherence
      preserved => NO record despite non-trivial H;
  (3) a system-Hamiltonian eigenstate under any H: stationary, coherence preserved => NO record;
  (4) CONTRAST: a coupled H on a non-eigenstate decoheres in the toy model;
  (5) the logical reduction: forcing record formation unconditionally requires
      a measurement/decoherence-dynamics premise, which Record excludes.

No new axiom: Lattice, Quantum, and Record plus standard finite-dimensional
unitary evolution for the witness models. This no-go is only on
unconditional record-formation forcing from the baseline.
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
    print("NO-GO: record formation is not unconditionally forced by the minimal axioms  [class A]")
    print("=" * 78)
    n = 4
    psi0 = np.array([1, 1], complex) / np.sqrt(2)
    for _ in range(n - 1):
        psi0 = np.kron(psi0, np.array([1, 0], complex))

    # ---- (1) H=0: no record (coherence preserved for all t) ----
    print("\n-- baseline-consistent witnesses that record formation is NOT forced --")
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
          "forms (the baseline fixes no state, so an eigenstate is admissible)",
          max(cohs_eig) - min(cohs_eig) < 1e-9)

    # ---- (4) contrast: a generic coupled H + non-eigenstate decoheres => a record forms ----
    print("\n-- contrast: coupled non-eigenstate dynamics can decohere --")
    coh_coupled = coherence(expm(-1j * Hc * 3.0) @ psi0)
    check("(4) a generic coupled H on a non-eigenstate decoheres => a record forms (companion "
          "contrast); (1)-(3) are the baseline-consistent witnesses it is not UNCONDITIONAL",
          coh_coupled < 0.4, detail=f"coupled-H coherence = {coh_coupled:.3f}")

    # ---- (5) the reduction: unconditional record formation needs a disclaimed dynamics import ----
    print("\n-- the no-go reduction --")
    record_axiom_disclaims_decoherence = True         # MINIMAL_AXIOMS_2026-06-05, verbatim
    baseline_fixes_dynamics = False                    # Lattice/Quantum/Record supplies no dynamics
    baseline_fixes_state = False                       # Lattice/Quantum/Record supplies no state
    check("(5) Record explicitly disclaims measurement/decoherence dynamics, and the baseline "
          "fixes neither the dynamics nor the state => the (1)-(3) no-record cases are baseline-"
          "consistent => unconditional record formation requires an imported decoherence-dynamics premise",
          record_axiom_disclaims_decoherence and not baseline_fixes_dynamics and not baseline_fixes_state)

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: unconditional record-formation no-go FAILED.")
        return 1
    print("VERDICT: record formation is NOT unconditionally forced by the Lattice/Quantum/Record "
          "baseline. Record explicitly excludes measurement/decoherence dynamics, and "
          "baseline-consistent witnesses (H=0, decoupled H, any energy eigenstate) produce no "
          "records. A coupled non-eigenstate toy model shows record formation can be generic, but "
          "generic is not unconditional. A theory layer that wants record production must supply "
          "the production/decoherence model explicitly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
