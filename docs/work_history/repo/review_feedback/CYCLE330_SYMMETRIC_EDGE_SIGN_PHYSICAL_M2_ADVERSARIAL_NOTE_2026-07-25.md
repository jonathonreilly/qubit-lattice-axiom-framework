# Cycle-330 symmetric edge sign: physical-M2 adversarial synthesis

Date: 2026-07-25
Status: **bounded exact-three-data-M2 no-unitary; N1-N8 PASS**
Authority: **none**
Audit: **unset**

## Result

The corrected bounded postproduct classifier is

```text
s = x_outer (1-tag_u) (1-tag_v).
```

It is exact on the landed Cycle-311/315 branch grammar and repairs the failed
first-round extrapolation

```text
s_old = x_outer z_outer (1-tag_u) (1-tag_v).
```

The corrected root candidate appropriately calls its eight-entry diagonal a
coefficient/ray-space translator and leaves a physical matrix-unit synthesis
open.  This audit tests that stronger open question.  No unitary on just the
outer-edge `M2` and its two endpoint-tag `M2`s realizes the translator on the
landed physical state vectors.

The obstruction is specific.  Every arm has a positive vacuum ray and a
negative `n_L=n_R=1` ray with endpoint tags `00`.  None of the shared edge's
single-factor `X`, `Z` or `Y` is in the fixed-Wilson vacuum stabilizer, so both
rays have local marginal

```text
rho_edge,tags = I_edge/2 tensor |00><00|_tags.
```

Exact action on the positive ray forces the local operator to restrict to
`+I` on this two-dimensional support; exact action on the negative ray forces
`-I` on the same support.  The physical matrix-unit equations have
coefficient rank 4 and augmented rank 5.  They have no exact solution, even
before unitarity is imposed.

This is a counterexample to the three-`M2` physical route, not a no-go for a
larger bounded support, clean physical syndrome registers, or an
ancilla-assisted extraction and uncomputation circuit.

## Corrected versus legacy sign

On the six interior Cycle-330 center-arm fixtures, the corrected and legacy
classifiers coincide because no positive `(x,z,t_u,t_v)=(1,0,0,0)` row occurs
there.  A fixed periodic-seam witness separates them without a refit:

- L5: outer edge 74, bodies `(0,0,4)` and `(0,0,0)`, modes 4 and 5;
- held L6: outer edge 89, bodies `(0,0,5)` and `(0,0,0)`, modes 4 and 5;
- logical labels `n_L=n_R=1`, each with mode label `(0,)`;
- term pairs `(6,9)` and `(7,8)` have local pattern `(1,0,0,0)` and physical
  order sign 1 at both sizes;
- the corrected classifier returns 1;
- Route B's six-term diagnostic returns 1 through monomial 4;
- the legacy `x*z` classifier returns 0.

The legacy formula is retained only as a failed extrapolation control.

## Label space is not state space

The corrected table uses the three bits `(x_outer,tag_u,tag_v)`, so its label
dimension 8 now matches the Hilbert dimension of three physical `M2`s.  The
remaining defect is not dimensional.

On the tag-`00` slice, the table fixes the `I,Z` preparation labels and negates
`X,Y`.  This is conjugation by `Z` on one-`M2` operator coordinates; its Choi
eigenvalues are `(0,0,0,2)`.  But the desired state-vector action is left
action on `P|vacuum>`, not conjugation of the preparation operator.  Because
the fixed-Wilson edge marginal is `I/2`, `Z_edge|vacuum>` is orthogonal to the
vacuum rather than equal to it.  A channel identity in Pauli-coordinate space
does not supply the requested phase on the physical rays.

## Actual encoding-level intertwiner check

The counterexample also survives the full Cycle-315 encoding, so it does not
depend on treating expansion terms as standalone inputs.

The encoded vacuum column is AB/BA fixed, has endpoint tags `00`, and is full
Schmidt rank on the shared edge.  Any three-`M2` encoding intertwiner must
therefore be identity on the entire edge tensor `|00>` local sector.  The
runner independently constructs the AB and BA matrices and projects their
difference onto that same sector.  At L5 and held L6:

- the abstract ray-index diagonal intertwiner has maximum column residual 0;
- the minimum over six arms of the largest projected AB/BA column residual is
  `1.4142135623730945`;
- 216 logical columns per size have nonzero projected AB/BA difference.

The sparse diagonal on the `RayReducer` row index is thus a valid abstract
global ray-basis unitary, but it is not supported on the declared three
physical tensor factors.

## Exact six-direction census

At each of L5 and held L6:

- 23,784 center-arm branch-term cases;
- 1,200 negative-order signs;
- zero corrected-formula errors;
- zero legacy-formula errors on this interior-only fixture;
- zero Route-B six-term errors;
- zero AB/BA Pauli phase-relation failures;
- zero physical-row sign conflicts;
- Route-B observed pattern counts `(347,258,347,258,158,158)`;
- zero endpoint-swap errors;
- zero abstract ray-diagonal encoding residual.

Route B remains correctly scoped as a label diagnostic.  Its six monomials
use seven active operator-coordinate bits on five underlying physical `M2`
factors (three face factors and two tags): label-space dimension 128 versus
physical Hilbert dimension 32.  The seam witness shows that Route B retains
the corrected sign, but it still does not supply a physical matrix-unit
circuit.

## Matrix-unit, support and leakage controls

Writing `K = H_edge tensor |00>_tags`, the branch requirements are

```text
U|K = +I_K,
U|K = -I_K.
```

The least-squares solution over arbitrary nonunitary `2 x 2` restrictions has
one unit of state-vector error on each witness and combined residual
`sqrt(2)`.  For every unitary on the full three-`M2` support, including any
leakage out of `K`, the equal local marginals imply

```text
||(U-I) psi_plus||^2 + ||(U+I) psi_minus||^2 = 4.
```

At least one witness residual is at least `sqrt(2)`.  The identity has zero
positive residual and negative residual 2.  A tag flip has unit target-ray
leakage probability and residual `sqrt(2)` on each witness.

## Deletion and covariance

Aggregated over the six interior directions per size:

- removing the corrected `x` control produces 11,064 errors;
- removing either endpoint-tag control produces 2,580 errors;
- deleting the sign gate produces 1,200 errors;
- deleting Route-B monomials 0 through 5 produces respectively
  `(3024,1512,3780,3780,3024,1200)` errors.

All corrected controls and all six Route-B monomials are active.

The result is endpoint symmetric and frame stable:

- every directed arm has the same positive/negative full-Schmidt witness at
  L5 and L6;
- all 24 proper-cubic frames were checked;
- each source direction reaches all six directions four times;
- all 576 ordered frame products and 3,456 direction-composition cases have
  zero failures;
- endpoint reversal leaves the corrected formula invariant.

Covariance transports the same physical-route defect; it does not turn a
Pauli preparation label into a physical state register.

## No-Go Discipline Gate

The gate uses the newer `origin/main` no-go-discipline skill fetched on
2026-07-25 and normalizes route families by mathematical object, mechanism and
terminal obligation.

Gate status: **PASS for the exact statement below.**

### Exact target contract

> For one landed Cycle-315 edge encoding, no unitary supported exactly on
> `S = {outer-edge M2, endpoint-tag-u M2, endpoint-tag-v M2}`, tensored with
> identity on every complementary factor, realizes the corrected coherent
> AB-to-BA ray translator on the declared `n<=2` columns.

The quantifier is every `U in U(8)`, for each of the six Cycle-330 arms at L5
and held L6.  The fixed-Wilson stabilizer semantics, Cycle-315 encoding and
corrected sign table are allowed premises.  Reading Pauli-label coordinates,
using state-dependent success amplitudes, leaving an environment record,
accessing another data `M2`, or weakening exact coherence does not satisfy the
target.

The claim does **not** concern larger support, non-clean ancillas,
measurement/postselection diagnostics, supplied qutrit feature copies,
two-star recurrence or the full lattice.

### N1 — normalized alternative-route census

| family | object / mechanism / terminal obligation | marker | disposition and exact evidence |
|---|---|---|---|
| arbitrary same-support unitary | `U(8)` / full-Schmidt local support / realize both phase requirements | **ATTEMPTED** | `scripts/frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25.py:174-209`: coefficient rank 4, augmented rank 5; one witness residual is at least `sqrt(2)` |
| same-support isometry with leakage | `V:S -> S direct-sum L` / equal local marginals / zero target error and zero leakage | **ATTEMPTED** | the embedded-target residual squares sum to 4 for every isometry; accepting leakage changes the target |
| clean-return ancillary dilation | unitary `W` on `S tensor A` / `A:|0> -> |0>` / one coherent induced data action | **ATTEMPTED** | `K=<0|W|0>` must obey the same rank-4/rank-5 equations for ancilla dimensions 1, 2, 4 and 8; the proof is dimension independent |
| staggered or time-multiplexed same-support circuit | product `U_m...U_1` / closure of `U(8)` / exact final translator | **ATTEMPTED** | schedule lengths 1 through 8 remain unitary and retain squared witness-residual sum 4; every finite product is one member of `U(8)` |
| local measurement and postselection | one Kraus operator `K` / common success amplitude preserving superpositions / postselected translator | **ATTEMPTED** | the 8-equation, 5-unknown homogeneous matrix system has rank 5 and nullity 0, forcing common success amplitude `c=0`; this is also not an acceptable unitary route |
| Pauli-coordinate or ray diagonal | diagonal on `RayReducer`/Route-B coordinates / read preparation labels / descend to `S` | **ATTEMPTED** | abstract diagonal residual 0, while the actual tag-`00` projected encoding residual is at least `1.4142135623730945` |
| enlarged-support syndrome extraction | extra face/check/feature `M2` plus returned work / physical syndrome extraction / construct and uncompute | **ATTEMPTED** | Cycle 315 and Route C show this is a live constructive escape, but it is outside the exact support quantifier and remains open |

These are seven distinct primary objects or mechanisms.  The enlarged-support
row is not counted as a failure of the narrow statement; it is the boundary
that prevents a broader no-go.

### N2 — wall-independence audit

The negative theorem itself has one collapsed support condition: exact action
on exactly the three named data factors.  Three ways to change that target are
kept as separate open escape families:

| left | right | closing left closes right? | closing right closes left? | independent? |
|---|---|---:|---:|---:|
| `E_support_enlargement` | `E_nonclean_environment` | no | no | yes |
| `E_support_enlargement` | `E_measurement_target_change` | no | no | yes |
| `E_nonclean_environment` | `E_measurement_target_change` | no | no | yes |

An enlarged coherent circuit need not leave an environment record; a non-clean
environment need not access a larger data neighborhood; measurement changes
the operation class independently of both.  None is silently presented as an
independent proof wall for the exact theorem.

### N3 — hidden-condition scan

The executable scan covers the claim-bearing runner source and this note
before the present gate.  It searches the complete skill trigger inventory,
including assumption, construction, standard-context, background,
naturalness, obviousness, registration and canonicality variants.  It reports
zero hits and zero hidden conditions.

The load-bearing conditions are stated explicitly: fixed-Wilson reference,
declared `n<=2` encoding, exact support `S`, identity on the complement, common
coherent action and exact rather than approximate translation.  The first two
come from landed Cycle-311/315 semantics; the rest define the theorem target.

### N4 — residual matching

| witness | witness residual | claimed residual | match? | use |
|---|---|---|---:|---|
| `scripts/physical_cycle269_overlap_aware_two_cell_cycle315_2026_07_18.py:324-448` | physical ray reduction and AB/BA encoding | same physical encoding on which local action is tested | yes | landed premise |
| corrected root translator | classifier accuracy and abstract ray diagonal | tensor-factor-supported state-vector unitary | no | dropped as negative evidence; retained only as target definition |
| Route-B six-term diagnostic | Pauli-label classifier accuracy | tensor-factor-supported state-vector unitary | no | dropped as negative evidence |
| Route-C naive two-basis echo | old `X/Z` copy target and work leakage | corrected `x/tag` same-support translator | no | dropped as negative evidence; retained only as a caution |
| `scripts/frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25.py:174-205,208-416,1100-1133` | full-Schmidt local matrix equations and tag-`00` encoding projection | exact same-support unitary and AB/BA projection | yes | load-bearing proof |

No prior route failure is used to close a mismatched residual.  The narrow
negative stands on the current analytic matrix equation and actual encoding
projection.

### N5 — rhetoric and resolution audit

| resolution | tested? | negative disposition |
|---|---:|---|
| one named positive/negative branch-ray pair | yes | exact `+I/-I` support contradiction |
| one complete Cycle-315 edge encoding | yes | nonzero tag-`00` projected AB/BA residual |
| all six Cycle-330 directions | yes | same witness and residual bound |
| L5 and held L6 | yes | stable without refit |
| larger local support | no | explicitly open; no negative claim |
| non-clean environment or measurement | no as physical unitary | changed targets; explicitly open as diagnostics/routes |
| simultaneous two-star or recurrent lattice | no | explicitly open; no negative claim |

The permitted rhetoric is only “no exact unitary on exactly these three data
factors realizes this declared encoding translator.”  The note does not say
that the sign is nonphysical, nonlocal at every radius, or impossible with
ancillas.

### N6 — partial-closure paths

| path | status | what it closes or could close |
|---|---|---|
| Cycle-315 doubled edge role plus relational `r_e` | landed positive local extension; `PHYSICAL_CYCLE269_OVERLAP_AWARE_TWO_CELL_CYCLE315_NOTE_2026-07-18.md:312` | repairs one adjacent AB/BA role after adding physical resources |
| Route-C qutrit feature transport | current positive bounded partial | gives a zero-residual coherent sign circuit once factor-private qutrit charts and clean work are supplied |
| larger stabilizer-syndrome extractor | open | could convert preparation-coordinate information into physical registers and uncompute them |
| non-clean environment or measurement | open target change | may diagnose/order branches, but is not the exact coherent unitary translator |

These are construction and resource paths, not convention problems or new
axiom requests.  This artifact makes no “no retained primitive” statement, so
the primitive-registry subcheck is not triggered.  No premise edit or
governance action is requested.

### N7 — hostile steelman

A hostile reviewer should reject any broader claim that the sign is not
physically local.  Cycle 315 already repairs endpoint order with an added
edge-role register, and Route C supplies a zero-residual coherent circuit once
qutrit features and work `M2`s are available.  A bounded neighborhood
containing stabilizer checks could extract the corrected `x/tag` syndrome,
phase it and uncompute it.  The actionable terminal obligation is an explicit
clean larger-support matrix-unit circuit tied to landed Cycle-311 state
vectors.  That route is strong and open, but it does not break the exact
three-data-factor statement because its defining mechanism accesses additional
physical support.  It blocks every broader negative.

### N8 — cross-cycle echo

The prescribed repository search over negative phrases and every available
physics-loop `NO_GO_LEDGER.md` was run.  The closest mathematical echoes are:

| prior result | retirement mechanism | present lesson |
|---|---|---|
| Cycle 308 bare odd-syndrome boundary | oriented complement carrier enlarged the code | a bare-support failure does not survive added carriers |
| Cycle 311 raw cell-role collision | cell role plus relational `r` | raw rank/order loss can become constrained gauge data |
| Cycle 315 endpoint order | doubled edge role plus relational `r_e`; note lines 312 and 424 | retain exactly-three-factor scope; added role data repairs the broader problem |
| Cycle 319/324 overlapping role checks | joint larger role register or serialized slot; Cycle-324 note lines 321 and 439 | enlarge or serialize before extending a local failure |
| Route C | supplied qutrit charts and returned work | larger coherent feature transport is a live escape |

Every echo warns against broadening.  All retirement mechanisms were
considered and remain explicitly open when they alter support or resources.
They do not change the rank contradiction inside the exact support contract.

### Gate conclusion

N1-N8 pass for the exact quantified statement.  Direct unitaries, leakage
isometries, clean-return dilations and same-support schedules all collapse to
the same `+I/-I` support contradiction.  Coherent postselection has only zero
common success amplitude.  Ray-coordinate diagonals do not descend to the
three factors.  Larger-support, non-clean ancillary, measurement and recurrent
routes remain open.

## Bound sources

- corrected root candidate SHA-256:
  `18c4d81fe0b909b6589c6c7b7bfd4b1bbbb54159a7549349e0c17654c139b9d0`;
- Route-B runner SHA-256:
  `1690b2aec7c1864988a158c56c0d78e8d69c257e6559cea1e048588908e30d78`.

The adversarial runner reports 9 PASS / 0 FAIL and terminal

```text
EXACT_THREE_DATA_M2_TRANSLATOR_NO_UNITARY_N1_N8_PASS_LARGER_SUPPORT_OPEN
```

The reference replay emits 19,270 bytes total, below the 24,000-byte stdout
target.  Its compact `SUMMARY_JSON` is 9,335 bytes and preserves the exact
aggregates,
seam-witness hashes and all-arm witness hashes while omitting repeated
per-edge prose and the full N1-N8 tables already retained in this note.

## Open

- a larger-support matrix-unit completion that extracts physical stabilizer
  syndromes rather than reading Pauli preparation coordinates;
- clean physical syndrome registers and their preparation/uncomputation;
- ancillas that access enlarged data support, and non-clean environments that
  retain a syndrome;
- measurement/postselection diagnostics as explicitly nonunitary changed
  targets;
- a primitive nearest-neighbor circuit and leakage-free intertwiner on that
  enlarged support;
- the complete simultaneous two-star `M64` update and recurrent schedule.

No broader impossibility, minimum-support, shared-obstruction or
axiom-pressure claim is made.

## Reproduce

```bash
python3 scripts/frontier_cycle330_symmetric_edge_sign_physical_m2_adversary_2026_07_25.py
```
