# Lane-Assignment Discriminator: Derived-Modulo-Gauge-Content, with the "color -> hierarchy" Mechanism Direction a Posited (and Structurally Dis-favored) Residual

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a hostile audit of one *proposed reframe* — that the charged-lepton Koide dial sits at
`r=1/2` because the sector is "charged AND colorless," with the further claim "color breaks toward
hierarchy (`r>1/2`), neutrality toward degenerate (`r<1/2`)." This note judges the **logic** of that
discriminator against the framework state on `origin/main` (it does **not** defer to the ledger for the
verdict). It sets no audit status, assigns no grade, changes no row, and introduces **no axiom, import, or
new framework language**. Every load-bearing fact is a finite check on objects already retained on main
plus the exact Koide-cone identity `Q = 1/3 + (2/3)r`.
**Runner:** `scripts/lane_assignment_derivable_or_input_2026_06_04.py` (SCORECARD 15/15).
**Cache:** `logs/runner-cache/lane_assignment_derivable_or_input_2026_06_04.txt`

## Verdict (one line)

**DERIVED-MODULO-GAUGE-CONTENT on the block-content axis; the "color -> hierarchy" *mechanism direction* is
a POSITED CORRELATION fitted to the observed quark hierarchy — the framework offers no native carrier for
it, and the genuine residual is the color-independent `det_C`-vs-`det_R` (`AC_φλ`) measure bit.**

The honest target stated in the charge ("the dial-point assignment follows from the framework-derived gauge
content **iff** the color->hierarchy mechanism direction is itself derivable; otherwise the mechanism
direction is the residual input") resolves to the **second** branch: the mechanism direction is **not**
derivable on the current surface, so it is the residual input — and in fact it is worse than merely
un-derived, because FACT 3/FACT 4 below show the framework's own structure makes color **r-blind**, so the
proposed discriminator is not even structurally available, let alone forced.

## Crucial framing correction (what is actually on main vs. the proposed frame)

The charge describes a discriminator — "charged ∧ colorless -> symmetric; color -> hierarchy; neutrality ->
degenerate." **This is not the state on `origin/main`.** The mapped flavor cluster
(`OPEN_KOIDE_FLAVOR_CLUSTER_CONSOLIDATION_MAP_2026-06-02`,
`FLAVOR_LANE_PANEL_REDUCES_TO_DOUBLET_MODE_COUNT_2026-05-31`,
`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02`,
`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`) reduces the charged-lepton value to **one
generation-intrinsic binary** — `det_C` (holomorphic, doublet = one complex mode -> `r=1/2` -> `Q=2/3`) vs
`det_R` (real, doublet = two real modes -> `r=1` -> `Q=1`), the Tier-A admitted input `AC_φλ`. This residual
lives entirely on the **C₃ generation factor** (the dial `r=|b|²/a²` of `H=aI+bC+b̄C²`). It has **nothing to
do with color or electric charge.** The "color -> hierarchy" discriminator is therefore a *new proposal*
laid on top of the existing reduction, and the hostile question is whether that proposal is derivable. It is
not.

## Q1 — Does the framework DERIVE the sectors' color/charge assignments?

**Block content: YES (derived, retained). Species name + electric charge: NO (admitted SM convention).**

- **Derived (FACT 1, runner).** On the retained graph-first SU(3) commutant
  (`graph_first_su3_integration_note`, **retained**; `cl3_color_automorphism_theorem`, **retained**), the
  LH-doublet base splits `C⁴ = Sym²(C²) ⊕ Anti²(C²)` into a **3-dim** and a **1-dim** block. By the su(3)
  dimension formula `dim(p,q)=(p+1)(q+1)(p+q+2)/2`, **no non-trivial su(3) irrep has dim ≤ 2**, so the 1-dim
  block **must** carry the trivial (color-singlet) rep and the 3-dim block the fundamental (color-triplet).
  That "one block is colored, the other colorless" is a **theorem**, not a label
  (`lhcm_matter_assignment_su3_block_representation_narrow_theorem_note_2026-05-17`, **retained_bounded**).
  The hypercharge **direction** `+1:(−3)` on (triplet:singlet) is likewise derived from tracelessness of the
  residual U(1) (FACT 2, derived part).
- **Admitted (FACT 2, runner).** The **SM species label** ("the color-singlet block *is the charged lepton*",
  "the color-triplet block *is the quark*") and the **electric-charge readout** `Q_em = T₃ + Y/2` — which
  needs the **absolute** hypercharge normalization `α = 1/3` (`hypercharge_identification_note` L3,
  **retained_bounded**, which explicitly admits L3 as SM convention) — are **admitted SM-definition
  convention**, not derived. So "this sector is *the charged lepton* and it is *electrically charged*" rides
  one admitted naming + one admitted scale.

**Q1 net:** the *colored/colorless* structural property the discriminator needs is **derived**; the
*charged-lepton-species* identity and the *electric-charge ≠ 0* property are **admitted**. The discriminator
is therefore *at best* one step from derived on its **color** half and rests on the admitted SM naming/`α`
on its **charge** half.

## Q2 — Is the MECHANISM (color -> shift `r` up) derivable? **No — it has no structural carrier.**

The dial `r` is a property of the **C₃ generation factor only**. Color SU(3) and weak SU(2) attach to the
fermion as **separate tensor legs** that are **C₃-trivial passengers**: the generation triplet is the hw=1
C₃ orbit, and color/weak act trivially on the C₃ label. Tensoring the C₃-equivariant Hermitian operator
(circulant, real DOF split 1 singlet : 2 doublet) with any C₃-trivial spectator multiplies **both** isotype
blocks by the same integer, leaving the **(1:2) ratio — and hence the entire `r`-structure — exactly
invariant** (FACT 3, runner; `quark_bae_analog_bounded_obstruction_note_2026-05-10`: the 6-dim quark host
yields the **same** (1,2) ratio as the 3-dim lepton host *because* the color/weak factors are C₃-trivial
passengers).

So at the level of framework structure, **color does not shift `r` in either direction.** There is no
SU(3)-coupling term in the C₃-equivariant generation operator that could push the block weight off
equipartition — the generation leg and the gauge legs are orthogonal and the gauge legs are C₃-silent
(FACT 1b: the gauge content distinguishing `Q_L=(3,2)` from `L_L=(1,2)` is the SU(3) label, which is
generation-`r`-silent). The proposed mechanism "color -> hierarchy" has **no carrier** in the retained
structure.

**Could color "equally well" push toward degenerate?** Structurally, yes — that is exactly the point
(FACT 3c). Passenger-tensoring is `r`-blind, so the cone `r∈[0,1]` (`Q∈[1/3,1]`) is fully reachable on
every host and **neither** sign of `(r−1/2)` is selected. The frame's choice of "hierarchy" is not derived
from any color property; it is read off the fact that the **observed** quarks are hierarchical.

## Q3 — Is this CIRCULAR? **Yes, for the mechanism direction — it is a post-hoc relabeling of the observation.**

We **observe** quarks hierarchical (`r>1/2`) and charged leptons balanced (`r=1/2`). The discriminator
"color -> hierarchy" is selected **because** the colored sector (quarks) is observed hierarchical — there is
no independent reason. The two candidate *independent* handles both fail:

- **C₃-passenger structure (FACT 3):** color-blind, predicts neither direction (above).
- **A shared color-generation Z₃ (FACT 4):** the only intrinsic candidate for a color->generation handle is
  a common Z₃. But the **SU(3)_c center Z₃** acts on the color triplet by a **scalar**, character
  `(3, 3ω, 3ω²)`, while the **generation C₃** axis-permutation acts by the **regular** rep, character
  `(3, 0, 0)`. These are **inequivalent Z₃ representations**
  (`z3_character_isomorphism_color_generation_open_gate_note_2026-05-10`, **open_gate**: a common
  axis-cycle would be needed to identify them, and that common action is "the work still to be derived").
  So the color Z₃ carries **no information** that could orient the generation block-weight `r` in any
  direction.

Neither QCD running nor the color-generation character structure independently predicts the hierarchy
*direction*. The discriminator is therefore a **post-hoc relabeling** of the observed mass hierarchy, not a
derivation. (This matches the field: Koide arXiv:1301.4143 leaves the per-sector ratio a **free fit** in
every sector; the framework's structural verdict — color is a passenger — is consistent with that freedom.)

## Q4 — Count the irreducible inputs honestly

For the full lepton/quark/neutrino Koide structure, after this analysis, the irreducible inputs are
**three** (option (c) of the charge, made precise):

1. **The gauge content's admitted half** — the SM **species naming** (`color-singlet ≡ charged lepton`,
   `color-triplet ≡ quark`) + the absolute hypercharge normalization **`α = 1/3`** (electric charge). The
   *colored/colorless block content* and the *hypercharge direction* are **derived** (Q1); only the naming +
   absolute scale are admitted. *(This is the input that lets us even say "the charged-lepton sector.")*

2. **The per-sector dial value `r`** — the **color-independent** `det_C`-vs-`det_R` / `AC_φλ` measure bit
   (equal-power-per-block -> `r=1/2` vs per-real-DOF/Born -> `r=1`), **per sector**. This is the single
   residual the whole flavor cluster already isolates; it is **not** supplied by color, and the "color ->
   hierarchy" discriminator does **not** discharge it (Q2/Q3). Charged leptons need the det_C reading;
   quarks need some `r>1/2`; the framework does not yet derive **which** reading any sector takes — that is
   the open `which-lane`/`which-vacuum` question.

3. **The neutrino mass mechanism** — Dirac-vs-Majorana / the active-neutrino mass scale and ordering — a
   *separate* sector input the charged-lepton analysis does not touch
   (`PMNS_NEUTRINO_MASS_OBSERVABLES_NO_PREDICTION_NARROW_THEOREM_NOTE_2026-05-17`).

The proposed discriminator tried to **collapse #2 into #1** (derive the dial value from the gauge
color/charge property). That collapse **fails**: the dial is generation-intrinsic and color-blind, so #2
remains a genuinely **separate** input from #1. The discriminator does **not** reduce the input count; it
re-describes input #2 in color language that the structure does not support.

## What stands (the next paths this opens — not closing anything)

- The **block-content** half of Q1 is solidly derived; if a future audit promotes the SM-naming + `α=1/3`
  step (e.g. via an electric-charge / Gell-Mann–Nishijima derivation), input #1 shrinks to zero and the
  "which sector is the charged lepton" question becomes derived.
- The honest open handle for input #2 remains the **det_C/det_R** measure question — derive the
  doublet-coefficient's emergent kinetic metric from the qubit coherent-state resolution-of-identity on the
  hw=1 C₃ orbit (holomorphic -> `r=1/2`; doubled-real -> `r=1`). This is **color-independent**, so it would
  fix the dial for **every** sector at once and is the correct target — *not* a per-sector color rule.
- A genuine `which-lane` *dynamics* (records/persistence, mass-generation) that selects different extrema for
  different sectors would be the only way a sector property could legitimately enter — but any such mechanism
  must act on the generation leg, where color is absent. A color-coupled selection would require first
  building the missing color->generation bridge (FACT 4's open gate), which is itself unbuilt.

## Provenance (verified 2026-06-04)

- All four facts verified directly (runner 15/15): the su(3) dimension forcing (FACT 1), the hypercharge
  ratio `+1:(−3)` (FACT 2 derived part), C₃-passenger ratio-preservation across lepton/quark hosts (FACT 3),
  the cone-reachability/direction-underdetermination (FACT 3c), the color-center-Z₃ ≠ generation-Z₃
  character inequivalence (FACT 4), and the color-independent `det_C/det_R -> r=1/2 / r=1` primitive.
- Anchors checked against the live ledger before landing: `graph_first_su3_integration_note` (**retained**),
  `cl3_color_automorphism_theorem` (**retained**), `native_gauge_closure_note` (**retained**),
  `lhcm_matter_assignment_su3_block_representation_narrow_theorem_note_2026-05-17` (**retained_bounded**),
  `hypercharge_identification_note` (**retained_bounded**), `koide_frobenius_isotype_split_uniqueness_note`
  (**retained_no_go**), `action_normalization_note` (**retained_no_go**),
  `z3_character_isomorphism_color_generation_open_gate_note_2026-05-10` (**open_gate / unaudited**),
  `quark_bae_analog_bounded_obstruction_note_2026-05-10` (**unaudited**, cited for the passenger fact which
  this runner re-derives independently).
- This note **sets no audit status and assigns no grade**; the row classification is the independent audit
  lane's call. It introduces no axiom, no import, and no new framework vocabulary. It does not load-bear on
  `closure_c_staggered_dirac_gate` or `koide_phase_aps_eta_parity_route`.
