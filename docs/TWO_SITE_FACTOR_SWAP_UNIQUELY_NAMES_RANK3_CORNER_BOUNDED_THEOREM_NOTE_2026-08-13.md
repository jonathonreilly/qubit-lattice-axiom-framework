---
claim_id: two_site_factor_swap_uniquely_names_rank3_corner_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the supplied mathematical host H=C^2⊗C^2, the factor-swap F is the unique linear map sending |i⟩⊗|j⟩ to |j⟩⊗|i⟩. It is a Hermitian involution with Tr(F)=2. The complex-Hermitian involutions implementing that factor swap on E_00 and E_01 are exactly ±F. The unique rank-3 spectral projection of F is p_+=(I+F)/2. No physical identification of that projection is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py
---

# The Two-Site Factor-Swap Has a Unique Rank-3 Spectral Projection

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact matrix identities and a universal complex-Hermitian
intertwiner classification on the supplied host `H = C^2 ⊗ C^2`.
No physical two-site composition rule or physical interpretation of the
rank-3 projection is asserted. `F` is displayed operator data, not axiom
content.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py`](../scripts/two_site_factor_swap_uniquely_names_rank3_corner_2026_08_13.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Write `H = C^2 ⊗ C^2` with product basis `|00>, |01>, |10>, |11>`.
The factor-swap is the unique linear map `F : H → H` with
`F(|i⟩ ⊗ |j⟩) = |j⟩ ⊗ |i⟩` on that basis. In the product basis

```text
F = ((1,0,0,0), (0,0,1,0), (0,1,0,0), (0,0,0,1)).
```

`F` is Hermitian, `F^2 = I_4`, and `Tr(F) = 2`. Conjugation exchanges
the displayed tensor factors:
`Ad_F(X ⊗ I_2) = I_2 ⊗ X` and `Ad_F(I_2 ⊗ X) = X ⊗ I_2`.

Every complex-Hermitian involution satisfying the factor-swap
intertwining equations for `{E_00, E_01}` is exactly `F` or `−F`.
The unique rank-3 spectral projection of `F` is
`p_+ = (I_4 + F)/2`. The complementary `p_- = (I_4 − F)/2` has rank 1,
and the corner unit is `p_+`, not `I_4`.

The word "unique" in this note refers only to these algebraic uniqueness
statements. It introduces no symbol-to-physics naming convention.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact matrix identities classify the complex-Hermitian factor-swap involutions and determine F's rank-3 spectral projection on one supplied two-site host."
trace_class: frontier_discovery
target_claim_id: two_site_factor_swap_uniquely_names_rank3_corner
target_blocker_text: "whether the displayed two-site factor swap has a uniquely determined rank-3 spectral projector"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact on the supplied mathematical host H=C^2⊗C^2; no physical two-site composition rule or physical interpretation is asserted"
hypothetical_axiom_status: "none; F is displayed operator data and is not proposed as axiom content"
admitted_observation_status: null
next_trace_action: "independent audit of the bounded algebraic claim"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Qubit sentence below supplies the
  repository's one-site `M_2(C)` terminology. It is quoted without rewrite.
- **Explicit theorem-domain condition:** `H = C^2 ⊗ C^2`, its product
  basis, and the standard tensor-factor embeddings are supplied mathematical
  data for this theorem. This note does not claim that the axioms derive a
  physical two-site composition rule.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** selection by Record or Admissibility and any
  physical interpretation of the rank-3 corner remain separate, open
  obligations outside the target proved here.

## Exact Objects

All runner coefficients are exact `Fraction` values. No float is used.

The live Qubit sentence, quoted and not rewritten:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

Write `T_2 = B(H) ≅ M_2(C) ⊗ M_2(C) ≅ M_4(C)` for the supplied
mathematical host. Matrix units are `E_ij = |i⟩⟨j|`. Kronecker products
are the standard product-basis embeddings. `Ad_F(Z) := F Z F` because
`F^{-1} = F^* = F`.

`p_+ = (I_4 + F)/2` and `p_- = (I_4 − F)/2` are the spectral
projections of the Hermitian involution `F`.

## Exact Target And Proof Obligations

The exact target is to classify the complex-Hermitian involutions satisfying
the two displayed generator intertwining equations and to identify the
rank-3 spectral projection of the resulting factor-swap.

The obligation graph is:

1. the four product-basis images determine `F`;
2. direct exact arithmetic proves the involution, trace, and factor-exchange
   identities;
3. exact row reduction on all 16 real coordinates of a general
   complex-Hermitian `4 × 4` matrix proves that the intertwiner kernel is
   `span_R{F}`;
4. involutivity on `U = tF` gives `t^2 = 1`, hence `U = ±F`;
5. exact projector arithmetic gives ranks 3 and 1.

All five obligations are closed below and in the runner. The fixed dimension,
the supplied tensor host, and Hermiticity are theorem hypotheses. Non-Hermitian
implementers, other hosts, and multi-site lifts are outside this theorem.
There is no missing lemma for the bounded algebraic target; a physical
interpretation would be a separate claim with separate support.

## Theorem 1 — `F` is a Hermitian involution of trace 2

Direct matrix arithmetic gives `F^* = F`, `F^2 = I_4`, and `Tr(F) = 2`.

## Theorem 2 — `Ad_F` exchanges tensor factors

For each matrix unit `X ∈ {E_00, E_01, E_10, E_11}`,

```text
F (X ⊗ I_2) F = I_2 ⊗ X,    F (I_2 ⊗ X) F = X ⊗ I_2.
```

The identities extend by complex linearity to all of `M_2(C)`.

## Theorem 3 — uniqueness of the linear swap

If `G : H → H` is linear and `G(|i⟩ ⊗ |j⟩) = |j⟩ ⊗ |i⟩` on the four
basis vectors, then `G = F`: the four images fix every matrix column.

## Theorem 4 — complex-Hermitian involutions implementing the swap

Let `U` be an arbitrary complex-Hermitian `4 × 4` matrix with `U^2 = I_4`
and

```text
U (E_00 ⊗ I_2) = (I_2 ⊗ E_00) U,
U (E_01 ⊗ I_2) = (I_2 ⊗ E_01) U.
```

A general complex-Hermitian `4 × 4` matrix has 16 real coordinates:
four real diagonal coordinates and real and imaginary coordinates for each
of the six entries above the diagonal. Separating real and imaginary parts
of the two intertwining equations gives a rational linear system in those
16 coordinates. Exact row reduction has rank 15 and nullspace
`span_R{F}`. Because a rational row reduction is valid over the reals, this
classifies every complex-Hermitian solution, not merely rational matrices or
a finite coefficient grid.

Thus `U = tF` for a real scalar `t`. The equation `U^2 = I_4` becomes
`t^2 = 1`, so `t = ±1` and `U = ±F`. Both signs implement the same
conjugation, and `F ≠ −F` because their traces differ.

## Theorem 5 — unique rank-3 spectral projection

`p_+ = (I_4 + F)/2` is an orthogonal projection of rank 3.
`p_- = (I_4 − F)/2` is an orthogonal projection of rank 1.
Therefore the unique rank-3 spectral projection of `F` is `p_+`.
It is not `I_4`. The corner `p_+ T_2 p_+` is unital with unit `p_+`.

## Physical-Interpretation Boundary

The proved output is the displayed algebraic projector. This note neither
assigns it a physical label nor changes the one-site Qubit statement.
`F` is displayed two-site operator data, not axiom content, and no additional
axiom is proposed.

## Mutation Checks

Three non-equivalences guard the load-bearing conclusions:

1. `F` and `−F` are distinct because their traces are 2 and `−2`;
2. `rank(p_+)` is 3 rather than 1;
3. `p_+` differs from `I_4`.

## What This Does Not Claim

- The supplied tensor host is not claimed to be a physically derived
  composition rule.
- The rank-3 projector is not assigned a gauge, particle, or other physical
  interpretation.
- No claim is made that Record locks `p_+` or that Admissibility selects `F`.
- Involutions that do not implement the displayed factor swap are not
  classified.
- The corner inclusion is not a unital inclusion of an `M_3` factor into
  `T_2`.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> A site with no record cannot be read.

Their dependency role is limited to the repository's local-algebra vocabulary
and lock rule. This theorem separately supplies the two-site host and swap;
physical interpretation of the projector remains outside its target.

## Runner Contract

The companion runner checks Theorems 1–5 with exact rational arithmetic. In
particular, it row-reduces the complete 16-real-coordinate complex-Hermitian
intertwining system rather than sampling a coefficient grid. It also checks
the three mutations, quotes the live axiom sentences, prints substantive N5
scope certificates, and records the import boundary. Declared review inputs
are this note and the axiom memo only.
