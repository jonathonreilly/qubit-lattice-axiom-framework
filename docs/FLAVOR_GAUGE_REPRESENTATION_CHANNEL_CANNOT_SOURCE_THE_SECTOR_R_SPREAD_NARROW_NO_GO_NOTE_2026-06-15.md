# The non-abelian (colour) gauge-representation channel cannot source the sector r-spread — the splitter is abelian/electroweak (narrow no-go / capstone)

- **Date:** 2026-06-15
- **Type:** narrow no-go
- **Claim type:** narrow_no_go
- **Status:** source note awaiting independent audit handling.
- **Primary runner:** [`scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py`](../scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py)
- **Cached output:** [`logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt`](../logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt)

## Claim

The sector dial r = |b|²/a² (Koide Q = 1/3 + 2r/3) takes different values per fermion sector
(charged leptons r = 1/2, down-quarks r ≈ 0.597, up-quarks r ≈ 0.773, neutrinos other). **No function
of the generation-carrier gauge action or the non-abelian (colour) gauge representation can source this
spread; the within-doublet splitter is forced into the abelian / hypercharge / T₃ / Higgs-partner
(electroweak) channel or the within-sector measure.** (The abelian channel is *not* closed — after
electroweak breaking the unbroken U(1)_em charges {ν = 0, d = −1/3, u = 2/3, e = −1} distinguish all
four sectors; that channel is the open fork, not the wall.) Three structural facts close the
non-abelian/generation-scalar avenue:

**(A) Gauge-uniformity ⟹ r is degree-0-inert under any generation-carrier gauge action.** The
generation carrier is the shared M₃(ℂ); the three generations carry *identical* gauge charges
(retained [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
[`three_generation_observable_m3c_burnside`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)).
Therefore a gauge action through the generation carrier is a *scalar* on the generation index — it
multiplies the singlet coupling a and the doublet coupling b by the **same** factor, which cancels in
the degree-0 ratio r = |b|²/a². (A non-uniform action that distinguished singlet from doublet would
require the generations to carry different charges, which gauge-uniformity forbids — the runner
exhibits this as the discriminating control.) This grounds the previously thinking-exercise-only
"degree-0 inertness" of r on retained content.

**(B) Within-doublet rep-degeneracy ⟹ a colour-rep function gives at most a 2-class partition.** Under
the standard identification of the sectors with their Standard-Model gauge representations, the
within-weak-doublet partners share the *entire* left-handed multiplet: up and down quarks both sit in
(3, 2, 1/6); neutrino and charged lepton both in (1, 2, −1/2). So any function of the unbroken
non-abelian (colour) representation is **constant within a weak doublet** — it assigns one value to
the colourless sectors and one to the coloured sectors, a colourless/coloured **2-class** partition of
the four sectors. It provably cannot resolve up from down or ν from e. The observed coloured sectors
have *distinct* r (r_up ≈ 0.773 ≠ r_down ≈ 0.597) inside one colour class, violating the 2-class
bound.

**(C) The two non-generation-scalar non-abelian channels are separately closed.** The gauge-rep
channels that do *not* act as a generation-scalar — the covariant-hopping holonomy and the
record-structure — are shown elsewhere to **suppress** r below the leptonic value (the gauge-holonomy
character bound r_R ≤ r₀, wrong ordering) and to be sector-**blind** (max-record-entropy is
gauge-uniform). Together with (A) and (B), every *generation-scalar and non-abelian colour-rep*
channel to r is accounted for and none can produce the observed spread.

**Conclusion (capstone).** The sector r-spread is **not a generation-scalar or non-abelian
(colour) gauge-representation prediction** — it is registered, sector-dependent dial data. This forces
no r value: r₀ and the per-sector couplings are free. The within-doublet resolution (up vs down, ν vs
charged lepton) is forced into an **abelian / hypercharge / T₃ / Higgs-partner (electroweak)** datum,
or the within-sector measure. That abelian/electroweak channel is **not closed** by this note (after
electroweak breaking U(1)_em distinguishes all four sectors); it is the open fork.

## The no-go (the counting bound)

A sector-distinguishing datum that is a function of the generation-carrier gauge action or the
*non-abelian* gauge representation R is constant on representation-equivalence classes. Over the four
sectors {e, ν, u, d}:
- the **generation-carrier** gauge action is a scalar (gauge-uniformity, A) — 1 class (cancels in r);
- the **non-abelian colour** rep is colourless/coloured — 2 classes, and constant within each weak
  doublet (B);
- the non-generation-scalar **holonomy / record-structure** channels suppress or are blind (C).

So the generation-scalar + non-abelian colour channel supplies at most a colourless/coloured 2-class
structure, while the observed spread has ≥ 3 distinct values with r_up ≠ r_down *inside* the coloured
class. That channel under-determines r: it cannot be the source. **The abelian channel is a separate
matter and is left open:** the unbroken U(1)_em charges (and right-handed hypercharges) *do*
distinguish all four sectors, so an arbitrary function of charge could in principle assign the four
values — but only as a per-sector charge assignment, i.e. a fit, not a structural prediction (the
observed r-ordering e < d < u is not even a *monotone* function of |Q|, whose ordering is d < u < e;
the runner records this as an ordering mismatch, which excludes the *simplest* |Q| laws, not the
abelian channel as a whole). Resolving whether the abelian/electroweak channel has a native
non-fit structure is the open fork.

## Significance

This consolidates the couplings-origin avenue: across the record-flow side (the dynamics forces the
form, conserves the measure, is weighting-blind) and the gauge-representation side (on-site Casimir
degree-0-inert, covariant-hopping holonomy suppressing, max-record-entropy sector-blind, and now the
within-doublet colour-rep degeneracy), **no generation-scalar or non-abelian (colour) gauge channel,
and no record-dynamics channel, sources the sector spread.** The result is firewall-affirming: it
explains *why* every attempt to derive r=1/2 (or the spread) from generation-carrier or colour
structure has failed — the only such sector-distinguishing channel that survives degree-0 inertness is
the colour 2-class, which is degenerate within a weak doublet — and it does so without forcing any
value. With the within-doublet splitter thereby forced into the abelian/electroweak channel, and that
channel found named-but-unbuilt (no native weak-isospin doublet; Hom_SU(2)(1, 2) = 0), the honest
present status is that **the sector r-spread is registered, per-sector dial data — a fit on the current
retained surface, not a gauge-structural prediction.** Promoting it to a prediction requires first
deriving the electroweak doublet structure from the axioms — a separate mountain.

## Boundary (honest)

- Forces **no** value of r; r₀ and the couplings are free registered data. Does not derive or force
  r = 1/2 (the firewall holds).
- (B) and (C)'s within-doublet and channel statements use the standard identification of the sectors
  with their SM gauge representations; the **core theorem (A)** — gauge-uniformity ⟹ degree-0
  inertness — rests only on retained `three_generation_observable` and needs no identification. The
  2-class bound is robust to the precise rep assignment (any function of the colour rep is constant
  within a weak doublet).
- Does **not** close the within-sector **measure / weighting-prior** channel, nor the abelian /
  hypercharge / T₃ / **electroweak-partner** channel — those are where the within-doublet splitter
  must live. A find-the-escape probe of that channel (this turn) found it **named-but-unbuilt**: the
  framework carries no native weak-isospin acting T₃-asymmetrically on a matter doublet (the retained
  SU(2) is the *spin* su(2)), and `hunit_to_ewsb_doublet_representation_no_go` (2026-06-15) gives
  Hom_SU(2)(1, 2) = 0 — the native scalar-singlet structure cannot derive the SU(2)_L doublet, which is
  a supplied import. The measure channel selected per-sector is a free per-sector coefficient
  (= relocation); the Frobenius-Schur / det_C-vs-det_R reality-type escape is measure-neutral
  ([J_cs, H] = 0) and acts on the *generation* irrep (sector-uniform), not the matter rep. So on the
  **current retained surface the spread is an irreducible per-sector fit**. The open fork (walls move)
  is to *derive* the weak-isospin doublet from the axioms — de-importing it — then test whether a
  native T₃-asymmetry raises coloured r coefficient-free; that is a distinct mountain (electroweak
  structure from A_min), not the couplings-flow lens.
- (C) cites the holonomy and entropy channel-closures as context; they are not re-proven here.

## Dependencies

Dependency edges (retained):
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), [`three_generation_observable_m3c_burnside`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md), [`three_generation_observable_no_proper_quotient`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) — the gauge-uniform shared M₃(ℂ) generation carrier (the core of A).
- [`koide_circulant_character_bridge`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) and [`koide_kappa_spectrum_operator_bridge`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) — H = aI + bC + b̄C², r = |b|²/a², Q = 1/3 + 2r/3.
- [`charged_lepton_koide_cone_algebraic_equivalence`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) — Q = 2/3 ⟺ r = 1/2.
- [`flavor_hw1_staggered_projection_democratic_r0`](FLAVOR_HW1_STAGGERED_PROJECTION_DEMOCRATIC_R0_2026-06-02.md) — the bare (undressed) generation hop gives r = 0 (the endpoint the suppression points toward).

Context (no edge): `flavor_gauge_holonomy_suppresses_r_below_leptonic_wrong_ordering` (the holonomy
character bound, C); `flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (the
sector-blindness, C); `color_generation_independent_z3_structures` (colour ⊥ generation modules);
`flavor_per_sector_orientation_is_gauge_cp_is_inter_sector` (per-sector orientation is gauge, R-odd);
`hunit_to_ewsb_doublet_representation_no_go` (Hom_SU(2)(1, 2) = 0 — the electroweak doublet is a
supplied import, so the within-doublet splitter channel is named-but-unbuilt).

## Forbidden-imports check

No new axiom. The core theorem (A) uses only retained `three_generation_observable`. The within-doublet
rep facts (B, C) are the standard SM identification used to *test the proposed gauge-rep escape under
its own premise* — not adopted as derived framework content; the conclusion (the channel cannot source
the spread) holds regardless. The observed r values enter only as anchors for the counting/ordering
contradiction, never as derivation inputs. r₀ and the per-sector couplings are free symbols; no r
value is computed or forced.
