# PMNS θ_23 Upper-Octant Chamber-Closure — Narrow Bridge Theorem

**Date:** 2026-05-17
**Claim type:** bounded_theorem (narrow rescope citing the Krawczyk
chamber-margin certificate)
**Status authority:** independent audit lane only. This source note does
not set or move its own audit verdict; downstream audit lane and packet
status are decided by the audit lane.
**Primary runner:**
[`scripts/frontier_pmns_theta23_upper_octant_chamber_closure_narrow.py`](../scripts/frontier_pmns_theta23_upper_octant_chamber_closure_narrow.py)
**Source-note proposal:** audit verdict and downstream status set only by
the independent audit lane.
**Authority role:** narrow rescope of the chamber-closure threshold
identity of the parent prediction note, with the rigorous-existence step
backed by a retained interval-arithmetic certificate rather than
multistart numerics.
**Framework baseline:** physical `Cl(3)` local algebra on the `Z^3`
spatial substrate.

## 0. Why this note exists

The parent prediction note
[`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
records the structural feature: requiring the affine chamber-pin

```text
Phi : (m, delta, q_+) -> (sin^2 theta_12, sin^2 theta_13, sin^2 theta_23)
```

to reproduce the PDG 2024 / NuFit 5.3 central triple has a chamber-
interior solution at (m_*, delta_*, q_*) approximately equal to
(0.6571, 0.9338, 0.7150) with chamber margin

```text
q_* + delta_* - sqrt(8/3) approximately equal to +0.0159 > 0.
```

As `sin^2 theta_23` is decreased at fixed `(sin^2 theta_12, sin^2
theta_13) = (0.307, 0.0218)`, the chamber margin decreases continuously,
reaches zero at a threshold `s_23^2 = s_23^2_min approximately equal to
0.541`, and turns negative below threshold (no chamber-interior closure).
Because `0.541 > 0.5`, the chamber closure forces `s_23^2` in the upper
octant.

In the parent note the chamber-interior step is supported by `fsolve`
multistart on the pin equations and by `brentq` on the boundary-distance
function. The certificate
[`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
(ledger row
`dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16`)
replaces the
multistart "Basin 1 lies inside the chamber" step by an explicit
Krawczyk-interval inclusion: the chamber margin over the Krawczyk box of
radius `10^-6` around the Basin 1 candidate is the interval

```text
q + delta - sqrt(8/3) in [+1.5849 * 10^-2, +1.5862 * 10^-2]
```

at 200-bit mpmath precision. The chamber-margin sign at the PDG-central
anchor is therefore a certified positive interval, not a multistart
finding.

This narrow note records, with explicit (X1, X2, X3, X4) -> conclusion
labelling, exactly which already-retained authorities back which step of
the chamber-closure threshold, and demarcates exactly what is rigorously
forced and what remains a conditional structural feature.

## 1. Cited authorities and their roles

Each cited authority is named together with the role it plays in the
narrow theorem below.

- **(X1) Chamber-margin existence certificate at the PDG-central anchor.**
  [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  fixes the chamber-side sign at
  the Basin 1 candidate: the interval-arithmetic evaluation of
  `q + delta - sqrt(8/3)` over the Krawczyk box of radius `10^-6` around
  Basin 1 is `[+1.5849 * 10^-2, +1.5862 * 10^-2]`. Its role here is to
  supply a certified positive lower bound `+1.5849 * 10^-2` for the
  chamber margin at the PDG-central anchor. The certificate's scope is
  exactly this anchor-side sign; it does not state anything about
  s_23^2-sweeps off the anchor.
- **(X2) Bounded forward-cycle coordinate extraction.**
  [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  supplies that, for an explicitly supplied `3 x 3` block, the projected
  forward-cycle coordinates are the diagonal of `A C^dagger` in the displayed
  cycle basis. Its role here is limited to algebra on the separately supplied
  chamber chart `H(m, delta, q_+) = H_base + m T_m + delta T_delta + q_+ T_q`
  and does not derive a physical `hw=1` carrier or readout
  on the active block, so that the chamber chart used in the prediction
  is the same chart the audit lane already retains.
- **(X3) NuFit 5.3 NO 3-sigma box on (s_12^2, s_13^2, s_23^2).**
  This is a NAMED EXTERNAL ADMISSION, not a derived target: the
  experimental rectangle
  `s_12^2 in [0.270, 0.341]`,
  `s_13^2 in [0.02029, 0.02391]`,
  `s_23^2 in [0.434, 0.610]`
  enters as the comparison box for falsifiability statements. No value
  inside the box is load-bearing on the algebraic identities below; the
  box is the post-derivation interval against which the threshold
  surface is compared.
- **(X4) Distinct translation-character algebra on the hw=1 triplet.**
  [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies three diagonal involutions on `C^3` with three
  distinct joint sign characters and the rank-1 sector projectors. Its
  role here is to keep the affine chamber chart's action on the hw = 1
  triplet anchored to the retained three-generation structure rather
  than to an alternative diagonal choice.

The chamber-boundary line `q + delta = sqrt(8/3)`, the Schur-Q algebraic
identity `2 * sqrt(6)/3 = sqrt(8/3)`, and the IVT structural feature on
the smooth pin map are not themselves cited as authorities; they are
purely algebraic content of this note.

## 2. Narrow theorem (explicit hypotheses)

**Theorem (chamber-closure threshold forces upper octant).**

Given

- **(X1)** the Krawczyk-certified chamber-margin lower bound at the
  PDG-central Basin 1 anchor,
  `q + delta - sqrt(8/3) >= +1.5849 * 10^-2 > 0`;
- **(X2)** the bounded coordinate identity on the separately supplied chamber
  chart;
- **(X3)** the NuFit 5.3 NO 3-sigma rectangle as named external admission
  on `(s_12^2, s_13^2, s_23^2)`;
- **(X4)** the distinct translation-character algebra on the hw = 1
  triplet,

the chamber-boundary identity, Schur-Q coincidence, and the IVT
structural feature of the chamber-closure threshold satisfy

1. **(Algebraic; sympy-exact) Chamber-boundary identity.**
   `sqrt(8/3) = 2 * sqrt(6)/3` as algebraic numbers in
   `Q(sqrt(2), sqrt(3), sqrt(6))`; equivalently
   `(sqrt(8/3))^2 = 8/3` and `(2 * sqrt(6)/3)^2 = 8/3`. The chamber-
   boundary line `q + delta = sqrt(8/3)` in the `(delta, q)`-plane
   passes through the Schur-Q point
   `(delta_S, q_S) = (sqrt(6)/3, sqrt(6)/3)` exactly.
2. **(Algebraic; sympy-exact) PDG-central anchor sits on the strict
   interior side of the chamber boundary.** Substituting the parent
   prediction note's anchor
   `(delta_*, q_*) = (0.93380634, 0.71504233)` gives
   `q_* + delta_* - sqrt(8/3) approximately equal to +0.01594`. The
   Krawczyk-certified interval `[+1.5849 * 10^-2, +1.5862 * 10^-2]`
   contains this value; in particular the chamber margin at the anchor
   is bounded below by a STRICTLY POSITIVE constant `+1.5849 * 10^-2`.
3. **(IVT; structural) Chamber-boundary saturation forces a threshold
   below the PDG-central s_23^2 = 0.545.** The chamber-margin function
   `m(s_23^2) := q(s_23^2) + delta(s_23^2) - sqrt(8/3)` along the smooth
   one-parameter family obtained by varying `s_23^2` at fixed `(s_12^2,
   s_13^2) = (0.307, 0.0218)` is continuous in `s_23^2`. At
   `s_23^2 = 0.545`, by (2), `m(0.545) >= +1.5849 * 10^-2 > 0`. The
   parent prediction note records `m(0.520) approximately equal to
   -0.0782 < 0` at the multistart-supported lower endpoint. Continuity
   + sign change on `[0.520, 0.545]` (intermediate value theorem) forces
   the existence of `s_23^2_min in (0.520, 0.545)` with
   `m(s_23^2_min) = 0`, hence `s_23^2_min > 0.500`. The point
   `s_23^2_min` is the chamber-closure threshold; below threshold no
   chamber-interior closure exists at PDG-central (s_12^2, s_13^2).
4. **(Conclusion under the named external admission) Upper-octant
   prediction.** Under the named external admission (X3), the chamber-
   closure threshold at the PDG-central (s_12^2, s_13^2) sits strictly
   above maximal mixing `s_23^2 = 0.500`. The NuFit 5.3 upper-octant
   best-fit `s_23^2 = 0.568 > s_23^2_min` is consistent with chamber
   closure; the NuFit 5.3 lower-octant alternative `s_23^2 = 0.445 <
   0.500 < s_23^2_min` is inconsistent with chamber closure. The
   chamber-closure prediction is therefore "theta_23 in the upper
   octant" with the falsifier "a future global fit settling on
   `s_23^2 < 0.500` at >3-sigma."

## 3. Proof sketch

(1) is direct algebra. Squaring `2 * sqrt(6)/3` gives `4 * 6 / 9 = 8/3`,
which is also the square of `sqrt(8/3)`; both are strictly positive, so
they are equal. The Schur-Q point `(sqrt(6)/3, sqrt(6)/3)` has
`delta + q = 2 * sqrt(6)/3 = sqrt(8/3)`, hence lies on the chamber-
boundary line. Sympy verifies the equality via `simplify` to zero.

(2) is direct substitution of the parent prediction note's anchor into
the chamber-margin function plus interval comparison against the
Krawczyk-certified interval. The interval-arithmetic certificate (X1) is
a 200-bit mpmath certificate at radius `10^-6` around the Basin 1
candidate; the parent-runner numerical anchor sits comfortably inside
that box. The sympy companion checks the floating-point margin against
the certified interval endpoints.

(3) is the intermediate value theorem applied to a continuous function on
a closed interval. Continuity of `m(s_23^2)` follows from continuity of
the `eigh` map on smooth Hermitian families plus continuity of
permutation-aware angle extraction inside any open chamber-interior
neighbourhood of the PDG-central anchor, which is the smoothness regime
established by the chamber chart of (X2) on the hw = 1 triplet (X4). The
positive endpoint is certified by (X1)+(2); the negative endpoint is the
parent prediction note's multistart-supported finding at `s_23^2 = 0.520`
and is not strengthened here.

(4) is the labeling step: `s_23^2_min > 0.500` by (3), so any
`s_23^2 < 0.500` is below threshold; the NuFit upper-octant best-fit
`0.568 > s_23^2_min`; the NuFit lower-octant alternative `0.445 < 0.500`
is below threshold. The named external admission (X3) is the rectangle
inside which the comparison is meaningful.

## 4. Scope versus the parent prediction note

| Parent prediction claim | Parent support | This narrow note |
|---|---|---|
| s_23^2_min `approximately equal to` 0.541 (12-digit brentq) | brentq + fsolve multistart | bracketed existence in (0.520, 0.545) by IVT + Krawczyk endpoint |
| Threshold surface in `[0.5335, 0.5476]` over 3-sigma rectangle | fsolve multistart per grid point | not in scope; only the central-point bracket is certified |
| Schur-Q lies on the chamber-boundary line | parent runner numerical | (1), algebraic, sympy-exact |
| Chamber-boundary `q + delta = sqrt(8/3)` | parent runner numerical | (1), algebraic, sympy-exact |
| Chamber-interior pin at PDG central | fsolve | (2), Krawczyk-certified lower bound `+1.5849 * 10^-2` |
| Upper-octant prediction `theta_23 > pi/4` | parent runner numerical conditional | (4), forced by IVT + Krawczyk |

So this narrow note closes the central-anchor side of the threshold
identity rigorously (chamber margin at PDG-central is certified
positive; chamber-boundary line is sympy-exact) and demarcates the
threshold-surface side as out of scope. The "exact value" `0.540970` of
the threshold at PDG-central is NOT claimed here as rigorous; only its
existence and its upper-octant location are.

## 5. What is forced versus what remains conditional

What this narrow theorem forces (under X1, X2, X3, X4):

- The chamber-boundary line `q + delta = sqrt(8/3)` is algebraic and
  passes through Schur-Q exactly (closed-form).
- The chamber margin at the PDG-central pin is bounded below by a
  certified positive constant `+1.5849 * 10^-2`.
- A chamber-closure threshold `s_23^2_min` exists in the open interval
  `(0.520, 0.545)` by IVT on the chamber-margin function.
- `s_23^2_min > 0.500` strictly, so chamber closure forces `s_23^2` in
  the upper octant at PDG-central `(s_12^2, s_13^2)`.

What remains conditional (out of scope for this narrow note):

- The exact numerical value `s_23^2_min = 0.540970` at PDG-central; only
  the bracket `(0.520, 0.545)` is rigorously established here.
- The threshold surface over the full 3-sigma rectangle on `(s_12^2,
  s_13^2)`; only the central-point bracket is certified.
- The smoothness statement on the closure map is itself a multistart-
  supported regime claim; this note's IVT uses continuity inside an open
  chamber-interior neighbourhood, not the full smoothness story.
- The lower-endpoint chamber-outside sign at `s_23^2 = 0.520` is
  inherited from the parent prediction note's multistart finding and is
  not strengthened here. The IVT is conditional on this endpoint sign.

## 6. What this note positively claims

1. Algebraic identity `sqrt(8/3) = 2 * sqrt(6)/3` (and corresponding
   Schur-Q chamber-boundary incidence) as a closed-form statement in
   `Q(sqrt(2), sqrt(3), sqrt(6))`.
2. Interval comparison: parent prediction note's PDG-central anchor
   chamber margin lies inside the Krawczyk-certified interval
   `[+1.5849 * 10^-2, +1.5862 * 10^-2]`, hence is bounded below by
   `+1.5849 * 10^-2 > 0`.
3. IVT-based existence of `s_23^2_min in (0.520, 0.545)` with
   `s_23^2_min > 0.500`.
4. Upper-octant labeling under (X3): chamber closure at the PDG-central
   anchor forces `s_23^2 > 0.500`.

## 7. What this note does NOT claim

- Does NOT derive the chamber chart `H(m, delta, q_+) = H_base + m T_m
  + delta T_delta + q_+ T_q`, which is an inherited construction from
  the prediction note's chamber chart.
- Does NOT supply or assume any PDG / NuFit value other than as the
  named external admission (X3).
- Does NOT strengthen the Krawczyk certificate (X1) beyond its stated
  scope; in particular does NOT claim a global completeness result on
  the chamber-spectral root set.
- Does NOT claim `s_23^2_min = 0.540970` to any specified number of
  digits; only the open bracket `(0.520, 0.545)` is rigorous here.
- Does NOT claim threshold-surface flatness or upper-octant retention
  off the PDG-central `(s_12^2, s_13^2)`; only the central-point case is
  in scope.
- Does NOT alter or supersede the parent prediction note's status; this
  is a narrow rescope.

## 8. Cited dependencies (markdown links for retained authorities)

- [`DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md`](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md)
  — (X1) Krawczyk-interval chamber-margin certificate at the PDG-central
  Basin 1 anchor.
- [`PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md`](PMNS_ORIENTED_CYCLE_CHANNEL_VALUE_LAW_NOTE.md)
  — (X2) bounded coordinates on an explicitly supplied `3 x 3` block; no
  physical carrier/readout or chart-selection bridge.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — (X4) distinct-character diagonal involutions and rank-1 sector
  projectors on the hw=1 triplet.
- [`PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md`](PMNS_THETA23_UPPER_OCTANT_CHAMBER_CLOSURE_PREDICTION_NOTE_2026-04-17.md)
  — parent prediction note; the present note isolates the
  central-anchor existence-side step of that prediction.

External admission (named per `feedback_no_new_axioms.md` legitimate-
import path):

- NuFit 5.3 NO 3-sigma rectangle on `(s_12^2, s_13^2, s_23^2)`. Source:
  NuFit 5.3 published tables, used as the comparison box for the
  upper-octant labeling step. No value inside the rectangle is load-
  bearing on the algebraic identities in this note.

## 9. Forbidden-imports check

- No new repo-wide axiom introduced. The Krawczyk certificate is a cited
  authority; X2 is only bounded supplied-block coordinate algebra and is not
  treated here as a retained physical value/readout law.
- No new repo vocabulary introduced; "chamber margin," "chamber-boundary
  line," and "upper-octant prediction" are taken directly from the
  parent prediction note's terminology.
- No PDG / NuFit observable consumed as a derived value; the rectangle
  is the named external admission for the comparison-box step only.
- Status authority remains the independent audit lane.
- No load-bearing reliance on any authority outside the parent
  prediction note for the central-anchor numerical coordinates that the
  Krawczyk interval certifies.
- Citation form: retained authorities cited as `[NAME.md](NAME.md)`;
  backtick form used only for ledger row identifiers.

## 10. Reproduction

```bash
PYTHONPATH=scripts python3 \
    scripts/frontier_pmns_theta23_upper_octant_chamber_closure_narrow.py
```

Expected final line:

```text
PASS=<N>  FAIL=0
```

The runner verifies:

- (S1) Algebraic identity `sqrt(8/3) = 2 * sqrt(6)/3` via sympy
  `simplify` to zero.
- (S2) Schur-Q point lies on the chamber-boundary line `q + delta =
  sqrt(8/3)` (sympy-exact).
- (S3) Parent prediction note's PDG-central anchor `(delta_*, q_*)`
  gives chamber margin inside `[+1.5849 * 10^-2, +1.5862 * 10^-2]`.
- (S4) Lower bound `+1.5849 * 10^-2` is strictly positive.
- (S5) PDG-central s_23^2 = 0.545 endpoint chamber margin > 0 (by the
  Krawczyk lower bound).
- (S6) Parent-note lower endpoint at s_23^2 = 0.520 chamber margin < 0
  (numeric; inherited; reproduced).
- (S7) IVT brackets `s_23^2_min in (0.520, 0.545)`.
- (S8) `s_23^2_min > 0.500` strictly.
- (S9) NuFit upper-octant best-fit `0.568 > s_23^2_min` (consistent).
- (S10) NuFit lower-octant alternative `0.445 < 0.500 < s_23^2_min`
  (inconsistent).
- (S11) Lower bound on the chamber-margin gap, propagated through the
  Krawczyk endpoint, leaves at least `+1.5 * 10^-2` of headroom against
  s_23^2 = 0.545.
- (S12) Sanity: `q_* + delta_*` computed at the parent anchor matches
  the floating-point chamber-margin readout to 1e-8.

The runner is a pure-Python sympy + `mpmath` script (no scipy, no
`numpy.linalg.eigh`), so the certified-sign step is reproducible
under interval arithmetic at 200-bit precision.

## 11. Cross-references

- `pmns_theta23_upper_octant_chamber_closure_prediction_note_2026-04-17`
  — parent prediction note.
- `dm_pmns_chamber_spectral_completeness_krawczyk_certificate_note_2026-05-16`
  — (X1).
- `pmns_oriented_cycle_channel_value_law_note` — (X2).
- `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10`
  — (X4).
