# Shapiro Static Discriminator

**Date:** 2026-04-06; exact-boundary repair 2026-07-11

**Type:** no_go

**Claim type:** no_go

**Status:** exact negative boundary on the supplied snapshot-only harness;
independent audit required before any effective status change

**Primary runner:**
[`scripts/shapiro_static_discriminator.py`](../scripts/shapiro_static_discriminator.py)

**Cached runner output:**
[`logs/runner-cache/shapiro_static_discriminator.txt`](../logs/runner-cache/shapiro_static_discriminator.txt)

## Question

Can the detector-line overlap phase in this runner identify whether its input
array was produced by causal propagation rather than supplied as an equal
position-only array?

## Minimal Premises And Forbidden Imports

For each run, fix the configured instance

```text
X = (V, positions, adjacency, source nodes, detector nodes,
     BETA, K, H, baseline field and all other non-field constants).
```

The runner then supplies only:

1. the fixed configured instance `X`;
2. one real scalar field value `F(v)` at each node;
3. a deterministic amplitude map `P_X(F)` from that array to detector
   amplitudes; and
4. the normalized detector-overlap phase relative to a fixed baseline field.

There is no time variable, source history, source turn-on event, detector
clock, probe speed, retarded field equation, or temporal boundary condition.
Those objects are forbidden as hidden proof inputs. The parameter called `c`
in the old runner changes only a position-dependent cone mask; on this surface
it is a cone-shape index, not an independently computed physical propagation
speed.

## Exact Input-Interface/History-Label Theorem

Let `V` be the node set of a fixed configured instance `X` and let

```text
P_X : R^V -> C^D
```

be the deterministic amplitude map implemented by `_propagate`, restricted to
the detector nodes `D`. For a fixed baseline `F_0`, define

```text
Phi_X(F; F_0) = Arg < P_X(F_0)/||P_X(F_0)||,
                        P_X(F)/||P_X(F)|| > .
```

Suppose a history label or proposed mechanism `M` supplies a node-wise
snapshot `F_M(q)` for parameter value `q`. The runner's field-input class is
the unconstrained array space `R^V`: it imposes no static field equation,
source law, boundary data, or physical admissibility condition. Define the
equal-array, position-only witness

```text
W_q(v) := F_M(q)(v)  for every v in V.
```

Then, exactly,

```text
P_X(W_q) = P_X(F_M(q))
```

and therefore

```text
Phi_X(W_q; F_0) = Phi_X(F_M(q); F_0).
```

### Proof

`W_q` and `F_M(q)` are the same element of `R^V`. A deterministic function has
the same output on equal inputs, so their detector amplitude vectors are
equal. The normalized overlap and its phase are functions of those vectors,
so they are equal as well. This argument applies to every configured graph,
family, seed, parameter value, and field strength for which the normalized
phase is defined. No displayed numerical phase value is used. QED.

## Consequence For This Runner

The old `_causal_field` routine did not evolve a field. It returned a
position-only cone-masked array, algebraically identical to the old
`_static_cone_field` array for the same cone index. The repaired runner names
that object `_cone_snapshot_field` and constructs its equal-array witness by
copying the node values. It checks zero maximum node difference on every one
of the 24 configured family/seed/cone rows.

The exact conclusion is therefore an input-interface/history-label
nonidentifiability no-go:

> In this snapshot-only harness, detector-line phase cannot distinguish a
> history label that is absent from the interface from an equal node-array
> input.

This is stronger than observing equal rounded curves, but narrower than a
claim about a genuine retarded-field experiment. The equal-array witness is
not an independently generated physical static solution. The result says the
present interface discards history before propagation begins; it does not say
that a physical static field equation admits the witness or that every
history-sensitive observable can be duplicated.

## Bounded Fixed-Layer Scheduling Control

The runner also completes a separate finite control. Its scheduling proxy is
not time evolution. For `d=0` the cone field is uncut. For `d>=1`, the source
layer and the next `d-1` downstream layers are set to zero, with
`d in {0, 1, 2, 3}` and cone index `1.0`.

Measured means on the configured three families and two seeds are:

| Mode | q=2.0 | q=1.0 | q=0.5 | q=0.25 |
|---|---:|---:|---:|---:|
| cone snapshot | +0.0372 | +0.0446 | +0.0569 | +0.0662 |
| equal-array position-only witness | +0.0372 | +0.0446 | +0.0569 | +0.0662 |

| Fixed-layer proxy | d=0 | d=1 | d=2 | d=3 |
|---|---:|---:|---:|---:|
| configured mean | +0.0446 | +0.0445 | +0.0446 | +0.0450 |

The completed runner asserts:

- self-overlap phase below `1e-15 rad` for all six configured baseline
  detector states;
- zero node-wise difference between every cone snapshot and its equal-array
  witness;
- exact curve reuse implied by the theorem;
- scheduling-proxy span below the declared operational near-flat tolerance
  `1e-3 rad` on these four rows; and
- cone-snapshot span minus scheduling-proxy span above `2e-2 rad`.

The completed values are a cone-snapshot span of `0.028991 rad`, a fixed-layer
span of `0.000446 rad`, and a span gap of `0.028544 rad`. The span comparison
does not identify cone indices with delay values and is invariant under row
permutation. Thus the fixed-layer proxy is near-flat and cannot reproduce the
cone curve's variation on the declared finite grid. This is not a theorem
about every static schedule, delay, field shape, or time-dependent source.

## No-Go Discipline Gate

- **N1 — alternative routes (PASS).** Seven distinct attacks on the exact
  theorem were tested by source inspection or explicit boundary case:
  hidden history-label input, direct `q` leakage, nondeterministic/stateful
  propagation, unequal fixed instances or baselines, zero-norm undefined
  phase, restriction to physically admissible static solutions, and one
  equal-array witness fixed across all `q`. The first four are absent from the
  runner interface, the theorem excludes undefined phase, and the last two
  change the comparator class or quantifier and therefore remain live outside
  the narrow result.
- **N2 — wall independence (PASS).** The exact theorem has no residual walls.
  Time evolution and history-sensitive readout are possible extensions, not
  premises silently counted as independent walls.
- **N3 — hidden-wall scan (PASS).** The proof uses one fixed configured
  instance, equality in the explicitly unconstrained input space `R^V`, and
  determinism only. Physical static-solution admissibility is not assumed.
  Family parameters, numeric curves, physical units, and a causal
  interpretation of `c` are non-load-bearing or explicitly excluded.
- **N4 — residual matching (PASS).** The exact witness attacks only the
  quoted missing residual: whether this runner's detector phase identifies
  causal propagation. The scheduling computation supports only its own four
  configured rows and is not counted as a witness for the exact theorem.
- **N5 — rhetoric (PASS).** Equality is established at unconstrained
  node-array, detector-vector, and single detector-phase resolutions. It is
  not established for physically admissible static solutions, multi-time or
  path-history data, one-field-across-`q` tests, or other interfaces. Adding
  more detector components at the same snapshot does not evade the theorem;
  only independently history-carrying data can do so.
- **N6 — partial-closure paths (PASS).** Adding a temporal state, source
  protocol, and history-sensitive readout is a live constructive path around
  the no-go. It changes the theorem's premise rather than refuting the present
  snapshot-factorization result.
- **N7 — steelman (PASS after narrowing).** A hostile reviewer can object that
  an equal-array witness need not solve any physically admissible static field
  equation, one physically fixed field may not reproduce the whole indexed
  curve, and a retarded field sampled along a probe trajectory need not reduce
  to one node array. Those objections defeat a physical causal-vs-static
  claim, so none is made. They do not defeat the exact input-interface result,
  which is now stated only on the runner's unconstrained `R^V` input class.
- **N8 — cross-cycle echo (PASS).** Earlier Shapiro repairs repeatedly found
  the same static-cone mimic and excluded a physical field-speed claim. No
  later source introduced temporal evolution into this runner. The known
  retirement mechanism is exactly the queued temporal/history-sensitive
  extension, not a reinterpretation of the existing cone mask.

## Claim Firewalls

This note does **not** claim:

- that the cone snapshot is a causal or retarded solution;
- that a physical Shapiro delay has been derived;
- that the equal-array witness is an independently admissible physical static
  solution;
- that a single position-only field matches every parameter value;
- that all static scheduling families are near-flat;
- that multi-time, edge-time, or history-sensitive observables obey the no-go;
- a lab calibration or physical field-speed measurement; or
- an audit verdict.

The independent audit lane alone may ratify an effective status for this
`no_go` source claim.
