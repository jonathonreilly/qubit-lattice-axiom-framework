# Coherent orientation-character CAR compiler — Cycle 272

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/coherent_orientation_character_car_compiler_cycle272_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status. It creates only this note and runner.

## Result up front

One ordinary M2 carrier per coarse cell exactly repairs the local covariance
obstruction isolated in Cycle 268.

Let `chi(g)` be the parity of the six-direction permutation induced by proper-
cubic frame `g`. Put one coherent orientation qubit `o_c` at the cell center
and let the frame act by

```text
U_g(o_c) = X_o^chi(g).
```

The character obeys the exact group law for all `24^2` frame products. Under
odd-character frames, both Cycle-268 reference chirality `B_ref` and `Z_o`
change sign. Therefore

```text
C_ref = B_ref Z_o
```

is a proper-cubic scalar. The exact Cycle-268 pseudoscalar sign system remains
constructive at `992/992`, with a 16-dimensional solution space. `C_ref`
anticommutes with exactly the six reference spokes, commutes with every
original physical edge and pair check, and has physical support four. All 24
frames, the exact group law, and full translations pass with no root or marked
orientation.

This closes the **local orientation-covariance component**. It does not close
the full-Fock compiler.

The one-qubit-per-cell repair merely moves the remaining problem into the
carrier constraints and global parity relation:

| constraint route | exact exponent | local scalar `C_ref` | matter parity |
|---|---:|---|---|
| fix every `X_o=+1`, retain `B_ref` equality | `V` | leaks once per cell through `X_o` | `P_m=b^N`; odd matter deleted for even `N` |
| impose onsite `B_ref Z_o=+1`, retain `B_ref` equality | `V` | fixed, not a free occupation; every spoke leaks through the onsite check | `P_m=b^N` |
| impose both `C_ref` equality and `Z_o` equality | `V+1` | lawful and scalar | one excess logical; `P_m=(cz)^N`, so even-volume odd matter still deleted |
| two orientation carriers locally bound to `B_ref` | `V` | scalar bindings | both carriers copy `b`; `P_m=b^N` remains |

Here `N=L^3` and `V=6N`. The exact volume-parity defect survives all tested
routes:

```text
L=3,5: both matter parities exist;
L=4 and held-out L=6: negative matter parity is phase inconsistent.
```

The orientation carrier cannot change this identity because the unmodified
reference-spoke loop code still imposes `P_m P_ref=+1`. Under diagonal
reference equality, `P_ref=b^N`. Adding a carrier representation changes how
frames act; it does not insert carrier parity into the loop-code central
relation.

The smallest physical placement is explicit. The one-carrier route uses the
empty cell-center site and raises overhead from 24 to 25 physical M2/cell. A
two-carrier comparison cannot stack two M2 factors at the same center. It uses
the center plus a six-site radius-30 repetition motif for the second logical
carrier, with five local equality checks. This is collision free, invariant
under all 24 frames, has constant route bound four, and gives 31 M2/cell.
Neither its extra physical orbit nor its exact target rank changes `b^N`.

All tested carrier constraints are local, commuting in their declared route,
and translation covariant. None supplies bounded preparation of an arbitrary
coherent matter-parity input or the three Wilson logicals. No common prepared
full-Fock `E` survives, so actual Cycle-230 coin/A/B-FSWAP/contact, mass, and
rank-73 seam synthesis is not reached.

The result is a constructive representation gain plus route-specific
residuals. It is not a no-go against non-diagonal reference pair-flip codes,
carrier-dressed loop stabilizers, changed reference graphs, subsystem
encoders, or orientation carriers generally. There is no axiom pressure.

## 1. Orientation character and local scalarization

The 24 proper-cubic frames induce permutations `p_g` of the six signed
coordinate directions. Their permutation parity

```text
chi(g) = parity(p_g) in GF(2)
```

is a one-dimensional group character:

```text
chi(gh) = chi(g) + chi(h) mod 2.
```

The runner checks all 576 products with zero character failures. Twelve frames
have `chi=0` and twelve have `chi=1`.

Conjugation by `X_o^chi(g)` fixes `X_o` and maps

```text
Z_o -> (-1)^chi(g) Z_o.
```

Cycle 268's constructive action maps reference chirality by the same sign,
while keeping physical chirality, original edges, and spokes positive. The
product `C_ref=B_ref Z_o` is therefore scalar. The combined local action has
the exact group law; it is not a frame-by-frame phase table.

The runner explicitly verifies zero frame failures for:

- two-reference `B_ref` equality checks;
- onsite `X_o` checks;
- scalar `B_ref Z_o` products;
- two-carrier products; and
- two-orientation `Z_o` equality checks.

At `L=3`, `C_ref` has support four, anticommutes with its six spokes, commutes
with every original edge, and has zero pair-check leakage.

## 2. One-carrier physical placement

The existing physical roles occupy nonzero direction shells at radii
`6,12,18,24`. The period-64 cell center `(0,0,0)` is unoccupied and is fixed by
every proper-cubic frame. One ordinary M2 carrier per cell is placed there.

The resulting overhead is

```text
Cycle-264 reference-spoke roles: 24 M2/cell
orientation carrier:             1 M2/cell
total:                           25 M2/cell.
```

The frame action `X^chi` is an internal coherent action on that physical M2;
it is not a classical orientation choice. Translations carry each center to
the corresponding center in the translated cell.

## 3. Route A — onsite X preparation

Retain Cycle 264's diagonal reference equality

```text
B_ref,c B_ref,c' = +1
```

and fix every carrier in `X_o=+1`. These checks commute, are local, are
proper-cubic covariant, and have the exact target rank. Exact physical results
are:

| `L` | rank | exponent | target | `C_ref` leakage | negative matter parity |
|---:|---:|---:|---:|---:|---|
| 3 | 513 | 162 | 162 | 27 | consistent |
| 4 | 1216 | 384 | 384 | 64 | inconsistent |
| 5 | 2375 | 750 | 750 | 125 | consistent |
| 6 | 4104 | 1296 | 1296 | 216 | inconsistent |

Each scalarized occupation contains `Z_o` and therefore anticommutes with its
onsite `X_o` check. The correct dimension is a duplicate even-code count, not
a lawful scalar reference occupation algebra.

The matter-parity law is unchanged. Reference equality leaves one bit `b`, so
`P_m=P_ref=b^N`.

## 4. Route B — onsite scalar binding

Replace the carrier-X checks by onsite scalar bindings

```text
B_ref,c Z_o,c = +1
```

and retain `B_ref` equality. The checks commute and transform as scalars. Their
rank again gives exponent `V` at every size, with no phase inconsistency.

This route fixes `C_ref=+1`; it does not leave `C_ref` as a reference
occupation operator. Each binding anticommutes with all six spokes incident on
that reference mode, giving exact auxiliary-spoke leakage

```text
162, 384, 750, 1296 = 6N
```

at `L=3,4,5,6`. The loop stabilizers themselves contain even spoke incidence
and remain consistent, but individual auxiliary spoke generators are no
longer lawful code operations. Matter parity remains `b^N`.

## 5. Route C — two commuting equality fields

Impose nearest-neighbor equality on both scalar chirality and carrier Z:

```text
C_ref,c C_ref,c' = +1,
Z_o,c Z_o,c'     = +1.
```

These checks commute. Every local `C_ref` preserves them. They are invariant
under every frame because `C_ref` is scalar and each Z equality receives two
orientation-character signs.

The exact ranks give exponent `V+1`, one logical too many:

| `L` | exponent | target | excess | `C_ref` leakage |
|---:|---:|---:|---:|---:|
| 3 | 163 | 162 | 1 | 0 |
| 4 | 385 | 384 | 1 | 0 |
| 5 | 751 | 750 | 1 | 0 |
| 6 | 1297 | 1296 | 1 | 0 |

Let their two repetition logicals be `c` and `z`. Since
`B_ref=C_ref Z_o`, the base loop relation gives

```text
P_m = P_ref = (c z)^N.
```

Thus both matter parities occur only for odd `N`; even `N` again fixes
positive matter parity. Removing the one excess logical with a single global
condition would reintroduce nonlocal sector selection. No local covariant
condition doing so is constructed.

## 6. Two-carrier/even-orbit comparison

Two abstract orientation carriers per cell both transform by `X^chi`. Retain
`B_ref` equality and impose two scalar onsite bindings

```text
B_ref Z_o1 = +1,
B_ref Z_o2 = +1.
```

The exact rank is the target `V` through `L=3,4,5,6`. Both carriers simply copy
the same reference bit. Therefore `P_m=b^N`, with the identical odd-sector
deletion at `L=4,6`.

Physical placement is not faked by putting two M2 factors at one center. The
first carrier uses the center. The second is encoded in the six radius-30
direction sites with five repetition checks. This shell is disjoint from
radii `6,12,18,24`, is preserved by all frames, has local code rank five, and
supports one logical qubit. More precisely, the generated rank-five equality
group—not merely the displayed chain generating set—is invariant under all 24
direction permutations. Its maximum periodic route is four. The physical
orientation overhead is seven M2/cell and total overhead is 31 M2/cell.

The two-carrier route proves that an even physical carrier motif and exact
target rank are not sufficient. It does not exhaust other two-carrier
Hamiltonians or non-diagonal pair-flip constraints.

## 7. Translation, Wilson, preparation, and held-out controls

Every nearest-cell carrier/check family has zero translation failures for all
`L^3` coarse translations at `L=3,4,5,6`.

The underlying reference-spoke code still has three Wilson logicals before
the noncontractible conditions are added. Their maximum supports are
`21,28,35,42`. Equality-carrier preparation retains a growing local causal
depth lower bound `2,3,3,5` across the tested sizes.

Consequently none of the rank-correct routes supplies a bounded encoder for an
arbitrary state

```text
alpha |matter-even> + beta |matter-odd>.
```

Onsite preparation of a center carrier or bounded radius-30 repetition code
does not prepare the system-spanning reference/Wilson correlations.

The held-out L=6 case reproduces all formulas: exact group action, constant
overhead/support, target ranks where declared, odd matter deletion, three
Wilson logicals, and no bounded preparation.

## 8. Actual-update firewall

No route gives one common prepared full-Fock `E` at every size. The actual
update chain therefore remains gated:

```text
common full-Fock E
  -> actual coin / A-FSWAP / B-FSWAP / contact
  -> E G_coarse = G_physical E
  -> leakage, mass, contact, and seam replay.
```

The runner verifies only the predecessor fixtures

```text
beta=-0.3
g=0.37
Cycle-219 rest fixture = 0.4534056541748851
Cycle-230 principal sea rank = 73.
```

Coin/A/B-FSWAP/contact synthesis, leakage, iteration, one-particle mass, local
contact, and rank-73 seam intertwining are not reached and are not called
failures.

## 9. Supplied-structure inventory

Cycle 272 supplies or inherits:

1. the Cycle-268 exact `992/992` pseudoscalar reference action;
2. the proper-cubic direction-permutation character `chi`;
3. one ordinary M2 carrier at every supplied period-64 cell center;
4. the internal frame action `X_o^chi(g)`;
5. the scalarized occupation candidate `B_ref Z_o`;
6. the Cycle-264 24-M2/cell reference-spoke code and pair checks;
7. the three tested one-carrier constraint families;
8. a two-carrier comparison with a six-site radius-30 repetition motif;
9. closed periodic sizes `L=3,4,5,6`, full translations, and three Wilson
   constraints;
10. constant placement/routing structure with bounds 16 and four;
11. exact Pauli, phase-aware rank, group-law, leakage, sector, and support
    arithmetic; and
12. fixed `beta=-0.3`, `g=0.37`, mass, and rank-73 seam fixtures.

No modified loop central relation, non-diagonal reference pair-flip code,
bounded global preparation, measurement, probability, Record semantics,
physical clock, update law, energy, source, or gravity coupling is derived.

## 10. Prior-art and novelty boundary

Bravyi-Kitaev and Setia et al. remain the direct bounded-degree even/GSE prior
art. Chen-Kapustin and Chen remain the direct higher-dimensional bosonization
comparators with explicit spin/topological structure. Cycle 272 does not claim
orientation or spin-character supply as new in general.

Cycle 268 supplies the exact pseudoscalar repair and identifies an orientation
character as the optimal next component. Cycle 272's fixture-specific new
content is limited to:

1. the exact one-M2 character representation and scalar `B_ref Z_o`;
2. all-frame/group-law/translation and local incidence certificates;
3. three exact one-carrier constraint dispositions;
4. the one-logical excess in the commuting double-equality route;
5. the physical two-carrier/even-orbit comparison; and
6. all-size rank, sector, leakage, support, and preparation controls.

No global novelty priority is claimed. No Thirring engine is used or compared.

## 11. TOE dependency ledger after Cycle 272

| Workstream | Cycle-272 effect | Remaining dependency |
|---|---|---|
| `C_ref` | strong gain: the missing proper-cubic orientation character now has one explicit coherent M2 carrier/cell and exact group action | derive carrier constraints that change the global parity relation rather than merely copy/fix its bit |
| `C_num` | scalar reference occupation exists locally with exact incidence | faithful both-matter-parity code at even and odd volume without leakage/excess |
| `C_wrap` | carrier repair leaves the three Wilson logicals and `P_m P_ref` central relation explicit | bounded/subsystem preparation and a lawful carrier-dressed topological join |
| `C_int` | actual gate synthesis remains correctly gated | common prepared `E`, then actual update/leakage |
| `C_local` | exact all-frame/group-law/translations, 25- and 31-M2 placements, constant support/routing | non-diagonal commuting carrier/reference constraints or carrier-dressed loops |
| `C_source` | unchanged | no energy, action, stress, source, or gravity coupling is selected |

The campaign-wide maturity estimates are maintained in Cycle 270 rather than
recomputed from this one compiler probe. Its integrated planning percentages
are operational quantum/Records `42%`, time `32%`, inertia/matter `58%`,
gravity/source `34%`, and Born/probability/history `30%`; they are not audit
verdicts or probabilities that the framework is correct.

## 12. No-go discipline N1–N8

The narrow negative is:

> None of the declared diagonal one- or two-orientation-carrier constraint
> families simultaneously preserves a free scalar `B_ref Z_o`, has exponent
> `V`, and realizes both matter parities at even and odd volume.

### N1 — alternative routes

| route | honesty marker | exact disposition |
|---|---|---|
| one-M2 orientation character | **ATTEMPTED** | constructive exact covariance and scalarization |
| onsite carrier `X=+1` | **ATTEMPTED** | target rank; one `C_ref` leak/cell |
| onsite scalar binding `B_ref Z_o=+1` | **ATTEMPTED** | target rank; scalar fixed and six spoke leaks/cell |
| commuting `C_ref` and `Z_o` equalities | **ATTEMPTED** | zero local leakage; one excess logical and `P_m=(cz)^N` |
| two-carrier/even-orbit binding | **ATTEMPTED** | target rank/physical placement; copies `b^N` |
| marked/global logical constraint | **RULED OUT BY REQUIREMENT** | would remove the excess by reintroducing global sector selection |
| local even/gauge encodings generally | **RULED OUT BY PRIOR ART as a negative route** | known constructive encodings block a broad no-go |

Non-diagonal reference pair flips, carrier-dressed loop stabilizers, subsystem
joins, measurement-assisted preparation, and changed reference graphs remain
live.

### N2 — condition independence

`K_cov` is now closed. The live conditions are `K_parity` (both matter
parities at every size), `K_centralizer` (lawful scalar occupation/spokes),
`K_rank` (no excess), `K_prep` (bounded parity/Wilson encoder), and downstream
`K_law`. The route table gives explicit examples closing any one without the
others. They remain independent.

### N3 — hidden-condition scan

“Orientation character” is the tested permutation-parity homomorphism, not a
classical selected axis. “Scalarized” means operator-sign cancellation under
all frames, not code preservation; leakage is audited separately. “Physical
carrier” means distinct ordinary M2 sites, including the six-site encoding of
the second logical carrier. Rank is not preparation. The macro origin,
periodic boundary, carrier constraints, Wilson data, and parameters are
supplied explicitly.

### N4 — residual matching

| witness | prior residual | Cycle-272 match |
|---|---|---|
| Cycle 268 pseudoscalar `992/992` | missing orientation character | closed exactly by `X_o^chi` |
| Cycle 268 odd-volume code-sector flip | scalarization must preserve global code | becomes explicit carrier/parity constraint problem |
| Cycle 264 `P_m=b^N` | diagonal equality loses odd matter at even volume | persists in all rank-correct diagonal routes |
| Cycle 252 coherent join | topological coherent carrier can join sectors | remains a live non-diagonal/subsystem route |
| Cycle 230 fixtures | downstream gate/mass targets | retained behind firewall only |

### N5 — resolution audit

Tested: all 24 frames, all frame products, all translations, local incidence,
physical placements, commuting check ranks, both matter sectors, leakage,
deletions, Wilson increments, and `L=3,4,5,6` including held-out `L=6`.

Not tested: all non-diagonal stabilizer codes, carrier-dressed loop relations,
multi-cell Clifford circuits, open boundaries, or actual update synthesis.

### N6 — partial-closure scan

| path | status | possible closure |
|---|---|---|
| non-diagonal even pair-flip reference/carrier code | priority | make total reference parity logical at even `N` |
| carrier-dressed loop stabilizers | untested | replace `P_m P_ref=1` by a scalar relation involving carrier parity |
| Cycle-252-style subsystem/topological join | untested synthesis | remove the extra logical operationally without a marked global check |
| measurement/dissipative cat preparation | outside current unitary grammar | address bounded preparation separately |
| changed reference orbit or boundary | target change | alter the volume-parity functional |

No axiom edit is indicated.

### N7 — steelman

> The orientation carrier succeeds completely at its assigned job: one M2 per
> cell turns the pseudoscalar reference occupation into a scalar with exact
> proper-cubic group law. The remaining `b^N` identity belongs to the unchanged
> diagonal reference code and loop central relation, not to covariance. A
> non-diagonal pair-flip code or carrier-dressed loop relation can change that
> identity. The successful `992/992` action and explicit physical placements
> are constructive evidence against a general obstruction.

This steelman is convincing; a broad no-go fails.

### N8 — cross-cycle echo

Past sign and frame walls were retired by coherent carriers. Cycle 272 does so
again for the orientation character. Past parity/Wilson walls required
non-diagonal or topological joins, and those mechanisms remain live. The cycle
therefore supports only the declared diagonal carrier-family negative, not a
shared substrate obstruction or axiom pressure.

## 13. Record and time firewall

Orientation carriers, reference bits, and repetition motifs are coherent code
degrees of freedom. They are not measurements, copied Records, or realized
histories.

**3D frame character is spatial structure, not physical time.** Frame-group
multiplication, carrier `X` actions, stabilizer layers, cat-depth bounds, and
runner duration are compiler resources. No generator is called a rate; no
clock, event, probability, energy, or source is derived.

## Route disposition and optimal next campaign

Retain the exact one-M2 orientation character, scalar `B_ref Z_o`, `992/992`
action, all-frame/group-law/translation certificate, physical placements, and
all route-specific rank/leakage/parity controls.

Reject the displayed diagonal one- and two-carrier codes as a common full-Fock
compiler. Do not synthesize Cycle-230 gates in them.

The optimal next campaign is an exact non-diagonal pair-flip or carrier-dressed
loop-code construction that makes total reference/carrier parity a logical for
both even and odd `N`, preserves local scalar `B_ref Z_o`, and removes the one
excess logical without a marked global check. Bounded preparation and Wilson
subsystem treatment remain separate demands. Only after those close should
actual `beta=-0.3`, `g=0.37` gates and mass/rank-73 seam be synthesized.

There is no shared obstruction, no axiom pressure, and no axiom conclusion.

## Verification

```text
python3 scripts/coherent_orientation_character_car_compiler_cycle272_2026_07_17.py
```
