# Physical Wilson measurement/reset stabilization — Cycle 535

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_wilson_measurement_reset_stabilization_cycle535_2026_07_21.py`

## Result

Cycle 535 instantiates the Cycle-240 measurement-and-membrane method on Cycle
532's rough, both-parity gauge subsystem and audits the resulting channel
against the complete target matter algebra.  The construction is useful but
does not retire the topological-encoding condition.

For each Wilson `W_a`, let

```text
P_a,+ = (I+W_a)/2,        P_a,- = (I-W_a)/2
```

and let `T_a,p` be the `Z` membrane on the outer stream faces crossing the
periodic plane `p` normal to axis `a`.  The deterministic measurement/reset
channel is

```text
R_a(rho) = P_a,+ rho P_a,+ + T_a,p P_a,- rho P_a,- T_a,p.
```

It is completely positive and trace preserving.  It sends either input
Wilson sign to `W_a=+1`, commutes with every bounded local code constraint,
and preserves both matter parities.  The three channels commute, so their
order need not choose a preferred axis.

The decisive failure is exact.  Each `T_a,p` anticommutes with the `L^2`
mapped matter hoppings on its seam.  For a crossed hopping,

```text
R_a^dagger(A_e)=W_a A_e.
```

Thus deterministic reset changes the encoded target observable before the
Cycle-532 runtime begins.  The corresponding target FSWAP changes from
`F_+` to `F_-` with operator-norm residual 2.  The one-particle mass operator,
onsite Givens generators, contact, and total matter parity survive, but the
Cycle-230 seam and full-Fock Gamma(P) do not.

Using a uniform mixture over all `L` translated membranes removes the
preferred cut at the channel level and makes the correction family covariant
under all 24 proper-cubic frames.  It does not repair matter: one translated
membrane crosses a given stream edge, so the averaged FSWAP residual is
exactly `2/L`—`0.4` at L5 and `1/3` at held L6.  The mixture additionally
requires a shared random cut position.

Postselecting the `+++` measurement outcome avoids membrane feedback and
preserves the matter algebra on the accepted branch.  It is trace decreasing,
has success probability `1/8` only for an explicitly uniform input over the
eight spin sectors, and cannot deterministically encode an unknown target
state by reject-and-retry.

This is a partial constructive result.  It distinguishes a failed
measurement/membrane feedback route from a general preparation obstruction.
A defect-mediated process that leaves the code transiently, a from-scratch
encoder, or a topology-changing code deformation remains open.  There is no
shared obstruction and no axiom pressure.

## Exact target contract

| field | contract |
|---|---|
| Target | form the proper-cubic all-plus Cycle-532 spin sector by bounded local physical operations while preserving the complete six-mode target factor |
| Domain | arbitrary full-Fock target inputs, both total matter parities, finite periodic L5 and held L6 |
| Allowed | fresh local measurement/reset ancillas, local classical outcomes, bounded-support gates, explicitly declared algebraic schedule or autonomous channel |
| Forbidden | host-computed Wilson parity, host-selected string/cut/sector, hidden preferred frame/order, or an unexplained prepared topological resource |
| Required fixtures | full-Fock Gamma(P), one-particle mass, onsite Givens, contact, Cycle-230 seam, inverse, leakage, deletion, lawful domain, all 24 frames and all 576 frame products |
| Completion witness | a literal locally generated `E` or a local convergence theorem whose terminal channel intertwines the complete target matter algebra |
| Not closure | postselection, a growing membrane controller, a covariant random mixture that dephases matter, or a channel that preserves only onsite observables |

## Literal measurement/reset protocol and resources

Cycle 240 already supplied a local Wilson-measurement/global-membrane protocol
for the closed total-even face code.  The fixed-cut implementation on the
rough code uses the same physical mechanism:

1. Initialize three syndrome ancillas, one for each commuting Wilson.
2. Move each syndrome carrier around its declared Wilson loop.  Apply the
   ordered `3L` controlled-`A` factors and the known `i^(3L)` ancilla phase.
   Every `A` factor has M2 support at most 9.  Measuring the carrier gives one
   physical syndrome bit without a host parity reduction.
3. If the outcome is `-1`, broadcast that bit across the selected membrane
   and apply its face `Z` factors in parallel.
4. Reset the bus, broadcast ancillas, and the three syndrome bits.

Every controlled block and face feedback has bounded support and the ancilla
density is constant.  The three loops use `9L` controlled-`A` blocks total.
The signal depth grows as `O(L)` and the worst-case three-axis correction
contains `3L^2` face operations.  The runner treats each at-most-nine-M2
controlled Pauli as one bounded-neighborhood block; its literal one-/two-M2
decomposition is not frozen.  The ordered block network is a local physical
realization of `R_a` at the campaign's bounded-neighborhood resolution, not a
bounded-depth preparation theorem.

The supplied resources are explicit:

- **Measurement outcomes:** three Wilson syndrome bits
  `(s_x,s_y,s_z)`.
- **Reset bath:** fresh cat/broadcast ancillas and erasure after use.  The bath
  is not derived from the current physics axioms and is not called energy or a
  Record.
- **Randomness:** none for a fixed cut; the covariant orbit mixture needs
  three shared random positions `p_a in Z_L`.
- **Periodic boundary conditions:** a finite `L^3` torus.  Fixed cuts use the
  supplied macro origin.  There is no open sink boundary.
- **Schedule:** bounded local Clifford coupling and classical propagation of
  depth `O(L)`.  This compiler latency is not identified with physical time.

The protocol therefore removes host arithmetic but not global physical
communication.  The fixed-cut version uses a supplied cut.  The uniform
orbit version removes that cut only by adding shared randomness and matter
dephasing.

## Exact reset-channel algebra

For every mapped matter observable in the even Pauli algebra, `W_a` is
central.  If `O` commutes with the correction membrane, direct evaluation of
the adjoint channel gives

```text
R_a^dagger(O)=O.
```

If `O` anticommutes with the membrane, it gives

```text
R_a^dagger(O)=W_a O.
```

This identity is the preservation audit; it does not rely on sampling states.
The L5 and held-L6 runner results are:

| quantity | L5 | held L6 | exact law |
|---|---:|---:|---:|
| translated membranes | 15 | 18 | `3L` |
| M2 weight per membrane | 25 | 36 | `L^2` |
| local-check commutator failures | 0 | 0 | 0 |
| Wilsons flipped per membrane | 1 | 1 | 1 |
| matter `B` generators twisted | 0 | 0 | 0 |
| matter `A` generators twisted | 25 | 36 | `L^2` |
| gauge generators twisted | 25 | 36 | `L^2` |
| total matter parity twists | 0 | 0 | 0 |
| fixed-cut FSWAP residual | 2 | 2 | 2 |
| uniform-orbit FSWAP residual | 0.4 | 0.3333333333333333 | `2/L` |

The gauge twists are allowed as gauge motion, but the matter `A` twists are
not: Cycle 532's subsystem theorem makes the full mapped matter algebra act as
target tensor gauge identity.  A correction that changes an `A_e` changes the
target factor, not merely the arbitrary `N-1` gauge state.

## Both matter parities and fixtures

The reset membrane is pure `Z`, as is total matter parity, so their
commutator is zero.  Phase-aware fixed-code ranks again show both total matter
parity signs are nonempty after all three Wilson signs are positive.  Reset
does not project onto one particle-number parity.

This separates what survives from what does not:

- one-particle mass: preserved, because it is an onsite `B`/coin fixture;
- all 15 contact parity-pair words: preserved;
- all onsite internal hopping representatives: preserved;
- both total matter parities: preserved;
- Cycle-230 seam stream: not preserved on a corrected membrane;
- complete full-Fock Gamma(P): not preserved; and
- inherited fixed-spin inverse/leakage: unchanged only after a lawful fixed
  sector has been prepared without the reset twist.

The runner re-executes Cycle 532's L5/held-L6 target-times-gauge ranks, Cycle
529 full-Fock target replay, and logical mass/contact/seam comparators.  Those
all still pass for the unchanged fixed-spin code.  They are not attributed to
the new reset channel; its seam residual is separately nonzero.

## Covariance and preferred-cut audit

At L3 the complete set of all translated membranes contains `3L=9` members.
All 216 membrane/frame images—`9*24`—remain exactly inside that set.  The
uniform orbit channel is therefore proper-cubic covariant as a channel and
needs no active runtime frame selector.

A fixed triple of cuts is different.  Of the 72 fixed-cut/frame cases, 36
leave the chosen triple.  It is a presentation with a preferred cut even
though the three axis labels are treated symmetrically.  This agrees with the
Cycle-269 distinction between the intrinsic Wilson center and a chosen
membrane basis.

Cycle 532's fixed all-plus code action is rerun on all 24 frames and all 576
frame products.  The new result does not weaken that covariance.  It shows
that one deterministic feedback implementation lacks it, while the orbit
average restores it at the cost of shared randomness and exact matter noise.

## Bounded lawful-jump exhaustion and light-cone boundary

The runner exhausts every Pauli operator supported inside an axis-aligned
owner-cell cube of width `w<L`.  It does this by solving the complete GF(2)
system for:

```text
[Q,S_j]=0 for every bounded local constraint S_j,
{Q,W_a}=0 for one requested Wilson W_a.
```

This is not a low-weight sample; for a support of `k` M2 factors the linear
solve covers all `4^k` Paulis.  For every `w=1,...,L-1` and all three Wilsons,
there is no solution at L5 or held L6.

| L | tested cube widths | largest proper cube | Pauli search log2 at largest cube | lawful flipper found |
|---:|---|---:|---:|---:|
| 5 | 1,2,3,4 | 1,408 M2 | 2,816 | 0 |
| 6 held | 1,2,3,4,5 | 2,750 M2 | 5,500 | 0 |

Translations and proper-cubic frames carry these boxes into equivalent
contractible boxes.  Hence a channel built only from bounded Pauli jumps that
remain in the local-check code after every jump conserves all three Wilson
signs.  It cannot stabilize `+++` from an arbitrary initial sector.

This is deliberately narrow.  A local defect-mediated sequence can violate
some checks temporarily, move the defects around a noncontractible cycle,
and annihilate them.  Such a process may realize a membrane after growing
latency.  The scan does not exclude it, does not prove its convergence, and
does not show how it would preserve the target state.  That is the live
autonomous route.

## Deletion and lawful-domain controls

- Deleting feedback entirely leaves Wilson populations unchanged; it is a
  nondestructive measurement, not an initializer.
- A complete membrane has zero local-check syndrome and flips exactly its
  paired Wilson.
- Deleting one face from the membrane produces four local-check syndromes and
  no longer flips that Wilson at both L5 and held L6.
- Fixed-cut feedback twists exactly `L^2` stream generators per corrected
  axis; deleting the feedback avoids the twist only by abandoning reset.
- The uniform orbit channel has exact nonzero FSWAP residual `2/L`; the
  residual is not hidden as finite-size noise.
- Postselection preserves the accepted branch but is not trace preserving.
- Deterministic reset discards three spin-sector bits into the reset bath and
  is not invertible.  Cycle 532's runtime inverse remains exact only after a
  correct fixed-sector encoding has been supplied.

These distinguish measurement, reset, local-code leakage, matter leakage,
and stochastic averaging rather than combining them into one success flag.

## Supplied structure and novelty boundary

Supplied rather than derived are the Cycle-532 rough code, its three Wilson
representatives, finite periodic domains, the membrane orbit, fixed macro
origin when fixed cuts are used, local syndrome ancillas, their reset bath,
the cat/walking-ancilla schedule, and shared cut randomness in the covariant
mixture.

Not supplied are a host-computed parity, a runtime frame selector, or a claim
that the syndrome bits are Records.  No semigroup parameter or circuit layer
is called physical time, no generator element is called a rate, no wrapped
phase is called energy, and no gravity/source/Born law is inferred.

Cycle 240 previously constructed bounded local check/Wilson measurements,
global outcome feedforward, `L^2` membrane corrections, `1/8` Wilson
postselection, and a coherent-dilation boundary for the closed even code.
Cycle 269 constructed the membrane pairing and established that conjugate
membranes act on matter rather than a spectator `M_8` factor.  Cycle 535 does
not claim either mechanism as new.  The new fixture-specific content is:

1. the exact channel lift to the Cycle-532 both-parity rough gauge subsystem;
2. its Heisenberg matter-twist identity on that subsystem;
3. the L5/held-L6 full-Fock parity, seam, and gauge-motion census;
4. the all-24 translated-membrane orbit versus fixed-cut covariance audit;
5. the exact `2/L` covariant random-mixture residual; and
6. the exhaustive contractible lawful-Pauli-jump scans through width `L-1`.

No general topological-state-preparation theorem or novelty priority is
claimed.  Thirring machinery is not used or compared.

## Dependency disposition

- `C_ref`: unchanged.  The fixed-cut reset replaces the supplied Wilson sign
  with a supplied cut and reset controller; the covariant variant replaces it
  with shared randomness and matter noise.
- `C_num`: unchanged.  Both target parity sectors remain exact.
- `C_wrap`: sharper.  Wilson outcomes, cat propagation, and reset iterations
  are not time, energy, winding history, or Records.
- `C_int`: split.  Mass, onsite Givens, and contact survive; the seam and full
  B matching fail under deterministic or averaged reset.
- `C_local`: advances diagnostically.  A literal bounded-gate reset channel,
  exact matter action, covariant membrane orbit, and contractible-jump scan
  are now available.  A matter-preserving autonomous initializer remains
  open.
- `C_source`: unchanged.

Maturity scores are unchanged by a partial preparation result: operational
quantum/records `2/5`, time `1/5`, inertia/matter `3/5`, gravity/source `2/5`,
and Born/probability `1/5`.

## No-go discipline N1–N8

Broad no-go gate status: **FAIL / DO NOT SHIP**.  The disposition is
`partial-attempt-with-named-untested-routes`.  The narrow result is that the
displayed measurement/membrane reset, covariant random mixture, and
code-preserving bounded Pauli-jump families do not retire
`W_topological-encoding`.

### N1 — alternative-route normalization

| family | object / mechanism / terminal obligation | status |
|---|---|---|
| fixed-cut measurement and feedback | Wilson projectors plus one conjugate membrane / deterministic sign reset / preserve full matter and cubic covariance | **ATTEMPTED** — sets `+++`, but twists `L^2` matter hoppings and uses a preferred cut |
| measurement with postselection | trace-decreasing `+++` projector / discard wrong outcomes / deterministic unknown-input encoder | **ATTEMPTED** — matter-perfect only on the accepted branch; no deterministic arbitrary-input map |
| covariant randomized feedback | uniform translated-membrane channel / orbit symmetry / exact matter intertwiner without shared global choice | **ATTEMPTED** — all-24 covariant, but requires shared randomness and leaves residual `2/L` |
| code-preserving local autonomous pumping | bounded lawful Pauli jumps / remain in the code at every step / change Wilson sign | **ATTEMPTED** — exhaustive proper-cube GF(2) scans find no lawful flipper at L5/L6 |
| defect-mediated autonomous pumping | local syndrome defects / leave code, wind, and annihilate / biased convergence to `+++` while restoring arbitrary matter | **OPEN — NOT CLOSED** |
| topology-changing code deformation | temporarily open/fill three cuts or punctures / unique-sector growth / homogeneous periodic final encoder | **OPEN — NOT CLOSED** |
| from-scratch coherent encoder | target input plus reset ancillas / local Clifford or non-Clifford growth / prepare one fixed spin representation without measuring an unknown sector | **OPEN — NOT CLOSED** |
| finite-light-cone operational quotient | arbitrary Wilson sectors / local indistinguishability before wrap / exact declared experiment domain | **OPEN — TARGET REFRAME, NOT CLOSED** |

These are distinct in object, mechanism, and terminal obligation.  The open
defect, deformation, coherent-encoder, and operational routes forbid a broad
negative.

### N2 — wall-independence audit

Raw labels—Wilson measurement, sign correction, state preparation, target
preservation, and fixed-spin encoding—collapse to the same condition:

```text
W_topological-encoding:
form the all-plus periodic spin representation by bounded local physical
operations while intertwining the complete target matter factor.
```

Measurement alone does not close it; correction without target preservation
does not close it; from-scratch encoding could close all labels at once.  The
reset bath and shared randomness are supplied resources of the tested
protocols, not separately asserted physics walls.  Literal optimization of
cat routing is downstream once a matter-preserving channel exists.

### N3 — hidden-wall scan

The mandatory scan covers “we assume,” “by construction,” “as is standard,”
“the framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical.”  None discharges a
proof obligation.  Periodic topology, macro origin, chosen cut, Wilson
representatives, fresh ancillas, reset/erasure, measurement outcomes, shared
randomness, growing signal depth, and the inherited Cycle-532 code are all in
the supplied inventory.  “Autonomous” is not applied to the global membrane
channel.

### N4 — residual matching

| witness | witness residual | Cycle-535 use | match? |
|---|---|---|---:|
| `PHYSICAL_ROUGH_GAUGE_SUBSYSTEM_QUOTIENT_CYCLE532_NOTE_2026-07-21.md:238-284` | three Wilson signs remain a supplied topological initialization | direct target of the reset protocol | yes |
| `MEASUREMENT_FEEDFORWARD_SQUARE_PYRAMID_PREPARATION_CYCLE240_NOTE_2026-07-17.md:27-136` | local Wilson measurement, global membrane feedback, `1/8` postselection, and growing communication | direct protocol predecessor; Cycle 535 changes the code/domain and audits full matter preservation | yes |
| `WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md:213-269` | `L^2` membrane flips one Wilson and matter seam hoppings | same membrane mechanism in the rough code | yes |
| `WILSON_SUBSYSTEM_SECTOR_FREE_COMPILER_CYCLE269_NOTE_2026-07-17.md:342-355` | fixed membrane basis is not covariant; Wilson center is | fixed-cut versus orbit audit | yes |
| `PHYSICAL_CORRELATED_DOUBLE_SHADOW_STREAM_CYCLE529_NOTE_2026-07-21.md:103-123` | full-Fock B requires exact exchange sign | nonzero reset seam residual rejects preservation | yes |
| Cycle 247 diagonal boundary-Z selectors | boundary multiplicity/gauge selection | autonomous measurement/reset convergence | no; dropped as proof |

The new negative is not inferred from Cycle 247's different diagonal-selector
search.

### N5 — rhetoric audit

| resolution | tested result |
|---|---|
| one Wilson measurement | exact nondemolition projector algebra |
| one correction face deleted | four local syndromes and lost Wilson flip |
| one complete membrane | lawful, one Wilson flip, weight `L^2` |
| one crossed hopping/FSWAP | `W_a A_e` twist and operator-norm residual 2 |
| one translated-membrane orbit | all-24 closure; averaged residual `2/L` |
| contractible owner cubes | every Pauli in widths `1,...,L-1` exhausted at L5/L6 |
| fixed code | inherited all-24/576 covariance and both matter parities |
| complete runtime | inherited target exact, new reset not intertwining |
| defect-mediated sequence | not completed; no negative closure claimed |
| arbitrary local quantum channel/from-scratch encoder | not exhausted; no general no-go claimed |

Accordingly the note says the displayed reset families fail, not that Wilson
initialization is impossible or that local dissipative preparation cannot
work.

### N6 — partial-closure path

The postselected branch is an exact partial closure: it preserves matter after
an accepted `+++` result but lacks deterministic arbitrary-input success.  The
translated membrane orbit closes proper-cubic covariance but not target
preservation.  The contractible-jump scan isolates the needed new mechanism:
leave the code transiently or prepare the fixed representation from scratch.

Candidate retirement paths are a defect-pair cellular automaton with a proved
`+++` bias and matter intertwiner, code deformation with a locally generated
temporary boundary, a coherent encoder whose ancillas start in a declared
product/reset state, or an exact finite-light-cone operational target.  These
are constructive paths and do not request an axiom edit.

### N7 — hostile steelman

> A hostile reviewer should reject any inference that local autonomous
> preparation is obstructed.  The lawful-jump scan deliberately forces every
> intermediate operation to commute with the code checks, while topological
> code preparation normally creates mobile defects, transports them, and
> annihilates them only at the end.  The matter-twist calculation begins from
> an arbitrary already encoded Wilson sector; a from-scratch encoder can
> correlate target input and ancillas so that no unknown-sector correction is
> ever applied.  Cycle 532 already supplies the exact target-times-gauge
> factor once the sector is formed.  The actionable next mechanism is a local
> defect/code-deformation protocol with an explicit convergence and
> intertwining proof, not a new premise.

This concrete route and terminal obligation make a broad no-go premature.

### N8 — cross-cycle echo

Cycle 235 moved global fermionic ordering into three spin/Wilson characters.
Cycle 240 built bounded local measurements but exposed global sign decoding,
Wilson membranes, postselection, and coherent-dilation latency; its closed
code still lacked odd parity.  Cycle 244 found local sparse-basin syndrome
decoders but kept Wilson selection separate.  Cycle 247 then opened odd parity
with rough terminals but left multiplicity.  Cycle 269 showed that membrane
conjugates change matter and that a chosen cut is not covariant.  Cycle 271
retired Wilson selection for contractible pre-wrap observable nets but not for
global preparation.  Cycle 263 separately showed that local state preparation
and local CAR updates can trade walls across encodings.  Cycle 529 made the B
runtime exact while leaving global chart preparation.  Cycle 532 removed that
chart and typed the rough multiplicity as a local gauge factor, leaving only
the three signs.

Earlier global-looking walls were narrowed by adding a gauge carrier,
puncture, or stateful auxiliary sector.  Defect-mediated deformation is the
corresponding untested mechanism here.  The cross-cycle echo therefore blocks
axiom pressure.

## Disposition and next campaign

Retain three exact pieces:

1. the Cycle-240 measurement network instantiated on the rough both-parity
   code with its explicit measurement/reset resources;
2. the exact deterministic reset law and matter-twist certificate; and
3. the covariant membrane orbit plus exhaustive contractible lawful-jump
   boundary.

Do not call the deterministic channel a compiler: it preserves both matter
parities, mass, onsite Givens, and contact, but fails the Cycle-230 seam and
full-Fock Gamma(P).  Do not call the orbit average autonomous or local without
supplying its shared random coordinate and broadcast law.

The optimal next campaign is a defect-mediated or code-deformation protocol
that starts from target matter plus reset ancillas, allows explicitly tracked
temporary syndromes, and ends in the all-plus rough code.  Its terminal test
must prove the complete target algebra intertwiner, not merely Wilson
convergence, then replay L5/held L6, all 24/576, mass/contact/seam, inverse,
leakage, deletion, and lawful-domain controls.
