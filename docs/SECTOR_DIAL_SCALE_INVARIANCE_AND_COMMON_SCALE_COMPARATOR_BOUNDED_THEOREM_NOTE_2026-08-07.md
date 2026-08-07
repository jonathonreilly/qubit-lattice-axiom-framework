# The C₃ Sector Dial Is Invariant Under a Common Mass Rescaling, So Within a Fixed Mass Scheme It Is Reference-Scale-Free (Bounded Theorem + Comparator Correction)

**Date:** 2026-08-07
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** proposed_retained
**Status authority:** independent audit lane only. This source note does not
set, predict, or apply an audit outcome, and edits no registry.
**Primary runner:**
[`scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py`](../scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py)
**Cached runner output:**
[`logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt`](../logs/runner-cache/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.txt)

## Question

[`QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md`](QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md)
opens the quark lane with a warning: quark masses are renormalization-scheme
and scale dependent, so "any numerical comparison must make the quark mass
scheme explicit," and its own displayed quark dials are labelled
"observational comparators only" under a "packet-local central-value
comparator convention."

That warning is correct as stated. This note asks the sharper question it
leaves open:

> Once a mass **scheme** is fixed, does the **dial** `(r, δ)` still depend on
> the reference **scale** at which the three masses are quoted?

The answer is no, and that is a strictly narrower result than "the dial is
convention-free". The dial is invariant under any common rescaling of a
sector's three masses, and flavour-universal QCD running *within a fixed
scheme* is exactly such a rescaling. So, **given a scheme**, the dial has a
single value per sector, independent of which common reference scale is
chosen.

This does **not** make the dial scheme-independent. A change of mass scheme is
generally *not* a common rescaling: the MSbar→pole conversion factor
`1 + 4α_s(m_q)/3π + …` depends on `α_s` at the quark's own mass and so differs
per generation (≈`1.164` at `m_c` against ≈`1.046` at `m_t` for the inputs
below). Converting the up-type sector to pole masses moves `r_up` by about
`−0.010`, about `4.5σ` of the PDG-propagated input error. Scheme choice therefore
remains a live convention; only the reference scale inside a scheme is free.
See the scope boundary.

The practical consequence for the open gate is that its displayed numbers do
not measure the dial: they mix reference scales (and, in the up-type sector, a
pole mass with MSbar masses), and re-quoting with unequal per-generation
factors is precisely the operation the invariance does *not* cover.

## Setting

For three generation coordinates `x_k = sqrt(m_k)` with `S = Σ x_k ≠ 0`, the
Brannen/C₃ circulant parametrization is `x_k = a + 2|b| cos(δ + 2πk/3)` with
`a = S/3`, and the dial is `r = |b|²/a²`, `δ = arg b`, with
`Q = Σm_k / S² = (1 + 2r)/3`.

Ordering `x_0 ≥ x_1 ≥ x_2`, the Fourier coefficient
`b = (1/3) Σ_k x_k ω^{-k}` (with `ω = e^{2πi/3}`) has

```text
C = Re(b)/a        = (x_0 - (x_1 + x_2)/2) / (3a)
J = Im(b)/(a·√3)   = (x_2 - x_1) / (6a)
r = C² + 3J²       δ = atan2(√3·J, C)
```

`C` and `J` are **rational** in the `x_k`, so the whole dial is pinned by an
exact rational pair. The runner's load-bearing checks take no square roots and
use no floating point.

## Theorem

### T1 — homogeneity (exact)

`Q`, `r`, `C`, and `J` are unchanged under `m_k ↦ λ m_k` for every `λ > 0`,
equivalently `x_k ↦ μ x_k` with `μ = √λ`. Each is a ratio of forms of equal
degree in `x`, so `μ` cancels identically. Since `μ > 0` preserves the
descending order, the ordering convention is applied to the same ordering
before and after.

This is elementary and is **not claimed as new**. Degree-0 homogeneity of the
Koide ratio is standard, and — more directly — the invariance itself is
already stated in the repo:
[`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)
records that `r` "is invariant under every permutation of the mass triple and
under a common positive rescaling of all three masses", along with
`Q = 1/3 + 2r/3` and `r = 1/2 ⟺ Q = 2/3`. T1 adds nothing to that statement
beyond carrying it through the explicit rational pair `(C, J)`, and it is
reproduced here only because T3 and the comparator need those same
coordinates.

### T2 — flavour-universal running is a common rescaling (supplied condition)

**Supplied, not derived:** in QCD the MSbar mass anomalous dimension `γ_m`
depends on the coupling and the active flavour number only, not on which quark
is being run, so on a fixed-flavour surface

```text
m_q(μ) = R(μ, μ₀) · m_q(μ₀)   with one R for every q in the sector.
```

This is already recorded in the repo at
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
eq. (5.6), which uses it for mass *ratios*. Applying it to the dial is
immediate from T1 with `λ = R`: **a sector's dial does not depend on the
common reference scale.**

The same universality survives flavour thresholds, with one precision that
matters. The decoupling coefficient `ζ_m` relating `m_q^{(n_f)}` to
`m_q^{(n_f-1)}` depends on the decoupled heavy mass, the coupling and `μ` —
not on `q`. So every sector member that *crosses* a given threshold receives
the **same** `ζ_m`.

It does not follow that the accumulated decoupling is common to the sector,
and in the transport used here it is not: members starting above a threshold
never cross it. Running to `μ = 1000 GeV`, `m_u` and `m_c` each cross `m_b`
and `m_t`, `m_b` crosses only `m_t`, and `m_t` crosses nothing. Those
accumulated factors differ per generation and are therefore an unequal
rescaling in exactly T3's sense.

This does **not** affect the invariance claim, which is the statement that
moving between two common scales *both at or above `m_t`* leaves the dial
fixed — that move crosses no threshold at all, so `R` is genuinely common and
T2 applies exactly. It affects only the accuracy of transporting mixed-scale
*inputs* onto the common scale, where the residual is the neglected
higher-order decoupling (`ζ_m = 1 + O(α_s²)`) itemized in the scope boundary
and bounded numerically by the runner. See the scope boundary for the
canonical `μ ≥ m_t` prescription.

### T3 — sharpness: T1's equal-factor hypothesis cannot be dropped (exact)

A **mixed-scale** convention quotes different generations at different
reference scales. That applies `m_k ↦ λ_k m_k` with the `λ_k` not all equal,
which is outside T1's hypothesis. T3 shows that hypothesis is doing real work
rather than being a removable technicality:

*Lemma (exact).* On the triple `x = (1, 1, 0)`, scaling the two nonzero
coordinates by `μ₁, μ₂` gives `Q = (μ₁² + μ₂²)/(μ₁ + μ₂)²`, and

```text
2(μ₁² + μ₂²) − (μ₁ + μ₂)²  =  (μ₁ − μ₂)² ,
```

so `Q` returns its unscaled value `1/2` **iff** `μ₁ = μ₂`. On this triple, any
unequal pair of factors applied to the two nonzero coordinates moves `Q`. The
runner also exhibits strictly positive, nondegenerate rational triples on which
unequal factors move both `Q` and `r`, with the before/after values displayed
as exact fractions.

**This is a sharpness witness, not a converse, and the distinction is
load-bearing.** The literal converse — "the dial is unchanged ⟹ the `λ_k` are
all equal" — is **false**, and the runner now exhibits exact counterexamples so
the stronger reading cannot be reinstated by accident:

- on this note's own witness triple `x = (1, 1, 0)`, the factors `(1, 1, 7)`
  are unequal but act on a zero coordinate and fix the dial exactly;
- on the strictly positive, nondegenerate triple `x = (4, 2, 1)`, the factors
  `(1/4, 1, 4)` permute the multiset back onto itself and leave `Q`, `r`, `C`
  and `J` *exactly* unchanged.

So unequal factors are not *guaranteed* to move the dial; what T3 establishes
is that they are not *protected* from moving it. That is all the argument
below needs: a mixed-scale re-quoting carries no invariance guarantee, so it
cannot be assumed to measure the dial, and in the quark case the comparator
shows it demonstrably does not.

Accordingly, "the dial is scale-free" is true for the common-scale class and
carries no guarantee outside it. There is nothing to choose *within* the
common-scale class; the choice *between* common-scale and mixed-scale is not a
free convention, because only the former is covered by T1.

## What this does to the open gate's numbers (comparator)

Everything in this section is a **comparator**. It uses external PDG central
values and floating point, is not exact, is not a derivation step, and
supplies no premise. T1–T3 stand without it.

Reading PDG-style inputs at the open gate's quoted (mixed) reference points
versus at any common scale:

```text
                                      r_up       r_down
open-gate note's displayed           0.773642    0.597141   (mixed; pole top)
same inputs, MSbar top m_t(m_t)      0.767630    0.597141   (mixed scales only)
common-scale, scale-invariant        0.830971    0.621090
  total shift from displayed          +0.0573     +0.0239
```

The runner reproduces the open gate's two displayed values to six decimals
from that note's own quoted mass list, which confirms the convention being
compared is the one it actually used.

One detail matters for attribution of the shift. The open gate's up-type list
is `[0.00216, 1.27, 173.0] GeV`: `m_u` and `m_c` are MSbar, but `173.0` is the
**pole** top mass. Its up-type convention is therefore mixed-*scheme* as well
as mixed-scale, and the `+0.0573` in `r_up` bundles both effects. Isolating
them, the pole→MSbar top replacement accounts for about `−0.0060` and the
mixed→common-scale move for about `+0.0633`. The down-type list is MSbar
throughout, so its `+0.0239` is a pure reference-scale effect.

With linear error propagation from PDG input uncertainties, the common-scale
dials are

```text
sector          Q                      r
charged lepton  0.666660511            0.499990767      (no QCD running)
up-type         0.887314 ± 0.001469    0.830971 ± 0.002204
down-type       0.747393 ± 0.004890    0.621090 ± 0.007335
```

and the six-common-scale invariance table agrees to float noise
(`2.4e-12` and `4.4e-16` spread in `Q` across `μ = 2 GeV … 1 TeV`).

These are quoted at `μ = M_Z` for continuity with the table above. `M_Z` is
below `m_t`, so it is one of the display-only rows; it agrees with the
canonical `μ ≥ m_t` value to `4e-12`, well below the last displayed digit.
See the scope boundary for the canonical prescription.

## What this buys the lane

The open gate's live blocker is stated as: "a retained positive quark-mass
spectrum lane must first supply a sector-specific mass scheme/scale **and**
quark dial theorem."

T1–T3 narrow that conjunction, and it is worth being precise about how much.
The dial half is not **scale**-blocked: once a mass scheme is fixed, no
framework-native choice of *reference scale* is needed to give a sector's
`(r, δ)` a well-defined value — only the discipline of quoting all three
masses of the sector at one common scale. What is *not* removed is the scheme
choice itself: as shown above, MSbar versus pole is not a common rescaling and
moves `r_up` at the `4.5σ` level. So the residual requirement on the dial half is
"fix one scheme", not "fix a scheme *and* a scale".

The `v₀` half — the overall scale that turns a dial into masses — is untouched
and remains fully open.

That is a narrowing of an open gate, not a closing of it. Nothing here derives
a quark dial from the framework; it says only that, once a scheme is named, the
target the framework would have to hit is a single well-posed number rather
than a whole family indexed by an arbitrary reference scale.

It also sharpens an existing negative direction without adding a new one: the
three sector dials sit at `0.4999907`, `0.6211 ± 0.0073`, `0.8310 ± 0.0022`,
which are `17σ` and `150σ` from the leptonic `1/2` when only PDG input errors
are propagated. Those quoted `σ` are input-error bars, not total errors: they
exclude the scheme systematic above. T1–T3 remove the *reference-scale* choice
as an explanation of the spread, and the scheme systematic is a `4.5σ`-scale
effect against a `17σ`/`150σ` separation — but "the spread survives the
conventions examined here" is the honest statement, not "the spread cannot be
convention". Whether it forbids any particular sector-blind supply of `r` is a
question for a no-go note under the negative gate, and is **not** claimed here.

## Prior art this note does NOT duplicate, and defers to

- Degree-0 homogeneity of `Q` is standard textbook Koide algebra and is not
  claimed as new.
- **T1 in full** — invariance of `r` under a common positive rescaling (and
  under permutations), together with `Q = 1/3 + 2r/3` and `r = 1/2 ⟺ Q = 2/3` —
  is repo prior art, stated in those words in
  ([`CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md`](CHARGED_LEPTON_REGISTERED_MASS_DFT_COORDINATE_THEOREM_NOTE_2026-07-11.md)).
  T1 is a restatement in `(C, J)` coordinates, not a new result, and the
  title's first clause should be read as recalling that prior art rather than
  claiming it.
- Flavour-universality of QCD mass running is repo prior art
  ([`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
  eq. 5.6), there applied to mass ratios rather than to the dial. It enters
  here as a **supplied physics condition**, not as something derived.
- The general observation that a *mixed* quantity — one whose components are
  read at different reference points — carries an extra scale prescription is
  also prior art in that same note, immediately below eq. 5.6 ("a bridge stated
  directly on that mixed ratio already contains an additional scale/readout
  prescription"). This note does not claim that principle; it applies it to the
  `C₃` dial and to one specific comparator convention.
- The `C₃` circulant/character algebra and the Koide-cone equivalence are
  prior art cited by the open gate itself and are not re-derived.

The content claimed here is narrower than the title alone suggests:
**T3** as a *sharpness* witness (with the exact identity, and the exact
counterexamples showing the literal converse fails), the identification that
the open gate's comparator convention is mixed-scale — and, in the up-type
sector, mixed-scheme — and therefore is not covered by T1, the corrected
common-scale comparator values, and the resulting narrowing of the open gate's
stated blocker from "scheme and scale" to "scheme only" on the dial half.

## Dependency standing (disclosure)

At the time of writing, the three notes this one links are not all
retained-grade in the pipeline-derived view: the quark-mass open gate is an
`open_gate` and still unaudited, the CKM scale-convention note carries a
terminal conditional audit outcome, and the charged-lepton DFT coordinate note
is retained but with an audit in progress. Grade is pipeline-derived after
independent ratification and dependency closure; this note asserts none of it.

Nothing here silently inherits retained grade from those rows:

- T1 and T3 are self-contained exact algebra; they need no premise from any of
  the three, and the DFT note is cited as prior art for attribution, not as a
  load-bearing premise.
- T2 is declared a **supplied physics condition**, not a result inherited from
  the CKM note. That note is cited as the place the same condition is already
  recorded. This supplied condition is the reason the claim type here is
  `bounded_theorem` rather than `positive_theorem`.
- The open gate is the **subject** of the comparator correction, not a premise
  of it.

A reader or auditor should therefore expect the chain-derived grade of this row
to be limited by those dependencies, and should not read the author-side
`proposed_retained` line as a prediction of the outcome.

## Non-claims

- This note **derives no quark mass**, no mass scale, no `v₀`, no quark
  Brannen phase, no sector weight, no species map, and no dial *value* from
  the framework. Every number in the comparator section is external.
- This note **does not close** the quark-mass-spectrum open gate, and supplies
  no part of a closing theorem.
- This note asserts **no** no-go. The `17σ`/`150σ` sector spread is displayed
  as a comparator; converting it into a negative claim about any candidate
  supply of `r` is separate work under the negative gate and is not attempted.
- This note does **not** claim the dial is scheme-independent, and it is not.
  Only the reference scale *within* a fixed scheme is shown to drop out. A
  scheme change is generally not a common rescaling and moves the dial; the
  quoted MSbar→pole size is itself a comparator, not a bound.
- No claim is made that a common reference scale is *physically* preferred.
  The claim is narrower: the dial is constant across the common-scale class,
  so that class has a single well-defined answer, while a mixed-scale
  convention carries no such guarantee.
- T3 is **not** a converse of T1 and is not claimed as one. Unequal
  per-generation factors are not guaranteed to move the dial — exact
  counterexamples are exhibited — only not guaranteed to preserve it.
- Charged-lepton QED running is neglected in the comparator, as it is in the
  open gate.
- No axiom, approved primitive, registry entry, or audit verdict is added,
  edited, retired, or predicted. The Tier-A count is unchanged.

## Scope boundary

Three-generation sectors, real nonnegative generation coordinates, nonzero
coordinate sum. `Q` and `r` are undefined at `Σx = 0`, which the runner
excludes rather than samples.

**Canonical prescription (load-bearing).** The common scale must be one at
which all three masses of the sector are legitimate active-flavour MSbar
masses. A quark below its *own* threshold is decoupled, so the common scale
must satisfy `μ ≥ m_Q` for the heaviest member `Q` of the sector: `μ ≥ m_t`
for up-type and `μ ≥ m_b` for down-type. **Taking `μ ≥ m_t` satisfies both
sectors simultaneously and is the prescription this note adopts.**

At `μ ≥ m_t` every mass is transported *upward* only, so at each threshold it
crosses it is a light (active) flavour — no sector member is ever the decoupled
one, and T2's hypothesis holds with no extrapolation. The runner segments each
upward run at the crossed thresholds with the correct active-flavour number
(for `μ = 1000 GeV`: `m_u` over `n_f = 4, 5, 6`; `m_c` over `4, 5, 6`; `m_b`
over `5, 6`; `m_t` over `6`), which is verified explicitly in Part D6.

The sub-threshold rows of the invariance table are **display-only**:

```text
row (mu)     extrapolated below its own threshold
2 GeV        m_t (up-type)  and  m_b (down-type)
4.18, 10     m_t (up-type)
91.1876      m_t (up-type)
162.5, 1000  none -- canonical
```

Note that this bites the up-type sector in four of the six rows, including the
`μ = M_Z` row at which the error propagation above is quoted; the down-type
sector is affected only at `μ = 2 GeV`.

They are shown only to exhibit the invariance across three decades. No result
here depends on them: every display-only row agrees with the canonical
`μ ≥ m_t` value to `4e-12` or better, so quoting the central values and error
bars at `M_Z` rather than at `μ ≥ m_t` changes no displayed digit. The
canonical numbers are the `μ = 162.5` and `μ = 1000 GeV` rows.

**Mass scheme is a named residual, not a resolved one.** Everything here is
stated inside one fixed scheme (MSbar). The invariance covers the reference
scale only. Converting the up-type sector to pole masses moves `r_up` by about
`−0.010` (≈`4.5σ` of the PDG-propagated input error), because the conversion
factor `1 + 4α_s(m_q)/3π + …` is evaluated at each quark's own mass and so is
not common to the sector. A framework-native dial target must still name its
scheme.

Residual comparator systematics: the active-flavour convention attached to the
quoted 2 GeV light-quark masses, and neglected higher-order decoupling. These
act on only the subset of masses quoted at 2 GeV — `m_u` alone in the up
sector, `m_d` and `m_s` in the down sector — so they are themselves unequal
per-generation factors in the sense of T3 and are not protected by the
invariance. The runner now bounds them directly: a common `ζ_m`-style shift of
`+0.3%` on the 2 GeV masses moves `r_down` by `4.2e-4` (`0.06σ`) and `r_up` by
`1.0e-5` (`0.005σ`), and even a deliberately excessive `3%` shift stays inside
`0.6σ`. They are therefore well inside the quoted PDG input errors, which are
dominated by `m_s` in the down sector and `m_t` in the up sector.

## Reproduce

```bash
python3 scripts/frontier_sector_dial_scale_invariance_common_scale_comparator_2026_08_07.py
```

Parts A–C, the anti-overclaim guard C′, and the scope guards E are standard
library only — `fractions.Fraction` and integers throughout, no floating point,
no randomness. Part D is explicitly marked comparator-only and uses `math` for
the four-loop running. The runner prints the exact and comparator tallies
separately; only the exact tally is load-bearing, and Parts A–C′ do not read
any Part D value.
