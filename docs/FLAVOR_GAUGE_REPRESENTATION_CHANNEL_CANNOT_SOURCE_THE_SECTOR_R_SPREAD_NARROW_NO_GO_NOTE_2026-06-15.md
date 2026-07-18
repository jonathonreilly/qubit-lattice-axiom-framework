# Common-scalar and non-abelian colour-representation channels cannot source the displayed sector r-spread (narrow no-go)

**Date:** 2026-06-15
**Type:** no_go
**Status:** source note awaiting independent audit handling.
**Primary runner:** [`scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py`](../scripts/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.py)
**Cached output:** [`logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt`](../logs/runner-cache/frontier_gauge_rep_channel_cannot_source_spread_2026_06_15.txt)
**Generation-uniform core split:** [`FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md)
**Core runner/cache:** [`scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py`](../scripts/flavor_gauge_representation_generation_uniform_core_2026_06_18.py),
[`logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt`](../logs/runner-cache/flavor_gauge_representation_generation_uniform_core_2026_06_18.txt)

## 2026-06-18 generation-uniform core split

[`FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md)
isolates an exact conditional homogeneity lemma. If a nonzero common real scalar
rescales both `a` and `b`, then `r=|b|^2/a^2` is degree-zero inert. The cited
generation surface does not imply that all generation-uniform gauge actions
have this form; a holonomy may dress the hopping coefficient without dressing
the onsite coefficient.

The SM sector representation assignment remains a conditional physical
premise. This split does not derive the allowed SM sector representation
assignment, hypercharge, `T3`, right-handed representation data, or a physical
sector-to-carrier/readout bridge. The parent no-go therefore remains a
conditional no-go for the standard representation-channel escape route, not a
framework derivation of the sector representation table.

## Claim

The sector dial r = |b|²/a² (Koide Q = 1/3 + 2r/3) takes different values per fermion sector
(charged leptons r = 1/2, down-quarks r ≈ 0.597, up-quarks r ≈ 0.773, neutrinos other). **No function
of the non-abelian (colour) gauge representation can source this spread, and a
stipulated common scalar rescaling of `(a,b)` cannot move it; the within-doublet
splitter therefore lies outside these two tested channel classes.** Abelian /
hypercharge / T₃ / Higgs-partner structure and the within-sector measure are
named open candidates, among other untested dynamical, nonlocal, or source-law
mechanisms. (The abelian channel is *not* closed — after
electroweak breaking the unbroken U(1)_em charges {ν = 0, d = −1/3, u = 2/3, e = −1} distinguish all
four sectors; that channel is the open fork, not the wall.) Two structural facts close the
generation-carrier/generation-scalar non-abelian colour-representation avenue:

**(A) A nonzero common scalar rescaling leaves `r` degree-0-inert.** The
generation-uniform core split proves only the algebraic implication
`(a,b)->(sa,sb) => r'=r` for `s!=0`. It does not infer the common-scalar form
from generation uniformity. An action can treat onsite and hopping structures
differently without assigning different charges to the three generations;
the neighboring holonomy channel provides exactly such a control.

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
charged lepton) remains outside the two tested classes. **Abelian / hypercharge /
T₃ / Higgs-partner (electroweak)** data and the within-sector measure are named
open candidates, not an exhaustive partition. The abelian/electroweak channel is **not closed** by this note (after
electroweak breaking U(1)_em distinguishes all four sectors); it is the open fork.

## The no-go (the counting bound)

A sector-distinguishing datum that is a function of the *non-abelian* gauge
representation `R` is constant on representation-equivalence classes. Over the four
sectors {e, ν, u, d}:
- a **stipulated common scalar rescaling** cancels in `r` (A), but is not forced by generation uniformity;
- the **non-abelian colour** rep is colourless/coloured — 2 classes, and constant within each weak
  doublet (B);

So the non-abelian colour channel supplies at most a colourless/coloured 2-class
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
common scalar rescaling is degree-0-inert, and the non-abelian colour representation has only
the colourless/coloured 2-class resolution. Therefore **neither a common
scalar rescaling nor the non-abelian colour-representation class function
sources the sector spread.** The result is firewall-affirming: it
explains the repeated failure to derive r=1/2 (or the spread) from generation-carrier or colour
structure — the only such sector-distinguishing channel that survives degree-0 inertness is
the colour 2-class within the tested representation-only family, which is degenerate within a weak
doublet — and it does so without forcing any value. The within-doublet splitter is thereby localized
only outside the tested common-scalar and colour-class-function channels. Abelian/electroweak,
within-sector-measure, dynamical, nonlocal, and source-law routes remain outside this theorem. The honest present status is that **the sector
r-spread remains registered, per-sector dial data on this gauge-representation surface, not a
non-abelian gauge-structural prediction.** Promoting it to a prediction requires additional native
structure for that open fork.

## Boundary (honest)

- Forces **no** value of r; r₀ and the couplings are free registered data. Does not derive or force
  r = 1/2 (the firewall holds).
- The 2026-06-18 generation-uniform core split proves the conditional
  common-scalar degree-zero statement in (A); it does not derive that premise
  from generation uniformity.
- (B)'s within-doublet statement uses the standard identification of the sectors
  with their SM gauge representations; the **core lemma (A)** is only the
  common-scalar homogeneity identity. The
  2-class bound is robust to the precise rep assignment (any function of the colour rep is constant
  within a weak doublet), but the physical sector-to-representation/readout bridge remains open.
- Does **not** close the within-sector **measure / weighting-prior** channel, the abelian /
  hypercharge / T₃ / **electroweak-partner** channel, or other dynamical, nonlocal, or source-law
  mechanisms. These are non-exhaustive open routes. This note does not evaluate whether a native
  T₃-asymmetric electroweak structure can be derived.
- Holonomy and entropy channel notes are context only; they are not re-proven here and are not
  required for the A+B counting no-go.

## Cited Source Context

The following notes motivate the conditional construction; their current
ledger status and the physical sector mapping/readout are not upgraded here:
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md), [`three_generation_observable_m3c_burnside`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md), [`three_generation_observable_no_proper_quotient`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md) — the gauge-uniform shared M₃(ℂ) generation carrier (the core of A).
- [`koide_circulant_character_bridge`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) — the abstract form `H = aI + bC + b̄C²` and ratio definition `r = |b|²/a²`. The separately located `KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md` proves only an abstract Fourier-coordinate identity and is not physical carrier/readout authority for this no-go.
- [`charged_lepton_koide_cone_algebraic_equivalence`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md) — Q = 2/3 ⟺ r = 1/2.
- [`flavor_hw1_staggered_projection_democratic_r0`](FLAVOR_HW1_STAGGERED_PROJECTION_DEMOCRATIC_R0_2026-06-02.md) — the bare (undressed) generation hop gives r = 0 (the endpoint the suppression points toward).

Source-side core support (audit required before any effective status change):
- [`flavor_gauge_representation_generation_uniform_core`](FLAVOR_GAUGE_REPRESENTATION_GENERATION_UNIFORM_CORE_NARROW_THEOREM_NOTE_2026-06-18.md) — conditional common-real-scalar homogeneity lemma for (A), with both that premise and the SM sector representation assignment left open.

Context (no edge): `flavor_gauge_holonomy_suppresses_r_below_leptonic_wrong_ordering` (the holonomy
character bound); `flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (the
sector-blindness); `color_generation_independent_z3_structures` (colour ⊥ generation modules);
`flavor_per_sector_orientation_is_gauge_cp_is_inter_sector` (per-sector orientation is gauge, R-odd);
`hunit_to_ewsb_doublet_representation_no_go` (Hom_SU(2)(1, 2) = 0 — the electroweak doublet is a
supplied import, so the within-doublet splitter channel is named-but-unbuilt).

## Forbidden-imports check

No new axiom. The core lemma (A) is exact only after supplying the common-real-scalar premise; the cited generation sources do not derive it. The within-doublet
rep facts (B) are the standard SM identification used to *test the proposed gauge-rep escape under
its own premise* — not adopted as derived framework content; the physical
two-class conclusion is conditional on that mapping and readout. The observed r values enter only as anchors for the counting/ordering
contradiction, never as derivation inputs. r₀ and the per-sector couplings are free symbols; no r
value is computed or forced.
