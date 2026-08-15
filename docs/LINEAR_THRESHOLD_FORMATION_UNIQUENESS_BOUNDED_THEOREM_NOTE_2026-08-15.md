---
claim_id: linear_threshold_formation_uniqueness_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Given a cube-equivariant linear map to the standard 3, the threshold L≠0 is either empty (α=0) or exactly L1's n≠0 rule (α≠0). Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/linear_threshold_formation_uniqueness_2026_08_15.py
---

# Unique Linear-Threshold Predicate In The Standard 3 Is `f_L1`

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact cube-equivariant linear algebra on the six signed
nearest-neighbor occupancy coordinates, with the threshold predicate
`f(c)=1` iff `L(c)≠0`. The resulting predicate is displayed mathematical
data, not adopted axiom content and not a selected physical formation law.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/linear_threshold_formation_uniqueness_2026_08_15.py`](../scripts/linear_threshold_formation_uniqueness_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Label the six signed nearest-neighbor occupations of a cubic site by

```text
c = (c_{+x}, c_{-x}, c_{+y}, c_{-y}, c_{+z}, c_{-z}) in {0,1}^6.
```

A general linear map `L : R^6 → R^3` has 18 coefficients. Proper cubic
rotations (24 matrices of determinant `+1`) act on the domain by permuting
the six signed directions and act on the target by the standard 3. Cube
equivariance collapses the 18 coefficients to one ray:

```text
L_μ(c) = α (c_{+μ} − c_{-μ}),    α in Q.
```

Write `n_μ(c) := c_{+μ} − c_{-μ}` for the displayed `α=1` representative
`L1`, and write

```text
f_L1(c) := 1_{n(c) ≠ 0}.
```

For every `α ≠ 0` the threshold `f_α(c) := 1_{L(c) ≠ 0}` equals `f_L1`.
The zero map `α=0` yields the empty predicate `f=0`. Those are the only two
threshold predicates arising from cube-equivariant linear maps to the
standard 3. The scale `α` is conventional once it is nonzero; no numerical
normalization is selected.

The claim is uniqueness inside this linear-threshold class. It is not a
classification of all Boolean predicates on the cube, and it is not merely
the statement that `L1` has a kernel.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact row reduction of the 18-coefficient equivariance system, an exact character inner product killing the even sector, and a complete 64-configuration census show that the only nonzero linear-threshold predicate in the standard 3 is f_L1."
trace_class: frontier_discovery
target_claim_id: linear_threshold_formation_uniqueness
target_blocker_text: "whether a cube-equivariant linear map to the standard 3 can present more than one nonzero formation threshold"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the six-direction occupancy cube with the standard-3 target; the predicate is displayed, not adopted"
hypothetical_axiom_status: "none; L, α, and f_L1 are displayed maps and are not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic uniqueness claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Lattice sentence below supplies
  nearest-neighbor adjacency and proper cubic rotations about each site.
  The live Admissibility reading note is quoted only to keep formation
  site, probability, and rate outside the present target. Sentences are
  quoted without rewrite.
- **Explicit theorem-domain condition:** the six signed occupations, the
  24 proper rotations, the standard 3 on the target, and the threshold
  `f=1_{L≠0}` are supplied mathematical data for this theorem.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection of a physical formation predicate by
  Record or Admissibility remains a separate, open obligation. The
  displayed `f_L1` is not adopted.

## Exact Objects

All runner coefficients are exact `Fraction` values. No float is used.

The live Lattice sentence, quoted and not rewritten:

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

The live Admissibility reading note, quoted and not rewritten:

> it does not supply the formation site, probability, or rate.

Write `V_6` for the real span of the six signed directions and `V_3` for the
standard 3. Split

```text
s_μ := c_{+μ} + c_{-μ},    n_μ := c_{+μ} − c_{-μ}.
```

The even subspace is spanned by the three vectors `e_{+μ}+e_{-μ}`. The odd
subspace is spanned by `e_{+μ}−e_{-μ}`. The displayed representative is the
odd map

```text
L1 : V_6 → V_3,    L1(c) = n(c).
```

## Exact Target And Proof Obligations

The exact target is to classify cube-equivariant linear maps `L : V_6 → V_3`
and the associated threshold predicates `f=1_{L≠0}` on `{0,1}^6`.

The obligation graph is:

1. the even pieces `s_μ` carry no copy of the standard 3;
2. the 18-coefficient equivariance system has a one-dimensional solution
   ray `L = α L1`;
3. for `α ≠ 0`, `L(c)=0` if and only if `n(c)=0`, so `f_α = f_L1`;
4. the zero map yields the empty predicate, which is not `f_L1`.

All four obligations are closed below and in the runner by exact integer
arithmetic. The six-direction cube, proper rotations, and the standard-3
target are theorem hypotheses. Nonlinear maps, other targets, and a
physical formation law are outside this theorem.

## Theorem 1 — even pieces are killed by the standard 3

The 24 proper cubic rotations act on the even coordinates `(s_x,s_y,s_z)`
by the unsigned permutation of axes, and on `V_3` by the rotation matrices
themselves. The exact character inner products over the group are

```text
⟨χ_even, χ_std⟩ = 0,    ⟨χ_odd, χ_std⟩ = 1.
```

Thus `Hom_G(even, standard 3) = 0` and `Hom_G(odd, standard 3)` is
one-dimensional. Equivalently, every cube-equivariant linear `L` vanishes
on the three even generators `e_{+μ}+e_{-μ}`.

## Theorem 2 — nonzero scale is conventional and recovers `f_L1`

A general real `3 × 6` matrix has 18 coefficients. Cube equivariance is
the linear system

```text
L ∘ ρ(R) = R ∘ L
```

at all 24 proper rotations `R`. Exact row reduction has rank 17 and
nullspace `span{L1}`. Therefore every cube-equivariant `L` is `L = α L1`
for a unique scalar `α`.

For every `α ≠ 0` and every `c in {0,1}^6`,

```text
L(c) = 0  iff  n(c) = 0  iff  c_{+μ} = c_{-μ} on all three axes.
```

Hence `f_α = f_L1`, independently of the conventional nonzero scale. On
the 64 configurations there are exactly eight zeros of `L1` and
fifty-six units of `f_L1`.

## Theorem 3 — the zero map is the only other threshold

The remaining ray point `α=0` is the zero map. Its threshold is the empty
predicate `f=0` (never form). Direct comparison on `{0,1}^6` gives
`f=0 ≠ f_L1`. Therefore the unique nonzero-linear-threshold predicate in
the standard 3 is `f_L1`.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. the even sum map `S_μ(c)=c_{+μ}+c_{-μ}` is not cube-equivariant to the
   standard 3;
2. the zero map is cube-equivariant but its threshold is not `f_L1`;
3. reversing a single pair of `L1` signs leaves the equivariance system.

## What This Does Not Claim

- `f_L1` is displayed, not adopted as axiom content or as a physical
  formation law.
- Admissibility is not claimed to supply a formation site, probability, or
  rate.
- The result is not a census of all Boolean predicates on `{0,1}^6`.
- The result is not merely the kernel computation for `L1`.
- No numerical scale for `α` is selected.
- Other targets, nonlinear maps, and multi-site lifts are outside the
  theorem.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
> adjacency, standard translations, and proper cubic rotations about each site.

> Records form.

> When present, a record locks exactly one admissible local possibility.

Their dependency role is limited to the cubic nearest-neighbor rotation
vocabulary and the existence of formation as an axiom name. This theorem
separately supplies the linear maps and the threshold comparison;
physical adoption of `f_L1` remains outside its target.

## Runner Contract

The companion runner checks Theorems 1–3 with exact rational arithmetic.
In particular, it row-reduces the complete 18-coefficient equivariance
system, evaluates the even and odd character inner products as integers,
and compares `f_α` to `f_L1` on all 64 configurations rather than sampling
a coefficient grid. It also checks the three mutations, quotes the live
axiom sentences, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
