# Direction α — First Cycle Result: Verified Retained Decoherence Slice Does Not Constrain the Generation-Sector Phase δ

**Date:** 2026-05-26
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Type:** research-cycle analysis note (sector-mismatch finding)
**Status:** not a theorem note; not a no-go claim; **a negative attack-surface
finding** — the verified retained decoherence subset of Chain 5 is silent on
the generation-sector phase δ, so direction α with that subset alone cannot
constrain δ.
**Imports:** NONE (uses only `origin/main` retained content + standard math).

## Question

Given the strict constraint of this lane (A1+A2 + verified retained inventory
only), can the verified retained slice of native dynamics — specifically the
two decoherence `retained_bounded` results

- `DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md` (claim_type `bounded_theorem`,
  effective_status `retained_bounded` per `audit_ledger.json` on `origin/main`),
- `DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17.md`
  (same)

— constrain the C₃-azimuthal phase `δ` that appears in the Brannen circulant
formula `m_k² ∝ (1 + √2·cos(2πk/3 + δ))²` (retained kinematic shape per
`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`)?

## Reading the retained decoherence results

### Decoherence action independence

The retained content is a **spatial 3D `1/L²` lattice replay** finding: for
two specific action laws

```
spent_delay(L, f_bar)    :=  L*(1 + f_bar) - sqrt(max((L*(1+f_bar))² - L², 0)),
valley_linear(L, f_bar)  :=  L*(1 − f_bar),
```

the decoherence observables (d_TV, MI, CL bath purity, S_norm) are **exactly
identical** across the two actions at every tested lattice spacing in the
`1/L²` replay. The Pattern-A narrow rescope (the zero-field phase-equality
theorem note) isolates the load-bearing algebraic step: at `f_bar = 0`,

```
spent_delay(L, 0)  =  L,
valley_linear(L, 0)  =  L,
exp(i*k*spent_delay(L, 0))  =  exp(i*k*valley_linear(L, 0))  =  exp(i*k*L).
```

This is a statement about **per-link, per-link-length, zero-field spatial
phase factors** in a 3D propagation lattice. The phase `exp(i*k*L)` is the
single-link complex phase factor used in the propagation accumulation.

### What this constrains

- A spatial per-link phase parameter `k*L` at zero field is identical for
  both action laws.
- The 3D lattice propagation observables agree between the two action laws.
- This is *action independence* (within the equivalence class of these two
  specific laws), not action *determination*.

### What this does NOT constrain

The C₃ generation triplet's azimuthal phase `δ` lives in the **generation
sector**, not the spatial-link sector. The retained Brannen circulant
(Chain 1, dependency map) gives `m_k² ∝ (1 + √2·cos(2πk/3 + δ))²` where:

- `k ∈ {0, 1, 2}` is the C₃ irrep label (not a spatial wavevector or
  link-length).
- `δ` is the offset from the C₃-symmetric point in the azimuthal angular
  parameter on the C₃ orbit — *not* a per-link spatial phase.

The two phases (`exp(i*k*L)` spatial, `δ` generation-sector) live in
**different sectors** of the framework's algebra. The retained decoherence
results describe a sector-internal property of the spatial sector at zero
field; they do not provide a coupling between sectors that would let
spatial-link dynamics constrain a generation-sector parameter.

## Sector-mismatch result

The verified retained decoherence slice of Chain 5 **does not constrain the
generation-sector phase δ**.

This is **not a no-go**: it does not claim that decoherence dynamics cannot
fix `δ`. It claims only that the **currently-verified retained subset** of
decoherence content does not provide a constraint on `δ`, because the
retained content's load-bearing claim is about spatial-link phases in a
specific zero-field 3D lattice replay, not about the generation sector.

## What's needed to attack δ natively

For Direction α to constrain `δ`, the lane needs **either**:

1. **A retained native-dynamics result that couples the spatial sector to
   the generation sector** — e.g. a "flavor-tagged Wilson line" result, a
   "C₃-equivariant decoherence" result, or a "generation-sector decoherence
   bath" result. Such results may exist in the broader native dynamics
   chain memory claims to be retained (Brannen CH closure, corrected
   propagator) but those pieces are currently unverified on `origin/main`
   per the lane's Chain 5 verification cycle.

2. **A retained native-dynamics result that operates directly in the
   generation sector** — e.g. a C₃-symmetry-breaking decoherence
   mechanism that picks out a specific azimuthal angle. No such result is
   currently surfaced by the lane's verification queries.

3. **A purely kinematic argument** — fix `δ` from the C₃ + Cl(3) +
   character-algebra structure alone, with no dynamics input. Per the
   dependency map (Chain 4c) this hits the radian-bridge primitive `P`
   which is open (six prior retained no-gos).

## Implications for the lane

The verified retained surface is **insufficient** for Direction α as
originally framed. Three productive pivots remain within the lane's
constraints:

- **α'** — complete the Chain 5 verification (locate Brannen-CH, corrected
  propagator, lattice-growth-with-decoherence on `origin/main`). If any of
  these surface as retained, re-attempt Direction α with the expanded
  verified subset.
- **γ** — pivot to native isolation of the π-bridge gap: characterize the
  exact structural input that would close `P`, using only the retained
  no-go inventory + standard math. (No δ-value derivation attempted; just
  a sharpened residual.)
- **δ** — entirely new direction: investigate whether `δ` is determined by
  a **kinematic boundary condition** rather than dynamics. The Brannen
  formula gives the mass observable shape; a boundary condition (e.g.
  matching at a C₃-orbit closure point, or a Cl(3) eigenstate selection
  rule) might bind `δ` without invoking dynamics. This is purely retained
  (boundary-condition reading of existing C₃ + Cl(3) retained content).

## Cited retained sources (load-bearing)

- `DECOHERENCE_ACTION_INDEPENDENCE_NOTE.md` (retained_bounded; bounded_theorem)
- `DECOHERENCE_ACTION_ZERO_FIELD_PER_LINK_PHASE_EQUALITY_NARROW_THEOREM_NOTE_2026-05-17.md`
  (retained_bounded; bounded_theorem)
- `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` (provenance for
  the Brannen circulant `cos(2πk/3 + δ)` kinematic shape)

## What this cycle does NOT claim

- Does **not** claim that no native dynamics can constrain `δ`.
- Does **not** claim that decoherence dynamics is fundamentally incompatible
  with generation-sector phase determination — only that the verified
  retained slice doesn't include the coupling.
- Does **not** propose a new axiom or import.
- Does **not** open a source PR (the analysis is research-lane internal).
- Does **not** assert any audit status.

## Next exact action

Per the opportunity-queue ranking, proceed in subsequent cycles with α'
(Chain 5 verification completion) and/or γ (native isolation of the
π-bridge gap), and/or δ (boundary-condition reading) as alternative
attack vectors. Each is bounded by the same lane charter constraints.
