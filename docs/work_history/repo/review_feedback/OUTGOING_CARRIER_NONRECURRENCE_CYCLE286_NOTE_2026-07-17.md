# Outgoing-carrier nonrecurrence route — Cycle 286

**Date:** 2026-07-17

**Type:** exact bounded-per-step open-rail continuation of the Cycle-282 same
connected-code apparatus and Cycle-281 positive close

**Status:** positive finite-horizon nonreturn construction on a supplied open
rail; rail genesis, origin, blank capacity, forward-only continuation, and
boundary remain supplied; inverse reconnection and bounded retargeting remain
possible outside that continuation domain

**Authority: none**

**Audit: unset**

**Constitutional effect: none**

Companion runner:

```text
scripts/outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py
```

This cycle creates exactly this note and runner. It changes no axiom,
foundation, Qualification, primitive, registry, policy, queue, or audit
surface. It neither stages nor packages any file and does not use the
Cycle-251 splice.

## Result up front

Cycle 286 replaces Cycle 282's finite cyclic token/fact storage with an open
non-wrapping rail. One repeated bounded local update moves a physical one-hot
program token rightward, reads the physical role marker at its current slice,
and executes the Cycle-281 positive-close echo:

```text
INIT -> WRITE(Q_x) -> ARCHIVE(pointer) -> RESET(Q_x) -> LAUNCH -> FORWARD ...
```

The positive close is not left in a finite core register. `LAUNCH` moves the
verified archive value into a synchronized outgoing carrier frontier. Every
later composition deposits one coherent fact copy on the departing fresh
slice and shifts both program and fact frontiers to the next fresh slice. No
host chooses a different role at different compositions.

For the actual Cycle-278 contact-active projector

```text
Q_x = 1_(N_x >= 2),
```

the complete outgoing-carrier effect is exactly `Q_x`, of intrinsic rank 57,
and exactly equals the Cycle-281 positive close effect. Deleting any of
`INIT`, `WRITE`, `ARCHIVE`, `RESET`, or `LAUNCH`, or deleting both
`Q_x`-controlled pointer calls, leaves zero outgoing-fact support.

On the declared forward fresh-target domain, the rail does what the cyclic
Cycle-282 register could not:

- the program token never revisits a slice before the boundary;
- the positive frontier never returns;
- every full state in the tested history is distinct;
- once a fact site is written, later intended forward updates never target
  it; and
- no wrap is defined at the finite boundary.

Training rail lengths/horizons are

```text
(R,h) = (12,10), (19,17), (28,26),
```

and the held-out rail length/horizon is `(43,42)`. The held positive branch
writes 38 stable fact sites and leaves the frontier at slice 42. All 43 states
from composition zero through 42 are unique on both contact branches.

This is exact finite-horizon nonreturn, not unrestricted permanence. An exact
reverse reconnection erases the complete trail and restores all apparatus
blanks. An adjacent bounded reversible retarget gate can erase and restore the
newest old fact. Old facts are controls only under the intended forward
continuation grammar; they are not protected against every bounded local law.

The outgoing carrier remains blind to deletion of the actual Cycle-230
contact phase `W_g`: `W_g` differs from identity, but it commutes with `Q_x`,
so the carrier effect is unchanged. Thus the construction retains
Cycle-281's deletion faithfulness for the two declared `Q_x` couplings but
does not certify application of `W_g` itself.

The result is an exact **outgoing coherent positive-contact carrier with
finite-horizon nonreturn**. The carrier is not a Record. Step count is not
physical time. There is no route-independent obstruction and no axiom
pressure.

## 1. One repeated open-rail update

Each rail slice carries six ordinary physical M2 roles:

```text
program-token bit T_i,
fact-frontier bit K_i,
deposited fact bit H_i,
three immutable role-marker bits R_i.
```

The bounded core has three working bits:

```text
ready r, pointer p, archive a.
```

The first five marker values are `INIT`, `WRITE`, `ARCHIVE`, `RESET`, and
`LAUNCH`; all remaining sites carry `FORWARD`. Starting from the supplied
blank interface and token at slice zero, the role gates are

```text
INIT:     r <- r xor 1
WRITE:    p <- p xor q                  if r=1
ARCHIVE:  a <- a xor p                  if r=1
RESET:    p <- p xor q                  if r=1
LAUNCH:   SWAP(a,K_i)                   if r=1 and p=0.
```

After the local role gate, the same update applies

```text
H_i     <- H_i xor K_i,
SWAP(K_i,K_(i+1)),
SWAP(T_i,T_(i+1)).
```

Freshness requires the outbound targets to be zero. The complete map is a
permutation on its declared synchronized fresh-target domain. The runner
exhausts 256 local basis cases across all pre-boundary roles and both values
of `q`, then applies the exact inverse and recovers every input.

This computational-basis permutation extends linearly to a unitary on the
declared quantum subspace. A superposition across `Q_x=0,1` remains a coherent
entangled state; no branch is selected.

`INIT` arms a supplied blank pointer. It is not a reversible reset from an
arbitrary pointer state. The unique one-hot token and first role site supply
the origin; the law does not generate them from homogeneous data.

## 2. Exact Cycle-281 positive close inheritance

Cycle 281 used the same physical pointer twice:

```text
U_I(write) -> CNOT(pointer,archive) -> U_I(reset)
            -> positive agreement close.
```

Cycle 286 keeps the same positive agreement condition but moves the archive
itself into the outgoing frontier. On `q=1`, the exact core path is

| stage | pointer `p` | archive `a` | frontier `K` |
|---|---:|---:|---:|
| blank/armed | 0 | 0 | 0 |
| WRITE | 1 | 0 | 0 |
| ARCHIVE | 1 | 1 | 0 |
| RESET | 0 | 1 | 0 |
| LAUNCH | 0 | 0 | 1 |

On `q=0`, pointer, archive, and frontier remain zero. Therefore the core is
clean after launch and the outbound effect is exactly

```text
V_out^dag 1_(K=1) V_out = Q_x.
```

The runner independently constructs the Cycle-281 64-column isometry and
checks

```text
||E_close^(281)-Q_x||_F = 0,
||E_out^(286)-Q_x||_F   = 0.
```

The outgoing rank is 57. This is the Cycle-281 positive close, not the
Cycle-282 split-coupling false `NO` close. No negative-contact fact is written:
silence on `Q_x=0` remains silence.

## 3. Training, held-out, and exact nonreturn

For every tested `(R,h)`, both `q=0` and `q=1` histories satisfy

```text
token positions = (0,1,...,h),
number of distinct complete states = h+1.
```

On the positive branch at horizon `h>=5`, the deposited fact set is exactly

```text
{4,5,...,h-1},
```

the frontier is exactly at `h`, and pointer/archive are zero. On the inactive
branch no fact or frontier is present, but the moving physical program token
still makes every complete state distinct.

| split | rail `R` | horizon `h` | positive fact sites | complete states | repeats |
|---|---:|---:|---:|---:|---:|
| training | 12 | 10 | 6 | 11 | 0 |
| training | 19 | 17 | 13 | 18 | 0 |
| training | 28 | 26 | 22 | 27 | 0 |
| held-out | 43 | 42 | 38 | 43 | 0 |

This is exact nonreturn before boundary, not a statistical recurrence search.
The proof is constructive: the one-hot token index strictly increases on the
declared open interval and the fact support is a strict prefix invariant on
the positive branch.

At token position `R-1`, the next update raises a lawful boundary error. It
does not wrap to zero, overwrite an occupied target, or silently add a new
site. The boundary is a supplied domain restriction, not an absorbing
dynamical theorem.

## 4. Bounded support and fresh-capacity growth

For rail length `R`, the resource count is

```text
apparatus M2              = 6 R + 3,
matter plus apparatus M2  = 6 R + 21,
positive deposited capacity = R - 5.
```

The 18 matter M2 are the same connected-code support union as Cycles 278,
281, and 282. The three core bits are `r,p,a`. Each extra slice adds six
physical M2 and one usable post-launch fact site.

The maximum per-step support is 29 M2:

```text
18 matter
+ 3 core
+ 2 program-token sites
+ 2 fact-frontier sites
+ 1 deposited-fact target
+ 3 role-marker bits
= 29.
```

Thus bounded per-step support remains constant while total fresh-capacity
growth is linear. No finite `R` is called an infinite tape. No M2 count is
called physical energy, entropy, stress, or gravity source.

At held-out `R=43`, the apparatus contains 261 M2 and the combined
matter/apparatus block contains 279 M2. These are explicit supplied resources,
not a derivation of their preparation cost.

## 5. Collision and proper-cubic covariance audit

The supplied rail has a six-site cross-section and three longitudinal nearest-
neighbor lanes for token, frontier, and facts. All route coordinates are
distinct. Merging the token and frontier lanes deliberately produces exactly
43 collisions on the held rail and is rejected. An occupied fact target is
also rejected by the update rather than XOR-overwritten.

For the held rail, every one of the all 24 proper-cubic frames is combined
with 27 integer translations. All 648 carried-motif tests preserve:

- the number of physical route sites;
- collision freedom;
- the complete longitudinal edge-distance multiset; and
- the scalar meanings of program, positive carrier, fact, and role data.

Separately, the connected-code `Q_x` family passes all 24 frames combined
with the full 27-element `L=3` translation group. The local-check family and
Wilson center are preserved exactly.

This is carried covariance of a supplied oriented apparatus. It does not
derive the rail orientation, its origin, or collision-free placement relative
to every other apparatus from one homogeneous microscopic law.

## 6. Deletion faithfulness and actual `W_g` blindness

The complete 64-state intrinsic effect is rebuilt after each role deletion:

| deleted role | outgoing-effect Frobenius norm |
|---|---:|
| `INIT` | 0 |
| `WRITE` | 0 |
| `ARCHIVE` | 0 |
| `RESET` | 0 |
| `LAUNCH` | 0 |
| both `WRITE` and `RESET` | 0 |

This preserves Cycle-281 deletion faithfulness. Deleting the first coupling
leaves the second to make the pointer nonzero, blocking launch. Deleting the
second leaves the written pointer nonzero, also blocking launch. Deleting
both leaves no archive value to launch.

The stronger physical-event claim fails a different control. With the actual
Cycle-230 fixture `g=0.37`,

```text
||W_g-I||_F = 9.750456122278623,
[Q_x,W_g]   = 0,
||W_g^dag Q_x W_g - Q_x||_F = 0.
```

Therefore deleting `W_g` changes the physical matter operator but not the
outgoing-carrier effect. The carrier certifies the two declared `Q_x`
pointer couplings on their omission grammar. It does not certify that the
contact phase itself was applied. An indivisible `W_g`-plus-syndrome update
remains a live constructive route.

The actual one-particle fixture remains protected because `Q_x=0` for
`N_x<=1`.

## 7. Old facts, retargeting, and reverse reconnection

Within the intended forward rule, a site `H_i` is targeted once when the
frontier departs slice `i`, then never targeted again. A controls-only export
from the newest old fact to a fresh probe leaves that old fact unchanged.
All tested earlier prefixes are exact invariants under every later intended
forward step.

This protection is conditional. At a state with frontier `K_i=1` and adjacent
old fact `H_(i-1)=1`, the bounded reversible gate

```text
H_(i-1) <- H_(i-1) xor K_i
```

erases the old fact. Applying the same gate again restores it. The retarget
gate is not in the intended update, but it is local and reversible. Therefore
the fact is not protected under an unrestricted local-gate grammar.

The exact inverse of the entire forward update gives the stronger global
control. At every training and held-out horizon, applying the inverse `h`
times:

- moves token and frontier back to their origin;
- erases each deposited fact in reverse order;
- undoes launch, reset, archive, write, and initialization; and
- restores all working and rail registers to the supplied blank.

On the held positive branch the reverse fact counts begin `38,37,36,...` and
finish at zero. Reverse reconnection residual is exactly zero on every tested
case.

Outgoing separation therefore removes recurrence only on the declared
forward fresh-target domain. It does not make coherent carriers permanently
unerasable.

## 8. Same connected code and state controls

The construction leaves the Cycle-269/271/275/278 connected edge code
unchanged. For `L=3,4,5` and held-out `L=6`, it rebuilds all eight fixed-Wilson
sector projectors and their two `B_0`-biased families: 24 rows per size.

Every row is consistent and reproduces the exact positive-carrier weights

```text
57/64, 13/16, 31/32.
```

All 64 Walsh words commute with every bounded local check and all Wilson
operators. Local-check/Wilson leakage is zero at all four sizes, and the
matter support union remains 18 M2.

These are coherent trace weights on supplied physical density operators. They
are not selected occurrences, Born frequencies, or an actual-history law.

## 9. Origin, rail, blanks, and boundary inventory

The complete supplied-structure ledger is:

| supplied structure | use | not derived here |
|---|---|---|
| Cycle-278 same connected code and `Q_x` | physical positive-contact control | microscopic selection/preparation of that instrument |
| Cycle-281 positive close grammar | deletion-faithful write/archive/reset ancestry | arbitrary-fault or `W_g`-application certificate |
| open six-lane M2 rail | outward carrier and deposited facts | genesis or indefinite extension |
| three-bit role marker at every slice | selects the local gate under one update | homogeneous role-texture generation |
| unique token at slice zero | physical program origin | origin selection by the law |
| blank pointer/archive/frontier/fact targets | reversible dilation and capacity | blank preparation or reset cost |
| rail orientation and collision-free placement | spatial apparatus embedding | unique preferred-direction-free genesis |
| one repeated local permutation | forward propagation | selection from a deeper microscopic law |
| forward fresh-target continuation grammar | leaves old facts off target lists | restriction of every lawful future |
| finite endpoint and boundary rejection | prevents wrap in tested domain | absorbing boundary or renewal law |
| exact inverse and adversarial retarget gates | stress controls | a claim that these are intended future dynamics |
| trace/effect pairing | reports exact coherent weights | physical read, occurrence, or Born frequency |

This is the requested inventory of origin, rail, blanks, and boundary. No
supplied item is renamed as a Record or causal-time law.

## 10. Record and time firewalls

The deposited `H_i` bits and moving frontier are coherent carriers. No
actual branch is selected; no commit or Record-formation map is present; and
the exact inverse can erase the entire packet. The carrier is not a Record.
A controls-only future is compatible with stable facts, but that future is a
supplied grammar, not lawful Record typing.

The strict order

```text
write -> archive -> reset -> launch -> outward propagation
```

is update ancestry. It supplies no duration, clock reading, waiting time, or
rate. Rail distance and archive count are not elapsed time. Step count is not
physical time.

The Cycle-170/243/255 receiving endpoint still requires actual Records and a
Record-dependency graph before causal depth can be interpreted. Nothing in
this cycle creates that graph.

## 11. Prior-art and novelty boundary

Moving program heads, reversible computation, quantum cellular automata, and
coherent copy trails are established constructions. Relevant bounded prior
art includes:

- P. Benioff, “The computer as a physical system,” *Journal of Statistical
  Physics* **22**, 563–591 (1980), DOI `10.1007/BF01011339`;
- R. P. Feynman, “Quantum mechanical computers,” *Optics News* **11**(2),
  11–20 (1985), DOI `10.1364/ON.11.2.000011`; and
- B. Schumacher and R. F. Werner, “Reversible quantum cellular automata,”
  arXiv `quant-ph/0405174`, published as *Physical Review A* **70**, 022317
  (2004), DOI `10.1103/PhysRevA.70.022317`.

No novelty is claimed for an open program tape, moving front, reversible
copy, or cellular update. The repo-local result is the exact integration of
an open nonreturning carrier with the Cycle-281 deletion-faithful positive
close on the Cycle-278 connected physical-M2 code, including held rail/code
sizes, all-24 covariance, collision and boundary controls, precise resource
growth, actual-`W_g` blindness, and exact reverse/retarget countercontrols.

## 12. Full N1–N8 no-go discipline

The main result is constructive. The only negative boundaries are scoped to
the tested finite rails, the actual `Q_x` carrier, and the displayed forward
or unrestricted reversible domains. No impossibility or minimum-content
claim is shipped.

### N1 — Alternative-route enumeration

| route | honesty marker | disposition |
|---|---|---|
| Cycle-282 cyclic token continuation | **RULED OUT BY PRIOR** — Cycle 282, lines 260–287 | exact close forms, but the packet changes at composition 28 and close is lost at 55 |
| open non-wrapping token/frontier | **ATTEMPTED** | succeeds with exact nonreturn on all training and held horizons |
| held rail beyond training lengths | **ATTEMPTED** | `R=43,h=42` gives 43 unique states and 38 stable positive facts |
| wrap or occupied-target continuation | **ATTEMPTED** | rejected explicitly at the boundary rather than treated as append |
| Cycle-281 positive-close deletion grammar | **ATTEMPTED** | every declared core-role deletion gives zero outbound effect |
| actual `W_g` deletion | **ATTEMPTED** | outbound effect is unchanged; the stronger contact-occurrence reading fails on this route |
| controls-only export from an old fact | **ATTEMPTED** | fresh probe changes while the old fact remains one |
| adjacent old-fact retarget | **ATTEMPTED** | bounded XOR erases and restores the old fact; unrestricted protection fails |
| exact inverse reconnection | **ATTEMPTED** | erases every fact and restores the complete blank at all horizons |
| merged token/frontier geometry | **ATTEMPTED** | produces one collision per held slice and is rejected |

Live untested routes include a law-generated infinite rail, an absorbing
Record-typed sector, an indivisible `W_g`/syndrome transition, and local
renewal/compression. The successful open route and those live repairs make a
broad no-go premature.

### N2 — Wall-independence audit

The raw conditions collapse to five:

```text
K_gen    = rail, orientation, origin, markers, and blanks are supplied,
K_cap    = indefinite fresh capacity or renewal is not derived,
K_future = old-fact no-target behavior is a supplied forward grammar,
K_event  = the carrier is blind to actual W_g application,
K_record = no actuality, lawful Record formation, or permanent type exists.
```

| pair | first closes second? | second closes first? | independent here? |
|---|---:|---:|---:|
| `K_gen/K_cap` | no | no | yes |
| `K_gen/K_future` | no | no | yes |
| `K_gen/K_event` | no | no | yes |
| `K_gen/K_record` | no | no | yes |
| `K_cap/K_future` | no | no | yes |
| `K_cap/K_event` | no | no | yes |
| `K_cap/K_record` | no | no | yes |
| `K_future/K_event` | no | no | yes |
| `K_future/K_record` | no | no | yes |
| `K_event/K_record` | no | no | yes |

Examples witness the separation. A homogeneously generated finite rail could
still exhaust capacity. Infinite blank capacity would not forbid a local
retarget gate. An occurrence-faithful syndrome could still be reversibly
erased. Record typing could preserve a value even if its apparatus origin was
contingent. None of the five follows from another in this construction.

### N3 — Hidden-condition scan

The required phrase scan covered “we assume,” “by construction,” “as is
standard,” “the framework provides,” “bridge context,” “background,”
“naturally,” “obviously,” “standard QFT,” “registered,” and “canonical.” No
such phrase carries an unlisted premise.

The scan promoted these load-bearing conditions into the explicit ledger:

- synchronized one-hot token/frontier sector;
- three role-marker bits at every slice;
- supplied open orientation and unique origin;
- all future targets blank;
- no wrap and an externally declared last lawful horizon;
- same `Q_x` value held during the bounded core episode;
- intended future only targets current and fresh slices;
- route geometry is carried covariantly, not generated;
- actual `W_g` application is not witnessed; and
- trace/effect evaluation is not occurrence or frequency.

The positive theorem is conditional on exactly these items.

### N4 — Residual matching

| cited witness and location | exact earlier residual | Cycle-286 residual | match? |
|---|---|---|---:|
| Cycle 282 note, lines 260–287 | finite cyclic recurrence changes packet at 28 and loses close at 55 | replace cyclic rail with open non-wrapping carrier and test nonreturn | yes |
| Cycle 282 note, lines 228–259 | split coupling deletion can false-close `NO` | use Cycle-281 positive close rather than silence-to-NO path | yes |
| Cycle 281 note, lines 121–204 | same-pointer write/archive/reset is deletion faithful on positive branch | inherit its exact close effect and deletion grammar | yes |
| Cycle 281 note, lines 282–323 | finite carrier is reversible; fresh continuation supplied | test long outgoing prefix, exact inverse, and local retarget | yes |
| Cycle 283 note, lines 168–264 | inverse reconnection and linear fresh capacity remain explicit | obtain the same scoped reversibility/capacity boundary under one repeated update | yes |
| Cycle 283 note, lines 293–315 | carried archive covariance does not generate placement | carry six-lane rail through all frames and keep origin/orientation supplied | yes |
| Cycle 284 note, lines 117–239 | lawful typing and global history remain supplied | receiving endpoint only; not used as proof of nonrecurrence | not a negative witness |

The Cycle-284 row is retained only as endpoint context and not counted as
support for a negative claim. No gravity, Born, or time residual is used as
evidence against an outgoing-carrier construction.

### N5 — Resolution and rhetoric audit

| resolution | tested statement | untested/broader statement rejected |
|---|---|---|
| one local update | exact inverse on 256 local basis inputs | arbitrary microscopic gate set |
| one contact cell | outbound effect equals rank-57 `Q_x` | every interaction event |
| finite rails `R=12,19,28,43` | exact nonreturn before boundary | infinite lattice or arbitrary rail |
| one old fact adjacent to frontier | controls-only export preserves it; retarget erases it | every possible future cone |
| complete tested rail | exact inverse erases all facts | universal impossibility of permanent Records |
| all 24 carried frames | collision-free covariance | homogeneous origin/orientation generation |
| `W_g` deletion | carrier effect unchanged | all possible contact syndromes are blind |
| Record/time | neither formed nor claimed | universal Record or time no-go |

Accordingly, “nonreturning” always means before the supplied open boundary
under the intended forward rule. “Old facts are controls only” always means
that intended continuation grammar, not unrestricted dynamics.

### N6 — Partial-closure path scan

Live constructive paths are:

1. generate the rail, role texture, and origin from a homogeneous lawful
   defect or boundary state;
2. use a growing lattice or locally produced fresh carriers and quantify its
   resource law;
3. add a local renewal/compression map with an exact decoder and information
   accounting;
4. make `W_g` and a syndrome one indivisible bounded transition so deleting
   `W_g` prevents launch;
5. type one deposited carrier through the actual Record-formation interface,
   then audit which inverse/retarget gates remain lawful;
6. replace the supplied no-target grammar with a selected local
   superselection/admissibility rule; and
7. connect the finite fact prefix to the Cycle-284 complete-packet decoder
   without calling archive position time.

These are import-retirement routes. None presently requires or motivates a
new axiom.

### N7 — Steelman

> A hostile reviewer should reject any permanence no-go immediately. The
> successful held rail already shows that the Cycle-282 recurrence was caused
> by a chosen cyclic finite register, not the common substrate. The remaining
> inverse and retarget attacks are admitted only because the test grammar
> permits them. A law-generated outward defect on an effectively unbounded
> lattice, or lawful Record typing that removes inverse gates from the future
> sector, could preserve the deposited facts. Likewise, an indivisible
> contact-plus-syndrome update could remove `W_g` blindness. The real open work
> is selecting that law and accounting for capacity, not proving it cannot
> exist.

The steelman is convincing. It narrows the result to finite-horizon nonreturn
with supplied capacity and future grammar.

### N8 — Cross-cycle echo

Cycle 282's cyclic recurrence is retired on the tested forward domain by
changing one physical feature: the token leaves on an open rail. Cycle 281's
positive deletion-faithful close survives unchanged and supplies the launch
condition. Cycle 283's fresh-capacity and reconnection warnings reappear, but
now under one repeated local sequencer rather than a host-applied append list.
Cycle 284 shows that complete finite packets can replay a declared process
once lawful typing is supplied.

These echoes show repeated progress by explicit constructors and scoped law
domains. The failure of unrestricted permanence has already been softened by
outward export; its remaining conditions have live physical routes. No shared
obstruction, minimum-content theorem, or axiom pressure survives N1–N8.

**N1–N8 status: PASS for the narrow finite-horizon construction and its named
countercontrols.**

## 13. TOE dependency ledger and next route

| wall | Cycle-286 effect | remaining dependency |
|---|---|---|
| `C_ref` | origin, orientation, blank targets, and boundary are counted explicitly | derive their lawful preparation or accept them as contingent apparatus data |
| `C_num` | exact `Q_(N>=2)` effect and one-particle identity remain unchanged | odd/full-Fock same-code preparation and broader matter observables |
| `C_wrap` | open rail removes wrap recurrence on all tested horizons | derive indefinite capacity, renewal, or a lawful boundary sector |
| `C_int` | Cycle-281 positive deletion faithfulness is preserved under one repeated outbound law | actual `W_g` occurrence syndrome and branch actualization |
| `C_local` | real gain: 29-M2 bounded per-step support, all-24 covariance, collision rejection, held nonreturn | homogeneous rail/origin generation and selected future no-target law |
| `C_source` | linear capacity cost `6R+3` is explicit | no energy/stress/source/gravity interpretation is derived |

Maturity scores remain conservative:

| lane | score | Cycle-286 effect |
|---|---:|---|
| operational quantum / Records | `2/5` | positive close now travels outward without finite-horizon recurrence, but remains coherent, erasable, and untyped |
| causal time | `1/5` | ancestry and spatial propagation only; no duration or rate |
| inertia / matter | `3/5` | same contact/mass fixture and code preserved |
| gravity / source | `2/5` | capacity counted, no source response |
| Born / probability | `1/5` | exact trace weights only |

The optimal next campaign is a **law-generated contact-syndrome defect**:
combine actual `W_g` application, positive syndrome launch, and outward
carrier propagation in one selected bounded update; generate or lawfully
prepare the origin/rail; require `W_g` deletion to prevent launch; and test
fresh-capacity renewal, collisions, reverse-law admissibility, all-24
covariance, held horizons, and the Record/time firewalls separately.

## Verification

Run:

```bash
python3 scripts/outgoing_carrier_nonrecurrence_cycle286_2026_07_17.py
```

The runner must finish with zero failures. PASS totals are regression
assertions, not counts of independent physical predictions.
