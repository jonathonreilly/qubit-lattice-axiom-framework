---
claim_id: record_additivity_does_not_supply_ad_invariant_step_measure_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Record scalar additivity on a finite dummy collection is a content-only sum with I(empty)=0. On the 3-element cyclic group C_3, a U(1) sample, two distinct probability measures give two distinct one-step kernels and the same additive I. On the quaternion group Q_8, an SU(2) sample, Haar and a non-Ad-invariant measure likewise give distinct kernels and the same I. I is blind to conjugacy-class structure and does not select ADM-2. The heat-kernel notes are context links only. No axiom is edited."
upstream_dependencies:
  - minimal_axioms
runner: scripts/record_additivity_does_not_supply_ad_invariant_step_measure_2026_08_13.py
---

# Record Additivity Does Not Supply An Ad-Invariant Step Measure

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** finite exact dummy-record readout versus finite-group one-step
kernels. The groups are the 3-element cyclic group `C_3` as a `U(1)` sample
and the quaternion group `Q_8` as an `SU(2)` sample.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/record_additivity_does_not_supply_ad_invariant_step_measure_2026_08_13.py`](../scripts/record_additivity_does_not_supply_ad_invariant_step_measure_2026_08_13.py)

## Result Up Front

The Record axiom supplies a content-determined scalar readout `I` on finite
pairwise-disjoint record collections, with `I(empty)=0`. That scalar is a
sum. It has no conjugacy-class argument and no step-measure argument.

On `C_3`, Haar and a biased triple produce two different one-step kernels.
A dummy three-record collection has the same additive `I` under both. On
`Q_8`, Haar is Ad-invariant and a two-point measure that splits a conjugacy
class is not; the kernels differ and `I` is again the same. So `I` does not
pick Haar versus a non-Ad-invariant measure.

ADM-2, the named extra input that a gauge-step measure is Ad-invariant,
therefore remains an extra input to any later heat-kernel attractor that
asks for it. This note does not claim Wilson/HK uniqueness. No axiom is
edited.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Finite dummy-record additivity and two exact finite-group kernel pairs are proved. ADM-2 is located as an extra input, not derived. Heat-kernel attractor statements stay in the cited context notes."
trace_class: negative_route_pruning
target_claim_id: record_additivity_to_ad_invariant_step_measure
target_blocker_text: "Record additivity does not select an Ad-invariant gauge-step measure"
source_of_blocker_text: handoff
reachability_to_target: locates
artifact_role: theorem
conditional_surface_status: "exact for the displayed dummy records and the C_3 / Q_8 kernels; no continuum group, no Wilson weight, no heat-kernel uniqueness"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

The current Record wording in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
is:

> Only records are readable. A readout value is determined by record content
> alone. For any finite collection of pairwise-disjoint records, scalar
> readout `I` is additive, with `I(empty)=0`.

A dummy record is a pair `(site, content)` with `site` in `Z^3` and
`content` a rational scalar. Sites of a collection are pairwise distinct, so
the records are pairwise disjoint. An unused decoration, such as a group
element, may be written next to a dummy record as a label. It is not record
content and is not readable.

```text
I(empty) = 0
I(R)     = sum_{r in R} content(r)
```

Additivity on disjoint union is ordinary addition of those scalars.

A finite-group step measure is a probability `μ` on a finite group `G`. The
one-step kernel is the left increment

```text
K_μ(g|h) = μ(g h^{-1}).
```

`μ` is Ad-invariant when `μ(x) = μ(s x s^{-1})` for every `s, x` in `G`.
Haar on a finite group is the uniform counting measure. ADM-2 is the extra
input that a gauge-step measure is Ad-invariant.

The dummy collection used below is

```text
r0 at (0,0,0) with content 1
r1 at (1,0,0) with content 2
r2 at (2,0,0) with content 4
R  = {r0, r1, r2}
I(R) = 7
```

Two further dummy records, used only for conjugacy,

```text
r_i  at (0,0,1) with content 5, unused label i
r_-i at (0,0,2) with content 5, unused label -i
```

have equal content, so `I({r_i}) = I({r_-i}) = 5`.

## Theorem 1 — I Is Blind To Conjugacy-Class Structure

Record readout is determined by record content alone. Conjugacy of unused
labels is not content. If two dummy records have the same content scalar,
they have the same readout, whether or not any unused labels are conjugate.

On `Q_8` the elements `i` and `-i` are conjugate: `j i j^{-1} = -i`. The
dummy records `r_i` and `r_-i` carry equal content `5`, so

```text
I({r_i}) = 5 = I({r_-i}).
```

`I` cannot tell those labels apart. Therefore `I` cannot test whether a step
measure is constant on conjugacy classes, and cannot test Ad-invariance.

Writing a class function into the content by hand would be an extra
assignment, not a consequence of additivity. Additivity would still only
sum the assigned scalars.

## Theorem 2 — Two Distinct Measures On C_3 Produce Two Kernels; I Cannot Select

Let `C_3 = {0,1,2}` with addition modulo `3`. This is a 3-element group and
a finite sample of `U(1)`. Define two probability measures

```text
μ_H(0) = μ_H(1) = μ_H(2) = 1/3
μ_B(0) = 1/2,   μ_B(1) = 1/3,   μ_B(2) = 1/6.
```

Both sum to `1`. They are distinct. The kernels are

```text
K_μ(g|h) = μ((g-h) mod 3).
```

`K_H` is the constant kernel `1/3`. The biased kernel has
`K_B(0|0) = 1/2`, so `K_H ≠ K_B`.

The dummy collection `R` does not take a measure argument. Hence

```text
I(R) under μ_H = 7 = I(R) under μ_B.
```

`I` cannot select the kernel.

Because `C_3` is abelian, conjugation is trivial and both measures are
Ad-invariant. That is the honest miss inside this theorem: `I` already
fails to select between two kernels before Ad-invariance is even in play.

## Theorem 3 — ADM-2 Remains An Extra Input To Any Heat-Kernel Attractor

The following notes are context links only. They are not used as a
derivation of ADM-2, and this note does not inherit their attractor
statements:

- [`HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md`](HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md)
- [`EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md`](EMERGENT_GAUGE_HEAT_KERNEL_CLT_ATTRACTOR_CONDITIONAL_ON_BI_INVARIANT_DYNAMICS_NARROW_THEOREM_NOTE_2026-06-08.md)

On their own terms those notes still take an Ad-invariant step measure as
an input when they discuss a heat-kernel attractor. Theorems 1 and 2 show
that Record additivity cannot supply that input: `I` is a scalar sum, blind
to conjugacy, and constant on the dummy collection while the kernels move.

The same dummy `I(R) = 7` also fails to pick Haar versus a non-Ad-invariant
measure on `Q_8`, a finite subgroup of `SU(2)`. Haar is

```text
μ_Haar(g) = 1/8  for every g in Q_8.
```

It is Ad-invariant by uniformity. The two-point measure

```text
μ_N(i) = 1/2,  μ_N(j) = 1/2,  μ_N(g) = 0 otherwise
```

fails Ad-invariance because `j i j^{-1} = -i` and `μ_N(i) = 1/2 ≠ 0 = μ_N(-i)`.
The kernels differ: `K_Haar` is constantly `1/8`, while `K_N(i|1) = 1/2` and
`K_N(-i|1) = 0`. The dummy readout is again `I(R) = 7` for both.

Therefore ADM-2 remains an extra input to any heat-kernel attractor that
asks for an Ad-invariant step measure. No axiom is edited.

## What This Does Not Claim

- It does not claim Wilson/HK uniqueness.
- It does not identify a Wilson weight or a heat-kernel weight.
- It does not derive ADM-2, a continuous Markov generator, a rate, or a
  gauge action.
- It does not replace `U(1)` or `SU(2)` by the finite samples; `C_3` and
  `Q_8` are finite witnesses only.
- It does not edit
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).
  The Record sentence `I(empty)=0` is preserved.

## Verification

```bash
python3 scripts/record_additivity_does_not_supply_ad_invariant_step_measure_2026_08_13.py
```
