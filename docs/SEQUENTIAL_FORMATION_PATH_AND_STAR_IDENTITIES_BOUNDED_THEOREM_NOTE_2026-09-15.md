---
claim_id: sequential_formation_path_and_star_identities_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "Exact conditional path/star joint-law identities, two-state and cubic-kernel residual formulas, and degree-two sphere moments in supplied sequential formation models. Explicit delayed-variation and radial-square witnesses delimit the scope. General negative certification and any axiom-derived physical process are deferred."
upstream_dependencies:
  - minimal_axioms
  - realized_state_primitive
runner: scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py
---

# Sequential formation: path and star identities

**Date:** 2026-09-15
**Type:** bounded_theorem
**Scope:** exact mathematics of the supplied finite sequential-product model;
finite-state rational checks and polynomial sphere moments. No physical process,
menu, order law or new axiom is selected. No audit verdict is applied.

**Primary runner:**
[`scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py`](../scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py)

**Pinned cache:**
[`logs/runner-cache/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.txt`](../logs/runner-cache/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.txt)

## Premises and authority

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) gives local
admissibility and permanent records, but specifies no sequential product
process, formation order/rate, selected menu or independent internal symmetry.
Those objects below are supplied mathematical hypotheses. The
[realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)
allows pointwise evaluation; it grants no distribution over alternative orders
and does not turn process-law statistics into registered state data.

Take an initially empty isolated finite nearest-neighbour window of `Z^3`.
At each step one site forms by a supplied kernel depending on its already
recorded neighbours. Joint probabilities are the sequential product of those
conditional laws. Write `mu_0` for the empty-neighbourhood law. The single-
neighbour kernel `K` is common to all spatial directions; this is an explicit
hypothesis stronger than lattice covariance. Otherwise the path composition
is `K_e2 K_e1`, not necessarily `K^2`.

The finite menus are a binary set with positive empty weight on each state,
and the six axis vectors with uniform empty law and cubic-covariant kernel.
For the sphere examples the empty law is normalized area measure and the
kernel is rotation covariant. Menus and internal covariance are supplied.
No Hamiltonian, empirical number, fitted parameter or physical readout bridge
is used. Repository authority links delimit premise grants, rather than
supplying the sequential model.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact conditional joint-law identities and constructive finite witnesses; broader negative certification is deferred."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "conditional sequential formation laws on finite windows"
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "preserve supplied process premises in any downstream use"
conditional_surface_status: "supplied sequential model, menus and covariance; finite identities and witnesses"
hypothetical_axiom_status: no edit
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Path identity

For an isolated path `L—M—R`, the ends-first order gives marginal
`mu_0(dL) mu_0(dR)`: the ends are independent because each forms with
no recorded neighbour. The chain order gives
`mu_0(dL) K(dM|L) K(dR|M)`, with endpoint marginal
`mu_0(dL) K^2(dR|L)`. Equality of the two order laws therefore implies
`K^2(.|L)=mu_0` for `mu_0`-almost every `L`. This is a necessary
endpoint identity, not a sufficient test of full order-law equality.

For a binary kernel let `pplus=K(+|+)`, `pminus=K(+|-)`. Direct
multiplication gives

```text
K^2(+|+) = pplus^2 + (1-pplus)pminus,
K^2(+|-) = pminus pplus + (1-pminus)pminus,
K^2(+|+) - K^2(+|-) = (pplus - pminus)^2.
```

With fair empty law and `(pplus,pminus)=(4/5,1/5)`, the chain has
`K^2(+|+)=17/25` and `P(L=R=+)=17/50`, whereas ends-first gives
`1/4`. With `pplus=pminus=1/2`, the endpoint laws agree exactly.
A degenerate empty law would test only its supported row, which is why the
full-support qualification matters for claims about both rows.

## Cubic-kernel residual identities

The proper cubic group has 24 elements and acts transitively on the six
axis vectors. Its average of a point mass is uniform. A cubic-covariant
kernel has weights `(a,b,c)` for same, opposite and orthogonal directions,
with `a+b+4c=1`. Multiplication gives

```text
(K^2)_same = a^2+b^2+4c^2,
(K^2)_opposite = 2ab+4c^2,
(K^2)_orthogonal = 2ac+2bc+2c^2,
(K^2)_same-(K^2)_opposite = (a-b)^2.
```

At `a=b=1/2-2c`, the residual from uniformity is
`2a^2+4c^2-1/6=(6c-1)^2/3`. These are exact polynomial identities.
The uniform kernel gives zero residual. The runner also enumerates the
finite denominator-at-most-eight sample; that enumeration has only its
stated finite domain and grants no general search certificate.

## Sphere moment and atomic identities

For `t=p·q`, normalized area measure has zonal coordinate law `dt/2`.
In the nonnegative normalized density family
`g(t)=1+beta*t+gamma*P_2(t)`, `P_2(t)=(3t^2-1)/2`, integration gives

```text
integral g(t) dt/2 = 1,
integral t*g(t) dt/2 = beta/3,
integral P_2(t)*g(t) dt/2 = gamma/5.
```

The runner integrates polynomial coefficients exactly with rational
arithmetic. It checks these finite moments, not an infinite harmonic
classification. For the equator kernel, after one equatorial step the
second direction lies on a great circle through `p`. Its projection is
`cos(phi)` for uniform angle, hence the two-step second moment is `1/2`;
area measure gives `1/3`. The runner integrates a Laurent polynomial in
`exp(i*phi)` by extracting its constant coefficient.

For the atomic kernel `a*delta_p+(1-a)*delta_-p`, composition gives masses
`a^2+(1-a)^2` at `p` and `2a(1-a)` at `-p`. The rational runner checks
this composition; it does not claim to sample every sphere measure.

## Star identity and delayed-variation witness

Suppose `K_1=mu_0` and take the origin with any `m` of its six neighbours.
These leaves are mutually nonadjacent. In center-first order the joint is
`mu_0^{m+1}`. In leaves-first order it is
`mu_0^m(d leaves) K_m(d center|leaves)`. Equality implies
`K_m=mu_0` for `mu_0^m`-almost every leaf tuple. On a finite full-support
menu this is pointwise; on a continuous menu it is only almost everywhere.

A concrete binary witness sets `K_0,K_1,K_2` to the fair law and lets
`K_3` copy the majority of its three recorded leaves. All orders on the
isolated three-site path then give the uniform product law. On the
three-leaf star, center-first is uniform while leaves-first puts zero
weight on a center opposite to the leaves' majority. The runner enumerates
these joint laws. Variation at three neighbours thus need not be visible
on a three-site path.

For a continuous scope boundary, set `K_0`, `K_1` and every `K_m` with `m >= 3` to area measure, and change
`K_2` only when its two inputs coincide, assigning their common direction
there. This is a covariant pointwise variation on a product-null set.
It does not change any finite sequential law from the product law: by
induction every reached neighbour tuple has the product law, and a finite
union of coincidence events has probability zero. This measure argument
is analytic, not a numerical execution on an atomless space.

## Radial-square witness and deferred original claims

Let `P` be the three-by-three matrix with all entries `1/3`,
`u=(1,-1,0)^T`, `v=(1,1,-2)^T`, and `K=P+uv^T/12`.
Every entry is positive and rows sum to one. Yet `K` is nonconstant and
`K^2=P`: `Pu=0`, `v^T P=0`, and `v^T u=0`. The runner checks all entries
exactly. This refutes the original extension from special menus to arbitrary
mixed-state radial kernels. Endpoint matching still does not prove full
order independence; two-site matching also requires detailed balance,
which this kernel fails.

The original universal variation-exclusion submission is not certified here.
Its all-window, pointwise continuous, mixed-radius and axiom-derived claims
are withdrawn or narrowed as above. The general negative packet lacks five
qualifying independent exact-target attack families; out-of-domain alternatives
and surviving counterexamples are not counted as failed attacks. Original
proof arguments and history remain preserved at PR8137 head
`d15d5d9074e343563700691afcfddb5afc761a21`; this note retains the valid
positive identities and witnesses without granting a general exclusion result.
The original branch remains a recovery handle for unlanded certification.

## Verification

```bash
python3 scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py
```

Independent review supplies separate exact controls. The cached primary output
records its actual finite scope; infinite domains and physical-lattice dynamics
are not executed. Formal scientific audit is separate and remains pending.
