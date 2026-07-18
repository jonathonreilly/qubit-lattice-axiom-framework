# Physical Cycle-269 collision-safe auxiliary ports — 2026-07-17

Type: constructive bounded operator-component probe

Status: collision-safe multiparticle catch-up word on a declared local
auxiliary port-code space; state encoding, joint coin routing, and full-Fock
compilation remain open

Authority: none

Audit: unset

Constitutional effect: none

Runner:
`scripts/physical_cycle269_collision_safe_auxiliary_ports_2026_07_17.py`

## Result

The overlapping-swap collision in the preceding physical Cycle-269 catch-up
artifact's catch-up word has a bounded constructive auxiliary-port resolution.
Replace the one cell reservoir by six auxiliary port M2 per coarse cell, one
for every oriented matter half-edge `v=(x,d)`. For each undirected outer edge
`(u,v)`, apply one port swap controlled by the occupation XOR

```text
n_u XOR n_v = (I-B_u B_v)/2.
```

The mapped product `B_u B_v` is phase-zero, pure `Z`, and weight eight on
every tested outer edge. Its conditional swap acts on the two endpoint port
M2s, so the local gate has ten-M2 support. It is an exact unitary,
auxiliary-tag-number-preserving involution.

Each half-edge port belongs to exactly one outer edge. Different catch-up
gates therefore use disjoint auxiliary pairs. Their face supports can overlap,
but all `B_u B_v` controls are diagonal and commute. Consequently the global
catch-up product is algebraically independent of gate enumeration. It needs
no global parity service or preferred edge order. No host-side control is
part of this catch-up operator word. The unassembled joint matter-coin/port
routing update and state preparation remain outside that statement.

This is a bounded operator word on a declared auxiliary constraint space. A
bounded state encoder remains open, and local matter-coin/port routing remains
open. The result is not yet a full-Fock compiler.

## Local auxiliary port constraint

The declared local port constraint is

```text
S_v = B_v Z_port(v) = +1
```

for each matter half-edge. It correlates the port tag occupation with the
mapped matter occupation without reducing the matter content: every tag has
its own local `Z`. The `S_v` commute with the inherited local checks and
Wilsons, and mutually commute. On every tested size the runner verifies that
all `6L^3` constraints are independent, raise both the local-check and
fixed-Wilson ranks by exactly `6L^3`, and leave the constrained code exponent
equal to the inherited matter-code exponent. The runner does not claim a
preparation or enforcement dynamics for this code space; it supplies the local
constraints and tests decoded constraint leakage of the catch-up macrostep.

On a single outer edge, the complete decoded four-bit abstract word is:

1. FSWAP the two matter modes, including the `-1` phase on double occupation;
2. swap their two port tags iff the arrival occupations differ.

On its decoded `S_u=S_v=+1` subspace this simultaneously transports matter and
tag. The decoded word is unitary, its own inverse, commutes with the abstract
constraint-space projector, and has zero constraint leakage. Deleting the
auxiliary catch-up after decoded FSWAP gives unit operator-norm leakage on the
one-carrier fixture. This is not an assembled encoded stream/catch-up matrix;
the physical ten-M2 catch-up gate and decoded four-bit macrostep are separate
tested surfaces.

The ten-M2 matrix has dimension 1024 and zero observed unitarity, involution,
and auxiliary-tag-number commutator residual. The decoded four-bit matrix has
zero observed unitarity, inverse, constraint-commutator, and constraint-leakage
residual; deleting catch-up gives leakage operator norm exactly 1.

The XOR, rather than two independently applied arrival controls, is
load-bearing outside the one-carrier fixture. With both endpoint modes
occupied, the FSWAP phase is retained while the two binary port tags are both
occupied; no second controlled swap cancels a first one.

## Physical support and local-check leakage

The runner builds the actual Cycle-269 code at training `L=3,4,5` and held
`L=6`. For every outer edge it verifies:

- exactly one auxiliary outer edge per port;
- pure-`Z`, phase-zero, weight-eight `B_u B_v` control;
- ten-M2 catch-up support;
- computed nine-M2 inherited outer-FSWAP support and eleven-M2 union support;
- zero commutator leakage against every bounded local check and Wilson;
- `6L^3` independent commuting local port constraints whose rank increment
  exactly cancels the `6L^3` added port qubits;
- zero anticommuting pairs among all XOR controls;
- maximum face-control incidence two; and
- size-independent physical support-conflict degree eight.

For `L=3,4,5,6`, the independent local-constraint ranks are respectively
162, 384, 750, and 1296. The constrained and inherited local code exponents
agree exactly at 164, 386, 752, and 1298, with zero constraint-commutation or
rank-increment failures.

The supplied allocation is

```text
15 Cycle-269 face M2/cell + 6 auxiliary port M2/cell = 21 M2/cell.
```

This is constant overhead. It is larger than the preceding one-reservoir
layout; no minimality claim is made.

## Multiparticle collision and held-size controls

For every body cell at `L=3,4,5,6`, the runner enumerates all 32 even subsets
of its six matter ports. This includes every two-port collision, four-port
collision, and the six-port filled fixture that made several old cell-tag
swaps share a reservoir. It also applies 128 deterministic random total-even
multiparticle fixtures per size.

For each fixture it checks:

- output matter and port tags satisfy every decoded local port constraint;
- ascending, reversed, and shuffled outer-edge enumerations agree;
- applying the macrostep twice restores the tested total-even occupation masks
  and independently chosen total-even tag masks; and
- the inherited FSWAP signs multiply to `+1` under the inverse word.

Held `L=6` is not used to choose the six-port layout, the XOR control, support
bounds, collision set, order tests, or thresholds. The result is an exhaustive
same-cell even-collision test plus deterministic random extended fixtures,
not an exhaustive census of the exponentially large full lattice code space.
The local outer-edge factorization and commuting product are the reason the
finite tests extend beyond the sampled global masks.

The exhaustive same-cell fixture counts are 864, 2048, 4000, and 6912 for
`L=3,4,5,6`, plus 128 deterministic random fixtures per size. Constraint,
collision, enumeration-order, inverse, and FSWAP-phase failure counts are all
zero.

## Proper-cubic and translation covariance

At `L=3`, the runner checks all 24 proper-cubic frames. A frame maps half-edge
port `u` to port `R u`, maps the paired outer endpoint and face edge, and sends
the physical control exactly as

```text
R(B_u B_v) = B_Ru B_Rv.
```

It also transforms each individual `B_v Z_port(v)` constraint descriptor and
complete decoded occupation/tag fixtures through the stream/catch-up
macrostep, and checks the FSWAP sign. The XOR control, individual constraint
descriptor, and decoded action pass all L=3 translations. The auxiliary ports
transform as the inherited six-direction orbit; no axis is designated as
first.

The runner executes 576 decoded frame tests and 648 decoded translation tests,
with zero descriptor or action failures.

## Color/phase schedule and preferred-frame audit

A simple shared-cell schedule that successively swaps one central tag along
the `x`, `y`, and `z` axes is tested explicitly. Its ordered word changes both
when the axes are cyclically rotated and when the order is reversed. That
specific axis-colored schedule therefore carries a preferred frame at the
substep level and is not used.

The auxiliary-port construction avoids that choice. Its three-axis local
model uses disjoint port pairs, whose swap product is unchanged by a cyclic
axis rotation or reversal. In the full code the gates can share diagonal face
controls but still commute, so their product is defined without selecting
compiler phases.

If a backend serializes the commuting gates with colors, the color labels and
their ordering are compilation structure only. The substep schedule is not
physical time, no substep is called a tick or rate, and only the completed
stream/catch-up word is the operator component proposed here. Treating those
colors as observable time would reintroduce a preferred-frame question and is
outside this result; the full physical macrostep remains open.

For the rejected shared-cell word, the cyclic-axis frame residual is
\(\sqrt3=1.7320508075688776\) and the reversal residual is 2. For the disjoint
port word both corresponding residuals are exactly zero.

The nonzero residuals establish noncovariance only for the tested three-axis
shared-cell word. Other constant-depth colorings, palindromic words, smaller
auxiliary layouts, and autonomous phase-register constructions remain open.
There is no no-go claim.

## Collision deletion and lawful domain

Collapsing the six port tags back to one tag per cell exactly reproduces the
old decoded order-dependent collision: two swaps sharing the cell send the tag
to different neighbors in opposite orders. Thus the extra port resource is
load-bearing for this construction.

The lawful-domain guard rejects:

- odd total matter occupation, because Cycle 269 exposes the total-even
  algebra;
- mismatched matter/tag masks that violate a local port constraint;
- negative or out-of-range masks; and
- periodic `L<3`, where the cellulation aliases undirected faces.

The guard is not an encoder. The prepared total-even auxiliary port-code
input remains supplied structure.

## Supplied structure and exact boundary

Load-bearing supplied structure is:

1. the Cycle-269 square-pyramid face code and its `B_v/A_e` dictionary;
2. the existing outer-edge FSWAP and half-edge arrival decoder;
3. six auxiliary port M2 per coarse cell;
4. the local port constraints `B_v Z_port(v)=+1`;
5. the XOR control `(I-B_u B_v)/2`;
6. the stream-then-catch-up macrostep convention;
7. a prepared total-even port-code input; and
8. periodic training `L=3,4,5`, held `L=6`, and the declared acceptance tests.

Derived here are the weight-eight mapped control, ten-M2 gate, commuting
order-free catch-up product, decoded local inverse and constraint preservation,
independence and dimension neutrality of the supplied local constraints,
decoded multiparticle collision closure through held size, bounded conflict
ledger, and all-frame/all-translation covariance.

Open markers retained are:

- a bounded physical state encoder into the auxiliary port-code space;
- a local joint matter-coin/port-routing word that preserves the constraints
  when the six-mode matter coin mixes direction ports;
- an assembled physical full-Fock macrostep and its state intertwiner;
- a smaller covariant port layout or a successful autonomous color register;
- the same-code contact seam; and
- all later matter, source, gravity, time, Record, and probability semantics.

The port tag is not a Record. Gate enumeration is not physical time. No
physical energy, rate, gravity, or source law is inferred. There is no axiom
pressure.

## Disposition

```text
bounded collision-safe auxiliary catch-up gate:       PASS
local constraint rank and decoded inverse:            PASS
decoded same-cell total-even multiparticle collisions: PASS
held L=6 and random extended fixtures:                PASS
descriptor/decoded frame and translation covariance:  PASS
catch-up parity/order/host-side service:               NOT USED
tested shared-cell axis-colored word:                  ROUTE-SPECIFIC FAIL
bounded state encoder:                                OPEN
local matter-coin/port routing:                        OPEN
full-Fock compiler:                                    OPEN
shared obstruction or axiom pressure:                 NONE IDENTIFIED
```

The strongest next test is the local joint matter-coin/port-routing word. It
must coherently preserve all six `B_v Z_port(v)` constraints under the actual
Cycle-219 six-mode coin without copying a tag, selecting an axis order, or
using an external controller.
