# Seven-Star Bilinear Carrier Exact Support and Homogeneous-Normalization No-Go

**Date:** 2026-07-11
**Claim type:** no_go
**Status:** exact support plus a narrow algebraic normalization no-go
**Status authority:** independent audit lane only
**Primary runner:**
[`scripts/frontier_s3_time_bilinear_tensor_primitive.py`](../scripts/frontier_s3_time_bilinear_tensor_primitive.py)
**Paired cache:**
[`logs/runner-cache/frontier_s3_time_bilinear_tensor_primitive.txt`](../logs/runner-cache/frontier_s3_time_bilinear_tensor_primitive.txt)

## Claim boundary

This note replaces the former definition-only row with two exact results:

1. a proper-cubic representation theorem for the seven-site star, including
   an oriented-axis bright-pair lemma and an equivariant center-excess
   decoupling lemma; and
2. a narrow normalization no-go inside the explicitly assumed family
   `O_lambda = lambda K_R`.

The second result says only:

> Rank, determinant, proper-cubic covariance, bright/dark support, and
> center-excess decoupling are homogeneous properties.  Within the family
> `O_lambda = lambda K_R`, they do not select `lambda=1`.

The physical ray identification `O proportional to K_R` is an assumption of
that family, not a conclusion.  This note does not prove that `K_R` is a
physical tensor observable and does not rule out a future source/action,
response, or readout theorem that fixes the ray and its normalization.

## Accepted-premise firewall

The full accepted-premise surface checked for possible normalization supply is:

- the [Lattice, Qubit, Admissibility, and Record axioms](MINIMAL_AXIOMS_2026-06-29.md);
- the [scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md);
- the [kinetic-isotropy primitive](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md);
- the [realized-state primitive](REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md);
- the sole [owner-governed residual premise](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md), whose scope is the current `AC_phi_lambda` occupancy and `R-eta` license only.  Its current adoption boundary is recorded in the non-graph context file `TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`.

The live Tier-A registry `docs/audit/data/tier_a_admissions.json` has zero
genuine admitted derivation targets.  The runner checks all entries of the
axiom/primitive registry, the owner-governed registry, and that zero-live-target
condition.  The owner-governed residual does not supply a tensor carrier,
source/action map, or carrier normalization.

No measured value, fitted endpoint, literature constant, state-selection rule,
tensor readout, source/action map, GR identification, or new framework
primitive is imported.  For the normalization theorem, the coordinate
functions and the carrier ray are granted explicitly; the proof does not use
their current upstream audit status.

## Exact seven-star representation theorem

Let the real star module have ordered basis

```text
(center, +x, -x, +y, -y, +z, -z).
```

Proper cubic rotations permute the six arms and fix the center.  The exact
orthogonal decomposition is

```text
R^7 = A1_center direct_sum A1_shell direct_sum E direct_sum T1.
```

An orthonormal adapted basis is

```text
e0 = center,
s  = (+x + -x + +y + -y + +z + -z)/sqrt(6),

e1 = (+x + -x - +y - -y)/2,
e2 = (+x + -x + +y + -y - 2(+z) - 2(-z))/sqrt(12),

T1x = (+x - -x)/sqrt(2),
T1y = (+y - -y)/sqrt(2),
T1z = (+z - -z)/sqrt(2).
```

The runner enumerates all 24 signed-permutation rotations, checks group
closure, and verifies the three isotypic projectors exactly.

### Supplied-axis fixed-pair lemma

Relative to a supplied oriented lattice axis `+x`, average the four proper
rotations fixing that directed axis.  The fixed subspace has dimension four.
Removing the two scalar directions leaves exactly

```text
B_x = span(E_x, T1x),

E_x = (sqrt(3) e1 + e2)/2.
```

Its orthogonal complement in `E direct_sum T1` is

```text
D_x = span(E_perp, T1y, T1z),

E_perp = (-e1 + sqrt(3) e2)/2.
```

Thus `u_E(q)=<E_x,q>` and `u_T(q)=<T1x,q>` are exact coordinates of the
non-scalar fixed pair after an oriented axis is supplied.  The axis is not
derived or privileged: choosing `y` or `z` rotates the component display.
This lemma does not select a physical readout context.

### Equivariant center-excess decoupling lemma

Let `G` be any linear star operator commuting with every proper cubic
rotation.  Define

```text
ell = center^* - (1/6) sum_arm arm^*,
Q(q) = sum_site q_site,
delta_G(q) = ell(Gq)/Q(q),  Q(q) != 0.
```

Both `ell` and `Q` are invariant covectors.  Every vector in `E direct_sum T1`
has zero group average.  Therefore, for `v` in that subspace,

```text
ell(Gv)=0,
Q(v)=0,
delta_G(q+v)=delta_G(q).
```

The runner independently computes that the full commutant has dimension six,
constructs its symbolic general element, and verifies annihilation of
`E_x,T1x,E_perp,T1y,T1z` identically.

This is a family theorem for any equivariant `G`.  It does not select the
historical numerical support Green map or a boundary condition from the
framework axioms.

## Conditional algebraic carrier core

Given real coordinate functions `delta,u_E,u_T`, define

```text
K_R(q) = [1, delta(q)]^T [u_E(q), u_T(q)]

       = [[u_E(q),          u_T(q)],
          [delta(q) u_E(q), delta(q) u_T(q)]].
```

This factorization and `det K_R=0` are exact polynomial identities.  They do
not derive the scalar feature list `[1,delta]`, prove its uniqueness, select
the concrete historical `delta_A1`, or identify the matrix with a physical
tensor.

## Homogeneous-normalization no-go theorem

Assume, as a separate premise, that a candidate carrier lies on the ray of the
algebraic matrix above:

```text
O_lambda(q) = lambda K_R(q),  lambda != 0.
```

Consider the following properties:

1. proper-cubic covariance of the `E` and `T1` coordinate channels;
2. rank at most one and zero determinant;
3. vanishing when both bright coordinates vanish;
4. the exact bright/dark decomposition above; and
5. center-excess decoupling for an equivariant `G`.

Every property is homogeneous under multiplication by nonzero `lambda`.
Moreover, the displayed star point

```text
q_* = e0 + E_x
```

is an exact nonzero witness: `Q(q_*)=1`, `u_E(q_*)=1`, and `u_T(q_*)=0`.
For any finite `delta(q_*)`, the `(1,1)` entry of `K_R(q_*)` equals one, so
`K_R(q_*)` and `2K_R(q_*)` differ.

Therefore the enumerated homogeneous properties do not select `lambda=1`
inside the assumed family `O_lambda=lambda K_R`.

The theorem is algebraic.  `O_lambda` is not claimed to be a framework model,
a Record readout, a source-response tensor, or a physical observable.  The
theorem does not establish non-entailment of the ray identification itself.

## Independent walls and exact movement

The former physical-carrier gap separates into two logically independent
questions:

| Wall | Question | Current result |
|---|---|---|
| W1: semantic/ray identification | Why is the physical/source-response carrier proportional to this `K_R`, including its relative `E:T1` channel normalization? | open; assumed by the normalization theorem |
| W2: overall normalization | Given `O proportional to K_R`, what fixes the common scale `lambda`? | the homogeneous algebra cannot fix it; exact no-go above |

Closing W1 does not close W2, and fixing W2 does not identify the ray.  The
runner's commuting family `c_E P_E+c_T P_T1` shows why relative-channel choice
belongs inside W1 rather than following from cubic covariance.  A sufficiently
strong response theorem may supply both walls simultaneously, but that
possibility does not make them logically dependent.

The exact claim-state movement is W2 route pruning plus exact support for the
star decomposition.  W1 remains the Nature-grade physical blocker.

## Superseded-surface compatibility record

Several downstream boundary runners quote the old row verbatim.  The quoted
boundary remains true: the line

`K_R(q) := [[u_E(q), u_T(q)], [delta_A1(q) u_E(q), delta_A1(q) u_T(q)]]`

is, by itself, a **class-A definition only** and **not** a positive theorem.
It does **not** derive a physical tensor primitive.  In particular, it does
**not** prove that this symbol is a physical tensor primitive in the
GR-readout chain.

For the pinned downstream boundary in one line: this definition does **not** prove that this symbol is a physical tensor primitive.

The former note described **three upstream gaps**.  Its third item was:

> A bridge theorem identifying the bilinear carrier `K_R(q)` with any
> physical tensor primitive in the GR-readout chain.

That item is the third upstream gap and is **not** closed by the readout.
The old bounded coefficients were fixed by the two endpoint
values measured from the old `eta_floor_tf` pipeline and remain
**endpoint-fitted, not first-principles**; they are not used here.

For compatibility with downstream scope guards, the superseded premise shape
was “named admitted-context inputs `(delta_A1, u_E, u_T)` and a
runner-verified algebraic identity.”  The exact lemmas above give the
`identification u_E ↔ <E_x, ·>`, `u_T ↔ <T1x, ·>` from a canonical
oriented-axis fixed subspace once that axis is supplied.  Even when
`(delta_A1, u_E, u_T)` and the decoupling fact are accepted, the definition
does not supply W1 or W2.

The equivalent vector definition remains

`K_R(q) := (u_E(q), u_T(q), delta_A1(q) u_E(q), delta_A1(q) u_T(q))`.

## No-Go Discipline Gate

The gate applies only to W2 and the family `O_lambda=lambda K_R`.

### N1 — Alternative-route enumeration

| Route | Marker | Authority / artifact | Result for selecting `lambda=1` |
|---|---|---|---|
| Proper-cubic covariance | ATTEMPTED | Lattice axiom plus exact 24-element runner | all `lambda K_R` transform identically |
| Rank/determinant/support algebra | ATTEMPTED | self-contained symbolic runner | all nonzero scales preserve the identities |
| Record scalar additivity | ATTEMPTED | linked minimal-axiom source | constrains an already specified finite scalar readout, not this tensor scale |
| Scale-reference route | ATTEMPTED | linked scale-reference primitive | supplies units only and no dimensionless normalization |
| Kinetic-isotropy route | ATTEMPTED | linked kinetic-isotropy primitive | supplies `c_t=c_s`, not carrier response normalization |
| Realized-state route | ATTEMPTED | linked realized-state primitive | evaluates an already-defined law but does not define or normalize it |
| Owner-governed residual route | ATTEMPTED | linked stable premise ID and checked adoption boundary | supplies only the scoped `AC_phi_lambda` occupancy/`R-eta` license |

### N2 — Wall-independence audit

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| W1 semantic ray (including relative E:T1 scale) / W2 common overall scale | no | no | yes |

The no-go assumes W1 and tests only W2.

### N3 — Hidden-wall scan

- “Supplied axis” is an explicit display premise for the fixed-pair lemma.
- “Canonical” refers only to the group-average fixed subspace after that axis
  is supplied.
- `G` is quantified over equivariant maps; the concrete historical Green map
  is not assumed derived.
- `O_lambda=lambda K_R` is the explicit family premise, not a physical claim.
- `q_*=e0+E_x` is constructed in the displayed seven-star vector space and
  checked exactly by the runner.

No physical tensor type, source/action response, endpoint value, background
state, or standard-QFT rule is hidden in the proof.

### N4 — Residual matching

No prior no-go is used as a witness.  The older scalar-Hessian route concerns
the absence of a tensor source, and the carrier-orbit cycle concerns
`E/T`-distinguishing operators.  Both are different from W2 and are not
dependencies of this theorem.

### N5 — Rhetoric audit

The tested resolution is the explicitly defined finite-dimensional carrier
family.  No per-site, per-mode, lattice-wide physical-observable, or all-future
theory impossibility is asserted.  The physical ray identification remains
open.

### N6 — Partial-closure path scan

| Candidate path | Current audit-ledger status (context only) | What it could close |
|---|---|---|
| `S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md` | `unaudited` bounded-theorem source | an imported/convention-backed endpoint normalization, not W1 |
| `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | `unaudited` positive-theorem source | a chosen restricted readout map if its uniqueness premises are supplied |
| future tensor source/action response theorem | absent | W1 and potentially W2 if the response normalization is derived |
| approved primitive or owner-governed premise | current registries checked | none currently supplies this tensor normalization |

A convention or admitted response law is a legitimate bounded path, not a new
axiom.  The no-go rules out only selection by the enumerated homogeneous
properties.

### N7 — Steelman

The strongest objection is that a physical source-response theorem could
identify the ray and impose a nonhomogeneous unit-response condition at one
endpoint, immediately fixing `lambda=1`.  That is convincing as the next
positive route.  It does not refute this theorem because the new unit-response
condition is not one of the homogeneous properties being tested.  The theorem
therefore keeps W1 and all nonhomogeneous normalization routes open.

### N8 — Cross-cycle echo

| Similar surface | Current audit-ledger status (context only) | Mechanism / lesson |
|---|---|---|
| `QUARK_RPSR_SINGLE_SCALAR_READOUT_UNDERDETERMINATION_NOTE_2026-04-28.md` | `unaudited` no-go source | explicit readout families separate algebraic input from value selection; not retired here |
| `OBSERVABLE_PRINCIPLE_RECORD_SCALAR_MAP_NO_GO_NOTE_2026-06-05.md` | `unaudited` no-go source | Record fixes additive form only after a scalar map is supplied; not retired here |
| `OBSERVABLE_PRINCIPLE_T1D_DETERMINANT_READOUT_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md` | `unaudited` no-go source | two compatible readout interpretations expose selection freedom; not retired here |
| `S3_TIME_READOUT_PRIMITIVE_BRIDGE_ASSESSMENT_BOUNDED_NOTE_2026-06-12.md` | `unaudited` bounded-theorem source | an explicit convention-backed partial-closure route exists and is preserved above |

The scale, kinetic-isotropy, realized-state, and owner-governed registries were
also checked because other walls can be retired by accepted premises.  None
fixes the present dimensionless carrier normalization.

**Gate result:** PASS for the narrow homogeneous-normalization no-go only.

## What this does not claim

- It does not derive the historical numerical support Green map.
- It does not prove uniqueness or physical necessity of `[1,delta]`.
- It does not identify `K_R` with a tensor readout, source response, Einstein
  tensor, Regge tensor, metric, curvature, or stress tensor.
- It does not rule out nonhomogeneous or convention-backed normalization.
- It does not promote any downstream quark-mass or GR claim.
- It does not alter any audit verdict or repo-wide authority surface.

## Reproduction

```bash
PYTHONPATH=scripts python3 scripts/frontier_s3_time_bilinear_tensor_primitive.py
```

The runner uses exact symbolic arithmetic and a strict accepted-premise
registry guard.  Independent audit remains required before this `no_go` author
hint can receive any effective retained-grade status.
