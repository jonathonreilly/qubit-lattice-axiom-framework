# Cycle-416 / seven-M2 exact common-code seed — Cycle 418

Date: 2026-07-19
Authority: none
Audit: unset

## Result and scope

Cycle 418 constructs the exact local common-code seed between the Cycle-416 source/mediator balance gate and the existing gate in `local_conjugate_reservoir_source_field_ledger_repair_2026_07_17.py`. In the ordered logical basis `(|source>, |mediator>)`, the encoding is

```text
E |source=1, mediator=0> = |R=1, F=000000>
E |source=0, mediator=1> = -|R=0, s_F>
s_F = (1/sqrt(6)) sum_d |1_d>.
```

At the frozen angle `theta = 0.36272452333990834`, it satisfies

```text
E G_416(r) = G_7(r) E,  r=0,1,
```

together with the adjoint/inverse relation. The minus convention is load-bearing: it maps Cycle 416's `+i` source/mediator rotation to the existing seven-M2 gate's `-i` reservoir/field exchange.

The construction is extended without a global field blockade to one complete M64 matter cell, one reservoir M2, and all 64 hard-core field states: `64 x 2 x 64 = 8192` computational basis states. Every field basis state is lawful and tested, but this `G_7` creation operator couples only the vacuum and uniform one-field state; every higher-occupation field sector is a spectator under this seed. The local gate is also a matter spectator, so the full update is `I_M64 tensor G_7`. This is not a full many-field emission/absorption vertex and is not yet the matter-controlled, carried, streamed recurrent update.

## Exact two-dimensional seed

The Cycle-416 code rotation is

```text
G_416(0) = I,
G_416(1) = cos(theta) I + i sin(theta) X.
```

The reservoir generator exchanges only `|R=1,F=0>` and `|R=0,s_F>`, and the existing gate is

```text
G_7(0) = I,
G_7(1) = exp(-i theta X_exchange).
```

The signed encoding therefore makes both forward columns and both inverse columns agree. It is an isometry; the two-state image is invariant; compression back through `E^dagger` returns `G_416`; and leakage from the code is zero within numerical precision.

The encoded basis carries exactly one reservoir-plus-field excitation. The full seven-M2 gate preserves `Q=R+F`, and its operator number ledger is

```text
G_7^dagger F G_7 - F + G_7^dagger R G_7 - R = 0.
```

From the encoded source state the field transfer is `sin^2(theta)` and the reservoir retention is `cos^2(theta)`. Applying the adjoint restores the source state.

## All-basis spectator lift: M64 x M2 x M64

The sparse operator has dimension 8,192 and admits every hard-core field occupation from zero through six as a lawful input. It is not a repeated zero/one-field comparison. However, all field occupations above one are unchanged spectators: they are tested for unitarity, number conservation, covariance, and inverse behavior, not for multi-field emission or absorption. The runner checks every one of the 8,192 inverse-error columns, the complete matter-plus-reservoir-plus-field number operator, the actual intrinsic contact phase `exp[i g N(N-1)/2]`, matter-block leakage, and the 128-column matter-replicated signed code.

Because the seed gate is identity on matter, it commutes with the complete M64 contact operator and does not mix any of the 64 matter basis blocks. This earns an all-basis spectator extension of the common seed, not a full many-field vertex, matter response, or recoil law.

For covariance, the runner uses the proper-cubic six-direction permutation on the field M2s and its fermionic Fock lift on the M64 matter cell. Both the full 8,192-state gate and the 128-column signed encoding intertwine all 24 proper-cubic frames.

## Deletion and adversarial controls

Coupling deletion (`theta=0`) returns exact identity on the logical and physical blocks and leaves the encoding relation exact. Sign deletion—replacing the required minus seed by a plus seed—produces a visible intertwiner residual. Deleting one direction from the normalized scalar seed also produces a visible intertwiner residual and breaks the scalar-frame content. These are construction controls, not minimum-content or impossibility claims.

## Supplied, derived, and open

Supplied structure:

1. the Cycle-416 strict-response bit and fixed `+i` source/mediator rotation;
2. the Cycle-219 vacuum-relative mass normalization and coupling `0.8` fixing the angle;
3. one prepared source excitation and the signed uniform scalar seed;
4. one reservoir M2, six hard-core field M2, the full 64-state field basis, and the existing `G_7` extension from the named local-repair runner;
5. one M64 matter spectator plus its proper-cubic Fock and contact representations.

Derived here:

1. the exact `r=0,1` common-code intertwiner, compression, zero leakage, and adjoint inverse;
2. the exact source-plus-field number ledger, transfer, coupling deletion, and sign/direction deletion visibility;
3. all-24-frame covariance of the seed and gate;
4. the sparse 8,192-basis spectator lift, with higher field occupations lawful/tested but unchanged.

Still open:

1. wiring the strict-response physical control into this local seed;
2. joining the field coin, stream, intrinsic contact, and carried-reservoir schedule in one recurrent update;
3. a genuine many-field emission/absorption vertex, two-source number-two history, matter recoil, work, and resource interpretation;
4. selection as physical energy, stress, or a gravity source; actual Records, time, and metric response.

The conserved coordinate is excitation number, **not energy, stress, or a gravity source**. The fixed update schedule is not time, and no generator is called a rate. No actual Record is formed. This is a constructive common-code seed with no host expectation query and no global parity or field-occupancy service. There is no negative, minimum-content, shared-obstruction, or axiom-pressure claim.
