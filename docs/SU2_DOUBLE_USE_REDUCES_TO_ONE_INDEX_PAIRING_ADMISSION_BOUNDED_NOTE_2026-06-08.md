---
claim_id: su2_double_use_reduces_to_one_index_pairing_admission_bounded_note_2026-06-08
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Internal/External su(2) Double-Use Reduces to One Index-Pairing Admission

**Date:** 2026-06-08
**Claim type:** bounded_theorem
**Scope:** conditional theorem plus admission-localization boundary.
**Primary runner:**
[`scripts/frontier_su2_double_use_reduces_to_pairing_admission_2026_06_08.py`](../scripts/frontier_su2_double_use_reduces_to_pairing_admission_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_su2_double_use_reduces_to_pairing_admission_2026_06_08.txt`](../logs/runner-cache/frontier_su2_double_use_reduces_to_pairing_admission_2026_06_08.txt)

## Question and verdict

Does {Lattice = `Z³` (`O_h` point group → emergent `SO(3)`), Quantum = `Cl(3,0)=M₂(ℂ)` per
site (the qubit; `σ_i` generate the **internal** `su(2)`), Record} **force** the per-site
internal `su(2)` to be the **external** spatial-rotation `su(2)` (the qubit doublet = physical
spin-½)?

**Verdict: no.** The double-use is neither an unconditional theorem nor a no-go.
It reduces to one index-pairing admission:

```text
The Clifford/derivative index μ of the dynamical (Kähler-/staggered-)Dirac
operator D = Σ_μ γ_μ ∂_μ is identified with the spatial lattice edge-direction
μ acted on by O_h.
```

with the clean dichotomy checked by the runner (**12/12**):

1. **Given the index-pairing admission, the identification is forced and tight**
   (a genuine conditional theorem).
2. **The index-pairing admission itself is not supplied by the axioms** — the
   qubit can genuinely *spectate*. Covariance *presupposes* the pairing; it
   does not deliver it.

## (1) Conditional theorem: given the pairing, the spin lift is forced

Given the `γ`-index = lattice-edge-index pairing, every proper `O_h` spatial
rotation `R` must be implemented on the per-site spinor by a spin lift, and:

- **The lift is inner (Skolem–Noether).** Every automorphism of `M₂(ℂ)` is inner; so the lift
  is a unitary `U_R ∈ M₂(ℂ)` with `U_R (σ·v) U_R† = σ·(Rv)`. The infinitesimal
  generators of these unitaries are **exactly `S_i = σ_i/2` — the per-site qubit's own
  `su(2)`**. Explicitly, closing the 90° generators yields the binary octahedral
  group `2O ⊂ SU(2)` (`|2O|=48`), whose `SU(2)→SO(3)` adjoint image is exactly the 24 proper
  `O_h` rotations — each `R` has an inner lift.
- **No spectator hatch at dim 2.** The commutant of `{σ_x,σ_y,σ_z}` in `M₂(ℂ)` is the scalars
  (runner C1), so the spin lift **cannot** act on a separate "spectator" factor inside the
  qubit — it must *be* the qubit's `su(2)`. A distinct spin factor would require
  `M₂(ℂ)⊗M₂(ℂ)` (dim 4), **violating the dim-2 Quantum axiom** (runner C2).

So **conditional on the index pairing and the dim-2 Quantum axiom, the external
spatial-rotation spin is forced to be the internal qubit `su(2)`
(`S_i=σ_i/2`), with no freedom.** This part is tight and runner-clean.

## (2) The pairing is not supplied by the axioms — the qubit can spectate

Without the index-pairing admission, nothing couples the qubit to spatial
structure:

- A **scalar `O_h`-invariant nearest-neighbour hop** `(hop on sites) ⊗ I` commutes with the
  internal `su(2)` `(I_sites ⊗ σ_i)` (runner D1) — the qubit is a spectator.
- The **8-site cube rotation is a factor-permutation** of sites (moves all 8; `P ≠ I`, runner
  D2) — the external rotation has a site-permutation part that **no one-site internal operator
  has**. Identifying the rotation's action *with* the internal `su(2)` is precisely the extra
  index-pairing datum.

So covariance **presupposes** the index pairing (the `γ`-edge hopping form)
rather than delivering it. The pairing is the
**(Kähler-/staggered-)Dirac realization gate**.

## No-go is refuted (the matched pair is globally consistent)

There is **no** representation-theoretic obstruction: the binary octahedral `2O ⊂ SU(2)`
double-covers `O ⊂ SO(3)` exactly (`48/24 = 2`, runner A3), the doublet is the spinor rep and
the vector is the adjoint, and the "`2π = −1`" sign is just the `Spin(3)→SO(3)` double cover —
not an obstruction. Identifying the two 3-spaces yields no contradiction. (Likewise, the
framework's live axiom memo does **not** assert a literal "algebra-3 ≠ spatial-3"
*contradiction*; it merely *declines* to supply a physical-observable bridge — a grantable
silence — which is exactly why the identification is an **admission**, not a no-go.)

## Residual (the minimal missing principle)

The only unsupplied hypothesis is the **index-pairing admission**. A future
result could promote this to "forced-modulo-covariance" *without a new axiom*
by proving a **lattice-native
`O_h`-Wigner-covariance lemma that derives the `γ_μ ↔ e_μ` edge-pairing from {Lattice,
Quantum, Record} without presupposing the `γ`-edge hopping form.** None exists in the repo,
and the pairing is the staggered/Kähler-Dirac realization gate, which itself
carries three further named-open admissions
(`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06`): FS fermionic
statistics, the Euclidean signature/time import, and the chirality selector
`ε(x)`.
The directly-analogous **boost-level** question is already a landed `retained_no_go`
(`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02`).

## Downstream impact

- **Dirac–Weyl physical-spin label** (`DIRAC_WEYL_FERMION_DOF_FROM_LORENTZ_AND_CHIRALITY…`,
  `audited_conditional`): its named-open "identify the framework SU(2) doublet with the
  physical spin/helicity label" bridge is exactly this index-pairing
  admission. This note pins that gap to the pairing and the forced-given-pairing
  conditional, rather than leaving it as a vague label admission.
- **Emergent Lorentz:** the continuum upgrade of this discrete spin link is the boost-spinor
  link, the single non-tight link; so even given the index pairing, relativistic
  spin covariance is a *separate* conditional, never closed from the axioms
  alone.
- **Spin-statistics:** the Finkelstein–Rubinstein rotation→exchange bridge fails on discrete
  `Z³` (no continuous `π₁(SO(3))=Z₂`), so the `2π=−1` on-site sign does **not** force CAR; FS
  stays forced-modulo {emergent Lorentz + Record}.
- **d=3 picture — unchanged and protected:** `d=3` remains a `Z³` lattice **primitive**
  (`Cl(3)⊗Z³`); the `M₂(ℂ)=Cl(3,0)=GA(3)` match is a **consistency, not a derivation**
  (#2559 closed). This note does **not** relocate `d=3` onto the matter/Dirac dynamics (the
  #2586-closed backwards move).

## Reprove-and-cite

Reproven from primitives in the runner (numpy, 12/12): the `2O→O` double cover (matched pair,
no-go refuted); every proper `O_h` rotation has an inner `M₂(ℂ)` lift with generators `σ_i/2`
(Skolem–Noether); the Pauli commutant = scalars (no dim-2 spectator); the scalar-hop spectator
and the 8-site cube-permutation separation (pairing unsupplied).
**Comparators / landed cites only** (never used to *supply* the pairing):
Skolem–Noether, the `SU(2)→SO(3)` double cover, the merger note's reading rule,
the boost-faith no-go. No PDG values.

## What this note does NOT claim (do-not-rewalk guards)

- It does **not** claim the internal `su(2)` *is* the external rotation `su(2)`
  unconditionally — only forced given the index-pairing admission.
- It does **not** force the pairing from the matched `3=3` count (`Cl(3,0)=M₂(ℂ)=GA(3)` vs `Z³`): that
  is the #2559-closed matched-pair **consistency**, ruled *not* a derivation by the d=3 panel;
  reusing it to force the pairing is the panel-flagged **inversion**.
- It does **not** cite `INTERNAL_EXTERNAL_SU2_MERGER` (273/273) or the `Cl(3) O_h` cubic-lift
  to *supply* the pairing: those prove only **well-definedness given the
  pairing** (the merger's reading rule forbids lattice/translation/scale use);
  citing them to force the pairing is exactly the "runner-passes-a-refuted-claim"
  failure mode.
- It does **not** pursue the no-go (refuted on all angles), and does **not** relocate `d=3`.
- **No** new axiom, primitive, or repo vocabulary; no PDG input; sets no audit status.

## Audit dependency links

These links make the boundary visible to the audit graph. They do not supply
the index-pairing admission.

- Baseline axioms: [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md).
- Staggered realization residuals: [`STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md`](STAGGERED_DIRAC_EXERCISE_HONEST_REASSESSMENT_NOTE_2026-06-06.md).
- Boost-level no-go comparator: [`QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md`](QUANTUM_LOCAL_ALGEBRA_DOES_NOT_FORCE_BOOST_ACTION_FAITH_NO_GO_NOTE_2026-06-02.md).
- Guardrail comparators only: [`INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md`](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md) and [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md).

**Independent audit required.** This note asserts no effective-status change.
