# Proper-cubic recoil-balanced carried source — Cycle 318

Date: 2026-07-18
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/proper_cubic_recoil_balanced_carried_source_cycle318_2026_07_18.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 318 constructs a proper-cubic direction-changing source vertex on the
unchanged Cycle-316 recurrent one-carrier physical code. Its local transition
channels are

```text
|E,d>  <->  |G,reverse(d); F,d>,       d in {+x,-x,+y,-y,+z,-z}.
```

The source vertex exactly conserves

```text
Q = N_source + N_field,
P = P_matter + 2 P_mediator,
[V,Q] = 0,
[V,P_axis] = 0 for axis x,y,z.
```

These are exact operator conservation statements on the full local
42-dimensional active space, not expectation-only cancellations. All four
commutators are literal zero in the runner. For every incoming direction, the
emission branch reverses the matter direction and emits the mediator along the
incoming direction. The matter recoil and weighted mediator flux cancel to
`1.11e-16` or better on every axis.

The physical recurrent compiler satisfies

```text
E_recoil G_recoil = G_physical,recoil E_recoil.
```

The maximum end-to-end residual is `9.86e-16` on `L=3,4` and held `L=6`.
No recoil M2 are added: the compiler retains the Cycle-316 total of 34
installed M2 per cell. Adjacent translated source blocks still share 14
physical pair rows; their order residual is zero and measured lawful-code
leakage is `3.27e-16`.

The exact result is a dimensionless direction/flux transfer ledger. The
relative mediator coefficient `2`, direction-reversing source vertex, coupling,
and source interpretation are supplied structure. It is not physical momentum,
not work, not energy, not stress, and not gravity. No energy calibration,
stress tensor, metric response, or operational generator identification is
claimed.

The comparator tournament also constructs a 222-dimensional local carried
link-reservoir vertex with a unit-weight ledger

```text
P_link = P_matter + P_mediator + P_aux.
```

It requires six extra auxiliary M2 per cell and has exact unitarity, Q/P
commutators, and all-frame covariance. Its recurrent auxiliary compiler is not
built, so it is a local counterroute rather than the retained physical
recurrent theorem.

## Exact local construction

Let `e_d` be the proper-cubic unit direction associated with port `d`. On the
excited branch define

```text
P_matter |E,d> = e_d |E,d>,
P_mediator |E,d> = 0.
```

On a ground matter plus mediator basis state define

```text
P_matter |G,m;F,f> = e_m |G,m;F,f>,
P_mediator |G,m;F,f> = e_f |G,m;F,f>.
```

For each active source transition, `m=reverse(d)` and `f=d`. Therefore

```text
e_reverse(d) + 2 e_d = -e_d + 2 e_d = e_d.
```

The exchange matrix is

```text
T_recoil = sum_d ( |G,reverse(d);F,d><E,d| + h.c. ),
V_recoil(theta) = exp(+i theta T_recoil).
```

The six channels are mutually orthogonal two-dimensional rotations. The
executed local controls are:

| control | residual |
|---|---:|
| unitarity of `V_recoil` | `0` |
| `[V_recoil,Q]` | `0` |
| `[V_recoil,P_x]` | `0` |
| `[V_recoil,P_y]` | `0` |
| `[V_recoil,P_z]` | `0` |
| maximum 24-frame covariance | `0` |

For the chosen angle, `sin(theta)^2 = 0.1258992161287137`. On an incoming
direction eigenstate the matter-vector change has magnitude
`2 sin(theta)^2 = 0.2517984322574275`, while the weighted mediator flux has the
opposite vector. This is a nonzero recoil/current response rather than a zero
mean scalar fixture.

The relative coefficient two is load-bearing. Replacing it by one gives an
operator commutator `0.709645590780958`; that deletion is executed. Nothing in
this cycle derives the relative coefficient from energy, wavelength, a clock,
or a translation generator.

## Three-route tournament

| route | local result | recurrent result | disposition |
|---|---|---|---|
| Cycle-316 direction-preserving scalar source | exact Q, but unit-weight vector commutator `0.7214786377822061` on every axis | retained Cycle-316 recurrence | falsifies this particular vector candidate |
| carried six-link reservoir | exact unit-weight Q/P with local dimension 222, six added M2, and frame residual zero | auxiliary coin/stream/catch-up compiler not assembled | constructive local counterroute, recurrence open |
| direction-changing matter | exact Q and `P_matter+2P_mediator`, active dimension 42, no added M2 | full Cycle-316 physical recurrence compiled through held `L=6` | strongest result |

The current direction-preserving route fails because it keeps matter direction
fixed while creating directional mediator occupation. The link route cancels
each mediator direction with a carried opposite auxiliary direction. The
direction-changing route instead flips matter and assigns the mediator twice
the direction-unit weight. These are distinct mechanisms, not three labels for
one construction.

A unit-weight rest-mode route remains open. A final matter rest state with a
mediator in direction `d` would conserve `e_d` without the factor two, but the
Cycle-312/316 matter compiler has no physical rest column. A paired-mediator
branch also remains open.

## Physical recurrent compiler

Cycle 318 keeps the Cycle-316 encoding exactly:

```text
excited:
    E_312 |x,d> tensor |port=x,d> tensor |source=x> tensor |field vacuum>,

ground plus mediator:
    E_312 |x,m> tensor |port=x,m> tensor |source vacuum>
                    tensor |field=y,f>.
```

At every cell, the physical source factor is the bounded identity completion

```text
L_x(V_recoil) = I + Phi_x (V_recoil-I) Phi_x^dagger,
```

where `Phi_x` contains the six excited columns and 36 onsite
ground-plus-field columns. The same source factor is applied at every cell.
No state-dependent selector and no host carrier query occurs.

The update order remains:

```text
matter and field coins;
homogeneous onsite recoil-source blocks;
Cycle-312 reverse/edge matter stream with source/tag catch-up;
directional mediator stream.
```

The cold end-to-end table is:

| L | status | matter Gram | common-update residual | largest local P residual |
|---:|---|---:|---:|---:|
| 3 | training | `4.45e-16` | `9.86e-16` | `1.39e-17` |
| 4 | training | `4.45e-16` | `8.74e-16` | `2.41e-17` |
| 6 | held | `4.45e-16` | `9.12e-16` | `2.09e-17` |

The finite-volume fixtures include coherent excited amplitudes, onsite
ground/mediator amplitudes, and separated mediator amplitudes. They exercise
source blocks at multiple cells and both source sectors.

## Emission, transport, and absorption

An initially excited proper-cubic scalar matter state emits total mediator
occupation `0.1258992161287138`. After the physical mediator stream, each of
the six neighboring cells receives `sin(theta)^2/6`; the maximum directional
error is `6.94e-18`. The source-plus-matter-plus-field physical stream agrees
with the encoded logical stream to `5.43e-16` on `L=3,4,6`.

The conjugate local input

```text
sum_d |G,reverse(d);F,d> / sqrt(6)
```

restores source occupation `0.1258992161287138` and leaves mediator occupation
`0.8741007838712865`. This proves the absorption channel is present. It does
not prove that a generic forward wavepacket returns and reabsorbs after a
finite number of updates.

The emitted matter branch and mediator stream in opposite spatial directions:
matter follows `reverse(d)` and the mediator follows `d`. The surviving
excited branch follows `d`. The physical source block changes the relational
matter port coherently before the existing reverse/edge stream moves the port
and source tag. Source/tag catch-up plus transport has residual `5.43e-16`.
Leaving a translated excited tag behind produces unit leakage. The executor
applies the source block at every cell and performs zero host carrier-cell
queries.

## Overlap, frames, translations, and held sizes

Adjacent source cells inherit the actual Cycle-312 coefficient patches. Each
patch touches 36 pair rows and the two patches share 14 rows. On the tagged
code:

| overlap control | result |
|---|---:|
| shared physical pair rows | `14` |
| opposite source-block order residual | `0` |
| measured lawful-code leakage | `3.27e-16` |

The full source, coin, matter-stream, and mediator-stream update is tested in
all 24 proper-cubic frames; the maximum residual is `2.12e-16`. All L=3
translations (27 origins) have zero residual. `L=6` is held out.

The strongest route adds zero M2. It retains 34 installed M2 per cell, a
42-dimensional source block, at most 36 physical pair rows per inherited local
block, and the supplied Cycle-312 216-M2 patch envelope. These are observed
constant envelopes, not a minimum-content theorem.

The link-reservoir comparator would raise the installed count to 40 M2 per
cell. Its local dimension is 222: six excited states plus `6^3` matter,
mediator, and auxiliary direction labels. Exact local algebra does not stand
in for the missing recurrent auxiliary compiler.

## Mass firewall, contact firewall, deletions, and lawful domain

The mass firewall is deliberately source-off. At zero source coupling the new
vertex is identity and the inherited Cycle-219 one-particle fixture remains:

| L | source-off mass fixture |
|---:|---:|
| 3 | `0.4534056541748850` |
| 4 | `0.4534056541748858` |
| 6 held | `0.4534056541748896` |

The interacting direction/flux ledger is not converted into a mass shift.

The contact firewall is also strict. The declared code contains exactly one
matter carrier, makes zero Cycle-230 contact calls, and cannot fire a
multiparticle contact. Recurrent contact, simultaneous carriers, and a
full-Fock source remain open.

Executed deletions and lawful-domain controls are:

- source coupling set to zero: vertex identity residual `0`;
- conjugate half removed: unitarity residual `1.297185990748149`;
- relative mediator weight changed from two to one: P-commutator
  `0.709645590780958`;
- source/port catch-up deleted: code leakage `1`;
- `L<3`, two carriers, wrong Q, and mismatched tags: four rejections.

## Supplied, derived, and open inventory

Supplied structure:

- the Cycle-316 one-carrier, prepared-Q1 tagged physical code;
- the Cycle-219 matter coin and Cycle-312 bounded block grammar;
- six direction-reversing source channels;
- coupling `theta = 0.8 m_fixture`;
- unit matter direction and twice-unit mediator direction in the P ledger;
- the factor schedule and identity completion outside each encoded block;
- response observables and finite periodic test volumes.

Derived here:

- exact local operator Q and vector commutators;
- nonzero matter recoil balanced by mediator flux;
- exact physical-code recurrence through held `L=6`;
- emission, mediator transport, conjugate absorption, and tag transport;
- 14-row overlap compatibility, frame covariance, translation covariance, and
  deletion residuals.

Open:

- derivation or operational calibration of the relative coefficient two;
- a recurrent carried link-reservoir compiler;
- a physical matter rest mode or paired-mediator alternative;
- simultaneous matter carriers, recurrent contact, and full Fock;
- same-code two-source response and reciprocity;
- physical momentum, work, energy, stress, metric, gravity, and time.

## TOE dependency ledger and maturity

| wall | Cycle-318 effect | remaining import |
|---|---|---|
| `C_ref` | unchanged | fixed reference sector, prepared one-carrier/Q1 sector, and response readout supplied |
| `C_num` | unchanged | simultaneous carriers, higher Fock, cross-number reference, and local sector preparation |
| `C_wrap` | unchanged | update count and factor schedule are not clock time or rate |
| `C_int` | a proper-cubic direction-changing source vertex with exact local Q/vector transfer now shares the recurrent physical code | coefficient, coupling, recurrent contact, multiparticle extension, and operational calibration supplied/open |
| `C_local` | unchanged constructive one-carrier recurrence; source blocks preserve the 14-row translated overlap | multiparticle overlap, primitive factor synthesis, recurrent contact, and full Fock |
| `C_source` | exact operator-level dimensionless matter/mediator recoil-transfer ledger added | source identity, coefficient, energy/stress normalization, tensor, and metric response |

The kinematic operator ledger supports a conservative gravity/source planning
bump because source transfer and recoil now coexist on the physical recurrent
code. It does not retire the energy/stress/metric imports.

| lane | integrated | strict floor | conditional | maturity |
|---|---:|---:|---:|---:|
| operational quantum / Records | 61% | 27% | 87% | 3.2/5 |
| causal time / clock | 34% | 17% | 62% | 1.8/5 |
| inertia / matter | 71% | 32% | 92% | 3.8/5 |
| gravity / source / resource | 39% | 16% | 65% | 2.0/5 |
| Born / probability / realized history | 33% | 14% | 82% | 1.8/5 |

The coarser campaign values remain operational quantum/records `2/5`, time
`1/5`, inertia/matter `3/5`, gravity/source `2/5`, and Born/probability `1/5`.

## No-Go Discipline Gate

The broad candidate negative is that no bounded proper-cubic local enlargement
can balance source emission as an operator vector law on the recurrent
one-carrier code. Cycle 318 supplies one recurrent counterexample and one
independent local link-reservoir counterroute. Any broader impossibility,
minimum-content, or axiom-pressure claim is premature.

Gate status: **FAIL / DO NOT SHIP** the broad negative. There is no shared
obstruction and no axiom pressure.

### N1 — alternative routes

| route | marker | actual disposition |
|---|---|---|
| Cycle-316 direction-preserving scalar vertex | **ATTEMPTED** | exact Q but the unit-weight vector commutator is `0.721479` on each axis |
| carried six-link reservoir vertex | **ATTEMPTED** | exact local unit-weight Q/P with six auxiliary M2; recurrent auxiliary compiler remains open |
| direction-changing weighted-flux vertex | **ATTEMPTED** | exact operator Q/P and full recurrent physical compiler through held `L=6` |
| unit-weight matter-rest vertex | **OPEN / UNTESTED** | a rest output could remove the factor two, but no Cycle-312/316 rest column is constructed |
| paired-mediator recoil branch | **OPEN / UNTESTED** | a bounded two-mediator channel could alter the integer flux balance; no such source sector is compiled |
| simultaneous-carrier recoil/contact splice | **OPEN / UNTESTED** | the retained theorem has one carrier and cannot exercise Cycle-230 contact |
| energy-calibrated stress/source law | **OPEN / UNTESTED** | no operational energy or stress normalization is selected |

The three requested routes are compared directly. Four broader constructive
routes remain open, so N1 blocks any universal negative.

### N2 — wall-independence audit

For a stronger physical source theorem, the collapsed walls are:

- `W_flux_norm`: derive or operationally select the relative vector weight;
- `W_energy`: identify conserved operational energy/stress and source coupling;
- `W_multi`: extend the physical code to simultaneous matter carriers;
- `W_contact`: compile recurrent multiparticle contact on that code;
- `W_pair`: realize two matter sources and same-code reciprocity.

The complete directed-pair audit is:

| pair | closing first automatically closes second? | closing second automatically closes first? | independent? |
|---|---|---|---|
| `W_flux_norm`, `W_energy` | no | no | yes |
| `W_flux_norm`, `W_multi` | no | no | yes |
| `W_flux_norm`, `W_contact` | no | no | yes |
| `W_flux_norm`, `W_pair` | no | no | yes |
| `W_energy`, `W_multi` | no | no | yes |
| `W_energy`, `W_contact` | no | no | yes |
| `W_energy`, `W_pair` | no | no | yes |
| `W_multi`, `W_contact` | no | no | yes |
| `W_multi`, `W_pair` | no | no | yes |
| `W_contact`, `W_pair` | no | no | yes |

A vector normalization need not be an energy normalization. A multiparticle
code need not choose a contact, and a contact need not produce two separated
matter sources. No directed implication collapses another wall.

### N3 — hidden-wall scan

The executable literal scan covers this note and the runner and returns zero
hits. Load-bearing choices appear in the supplied inventory: the one-carrier
sector, Q1 preparation, vertex, relative coefficient, coupling, factor
schedule, identity completion, and observables.

### N4 — residual matching

| exact witness | witness residual | Cycle-318 use | match? |
|---|---|---|---|
| `CARRIED_SOURCE_RECURRENT_TAGGED_BLOCK_CYCLE316_NOTE_2026-07-18.md:70` | direction-preserving vertex has no matter recoil | comparator route using that exact 42-state vertex | yes |
| same file, line 156 | 14-row overlap leakage control | inherited translated-block overlap | yes |
| same file, line 171 | simultaneous carriers outside the code | Cycle-318 multiparticle boundary | yes |
| `PHYSICAL_CYCLE269_LOCAL_FOCK_EXTENSION_CYCLE312_NOTE_2026-07-18.md:171` | simultaneous translated patches open | recurrent higher-number boundary | yes |
| `CARRIED_INTERNAL_SPECIES_SOURCE_FIELD_LEDGER_REPAIR_NOTE_2026-07-17.md:41` | Q ledger is not energy/stress/gravity | interpretation firewall for the inherited source sector | yes |

No failed local vector candidate is cited against an enlarged vertex. The
link and rest routes remain constructive alternatives.

### N5 — rhetoric audit

The phrase “not physical momentum” means only that the diagonal local vector
operator lacks an operational calibration and translation-generator theorem.
The runner tests the local 42-state operator, bounded physical source blocks,
and finite periodic one-carrier recurrence. It does not test a multiparticle
generator, continuum stress tensor, or scattering calibration. The statement
is therefore an interpretation firewall, not a lattice-wide impossibility.

The direction-preserving no-recoil statement is tested only for the retained
Cycle-316 42-state vertex. Cycle 318 gives an explicit enlarged-law
counterexample on the same state dimension. No statement against all local
vertices survives.

The contact boundary is one-carrier and per-code. It is not a negative result
about Cycle-230’s fixed seam or every higher-number compiler.

### N6 — partial-closure paths

Five live import-retirement paths remain:

- calibrate the relative vector weight with a retained operational generator;
- compile the six-link auxiliary label through matter and field coins;
- add a bounded physical matter-rest column;
- compile the Cycle-311 higher-number seam across translated overlaps;
- build two carried matter sources and test response reciprocity.

Each path would close a named import without implying a new axiom. No axiom
language is drafted.

### N7 — hostile steelman

A hostile reviewer should reject any minimum-content claim immediately. The
coefficient-two construction already shows that no new M2 is required if a
weighted direction ledger is allowed, while the six-link construction shows
that unit weights can be retained with bounded auxiliary support. A matter
rest column or paired mediator could combine unit weights with direct matter
recoil. Cycle 312 also leaves higher-number block completions open. The
evidence supports a constructive kinematic theorem, not a unique source law or
an impossibility boundary.

### N8 — cross-cycle echo

Earlier walls in this campaign were retired by changing the representation at
the exact residual:

- Cycle 295 moved source capacity with matter rather than leaving a fixed
  defect;
- Cycle 312 replaced a volume-wide one-carrier projector by bounded encoded
  blocks;
- Cycle 313 put source response on the physical M2 seam;
- Cycle 316 joined carried source response to the recurrent tagged code;
- Cycle 318 changes the source channels and vector normalization at the local
  operator residual.

The same mechanism remains available for the rest, link, multiparticle, and
calibration walls. The broad gate stays **FAIL / DO NOT SHIP**.

## Optimal next campaign

The sharpest next source campaign is a unit-normalization discriminator.
Compile either a matter-rest output or the six-link auxiliary route through the
full recurrent physical schedule, then compare it with the coefficient-two
direction-changing theorem using the same emission, absorption, overlap,
deletion, all-frame, translation, and held-size controls. The goal is to learn
whether unit direction weights can coexist with direct matter recoil without
an imported coefficient.

In parallel, the higher-value framework wall remains the simultaneous-carrier
compiler: only that lane can bring recurrent Cycle-230 contact, two matter
sources, and same-code reciprocity into the source/recoil theorem.
