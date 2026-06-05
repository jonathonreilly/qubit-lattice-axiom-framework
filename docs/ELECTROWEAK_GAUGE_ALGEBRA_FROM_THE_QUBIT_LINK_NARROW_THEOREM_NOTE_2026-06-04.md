# The Electroweak Gauge Algebra su(2)⊕u(1) Is the Qubit-Link Connection Algebra (Narrow Theorem)

**Date:** 2026-06-04
**Type:** theorem (narrow)
**Claim type:** narrow theorem — the gauge **algebra** carried by a qubit-link connection is
exactly `u(2) = su(2) ⊕ u(1)`, the electroweak gauge algebra; and color `su(3)` is **structurally
absent** from a single qubit-link. The gauge **dynamics** (coupling, action), the **chiral** (L-only)
structure of SU(2)_L, the **hypercharge normalization**, and **color** are all separate/flagged.
**Claim scope:** the connection between two on-site qubits (`M₂(ℂ)`) is a unitary on `ℂ²`; its Lie
algebra is `u(2) = su(2) ⊕ u(1)`. The `su(2)` (`= Aut M₂(ℂ) = SO(3)`, state-action SU(2)) is the
**weak isospin** acting on the qubit **doublet**; the `u(1)` is the connection phase. Its gauge
invariance is the Record-grounded corollary (companion note: gauge invariance of observables follows
from `{Quantum, Locality, Record}`). **Color `su(3)` is not representable on a qubit** — the
traceless-Hermitian part of `M₂(ℂ)` is 3-dimensional (`= su(2)`); `su(3)` (dim 8) needs `M₃(ℂ)` (a
qutrit). So the framework's qubit-link gauge sector is **electroweak**, and **color is the honest gap.**
**actual_current_surface_status:** narrow theorem on the qubit-link connection algebra; standard Lie
algebra reproven from Pauli primitives. Not retained.
**bare_retained_allowed:** false
**Status:** independent audit required.
**Runner:** [`scripts/audit_companion_electroweak_algebra_from_qubit_link_exact.py`](./../scripts/audit_companion_electroweak_algebra_from_qubit_link_exact.py)

## Statement (reproven, numpy, 6/6)

1. The weak-isospin generators `T^a = σ^a/2` close as `su(2)`: `[T^a,T^b] = i ε^{abc} T^c`.
2. The connection phase `Y₀ = 𝟙/2` is central (`[Y₀, T^a] = 0`). So the qubit-link connection algebra
   is `su(2) ⊕ u(1) = u(2)` — the **electroweak gauge algebra**.
3. The qubit `ℂ²` is the `su(2)` **doublet** (fundamental): Casimir `= 3/4 = ½(½+1)` — weak isospin
   on a doublet, matching SU(2)_L acting on left-handed doublets.
4. The qubit connection algebra is `u(2)`, dim 4 = 3 (`su(2)`) + 1 (`u(1)`). `su(3)` (dim 8) is **not
   representable on `ℂ²`**.
5. **Color `su(3)` is structurally absent:** traceless-Hermitian `M₂(ℂ)` = dim 3 = `su(2)`; `su(3)`
   = dim 8 requires `M₃(ℂ)` (a qutrit per link). A qubit-link cannot carry color.
6. Gauge invariance under `su(2) ⊕ u(1)` is the Record-grounded observable algebra (companion note).

## Why this is the right gauge group, and where it stops

- **The electroweak group is what a qubit-link naturally carries.** A connection relates two `M₂(ℂ)`
  qubits; the unitaries doing that are `U(2)`, whose algebra is `su(2) ⊕ u(1)`. The framework does not
  *choose* the electroweak group — it is the gauge group of a connection between qubits. Combined with
  the companion result (gauge invariance from Record), the electroweak gauge **kinematics** —
  the group, its action on the doublet, and the gauge-invariance of observables — is grounded in
  `{Quantum, Locality, Record}` with no new axiom.
- **Color is the honest structural gap.** `su(3)` is not the automorphism algebra of a qubit; it needs
  a 3-dimensional internal space (a qutrit / `M₃(ℂ)`, or three rishons per link) that a single qubit
  does not contain. This is *why* the framework gives electroweak cleanly and color does not — a real,
  specific statement, not a hand-wave.

## What is NOT claimed (flags)

- **Algebra, not dynamics.** This is the gauge algebra and its action — the kinematics. The coupling,
  the action's gauge-invariance, gauge bosons, and any quantitative parameter (β=6, the weak coupling)
  are the **dynamics**, separate and still inputs.
- **Chirality not established here.** SM SU(2)_L is *chiral* (acts on left-handed only). The qubit-link
  `su(2)` acts on `ℂ²`; the *left-only* restriction needs the framework's chirality grading
  (`ε = (-1)^{x+y+z}`, the same η/ε structure as the Koide phase). Flagged, not derived here.
- **Hypercharge normalization not fixed.** The `u(1)` exists (the connection phase); identifying it
  with the SM hypercharge `Y` with the correct fractional assignments and the electroweak mixing is a
  separate input.
- **Color SU(3) is the gap** (needs a qutrit/rishon, not in a qubit).

## Trace gate

```yaml
trace_class: gauge_kinematics_from_axioms
target_blocker_text: "the SM gauge group is an input"
source_of_blocker_text: standard_model
reachability_to_target: derives the electroweak ALGEBRA (kinematics); color SU(3) is the structural gap
artifact_role: theorem
next_trace_action: "the chiral (L-only) restriction of SU(2)_L via the eps/eta grading -- the same chirality the Koide phase delta needs; and the color SU(3) qutrit/rishon structure (the gap)."
```

## Forbidden imports / reprove-and-cite

- The `u(2) = su(2)⊕u(1)` decomposition, the spin-½ Casimir, and `Der(M₂(ℂ)) = su(2)` are standard
  Lie theory, reproven from Pauli primitives. The electroweak group `SU(2)×U(1)` is cited as the
  comparator. No PDG values; no fitted parameters.

## Cross-references

- `GAUGE_INVARIANCE_OF_OBSERVABLES_COROLLARY_OF_THREE_AXIOMS_NARROW_THEOREM_NOTE_2026-06-04.md` (#2667)
  — the gauge invariance of observables, grounded in Record, that pairs with this gauge group.
