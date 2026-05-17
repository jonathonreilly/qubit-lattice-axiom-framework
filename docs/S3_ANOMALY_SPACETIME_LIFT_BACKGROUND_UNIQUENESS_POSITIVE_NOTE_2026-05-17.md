# S^3 + Anomaly-Forced Time: Background Composition Uniqueness (Positive)
# + Observable-Hessian Dynamics-Bridge Channel No-Go (Sharp)

**Date:** 2026-05-17
**Type:** positive_theorem (kinematic background composition) + named no-go (observable-Hessian dynamics-bridge channel)
**Claim scope:** TWO scope-bounded claims on the route-2 spacetime-lift step.

  - **Claim A (positive theorem):** Given (i) the cited PL `S^3` spatial
    background candidate from the PL boundary-link + PL cap-uniqueness chain
    and (ii) the cited anomaly-forced single-clock evolution structure
    `U(t) = exp(-itH)` from `ANOMALY_FORCES_TIME_THEOREM.md` together with
    `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`,
    the kinematic background candidate consistent with both inputs is uniquely
    the non-compact direct product `PL S^3 × R`. Three named alternative
    product manifolds (`PL S^3 / Z_k × R` quotient, `PL S^3 × S^1` periodic-time,
    `PL S^3 × {*}` trivial-time) are each excluded by an explicit single-step
    contradiction with one of the cited inputs.
  - **Claim B (named no-go):** Any dynamics-bridge primitive that factorizes
    through the scalar observable generator `W[J] = log|det(D+J)|` evaluated
    against a scalar source channel `J = sum_a j_a P_a` (with `P_a` scalar
    site projectors) and is built from finite-order source derivatives of `W`
    yields a multilinear *scalar* source form, NOT a rank-`(0,2)` covariant
    tensor field on `PL S^3 × R`. In particular the second variation
    `δ²W/δj_x δj_y` is a scalar bilinear in source space and so cannot be
    promoted to an Einstein/Regge field equation by Hessian extraction alone.
    Therefore the observable-Hessian dynamics-bridge channel is structurally
    incapable of supplying any of the three named open dynamics primitives
    (P-1 spacetime-lift observable, P-2 GR-field-equation action, P-3
    uniqueness theorem) named in §"What the route would need" of
    `S3_ANOMALY_SPACETIME_LIFT_NOTE.md`.

  Claim A is a positive composition theorem in the cited-imports class A
  (algebraic identification under three named upstream authorities). Claim B
  is a structural impossibility result with explicit source-tensor-rank
  arithmetic. Together they:
  (a) close the implicit kinematic-uniqueness substep of the parent
      `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` (which states `PL S^3 × R`
      as the kinematic background without naming uniqueness), and
  (b) eliminate one of the three named open dynamics-bridge channels
      (the observable-Hessian channel), narrowing the remaining open
      problem to non-Hessian dynamics-bridge candidates only.

**Status:** awaiting independent audit. Source-note status is not an audit
verdict. The author does NOT propose retained / positive_theorem promotion
of `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` itself; this note records two
scope-bounded substep closures (one positive composition theorem on the
kinematic background, one structural no-go on the observable-Hessian
dynamics-bridge channel), and leaves the parent row as `open_gate` with
sharpened residual dynamics-bridge surface.
**Status authority:** independent audit lane only.
**Loop:** `filter-excluded-positive-closures-2026-05-17`
**Block:** 07 (s3-anomaly-spacetime-lift)
**Branch:** `physics-loop/s3-anomaly-spacetime-lift-block07-2026-05-17`
**Primary runner:** [`scripts/s3_anomaly_spacetime_lift_block07_check.py`](../scripts/s3_anomaly_spacetime_lift_block07_check.py)

---

## Audit boundary

This note is a scope-bounded substep claim on the parent open_gate
`S3_ANOMALY_SPACETIME_LIFT_NOTE.md`. The note does NOT close the parent
row; it closes two substeps.

**Cited authorities (one-hop deps; cited, not closed in this note):**

- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  (`claim_type: positive_theorem`, `audit_status: audited_conditional`) —
  PL boundary-link disk theorem on `B_R`; supplies one of the two
  authorities behind the PL `S^3` spatial background candidate.
- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_conditional`) —
  PL cap-uniqueness; cone-capping is the unique closure to a simply
  connected PL 3-manifold. Combined with the boundary-link disk theorem
  this gives the PL `S^3` candidate at the kinematic level.
- [`ANOMALY_FORCES_TIME_THEOREM.md`](ANOMALY_FORCES_TIME_THEOREM.md)
  (`claim_type: bounded_theorem`) — gauge-anomaly-forced single-time
  direction `d_t = 1`. Imported for the temporal-factor cardinality.
- [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
  (`claim_type: positive_theorem (lattice form)`, `audit_status:
  audited_conditional`) — strongly-continuous one-parameter unitary
  group `U(t) = exp(-itH)` indexed by `t ∈ R`. Imported here as the
  temporal-factor-topology authority: the group parameter is on the
  non-compact real line, not on a compact circle, so the time factor
  of the kinematic background is non-compact `R`, not `S^1`.
- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  (`claim_type: bounded_theorem`, `audit_status: audited_conditional`) —
  the scalar observable generator `W[J] = log|det(D+J)| - log|det D|`
  on the exact minimal hierarchy block. Imported in Claim B as the
  scalar generator whose finite-order source derivatives produce
  scalar multilinear forms (and not rank-(0,2) covariant tensors).
- [`S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md`](S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md)
  (open_gate, prior route note). Cited as the prior negative-direction
  observation that the Hessian channel is scalar-only on this route;
  Claim B promotes that observation to a sharp structural no-go with
  explicit source-tensor-rank arithmetic.
- [`S3_ANOMALY_SPACETIME_LIFT_NOTE.md`](S3_ANOMALY_SPACETIME_LIFT_NOTE.md)
  (open_gate, parent). Cited as the parent row whose two substeps
  (kinematic background uniqueness; dynamics-bridge channel exclusion)
  are closed here.

**In-note content (what the runner actually verifies):**

- Claim A: three single-step contradictions exclude each named
  alternative product manifold against the cited inputs (Lemmas A1, A2,
  A3 below). The remaining product is `PL S^3 × R`.
- Claim B: source-tensor-rank arithmetic on `W[J]` shows finite-order
  source derivatives are scalar-valued multilinear forms in the source
  channel; the rank of the spacetime-tensor output is zero regardless
  of derivative order, so no Hessian channel produces a rank-(0,2)
  covariant tensor (Lemma B1 below). The four named coupling-promotion
  attempts (B2a/B2b/B2c/B2d) each fail to produce a rank-(0,2) tensor
  by explicit rank counting.

**Admitted-context derivation gap (what this note does NOT close):**

- This note does NOT derive any of the three named open dynamics-bridge
  primitives (P-1/P-2/P-3) of the parent note. Claim B eliminates the
  observable-Hessian channel; it does NOT exclude non-Hessian dynamics-
  bridge candidates (e.g. the transfer-matrix bridge of
  `S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md`, the discrete Einstein/Regge
  lift of `DISCRETE_EINSTEIN_REGGE_LIFT_NOTE.md`, or any candidate that
  augments the scalar source channel with a tensor-valued source
  channel).
- This note does NOT close the parent `open_gate`. The parent row's
  dynamics-bridge primitive remains open; Claim B narrows the residual
  surface (Hessian channel excluded) but does not close it.

---

## Setup and notation

Let `M_3 = PL S^3` denote the closed simply-connected PL 3-manifold
obtained from the cone-capped cubical ball as per the cited PL
boundary-link + PL cap-uniqueness chain.

Let `H : H_phys -> H_phys` denote the reconstructed Hamiltonian and
`U(t) = exp(-itH)` the strongly-continuous one-parameter unitary group
of `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`,
indexed by `t ∈ R`.

A *candidate kinematic background* is any product manifold `M_3 ⊠ T`
where `T` is a connected 1-manifold (possibly with boundary). The four
candidate spacetimes generated by the cited inputs alone are:

| Candidate | Spatial factor    | Time factor |
|-----------|-------------------|-------------|
| C-0       | PL `S^3`          | `R`         |
| C-1       | PL `S^3 / Z_k`    | `R`         |
| C-2       | PL `S^3`          | `S^1`       |
| C-3       | PL `S^3`          | `{*}` (point) |

Candidate C-0 is the parent note's `PL S^3 × R`. Claim A excludes
C-1, C-2, C-3 by single-step contradiction with the cited inputs,
proving the candidate space {C-0, C-1, C-2, C-3} reduces to {C-0}.

---

## Claim A: Kinematic background composition uniqueness (positive theorem)

**Theorem A (kinematic background uniqueness).** Under the cited inputs
(PL `S^3` from cap-uniqueness chain; one-parameter unitary group
`U(t) = exp(-itH)` indexed by `t ∈ R` from single-clock codim-1
evolution; gauge-anomaly-forced `d_t = 1`), the kinematic background
candidate satisfying all three inputs is uniquely

> `PL S^3 × R`  (candidate C-0).

The three alternative products C-1, C-2, C-3 are each excluded by a
single-step contradiction with one of the cited inputs.

### Lemma A1 (exclude C-1: PL `S^3 / Z_k × R`)

Suppose the spatial factor were `PL S^3 / Z_k` for some `k >= 2`. The
cap-uniqueness theorem (`S3_CAP_UNIQUENESS_NOTE.md`, §"What Is Actually
Proved", Step 4.1) states: "By the Poincaré conjecture (Perelman 2003)
and Moise's theorem (1952, TOP = PL in dimension 3), M is PL
homeomorphic to PL `S^3`." The Poincaré-Perelman closure was applied
SPECIFICALLY to the simply-connected closure `M = B ∪_{∂B} X`; the
hypothesis `pi_1(M) = 0` is built into the cap-uniqueness statement.

Now `pi_1(PL S^3 / Z_k) = Z_k` is non-trivial for `k >= 2`, in
contradiction with the `pi_1 = 0` hypothesis of the cap-uniqueness
theorem. Therefore C-1 cannot satisfy the cited PL `S^3` input as
stated. C-1 is excluded.  QED.

### Lemma A2 (exclude C-2: PL `S^3 × S^1`)

Suppose the temporal factor were a compact `S^1` of period `T > 0`,
so that the time direction is the circle `S^1 = R / T*Z`. The cited
single-clock theorem
(`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`)
states that the evolution generator `H` produces a strongly-continuous
one-parameter unitary group `U(t) = exp(-itH)` indexed by `t ∈ R`. If
the time were periodic with period `T > 0`, then `U(T) = U(0) = I`,
which forces `exp(-iTH) = I`, hence `Sp(H) ⊂ (2π/T) Z`, i.e. the
spectrum of `H` is discrete and bounded below by `0` only if `H` were
positive-semidefinite-on-an-arithmetic-progression. But this contradicts
the cited theorem's S1: `U(t)` is "the unique generator of a
strongly-continuous one-parameter unitary group", not the
periodic-time generator of a unitary representation of `U(1)`. The
single-clock S1 statement names `R` (not `U(1)`) as the parameter
group. Therefore the cited input forbids a compact periodic time
factor.

Stronger consequence: the same theorem's S2 requires arbitrary
codimension-1 Cauchy data at each `Σ_t = {t} × Z^3`. For any local
operator that does not commute with `H`, the Heisenberg evolution
`A(t) = U(t)^† A U(0) U(t)` is generically non-periodic; periodic time
would force `A(t + T) = A(t)`, contradicting the existence of generic
non-stationary Heisenberg trajectories on the lattice. Therefore C-2
cannot satisfy the cited single-clock input. C-2 is excluded.  QED.

### Lemma A3 (exclude C-3: PL `S^3 × {*}`)

Suppose the temporal factor were a single point `{*}`, so that the
spacetime has zero temporal dimension. The cited
`ANOMALY_FORCES_TIME_THEOREM.md` derives `d_t = 1`, which by Step 5 of
its proof forces "exactly one temporal dimension". A spacetime
`PL S^3 × {*}` has temporal dimension `d_t = 0`, contradicting the
cited theorem's conclusion. Therefore C-3 cannot satisfy the cited
anomaly-forced-time input. C-3 is excluded.  QED.

### Composition

By Lemmas A1, A2, A3, the candidate set {C-0, C-1, C-2, C-3} reduces
to {C-0}. Therefore the kinematic background candidate satisfying all
three cited inputs is uniquely

> `PL S^3 × R`.  QED.

This is the positive composition theorem promised in Claim A. It is
NOT a derivation of the cited inputs; it is an algebraic composition
result that closes the implicit kinematic-uniqueness substep of the
parent `S3_ANOMALY_SPACETIME_LIFT_NOTE.md`.

---

## Claim B: Observable-Hessian dynamics-bridge channel no-go (structural)

**Theorem B (observable-Hessian dynamics-bridge channel exclusion).**
Let `W[J] = log|det(D+J)| - log|det D|` be the scalar observable
generator of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`, evaluated
against a scalar source channel `J = sum_a j_a P_a` with scalar site
projectors `P_a` (i.e. each `P_a` is a `dim(D) × dim(D)` matrix
acting on the fermionic mode space). Then for any finite derivative
order `n >= 1`, the `n`-th source derivative

> `W^(n)_{a_1,...,a_n} := (∂^n W / ∂j_{a_1} ... ∂j_{a_n})|_{J=0}`

is a scalar `n`-multilinear form in the source labels `(a_1, ..., a_n)`,
NOT a rank-`(0,2)` covariant tensor field on `PL S^3 × R`. The rank of
the spacetime-tensor output is zero for every finite `n`.

In particular, the second source derivative

> `W^(2)_{a,b} = -Re Tr[(D)^(-1) P_a (D)^(-1) P_b]`

is a real symmetric scalar bilinear form on source labels, and is NOT
a rank-(0,2) covariant tensor on `PL S^3 × R`.

Consequently, no dynamics bridge whose Euler-Lagrange equation is the
Hessian of `W` against the scalar source channel can produce a
covariant rank-(0,2) Einstein/Regge field equation on `PL S^3 × R`.
The observable-Hessian dynamics-bridge channel is therefore structurally
incapable of supplying any of the three named open dynamics-bridge
primitives (P-1 spacetime-lift observable, P-2 GR-field-equation
action, P-3 uniqueness theorem) named in §"What the route would need"
of `S3_ANOMALY_SPACETIME_LIFT_NOTE.md`.

### Lemma B1 (source-tensor-rank arithmetic on `W^(n)`)

The source channel `J = sum_a j_a P_a` is a scalar linear combination
of fixed matrices `P_a`. By chain rule and Jacobi's formula
`d log det(M) = Tr(M^(-1) dM)`, the first variation is

> `δW = Tr((D+J)^(-1) δJ) = sum_a (δj_a) * Tr((D+J)^(-1) P_a)`,

so `W^(1)_a = Tr(D^(-1) P_a)` is a scalar in source label `a`.

For the second variation, using `δ(M^(-1)) = -M^(-1) (δM) M^(-1)`:

> `δ²W = -Tr((D+J)^(-1) δJ (D+J)^(-1) δJ)`,
> giving `W^(2)_{a,b} = -Tr(D^(-1) P_a D^(-1) P_b)` (real part after
> CPT-even projection).

By induction on `n`, the `n`-th variation is

> `W^(n)_{a_1,...,a_n} = (-1)^(n-1) (n-1)! * sum_(σ ∈ S_n / cyclic)
>                          Tr(D^(-1) P_{a_σ(1)} D^(-1) P_{a_σ(2)} ... D^(-1) P_{a_σ(n)})`

which is a sum of traces of operator products in the fermion mode
space, summed over cyclic permutations of `n` source labels. The
output is a single complex number per index tuple
`(a_1, ..., a_n)`; the spacetime-tensor rank of the output is zero
(scalar field on source-label space).

This concludes Lemma B1: every finite source derivative of `W` is a
scalar multilinear form in source labels with spacetime-tensor rank
zero.  QED.

### Lemma B2 (four named coupling-promotion attempts fail)

The Hessian channel is naturally a scalar bilinear form in source
labels. To promote it to a rank-(0,2) covariant tensor on `PL S^3 × R`,
one would need an additional structural ingredient. We enumerate the
four named promotion attempts and show each fails to produce a
rank-(0,2) covariant tensor by explicit rank counting.

**Attempt B2a: pair source labels (a, b) with covariant index pair
(mu, nu).**  The proposal: identify `W^(2)_{a,b}` with a metric tensor
component `g_{mu, nu}` by some index labeling `a ↔ mu`, `b ↔ nu`.

Rank count: source labels `(a, b)` index scalar site projectors `P_a`,
`P_b`, NOT covariant directions on `PL S^3 × R`. Each `P_a` is a
`dim(D) × dim(D)` matrix; the source labels run over a discrete index
set (lattice sites or mode labels), not over the 4 covariant tangent
directions at a point. A bijection `a ↔ mu` would require source
labels to come in groups of 4 per spacetime point with covariant
transformation law, which is NOT supplied by the scalar projectors
`P_a`. Attempt B2a fails by lack of a covariant transformation law on
source labels.

**Attempt B2b: contract with two fixed vector fields `(X^mu, Y^nu)`.**
The proposal: form `W^(2)_{ab} X^a Y^b` and call the result the
`(mu, nu)` component of a tensor by some additional index lifting.

Rank count: contracting a scalar bilinear `W^(2)_{ab}` with two
source-index vector fields produces a scalar, NOT a rank-(0,2) tensor.
The covariant indices `(mu, nu)` are NOT introduced by source-index
contraction; they would have to come from the vector fields `(X^mu,
Y^nu)` themselves, but the contraction sums them out. Attempt B2b
fails: the output rank is zero.

**Attempt B2c: take the Hessian against a tensor-valued source `J^mu`
instead of a scalar source `J`.**  The proposal: replace the scalar
source channel with a vector- or tensor-valued source.

Rank count: this is precisely the move named as one of the two
admissible escape routes in the parent note (§"What this changes":
augment the observable generator with a tensor-valued source channel).
The current `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` derives `W` from
the *scalar* additivity premise P1; a tensor-valued source channel
would require a separate derivation of an enlarged additivity premise
(or a new observable principle). No such derivation is supplied on
the current atlas. Attempt B2c is NOT a Hessian-channel closure; it
explicitly leaves the observable-Hessian channel and enters a separate
channel (tensor-valued observable). Hence it does not contradict
Claim B's exclusion of the observable-Hessian channel; it is the
named escape route.

**Attempt B2d: differentiate `W` along a metric perturbation `h_{mu
nu}` directly via the operator `D[g]`.**  The proposal: treat `W` as
a functional of the background geometry through the Dirac operator
`D[g]` and take a metric Hessian
`δ²W / δg_{mu nu}(x) δg_{rho sigma}(y)`.

Rank count: this introduces a *new* source channel (metric perturbations
`h_{mu nu}` taking values in symmetric rank-2 tensors), distinct from
the scalar source channel `J = sum_a j_a P_a` that defines the
observable principle in `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`. The
output is rank-(0,4) (bi-tensor index `(mu nu, rho sigma)`), not
rank-(0,2), and again requires an additional derivation step
(geometric source coupling to `D`) that is not part of the cited
observable principle. Attempt B2d is structurally analogous to B2c:
it escapes the observable-Hessian channel by introducing a new source
channel, which is again the named non-Hessian escape route. It does
NOT close the Hessian channel.

### Composition of Lemmas B1, B2

By Lemma B1, every finite source derivative of `W` against the scalar
source channel is a scalar multilinear form (spacetime-tensor rank
zero). By Lemma B2 (B2a, B2b), no rank-promotion of these scalar
forms within the observable-Hessian channel yields a rank-(0,2)
covariant tensor on `PL S^3 × R`. Attempts B2c and B2d are the two
named escape routes to non-Hessian channels (tensor-valued or
metric-perturbation source), each of which leaves the Hessian channel
and is therefore outside the scope of Claim B's exclusion.

Conclusion: the observable-Hessian dynamics-bridge channel is
structurally incapable of producing a rank-(0,2) covariant tensor
field equation on `PL S^3 × R`. The three named open dynamics-bridge
primitives (P-1, P-2, P-3) cannot be supplied through this channel.
The remaining dynamics-bridge surface for the route is reduced to
non-Hessian candidates: (i) the transfer-matrix bridge of
`S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md`, (ii) the discrete
Einstein/Regge lift of `DISCRETE_EINSTEIN_REGGE_LIFT_NOTE.md` on the
restricted static-conformal class, (iii) tensor-valued source channel
(named escape B2c), and (iv) metric-perturbation source channel (named
escape B2d).  QED.

---

## Effect on the parent note

The parent `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` says:

> "[The composition `PL S^3 × R`] is the right kinematic target"
> (§"Route 2 in context")

without naming what alternatives are excluded by which cited inputs.
Claim A makes the composition uniqueness explicit (one positive
composition theorem; three single-step exclusions).

The parent note also says:

> "no exact `S^3`-to-curvature law is present"
> "no exact anomaly-to-Einstein-field-equation derivation is present"
> "no exact discrete variational action is present for this route"
> (§"Verdict")

These are three negatives. The companion `S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md`
observes that the observable principle is "scalar-only on this route" but
does not promote that observation to a structural no-go with rank
arithmetic. Claim B does the rank arithmetic explicitly (Lemma B1 + Lemma
B2), showing the Hessian channel is structurally incapable of supplying
P-1/P-2/P-3 on the route. This is a sharp dynamics-bridge channel
exclusion, not a closure of the parent note.

The residual dynamics-bridge surface after this note is the four named
non-Hessian candidates (i)/(ii)/(iii)/(iv) listed at the end of §"Lemmas
B1, B2 composition" above. Each is a separate open theorem target.

---

## Runner verification

`scripts/s3_anomaly_spacetime_lift_block07_check.py` performs the
following exact algebraic / rank-counting checks (no fitted, no
observational, no literature):

**Claim A checks (kinematic background composition uniqueness):**

- A1 (C-1 exclusion): construct the cyclic group `Z_k` for `k = 2, 3, 4, 5`
  and verify that `pi_1(S^3 / Z_k) = Z_k` is non-trivial for each `k >= 2`
  (computed as cardinality `|Z_k| = k >= 2`); confirm contradiction with
  `pi_1 = 0` hypothesis of the cap-uniqueness theorem.
- A2 (C-2 exclusion): for periodic time of period `T > 0`, check
  `U(T) = I` forces `Sp(H) ⊂ (2π/T) Z` on a finite Hilbert space sample
  by direct spectral computation; verify the existence of generic local
  operators `A` whose Heisenberg trajectories `A(t)` are non-periodic
  (constructed as random hermitian projectors on a 4-d sample Hilbert
  space; non-periodicity verified to numerical tolerance `1e-10`).
- A3 (C-3 exclusion): direct dimensional check `d_t({*}) = 0 != 1`.
- A4 (composition uniqueness): tabulate the four candidates
  {C-0, C-1, C-2, C-3} and verify each of A1/A2/A3 rules out
  C-1/C-2/C-3 respectively, leaving C-0 as the unique survivor.

**Claim B checks (observable-Hessian channel no-go):**

- B1a (source-derivative scalar rank): on a `dim(D) = 4` sample Dirac
  operator with 3 scalar site projectors `P_1, P_2, P_3`, compute
  `W^(2)_{a,b} = -Re Tr(D^(-1) P_a D^(-1) P_b)` for all `(a, b)` and
  verify the output is a scalar (single real number) per index pair,
  i.e. spacetime-tensor rank zero.
- B1b (third source derivative scalar rank): compute `W^(3)_{a,b,c}` on
  the same sample and verify scalar rank zero.
- B2a (label-bijection rank failure): attempt to identify source labels
  `(a, b)` with covariant indices `(mu, nu)` on `PL S^3 × R` (sample:
  4-dimensional tangent space at one point). Verify the source labels
  do NOT carry the covariant transformation law: under a sample
  coordinate rotation `R ∈ SO(4)`, the scalar projectors `P_a` are
  invariant (source labels are unchanged by spacetime coordinate
  changes), while a covariant rank-(0,2) tensor would transform as
  `T'_{mu nu} = R^a_mu R^b_nu T_{a b}`. Verify the no-transformation
  property of `P_a` produces a contradiction with covariant
  transformation, certifying B2a fails by lack of transformation law.
- B2b (contraction rank reduction): form `W^(2)_{ab} X^a Y^b` for a
  pair of sample source-index vectors `X, Y` and verify the result is
  a scalar (rank zero), not a rank-(0,2) tensor.
- B2c/B2d (named escapes outside Hessian channel): record as
  out-of-Hessian-channel; runner emits a `NAMED_ESCAPE` line per attempt
  with an algebraic check that the escape introduces a NEW source
  channel (tensor- or metric-valued) distinct from the scalar source
  channel of `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.

**SCORECARD line:** the runner emits a single `SCORECARD` line
`A_checks_pass / total | B_checks_pass / total | named_escapes / 2`
summarizing the count of exact-algebra checks passed.

---

## Honest assessment

**What is proved (positive):**
- Theorem A: `PL S^3 × R` is the unique kinematic background composition
  under the three cited inputs; the three alternative product manifolds
  are excluded by named single-step contradictions (Lemmas A1, A2, A3).
- Lemma B1: every finite source derivative of the scalar observable
  generator `W[J] = log|det(D+J)| - log|det D|` against a scalar source
  channel is a scalar multilinear form with spacetime-tensor rank zero.
- Lemma B2 (parts B2a, B2b): no rank-promotion within the observable-
  Hessian channel produces a rank-(0,2) covariant tensor on
  `PL S^3 × R`. The two named escape routes B2c (tensor-valued source)
  and B2d (metric-perturbation source) explicitly leave the Hessian
  channel and are out-of-scope of Claim B's exclusion.

**What is NOT proved (out of scope):**
- The parent `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` open_gate is NOT
  closed. The note's three named dynamics-bridge primitives (P-1
  observable, P-2 action, P-3 uniqueness) remain open on the four
  named non-Hessian candidate channels.
- No retained / positive_theorem promotion is proposed for the parent
  row.
- The cited upstream authorities (PL `S^3` chain, anomaly-forced time,
  single-clock evolution, observable principle) are imported, not
  re-derived. Their own `audited_conditional` status is unchanged by
  this note.

**Effect on the route's open surface:**
- Block 02 (this campaign) already classified `AC_φλ` into P1/P2/P3
  closure paths. Block 07 here adds:
  - Substep closure 1 (Claim A): the implicit kinematic-uniqueness
    step of the parent note is now an explicit positive composition
    theorem.
  - Substep closure 2 (Claim B): the observable-Hessian dynamics-
    bridge channel is structurally excluded, narrowing the residual
    open surface to four named non-Hessian channels.
- The route remains `open_gate` at the parent level; the residual
  open problem is now sharper (named non-Hessian channels only).

**Verdict (scope-bounded):** Two scope-bounded substep closures land
on the parent open_gate route. The parent row stays `open_gate`. The
author does NOT propose retained or positive_theorem promotion for
the parent. The note's authority is the algebraic content of Lemmas
A1/A2/A3/B1/B2 plus the runner's direct rank-arithmetic verification.

---

## References

(All references are internal source-theorem notes on the current `main`;
no external observational, fitted, or literature data is used.)

- `S3_ANOMALY_SPACETIME_LIFT_NOTE.md` (parent open_gate; cited)
- `S3_BOUNDARY_LINK_THEOREM_NOTE.md` (PL boundary-link disk theorem)
- `S3_CAP_UNIQUENESS_NOTE.md` (PL cap-uniqueness)
- `ANOMALY_FORCES_TIME_THEOREM.md` (anomaly-forced `d_t = 1`)
- `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
  (single-clock `U(t) = exp(-itH)` on `R`)
- `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` (scalar generator `W[J]`)
- `S3_TIME_OBSERVABLE_HESSIAN_ROUTE_NOTE.md` (prior negative-direction
  observation; promoted here to sharp structural no-go)
- `S3_TIME_TRANSFER_MATRIX_BRIDGE_NOTE.md` (named non-Hessian
  candidate (i) of residual surface)
- `DISCRETE_EINSTEIN_REGGE_LIFT_NOTE.md` (named non-Hessian candidate
  (ii) of residual surface)
