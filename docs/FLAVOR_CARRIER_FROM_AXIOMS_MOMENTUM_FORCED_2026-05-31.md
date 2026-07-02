# Flavor carrier from framework baseline up: the momentum-factor carrier TYPE is FORCED; the hw=1 triplet LOCUS reduces to the one chiral operator-class import (the framework's recurring chirality gate); r=1/2 stays a separate input

**Date:** 2026-05-31
**Claim type:** open_gate / conditional integration map
**Claim boundary:** parent conditional integration map. The clean Layer-A carrier-type
theorem is split out to
[`FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md).
This parent keeps the broader package: Layer A support, the open Layer-B
physical `hw=1` locus bridge, the separate `r=1/2` input, and the separate
readout-class input. Not a full closure and not a retained-status proposal.
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Runner:** `scripts/flavor_carrier_from_axioms_momentum_forced_2026_05_31.py` (SCORECARD PASS=16 FAIL=0 after the parent-boundary checks).
**Source:** workflow `wf_de220c3f-291` — 6 axioms-up routes + 3-lens adversarial verification + synthesis (25 agents). Directive: derive the carrier from framework baseline up, ledger status set aside.

**Post-audit split (2026-06-15).** The clean carrier-type theorem is
now extracted as
[`FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md).
This parent note remains the combined conditional packet for the physical
`hw=1` locus bridge, the `r=1/2` input, and the readout-class input. The split
does not apply an audit verdict; independent audit owns any status change.

## 2026-06-18 parent-boundary repair

This source repair makes the parent/split boundary explicit:

- cite
  [`FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md`](FLAVOR_CARRIER_MOMENTUM_TYPE_FROM_TRANSLATION_THEOREM_NOTE_2026-06-15.md)
  for the clean Layer-A theorem that translation symmetry forces
  flavor-separating observables onto the momentum/BZ factor rather than
  position-diagonal local readouts;
- cite this parent only for the combined conditional packet that also names
  the still-open physical `hw=1` locus bridge, the `r=1/2` input, and the
  index/readout-class input;
- do not use this parent as a standalone closure of the physical generation
  carrier;
- re-audit this parent as a full package only after a separate theorem forces
  the staggered/KS `hw=1` physical locus from baseline and closes the
  `r=1/2` and readout selections.

No audit verdict, ledger status, publication status, or repo-wide authority
surface is changed by this source-side repair.

## Question
The carrier sub-claim is: the physical charged-lepton flavor observable lives on the intrinsic
generation factor (the C₃ orbit of the hw=1 BZ corners, read as the intensive index density δ=2/9),
not the Γ₅-graded extensive position-space lattice index. The prior note showed position-locality is
generation-blind, so a *momentum/spectral* principle is required. **Can that principle — and the carrier
— be built from framework baseline up?**

## Verdict: Layer A is delegated to the split theorem; the parent remains conditional

The result splits cleanly into two layers, and the adversarial verification is internally consistent on
which layer survives (the "lands-on-momentum-factor" lens upheld Layer A for **all six** routes, 0
refutations; the "genuinely-from-A1A2" and circularity lenses refuted the Layer-B over-claims).

### LAYER A — the carrier TYPE (momentum, not position) is DERIVED from framework baseline (the genuine advance)
- **A1** gives the Hilbert space `⊗_{x∈Z³} M₂(ℂ)` with three commuting translation unitaries `T_x,T_y,T_z`.
- **A2** (locality) forces a translation-invariant local `H_dyn` with `[H_dyn, T_μ] = 0`; emergent time
  gives it a spectrum and a propagator `G(ω,k)=1/(ω−H(k))`.
- The **spectral theorem for the commuting normal family** `{T_x,T_y,T_z}` then forces a *basis-independent*
  joint spectral decomposition over the Pontryagin dual `Ẑ³ = T³` (the Brillouin zone) — **no choice**.
- **Generation-blind trap cleared (verified):** a local per-site observable has identical expectation
  across all three generations (runner A3: `⟨P_site0⟩ = 1/8` for each), while a flavor-*separating*
  observable is necessarily a non-local **momentum-block / corner-projector** (runner A3: `⟨P_k0⟩ =
  (1,0,0)`). The `Γ₅=(−1)^{x+y+z}` extensive position index sums to 0 on the torus (runner A4) — a
  bulk/off-shell total, disqualified as a single-particle observable.

**So the carrier is the momentum factor as a theorem of A2.** The position-vs-momentum question — the
half of the carrier that looked like a free choice — is *dissolved*. This is the substantive new content.

### LAYER B — which momentum LOCUS is "the species" (hw=1 triplet) needs one named import
A2 yields *some* translation-invariant local `H_dyn` whose spectrum is BZ-graded, but it does **not**
single out the regulator that places exactly three poles at the hw=1 corners. Verified counterfactuals:
- the naive/first-order dispersion `|D|²=Σ sin²(k_μ)` has its zero locus on **all 8** corners `{0,π}³`,
  Hamming-graded `(1,3,3,1)` (runner B1) — hw=1 is a single C₃ orbit but is *not* singled out by the
  dispersion alone;
- a **Wilson / second-difference** operator puts its distinguished massless mode at **hw=0** (mass
  staircase `0,2r,4r,6r`, runner B2) — not hw=1.

Singling out the hw=1 C₃ triplet requires the **staggered / Kawamoto-Smit first-order CHIRAL operator** =
single-mode Grassmann fermionization of the `M₂(ℂ)` qubit **+** chiral anticommutation `{ε,D}=0` (`ε=(−1)^{x+y+z}`).
The current qubit substrate supplies a **bosonic** qubit; these are *premises*
([`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md),
premise table BlockT1 + `{ε,D}=0`; the note is conditional, its own discriminator calls fermionization
"compatibility, not forcing"). So the locus is a **genuine import**, not definitional.

**The consolidation:** this import — the C₃-orbit-splitting chiral grading on the generation factor — is
the same named chirality-gate family tracked by
[`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md)
and the scope-limited
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md).
So the carrier *locus* is gate-aligned with the one recurring chirality import
family the flavor sector already isolates. This is a bookkeeping
consolidation, not a proof that the physical generation bridge has closed and
not a removal of the locus premise.

(Note: "physical species = propagator poles / band-degeneracies" is *near-definitional* once you have a
propagator — granting it changes nothing; it only labels *which* momenta in T³ are species. The genuine
import is the *operator class* that fixes the pole locus, not the pole reading.)

### BASEPOINT r=1/2 — a separate continuous input
The discrete pole/corner structure fixes only `δ=2/9` (the equivariant-η / Atiyah-Bott density
`L₃(1,2)=2/9`, retaining the index apparatus — distinct from the bare doublet character `ω+ω²=−1`, runner
C1). It says nothing about the **continuous** Yukawa modulus `r=|b|²/a²`: for `F=aI+b(J−I)`, the runner
derives `Tr F = 3a`, `Tr F² = 3a²+6b²`, hence
`Q(F)=Tr(F²)/(Tr F)² = 1/3+(2/3)r` (runner D1). Thus `r=1/2 ⟺ Q=2/3` is a separate specialization
(runner D2). `r=1/2` (tied to the signed/√m-sign readout class) remains a genuine continuous input,
orthogonal to carrier selection.

## Net standing of the charged-lepton flavor inputs (after this attack)
1. **Carrier TYPE = momentum factor** — **DERIVED** from framework baseline (spectral theorem on commuting translations).
2. **Carrier LOCUS = hw=1 triplet** — reduces to the **chiral operator-class import** (staggered/KS;
   single-mode Grassmann + `{ε,D}=0`), which is gate-aligned with the framework's recurring generation-ID /
   `Q=2/3` chirality family. This remains an open physical-locus bridge.
3. **Basepoint r=1/2** — a separate continuous Yukawa input.
4. **Readout-class** (retain the index density over the bare character to land δ=2/9, not −1) — a separate
   selection, consistent with the index/η signpost.

This is the campaign's strongest consolidation, but this parent remains a
conditional packet. The clean carrier-type theorem is the 2026-06-15 split
note. Half of the carrier problem (momentum type) is a theorem; the other half
(physical `hw=1` locus) is the same chirality import the rest of the flavor
sector pays for once. What remains genuinely free is the continuous `r=1/2`
and the readout class. Per standing practice, the chirality import is a
`gate`, not an airtight impossibility: the open physics question is whether a
first-order chiral Dirac operator with hw=1 zero-modes can be forced from the
bosonic `M₂(ℂ)` qubit (the single-mode-Grassmann/`{ε,D}=0` premises), which
is the one lever that would also discharge generation-ID and `Q=2/3`
simultaneously.

## Provenance (verified 2026-05-31; derivation stands on framework baseline, ledger status non-constraining per directive)
- Layer A is a direct framework baseline + spectral-theorem construction (no note authority needed).
- The Layer-B import premises are sourced to
  [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
  (premise table BlockT1 + `{ε,D}=0`; conditional). The coinciding chirality gate is the one named in
  [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  (ratified bounded-surface context) and
  [`KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`](KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md).
- `δ=2/9` = `L₃(1,2)` equivariant-η density (verified ≠ bare character −1). `Q(F)=1/3+(2/3)r`
  is derived from `F=aI+b(J-I)`, and `r=1/2` is free (verified).
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
