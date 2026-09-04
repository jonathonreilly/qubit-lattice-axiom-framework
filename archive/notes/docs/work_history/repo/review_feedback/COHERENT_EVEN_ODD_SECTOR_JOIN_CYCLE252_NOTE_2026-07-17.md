# Coherent even/odd common-Wilson sector join — Cycle 252

**Date:** 2026-07-17

**Type:** constructive coherent sector join with an exact local-code/topology
split and an ordinary-M2 CAR discriminator

**Status:** reference-free local sector subsystem and one quantum-controlled
sign update constructed; full ordinary-M2 CAR compiler not closed

**Authority: none**

**Audit: unset**

**Constitutional effect:** none

Companion runner:

```text
scripts/coherent_even_odd_sector_join_cycle252_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.  It creates only this note and runner.

## Result up front

Promoting Cycle 245's `h`-dependent signs to local quantum frame qubits works:
one fixed sector-blind update consumes the Cycle-219 coin evaluated at Cycle
230's fixed `beta=-0.3` and the Cycle-230 `A/B` FSWAP/contact signs without a
classical `000`/`111` gate table.

The marked reference charge can also be removed from the **local code
definition**.  Introduce one charge-frame qubit `R_v` per matter vertex and
coherently retain every charge background `r` with the same parity as the
matter state.  Local charge-pair and connection-frame moves make the choice of
`r` and the flat representative `h` gauge on the enlarged joint state.

The resulting reference-free local subsystem has, per coarse cell,

```text
 6 ordinary matter M2 factors M_v,
15 Cycle-245 gauge M2 factors G_e,
15 local connection-frame M2 factors F_e,
 6 charge-frame M2 factors R_v,
-----------------------------------------
42 ordinary M2 factors.
```

Its bounded local stabilizers leave exactly **three Wilson logical qubits**.
Three nonlocal conditions recover the exact `6L^3` full-Fock dimension:

```text
W_F,0 W_F,1 = +1,
W_F,1 W_F,2 = +1,
W_F,0 (-1)^(sum_v r_v) = +1.
```

The first two have weights `6L`.  The parity-Wilson condition has weight

```text
6L^3 + 3L.
```

Thus the Cycle-245 trilemma is sharpened:

- **local quantum storage of the `h` signs:** constructive and bounded;
- **preparation/correlation with global parity and common Wilson:** still
  topological/nonlocal; and
- **marked reference charge:** avoidable by a coherent charge orbit, at the
  cost of retaining the global parity-Wilson condition.

This is not yet the requested ordinary-M2 CAR compiler.  The natural promoted
`h` hopping image

```text
X_(M_u) X_(M_v) Z_(G_e) Z_(F_e)
```

still commutes with the corresponding operator on an incident edge.  The
Cycle-235 even-CAR hopping generators anticommute when exactly one endpoint is
shared.  Commuting diagonal `F/R` dressings do not repair that algebra.
Prepending a Jordan-Wigner matter map restores the algebra only with maximum
stream strings `54,96,150,216` at `L=3,4,5,6`.

Accordingly:

- an exact local two-mode coherent join and sector-blind FSWAP pass;
- actual coin/FSWAP/contact quantum sign control is bounded;
- the 42-role stabilizer code has the exact full-Fock rank after three
  topological conditions;
- all translations, all 24 proper-cubic frames, and **held-out L=6** pass;
- but no lawful global ordinary-M2 CAR isometry `E` is constructed.

The Cycle-219 one-particle mass and Cycle-230 rank-73 seam are therefore kept
as predecessor targets and are **not** claimed physically reproduced.  This
is an exact partial construction, not a shared obstruction.  There is **no
axiom pressure**.

## 1. Reference-free coherent join

Cycle 245's sector map is

```text
V_(r,h)|psi>
 = 2^(-(abs(V)-1)/2)
   sum_[s in F2^V/<1>]
   (-1)^(r dot s) Z_M(s)|psi> |h + delta s>_G,
```

with

```text
sum_v r_v = p,
Wilson(h) = (p,p,p),
p = total matter parity.
```

Cycle 245 used `r=0,h=000` in the even sector and one marked negative charge
with `h=111` in the odd sector.  Cycle 252 instead defines the coherent orbit

```text
E_join |psi_p> proportional to
  sum_(r: sum r=p)
  sum_(h flat: Wilson(h)=(p,p,p))
    |r>_R |h>_F V_(r,h)|psi_p>.
```

The `R` and `F` words are orthogonal quantum labels.  Normalization therefore
preserves the sector isometry, and the direct sum over `p=0,1` has the full
input dimension.  No `r`, `h`, seam, or parity branch is read or classically
selected.

This formula should not be mistaken for an autonomous preparation circuit.
It is a coherent code definition.  The local stabilizers below specify a
three-topological-qubit subsystem; preparing the three parity/Wilson
correlations remains separate.

## 2. Bounded local stabilizers

Let

```text
A_v = Z_(M_v) product_(e incident v) X_(G_e)
```

be the Cycle-245 Gauss star.  The coherent join is stabilized locally by:

```text
C_v = A_v Z_(R_v),

K^R_e = X_(R_u) X_(R_v) Z_(G_e) Z_(F_e),

K^F_v = [product_(e incident v) X_(F_e)] Z_(M_v) Z_(R_v),

L^F_c = product_(e in c) Z_(F_e)
```

for every dual edge `e=(u,v)` and every local primal-edge cycle `c`.

The identities behind the two gauge-motion families are exact:

```text
Z_(G_e) V_(r,h)
  = (-1)^(h_e) V_(r+e_u+e_v,h),

Z_(M_v) V_(r,h)
  = (-1)^(r_v) V_(r,h+delta e_v).
```

The `Z_F` and `Z_R` factors cancel these branch phases, so `K^R_e` and
`K^F_v` genuinely stabilize the **joint** orbit.  They do not declare a
data-only action gauge.

All four local families commute.  At `L=3`, adding the three topological join
conditions gives 1029 displayed rows, rank 972, zero phase inconsistencies,
and zero pairwise commutator failures.

The rank census is:

| `L` | physical M2 | local rank | local exponent | full rank after 3 topological conditions | joined exponent |
|---:|---:|---:|---:|---:|---:|
| 3 | 1134 | 969 | 165 | 972 | 162 |
| 4 | 2688 | 2301 | 387 | 2304 | 384 |
| 5 | 5250 | 4497 | 753 | 4500 | 750 |
| 6 held out | 9072 | 7773 | 1299 | 7776 | 1296 |

In general,

```text
local exponent = 6L^3 + 3,
joined exponent = 6L^3.
```

The local excess is not arbitrary multiplicity: it is exactly the three
Wilson logical bits of the flat `F` connection.

## 3. Exact local sector-blind update

For a local symmetric matter operator with endpoint word `a` and a bounded
gauge chain `c`, Cycle 245's sector map contains the sign

```text
(-1)^(c dot h).
```

Cycle 252 replaces this scalar branch table by the operator

```text
Z_F(c) = product_(e in c) Z_(F_e).
```

The result is one fixed quantum operator on `M/G/F/R`.  It is block diagonal
in a computational `F` basis, but no classical controller chooses a block.
`R` remains a coherent spectator because the compatible observable map does
not depend on which charge-background representative is used.

### Exact joined edge fixture

The runner constructs an explicit two-mode isometry that sums both charge
backgrounds of the matter parity, both local flat representatives, and the
Cycle-245 gauge orbit.  A seventh local test bit represents the global Wilson
logical label; it is tied to charge parity but does not control the gate.

The results are:

```text
isometry residual:                 2.22044604925e-16
sector-blind FSWAP residual:       0
joined stabilizer residual:        0
classical sector table:            absent
marked reference:                  absent
```

The seventh test bit is only a finite fixture proxy for the global common
Wilson logical.  It is not claimed to localize the lattice-wide
parity-Wilson constraint.

### Actual fixed Cycle-230 gate sequence

The Cycle-219 six-mode coin evaluated at the fixed Cycle-230 value
`beta=-0.3` has 792 nonzero Pauli terms in the tested
decomposition; every endpoint word is parity even and every minimum internal
chain has length at most three.  The actual contact has 64 terms, all
`h`-independent.  The actual FSWAP has four terms.

The fixed quantum-controlled support bounds are:

| factor | matter | gauge | frame | total bounded region |
|---|---:|---:|---:|---:|
| onsite coin | 6 | 12 | 12 | 30 |
| onsite contact | 6 | 0 | 0 | 6 |
| outer `A/B` FSWAP | 2 | 1 | 1 | 4 |

On local flat branches, the actual matrix controls give:

| factor | intertwining residual | interference-uncompute residual | branch-weight residual |
|---|---:|---:|---:|
| coin | `1.8094e-16` | `1.8094e-16` | `6.9389e-18` |
| `A` FSWAP | `0` | `0` | `0` |
| `B` FSWAP | `0` | `0` | `0` |
| contact | `1.2313e-16` | `1.2313e-16` | `1.3878e-17` |

This is a genuine branch-interference test, not only a diagonal branch
probability check.

## 4. The three questions separated

### (a) Local quantum storage of the h-dependent signs

**Constructed.**  One `F_e` qubit per graph edge stores the sign locally.
Coin chains use at most three nearby `F` qubits, stream FSWAP uses one, and
contact uses none.  The controlled operator is fixed and proper-cubic.

### (b) Preparation/correlation with parity and common Wilson

**Not localized.**  Local constraints leave three Wilson logicals.  The
rank-complete even/odd join needs:

| condition | support weight |
|---|---:|
| `W_F,0 W_F,1` | `6L` |
| `W_F,1 W_F,2` | `6L` |
| `W_F,0 Z_R(all vertices)` | `6L^3+3L` |

The last relation is the exact parity-Wilson correlation.  The product of all
local `C_v` already identifies `Z_R(all)` with total matter parity, but it
does not make that global logical operator bounded.

No bounded-depth autonomous preparation of these three correlations is
claimed.  No universal preparation no-go is claimed either.

### (c) Marked reference charge

**Removed from the local code definition.**  The `R` orbit coherently includes
all `2^(6L^3-1)` backgrounds of the correct parity, and `K^R_e` moves charge
pairs locally.  There is no selected vertex.  By contrast, the Cycle-245
single reference has a six-element proper-frame orbit and is moved by every
nonzero coarse translation.

The reference has not disappeared for free.  Its role has been replaced by a
large coherent gauge orbit and the nonlocal parity-Wilson condition above.

## 5. Ordinary-M2 CAR discriminator

The rank and local sector map are not enough.  The matter carriers in this
candidate are ordinary `M_2` tensor factors.  On two incident edges, the
promoted hard-core images are schematically

```text
O_uv = X_u X_v Z_(G_uv) Z_(F_uv),
O_uw = X_u X_w Z_(G_uw) Z_(F_uw).
```

They commute.  Their shared matter action is the same `X_u`, and every other
displayed factor is a commuting diagonal operator on a distinct carrier.
The actual Cycle-235 framed even-CAR edge generators anticommute for one
shared endpoint.

The runner repeats this on the actual square-pyramid graph:

```text
promoted-h hard-core pair commutator: 0
Cycle-235 incident even-CAR relation: anticommutes
shared endpoints:                    1
```

Adding the local `h` control therefore fixes Cycle 245's sector-dependent
sign table but not its fermion-sign problem.  If a Jordan-Wigner map is first
placed on the ordinary matter tensor factors, the maximum shorter-sector
stream string is:

| `L` | JW matter string | with local gauge/h dressing |
|---:|---:|---:|
| 3 | 54 | 58 |
| 4 | 96 | 100 |
| 5 | 150 | 154 |
| 6 held out | 216 | 220 |

This is a candidate-family failure, not a theorem against noncommuting
auxiliary dressings, subsystem fermionization, open boundaries, or other
ordinary-M2 codes.

## 6. Proper-cubic covariance and translations

The local stabilizer families are defined only by vertex-edge incidence,
local cycles, and the two proper-cubic role orbits.  They pass all unit coarse
translations at `L=3,4,5,6`.

The `111` cohomology class is invariant under all 24 proper frames even though
a displayed three-membrane representative changes by a cut.  The coherent
`F` orbit retains all such representatives, so no seam plane is preferred.
The onsite minimum-chain set is permuted exactly by all 24 frames.  The actual
coin/contact maximum matrix-frame residual is `1.6022e-15`, and outer `A/B` edges
are permuted by the full graph action.

A selected Cycle-245 charge has a six-element proper-frame orbit.  Cycle 252
selects none: all `6L^3` charge roles occur in the coherent background orbit.

## 7. Explicit physical M2 macro placement

One collision-free period-64 placement is:

```text
matter vertices:          6 D_a                         [6]
charge-frame vertices:   20 D_a                         [6]
gauge internal faces:     8 (D_a+D_b)                  [12]
gauge outer faces:       32 e_axis modulo 64            [3]
frame internal faces:    12 (D_a+D_b)                  [12]
frame outer faces:       32 (e_i+e_j) modulo 64         [3]
```

All 42 positions are distinct and form proper-cubic orbits.  At physical
`L=3`, a period-64 translation has active-set symmetric difference zero,
while a unit translation has difference 2268.

The period-64 origin, role labels, blank carriers, bounded routing, and
macro-gate synthesis are supplied.  This is coarse-translation covariance,
not a homogeneous unit-translation physical law.  The **macro-marker** remains
open.

## 8. Leakage, deletion, and lawful-domain controls

Ideal symmetric-qubit update leakage is zero on the declared joined code:
each `r,h` branch is intertwined by the compatible map, while the fixed
quantum controls preserve coherent `R/F` labels.

This must not be upgraded to physical CAR leakage.  Since no lawful global
ordinary-M2 CAR `E` was constructed, a CAR leakage residual is unavailable.

Deletion controls retain the failure:

- deleting one independent local charge-motion stabilizer lowers rank by one
  and adds one logical qubit;
- deleting the parity-Wilson join also lowers rank by one;
- deleting one local `h` control gives FSWAP residual
  `2.82842712475`; and
- no branch is projected away or silently postselected.

The full-rank code conditions commute and are phase consistent.  Malformed
charge or frame words violate their adjacent local combined-Gauss/flat checks
unless they represent one of the retained global logical sectors.

## 9. Mass and rank-73 seam firewall

The rank-complete joined code contains a slot of the correct total dimension,
including an odd sector.  That is not yet a physical CAR state isometry.

The runner retains the predecessor values:

```text
Cycle-219 rest value at Cycle-230 beta=-0.3: 0.4534056541748851
Cycle-219 rest/analytic mass ratio residual: below 2e-12
Cycle-230 principal sea rank:                73, odd
```

But it reports:

```text
ordinary-M2 CAR isometry:       unavailable
one-particle mass intertwining: not claimed
rank-73 seam intertwining:      not claimed
```

If the Cycle-245 matter carrier is left genuinely fermionic, its sector maps
remain conditional targets for those fixtures, but the target is then not the
requested ordinary-M2 compiler.  Cycle 252 does not blur that distinction.

## 10. Record and time firewall

`F_e` is a coherent local connection/sign carrier.  `R_v` is a coherent
charge-background carrier.  Neither is measured, actualized, permanent, or
readable here.  **Ancilla carriers are not Records.**

The orbit sums, controlled-sign gates, stabilizer schedules, macro routing,
and preparation depth are compiler resources.  **Compiler layers are not
physical time.**  No occurrence rule, probability, clock, duration, rate,
realized history, Record-formation law, or physical source is derived.

## 11. Supplied-structure inventory

The construction supplies or inherits:

1. the Cycle-235 square-pyramid dual graph and its proper-cubic framing;
2. one ordinary matter `M_2` role per pyramid vertex;
3. one Cycle-245 gauge `M_2` role per primal face/dual edge;
4. one new connection-frame `F_e` and one charge-frame `R_v` role;
5. product/coherent initialization adequate to define the `R/F` orbit;
6. the combined-Gauss, charge-move, frame-move, and local-flat stabilizers;
7. the three nonlocal parity/common-Wilson conditions;
8. a flat common-Wilson `000/111` sector relation;
9. the compatible symmetric-qubit observable map and its local controlled
   `h` signs;
10. the fixed Cycle-230 coin at `beta=-0.3` and its A/B FSWAP/contact order;
11. the period-64 macro origin, role layout, blanks, routing, and gate
    synthesis; and
12. the closed periodic boundary and tested size family.

The framework does not derive these in Cycle 252.  In particular, the current
axioms do not supply an update law, a CAR-to-M2 compiler, Wilson/parity state
preparation, a macro-marker, measurement, probability, or Record semantics.

## 12. Prior-art and novelty boundary

Cycle 245 supplies the exact sector gauging formula, local symmetric-observable
map, common-Wilson rank schema, marked-charge odd sector, and ordinary-matter
CAR warning.  Cycle 249 supplies the controlled-conjugation insight: retain a
quantum frame instead of selecting a classical representative.

Cycle 252 does not claim a new general gauging or fermionization theorem.  Its
fixture-specific content is:

1. the coherent `R/F` direct-sum formula;
2. the bounded stabilizers `C_v,K^R_e,K^F_v,L^F_c`;
3. the exact `6L^3+3` local-subsystem exponent and three-condition full-rank
   join through held-out `L=6`;
4. removal of the marked reference via a coherent charge orbit;
5. the exact migration of its cost to a weight-`6L^3+3L` parity-Wilson
   condition;
6. one fixed quantum `h`-controlled image of the actual gates;
7. the exact two-mode joined isometry and FSWAP fixture;
8. the repeated ordinary-M2 incident-CAR failure; and
9. the explicit 42-site proper-cubic macro placement and deletion controls.

No global novelty priority is claimed.  No Thirring machinery is used or
compared.

## 13. TOE dependency ledger after Cycle 252

| Workstream | Cycle-252 effect | Remaining dependency |
|---|---|---|
| `C_ref` | marked charge and classical `h=000/111` gate table are retired inside the coherent local subsystem | global parity-Wilson state, macro origin, physical sea, parameters, and realized preparation remain supplied |
| `C_num` | exact rank-complete even/odd common-Wilson code constructed | ordinary-M2 CAR state/algebra map and physical number/parity realization remain open |
| `C_wrap` | sharpened: exactly three Wilson logicals remain after all bounded local constraints; parity link has weight `6L^3+3L` | topological selection/preparation is not a clock, phase-unwrapping rule, or realized winding history |
| `C_int` | actual coin/A-B FSWAP/contact receive one bounded quantum `h`-controlled symmetric-qubit image | ordinary-M2 CAR update, rank-73 state, coupling/law selection, iteration, and physical rate remain open |
| `C_local` | strong gain: reference-free 42-role coherent subsystem, exact ranks, held-out L6, all translations/frames, and macro placement | three nonlocal joins, ordinary-M2 CAR, autonomous preparation, and unit-translation marker remain |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

Maturity scores remain operational quantum/records `2/5`, time `1/5`,
inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.
The rank-complete odd slot is a substantial compiler gain, but without a
lawful ordinary-M2 CAR `E` it does not advance the physical mass fixture.

## No-go discipline gate

The fresh `origin/main` no-go-discipline procedure and current primitive
registry were applied because this note names residual nonlocal and CAR
boundaries.

> **N1-N8 result: PASS for the narrow statement that the explicit promoted-h,
> coherent-charge-orbit ordinary-M2 family localizes the gate signs and
> removes the marked reference but still requires three topological joins and
> fails the incident-edge CAR test.  FAIL for a general auxiliary-fermion
> compiler no-go, a universal parity-Wilson preparation no-go, minimum content,
> shared substrate obstruction, or axiom pressure.**

### N1 — alternative routes

| Route | Honesty marker | Attempt and disposition |
|---|---|---|
| classical even-`000`/odd-`111` gate table | **ATTEMPTED** | replaced exactly by local quantum `F` controls; no longer load bearing |
| marked negative Gauss charge | **ATTEMPTED** | gives the Cycle-245 odd isometry but has a six-frame orbit and translation anchor |
| coherent charge-background orbit | **ATTEMPTED** | removes the marked reference with bounded `K^R_e`, but leaves global charge parity |
| local flat-connection frame orbit | **ATTEMPTED** | removes a preferred seam representative with bounded `K^F_v`, but leaves three Wilson logicals |
| three common-Wilson/parity joins | **ATTEMPTED** | restore exact full-Fock rank; supports grow as `6L,6L,6L^3+3L` |
| ordinary hard-core hopping with diagonal G/F dressings | **ATTEMPTED** | remains commuting on incident edges and fails CAR |
| Jordan-Wigner before gauging | **ATTEMPTED** | restores CAR semantics only with stream strings `6L^2` before bounded dressings |

All seven routes are distinct and executable in the finite runner.  Their
mixed successes block a broad negative.

### N2 — condition independence

Two raw conditions close and are removed from the wall count:

- `K_hstore`: local quantum sign storage is constructed;
- `K_reference`: a marked charge is avoided by the coherent `R` orbit.

The collapsed remaining conditions are:

- `K_CAR`: a local ordinary-M2 representation of the incident CAR algebra;
- `K_top`: the three common-Wilson/parity joins;
- `K_prep`: autonomous preparation of the joined code state;
- `K_marker`: homogeneous unit-translation physical roles; and
- `K_law`: selection of the actual coin/contact law and parameters.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---:|---:|---:|
| `K_CAR`,`K_top` | no | no | yes |
| `K_CAR`,`K_prep` | no | no | yes |
| `K_CAR`,`K_marker` | no | no | yes |
| `K_CAR`,`K_law` | no | no | yes |
| `K_top`,`K_prep` | no: code may be defined without prepared state | no | yes |
| `K_top`,`K_marker` | no | no | yes |
| `K_top`,`K_law` | no | no | yes |
| `K_prep`,`K_marker` | no | no | yes |
| `K_prep`,`K_law` | no | no | yes |
| `K_marker`,`K_law` | no | no | yes |

The three Wilson equations are one `K_top` family, not inflated into three
independent physics walls.

### N3 — hidden-condition scan

| Phrase or possible hidden condition | Classification |
|---|---|
| “coherent charge orbit” | explicit uniform orbit over fixed parity, not a measure or probability claim |
| “flat h” | explicit local `F`-cycle constraints plus three unresolved Wilson logicals |
| “reference free” | no selected vertex in the local code; global parity-Wilson relation remains explicit |
| “one fixed update” | fixed quantum-controlled symmetric-qubit image; not a completed CAR update |
| “ordinary M2” | tensor-qubit matter carriers, whose CAR failure is directly tested |
| “local” | bounded coarse-role support and period-64 placement; unit physical translation fails |
| “isometry” | exact two-mode fixture and global rank schema; no global ordinary-M2 CAR E claimed |
| “preparation” | code definition separated from autonomous state preparation |
| “Record” / “time” | explicitly not inferred from R/F carriers or compiler layers |

The required phrases “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical” were scanned.  Any
occurrences in the checklist are non-load-bearing; all actual inputs are in
the supplied-structure inventory.

### N4 — residual matching

| Witness | Exact residual there | Cycle-252 use | Match? |
|---|---|---|---:|
| `HAEGEMAN_PARITY_SECTOR_GAUGING_CYCLE245_NOTE_2026-07-17.md:54-82` | even/odd sector maps exist but use different h signs, marked charge, and common-Wilson resources | directly joins those sectors and separates all three resources | yes |
| Cycle-245 note `:36-44` and runner `:660-717` | ordinary matter qubits retain wrong CAR/JW strings | repeats after adding local F/R frames | yes |
| `COHERENT_GAUGE_FRAME_AUTONOMOUS_COMPILER_CYCLE249_NOTE_2026-07-17.md:46-74,262-279` | a quantum frame can replace deterministic sign selection | applies the same mechanism to h-dependent sector signs | yes |
| `EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md:66-107` | exact even-CAR face algebra and odd closed-code absence | used only as the incident-CAR comparison, not as the joined state map | yes, scoped |
| `SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md:32-106` | actual CAR update and rank-73 seam fixture | gates tested; seam withheld because joined CAR E is absent | yes |
| `ROUGH_TERMINAL_SUBSYSTEM_GAUGE_FACTORIZATION_CYCLE251_NOTE_2026-07-17.md:337,430` | rough-boundary/charge-sink and coherent routes remain target changes | alternative context only | no; not proof here |

The candidate-family CAR result is self-contained and does not borrow a
different no-go.

### N5 — resolution audit

| Resolution | Tested | Not established |
|---|---|---|
| one edge | exact coherent joined isometry, FSWAP, stabilizers | global CAR algebra |
| incident-edge pair | hard-core promoted-h commutator versus Cycle-235 CAR | every noncommuting auxiliary dressing |
| one onsite cell | actual coin/contact Pauli images and h-chain supports | selected physical law |
| one outer stream edge | actual FSWAP and h deletion | complete noisy implementation |
| `L=3,4,5` plus held-out `L=6` | ranks, JW strings, topology, covariance | thermodynamic theorem |
| all 24 proper frames | local paths, h cohomology, role placement, actual matrices | boosts/Lorentz closure |
| local code | 42-role bounded stabilizers | bounded preparation of topological joins |
| global joined rank | exact full-Fock exponent | lawful ordinary-M2 CAR E |
| physical lattice | period-64 collision-free placement | unit-translation autonomous marker |

The negative ships only for the displayed commuting promoted-h ordinary-qubit
operator family and the named JW ordering.

### N6 — partial-closure and primitive scan

The current minimal-axiom note, primitive registry, and the scale-reference,
kinetic-isotropy, and realized-state current paths were read.  Approved
premises chain-satisfy only their declared content; they are not walls or
bounded-status sources.  None supplies CAR fermionization, Wilson/parity
preparation, connection/charge frames, macro roles, dynamics, measurement,
probability, or Record formation.

Partial closures requiring no axiom edit are explicit:

| Path | Status | What it closes |
|---|---|---|
| local F frame | executable | classical h-dependent seam-sign table |
| coherent R charge orbit | executable | marked reference charge |
| retain three Wilson logicals as subsystem | executable | avoids pure-sector preparation when operationally acceptable |
| supply three topological resource constraints | exact conditional | full-Fock rank |
| find noncommuting local R/F logical dressing | live | may close ordinary-M2 CAR |
| use a rough boundary or charge sink | live target change | may alter parity/topology relation |
| autonomous macro-marker law | live | unit-translation role formation |

These are constructive/import-retirement paths.  No new axiom is required by
the evidence.

### N7 — steelman

> A hostile reviewer should reject any general compiler no-go.  Cycle 252 has
> already shown that two apparent global choices—the h sign table and marked
> charge—become bounded gauge redundancies after adding coherent local
> registers.  The remaining CAR failure tests only commuting diagonal F/R
> dressings of hard-core hopping.  A noncommuting auxiliary Pauli, subsystem
> gauge qubit, local Majorana-pair code, or rough-boundary charge sink could
> change the incident-edge algebra.  The three Wilson bits can remain logical
> subsystem degrees rather than be prepared as a pure common-parity state.
> Cycle 249 demonstrates that coherent conjugation can turn a classical sign
> family into one autonomous unitary.  Therefore the present result is a
> strong design discriminator, not evidence that ordinary-M2 fermionization
> or a full joined compiler is impossible.

This steelman is convincing and fixes the broad no-go result to FAIL.

### N8 — cross-cycle echo

The required repository phrase search and every physics-loop
`NO_GO_LEDGER.md` were scanned.  No ledger contains the exact coherent
charge-orbit/parity-Wilson/CAR residual.  Similar mechanisms were handled as:

| Earlier boundary | Retirement/live mechanism | Cycle-252 response |
|---|---|---|
| Cycle 244 deterministic sign inverse | retain quantum frame orbit | applied successfully to h signs |
| Cycle 245 marked odd charge | promote charge background to coherent local orbit | marked reference retired locally |
| Cycle 245 common-Wilson projector | expose topological logicals separately | exact three-condition rank audit |
| Cycle 246 auxiliary repetition bit | cat/global conjugate remains after local constraints | analogous parity-Wilson logical kept explicit |
| Cycle 249 pure affine coset | local subsystem leaves three Wilson qubits | same topology reappears in joined sector code |
| prior marker walls | proper-cubic macro orbit plus explicit marker | covariance retained without claiming marker formation |
| prior Record/time walls | pointers and circuit layers are not physical semantics | firewall retained |

The successful auxiliary-field retirements are incorporated, not ignored.
They are exactly why no broad negative or axiom conclusion is allowed.

## Route disposition and optimal next campaign

**Retain:** the 42-role reference-free coherent subsystem, bounded stabilizer
families, exact full-rank three-condition join, local h-controlled actual gate
images, exact two-mode joined FSWAP fixture, all-size/all-frame/macro tests,
and deletion controls.

**Reject as the requested final compiler:** the natural commuting promoted-h
ordinary-qubit operator family.  It has the wrong incident CAR algebra, while
its JW repair is nonlocal.  Do not claim mass or rank-73 seam preservation.

The optimal next campaign is an **incident-CAR auxiliary-dressing search on
the Cycle-252 stabilizer code**.  Enumerate bounded Pauli/Clifford dressings of
the hard-core edge generators using conjugate `R/F/G` operators, quotient by
the local stabilizers, and demand simultaneously:

1. exact CAR anticommutation for every one-endpoint overlap;
2. commutation for disjoint edges;
3. gauge-code preservation;
4. all 24 proper frames and translations;
5. bounded actual coin/A-B FSWAP/contact synthesis; and
6. no reintroduction of a marked reference or global order.

Only if that closes should the campaign return to autonomous preparation of
the three parity-Wilson correlations and the mass/rank-73 fixtures.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/coherent_even_odd_sector_join_cycle252_2026_07_17.py
```
