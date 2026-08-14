---
claim_id: stabilizer_covariant_pvm_uniqueness_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "Fix n=(1,0,0). Rank-1 projectors on C^2 are P_u=(I+u·σ)/2 for |u|=1, and a rank-1 PVM is the pair {P_u, P_{-u}}. The displayed stabilizer rotation R(x,y,z)=(x,-z,y) acts on Bloch vectors. The only unit vectors with R u=±u, and likewise for R^2 and R^3, are u=±e_x. Hence the unique rank-1 PVM covariant under rotations about n is the spectral pair of n. No physical menu-selection rule is derived."
upstream_dependencies:
  - minimal_axioms
runner: scripts/stabilizer_covariant_pvm_uniqueness_2026_08_14.py
---

# Unique Stabilizer-Covariant Rank-1 PVM Given `n`

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact integer and rational Bloch-vector algebra for one displayed
order-4 rotation about a fixed axis `n`. The output is uniqueness of that
spectral rank-1 PVM. No physical support selector, Qubit rewrite, or
adopted menu law is claimed.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/stabilizer_covariant_pvm_uniqueness_2026_08_14.py`](../scripts/stabilizer_covariant_pvm_uniqueness_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result Up Front

Fix the axis `n = (1,0,0)`. Scale of `n` does not matter. Rank-1 projectors
on `C^2` are `P_u = (I + u·σ)/2` for `|u|=1`. A rank-1 PVM is the pair
`{P_u, P_{-u}}`. That pair always totalizes: `P_u + P_{-u} = I`.

The stabilizer of `n` in the proper cube group contains the 90-degree
rotation about the first coordinate axis

```text
R(x,y,z) = (x, −z, y).
```

`R` acts on Bloch vectors. The PVM `{P_u, P_{-u}}` is covariant under `R`
if and only if `{R u, −R u} = {u, −u}` as unordered pairs, equivalently
`R u = ± u`. The same set-equality is required for `R^2` and `R^3`.

**Theorem.** The only unit vectors satisfying `R u = ± u` for this `R`,
and also for `R^2` and `R^3`, are `u = ± e_x`. Therefore the only rank-1
PVM covariant under these rotations about `n` is the spectral pair
`{P_n, P_{-n}}`. This note names that unique pair the menu axis of `n`.
The name is mathematical: it does not assert that Admissibility selects
this pair as a physical support.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact integer linear algebra classifies the Bloch vectors fixed up to sign by the displayed order-4 stabilizer rotation about n, and the resulting rank-1 PVM is unique."
trace_class: frontier_discovery
target_claim_id: stabilizer_covariant_pvm_uniqueness
target_blocker_text: "whether more than one rank-1 PVM is covariant under rotations about a fixed axis n"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded algebraic uniqueness claim"
conditional_surface_status: "exact for the displayed R about n=(1,0,0); other axes are equivalent by a coordinate relabel, but no physical menu law is claimed"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Import Boundary

- **Framework dependency:** the live Qubit sentence supplies the
  repository's one-site `M_2(C)` terminology. The live Admissibility
  sentences supply covariance of the nearest-neighbor rule under proper
  cubic rotations. Both are quoted without rewrite. As the registered
  `minimal_axioms` premise, the memo is not a bounded-status source.
- **Explicit theorem-domain condition:** the axis `n=(1,0,0)`, the Bloch
  chart `P_u=(I+u·σ)/2`, and the displayed rotation `R` are supplied
  mathematical data for this theorem. The note does not claim that the
  axioms derive a physical Bloch chart or a physical menu-selection rule.
- **External empirical or literature inputs:** none.
- **Open physical bridge:** whether Admissibility's support at a site is
  this spectral pair remains a separate, open obligation.

## Exact Objects

All runner coefficients are exact integers or `Fraction` values. No float
is used. Scale of a Bloch label does not matter for the PVM, because
`P_u` depends only on the unit direction; the companion runner therefore
classifies integer vectors in `Z^3` and then imposes the unit condition
on the surviving line.

```text
e_x = (1,0,0),   e_y = (0,1,0),   e_z = (0,0,1)
R(x,y,z) = (x, −z, y)
R^2(x,y,z) = (x, −y, −z)
R^3(x,y,z) = (x, z, −y)
R^4 = id
```

The spectral pair of `n` is written with exact rational matrices

```text
P_n     = (I + σ_x)/2 = ((1/2, 1/2), (1/2, 1/2))
P_{-n}  = (I − σ_x)/2 = ((1/2, −1/2), (−1/2, 1/2))
```

and obeys `P_n + P_{-n} = I`, `Tr(P_n) = Tr(P_{-n}) = 1`.

## Exact Target And Proof Obligations

The exact target is to classify the unit Bloch vectors whose rank-1 PVM
is covariant under `R`, `R^2`, and `R^3`, and to identify the unique
such PVM as the spectral pair of `n`.

The obligation graph is:

1. `R e_x = e_x`, so the spectral axis works, and the constructed pair
   totalizes;
2. `R e_y = e_z ≠ ± e_y`, so the `e_y` axis fails;
3. `R e_z = −e_y ≠ ± e_z`, so the `e_z` axis fails;
4. the unnormalized equatorial label `(0,1,1)` is sent to `(0,−1,1)`,
   which is not `±(0,1,1)`;
5. a general triple `u=(a,b,c)` is solved exactly over `Q`: the plus
   case forces `b=c=0`, and the minus case is empty on nonzero vectors;
6. every survivor of `R u = ± u` automatically satisfies the same
   sign-condition for `R^2` and `R^3`; the 180-degree condition
   `R^2 u = ± u` alone is strictly weaker.

All six obligations are closed below and in the runner. Other rotations,
other axes as independently chosen physical selectors, continuous
families of POVMs that are not rank-1 PVMs, and any identification of
the menu axis with a physical Admissibility support are outside the
target.

## Theorem 1 — the spectral axis is covariant and totalizes

`R e_x = (1,0,0) = e_x`. Hence `R^k e_x = e_x` for `k=1,2,3`, and
`{R^k e_x, −R^k e_x} = {e_x, −e_x}`. The associated rank-1 PVM is
`{P_n, P_{-n}}`. Direct matrix arithmetic gives

```text
P_n + P_{-n} = I,    Tr(P_n) = 1,    Tr(P_{-n}) = 1,
P_n^2 = P_n = P_n^*,    P_{-n}^2 = P_{-n} = P_{-n}^*.
```

The same identities hold after replacing `n` by `R^k n` for `k=1,2,3`,
because those labels are `n` itself. This is the constructed
PVM-totalize trace for each of those three powers.

## Theorem 2 — the `e_y` axis fails

`R e_y = (0,0,1) = e_z`. This is neither `e_y` nor `−e_y`. The pair
`{e_y, −e_y}` is therefore not covariant under `R`.

## Theorem 3 — the `e_z` axis fails

`R e_z = (0,−1,0) = −e_y`. This is neither `e_z` nor `−e_z`. The pair
`{e_z, −e_z}` is therefore not covariant under `R`.

## Theorem 4 — a displayed equatorial label fails

Stay in `Q` by using the unnormalized label `u = (0,1,1)`. Then
`R u = (0,−1,1)`. The two triples `(0,−1,1)` and `±(0,1,1)` are
unequal, so this label is not an axis of the PVM-covariance condition.
(The corresponding unit vector is a positive rational multiple of `u`
times a common positive scale; the scale cannot restore a missed
sign-eigenvalue of `R`.)

## Theorem 5 — only `± e_x` survive

Let `u = (a,b,c)` with `a,b,c ∈ Q`. Then `R u = (a, −c, b)`.

Plus case `R u = u`: the last two coordinates give `b = −c` and `c = b`,
hence `b = c = 0`, while `a` is free. The rational solutions are the
line spanned by `e_x`. Imposing `|u|=1` leaves exactly `u = ± e_x`.

Minus case `R u = −u`: the first coordinate gives `a = −a`, hence
`a = 0`. The remaining equations are `(−c, b) = (−b, −c)`, equivalently
`b = c` and `b = −c`, hence `b = c = 0`. The only rational solution is
the zero triple, which is not a unit vector. The minus case is empty.

Thus the only unit solutions of `R u = ± u` are `u = ± e_x`. These two
labels determine one and the same rank-1 PVM `{P_n, P_{-n}}`.

## Theorem 6 — `R^2` and `R^3` do not add extra survivors

If `R u = ± u`, then `R^2 u = R(± u) = ± R u = u` and
`R^3 u = R(R^2 u) = R u = ± u`. Every survivor of Theorem 5 therefore
satisfies the same sign-condition for `R^2` and `R^3`.

The 180-degree condition alone is strictly weaker. Direct evaluation
gives `R^2 e_y = −e_y` and `R^2 e_z = −e_z`, so both equatorial axes
are covariant under `R^2` and fail already under `R`. Uniqueness uses
the order-4 generator, not only the 180-degree square.

## Physical-Interpretation Boundary

The proved output is uniqueness of the displayed spectral pair among
rank-1 PVMs covariant under this stabilizer rotation. The phrase
“menu axis” names that pair and does not change the Qubit statement.
`R` is displayed rotation data on Bloch vectors, not axiom content, and
no additional axiom is proposed. Admissibility is not shown to select
this pair.

## Mutation Checks

Four non-equivalences guard the load-bearing conclusions:

1. `R e_y ≠ ± e_y` and `R e_z ≠ ± e_z`;
2. `R(0,1,1) ≠ ±(0,1,1)`;
3. the minus eigenspace of `R` on `Q^3` is `{0}`;
4. `R^2 e_y = −e_y`, so replacing `R` by `R^2` would admit extra axes.

## What This Does Not Claim

- No Qubit rewrite.
- No derived Admissibility support selector and no physical locking of
  the menu axis by Record.
- No claim that every covariant POVM, as opposed to every rank-1 PVM,
  is this pair.
- No classification of rank-1 PVMs under a proper subgroup generated
  only by `R^2`.
- No lattice-wide gluing, nearest-neighbor weight, or formation rule.
- Independent class-`C` leftovers are not used as parents.

These are scope boundaries, not impossibility or route-exhaustion claims.
Accordingly, no no-go verdict is authored here.

## Live Parent Quotes

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone.

> There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

> For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

Their dependency role is limited to the repository's local-algebra
vocabulary and to the named covariance of the Admissibility rule under
proper cubic rotations. This theorem separately supplies `n`, the Bloch
chart, and `R`; physical selection of the menu axis remains outside its
target.

## Runner Contract

The companion runner checks Theorems 1–6 with exact integer vectors and
exact rational matrix arithmetic. In particular, it row-reduces the plus
and minus eigen-conditions on a general rational triple rather than
sampling a coefficient grid. It constructs the spectral pair, verifies
the PVM-totalize traces for `k=1,2,3`, rejects the four mutations,
quotes the live Qubit and Admissibility sentences, prints substantive N5
scope certificates, and records the import boundary. Declared review
inputs are this note and the axiom memo only.
