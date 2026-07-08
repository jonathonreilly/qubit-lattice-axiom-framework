# WEP Source-Side Reduction, Finite-Spacing Boundary, and Scaling-Window Universality -- Bounded Theorem

**Date:** 2026-07-08
**Type:** bounded_theorem (with one exact negative boundary and one
constructive witness)
**Claim type:** bounded_theorem
**Claim scope:** On the declared free two-step surface with the composite
comparator of the composite-additivity companion note, this note (i) proves
that single-particle universality forces any species-blind rest-energy source
to be the universal function `F(x) = (1/2) sinh(2x)` up to one constant,
(ii) proves exactly that this forced source fails every equal-mass free
composite at finite lattice spacing, (iii) exhibits a constructive witness
that no function of composite rest energy alone can determine composite
inertial response, (iv) proves the scaling-window universality statement with
derived exponents, and (v) reduces the remaining exact-WEP question to the
identification of a source that reads the object's own inertial-response
coefficient -- a dynamical band property. It closes no EP row, adopts no
axiom, and sets no audit status.
**Status authority:** independent audit lane only, sets no audit status.
**Primary runner:**
[`scripts/wep_source_reduction_scaling_window_2026_07_08.py`](../scripts/wep_source_reduction_scaling_window_2026_07_08.py)
**Runner cache:**
[`logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt`](../logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt)

## Why This Note Exists

The Record-stiffness context-independence no-go leaves the source side open
as its third residual: a theorem deriving the gravitational source
coefficient from the same object that carries the inertial rest gap. The
weak-field interface note holds the coefficient identity (`EP-S3b`) as
supplied shared-coupling template data.

The mass-observable, inertial-closure, and composite-additivity companion
notes changed what that residual can mean. Rest gap and inertial response
are now two readouts of one datum through the species-independent universal
function `F`; the inertial response of composites is bandwidth-dominated
rather than additive in rest energy. This note assembles the source-side
consequences: what exact weak-equivalence would require, what is impossible
at finite lattice spacing, and what is recovered in the scaling window.

## Imports And Premises

Inherited by citation: the mass-observable note's I-DYN / I-MASS / I-TIME
surface and `F` identity; the inertial-closure note's I-EXT probe discipline
(the probe is never the gravitational coupling); the composite note's I-1D /
I-DIST / I-INT comparator surface and measured legs. New here: **EP-S3a**
(the bounded-support normalized source-readout and weak-field coupling form
of the 2026-06-16 interface note) is consumed as the additive readout shape
for composite sources. No new axiom, primitive, or Tier-A content is used.

## Statement

Let `m_gap = arcsinh(m)`, `M_I = m sqrt(1+m^2) = F(m_gap)`,
`F(x) = (1/2) sinh(2x)`.

**T1 - singles force `F` (exact).** A species-blind source functional
`G(rest gap)` gives exact single-particle universality (acceleration
`gamma G(m_gap)/M_I` independent of species) if and only if
`G = c F` for one constant: substituting `m = sinh(x)` gives
`m sqrt(1+m^2) = (1/2) sinh(2x)` identically (runner residual `0`). The
species-blind rest-energy source is therefore unique up to normalization.

**T2 - the forced source fails free composites (exact negative boundary).**
For an equal-mass free composite, rest energy adds (`2 m_gap`) while
inertial response adds (`2 M_I`), and

```text
    F(2 m_gap) / (2 F(m_gap)) = cosh(2 m_gap) > 1   for m > 0,
```

exactly (runner: identity residual `0`; positivity witness exact;
`cosh(2x) - 1 = 2x^2 + O(x^4)`). So the unique singles-exact source
over-sources every equal-mass free composite at finite spacing, with
fractional violation `2 m_gap^2` at leading order. No interaction import is
involved in this leg.

**T3 - same rest energy, different inertia (constructive witness).** Two
bound composites tuned by bisection to the same rest energy
`E_2(0) = 0.8661812851` (equal to `3.5e-13`) have inertial masses differing
by `47%`:

```text
    (m, U) = (0.5, 0.37250328):  M_comp = 1.5506,  E_B = 0.0962
    (m, U) = (0.6, 0.59883401):  M_comp = 2.9050,  E_B = 0.2715
```

Both extractions are size-valid (`kappa_L = 15` and `27` at `L = 64`;
re-verified within the runner's size-diagnostic discipline). Therefore no
function of composite rest energy alone -- `F` or any other -- determines
composite inertial response: any such source assigns these two objects the
same source value while their inertial masses differ by half. The witness
lives on the declared I-INT comparator family; its scope is stated in the
boundaries.

**T4 - scaling-window universality (the positive statement).** All candidate
couplings coincide in the window `m << 1`, `E_B / E_2(0) << 1`, with derived
leading exponents (runner sympy-exact):

```text
    mass-weighted vs inertial-weighted (singles):  (1/2) m^2 + O(m^4)
    linear-rest-gap vs F (singles):                (2/3) m_gap^2 + O(m_gap^4)
    free-composite F-violation:                    2 m_gap^2 + O(m_gap^4)
```

and, at a size-valid shallow bound state (`m = 0.05`,
`E_B / E_2(0) = 2.0%`, `kappa_L = 10.2`, `L = 1024`), the composite falls
within `4.1%` of the singles' exact rate under the inertial-weighted
additive source, inside the derived window bound
`5 (2 m_gap^2 + E_B/E_2(0)) = 12.7%`. Universal free fall holds in the
scaling window to the stated order; the binding trend is monotone for the
charge-counting violation (log-log slopes `0.83` and `0.73` against `E_B`)
and consistent with the convexity baseline for the `F`-violation at the
smallest binding (`12%` and `15%` agreement).

**T5 - the accidental crossing is not universality.** `F(E_2(0))/M_comp`
crosses `1` at a fine-tuned interaction strength (detected between
`U = 0.2` and `U = 0.4` for both tested masses; at `(m, U) = (1.0, 0.4)`
the signed value is `-0.0089`). This is a single-configuration coincidence:
the T3 witness shows no single normalization can serve two configurations of
equal rest energy simultaneously. It is reported to prevent a fine-tuned
point being mistaken for closure.

## Reduction

Combining T1-T3: exact finite-spacing weak equivalence requires the
gravitational source of an object to track the object's own
inertial-response coefficient -- for composites, the curvature of its
center-of-mass band -- and this quantity is not a functional of the
object's rest-energy/record readout. The remaining exact-WEP identification
therefore targets a dynamical band property. The `EP-S3b` residual
("identifying the gravitational source coefficient with the same `m` as the
inertial rest gap") is sharpened, not closed: the identification must target
the inertial-response functional itself, and no rest-energy carrier can
stand in for it at finite spacing.

Two readings of this reduction are recorded for the owner surface, without
verdict:

- Read as a scaling-window requirement, T4 is the closure shape: universal
  free fall with derived correction exponents, which is the regime where
  equivalence is physically tested. The finite-spacing boundary (T2/T3) is
  then a lattice fact -- it holds in any lattice theory with bound states,
  including textbook contact-interaction models -- not a defect of this
  framework's axioms.
- Read as an exact finite-spacing requirement, the identification of a
  source that reads band curvature is not supplied by the current axiom
  surface (source/action identification is on the axioms' excluded list;
  the Gate-B context-independence no-go closes the generated-geometry
  supplier; the no-go discipline route table in the loop pack records the
  per-route diagnosis). That reading routes to the owner's axiom
  conversation, and this note takes no step in it.

## No-Go Discipline

The negative content of T2/T3 was run through the N1-N8 discipline gate
before this note was shipped; the completed checklist (six enumerated
routes with ATTEMPTED / RULED-OUT-BY-PRIOR markers, wall-independence table,
hidden-wall scan, residual matching, rhetoric audit at the tested
resolutions, partial-closure scan naming T4 as the shipped partial closure,
steelman, and cross-cycle echo) is recorded in the campaign loop pack
(`.claude/science/physics-loops/matter-mass-wep/NO_GO_DISCIPLINE_CHECKLIST.md`)
and reproduced in the review PR body. Gate result: PASS for the narrow
boundary as scoped here.

## Boundaries

- Free two-step surface; 1D composite reduction; distinguishable species;
  equal-mass gated legs (unequal-mass reported by the companion runner).
- The T3 witness lives on the declared I-INT comparator family. A framework
  that later derived its interacting surface could correlate binding with
  record content and would need to be re-examined; T2 is independent of any
  interaction import and survives that steelman unconditionally.
- T4's window bound uses slack factor 5 on the derived leading terms; the
  binding-trend slopes are measured, not derived.
- No gravitational dynamics is derived; EP-S3a is consumed as a bounded
  interface; EP-S3b is sharpened, not closed; no WEP row is closed.
- No axiom, primitive, or Tier-A admission is proposed, adopted, or
  evaluated here; the two readings above are recorded for the owner and
  neither is selected.
- This note sets no audit status. Independent audit is required.

## Dependencies

- [`MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](MASS_OBSERVABLE_REST_GAP_INERTIAL_RESPONSE_UNIVERSAL_FUNCTION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md) -- `F` identity, rest gap, inertial coefficient.
- [`INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md`](INERTIAL_CLOSURE_WIDTH_INDEPENDENT_ACCELERATION_TWO_STEP_SURFACE_BOUNDED_THEOREM_NOTE_2026-07-08.md) -- probe discipline; `M_I` governs acceleration.
- [`COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md`](COMPOSITE_MASS_ADDITIVITY_BINDING_DEFECT_TWO_STEP_SURFACE_BOUNDED_NOTE_2026-07-08.md) -- composite comparator, bandwidth domination, C1.
- [`EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md`](EP_RECORD_STIFFNESS_WEAK_FIELD_SOURCE_READOUT_INTERFACE_NOTE_2026-06-16.md) -- EP-S3a interface; EP-S3b residual sharpened here.
- [`EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md`](EP_RECORD_STIFFNESS_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md) -- R3 residual; two-completion mechanism echoed constructively by T3.
- [`GATE_B_DYNAMICS_NOTE.md`](GATE_B_DYNAMICS_NOTE.md) -- generated-geometry supplier status cited in the reduction's second reading.

## Runner And Cache

Primary runner:
[`scripts/wep_source_reduction_scaling_window_2026_07_08.py`](../scripts/wep_source_reduction_scaling_window_2026_07_08.py)

Runner cache:
[`logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt`](../logs/runner-cache/wep_source_reduction_scaling_window_2026_07_08.txt)

Current local runner result:

```text
TOTAL: PASS=6 FAIL=0
```

Load-bearing residuals from the cached run: T1 uniqueness residual `0`
(sympy-exact); T2 identity and positivity residuals `0` with series
coefficient `2`; T3 witness rest energies equal to `3.5e-13` with relative
inertial-mass difference `0.466`; T4 window exponents `(1/2, 2/3, 2)` exact
with numeric leading-term agreement `0.7%` at `m = 0.1`, and the
size-valid shallow-bound-state universality exhibit `|a/g - 1| = 4.1e-2`
inside the derived bound `1.27e-1` at `kappa_L = 10.2`; T5 crossing detected
between `U = 0.2` and `0.4` for both tested masses. All composite
extractions carry the printed `kappa_L >= 8` size-validity discipline.

## Changelog

- **2026-07-08.** Initial bounded-theorem note. The first runner draft's
  binding-trend and window legs failed on finite-size-corrupted composites
  (shallow bound states larger than the ring) and on a wrongly expected
  monotone `F`-violation; the size-validity diagnostic `kappa_L`, `L = 256`
  and `L = 1024` legs, and the crossing detection replaced them. Local
  runner result `TOTAL: PASS=6 FAIL=0`.
