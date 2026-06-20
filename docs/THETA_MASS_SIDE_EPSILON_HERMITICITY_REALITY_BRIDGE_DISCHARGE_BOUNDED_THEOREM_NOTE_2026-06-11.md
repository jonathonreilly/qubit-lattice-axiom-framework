# The Mass-Side Strong-CP Phase Is Real on the Staggered Realization for Every Gauge Background: ε-Hermiticity Discharges the Determinant-Readout Bridge at the Bilinear Matter Level (Bounded Theorem)

**Date:** 2026-06-11 (SU(3) seeded-background verifier added
2026-06-18)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome, does not retire or re-grade any Tier-A
admission, and does not edit any audit data file.
**Primary runner:**
[`scripts/frontier_theta_mass_side_epsilon_hermiticity_reality_2026_06_11.py`](../scripts/frontier_theta_mass_side_epsilon_hermiticity_reality_2026_06_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_theta_mass_side_epsilon_hermiticity_reality_2026_06_11.txt`](../logs/runner-cache/frontier_theta_mass_side_epsilon_hermiticity_reality_2026_06_11.txt)
(SCORECARD: PASS=10, FAIL=0; deterministic, seeded backgrounds)

> **Not claimed:** retirement of the θ admission, a derivation of K-reality,
> any statement about the gauge-side residual `θ_gauge`, or any audit
> status. **Claimed (bounded):** at the bilinear matter level on the
> staggered realization, the determinant-readout bridge named open by
> [`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md)
> **discharges**: the matter measure's only partition-level phase object is
> `arg det` (first-power Berezin, reproven by explicit Grassmann
> expansion), and the exact identity `εMε = M† ⟹ det M ∈ ℝ` makes
> `det(D(U) + A)` **real for every unitary gauge background** in the
> enumerated ε-graded K-real bilinear coupling classes. On that bilinear
> determinant-readout surface, the mass-side strong-CP phase collapses to
> the orientation bit `{0, π}` *identically* — conditional on the
> K-reality premise, which is the same C₃ K-real structure as the
> `AC_φλ` reading selection.

## The named target

The 06-10 phase-erasure note closed the determinant *phase character*
inside the registrable multiplicative determinant class and named the
residual bridge: *"a later retained bridge must show that the physical
`arg det(M_u M_d)` contribution … is exhausted by this determinant-class
registrable readout, and that no phase-sensitive non-multiplicative or
action-level datum remains relevant to that premise."* The Tier-A
minimum-statement refinement carries this as the mass-side residual θ(b).
This note supplies the bilinear-matter-level half of that bridge, on the
realization surface rather than in a supplied readout context.

## The two exact mechanisms (runner, 10/10)

**Mechanism 1 — the measure has no other phase object.** The
single-pair-per-site Grassmann measure yields `Z = det(D + A)` to the
**first power**, computed by explicit exterior-algebra expansion with no
determinant identity assumed (check 1). At the bilinear level there is no
non-multiplicative matter datum: the only matter phase object that can
reach a partition-level readout is `arg det`. This is precisely the
"exhausted by the determinant class" half of the named bridge, derived
from the matter-statistics clause instead of supplied.

**Mechanism 2 — the determinant is real, for every gauge background.**
The identity chain is exact for any matrix: if `εMε = M†` then
`det M = det(εMε) = det(M†) = conj(det M)`, so `det M ∈ ℝ` (check 2). The
premise holds on the realization:

- the gauge-dressed staggered operator satisfies
  `εD(U)ε = −D(U) = D(U)†` for **every** unitary link configuration —
  verified on three U(1), two SU(2), and two SU(3) seeded backgrounds;
  the hop structure makes the argument gauge-group-independent
  (check 3);
- the enumerated **ε-graded K-real** bilinear coupling classes preserve
  the premise:
  real site-diagonal taste/generation channels (`m₀I + m₁ε + c_με_μ` —
  including the hw=1↔hw=2 mixing classes) and anti-Hermitian
  h.c.-paired one-link taste channels (the gauge-covariant kinetic-class
  dressing). Across 21 background × parameter combinations,
  `det(D(U)+A)` is real to `|Im det|/|det| < 5×10⁻¹⁶` (checks 4–5).

The exact classification (check 6): ε-**even** channels must be
Hermitian-real and ε-**odd** channels must be anti-Hermitian — the
realization form of the K-reality premise. Both violation classes are
computed to produce nonzero determinant phases: a complex site-diagonal
coefficient (K-reality broken; phase 2.97) and a Hermitian one-link
coupling (ε-grading pairing broken; phase 0.66) (checks 7–8). **Within
this bilinear channel classification, the mass-side phase enters through
ε-graded K-reality violation** — the gauge-dressed extension of the
count-twice localization pattern.

**Sign bookkeeping** (check 9): in the tested diagonal-dominant K-real
family the determinant is positive throughout (`arg det = 0`, not `π`) —
a family-bounded observation, not a theorem over all couplings; the
orientation bit remains the admitted residual.

## What this changes — θ(b) reduces to a shared premise plus one bit

After this block, the mass-side admitted content at the bilinear matter
level is exactly:

1. **the K-reality premise** — consumed, not derived; the *same* C₃
   K-real structure as `AC_φλ`'s reading selection (the cross-admission
   identification of
   [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md),
   now load-bearing); and
2. **the discrete orientation bit** (`0` vs `π`).

Unlike the prior selected-surface statement ("positive-real mass
orientation remains an explicit condition"), the reality itself is now a
*theorem of the realization for every gauge background*, not a condition:
no gauge configuration can generate a continuous mass-side phase through
the bilinear matter determinant. An elimination of the `AC_φλ` reading
selection would simultaneously move θ(b) — the two admissions' mass-side
content is one shared structure plus one bit.

## What this note does NOT claim

- **Not** a discharge of the gauge-side residual `θ_gauge`
  (winding/multi-plaquette account) — untouched.
- **Not** a derivation of K-reality — it is the consumed premise, Tier-A
  admitted content shared with `AC_φλ`.
- **Not** a claim beyond bilinear matter terms; interacting/beyond-
  bilinear contributions to the bridge remain open (declared residual).
- **Not** a construction of the gauge-covariant rotation-channel
  dressing (the ungauged rotation channel was treated in the 06-11
  channel-space work; its dressed form is a residual here).
- **Not** a sign theorem: positivity is reported for the tested family
  only; the orientation bit stays admitted.
- **No** PDG value, fitted selector, or empirical comparator anywhere.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
  (the matter-statistics clause and surface, at declared grade; §5
  residuals inherited)
- [`THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md`](THETA_P2_K_CPT_DETERMINANT_CHARACTER_PHASE_ERASURE_BOUNDED_NOTE_2026-06-10.md)
  (the named bridge this note half-discharges)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)
  (the θ̄ split and the cross-admission identification)
- [`STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md`](STRONG_CP_OPERATOR_BASIS_AND_MASS_ORIENTATION_THEOREM_NOTE_2026-05-19.md)
  (the prior selected-surface `{0, π}` collapse this note upgrades to a
  gauge-background-independent realization theorem)
- [`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`](CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md)
  (the K-reality selector consumed)
- Context, not load-bearing (plain text): the 06-11 koide
  stack (`KOIDE_STAGGERED_FIRST_ORDER_...`, `KOIDE_GENERATION_CHANNEL_
  SPACE_...`) and the landed Tier-A minimum-statement refinement, which
  record the ungauged localization pattern and the registry decomposition
  this block attacks.

## Reprove-and-cite ledger

- **Reproven here (runner):** the Berezin first-power identity (explicit
  Grassmann engine); the `det(M†) = conj det M` / `det(εMε) = det M`
  identity chain on a generic complex matrix; anti-Hermiticity and
  ε-oddness of `D(U)` on every tested background; the ε-graded K-real
  channel classification in both directions; reality across all tested
  background × channel combinations; both violation-class phases; the
  sign survey.
- **Cited at declared grade:** the matter-statistics clause; the 06-10
  bridge sentence (interface-pinned); the θ̄ split; the K-reality
  selector naming.

## Verification

```bash
python3 scripts/frontier_theta_mass_side_epsilon_hermiticity_reality_2026_06_11.py
```

Expected: 10 `[PASS]` lines, four `RESIDUAL (declared-open)` lines, then
`TOTAL: PASS=10 FAIL=0` and the verdict paragraph. Exit code 0 iff
FAIL=0. Deterministic (seeded backgrounds).

**Independent audit required.** This note asserts no effective-status
change.
