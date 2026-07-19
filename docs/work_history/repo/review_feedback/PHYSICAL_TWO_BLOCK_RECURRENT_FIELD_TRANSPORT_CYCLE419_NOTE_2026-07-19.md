# Physical two-block recurrent field transport — Cycle 419

Date: 2026-07-19

Authority: none

Audit: unset

Constitutional effect: none. No axiom, foundation, Qualification, primitive,
registry, policy, queue, or audit-status surface is changed or proposed.

Companion runner:

```text
scripts/physical_two_block_recurrent_field_transport_cycle419_2026_07_19.py
```

## Result up front

Cycle 419 constructs **two neighboring seven-M2 field blocks**. Each block
contains one local source-reservoir M2 and six directional field M2. The
inherited Cycle-417 retarded source port is transferred into block A by a
coherent ownership move through one blank boundary rail. No source-port or
mediator expectation is queried. One fixed coin–exchange–directed-SWAP update
then advances the field, and the adjoint gives the exact inverse.

The construction gives a positive one-edge retarded finite-cone history. For
every Cycle-399 source route, both orientations, L5, and blind held L6, the
actual coherent Cycle-417 port produces the expected field occupation on the
neighboring block. The update uses no expectation feedback and calls no
separate numerical field solver.

The construction and update are tested in all 24 proper-cubic frames. The
excitation ledger is not physical energy, work, stress, or a selected source.

**Global-ledger boundary:** the upstream Cycle-417 CNOT fanout is not number
conserving. On its mediator-one branch it maps mediator-plus-port Hamming
number `1 -> 3` by retaining the mediator and setting both blank port bits.
Cycle 419 moves the retarded copied label into block A without another number
increase, but this does not undo the upstream duplication. Therefore Cycle
419 does not close global mediator-plus-port-plus-field source/resource
balance. Its exact reservoir/field excitation ledger begins only after
ownership, on the declared Cycle-419 block code.

The same injected orbit does not become a stationary ray or a fixed
reservoir/field occupation profile in the frozen 64-update probe. This is a
**route-specific stationary failure**, not a general result about reversible
fields. The runner does not construct a resolvent and does not supply an
eigenstate as initial data. Because the one-step ray residual of an orbit of
one fixed unitary is invariant, a stationary eigenstate is not generated later
from this non-eigenstate port preparation. A separately selected/prepared
dressed eigenstate, a larger recurrent-return geometry, or another lawful
update remains live.

This is a bounded physical source-port and propagation seam. It is **not a
field-receiver compiler** for the Cycle-213/216 arrays. It does not derive a
cubic point profile, field sign or normalization, a static Green response,
physical energy, stress, source selection, time, metric, gravity, a Record, or
a Born law.

## Physical code and ownership

The two blocks use 14 new M2 factors:

```text
block A:  reservoir A + six directional field rails A_d;
block B:  reservoir B + six directional field rails B_d.
```

Block A's and block B's centers are separated by three physical-M2 edges.
Their `+x` and `-x` boundary rails are adjacent, so the interblock directed
transport is one two-M2 SWAP. Each block is a seven-site star. The inherited
Cycle-417 retarded port is two edges from reservoir A through the initially
blank `-y` boundary rail.

The coherent ownership move is

```text
SWAP(retarded port, blank A_-y);
SWAP(A_-y, reservoir A).
```

It sends `|port=p, A_-y=0, reservoir=0>` to
`|0,0,p>` for both `p=0,1`. Reversing the SWAP order releases the source bit
exactly. Thus the operation moves the correlated Cycle-417 control; it does
not create a third copy and does not increase a claimed resource number.
The Cycle-417 static port remains a correlated spectator in this route.
The ownership permutation commutes with port-plus-rail-plus-reservoir Hamming
number with residual zero. This local conservation must not be extrapolated
backward across Cycle 417's non-number-conserving CNOT fanout.

The executed propagation block is the vacuum plus total-one-excitation code,
of dimension `1 + 2(1+6) = 15`. This prepared sector is an explicit scope
condition, not a full-field Fock compiler.

## Same fixed recurrent update

Let `|r_x>` be the reservoir excitation of block `x` and

```text
|s_x> = (1/sqrt(6)) sum_d |f_(x,d)>
```

be its scalar one-field state. With the Cycle-416/Cycle-295 angle

```text
theta = 0.8 * Cycle-219 vacuum-relative mass charge,
```

the local reservoir/field gate is

```text
V_x |r_x> = cos(theta)|r_x> - i sin(theta)|s_x>;
V_x |s_x> = -i sin(theta)|r_x> + cos(theta)|s_x>,
```

and is identity on transverse one-field directions and on the vacuum. The
same Cycle-214 field coin acts on the six rails of both blocks. For oriented
edge `d=+x`, `S_d` swaps `A_d` with `B_reverse(d)` and fixes every other mode.
The time-homogeneous update is

```text
G_d = S_d (V_A direct-sum V_B) (C_A direct-sum C_B).
```

The inverse is the reverse adjoint schedule. Reservoir-plus-field excitation
is exactly conserved. For block A, its charge change equals the explicit
incoming-minus-outgoing boundary projector after the local layers. This is an
excitation continuity coordinate, not energy or work.

Cold operator residuals are:

| control | residual |
|---|---:|
| update unitarity / inverse | `1.9427911635093735e-15` |
| total-excitation commutator | `0.0` |
| block-A continuity identity | `1.447753279559963e-15` |
| maximum 24-frame intertwiner | `6.181460191301304e-16` |
| 576 frame group-law failures | `0` |

## Proper-cubic covariance

Reservoirs and vacuum use the supplied scalar representation. The six field
rails use the Cycle-210 direction permutation. A proper-cubic frame sends
edge direction `d` to `R d`, including `reverse(d)` to `reverse(R d)`. The
runner checks

```text
U_R G_d U_R^dagger = G_(R d)
```

for all 24 frames, plus all 576 representation group products. Rotating the
physical coordinates preserves both seven-site stars, both ownership SWAP
edges, and the directed boundary SWAP. These are spatial frame controls, not
physical time.

## Coherent held retarded history

For each Cycle-399 route, L5/blind held L6, and origins A/C, the runner
executes the actual chain

```text
strict response
  -> Cycle-416 source/mediator balance
  -> Cycle-417 coherent retarded port
  -> Cycle-419 ownership move
  -> G_(+x).
```

No squared-norm expectation is used to prepare or control a gate. It is read
only afterward as a diagnostic. If the inherited coherent port weight is
`p_port`, the one-update neighboring field weight is derived as

```text
p_neighbor = p_port sin^2(theta) / 6.
```

This is a coherent sector squared norm, not a Born probability or occurrence
frequency. Deleting the local exchange leaves all field rails blank. Deleting
the directed SWAP leaves block B blank while block A retains its locally
emitted field. Applying the adjoint and reversing the ownership move restores
the complete Cycle-417 injection state.

The held neighboring weights are `1.574092565133932e-08` for the unit-weight
route and `7.937657671749998e-08` for the coefficient-two route, with the
opposite-origin differences at floating-point roundoff. The maximum full
ownership/update/release inverse residual is `4.880424200754915e-19`. Vertex
deletion residual is zero; transport deletion leaves neighboring weight zero.

## Explicit stationary-origin audit

The static probe starts from the same owned port state `psi_0=|r_A>` and only
iterates `G_d`. It neither diagonalizes `G_d` nor inverts a static operator.
For

```text
psi_t = G_d^t psi_0,
epsilon_ray(t)^2
  = 2 - 2 |<psi_t, G_d psi_t>|,
```

unitarity gives

```text
<psi_t, G_d psi_t> = <psi_0, G_d psi_0>.
```

The nonzero initial ray residual is therefore invariant along this orbit. The
runner also measures nonzero changes in the four-component occupation profile

```text
(reservoir A, field A, reservoir B, field B)
```

over frozen training updates 1–32 and held updates 33–64. Consequently no
stationary object is generated as an eigenstate or resolvent of the same
recurrent update in this route. Any eigenstate used as a static object would
have to be separately selected and prepared; an externally solved resolvent
would likewise be an import. Neither is silently supplied here.

This result does not say that the update lacks eigenstates, that a larger
field cannot form a stationary dressed state, or that a static response is
impossible. It only rejects promotion of this injected two-block transient to
an autonomously generated static response.

The cold same-update values are:

| stationary-origin control | value |
|---|---:|
| invariant one-step ray residual | `0.36073931889110306` |
| maximum residual drift, updates 1–64 | `9.81992265280951e-14` |
| minimum profile change, training 1–32 | `0.03875151804295808` |
| minimum profile change, held 33–64 | `0.0160963342713103` |
| norm residual at update 64 | `1.9095836023552692e-14` |

No stationary initial state is supplied, no eigensolver selects one, and no
resolvent is computed or injected.

## Supplied, derived, and open inventory

Supplied:

1. the Cycle-399/403 strict response and Cycle-416 balance;
2. the Cycle-417 blank-port preparation, non-number-conserving CNOT fanout,
   and retarded label;
3. two seven-M2 star blocks, a blank ownership rail, and a blank block-B
   reservoir;
4. the Cycle-214 field coin, the Cycle-295 local exchange form, the mass-based
   angle, gate order, and chosen `+x` edge;
5. the vacuum/total-one-excitation sector, finite two-block boundary, spatial
   frame action, L5/L6 cases, tolerances, and diagnostic readout.

Derived:

1. bounded coherent port-to-reservoir ownership and release;
2. unitary number-preserving local exchange and directed one-edge transport;
3. exact inverse and blockwise excitation continuity;
4. all-24-frame edge covariance and group action;
5. exact L5/blind-held-L6 branchwise neighboring arrival, deletion visibility,
   and absence of expectation feedback;
6. nonstationarity of the declared injected orbit under the frozen same-update
   probe.

Open:

1. a complete cubic field lattice and physical-M2 Cycle-213/216 update/solve;
2. endogenous selection and preparation of a stationary dressed eigenstate or
   static Green profile;
3. recurrent return and reabsorption in a larger geometry;
4. carried matter/source motion, FSWAP-correct multiparticle transport, recoil,
   contact work, recurrence, coupling, and calibration;
5. one global mediator-plus-ports-plus-field resource balance across the
   Cycle-417 fanout and Cycle-419 propagation;
6. physical energy/stress/source identification, Records, clock, metric,
   gravity, probability, and realized-history law.

The source-port and block layout, field coin, coupling, boundary, and initial
sector are supplied structure. The copied Cycle-417 ports are not independent
confirmations. No actual Record is formed.

## Ledger effect and disposition

- `C_ref`: unchanged; phase, coupling, and source normalization remain
  supplied.
- `C_num`: after ownership, one prepared field-block excitation sector has an
  exact local/transported ledger; the upstream Cycle-417 fanout is not number
  conserving, so no global source/resource ledger is closed.
- `C_wrap`: unchanged; iteration count is not physical time.
- `C_int`: local reversible reservoir/field exchange and transport now share
  one update; contact, recoil, and carried-source composition remain open.
- `C_local`: a coherent Cycle-417 port reaches a neighboring physical field
  block through bounded gates with inverse, frames, deletion, and held controls.
- `C_source`: the expectation-to-port seam remains physical and gains one
  retarded propagation step; source meaning, static response, tensor/metric
  action, and gravity remain open.

Science disposition: the bounded retarded construction is certified on its
declared code. The stationary audit is a route-specific discriminator
identifying the missing eigenstate/return-law surface. There is no shared
obstruction, no broad no-go, and no axiom pressure.

## Reproduction

```bash
python3 -u \
  scripts/physical_two_block_recurrent_field_transport_cycle419_2026_07_19.py
```

Expected cold result: all checks pass and

```text
RESULT PHYSICAL_TWO_BLOCK_RECURRENT_FIELD_TRANSPORT_CERTIFIED
```
