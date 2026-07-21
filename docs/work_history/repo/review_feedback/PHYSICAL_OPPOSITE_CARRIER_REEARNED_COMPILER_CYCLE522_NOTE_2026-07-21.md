# Physical opposite-carrier re-earned compiler — Cycle 522 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_opposite_carrier_reearned_compiler_cycle522_2026_07_21.py`.

## Result

Cycle 522 upgrades Cycle 519's zero-new-M2 opposite-carrier comparator into a
bounded algebraic compiler route.  It reconstructs the selected local branch
grammar, proves an exact local M64 code through every number sector, reruns the
adjacent-twelve-cell and seven-cell static shells, and gives one full two-cell
coin-FSWAP-contact seam with the Cycle-219 mass fixture.

The result requires a **rebuilt dense coin**.  The inherited Cycle-311 dense
coin does not preserve the selected subspace.  The rebuilt coefficients,
matrix-unit application, off-code identity completion, role preparation, and
schedule remain supplied.  Therefore this is a zero-new-M2 **algebraic**
compiler route, not a primitive or recurrent multi-edge physical M2 compiler.

## Exact selected-carrier grammar

Directions are the three opposite pairs `(0,1)`, `(2,3)`, `(4,5)`.  For an
odd occupation label (S\subset\{0,\ldots,5\}), retain precisely

\[
 D(S)=\{d\notin S:d\mathbin{\mathsf{xor}}1\in S\}.
\]

If the native Cycle-311 common branch has amplitude (a_d), replace it on the
retained set by

\[
 a'_d=a_d\sqrt{\frac{6-|S|}{|D(S)|}}.
\]

Even sectors are unchanged.  The exact odd-sector census is:

| sector | labels | selected carriers per label | common-branch squared weight |
|---:|---:|---:|---:|
| (n=1) | 6 | 1 | 1 |
| (n=3), one antipodal pair plus one mode | 12 | 1 | 1 |
| (n=3), one mode from each antipodal pair | 8 | 3 | (1/3) |
| (n=5) | 6 | 1 | 1 |

The existing Cycle-306/311 cell-role gauge still duplicates each common
branch with an additional factor (1/\sqrt2).  Hence selected gauge-term
squared weights are (1/2), except for the three-carrier (n=3) orbit where
they are (1/6).  Every column has exact norm one.

The rule is relational and proper-cubic: every signed permutation maps
opposite pairs to opposite pairs.  Across all 24 proper frames, 768 odd-label
selector tests and their normalization counts have zero failures.  There is
no fixed global direction, Jordan-Wigner order, or parity service.

## Complete local M64 shell

The selected fixed-seam shell has 159 flagged microsectors rather than the
native 255:

| number | flagged input/output microsectors |
|---:|---:|
| 0 | 1 |
| 1 | 12 |
| 2 | 30 |
| 3 | 72 |
| 4 | 30 |
| 5 | 12 |
| 6 | 2 |
| total | 159 |

At L5 and held L6:

- the 159-by-127 flagged map has rank 127 and Gram residual
  (8.88\times10^{-16});
- the existing `f+r` role-gauge lift has constrained rank 127 and exact
  constraint eigenvalue;
- deleting the cell role leaves 153 raw rows, rank 121 rather than 127, and
  Gram operator residual 1;
- the literal stream/catch-up and physical occupation-counting contact have
  zero intertwiner residual;
- every selected input contact is
  (\exp(i\binom n2 g)), and every separated-slice contact is one.

Thus opposite-carrier selection does not eliminate the existing relational
cell role.  “Zero new M2” means no M2 beyond the already-declared Cycle-311
cell flag and companion, not that those inherited roles disappear.

## The inherited coin fails; the rebuilt dense coin succeeds

Embed the selected code into the native 255-row Cycle-311 shell and apply the
unchanged native dense coin.  At both sizes:

| control | exact/numerical result |
|---|---:|
| selected-code Gram residual | (8.88\times10^{-16}) |
| inherited-coin intertwiner residual | `5.441845322043213` |
| inherited-coin leakage operator norm | `0.9402775659787453` |
| rebuilt-vs-inherited coin operator norm | `1.7837492182395673` |

This falsifies only the shortcut “delete four (n=1) carriers but retain the
same physical coin.”  It is not a failure of the selected code.

For selected flagged isometry (E_{\rm opp}), define

\[
 K_{\rm opp}
 =E_{\rm opp}K_{\rm logical}E_{\rm opp}^\dagger
  +I-E_{\rm opp}E_{\rm opp}^\dagger .
\]

At L5 and held L6 this rebuilt dense coin has:

- intertwiner residual (1.25\times10^{-15});
- unitarity residual (6.04\times10^{-15});
- 1,608 active off-diagonal microterms;
- zero number-changing terms;
- zero inherited port-constraint or fixed-sector commutator failures; and
- maximum Pauli transition support 27 M2.

Coin, stream, contact, and composed update covariance pass all 24 physical
frames at both sizes.  Physical branch failures and isometry covariance are
zero; the largest rebuilt-coin/composition covariance residual is
(1.56\times10^{-15}).  All 576 logical frame products close exactly.

This is a re-earned bounded dense lift.  It does not derive its coefficients
from an approved primitive update law or synthesize them into elementary M2
gates.

## Adjacent twelve-cell exact Gram

On the Cycle-517 adjacent-two-star global-(N\leq2) domain, only (n=1)
changes.  Each logical local state now has exactly two cell-gauge terms.
The exact compressed census at L5 and held L6 is:

| sector | excitation seeds | expanded rows |
|---|---:|---:|
| vacuum | 1 | 4,096 |
| one particle | 144 | 294,912 |
| same-cell two particle | 360 | 737,280 |
| split-cell two particle | 9,504 | 9,732,096 |
| total | 10,009 | 10,768,384 |

All 10,009 quotient fibers are singleton at both sizes.  Every one of the
2,629 logical columns has exactly 4,096 branches of squared weight (1/4096).
The expanded rows are therefore disjoint and every column has exact norm one:

\[
 E_{\rm opp,12}^\dagger E_{\rm opp,12}=I_{2629}.
\]

No tag M2 is appended.  Restoring the native five-carrier (n=1) grammar
restores Cycle 518's 24 doubletons, 6,144 expanded collisions, and exact Gram
operator residual (1/400).

This closes the static adjacent-twelve-cell separation wall for this changed
representative grammar.  It does not yet apply the rebuilt dense update across
all eleven adjacent-star seams or prove recurrent overlapping constraints.

## Seven-cell all-order shell

The selected grammar was rerun on the complete Cycle-515 seven-cell,
global-(N\leq2) domain.  At both L5 and held L6:

| item | result |
|---|---:|
| logical columns | 904 |
| branches per column | 128 |
| structural branches | 115,712 |
| distinct physical rows | 115,712 |
| row reuses | 0 |
| maximum norm residual | (2.23\times10^{-16}) |
| anticommutation masks | `0,1,2,4,8,16,32` |
| maximum base branch support | 33 M2 |
| with inherited thirteen-M2 order role | 46 M2 |

Every one of the 5,040 cell-factor orders changes a unique row only by the
exact Cycle-515 anticommutation character.  Hence every order map remains an
isometry and the correlated order-role construction remains isometric.  The
Cycle-516 physical term identities apply to this covariant subset, but its
full multi-star primitive realization is not inferred.

## Full two-cell all-Fock seam

The selected grammar also re-earns the Cycle-315 neighboring-cell seam on the
complete 4,096-dimensional two-cell Fock space, not merely (N\leq2).

At L5 and held L6:

| item | result |
|---|---:|
| logical columns | 4,096 |
| physical reduced rays | 25,088 |
| nonzero amplitudes | 25,600 |
| processed Gram operator residual | 0 |
| raw Gram maximum | (4.45\times10^{-16}) |
| minimum Gram eigenvalue | (0.9999999999999997) |

On the L5 shell the explicit dense completion

\[
 A(U)=E_{\rm opp}UE_{\rm opp}^\dagger+I-E_{\rm opp}E_{\rm opp}^\dagger
\]

is tested for the full coin-FSWAP-contact update.  The physical intertwiner is
zero after the declared exact-support pruning and four randomized ambient
inverse residuals are at most (5.90\times10^{-16}).  The inherited edge-role
gauge has exact constraint involution, eigenvalue, commutator, and update
intertwiner.  Deleting that relation leaves unordered Gram operator residual
approximately one and minimum Gram eigenvalue numerically zero.

The logical update retains:

- 627,264 coin coefficients;
- one signed FSWAP entry per column;
- 4,047 nontrivial contact columns;
- exact processed coin, FSWAP, contact, and composition unitarity; and
- noncommuting ordered factors, so the order is load bearing.

All 24 carried edge frames pass update covariance; twelve preserve endpoint
role and twelve reverse it.  The edge-role group and translation controls have
zero failures.

The uniform two-cell one-particle ray gives

```text
Cycle-219 fixture       0.4534056541748851
opposite-carrier seam  0.4534056541748851
eigenvector residual   3.8571762755144336e-16
```

The matching mass follows through the explicit selected-code intertwiner.  A
wrapped phase is not called physical energy, a dense matrix unit is not called
a rate, and a compiler step is not physical time.

## Resources, leakage, deletion, and lawful domain

The selector changes amplitudes and branch support but adds no site.  It
inherits the Cycle-311 installation of 23 M2 per cell.  The full two-cell seam
still uses 83 M2 including its already-declared edge flag and edge companion,
with maximum joint branch support 65 M2.  The selected two-cell patch has zero
port-constraint and fixed-sector commutator failures.

Destructive controls are independent:

- omitting the (\sqrt5) renormalization in (n=1) leaves local column norm
  (1/5), hence Gram deficit (4/5);
- deleting the only selected (n=1) carrier gives Gram residual 1;
- deleting one selected (n=3) carrier gives residual (1) on the one-carrier
  orbit or (1/3) on the three-carrier orbit;
- deleting the cell role gives raw rank 121 and Gram residual 1;
- applying the inherited native coin gives leakage `0.9402775659787453`;
- deleting one FSWAP column gives unitarity residual 1;
- deleting the largest active logical coin coefficient gives unitarity
  residual greater than 0.5;
- deleting nontrivial contact gives residual greater than 1; and
- deleting the edge relation doubles the lawful shell rank.

The local theorem covers all (n=0,\ldots,6).  The two-cell theorem covers
all total (n=0,\ldots,12).  The adjacent-twelve and seven-cell theorems
retain global (N\leq2), L5, and held L6.  L4 remains rejected because of
the extra periodic edge.  Malformed or repeated labels, invalid number, and
determinant-minus-one frames are outside the lawful domain.

The final runner uses a 600-second hard wall, 3 GB RSS guard, and zero-swap
checkpoints.  These are execution controls, not physical premises.
The final cold certificate completed in `166.01483808306511` seconds with
maximum resident memory `506200064` bytes, zero swap, and summary
`PASS=13 FAIL=0`.

## Supplied structure and novelty boundary

Supplied or inherited are:

1. the fixed-Wilson reference, face/port dictionary, and preparation;
2. the Cycle-311 cell flag, cell companion, and relational constraint;
3. the opposite-carrier selector and its exact normalization;
4. the Cycle-315 edge role, edge companion, and their preparation;
5. the Cycle-515 order role and dense shell projector;
6. the Cycle-219 coin at `beta=-0.3`, Cycle-230 coupling `g=0.37`, and the
   coin-FSWAP-contact order;
7. rebuilt dense local and seam matrix-unit coefficients;
8. off-code identity completions and application of those dense blocks;
9. the finite L5/L6 patches, boundary conditions, and global-(N\leq2)
   adjacent/star cutoff; and
10. state preparation, primitive gate genesis, and the circuit schedule.

The standard ingredients—complement carriers, exterior powers, dense
isometric extensions, local role gauges, and antipodal cubic relations—are
prior-art territory.  Cycle 522 claims only this exact opposite-carrier
selection, its re-earned repository fixtures, and the stated residuals.  It
does not claim the selector is unique or minimal.

Primitive synthesis of the rebuilt coefficients, simultaneous constraints on
several edges sharing one cell, a recurrent volume schedule, larger-number
adjacent stars, physical time, Records, Born probability, source/stress,
gravity, backreaction, and continuum limits remain open.  None is converted
into an axiom proposal.

## Full current no-go discipline

The current `origin/main` no-go-discipline procedure was read after a freshness
fetch and applied.  The only negative result retained is that the particular
inherited Cycle-311 dense coin fails on the selected subspace.  The successful
rebuilt dense route forbids a broader no-go, minimum-content claim, or axiom
pressure.

### N1 — alternative-route enumeration

| normalized route | honesty | disposition |
|---|---|---|
| opposite-carrier selected code plus rebuilt dense coefficients | **ATTEMPTED** | succeeds locally, on the static stars, and on one two-cell seam |
| opposite-carrier selected code with unchanged native coin | **ATTEMPTED** | exact candidate fails with intertwiner `5.4418` and leakage `0.9403` |
| native five-carrier grammar | **ATTEMPTED / prior Cycle 518** | retains the original local update but has 24 adjacent-star doubletons |
| independent parity tag | **ATTEMPTED / Cycle 519** | static isometry succeeds; preparation, physical control, and recurrence remain open |
| persistent occupation/gauge registers | **OPEN** | can retain the distinguishing data before overlap; terminal obligation is bounded preparation and update |
| changed face/path representatives | **OPEN** | can preserve carrier multiplicity while changing the collision quotient; must re-earn coin and frames |
| staggered or time-multiplexed carrier role | **OPEN** | can retain the missing relation dynamically; must close schedule covariance and coherent recurrence |

The successful rebuilt route makes the broad negative gate **FAIL / DO NOT
SHIP**.  The live alternatives also prevent a uniqueness or minimum-M2 claim.

### N2 — wall-independence audit

After collapsing downstream duplicates, the remaining walls are:

- **W_primitive:** synthesize the selected encoder, rebuilt dense coin, role
  constraints, and off-code completion from a lawful M2 update basis;
- **W_recur:** make several selected edge/star shells sharing a cell commute or
  supply an autonomous covariant schedule; and
- **W_prediction:** connect a recurrent compiled law to causal time,
  Record/Born occurrence, and source/response predictions.

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| W_primitive / W_recur | no | no | yes |
| W_primitive / W_prediction | no | no | yes |
| W_recur / W_prediction | no | no | yes |

The inherited-coin failure is not a fourth wall; it is a deleted-candidate
control already bypassed by rebuilding the dense lift.  The mass retest is a
validation of the rebuilt update, not an independent wall.

### N3 — hidden-wall scan

The selector, opposite-pair convention, normalization, fixed reference,
cell/edge/order roles, dense coefficients, off-code completion, state
preparation, beta, coupling, factor order, number cutoffs, boundary, and
schedule are all explicit.  “By construction” is used only for displayed
linear-algebra identities whose hypotheses are executed.  No background
host query selects a carrier at runtime: the complete selected table is fixed
before the update.  Primitive genesis and recurrence are promoted to W_primitive
and W_recur rather than hidden in “standard” or “canonical” language.

### N4 — residual matching

| witness | exact residual witnessed | Cycle-522 use | match? |
|---|---|---|---:|
| Cycle 518 compressed Gram | 24 native adjacent-star doubletons and (1/400) Gram residual | native five-carrier deletion comparator only | yes |
| Cycle 519 opposite comparator | 10,009 singleton excitation fibers under one opposite carrier | selected adjacent-star grammar reconstructed here | yes |
| Cycle 311 common M64 | local cell role, stream, contact, and native dense coin | inherited fixtures retested; native coin separately falsified | yes |
| Cycle 315 two-cell seam | edge role and dense coin-FSWAP-contact obligation | same one-edge full-Fock terminal with selected encoding | yes |
| Cycle 515/516 all-order/frame shell | seven-cell order characters and proper-frame term identities | selected subset and rebuilt local frame lift | yes, within the bounded subset |

No source, time, Born, Record, mediator, or gravity residual is cited as
evidence about the opposite-carrier compiler.

### N5 — rhetoric audit

“The inherited coin fails” means the exact 255-row Cycle-311 dense coin acting
on the selected 127-column local code at L5 and held L6.  It does not mean no
coin exists: the rebuilt dense coin succeeds.  “Exact isometry” is tested at
the local column, two-cell full-Fock seam, seven-cell all-order shell, and
adjacent-twelve global-(N\leq2) resolutions.  Recurrent multi-edge and
infinite-volume resolutions are not tested and receive no negative statement.
“Zero-new-M2” is relative to the inherited Cycle-311/315/515 role inventory;
it is not a lower bound or a claim of zero auxiliaries.

### N6 — partial-closure paths

Cycle 522 is itself a partial-closure path: change one explicit representative
selector, renormalize, rebuild the bounded dense lift, and re-run the prior
fixtures without an axiom or primitive edit.  A future import-retirement audit
can decompose the 1,608 local coin microterms and the sparse two-cell shell into
an approved local update basis.  Separately, edge coloring, relational clocks,
or a commuting multi-edge gauge can attack W_recur.  These are physics and
implementation obligations, not naming conventions and not automatic new
axioms.

### N7 — hostile steelman

A hostile reviewer should say that the positive update is algebraically easy
once an isometry is known: (EUE^\dagger+I-EE^\dagger) simply installs the
desired logical law as supplied dense coefficients.  The old physical coin
actually leaks by `0.9403`, so Cycle 522 has not shown that the repository's
existing primitive dynamics naturally selects the opposite carrier.  The
three-carrier (n=3) orbit and the one-carrier orbit also require different
normalizations, and no simultaneous shared-cell edge schedule is executed.
The actionable terminal is an explicit local primitive decomposition with
constraint-preserving intermediate states, followed by a three-edge shared-cell
commutator/schedule and mass retest.  This steelman blocks promotion to a
primitive or recurrent compiler; it does not undo the exact bounded algebraic
theorem.

### N8 — cross-cycle echo

Cycles 306, 311, and 315 repeatedly repaired raw collision or order defects by
retaining bounded relational roles and rebuilding the appropriate shell.
Cycles 515/516 showed that exact order and frame characters must be carried,
not discarded.  Cycle 519 showed both a successful tag repair and a
factor-local/global constraint mismatch.  Cycle 522 follows the constructive
side of that history: it changes a bounded representative grammar and re-earns
the fixtures, while the native-coin deletion demonstrates why old coefficients
cannot be silently inherited.  This history argues against substrate or axiom
pressure.

Gate disposition: **PASS for the narrow inherited-coin counterexample; FAIL /
DO NOT SHIP for any broad compiler no-go, minimum-content claim, or axiom
pressure.**

## Six-wall dependency ledger

| wall | Cycle-522 movement | exact remaining obligation |
|---|---|---|
| (C_{\rm ref}) | unchanged; the selected grammar remains fixed-reference and its selector is supplied | reference genesis/preparation and selector derivation |
| (C_{\rm num}) | complete local M64 and full two-cell Fock close; adjacent/seven-cell (N\leq2) isometric without a new tag | widen recurrent adjacent stars beyond (N\leq2) |
| (C_{\rm wrap}) | unchanged; L4 remains rejected and compiler order is not time | recurrent boundary, interval, and causal-time law |
| (C_{\rm int}) | rebuilt dense coin, stream, contact, one seam, and mass re-earn exact intertwiners | primitive coefficient synthesis and multi-edge interaction schedule |
| (C_{\rm local}) | materially advanced: zero-new-M2 adjacent Gram, seven-cell all order, all 24 frames, and held L6 | simultaneous shared-cell constraints and recurrent volume |
| (C_{\rm source}) | unchanged | autonomous conserved source/response and prediction bridge |

The optimal next attack is not another static Gram variant.  It is a primitive
decomposition tournament for the 1,608-term rebuilt local coin against a
three-edge shared-cell recurrence test, with the dedicated-tag route retained
as the independent comparator.  Only a route-independent failure after those
constructive attempts could be considered for broader pressure, and no such
failure exists here.
