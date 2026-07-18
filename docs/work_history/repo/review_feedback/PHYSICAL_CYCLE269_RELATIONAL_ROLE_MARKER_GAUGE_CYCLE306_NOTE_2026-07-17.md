# Physical Cycle-269 relational role-marker gauge — Cycle 306

Date: 2026-07-17
Branch: `codex/bare-metal-mvp-probes-20260713`
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

```text
scripts/physical_cycle269_relational_role_marker_gauge_cycle306_2026_07_17.py
```

This cycle changes no axiom, foundation, Qualification, primitive, registry,
policy, queue, or audit status.

## Result up front

Cycle 306 replaces the Cycle-304 supplied free phase flag by a locally
constrained relational carrier-role marker on the same fixed-seam `n=1+n=2`
comparator.

Let `K_exchange` be the signless, collision-safe local branch exchange on the
ninety Cycle-304 microsectors. It is the exact bounded matrix-unit analogue of
`X_flag R`: `R` exchanges the face/occupation/port carrier representatives and
`X_flag` exchanges their displayed Cycle-304 flag values. A standalone
selector

```text
K_exchange = +1
```

does not preserve the intended code. Its intersection with the forty-two
column common shell has dimension twenty-one. It also has nonzero commutators
with the active-slice coin and contact. This is an exact disposition of that
one selector, not a no-go for non-diagonal local gauges.

Add one additional ordinary M2 `r` at every cell and impose the bounded local
constraint

```text
C_role = K_exchange X_r = +1.
```

If `E_304` is the Cycle-304 isometry, the new isometry is

```text
E_306 = ( E_304 |0>_r + K_exchange E_304 |1>_r ) / sqrt(2).
```

The inherited common-shell projector tensored with `I_r` has rank 84. It
commutes with `(I+C_role)/2`, and their product is exactly
`E_306 E_306^dagger`, with rank and trace exactly forty-two. Thus `r` is not
another free flag. It supplies the gauge partner that the standalone selector
lacked.

The gauge-invariant physical marker is

```text
M_role = Z_slice Z_r.
```

Its eigenvalue is `+1` on the twenty-one input-slice logical columns and `-1`
on the twenty-one separated-slice columns. The physical stream/catch-up
anticommutes with `M_role` and therefore updates the marker autonomously. The
coin and contact commute with it. No host-side branch control is used.

For every Cycle-304 bounded physical block `A`, use the physical-`r`-controlled
completion

```text
A_306 = A |0><0|_r + K_exchange A K_exchange |1><1|_r.
```

This operator commutes with `C_role` identically and satisfies

```text
A_306 E_306 = E_306 A_logical.
```

The identity holds separately for the Cycle-219 coin, collision-safe
stream/catch-up, Cycle-230 local contact, and their declared coin-then-stream-
then-contact composition, including held `beta=-0.35`. The one-particle mass
fixture and contact firewall are unchanged.

This is the strongest constructive marker result in this route. It is a
fixed-seam comparator, not a recurrent-volume compiler. It does not repair the
Cycle-304 measured separated-cell recurrence leakage, compile the rank-73 sea,
or extend the code to the missing Fock sectors.

## Exact construction

Write the Cycle-304 physical coefficient space as `H_90`. The signless
exchange obeys

```text
K_exchange^2 = I,
[K_exchange, P_304] = 0,
```

where `P_304=E_304 E_304^dagger`. The actual physical stream is the same
exchange with the already-derived number-sector signs: `-1` on the `n=1`
half-stream branches and `+1` on the declared `n=2` wedge branches.

On `C^2_r tensor H_90`, define

```text
C_role = X_r tensor K_exchange,
P_shell = I_r tensor P_304,
Q_role = (I+C_role)/2.
```

Then

```text
[P_shell,C_role] = 0,
rank(P_shell) = 84,
rank(P_shell Q_role) = 42,
P_shell Q_role = E_306 E_306^dagger.
```

The two branches of `E_306` are not two host-selected cases. They are one
coherent local code state. The `r`-basis projectors in `A_306` are physical
local projectors, and the runner verifies the complete operator rather than
querying a branch label outside the substrate.

The completion is multiplicative:

```text
Phi(A) Phi(B) = Phi(AB),
Phi(A) = A |0><0|_r + KAK |1><1|_r.
```

Therefore the separate intertwining identities compose without another
schedule choice. Unitarity and inverses are inherited exactly from each
Cycle-304 block.

## Local constraint and physical support

`C_role` is not claimed to be a single Pauli stabilizer. It is an explicit
non-diagonal local constraint formed from ninety orthogonal matrix units. Each
term exchanges one Cycle-304 face/tag/flag representative and applies `X_r`.
The same local projectors used by the Cycle-302/Cycle-304 matrix-unit grammar
make the sum an exact Hermitian involution.

The runner checks the physical Pauli transition word for all ninety terms.
Every word commutes with every inherited `B_v Z_port(v)=+1` constraint and
every fixed local/Wilson-sector stabilizer. The bounds at both training `L=3`
and held `L=6` are:

```text
face M2 in bounded patch                    30
port M2 in bounded patch                    12
role-marker M2                               2
bounded patch union                         44 M2
maximum exchange transition support         22 M2
maximum encoded branch representative       19 M2
installed homogeneous overhead              23 M2/cell
```

The two role-marker sites are the inherited Cycle-304 flag site and the new
ordinary `r` site. All support and overhead are constant in lattice size.
In words, the constraint occupies a forty-four M2 bounded patch with
twenty-three M2 per cell of homogeneous installed overhead.

## Covariance, translations, and held size

`K_exchange` commutes with the direct sum of the ordinary ordered-pair and
signed wedge representations. `r` is a scalar cell role. Therefore
`C_role`, `M_role`, `E_306`, and every completed operator are covariant under
all 24 proper-cubic frames. The runner tests the complete coefficient
operators and the homogeneous physical placement of every `r` site.

All 27 L=3 translations map the ninety face/tag/flag branches and the added
`r` site to the corresponding translated patch with zero phase, tag, slice,
or placement failures. Held L=6 repeats the support, inherited-constraint,
fixed-sector, and matrix-unit tests. Translation and frame maps are still the
declared Cycle-269 framing repair; they are not reinterpreted as dynamics.

## Coin, stream, contact, and mass firewall

For `beta=-0.2,-0.3,-0.4` and held `beta=-0.35`, the runner evaluates:

```text
E_306^dagger E_306 - I,
A_306 E_306 - E_306 A_logical,
[A_306,C_role],
(I-E_306 E_306^dagger) A_306 E_306,
A_306^dagger A_306-I.
```

It does so for coin, stream/catch-up, contact, and the declared composition.
All printed residuals are below `1e-11`.

The encoded uniform `n=1` scalar retains the Cycle-219 mass fixture. The
Cycle-230 `g=0.37` contact is still exactly identity on all `n=1` columns and
acts on the onsite `n=2` slice only. Exchanging contact and stream remains
detectably different. This preserves the Cycle-304 schedule rather than
silently commuting the two laws.

The contact phase is not called mass, physical energy, or a rate. The two
marker eigenvalues are not clock readings or physical time. The coherent
gauge marker is code data, not a Record.

## Leakage and deletion controls

The positive construction is accompanied by independent destructive controls:

- deleting `C_role` leaves the shell-times-`r` space with dimension 84 rather
  than 42;
- deleting the `r` partner from the constraint reduces it to the bare
  selector and produces order-one leakage on `E_306`;
- deleting `K_exchange` from the constraint also produces order-one leakage;
- applying the same un-conjugated coin or contact in both `r` branches breaks
  constraint preservation and leaks from the 42-column code;
- deleting `K_exchange` from the physical stream removes the role update and
  breaks the logical stream intertwiner; and
- repeated-mode, invalid-port, and aliased `L=2` inputs are rejected.

These controls distinguish local constraint enforcement from mere
preservation of a declared list of columns.

## Route-by-route disposition

| route | disposition |
|---|---|
| diagonal `Z_flag f(face,occupation,ports)` with no new register | the displayed `n=1` data have 30 patterns and every pattern occurs with both flag values; this exact grammar cannot retain both copies while fixing one diagonal flag value |
| standalone non-diagonal `K_exchange=+1` | bounded and covariant, but its common-code `+1` space has dimension 21 and it does not commute with the active coin or contact |
| one-extra-M2 relational gauge `K_exchange X_r=+1` | constructive: exact dimension 42, commuting bounded local constraint, autonomous marker update, all-frame covariance, translation and held-size closure |
| two-marker diagonal repetition code | live but unnecessary for this result; not used as evidence against the non-diagonal construction |
| larger direction-orbit or clocked marker register | live and untested here; no negative conclusion is drawn |

The successful third route is precisely why the first two failures are not a
shared substrate obstruction.

## Supplied structure and novelty boundary

Supplied are:

1. the fixed `+++` Wilson reference ray and Cycle-269 local sector;
2. the Cycle-304 42-column fixed-seam shell and its ninety local
   face/tag/flag representatives;
3. the Cycle-302 local projector/matrix-unit grammar and framing-cocycle
   repair;
4. the Cycle-219 coin and its declared two-particle exterior lift;
5. the Cycle-230 `g=0.37` local contact and the declared
   coin-stream-contact schedule;
6. one additional homogeneous ordinary `r` M2 per cell;
7. the dense ninety-term `C_role` constraint candidate and the dense
   branch-conjugated matrix-unit coefficients;
8. the common-shell projector, initial lawful code state, macrocell origin,
   and framing maps.

Derived are the rank-42 relational code, constraint involution/rank and
commutators, gauge-invariant marker, autonomous update, separate and composed
intertwiners, covariance, translations, held size, support, leakage, deletion,
and mass firewall.

There is no global Jordan–Wigner ordering, nonlocal parity service, copied
tag, or host-side branch control. Dense primitive synthesis is still supplied;
the physical `r` projectors are local substrate controls, not an external
conditional.

Local auxiliary stabilizer/subsystem encodings and local fermion-to-qubit
matrix-unit completions are prior-art territory. Cycle 306 claims only this
explicit relational completion on the repository's Cycle-304 comparator.
Global novelty is not established. No result uses or compares with the
Thirring engine.

## Remaining boundary

The locally free carrier-role flag is retired on the declared 42-column
fixed-seam code. The following tasks are separate and remain open:

- primitive synthesis of the dense bounded matrix-unit constraints and laws;
- absolute vacuum and arbitrary coherent-position preparation;
- a recurrent volume update closed under the actual separated-cell coins;
- simultaneous overlapping patches and Fock sectors `n=0,3,4,5,6`;
- a rank-73 principal-sea physical compiler;
- removal or local dynamical selection of the fixed Wilson reference; and
- any energy, gravity/source/resource, probability, or realized-history law.

The result supplies no axiom pressure.

## No-go discipline gate

The proposed broad negative tested by the gate was: "no bounded local marker
grammar can retain all 42 Cycle-304 columns." The gate rejects that statement,
because the one-extra-M2 relational construction is a counterexample. The two
negative controls above are retained only as exact matrix/rank statements.

**Broad gate status: FAIL / DO NOT SHIP.** There is no shared obstruction and
no axiom pressure.

### N1 — alternative-route enumeration

| route | status | result |
|---|---|---|
| diagonal tie to existing displayed face/occupation/port data | **ATTEMPTED** | exact 30/30 two-valued collisions |
| standalone non-diagonal exchange selector | **ATTEMPTED** | rank 21 and active coin/contact commutators |
| one-extra-M2 relational exchange gauge | **ATTEMPTED** | succeeds with rank 42 |
| one shared spectator tied independently to six local roles | **RULED OUT BY PRIOR RESULT** | Cycle 248 lines 137–141 gives six independent equalities and code exponent one |
| diagonal two-marker repetition code | **OPEN / UNTESTED** | distinct local stabilizer alternative; no closure claim |
| six-state direction-orbit role register | **OPEN / UNTESTED** | could encode a larger covariant carrier label |
| time-multiplexed local marker schedule | **OPEN / UNTESTED** | could trade onsite register structure for an explicit phase schedule |

The open routes and the successful relational route make the broad negative
gate fail. The cycle is constructive.

### N2 — wall-independence audit

The remaining conditions after local marker enforcement are `W_prim` (dense
primitive synthesis), `W_rec` (actual recurrent-volume closure), `W_prep`
(absolute/coherent-position preparation), and `W_Fock` (missing number
sectors). The complete directional implication audit is:

| source wall | target wall | automatic implication? | separator |
|---|---|---:|---|
| `W_prim` | `W_rec` | no | a primitive local block need not close the separated-cell orbit |
| `W_rec` | `W_prim` | no | a dense recurrent matrix can exist without a primitive decomposition |
| `W_prim` | `W_prep` | no | gate synthesis does not prepare the fixed reference or coherent input |
| `W_prep` | `W_prim` | no | a prepared state does not synthesize its update law |
| `W_prim` | `W_Fock` | no | one block synthesis does not add missing number sectors |
| `W_Fock` | `W_prim` | no | a larger state space does not decompose the dense blocks |
| `W_rec` | `W_prep` | no | orbit closure does not prepare an arbitrary input |
| `W_prep` | `W_rec` | no | preparation does not make independent separated-cell coins orbit-closed |
| `W_rec` | `W_Fock` | no | recurrence on `n=1+n=2` does not construct `n=0,3,4,5,6` |
| `W_Fock` | `W_rec` | no | adding sectors does not close the current separated pair orbit |
| `W_prep` | `W_Fock` | no | preparing the present code does not enlarge its number content |
| `W_Fock` | `W_prep` | no | sector completion does not supply absolute or coherent-position preparation |

The fixed Wilson reference is an additional explicit import, not silently
pooled into those four implementation walls.

### N3 — hidden-wall scan

The synthesis runner searches all four Cycle-306 release paths for the ten
prohibited hidden-premise phrase families. The literal hit count is zero. The
common-shell projector, dense ninety-term constraint, fixed reference,
coefficients, schedule, and initial code state are explicit supplied
structure.

### N4 — residual matching

| witness with exact location | witness residual | Cycle-306 use | match? |
|---|---|---|---:|
| `PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md:112` | deleting one equality changes rank | deletion of `C_role` changes 42 to 84 | yes |
| `PARITY_DOUBLING_SPECTATOR_COMPILER_CYCLE248_NOTE_2026-07-17.md:115` | omitted spectator transport leaks by `sqrt(2)` | deleting `K_exchange` yields stream residual 2 | yes |
| `COHERENT_GAMMA_PARITY_SECTOR_DOUBLING_CYCLE264_NOTE_2026-07-17.md:27` | correct exponent is distinct from faithful algebra, covariance, and preparation | Cycle 306 tests rank, operations, covariance, and names preparation separately | yes, methodological |
| `DRESSED_SPOKE_PARITY_GAUGE_CYCLE273_NOTE_2026-07-17.md:39` | a rank-`N-1` commuting family can still lose frames and matter algebra | Cycle 306 separately tests all frames and completed matter laws | yes, methodological |
| `PHYSICAL_CYCLE269_JOINT_SIX_MODE_COIN_LIFT_CYCLE302_NOTE_2026-07-17.md:46` | local tag-projector matrix units and auxiliary checks form the physical completion | Cycle 306 uses and rechecks that exact local grammar | yes |
| `PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md:89` | 30 unflagged patterns each occur with both flag values | Cycle 306 reruns the same 30/30 collision | yes |

Cycles 264 and 273 are not cited as evidence that this local 42-column marker
must fail. Their residuals are broader full-Fock/gauge problems.

### N5 — rhetoric and resolution audit

| claim surface | microsector | 42-column shell | bounded patch | lattice-wide | outside tested resolution |
|---|---:|---:|---:|---:|---|
| diagonal existing-data collision | all 60 `n=1` flagged representatives | both 12-column `n=1` slices retained | one body-neighbor patch | translations replay the same local collision | added registers and non-diagonal laws remain outside this statement |
| bare-selector rank | all 90 sectors | exact `+1` intersection rank 21 | selector is bounded | frame/translation covariance tested | larger-register selectors remain outside this statement |
| relational constraint | all 90 exchange terms | exact joint rank 42 | union 44 M2, term support at most 22 | all 24 frames, all 27 L=3 translations, held L=6 locality | simultaneous overlapping patches remain untested |
| completed laws | dense coin, stream, and contact blocks | separate/composed residuals below tolerance | bounded matrix-unit completion | frame and translation covariance tested | primitive gate synthesis and recurrent volume remain untested |

### N6 — partial-closure path scan

The one-extra-M2 relational gauge is the partial-closure path: it turns an
explicit free-flag import into a bound theorem with one extra local resource
and one explicit constraint. No convention change or axiom is needed. The
remaining fixed reference, dense synthesis, preparation, recurrence, and Fock
extensions stay named rather than being promoted to constitutional language.

### N7 — steelman

Reject the broad negative. The bare selector loses a factor of two only
because it fixes the exchange eigenvalue without a gauge partner. One local
companion restores that factor, while physical-`r` branch conjugation makes
every comparator law centralize the constraint. Cycle 306 executes this
counterexample. Larger repetition, direction-orbit, subsystem, and scheduled
marker grammars also remain available.

### N8 — cross-cycle echo

Cycle 248 found that deleting spectator transport causes local-code leakage;
Cycle 306 supplies and tests the missing autonomous exchange. Cycle 273 found
that matter dressing retired a predecessor's reference-only leakage and moved
the residual rather than proving a shared obstruction. The same pattern
occurs here: the Cycle-304 free-flag residual is retired by a larger local
gauge grammar. Past route failures therefore provide no axiom pressure.

Gate disposition: **FAIL / DO NOT SHIP for the proposed broad negative.** The
two route-specific matrix/rank controls remain lawful diagnostics only.

## Six-wall ledger

| wall | Cycle-306 change | residual |
|---|---|---|
| `C_ref` | unchanged; every column remains relative to one supplied fixed `+++` Wilson ray | absolute preparation, cross-Wilson equivalence, and physical reference genesis |
| `C_num` | exact rank/trace 42 after the new constraint; both `n=1` and `n=2` comparator slices retained | missing Fock sectors and rank-73 principal sea |
| `C_wrap` | unchanged; the role marker and compiler schedule are not time | physical event equivalence, clock selection, recurrence, interval, and rate calibration |
| `C_int` | coin, stream/catch-up, contact, and fixed-seam composition all preserve `C_role`; mass firewall retained | actual separated-cell recurrence and volume-wide intertwiner remain open |
| `C_local` | the free role-flag clause is retired by one extra M2 and `C_role`; 23 M2/cell, 44-M2 patch, 22-M2 transition bound, frames, translations, held size, leakage, and deletion close | dense primitive synthesis, common-shell projector, initial code state, arbitrary preparation, recurrence, and overlapping patches remain supplied/open |
| `C_source` | unchanged | no energy, action, stress, gravity/source, resource, or realized-history law selected |

## TOE lane update

These are evidence-weighted planning scores, not probabilities or audit
verdicts. The increase is narrow because local role enforcement was an
explicit success-contract clause; recurrence, preparation, full Fock,
occurrence, and source remain open.

| TOE lane | integrated | strict floor | conditional | maturity | disposition |
|---|---:|---:|---:|---:|---|
| operational quantum / Records | 59% | 26% | 82% | 3.1/5 | raised narrowly: one exact local auxiliary constraint now selects and preserves the 42-column comparator; occurrence and Record remain open |
| causal time / clock | 33% | 17% | 60% | 1.7/5 | unchanged: marker values and schedule order are not events, clocks, or intervals |
| inertia / matter | 67% | 30% | 87% | 3.6/5 | raised narrowly: the locally enforced comparator preserves the coin/contact/mass firewall; recurrence, higher sectors, and dressed inertia remain open |
| gravity / source / resource | 38% | 15% | 63% | 1.9/5 | unchanged: no source or response observable is selected |
| Born / probability / realized history | 33% | 14% | 79% | 1.7/5 | unchanged: coherent code amplitudes are not occurrence or probability |

## Optimal next probe

Use the now-constrained marker as an input to the actual recurrent separated-
cell coin problem. Start from the measured Cycle-304 leakage
`0.9929474834848379` and enlarge the output orbit only by complete
proper-cubic/translation orbits. Demand closure under independent onsite
coins at the two separated cells, then rerun contact, marker constraints,
support, deletion, and held-size tests before adding another Fock sector.
