# The Quark-Lane Dial Comparators Are Mixed-Convention; Corrected Common-Scale Values (Comparator Correction with Exact Support)

**Date:** 2026-08-07
**Type:** meta
**Claim type:** meta (comparator correction and reference-scale convention;
no premise-conditional proposition is asserted — see "What is and is not
claimed" below)
**Status:** support
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py`](../scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt`](../logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt)

## What this corrects

[`QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md`](QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md)
displays quark dial values `r_up = 0.773642` and `r_down = 0.597141`, correctly
labelled "observational comparators only" under a "packet-local central-value
comparator convention."

That convention quotes the three masses of a sector at **different reference
scales** — and, in the up-type sector, mixes a pole mass with MSbar masses.
Re-quoting a mass triple with unequal per-generation factors is precisely the
operation the dial is *not* invariant under. So those numbers do not measure
the dial, and this note supplies the values that do.

It is the only source note carrying the six-decimal values, but not the only
consumer. Five landed notes quote the three-decimal roundings `r_up ≈ 0.773`
(or `0.774`) and `r_down ≈ 0.597` as sector comparators:
`FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05` §2.1, the three 2026-06-15
narrow no-go notes on flavor-gauge holonomy, flavor-gauge representation, and
max-record-entropy, and
`KOIDE_KAPPA_BOOKKEEPING_FLOW_CLASS_FIXED_POINT_INVERSION_AND_LANE_SCOPING_BOUNDED_THEOREM_NOTE_2026-07-11`.
No claim of theirs is overturned: each uses only the ordering
`r_lep < r_down < r_up` and the fact that the three differ, and the correction
preserves both while widening the gaps. One *displayed* number does move — the
kappa note's `kappa_down_report = 1/r_down` goes from `1.675` to `1.610`, so
its near-hit on the display-grid value `5/3` does not survive. That note
already marks the figure as display-only arithmetic with no confidence-level
meaning, so nothing is retracted; the near-hit simply should not be carried
forward. (The two audit-data files that also carry the old values are
pipeline-generated and belong to the audit lane.)

## The correction

```text
                                       r_up       r_down
open-gate note, as displayed         0.773642    0.597141   (mixed scale; pole top)
same inputs, MSbar top m_t(m_t)      0.767630    0.597141   (mixed scale only)
canonical common scale               0.830971    0.621090
                                     ± 0.002211  ± 0.007511
```

The runner reproduces the open gate's two displayed values to six decimals from
that note's own quoted mass list, which confirms the convention being compared
is the one it actually used. The `+0.0573` shift in `r_up` splits as `−0.0060`
from pole→MSbar and `+0.0633` from the scale correction.

The numerical packet deliberately preserves the landed comparator's input
vintage rather than silently substituting a newer fit: masses and their errors
come from the [PDG 2022 quark summary
table](https://pdg.lbl.gov/2022/tables/rpp2022-sum-quarks.pdf), while
`α_s(M_Z)=0.1180±0.0009` comes from the [PDG 2023 QCD
review](https://pdg.lbl.gov/2023/reviews/rpp2023-rev-qcd.pdf). The asymmetric
mass errors are symmetrized as half the sum of their upper and lower
magnitudes, then rounded to the precision displayed by the runner. These are
comparator inputs, not a claim to reproduce the newest PDG table.

The corrected values sit *further apart* than the ones they replace. Anyone
using the sector spread should note that this correction widens it rather than
narrowing it.

## Why the common-scale convention is the well-defined one

Two ingredients, both **prior art**, and one exact step that is not.

**Homogeneity (prior art, not claimed here).** `Q`, `r` and the rational pair
`(C, J)` pinning `δ` are ratios of equal-degree forms in `x_k = √m_k`, so a
common rescaling `m_k ↦ λ m_k` cancels identically.
[`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
already records that `r` "is invariant under every permutation of the mass
triple and under a common positive rescaling of all three masses." The runner
reproduces it exactly only because the step below needs the same coordinates.

**Flavour-universal running (prior art, supplied physics).** In QCD the MSbar
mass anomalous dimension depends on the coupling and the active flavour number
only, so on a fixed-flavour surface one factor `R(μ, μ₀)` rescales the whole
sector. Recorded at
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
eq. (5.6), there used for mass ratios. Combined with homogeneity: **within a
fixed scheme, a sector's dial does not depend on which common reference scale
is chosen.** The runner exhibits this across six common scales spanning three
decades, agreeing to `4e-12`.

**Sharpness (exact, the one step here that is not prior art).** The equal-factor hypothesis
is doing real work, not sitting there as a removable technicality. On the
triple `x = (1, 1, 0)`, scaling the two nonzero coordinates by `μ₁, μ₂` gives

```text
2(μ₁² + μ₂²) − (μ₁ + μ₂)²  =  (μ₁ − μ₂)² ,
```

so `Q` returns its unscaled value **iff** `μ₁ = μ₂`. The runner also moves both
`Q` and `r` on strictly positive nondegenerate rational triples, with exact
before/after fractions.

This is a **sharpness witness, not a converse**, and the distinction is
load-bearing. The literal converse — dial unchanged ⟹ all `λ_k` equal — is
**false**: the dial depends only on the *multiset*, so the coordinate triple
`x = (4, 2, 1)` with unequal factors `(1/4, 1, 4)` on `x` — equivalently
`λ = (1/16, 1, 16)` on the masses — permutes the multiset onto itself and
leaves `Q` and `r` exactly fixed. The runner exhibits that counterexample so
the stronger reading cannot return by accident.

## Canonical prescription (load-bearing for the values above)

The common scale must be one at which all three masses are legitimate
active-flavour MSbar masses. A quark below its **own** threshold is decoupled,
so `μ ≥ m_t` for up-type and `μ ≥ m_b` for down-type; **taking `μ ≥ m_t`
satisfies both and is the prescription adopted here.** At `μ ≥ m_t` every mass
is transported *upward* onto one `n_f=6` surface. Crossing a heavy-quark
threshold also requires finite matching for the quarks light at that threshold
([Liu and Steinhauser 2015](https://arxiv.org/abs/1502.04719)); that coefficient
is common among those light flavours, not necessarily across a sector that
contains the newly activated heavy member. It therefore need not cancel from a
sector dial and remains a separately sized residual below.

The sub-threshold rows of the runner's invariance table are **display-only**:
they extrapolate `m_t` (both sectors, four of six rows including `μ = M_Z`) and
`m_b` (down sector, at 2 GeV) below their own thresholds. They exist to exhibit
the invariance; every one agrees with the canonical value to `4e-12`, so no
displayed digit depends on them.

## Two named conditions

**Mass scheme is a named residual, not a resolved one.** Everything here sits
inside one fixed scheme (MSbar); the invariance covers the reference scale
only. A scheme conversion is generally *not* a common rescaling. As an
illustration, applying the one-loop MSbar→pole factor
`1 + 4α_s(m_q)/3π + …` to the charm and top entries gives different factors
(`≈1.164` at `m_c` against `≈1.046` at `m_t`) and moves `r_up` by about
`−0.010`, roughly `4.5σ` of the propagated input error. This does not define a
light-quark pole mass or a complete pole-scheme sector; it only exhibits the
non-common character of the conversion. A framework-native dial target must
still name its scheme.

**The mass-to-dial dictionary is non-retained.** The values above are not
measured values of `r`. They are computed from PDG masses through the
C₃-circulant parametrization *together with* the identification of its
eigenvalues as one-leg amplitudes `√m` rather than masses.
[`QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md`](QUARK_C3_CIRCULANT_SOURCE_LAW_BOUNDARY_NOTE_2026-04-28.md)
records that identification verbatim among its "non-retained inputs" (`P1`).
The exact content above is unaffected — it concerns a defined function of three
masses and holds whatever that function is later identified with — but any
reading of these numbers *as the framework's dial* is conditional on `P1`.

## What this buys the lane

The open gate's blocker is stated as a conjunction: a quark-mass lane needs a
sector-specific mass scheme/scale **and** a dial theorem. This separates the
two. Fixing a scheme leaves no residual freedom in the reference scale, so the
scale half of that conjunction is not an obstruction to defining the dial —
only to fixing `v₀`. The scheme half stands, unreduced. The separation follows
from the prior art cited below, not from anything first established here.

That is a narrowing, and a corrected set of comparators to aim at. It **does
not close** the open gate and supplies no part of a closing theorem.

## Prior art this note does NOT duplicate, and defers to

- Degree-0 homogeneity, and the rescaling invariance itself, are already in
  `CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11`,
  along with `Q = 1/3 + 2r/3` and `r = 1/2 ⟺ Q = 2/3`.
- Flavour-universality of QCD mass running is in
  `CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22` eq. (5.6).
- **The mixed-scale/common-scale distinction itself is prior art in the CKM
  lane**, and this note claims no part of it. `CKM_FIVE_SIXTHS_BRIDGE_SUPPORT_NOTE`
  already contrasts a "threshold-local self-scale comparator" against the
  common-scale comparison and sizes the difference;
  `QUARK_FIVE_SIXTHS_SCALE_SELECTION_BOUNDARY_NOTE_2026-04-28` already asks
  whether a separate scale-selection theorem is load-bearing for exactly that
  choice; and
  `CKM_DOWN_TYPE_SCALE_CONVENTION_AUDITED_SCOPE_NARROW_BOUNDED_NOTE_2026-05-10`
  already records that "a directly mixed surface must carry its scale
  prescription inside the mass/operator map." All this note adds is the
  bookkeeping observation that the quark open gate's displayed dial values are
  such a mixed surface.
- The C₃ circulant/character algebra and the Koide-cone equivalence are prior
  art cited by the open gate itself.
- That a single universal `r` cannot fit all three sectors is already recorded
  — and **quantified**, with a 15/15 exact runner — in
  [`FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md`](FOURTH_AXIOM_RG_SCALE_DYNAMICS_SCOPING_2026-06-05.md)
  §2.1, which tabulates the four sector moduli and their spread. This note
  neither restates nor re-quantifies it; it only supplies corrected inputs.

## What is and is not claimed

Claimed here, and nothing else: the exact sharpness witness with its multiset
counterexample, the `μ ≥ m_t` common-scale prescription, and the corrected
comparator values.

Of those three, the first is a one-line algebraic identity qualifying a
prior-art hypothesis, the second is a **convention** — a stipulation about
which reference scale to quote at, not a derived proposition — and the third
is floating-point comparator data that the runner tallies separately and that
supplies no premise. There is no premise-conditional algebraic proposition
here that this note establishes and that is not already prior art. That is why
the claim type is `meta` and not `bounded_theorem`: `retained_bounded` grade is
for algebraic claims with explicit named premises, and after the deferrals
above there is no such claim left to carry it.

## Dependency standing (disclosure)

None of the four load-bearing dependencies is currently retained-grade: the
quark open gate is `unaudited`/`open_gate`, the CKM scale-convention note is
`audited_conditional`, the C₃ circulant boundary note is `unaudited`, and the
charged-lepton DFT coordinate note is `audit_in_progress`. A retained-grade
claim could not chain through any of them. This note does not seek a
retained grade — it is typed `meta` — so it does not depend on that changing.
Grading is the audit lane's determination, not this note's.

## Non-claims

- This note **derives no quark mass**, no mass scale, no `v₀`, no Brannen
  phase, no sector weight, no species map, and no dial *value* from the
  framework. Every number is an external comparator.
- It **does not close** the quark-mass-spectrum open gate.
- It asserts no no-go, and makes no claim about why the sectors differ.
- It does not claim the dial is scheme-independent — see the named conditions.
- No claim that a common reference scale is *physically* preferred; only that
  the dial is constant across the common-scale class while mixed conventions
  give convention-dependent answers.
- Charged-lepton QED running is neglected, as it is in the open gate.
- Reconciling the open gate's own displayed values is left to that note's
  owners; nothing here edits it.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.

## Scope boundary

Three-generation sectors, real nonnegative generation coordinates, nonzero
coordinate sum; `Q` and `r` are undefined at `Σx = 0`, which the runner
excludes rather than samples. Symmetric `±1σ` finite-difference error
propagation from the sourced PDG-vintage inputs. Residual comparator
systematics are sized separately: the active-flavour convention shifts the
quoted 2 GeV `u,d,s` inputs, while neglected higher-order threshold matching
acts on flavours light at each crossed heavy threshold — represented by
`u,c` relative to `t` and `d,s` relative to `b`. With a deliberately common
`+0.3%` proxy amplitude, the former moves `r_down` by `4.2e-4` (`0.056σ`), and
the latter moves `r_up` by `3.1e-4` (`0.14σ`); both remain comparator-only
residuals below one propagated input sigma.

## Reproduce

```bash
python3 scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py
```

Load-bearing parts are standard library only — `fractions.Fraction` and
integers, no floating point, no randomness. The comparator part is tallied
separately and supplies no premise.
