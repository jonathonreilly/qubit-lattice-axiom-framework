# Carried internal-species source/field ledger repair — 2026-07-17

**Status:** conditional constructive repair with an explicit compiler boundary

**Authority:** none

**Audit:** unset

**Branch:** `codex/bare-metal-mvp-probes-20260713`

**Runner:** `scripts/carried_internal_species_source_field_ledger_repair_2026_07_17.py`

## Result

A finite source capacity can move with a one-particle matter carrier.  Give the
carrier six excited direction modes `e_d` and six ground direction modes
`g_d`.  Give the field six direction modes `f_b`.  At a matter/field contact,
the onsite vertex is

```text
T = sum_d ( |g,d><e,d| tensor b_s^dagger
          + |e,d><g,d| tensor b_s ),

b_s^dagger |0_f> = (1/sqrt(6)) sum_b |f_b>,

V(theta) = exp(+i theta T).
```

Emission consumes the matter's internal excitation and creates one scalar
field carrier.  Absorption removes that field carrier and restores the
internal excitation.  Both `e` and `g` receive the same Cycle-219 massive coin
and the same direction-preserving one-edge stream.  Thus the source capacity
moves with matter; it is not a fixed reservoir qubit at a lattice site.

The exactly conserved ledger is

```text
Q = N_e + N_f.
```

This internal excitation plus field number is not energy, a stress tensor, or
a gravitational source.  No wrapped phase is assigned physical-energy
semantics.  The construction supplies a local exchange ledger only.

## Physical-M2 encoding and exact intertwiner domain

This repair deliberately uses a new direct hard-core physical allocation per
coarse cell:

- 12 matter M2: six `e_d` and six `g_d`;
- six field M2: one for each `f_b`;
- 18 M2 total per cell, constant in lattice size.

On the declared one-matter, `Q=1` domain, the active contact block is the
42-dimensional direct sum

```text
span{|e,d;0_f>}                         dimension 6
  direct-sum
span{|g,d;f_b>}                         dimension 36.
```

The encoding `E` maps these labels injectively to computational basis states:
one occupied excited M2, or one occupied ground M2 plus one occupied field M2.
The runner finds 42 distinct basis indices.  The selected physical hard-core
vertex law on the complete 18-qubit cell Hilbert space is

```text
V_physical = E V_active E^dagger + I - E E^dagger.
```

It therefore acts as the tested 42-dimensional unitary on the code and as the
identity on the other `2^18 - 42 = 262102` computational dimensions.  This
identity completion is supplied law content, not derived.  The local vertex,
the two common matter coins, the field coin, and the physical one-edge qubit
permutations preserve the declared domain.  Consequently, for that code and
schedule,

```text
E G_carried = G_physical E.
```

There are no new local auxiliary or gauge constraints in this direct encoding.
Here "zero leakage" means invariance of the displayed active subspace under
the identity-completed physical unitary; it does not mean a new stabilizer
construction.  The
global one-matter and `Q=1` choice is a state-preparation boundary, but the
update does not query it: the onsite gate commutes with the charge operators,
and the streams merely relocate their local densities.  Hence there is no
global occupancy service or host-side parity controller during evolution.

The active exchange core for one direction touches two matter M2 and all six
field M2, so that core has support eight.  Exact identity completion on every
off-code state uses the active-space selector and therefore gives the complete
physical vertex support 18, still one bounded cell.  Coins have six-M2 species
support, the matter contact is onsite on 12 matter M2, and each stream is a
nearest-neighbor mode permutation.

## Schedule and declared carried-code continuity

One tick is explicitly supplied as

```text
common matter coin + field coin
    -> onsite E/G-field vertex
    -> excited and ground matter streams
    -> field stream
    -> local matter contact.
```

The executed sparse sector contains one matter carrier, so the final contact
is the identity there.  Algebraically the supplied onsite contact control is

```text
W_g = exp(i g binom(N_m,2)).
```

It is one on `N_m=0,1`, has the algebraic value `exp(i g)` on `N_m=2`, and
becomes the identity when `g=0`. The executed declared carried code has one
matter, so no two-matter carried-code contact evolution is run. This is only a retained
contact/deletion phase control, not a claim that the new hard-core streams
reproduce the Cycle-230 CAR seam.

This is the contact deletion control; it is not an executed two-matter result.

At the vertex, the signed field-number change `j_x` obeys

```text
Delta N_e(x) + j_x = 0.
```

The runner then records separate directed one-edge currents for excited
matter and field.  The incoming-current reconstruction equals the next-tick
`Q` density on the same declared carried code. Four ticks give:

```text
norm residual                         4.884981308350689e-15
coin Q-density residual               1.1102230246251565e-15
vertex Q residual                     1.3877787807814457e-16
matter edge-current residual          1.1102230246251565e-16
Q edge-current residual               1.1102230246251565e-16
matter current-sum residual           2.220446049250313e-16
Q current-sum residual                0.0
four-tick inverse residual            2.750844983854659e-15
```

Both matter labels and the field remain inside their four-edge causal cones.
An excited basis packet and a ground-plus-field basis packet move their matter
coordinate along the identical edge.  This is the operational check that the
source state is carried rather than pinned.

## Covariance, mass, emission, and deletion controls

The direction representation is `D(R)` for each of the 24 proper-cubic
frames.  On the active block it is

```text
D_active(R) = D(R) direct-sum (D(R) tensor D(R)).
```

Both `V(theta)` and the active coin commute with all 24 representations; the
maximum matrix residual is exactly `0.0`.  A random non-contact/contact sparse
state also satisfies schedule covariance across all 24 frames with maximum
state residual `2.7575098023275394e-15`.

Thus the matrix and schedule tests cover all 24 proper-cubic frames.

For `beta=-0.3`, both internal matter labels use the same Cycle-219 coin:

```text
analytic mass                         0.4534056541748852
dispersion mass                       0.4534056690336209
theta = 0.8 times analytic mass       0.3627245233399082
```

Thus the one-particle mass fixture is preserved rather than retuned.  At this
angle, a scalar excited input emits field weight
`0.1258992161287138`; the conjugate scalar ground-plus-field input restores
excited weight `0.12589921612871388`.  Setting `theta=0` makes the vertex the
identity and leaves two decoupled copies of the common matter coin/stream.
Setting `g=0` deletes the matter contact.

The active vertex's unitarity residual is `9.808906422059767e-16`; its
`[V,Q]` residual is `0.0`.  The identity-completed physical operator has
dimension `262144`, active dimension 42, and complement dimension 262102.
Because the physical computational basis images are distinct and every
elementary active transition remains inside them, active-subspace leakage is
zero.  Separated one-matter packets satisfy the linear composition control
with state residual `0.0`.  This is a superposition/spectator control, not a
same-lattice multiparticle theorem.

## Exact boundary against the existing CAR compiler

This 18-M2 direct code is not the Cycle-269 even-CAR code and is not a physical
CAR compiler.  Two exact measurements keep that distinction visible.

First, on the declared one-matter stream sector an ordinary qubit SWAP and a
fermionic FSWAP agree exactly.  Outside that sector they differ by a sign on
double occupancy:

```text
|| SWAP - FSWAP ||_2 = 2.0.
```

Therefore the direct qubit streams are exact on the tested one-matter domain,
but the result does not extend by assertion to full-Fock CAR transport, the
Cycle-230 seam block, or multiparticle exchange.

Second, the runner reconstructs the unchanged Cycle-269 local-check ranks
rather than importing a displayed formula.  For a literal simultaneous
two-internal-species target, the tested logical-exponent table is:

| `L` | physical M2 | unchanged C269 exponent | literal target exponent | residual deficit |
|---:|---:|---:|---:|---:|
| 3 | 405 | 164 | 326 | 162 |
| 4 | 960 | 386 | 770 | 384 |
| 5 | 1875 | 752 | 1502 | 750 |
| 6 held out | 3240 | 1298 | 2594 | 1296 |

For these tested sizes, the unchanged-code exponent is `6 L^3 + 2`, the
literal target exponent is `12 L^3 + 2`, and the exact residual is `6 L^3`.
This is a route-specific capacity measurement for an unchanged code and a
literal tensor-factor target.  It does not rule out a compressed internal
label, reuse of different gauge degrees, a changed check complex, staggered
encoding, or another local fermionization.

## Supplied structure inventory

The result imports rather than derives:

1. the direct 12-matter-M2 plus six-field-M2 allocation;
2. the one-matter, `Q=1` state-preparation domain;
3. identification of `e` as finite source capacity and `g` as discharged;
4. the direction-preserving scalar exchange operator `T`;
5. the coupling rule `theta = 0.8 m` and its sign;
6. identical Cycle-219 coins for the two matter labels;
7. the Cycle-214 field coin and its full off-scalar completion;
8. the coin/vertex/matter-stream/field-stream/contact schedule;
9. the local hard-core contact `W_g` and coupling `g=0.37`;
10. the vacuum reference and initial packet preparation;
11. the use of `c^-2` normalization already present in the mass fixture;
12. off-code unitary completions of the number-preserving qubit coins.

No source/action equation, static Green response, stress tensor, full-Fock
CAR compiler, clock, Record, Born/probability law, empirical calibration, or
realized-history selector is derived here.

## No-go discipline gate (N1–N8)

The negative statement initially under consideration was broad: "the
Cycle-269 substrate cannot carry an internal source species."  The gate status
is **FAIL for that broad statement**, so it is not shipped.  Only the measured
unchanged-code/literal-target residual above is retained as a partial
narrowing.

### N1 — alternative routes

| attack route | honesty marker | disposition |
|---|---|---|
| add six ground matter M2 per cell | **ATTEMPTED** | succeeds in this runner on the one-matter hard-core code, so it directly defeats any broad substrate no-go |
| repurpose the three Cycle-269 Wilson-center degrees | **ATTEMPTED** | this runner reconstructs the local-check rank including the `+2`; it does not supply the literal extra `6L^3` target exponent |
| compress the internal label into a non-tensor subsystem | **OPEN / UNTESTED** | not attempted here; invalidates a broad no-go |
| stagger or time-multiplex the internal label | **OPEN / UNTESTED** | not attempted here; changes the simultaneous target and invalidates a broad no-go |
| alter the local-check complex while keeping bounded gauge support | **OPEN / UNTESTED** | not attempted here; changes "unchanged Cycle 269" and invalidates a broad no-go |
| use an autonomous link-gauge fermionization | **OPEN / UNTESTED** | not attempted here; could address the full-Fock SWAP/FSWAP residual |
| reuse a doubled spectator construction | **OPEN / UNTESTED** | prior attempts expose different assembly residuals, so they do not rule out this residual-matched route |

Because several routes are `OPEN / UNTESTED`, N1 fails for a broad no-go.
This is why the note ships a constructive direct code plus an exact
route-specific residual only.  No route is marked `RULED OUT BY PRIOR RESULT`
where its residual or domain differs.

### N2 — wall independence

There is one measured residual, not a multi-wall set: the logical-exponent
difference between one unchanged code and one literal target.  The separate
SWAP/FSWAP residual concerns full-Fock exchange and is not presented as an
independent wall supporting the dimension statement.

### N3 — hidden-condition scan

The load-bearing conditions are explicit: unchanged Cycle-269 checks,
literal simultaneous two-species tensor semantics, finite sizes `L=3,4,5,6`,
and the displayed one-matter direct-code domain.  Sector preparation,
off-code completion, coupling, and schedule are listed as imports.  No
"standard QFT", preferred background, or canonical-state premise is used.

### N4 — residual matching

| witness | witness residual | current residual | match? |
|---|---|---|---|
| `WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md` | local-check exponent `6N+2` and three-dimensional Wilson center | unchanged-code exponent in the table | yes |
| `ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md` | pair-shadow nonadjacent assembly residual `sqrt(8)` | literal-target exponent deficit | no; not used as a witness |
| `PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md` | bounded canonical full-Fock assembly residuals | literal-target exponent deficit | no; not used as a witness |

### N5 — rhetoric and resolution audit

Tested resolutions are the local active 42-state block, one-edge streams,
four-tick sparse evolution, and global periodic local-check ranks at
`L=3,4,5,6`.  Not tested are arbitrary lattice sizes, compressed encodings,
changed physical complexes, or full-Fock multiparticle evolution.  Therefore
the note says "tested unchanged-code exponent deficit" and does not say
"internal species are impossible" or "CAR cannot be local."

### N6 — partial-closure paths

The direct 18-M2 code is an explicit partial-closure path and succeeds for the
carried one-matter source ledger.  A compressed subsystem, altered check
complex, staggered schedule, or local gauge encoding could retire more of the
boundary without any axiom change.  No claim that a new primitive or axiom is
required is made.

### N7 — steelman

A hostile reviewer should reject any broad negative conclusion immediately:
the present runner itself constructs a bounded proper-cubic carried-source
code, and the Cycle-269 exponent comparison fixes a target representation
rather than proving that every encoding of an internal two-level label needs
six fresh logical qubits per cell.  A subsystem or time-multiplexed label could
avoid the literal dimension count, while a link-gauge construction could
replace ordinary SWAP by a locally signed transport.  The evidence supports
only the displayed unchanged-code/literal-target mismatch.

### N8 — cross-cycle echo

Cycle 232's pair-shadow attempt showed that correct local dimension did not
guarantee global fermionic assembly.  Cycle 248 kept local Majorana/subsystem
and autonomous gauge routes live.  Cycle 269 then reframed its apparent gauge
factor as a direct sum of Wilson sectors.  Those prior corrections demonstrate
the applicable retirement mechanism: narrow the representation claim and
construct a different local code.  This note applies both mechanisms and does
not promote the residual to shared substrate obstruction.

**Gate disposition:** broad no-go **FAIL**; exact partial-narrowing measurement
retained.  There is no shared obstruction and no axiom pressure.

## Dependency-ledger effect and next test

- `C_ref`: unchanged; the Cycle-219 mass normalization is imported.
- `C_num`: unchanged at the framework level; the direct code adds a supplied
  hard-core field-number ledger only.
- `C_wrap`: unchanged; no phase lift or physical-energy reading is used.
- `C_int`: locally improved for a reversible carried emission/absorption
  vertex, but the coupling law and same-lattice multiparticle sector remain
  open.
- `C_local`: improved on the declared one-matter direct code: bounded support,
  zero leakage, 24-frame covariance, and no runtime occupancy service are
  explicit.  Full-Fock CAR transport remains open with residual `2.0` for the
  ordinary-SWAP control.
- `C_source`: improved from site-fixed finite capacity to capacity carried by
  matter, with an exact `N_e+N_f` continuity ledger.  Identification with a
  gravitational source and a sourced field equation remain open.

The highest-value next test is a same-lattice two-matter local-gauge version:
replace ordinary qubit stream crossings by an explicit bounded signed link
update, retain the carried `e/g` exchange, and test the Cycle-230 contact/seam
block without a global parity service.  Failure of that route would still be
route-specific unless the independent direct, gauge, and staggered classes all
converge on the same residual under N1–N8.
