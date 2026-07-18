# Physical Cycle-269 staggered reservoir catch-up — 2026-07-17

**Type:** constructive bounded operator-component probe

**Status:** reversible physical catch-up gate plus decoded action controls on a
declared total-even port/tag domain; state and full-Fock compilation open

**Authority:** none

**Audit:** unset

**Constitutional effect:** none

**Runner:**
`scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py`

## Result

The conditional part of the reversible staggered catch-up now has a bounded
physical Cycle-269 gate representative.  For the mapped half-edge matter mode
(v=(x,d)), Cycle 269 supplies the five-face parity word (B_v).  Its mapped
occupation projector is

```text
n_v=(I-B_v)/2.
```

Supply one auxiliary reservoir M2 per coarse cell.  If `vbar` is the unique
outer-edge partner of (v), define

```text
K_v = (I-n_v) tensor I_tags + n_v tensor SWAP(r_x,r_xbar).
```

This is a conditional transposition, not a tag reset.  Its physical support is
the five face M2s of (B_v) plus the two endpoint reservoir M2s: one
**seven-M2** gate.  It is exactly unitary, involutive, and auxiliary-number
preserving on its complete `128`-dimensional support.

The inherited outer FSWAP has nine face-M2 support.  One streamed-edge FSWAP
plus the arrival catch-up has an **eleven-M2** support union: nine face M2s plus
two auxiliary tags.  With the supplied reservoir layer, the allocation is

```text
15 Cycle-269 face M2/cell + 1 reservoir M2/cell.
```

The new gate commutes with every bounded local check and every Wilson.  The
inherited `B/A` terms of the outer FSWAP do too.  This is a bounded physical
gate component plus a decoded operator-action test; it is not an assembled
encoded-state macrostep, a bounded state encoder, or a full-Fock compiler.

There is no bounded state encoder in this result, and there is no full-Fock
compiler.  The auxiliary transport ledger is not gravity.

## Half-edge stream and exact catch-up action

Cycle 269 represents the six directions as oriented half-edge ports.  Its
outer face joins

```text
(x,d) <-> (x+e_d,d xor 1).
```

Thus a streamed carrier arrives at the opposite-oriented port of the next
cell.  That arrival-port convention is supplied structure and must not be
silently identified with the carried code's persistent direction label.

On a code-image port/tag label, the two substeps are

```text
outer FSWAP:
  |matter=(x,d); tag=x>
    -> |matter=(x+e_d,d xor 1); tag=x>

arrival catch-up:
  |matter=(x+e_d,d xor 1); tag=x>
    -> |matter=(x+e_d,d xor 1); tag=x+e_d>.
```

The second arrow is `K_vbar`, controlled by the arrival partner of `v`.  On
the complete declared port/tag basis it is a permutation and its own inverse.
The composed label action is exactly the co-moving tag action.  Omitting
catch-up leaves the tag at the departure cell for every matter port.

This is an exact port/tag action identity for the mapped occupation controls.
The exhaustive table is a host-side decoded label permutation, not execution
of encoded physical basis states or their coherent amplitudes.  It is not the
state-intertwiner equation

```text
E G_coarse = G_physical E.
```

No bounded Cycle-269 state map `E` is constructed or executed here.

## Physical support and leakage controls

The runner constructs the actual Cycle-269 square-pyramid code at
`L=3,4,5,6`, with `L=6` held out.  For every one of the `6 L^3` matter ports it
checks:

- exactly one outer partner with the correct translated cell and reversed
  half-edge direction;
- `B_v` is phase-zero, pure `Z`, and weight five, exactly matching the control
  used in the local matrix;
- seven-M2 support for (K_v);
- nine-face-M2 support for the mapped outer FSWAP polynomial;
- eleven-M2 support for their union;
- zero commutator leakage against all local checks and all three Wilsons; and
- zero leakage for each inherited `B_u`, `B_v`, and `A_e` stream term.

The complete port/tag basis controls are:

| `L` | held out | port/tag basis | catch-up inverse failures | staggered/co-moving failures | fixed mismatches without catch-up |
|---:|---:|---:|---:|---:|---:|
| 3 | no | 4,374 | 0 | 0 | 162 |
| 4 | no | 24,576 | 0 | 0 | 384 |
| 5 | no | 93,750 | 0 | 0 | 750 |
| 6 | yes | 279,936 | 0 | 0 | 1,296 |

These are exhaustive finite-basis tests of the displayed decoded port/tag
action, not a sampling claim and not a physical-state basis census.

## Proper-cubic and translation covariance

At `L=3`, the runner applies all 24 proper-cubic frames.  It checks the mapped
outer partner, physical face edge, (B_v), framed `A_e`, auxiliary endpoint
pair, and every reservoir-tag basis position.  The inherited bounded local
incident-order Clifford repair is included for `A_e`; no preferred physical
frame is inserted.

The catch-up and outer-edge descriptor also pass the full 27-element `L=3`
translation group.  The totals are

```text
proper-frame port/tag tests       104,976
translation port/tag tests        118,098
frame failures                          0
translation failures                    0.
```

This is descriptor-level covariance of the inherited operator word, the new
controlled gate, and their decoded port/tag action.  The runner does not
conjugate an assembled full stream/catch-up matrix on an encoded state space.
The stream-then-catch-up substeps are schedule structure, not physical time.

## Total-even lawful domain

Cycle 269 represents the total-even matter algebra.  A lone one-particle state
is not in its state-code domain.  The lawful-domain decoded fixture therefore
uses:

1. one active mobile carrier;
2. one even-parity spectator whose outer tag-swap edge is disjoint from the
   active edge; and
3. one auxiliary reservoir excitation initially at the mobile cell.

The spectator's disjoint swap sees tag vacuum at both endpoints, so it does not
change the active reservoir tag.  Through held-out `L=6`, every body cell has
one spectator choice whose outer edge is disjoint from all six mobile-direction
edges at that body.  On the mutually exclusive one-active decoded sectors, the
same spectator therefore supports the full local six-direction block, and the
displayed operator action extends linearly.  No coherent encoded state is
constructed or executed.  Forward and reverse control orders agree, catch-up
is involutive, and the staggered tag reaches the mobile arrival cell exactly.

The even-parity spectator is a prepared lawful-domain condition.  The runner
does not construct its state preparation or promote it to a physical reference
origin.  It also does not prove one fixed spectator works for an arbitrary
spatially extended mobile wavepacket or after applying a coin to the spectator;
this probe executes the stream/catch-up component, not a whole matter update.

## Collision boundary

The runner rejects odd, coincident mobile/spectator, overlapping-edge, and
mistagged fixtures.  This is load-bearing.  If two occupied controls use
different auxiliary swaps sharing one cell, the swaps do not commute:

```text
operator norm of [SWAP_01,SWAP_02] = 1.7320508075688772.
```

The two control orders move a tag at the common cell to different neighboring
cells.  Therefore a multiparticle collision schedule or a larger auxiliary
port construction is still required outside the declared disjoint-edge
domain.  This is unfinished implementation, not a shared substrate
obstruction, no no-go claim, and no axiom pressure.

## Supplied structure

Load-bearing supplied structure is:

1. the Cycle-269 local-check-only square-pyramid face code, its bounded
   `B_v/A_e` operator dictionary, and its sector-indexed Wilson behavior;
2. the occupation convention (n_v=(I-B_v)/2);
3. the half-edge arrival decoder `d -> d xor 1` under outer FSWAP;
4. one auxiliary reservoir M2 per coarse cell and a prepared one-tag sector;
5. the stream-then-catch-up order;
6. the conditional transposition (K_v);
7. a prepared separated even-parity spectator; and
8. periodic `L=3,4,5,6` domains and all acceptance conditions.

Derived here are the seven-M2 local matrix, its exact inverse and number
ledger, confirmation that every mapped `B_v` is the literal pure-`Z`
weight-five control used by that matrix, constant eleven-M2 stream/catch-up
support union, zero local-check and Wilson leakage, exhaustive held-size
decoded port/tag equality, descriptor-level cubic/translation covariance, and
the explicit collision fixture.

Not earned are a bounded physical state encoder, a full-Fock compiler, a
same-code contact update, multiparticle collision law, dressed mass, stationary
response, physical energy/stress/source, gravity, a clock/rate, occurrence, a
Record, a Born law, or empirical calibration.  A Wilson label is not a Record.

## Ledger effect and disposition

- `C_local` improves at operator-component level: the conditional catch-up gate
  now has a bounded physical Cycle-269 representative with exact constraints
  and descriptor-level covariance.  A bounded state `E`, an assembled encoded
  macrostep, and a multiparticle schedule remain open.
- `C_source` improves only at the auxiliary transport interface.  No physical
  source selection, normalization, stationary moving response, or gravity law
  is added.
- `C_ref`, `C_num`, `C_wrap`, and `C_int` are unchanged.  In particular, the
  even-sector spectator and one-tag preparation remain supplied.

No framework maturity score changes.  The strongest disposition is:

```text
bounded physical catch-up gate:           PASS
local checks and Wilson preservation:     PASS
descriptor-level cubic/translation covariance: PASS
held-out L=6 decoded port/tag action:      PASS
total-even decoded spectator domain:      PASS
multiparticle collision schedule:         OPEN
bounded state/full-Fock compiler:          NOT CONSTRUCTED
shared obstruction or axiom pressure:     NONE IDENTIFIED
```

The next constructive test is a collision-safe auxiliary port layout or
constant-depth edge coloring whose completed macrostep is proper-cubic
covariant on a genuine multiparticle Cycle-269 sector, followed by the
same-code contact seam.

## Verification

```text
python3 -m py_compile \
  scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py

PYTHONPATH=scripts python3 \
  scripts/physical_cycle269_staggered_reservoir_catchup_2026_07_17.py
```
