# The non-abelian (colour) gauge-representation channel cannot source the sector r-spread — the splitter is abelian/electroweak (narrow no-go)

**Date:** 2026-06-15
**Type:** narrow no-go
**Claim type:** no_go
**Status:** source note awaiting independent audit handling.
**Primary runner:** [`scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py`](../scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py)
**Cached output:** [`logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt`](../logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt)
**Generation-uniform core split:** [`FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md)
**Core runner/cache:** [`scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py`](../scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py),
[`logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt`](../logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt)

## 2026-06-18 generation-uniform core split

[`FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md)
isolates the framework-native part of this no-go. On the retained
three-generation observable surface, a gauge action that is scalar on the
shared generation carrier multiplies `a` and `b` by the same factor, so
`r=|b|^2/a^2` is degree-zero inert. This core rests only on the retained
generation and Koide-ratio authorities cited below.

The SM sector representation assignment remains a conditional physical
premise. This split does not derive the allowed SM sector representation
assignment, hypercharge, `T3`, right-handed representation data, or a physical
sector-to-carrier/readout bridge. The parent no-go therefore remains a
conditional no-go for the standard representation-channel escape route, not a
framework derivation of the sector representation table.

## Claim

The sector dial r = |b|²/a² (Koide Q = 1/3 + 2r/3) takes different values per fermion sector
(charged leptons r = 1/2, down-quarks r ≈ 0.597, up-quarks r ≈ 0.773, neutrinos other). **No function
of the generation-carrier gauge action or the non-abelian (colour) gauge representation can source this
spread; the within-doublet splitter is forced into the abelian / hypercharge / T₃ / Higgs-partner
(electroweak) channel or the within-sector measure.** (The abelian channel is *not* closed — after
electroweak breaking the unbroken U(1)_em charges {ν = 0, d = −1/3, u = 2/3, e = −1} distinguish all
four sectors; that channel is the open fork, not the wall.) Two structural facts close the
generation-carrier/generation-scalar non-abelian colour-representation avenue:

**(A) Gauge-uniformity ⟹ r is degree-0-inert under any generation-carrier gauge action.** The
generation-uniform core split isolates the retained-input part: the generation carrier is the
shared M₃(ℂ), so any action scalar on that carrier multiplies the singlet coefficient `a` and the
doublet coefficient `b` by the same factor, which cancels in `r=|b|²/a²`. In the parent
representation-channel reading, this is the statement that the three generations carry *identical* gauge charges
(retained [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
[`three_generation_observable_m3c_burnside`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)).
Therefore a gauge action through the generation carrier is a *scalar* on the generation index. (A non-uniform action that distinguished singlet from doublet would
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

Adjacent non-generation-scalar channels are context, not hidden authority for this note. The
covariant-hopping holonomy channel has its own source-side no-go surface, and the record-structure
sector-blindness row has its own audit status. They motivate the remaining fork, but the no-go proven
here is the A+B counting statement above.

**Conclusion.** The sector r-spread is **not a generation-carrier scalar or non-abelian
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

This consolidates the gauge-representation side of the couplings-origin avenue: on-site
generation-carrier scalar action is degree-0-inert, and the non-abelian colour representation has only
the colourless/coloured 2-class resolution. Therefore **no generation-scalar or non-abelian (colour)
gauge-representation channel sources the sector spread.** The result is firewall-affirming: it
explains the repeated failure to derive r=1/2 (or the spread) from generation-carrier or colour
structure — the only such sector-distinguishing channel that survives degree-0 inertness is
the colour 2-class, which is degenerate within a weak doublet — and it does so without forcing any
value. The within-doublet splitter is thereby localized outside this channel, in the
abelian/electroweak or within-sector-measure fork. The honest present status is that **the sector
r-spread remains registered, per-sector dial data on this gauge-representation surface, not a
non-abelian gauge-structural prediction.** Promoting it to a prediction requires additional native
structure for that open fork.

## Boundary (honest)

- Forces **no** value of r; r₀ and the couplings are free registered data. Does not derive or force
  r = 1/2 (the firewall holds).
- The 2026-06-18 generation-uniform core split is source-side bounded support for
  the degree-zero inertness statement in (A).
- (B)'s within-doublet statement uses the standard identification of the sectors
  with their SM gauge representations; the **core theorem (A)** — gauge-uniformity ⟹ degree-0
  inertness — rests only on retained `three_generation_observable` and needs no identification. The
  2-class bound is robust to the precise rep assignment (any function of the colour rep is constant
  within a weak doublet), but the physical sector-to-representation/readout bridge remains open.
- Does **not** close the within-sector **measure / weighting-prior** channel, nor the abelian /
  hypercharge / T₃ / **electroweak-partner** channel — those are where the within-doublet splitter
  must live. This note does not evaluate whether a native T₃-asymmetric electroweak structure can be
  derived; that remains a distinct open fork.
- Holonomy and entropy channel notes are context only; they are not re-proven here and are not
  required for the A+B counting no-go.

## Dependencies

Dependency edges (retained):
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), [`three_generation_observable_m3c_burnside`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md), [`three_generation_observable_no_proper_quotient`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) — the gauge-uniform shared M₃(ℂ) generation carrier (the core of A).
- [`koide_circulant_character_bridge`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) and [`koide_kappa_spectrum_operator_bridge`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) — H = aI + bC + b̄C², r = |b|²/a², Q = 1/3 + 2r/3.
- [`charged_lepton_koide_cone_algebraic_equivalence`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) — Q = 2/3 ⟺ r = 1/2.
- [`flavor_hw1_staggered_projection_democratic_r0`](FLAVOR_HW1_STAGGERED_PROJECTION_DEMOCRATIC_R0_2026-06-02.md) — the bare (undressed) generation hop gives r = 0 (the endpoint the suppression points toward).

Source-side core support (audit required before any effective status change):
- [`flavor_gauge_representation_generation_uniform_core`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md) — framework-native scalar-action/degree-zero-inertness split for (A), with the SM sector representation assignment left conditional.

Context (no edge): `flavor_gauge_holonomy_suppresses_r_below_leptonic_wrong_ordering` (the holonomy
character bound); `flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (the
sector-blindness); `color_generation_independent_z3_structures` (colour ⊥ generation modules);
`flavor_per_sector_orientation_is_gauge_cp_is_inter_sector` (per-sector orientation is gauge, R-odd);
`hunit_to_ewsb_doublet_representation_no_go` (Hom_SU(2)(1, 2) = 0 — the electroweak doublet is a
supplied import, so the within-doublet splitter channel is named-but-unbuilt).

## Forbidden-imports check

No new axiom. The core theorem (A) uses only retained `three_generation_observable` and the 2026-06-18 generation-uniform core split. The within-doublet
rep facts (B) are the standard SM identification used to *test the proposed gauge-rep escape under
its own premise* — not adopted as derived framework content; the conclusion (the channel cannot source
the spread) holds regardless. The observed r values enter only as anchors for the counting/ordering
contradiction, never as derivation inputs. r₀ and the per-sector couplings are free symbols; no r
value is computed or forced.
