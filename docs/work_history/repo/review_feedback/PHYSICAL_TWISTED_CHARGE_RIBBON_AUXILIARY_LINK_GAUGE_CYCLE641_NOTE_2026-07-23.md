# Physical twisted charge-ribbon / auxiliary-link-gauge discriminator — Cycle 641

Status: **PASS — exact contractible compiler and conditional periodic extension only**  
Authority: **none**  
Audit: **unset**  
Accepted: **false**  
Constitutional effect: **none**

## Immutable provenance

All Cycle-235/247/532/639 premises are loaded from the exact committed shore
`c27f72ff8b1058d872695829c05e95da415813bc` through a temporary `git archive`.
The runner records that no dirty working-tree premise bytes were used.  The
dirty Cycle-532 runner hash is retained only as a comparison diagnostic; it is
not executed and supplies no evidence.

## Question

Can a smallest twisted cubic charge ribbon or auxiliary link gauge remove the
Cycle-639 alternate-path sign without a global prefix, then extend to the
Cycle-230 seam-bearing L3/L6/L7 torus on one physical code?

Cycle 641 answers the first clause constructively on one contractible
plaquette.  It does **not** answer the periodic clause unconditionally.  The
existing rough-face extension remains conditional on three supplied
Wilson/spin signs.  The auxiliary-Majorana and overlapping-tensor alternatives
remain live, separately typed routes.

## Exact contractible result

Take four physical M2 factors on the oriented square edges

```text
e0=(0,1), e1=(1,2), e2=(2,3), e3=(3,0).
```

The local even-CAR presentation uses

```text
B_i = product of Z on edges incident at vertex i,
A_01 = X_0,
A_12 = X_1 Z_0,
A_23 = X_2 Z_1,
A_30 = X_3 Z_0 Z_2.
```

Adjacent `A` generators anticommute, disjoint generators commute, and every
generator has bounded support.  The local loop operator is

```text
Q = A_01 A_12 A_23 A_30.
```

For each even four-mode occupation word, the four `B_i` eigenvalues select two
complementary edge words.  The `Q=+1` condition selects one normalized ray.
After a fixed column-phase convention, these eight rays form a single
`16 x 8` isometry `E`.  This is one encoding and one code; the edge and exchange
tests do not switch charts or sectors.

On each edge use the exact bounded polynomial

```text
F_e = (B_u + B_v + i B_u A_e - i B_v A_e)/2.
```

The declared edge `e0` obeys

```text
F_e0 E = E Gamma((01))
```

to residual `1.11e-16`.  For the two schedules

```text
U_cw  = F_12 F_30 F_01 F_23,
U_ccw = F_01 F_23 F_12 F_30,
```

the runner finds, on the complete even code rather than on one witness state,

```text
U_cw E  = E Gamma((02)(13)),
U_ccw E = E Gamma((02)(13)),
||(U_cw-U_ccw)E||_max = 0.
```

Both opposite-carrier words `0101` and `1010` return with amplitude `-1`.
Changing only the local loop sector to `Q=-1` changes both amplitudes to `+1`.
Thus the exchange sign is carried by the local contractible flux.  It is not
read from a prefix register, a Jordan-Wigner interval, a runtime parity query,
or host-side branching.

The empty-charge link state is explicitly

```text
(|0000> + |1111>)/sqrt(2).
```

It is prepared on this bounded square by `H(e0)` followed by three CNOTs from
`e0`.  Deleting one entangler produces a norm-one preparation residual.  The
loop constraint has weight four; each displayed FSWAP polynomial has Pauli
support at most three.  The overhead is four M2 factors for four matter modes,
constant on this declared block.  Edge and both exchange schedules have zero
code leakage at numerical tolerance.  All eight lawful even syndromes are
encoded; all eight malformed odd syndromes are rejected because the product
of the four star parities is identically even.

This directly retires the **contractible-square** residual identified in
Cycle 639.  It does not by itself retire the periodic initialization wall.

## Periodic extension boundary

Because the local pull-through closes, the runner extends it through the
Cycle-247/Cycle-532 rough-face presentation at training L3 and held L6/L7.
The results are:

| L | cells | physical M2 | local rank | fixed rank | Wilson increment | maximum local weight | maximum Wilson weight |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 27 | 594 | 403 | 406 | 3 | 28 | 21 |
| 6 | 216 | 4752 | 3238 | 3241 | 3 | 28 | 39 |
| 7 | 343 | 7546 | 5143 | 5146 | 3 | 28 | 45 |

The bounded data are strong:

- overhead is exactly `22 M2/cell` on all three sizes;
- the three Cycle-230 outer seam edges per cell are present;
- every mapped outer `A` commutes with all bounded local constraints;
- maximum B-FSWAP support is 13 and does not grow with L;
- all 15 onsite pairs and all 15 contact words commute with stabilizer and
  gauge generators;
- placement has zero collisions and all 24 proper-cubic frame checks pass;
- the all-24/all-576 covariance replay has zero failures, including 684,288
  single-face group-law cases;
- the Cycle-219 one-particle mass residual is `2.22e-16`;
- the Cycle-230 contact deletion residual is `0.367893...` and all six seam
  subchecks pass;
- deleting an independent local constraint lowers rank by one, deleting a
  Wilson initializer lowers fixed rank by one, and deleting one stream
  dressing creates nonzero syndrome.

But the locally generated stabilizer space is three ranks short of one fixed
periodic spin sector for every L.  The required Wilson weights grow
`21,39,45` at L3/L6/L7.  No bounded local or autonomous preparation of those
three signs is supplied.  The periodic result is therefore exactly:

```text
conditional fixed-spin factorization and bounded runtime: PASS
unconditional periodic local E and gauge-vacuum genesis: OPEN
```

The seam result in this runner is seam incidence plus the re-executed logical
Cycle-230 comparator, pulled back conditionally through the pinned faithful
matter factor.  A literal full rough-code seam matrix is not enumerated here.
Accordingly this artifact does not claim the full periodic Cycle-230 update as
a newly closed physical `EG` certificate.

Calling the former a complete physical-site compiler would hide supplied
topological structure.  Cycle 641 does not do that.

## Route-by-route disposition

### 1. Charge-bound flux/ribbon — priority route

Disposition:
`EXACT_ON_ONE_CONTRACTIBLE_PLAQUETTE__CONDITIONAL_PERIODIC_EXTENSION`.

This is the strongest result.  It supplies a literal local `E`, a local loop
constraint, explicit vacuum preparation, edge `EG`, two alternate exchange
`EG` identities, exchange phase `-1`, and a wrong-flux deletion.  Its periodic
runtime is bounded and cubic-covariant conditional on three supplied Wilson
signs.  Bounded periodic sector genesis remains open.

### 2. Auxiliary Majorana link

Disposition:
`ATTEMPTED_TWO_NATURAL_ORDERINGS__OPEN_AUXILIARY_CLIFFORD_VARIANTS`.

The runner allocates one auxiliary fermionic mode at each end of each square
edge and audits two explicit Jordan-Wigner layouts.

- Vertex-block ordering cancels the intermediate string in a dressed matter
  edge, but the bare auxiliary link stabilizer spans intervening vertex
  blocks; the closing-link support grows on a held cycle.
- Edge-pair ordering makes every auxiliary link stabilizer support two, but
  the matter interval remains in the dressed update and grows with held size.

This is an ordering tradeoff for the two tested constructions, not an
auxiliary-link no-go.  A non-JW Clifford link code, extra local Majoranas,
measurement/reset preparation, or a different cellulation was not exhausted.

### 3. Overlapping pull-through tensor

Disposition:
`ATTEMPTED_LOCAL_PULL_THROUGH__PERIODIC_PREPARATION_OPEN`.

The same exact `16 x 8` square map is treated as an overlapping plaquette
tensor, with neighboring projectors sharing edge M2 factors.  Local
pull-through is exact.  On the periodic rough-face complex the bounded
projectors leave the same three characters shown by the rank table.  No
bounded tensor-contraction, dissipative, or measurement/reset procedure that
selects one periodic sector is supplied.

The charge-ribbon and overlapping-tensor periodic walls are correlated
presentations of the same higher-form code.  They are not counted as two
independent failures.

## N1-N8 discipline

The current origin-main `no-go-discipline` skill was used; its hash is
`7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7`.

### N1 — alternative routes

Three requested routes were attempted.  Two further live routes are retained:
an open/punctured boundary that types the spin sector by local inflow, and a
bounded dissipative or measurement/reset Wilson preparation.  The latter two
were not attempted and cannot be silently counted as failures.

### N2 — wall independence

The charge-ribbon and tensor periodic preparation walls are correlated.  The
auxiliary ordering tradeoff is distinct, but its broader Clifford family was
not exhausted.  Independence is incomplete.

### N3 — hidden walls

Explicit walls/supplies are the square orientation, `Q=+1` flux, GHZ-like
gauge vacuum, four-mode target presentation order, Cycle-247 cellulation,
three fixed Wilson signs, 22-M2/cell layout, support-13 mapped polynomial, and
the absence of a literal elementary-gate factorization for those support-13
blocks.  No energy, rate, Record, source, tick, or frame selector is imported.

### N4 — exact residual matching

Cycle 639's ordinary-M2 cubic-square path residual was `4`.  On the same
contractible path question, the flux-bound code gives residual `0` and an
exchange phase `-1`.  The mechanism change is explicit: the path sign is the
local loop character.  No zero periodic-preparation residual is claimed.

### N5 — rhetoric audit

- Element: one edge and one exchange square are exact.
- Site: the four-edge block has constant overhead.
- Mode: the complete even four-mode algebra is represented.
- Block: two contractible exchange paths agree.
- Lattice: the periodic extension is conditional on growing initializers.

These resolutions are not conflated.

### N6 — partial closure paths

The surviving paths are boundary/puncture inflow, bounded dissipative or
measurement/reset spin-sector preparation, non-JW auxiliary Clifford links,
and literal elementary factorization of support-13 mapped matter blocks.

### N7 — steelman

A fermionic PEPS or auxiliary-Majorana stabilizer construction could combine
the exact local pull-through proved here with local boundary inflow or
autonomous dissipation that fixes the spin sector.  The decisive certificate
would be one fixed periodic `E/G` on L3/L6/L7, bounded vacuum genesis, no
Wilson initializer input, all24/all576, full seam, onsite A2/contact/mass, and
elementary physical gate factorization.

### N8 — cross-cycle echo

Cycles 235 and 532 already exposed three spin/Wilson labels in closely related
higher-form presentations, so the periodic rank defect is an echo, not new
independent obstruction evidence.  Cycle 639 exposed the local path-sign
failure; Cycle 641 retires that witness only on a contractible flux-bound
block.

Therefore:

```text
broad negative gate: FAIL / DO NOT SHIP
minimum-content gate: FAIL / DO NOT SHIP
shared-obstruction gate: FAIL / DO NOT SHIP
axiom-pressure gate: FAIL / DO NOT SHIP
```

No impossibility, minimum-content, shared-obstruction, or axiom-pressure claim
is shipped.

## Supplied structure

The construction supplies rather than derives:

- four named square vertices and four named edge M2 factors;
- one proper edge orientation/incidence framing for `A_e`;
- the local `Q=+1` flux sector;
- a four-mode order used to state the exterior target;
- a GHZ-like empty-link vacuum and bounded one-square preparation circuit;
- the Cycle-247 rough/punctured face graph for the periodic extension;
- three all-plus Wilson/spin signs for the conditional periodic code;
- the Cycle-532 22-M2/cell layout and support-13 polynomial runtime;
- the Cycle-219 mass and Cycle-230 contact/seam laws.

It does not supply a runtime global parity service, global Jordan-Wigner
prefix, host branch, active frame selector, physical energy, generator rate,
Record, realized-history tick, stress/source, gravity, or autonomous resource
genesis.

## Prior-art and novelty boundary

The broad idea of bosonizing fermions with link variables, Gauss/loop
constraints, and spin-structure sectors is prior art; Cycle 235 and Cycle 532
already instantiated that family in this repository.  Cycle 641's new content
is narrower and executable:

1. the smallest four-edge physical-M2 code is written as a literal `16 x 8`
   `E`;
2. one fixed phase convention simultaneously proves one-edge `EG` and two
   complete-code alternate-path `EG` identities;
3. the wrong local flux flips the exchange witness from `-1` to `+1`;
4. the same runner audits L3/L6/L7 ranks, locality, seam, onsite, mass/contact,
   deletion, and all24/all576 covariance;
5. auxiliary-Majorana and tensor routes are dispositioned without promoting
   their scoped failures to constitutional evidence.

No claim of inventing higher-form bosonization, fermionic PEPS, or auxiliary
Majorana mappings is made.  Thirring is not used by this result.

## Dependency ledger

| Wall | Cycle-641 disposition |
|---|---|
| `C_ref` | Square orientation, `Q=+1`, gauge vacuum, and three periodic Wilson signs are explicit supplies; autonomous periodic reference genesis remains open. |
| `C_num` | Four-mode even CAR has a literal four-M2 code.  The Cycle-583 A2 payload is preserved through the conditional Cycle-532 matter factor. |
| `C_wrap` | Contractible alternate paths close.  Periodic L3/L6/L7 retains three growing Wilson initializers; no tick or Record follows. |
| `C_int` | Edge/exchange, onsite Givens/contact, Cycle-219 mass, and Cycle-230 logical seam comparators pass on their declared surfaces; no literal full rough-code seam matrix is enumerated. |
| `C_local` | Advanced: the Cycle-639 square residual is removed with constant overhead and no prefix.  Unconditional periodic `E`/preparation remains open. |
| `C_source` | Unchanged: no energy, source, stress, gravity, or resource genesis is derived. |

This narrow result does not independently rebase the campaign's five-lane
planning coordinates.  It sharpens `C_local`; it does not add a Record, clock,
source, or probability derivation.

## Scope firewall

- A contractible plaquette compiler is not a full periodic compiler.
- A conditional Wilson-fixed factorization is not bounded local sector
  genesis.
- A logical seam comparator is not a newly enumerated full rough-code seam
  matrix.
- Two failed JW layouts are not an auxiliary-Majorana no-go.
- The ribbon and overlapping tensor are not independent obstruction evidence.
- A wrapped phase is not physical energy.
- A generator element is not a rate.
- The gauge-vacuum preparation is not a Record.
- A factor order is not a tick or realized history.
- No source or gravity claim is present.

## Optimal next campaign

Run a bounded spin-sector genesis tournament:

1. punctured/open boundary inflow with locally typed spin structure;
2. bounded dissipative or measurement/reset Wilson preparation;
3. a non-JW auxiliary-Clifford link code with local link checks and local
   dressed updates in the same tensor order.

Require one fixed periodic `E/G` on L3/L6/L7 with no supplied Wilson signs,
then factor every support-13 matter polynomial into elementary one/two-M2
gates and rerun the complete Cycle-230 coarse update.  Only after that closure
should the Cycle-612 causal-time harness be rerun.
