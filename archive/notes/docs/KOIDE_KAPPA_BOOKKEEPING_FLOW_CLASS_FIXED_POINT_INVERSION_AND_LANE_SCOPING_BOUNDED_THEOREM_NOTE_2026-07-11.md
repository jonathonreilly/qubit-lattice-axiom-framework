# The Kappa Bookkeeping Flow Class and Conditional Fixed-Point Inversion

**Date:** 2026-07-11
**Review repair:** 2026-07-12
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets no
audit outcome and changes no premise registry or audit-owned surface.
**Primary runner:**
[`scripts/frontier_koide_kappa_flow_class_2026_07_11.py`](../scripts/frontier_koide_kappa_flow_class_2026_07_11.py)
**Runner cache:**
[`logs/runner-cache/frontier_koide_kappa_flow_class_2026_07_11.txt`](../logs/runner-cache/frontier_koide_kappa_flow_class_2026_07_11.txt)

The filename is retained for downstream citation stability. The repaired note
keeps the T1 flow-class theorem. The submitted T2 identification of the
coefficient fork with a physical partition binary and the submitted T3
quark-lane scoping corollary are withdrawn; their replacement statement names
are recorded below for downstream citation review.

> **Bounded claim.** Given a positive bookkeeping coefficient `kappa` and the
> supplied independent agreement filter on a two-cell bookkeeping, the induced
> coordinate map is `f_kappa(r)=kappa r^2`. Its finite positive fixed point is
> `1/kappa`, its projective endpoint is fixed, and all members are linearly
> conjugate to the square map with local multiplier two at the positive fixed
> point. Evaluating `kappa=1` or `kappa=2` gives two exact algebraic examples;
> no current-source theorem identifies those coefficient choices with the
> distinct equipartition-granularity count or selects either physically. The
> identity `kappa=1/r` is conditional on `r` already being the positive fixed
> point. Quark and charged-lepton numbers below are report-only comparators and
> support no PASS condition, threshold, exclusion, or lane-scoping inference.

## Supplied surface

The conditional map uses the agreement filter from the
[`agreement-conditioned double-registration anatomy note`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md):

```text
p_i' = p_i^2/(p_s^2+p_d^2).
```

That source and its independence interpretation are currently unaudited. This
note rederives the algebra but does not derive independent outcomes,
agreement-conditioning, a probability law, or any physical value of `kappa`.

For `a^2>0`, `|b|^2>=0`, and `kappa>0`, define the supplied bookkeeping

```text
(p_s,p_d) = (a^2,kappa|b|^2)/(a^2+kappa|b|^2),
r = |b|^2/a^2.
```

The coefficient is a bookkeeping condition. It is not an approved primitive,
derived multiplicity, fitted parameter, or observed quantity in this note.

## T1 — the kappa flow class

**Statement.** On the supplied surface, independent agreement-conditioning
induces

```text
f_kappa(r)=kappa r^2.
```

On the projectively completed nonnegative line its fixed set is
`{0,1/kappa,infinity}`. The positive finite fixed point is unique, every member
is linearly conjugate to `x -> x^2`, and the derivative at the positive fixed
point is two for every `kappa`.

**Proof.** The odds coordinate is

```text
x = p_d/p_s = kappa r.
```

The common agreement normalizer cancels from the ratio, so

```text
x' = p_d'/p_s' = (p_d/p_s)^2 = x^2.
```

Converting back gives

```text
r' = x'/kappa = kappa r^2.
```

Solving `kappa r^2=r` gives `r=0` and `r=1/kappa`. In the reciprocal chart
`s=1/r`, the map is `s'=s^2/kappa`, so `s=0`, corresponding to
`r=infinity`, is fixed. Finally,

```text
f_kappa'(1/kappa)=2,
h(r)=kappa r,
(h o f_kappa o h^-1)(x)=x^2.
```

Thus the positive-fixed-point multiplier is coefficient-independent. ∎

This is local map algebra. In particular, after the repaired permanence note
`RECORD_PERMANENCE_FORCES_FRESH_SITE_DOUBLE_REGISTRATION_AND_AGREEMENT_SURVIVAL_BOUNDED_THEOREM_NOTE_2026-07-11.md`
withdrew finite-time exactness, a multiplier of two cannot be cited as proof
that finite-precision persistence forces exact siting. The exact finite-window
bounds depend on the coordinate scale and observation band.

## T2 — the kappa-one and kappa-two coefficient evaluations

The submitted name “the fork is the partition binary” is withdrawn. The exact
replacement is only the following pair of evaluations:

```text
kappa=1: f_1(r)=r^2,  positive fixed point r*=1;
kappa=2: f_2(r)=2r^2, positive fixed point r*=1/2.
```

The `kappa=2` member reproduces the coefficient used on the supplied
singlet/doublet anatomy surface. The `kappa=1` member reproduces the algebraic
counterexample map `psi(r)=r^2` discussed in the context-only
`KOIDE_OO_RD_PREMISE_RELATION_ON_CURRENT_SURFACE_NARROW_THEOREM_NOTE_2026-06-12.md`.
Both statements follow by substitution and neither selects a physical
bookkeeping.

The coefficient `kappa` must not be conflated with the aggregate doublet
counting unit `n_d` in the repaired
[`orbit-occupancy equipartition-granularity note`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md).
They enter different equations:

```text
flow fixed point:                 r = 1/kappa,
aggregate equipartition condition: r = n_d/2.
```

The equality of a numerical endpoint under selected values does not identify
the two parameters or attach “count once,” “count twice,” “sector,” or “orbit”
labels to `kappa`. A physical theorem relating the bookkeeping coefficient to
an outcome or energy count remains open.

The linear conjugacy in T1 also shows that the dynamics does not select
`kappa`: changing the supplied coefficient rescales the coordinate while
leaving the square-map form unchanged. A correlated second registration would
instead give the identity map `r'=r`, so the whole class remains conditional
on the independent agreement-filter mechanism.

## T3 — conditional fixed-point inversion; comparators report-only

The submitted name “fixed-point inversion and lane scoping” is narrowed. The
theorem-grade part is only the conditional inversion:

> If `r>0` is already known to be the positive fixed point of
> `f_kappa(r)=kappa r^2`, then `kappa=1/r`.

This is the algebraic rearrangement of `r=1/kappa`. It does not show that an
observed or registered value is governed by this flow, does not derive a
lane's `kappa`, and does not license an empirical exclusion.

### Report-only comparator table

The following decimal values are quoted from the support-only
[`sector-blind max-record-entropy note`](FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md):

```text
charged-lepton comparator: r=1/2,
down-quark comparator:      r=0.597,
up-quark comparator:        r=0.773.
```

That source is unaudited. These values are not used to establish that any lane
is persistent, that the map applies, or that `kappa` is physical. Applying the
conditional inversion merely prints the arithmetic comparators

```text
kappa_lepton_report = 2,
kappa_down_report   = 1000/597 = 1.675042...,
kappa_up_report     = 1000/773 = 1.293661....
```

For transparency, the table below compares those printed numbers with one
finite display grid

```text
{1,5/4,4/3,3/2,5/3,2}.
```

`Delta_r=0.001` is the quoted decimal display unit, not a measurement
uncertainty or statistical sigma. `Delta_kappa=Delta_r/r^2` is a linearized
display scale. “Display units” have no confidence-level meaning.

Down-quark report (`r=0.597`, `kappa_report=1.675042...`,
`Delta_kappa=0.002806...`):

| grid value `t` | `1/t` | `|kappa_report-t|` | linearized kappa display units | r display units |
|---:|---:|---:|---:|---:|
| 1 | 1.0000 | 0.675042 | 240.591 | 403.000 |
| 5/4 | 0.8000 | 0.425042 | 151.489 | 203.000 |
| 4/3 | 0.7500 | 0.341709 | 121.788 | 153.000 |
| 3/2 | 0.6667 | 0.175042 | 62.386 | 69.667 |
| 5/3 | 0.6000 | 0.008375 | 2.985 | 3.000 |
| 2 | 0.5000 | 0.324958 | 115.818 | 97.000 |

Up-quark report (`r=0.773`, `kappa_report=1.293661...`,
`Delta_kappa=0.001674...`):

| grid value `t` | `1/t` | `|kappa_report-t|` | linearized kappa display units | r display units |
|---:|---:|---:|---:|---:|
| 1 | 1.0000 | 0.293661 | 175.471 | 227.000 |
| 5/4 | 0.8000 | 0.043661 | 26.089 | 27.000 |
| 4/3 | 0.7500 | 0.039672 | 23.705 | 23.000 |
| 3/2 | 0.6667 | 0.206339 | 123.293 | 106.333 |
| 5/3 | 0.6000 | 0.373006 | 222.882 | 173.000 |
| 2 | 0.5000 | 0.706339 | 422.058 | 273.000 |

The grid is illustrative and not exhaustive. No nearest-grid selection,
acceptance band, sigma threshold, kill condition, incompatibility verdict, or
lane-scoping corollary is drawn. The paired runner prints this section only
after every PASS/FAIL check is complete; comparator values never enter a check
or exit-code path.

## Import and support inventory

- **Supplied bounded dependency:** the independent agreement filter and
  `kappa=2` bookkeeping surface from the linked anatomy note; currently
  unaudited.
- **Exact conditional algebra:** odds-map squaring, `f_kappa`, fixed sets,
  conjugacy, multiplier, two coefficient evaluations, and fixed-point
  inversion.
- **Distinct support context:** the repaired equipartition counting unit
  `n_d`; it is cited to prevent parameter conflation, not to select `kappa`.
- **Observational/support-only comparators:** three quoted `r` values and the
  finite display grid. They are printed only and support no scientific
  conclusion or PASS/FAIL result.
- **Not consumed:** a derived probability rule, physical bookkeeping bridge,
  quark uncertainty model, empirical threshold, fitted selector, or universal
  durability law.

## No-Go Discipline Gate

The negative claim is limited to current-source nonselection: the displayed
conditional algebra does not itself identify or choose a physical `kappa`, and
the report-only table licenses no empirical conclusion.

### N1 — Alternative-route enumeration

1. **Agreement-conditioned anatomy — ATTEMPTED.** It supplies the map form and
   one coefficient choice but leaves independence and physical bookkeeping as
   conditions.
2. **Linear conjugacy — ATTEMPTED.** All positive `kappa` members reduce to the
   same square map; conjugacy therefore does not select the coordinate scale.
3. **Special values `kappa=1,2` — ATTEMPTED.** Substitution gives exact example
   maps but no physical label or selection theorem.
4. **Equipartition granularity — ATTEMPTED.** Its separate parameter `n_d`
   enters `r=n_d/2`; no source theorem equates it with `kappa`.
5. **Correlated registration — ATTEMPTED.** Perfect correlation gives the
   identity map rather than `f_kappa`, showing that independence is
   load-bearing.
6. **Record-production/readout dynamics — OPEN.** A concrete retained theory
   could derive a bookkeeping coefficient or a different map.
7. **Comparator inversion — ATTEMPTED AS REPORT ONLY.** Numerical inversion
   prints arithmetic but cannot establish that the fixed-point premise holds.
8. **Other flow families — OPEN.** The square-map conjugacy class is not shown
   exhaustive.

### N2 — Wall-independence audit

Outcome independence, the physical definition of `kappa`, identification of a
lane with the positive fixed point, and flow-family exhaustiveness are separate
conditions. Closing one does not automatically close the others. The finite
comparator grid is not counted as a wall because it supplies no verdict.

### N3 — Hidden-wall scan

The probability/filter mechanism and coefficient are labeled supplied. The
equipartition count is kept distinct. The comparator source is unaudited;
decimal display units are not statistical errors; no comparator enters the
runner's checks. No physical lane assignment, threshold, or universality
premise is hidden in the conclusion.

### N4 — Residual matching

| source | source role | residual used here | match |
|---|---|---|---|
| [`RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md`](RD_BRIDGE_ANATOMY_AGREEMENT_CONDITIONED_DOUBLE_REGISTRATION_BOUNDED_NOTE_2026-06-12.md) | conditional agreement filter and coefficient-two surface | whether independence and bookkeeping are physically derived | yes |
| [`KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md`](KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md) | distinct aggregate equipartition parameter | whether its counting unit is the same object as `kappa` | yes |
| [`FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md`](FLAVOR_MAX_RECORD_ENTROPY_IS_SECTOR_BLIND_CANNOT_DERIVE_THE_KOIDE_DIAL_NARROW_NO_GO_NOTE_2026-06-15.md) | source of report-only decimal comparators | no scientific residual is discharged from those values | yes |
| [paired runner](../scripts/frontier_koide_kappa_flow_class_2026_07_11.py) | exact conditional algebra plus post-check report output | whether the formulas and report-path separation hold | yes |

### N5 — Rhetoric audit

The theorem is a coordinate/bookkeeping statement on one supplied two-cell
surface. It is not a per-record, full-lattice, physical-sector, or universal
durability theorem. “Fixed point” never means “observed lane value” without the
explicit conditional premise.

### N6 — Partial-closure path scan

The missing bookkeeping and outcome conditions change the physical map, so
they are not labeling conventions. A retained record-production theorem,
action/measure construction, or physical readout bridge could derive `kappa`
or reject this flow family. Premise approval is a separate governance path;
this note neither requests nor infers it.

### N7 — Steelman

A microscopic colored-sector action could produce a continuous effective
coefficient matching one printed comparator, or could yield a non-square flow.
Conversely, a retained record theorem could derive an integer coefficient.
Because none of these routes is tested, the comparator table cannot close or
resurrect a universal law.

### N8 — Cross-cycle echo

The repaired orbit-occupancy note separates aggregate equipartition granularity
from partition/kernel arithmetic, and the repaired permanence note separates a
local multiplier from finite-time exactness. This note preserves both
distinctions: `kappa` is not silently relabeled as the equipartition count, and
multiplier two is not promoted to a physical persistence selection.

**No-Go Discipline result:** `PASS` for the narrow current-source
nonselection boundary. It would be `FAIL` for a claim that no future dynamics
can derive a lane-dependent coefficient or that the report grid excludes a
lane; this note makes neither claim.

## What this note does not claim

- no derivation, adoption, or empirical fit of `kappa` for any lane;
- no identification of `kappa` with the equipartition counting unit `n_d`;
- no physical “count once/count twice,” sector/orbit, or partition-binary
  interpretation of the `kappa=1,2` evaluations;
- no derivation or preference for `r=1/2`;
- no empirical uncertainty, threshold, exclusion, kill condition, or
  lane-scoping conclusion from the comparator table;
- no exhaustiveness of the square-map flow family, universal durability law,
  new axiom, approved primitive, audit verdict, or effective-status change.

## Citation-stability note

The note filename and T1 theorem name are unchanged. Downstream citations to
T2 as “the fork is the partition binary” or T3 as “fixed-point inversion and
lane scoping” must be rewritten to the repaired statement names:

```text
T2: the kappa-one and kappa-two coefficient evaluations;
T3: conditional fixed-point inversion; comparators report-only.
```

The context-only permanence note and premise-relation note remain named in
plain text to avoid adding non-load-bearing citation-graph edges.

## Verification

```bash
python3 scripts/frontier_koide_kappa_flow_class_2026_07_11.py
```

Exit code is zero iff `FAIL=0`. Independent audit is required before any
status promotion.
