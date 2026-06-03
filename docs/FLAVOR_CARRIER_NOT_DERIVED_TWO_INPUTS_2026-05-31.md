# Flavor — carrier-derivation attempt FAILS: 2/9 is an index/eta object (not a finite-rep character), the retained theorems bracket species→flavor as out-of-scope; TWO independent flavor inputs remain

**Date:** 2026-05-31
**Claim type:** bounded_theorem
**Claim boundary:** bounded negative (a refuted derivation lead) + an honest input-count refinement. Not a closure; not an import.
**Runner:** `scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py` (SCORECARD 6/6).
**Source:** workflow `wf_26eb7111-7e7` — 6 attack routes + 3-lens adversarial verification + synthesis (25 agents). All 6 attackers claimed the carrier was *derived*; adversarial verification refuted **every** one (survivors: none).

## Question
Can the carrier sub-claim be *derived* — "the physical charged-lepton flavor observable lives on the
intrinsic finite generation rep R³ (the momentum-corner module), **not** the Γ₅-graded extensive
position-space lattice index" — from retained `three_generation_observable`? And is the basepoint
`r=1/2` separately derivable or the irreducible input? (Targeting the single premise that the prior
`FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION` note had reduced everything to.)

## Verdict: carrier NOT derived; basepoint irreducible; TWO independent inputs remain

The momentum-corner "category-error" lead — that 2/9 is a *bare character* on the finite 3-corner rep,
needing no manifold, so the extensive-lattice framing is a conflation — **does not survive**. It fails
for a decisive, verified reason, and the carrier reduces to an *existing open gate*, not to the count.

### (A) The killer numeric — 2/9 is an index/eta object, not a representation character
The lead's whole force was "compute 2/9 on the finite corner rep, no position-space manifold." But:
- the **bare doublet character** is `tr(g|doublet) = ω + ω² = −1` (full R³ char `1+ω+ω² = 0`, singlet `= 1`);
- **none of these is 2/9.** `2/9 = L₃(1,2) = (1/3) Σ_{k=1,2} 1/((ωᵏ−1)(ω²ᵏ−1))` arises *solely* from the
  Atiyah-Bott / equivariant-η **normal-bundle denominators** `1/(ωᵏ−1) = det(1−g)⁻¹`.

So 2/9 is an **index / spectral-asymmetry** object, **not** a character. The "finite-carrier, no
manifold" reading either keeps the value 2/9 — and thereby keeps exactly the fixed-point/index
apparatus the lead called a "category error" — or strips the apparatus and lands on the character `−1`,
**losing the value**. You cannot have both. The lead is refuted (runner A1–A3; index-meaning lens
refuted all routes). The physically load-bearing object is moreover `δ = 2/9` *radians* (a Brannen
phase, `open_gate`), admissible as a radian only via the η-mod-ℤ reading the bare-character reading
discards.

### (B) The retained theorems bracket species→flavor as out-of-scope — the carrier is the open gate
The retained `three_generation_observable_*` theorems prove **more** than a count: `{C₃[111], T_x,T_y,T_z}`
generate `M₃(ℂ)` acting **irreducibly** on ℂ³ with no proper algebra-preserving quotient — a genuine
*carrier-for-the-algebra*. But they **explicitly hold the physical species→flavor identification out of
scope** (verified note text on origin/main):
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE` l.19 *"Physical species … remain out of scope here"*;
  l.151-153 *"not a standalone claim about physical-species semantics … delegated to
  `PHYSICAL_LATTICE_NECESSITY_NOTE` (Parts 7 and 9)"*; l.285-288 listed under *"Honest open items"*.
- `M3C_BURNSIDE` l.164 / l.179-184: does **not** identify ℂ³ with the *"charged-lepton flavor space"*;
  that identification is an *"admitted-context input … `claim_type: open_gate`"*.

So "flavor lives on the corner module *by construction*" **smuggles** the very species attachment the
theorems delegate. The carrier reduces to `PHYSICAL_LATTICE_NECESSITY_NOTE` Part 7 (`retained_no_go`)
and `open_gate` `lepton_brannen_bae_delta_two_ninths` — it is **open, not derived**. The factor-separation
fact (`koide_z3_equivariant_anticommuting_no_go`, retained_bounded) rules the extensive index *out* as
the *same* factor but does **not** rule the intrinsic ℂ³ *in* as the physical flavor carrier; that
selection is the open gate.

### (C) The basepoint r=1/2 is a separate, certified-missing input
The carrier theorems fix only the operator **form** `H=aI+bC+b̄C²` — `r=|b|²/a²` ranges freely (runner
B1: equivariance constrains the form, never `r`). `retained_no_go` `koide_q_delta_residual_cohomology_obstruction`
proves exactness yields a section **family** `s_a(t)=(t,at)`: `z=0` (`r=1/2 → Q=2/3`) and `z=−1/3`
(`r=1 → Q=1`) **both** preserve the retained total; there is no canonical zero-section ("naturality of
the zero section" is a *listed unmet falsifier"). So `r=1/2` neither derives from the carrier theorem
nor reduces to another retained row — it is an irreducible flavor input, **independent** of the carrier
question (factor selection vs section selection).

## Net — two independent irreducible inputs, and a correction to the prior framing
After this attack the open flavor content has **two independent unforced degrees of freedom**:
1. **(I) Carrier / factor selection** — that the observable is the intensive density on the intrinsic
   generation factor rather than the Γ₅-graded extensive lattice index (= the open species-ID gate);
2. **(II) Basepoint / section selection** — `r=1/2` (the `z=0` zero-section) over `r=1`.

**Correction to `FLAVOR_READOUT_GATE_EQUALS_CARRIER_IDENTIFICATION_2026-05-31`:** its *core* stands —
the readout question adds no new gate; it reduces to the carrier-ID. But its "single premise
(carrier-plus-basepoint)" framing **undercounts**: the basepoint is a *second, independent* input, and
the carrier-ID does **not** reduce to the retained count theorem (it is the explicitly out-of-scope
open gate). Honest count after derivation pressure: **two** inputs, not one. (And the momentum-corner
shortcut to *derive* the carrier is refuted: 2/9 is not a finite-rep character.)

This is a wall that held under direct attack — but per standing practice it is provisional: the carrier
gate is `open_gate`/`retained_no_go`, not an airtight impossibility, and either input may yet be reached
from upstream structure not exercised here (e.g. the substrate-necessity argument of
`PHYSICAL_LATTICE_NECESSITY_NOTE` Parts 7/9, untouched by this attack).

## Stale-citation guard (verified vs origin/main ledger + note text, 2026-05-31)
- `lepton_brannen_bae_delta_two_ninths` — **open_gate** (carrier sub-claim I).
- `koide_q_delta_residual_cohomology_obstruction` — **retained_no_go** (basepoint sub-claim II; section family, no canonical zero-section).
- `three_generation_observable_theorem` (+ `_m3c_burnside`, `_no_proper_quotient`, `_hw1_distinct_translation_characters`) — **retained** (algebra/count carrier; species→flavor ID explicitly out-of-scope, l.19/151-153/285-288 and l.164/179-184).
- `koide_z3_equivariant_anticommuting_no_go`, `axiom_first_z_n_equivariant_spectral_asymmetry_narrow` — **retained_bounded**.
- `PHYSICAL_LATTICE_NECESSITY_NOTE` — **retained_no_go** (where the species identification is delegated; untouched here).
- Does **NOT** load-bear on `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route` (both **unaudited**).

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [physical_lattice_necessity_note](PHYSICAL_LATTICE_NECESSITY_NOTE.md)
