# Conditional Equivariant Tick-Realization Lemma on a Binary Ring

**Date:** 2026-07-10
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Claim scope:** On an even one-axis ring with `L >= 4`, binary condition and
possibility sets, and one stipulated complex component per site, suppose a
unitary nearest-neighbor tick obeys the named conditional realization predicate
`REAL(U; A, F)`. The one-dimensional translation-covariance clause then gives
full one-site tick covariance modulo local `U(1)` frames. Nonvacuous rule
variation gives off-site tick support only because the separate
conditioning-faithfulness condition assumes that support on every varying
edge. The fixed-assignment implication is an exact conditional lemma; the
conditioning-faithfulness implication is an unpacking of a named premise. This
note does not derive a physical tick--Admissibility realization bridge, the
existence or choice of a realized tick, a kinetic branch or winding, proper
cubic covariance, probabilities, weights, Hamiltonians, or dynamics.
**Status:** bounded conditional algebraic lemma proposed for independent audit;
effective status remains pipeline-derived.
**Primary runner:**
[`scripts/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.py`](../scripts/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.py)
**Runner cache:**
[`logs/runner-cache/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.txt`](../logs/runner-cache/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.txt)

## Why This Note Exists

The selector note says that a supplied tick--Admissibility realization bridge
is the additional premise that identifies the rule clauses with tick
predicates. It therefore treats the bridge as supplied rather than proved.

As of 2026-07-10, the audit-ledger row
`tick_cell_selection_by_translation_and_variation_clauses_narrow_theorem_note_2026-07-09`
carries in its re-audit notes a request for a theorem mapping the two
Admissibility clauses to full tick covariance modulo local `U(1)` frames and
off-site tick support. This note does **not** discharge that request: it isolates
a sufficient fixed-assignment condition for the covariance leg and shows that
the support leg remains assumed by conditioning faithfulness. It does not
inspect or gate on any audit-status field.

## Setting And Objects

Let the site set be the even ring `Z_L`, with `L >= 4`, and let there be one
stipulated complex component at every site. These are explicit surface
restrictions, not consequences of the framework axioms. A tick is a unitary
matrix `U` on `C^L` with stipulated nearest-neighbor support:

```text
U[x,y] = 0 unless dist(x,y) <= 1 on the ring.
```

Let `T e_x = e_{x+1}`, with indices modulo `L`. A local `U(1)` frame is a
diagonal unitary `g = diag(exp(i theta_x))`, acting by
`U -> g U g^dag`.

Define the first tick predicate by:

```text
M(U) = max_xy ||T U T^dag|[x,y] - |U|[x,y]| = 0.
```

In ring-index notation, its quantity is

```text
M(U) = max_{x,y} | |(T U T^dag)[x,y]| - |U[x,y]| |.
```

Thus the predicate is the equality `M(U) = 0`. Define the second tick predicate
by:

```text
O(U) = true  iff  U[x,y] != 0 for at least one x != y.
```

In ring notation this says exactly that at least one strictly off-diagonal
matrix entry of the tick is nonzero.

## One-Dimensional Clause Analogues

The first Admissibility sentence is:

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

The second is:

> For each site, the available possibilities are determined by, and vary with, the nearest-neighbor conditions.

The statements above belong to the full `Z^3` framework. The lemma below uses
only their one-dimensional translation restriction; it does not derive the
binary ring model or proper-cubic covariance from them.

On the present one-axis surface, take the finite condition set
`C_cond = {0,1}`. An availability rule `A` assigns to each site `x` and every
nearest-neighbor condition profile
`c : {x-1, x+1} -> C_cond` a nonempty subset `A_x(c)` of the one-site
possibility set `{0,1}`.

The translation clause is formalized along the stipulated axis by

```text
A_{x+1}(shifted profile) = A_x(profile)
```

for every `x` and every profile. It is one fixed rule, copied to every site.
Clause 2 is formalized by requiring the variation set

```text
V(A) = { (x,y) : y is a nearest neighbor of x and there exist profiles c,c'
         equal off y with A_x(c) != A_x(c') }
```

to be nonempty. For displacement `d = y-x` in `{-1,0,+1}`, the rule data at
`(x,y)` are `(d, v_x(d))`, where `v_x(d) = 1` exactly when
`(x,x+d) in V(A)`, and `v_x(d) = 0` otherwise.

## The Named Realization Predicate

`REAL(U; A, F)` means that the tick `U` realizes the availability rule `A` via
the assignment `F`, with both of the following parts.

**Fixed-assignment condition.** There is one site-independent map `F` from
rule data `(d,v)` to complex amplitudes, and a local `U(1)` frame `g`, such that

```text
U = g U0 g^dag,
U0[x,x+d] = F(d,v_x(d)).
```

Physical reading: the same assignment converts the same local rule data into
the same tick amplitude at every site, with only the allowed local frame left
free.

**Conditioning-faithfulness condition.** For every `(x,y) in V(A)` with
`x != y`, `U[x,y] != 0`.

Physical reading: a nearest-neighbor dependence in the availability rule is
carried by a matrix element of the tick claimed to realize that rule.

## Fixed-Assignment Covariance Lemma

**Covariance implication.** Suppose `A` satisfies the one-dimensional
translation clause and the fixed-assignment condition holds. If changing the
condition at `y` changes
`A_x`, translating the two witnessing profiles by one site changes the
condition at `y+1` and, by clause 1, changes `A_{x+1}`. Translating backward
gives the converse. Therefore

```text
(x,y) in V(A)  iff  (x+1,y+1) in V(A).
```

It follows that `v_x(d)` is independent of `x`; write it as `v(d)`. Hence
`U0[x,x+d] = F(d,v(d))` depends only on the displacement. Since
`(T U0 T^dag)[x,y] = U0[x-1,y-1]`, translation preserves that displacement
and `T U0 T^dag = U0` exactly. Because `U = g U0 g^dag`, `U` is
frame-equivalent to an exactly one-site-covariant tick. This is full tick
covariance modulo local U(1) frames.

**Modulus shadow.** Diagonal unitary conjugation preserves every
entrywise modulus. From the exactly covariant representative,

```text
|U[x,y]| = |U0[x,y]| = |U0[x-1,y-1]| = |U[x-1,y-1]|.
```

The literal definition of `M` therefore gives `M(U) = 0`. The selector's
modulus predicate is a derived shadow of the full frame statement.

**Strictness.** Let

```text
U_alt = diag((-1)^x).
```

Its entrywise moduli are translation invariant, so `M(U_alt) = 0`. Every local
frame `g` is diagonal and therefore commutes with `U_alt`; consequently
`g U_alt g^dag = U_alt` for every such frame. On an even ring,
`T U_alt T^dag = -U_alt != U_alt`. No local frame can render `U_alt`
one-site covariant. Thus full covariance modulo frames is strictly stronger
than `M(U) = 0`.

**Fixed-assignment sharpness.** Drop the site-independent assignment while
keeping a covariant rule. Partition the `L=6` ring into the neighboring pairs
`(0,1)`, `(2,3)`, `(4,5)` and define

```text
U_giv = R(0.3) direct-sum R(0.9) direct-sum R(0.3),
R(theta) = [[cos(theta), -sin(theta)], [sin(theta), cos(theta)]].
```

This is an actual unitary, nearest-neighbor-supported complex matrix. The
covariant rule data are the same at translated sites, but site-dependent maps
`F_x` may assign the different displayed rotation amplitudes to those same
data. Direct translation changes both occupied bonds and, between the first
two pairs, their nonzero moduli; the literal matrix computation gives
`M(U_giv) > 0`. Thus the covariance clause alone does not imply `M(U)=0`.
The fixed-assignment condition is load-bearing.

**Mover gauge uniformization.** Let a unitary pure mover have

```text
(U psi)(x) = t_x psi(x-1),    |t_x| = 1.
```

Choose any fixed `L`th root `t_bar` satisfying
`t_bar^L = product_x t_x`. With a seam at site zero, set `g_0 = 1` and use the
explicit cumulative-product construction

```text
g_x = t_bar^x / (t_1 t_2 ... t_x).
```

For `1 <= x <= L-1`, direct substitution gives
`g_x t_x conjugate(g_{x-1}) = t_bar`. The seam entry gives the same result
because `t_bar^L = product_x t_x`. Equivalently, extending the recurrence once
around the ring gives `g_L = 1`, so the gauge closes exactly. Thus
`g U g^dag` is the uniform mover with amplitude `t_bar`. For the opposite
direction, the recurrence `g_{x+1} = g_x t_x/t_bar` gives the same conclusion.
This is the explicit realization-frame construction behind the cyclic gauge
condition.

## Conditioning-Faithfulness Consequence

**Variation-to-support implication.** Suppose the one-dimensional variation
clause holds, so some `(x,y) in V(A)` has `x != y`, and suppose the
conditioning-faithfulness condition holds. That condition gives `U[x,y] != 0`
at the pair. By the literal definition, `O(U) = true`. This is bookkeeping,
not a derivation of conditioning faithfulness from Admissibility.

**Conditioning-faithfulness sharpness.** Drop the condition. The identity tick
`U=I` can coexist with any
varying availability rule: the rule varies with a neighbor condition while
the tick carries none of that variation. Since every off-diagonal entry of
`I` vanishes, `O(I) = false`. The variation clause alone does not imply
off-site support. Conditioning faithfulness is load-bearing.

**Converse failure.** Let `A` be constant, with
`A_x(c) = {0,1}` for every `x,c`. Then `V(A)` is empty. A uniform mover is
nevertheless obtained from the site-independent assignment
`F(-1,0)=1`, with the other amplitudes zero, and it has `O(U)=true`.
Therefore off-site support does not detect rule variation. The conditional
predicate is one-directional: the clause analogues imply tick predicates under
`REAL`; the tick predicates do not imply the clause analogues.

## Boundary And Honest Auditor Read

- The realization predicate `REAL(U; A, F)` is named, not derived. Whether any
  tick realizes the availability rule, including the existence and choice of
  a realized kinetic branch, remains downstream content. The axiom boundary
  says Admissibility "does not choose a Hamiltonian or transfer operator", and
  a realized kinetic branch "is downstream content: it needs derivation,
  bridge, explicit admission". This note supplies only a conditional
  sufficient-condition lemma; it does not supply that physical bridge or
  existence.
- This is a one-axis surface. The covariance mapped here is translation
  covariance along the stipulated axis on an even ring with `L >= 4`. Proper
  cubic rotations and the full `Z^3` condition profile are outside this surface.
- The binary condition set, binary possibility set, one-component carrier,
  unitary nearest-neighbor tick, and diagonal local `U(1)` frame group are
  explicit surface assumptions.
- No probabilities, weights, Hamiltonian, or dynamics are selected, and there
  is no claim about which mover is realized.
- The modulus shadow `M(U)=0` is strictly weaker than covariance modulo local
  frames, as the alternating-diagonal witness proves.
- The existing selector's missing physical bridge remains open. This note must
  not be cited as discharging that repair target.

## Falsifiers

- A covariant availability rule and fixed, site-independent `F` satisfying the
  fixed-assignment condition whose realized tick has `M(U)>0` would refute the
  covariance implication and its modulus shadow.
- A local diagonal frame that renders `U_alt` one-site covariant would refute
  the strictness witness.
- Failure of the displayed Givens direct sum to be unitary or
  nearest-neighbor supported, or a literal computation giving
  `M(U_giv)=0`, would refute the fixed-assignment sharpness witness.
- Failure of the cumulative-product gauge to close or to uniformize either
  fixed phase list in the runner would refute mover gauge uniformization.
- A varying rule satisfying conditioning faithfulness whose realized tick has
  `O(U)=false` would refute the variation-to-support implication.
- A nonempty variation set for the constant rule would refute the converse
  witness or the runner's variation extractor.

## Dependencies

- [MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) — the two
  Admissibility clauses quoted above and the boundary that kinetic branch
  realization is downstream. The ring, carrier, tick, and frame restrictions
  are stated hypotheses here, not content imported from this dependency.

The motivating selector row is context only and is not consumed by this
self-contained lemma:
`TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_NARROW_THEOREM_NOTE_2026-07-09.md`.

## Paired Runner

The deterministic NumPy runner
`scripts/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.py`
builds the ring operators as complex matrices. It checks the support surface,
the fixed-assignment covariance lemma including strictness and a sharpness
witness, mover gauges in both directions, conditioning-faithfulness bookkeeping
including its sharpness and converse failure, and exact clause pins against the
minimal-axiom source. Every positive numerical construction is paired with a
contrasting object that the same machinery rejects. The runner writes no cache
itself.

Runner cache:
[`logs/runner-cache/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.txt`](../logs/runner-cache/tick_admissibility_realization_bridge_clause_to_predicate_2026_07_10.txt)

Current local runner result is recorded in the SHA-pinned cache.
