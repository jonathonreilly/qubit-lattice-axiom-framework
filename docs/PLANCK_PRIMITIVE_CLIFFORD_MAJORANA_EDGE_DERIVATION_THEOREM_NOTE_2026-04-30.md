# Planck Primitive Clifford-Majorana Edge Substrate-Descent Obstruction

**Date:** 2026-04-30; substrate-descent repair 2026-07-10
**Type:** no_go
**Status:** exact negative boundary on the supplied exterior one-form action;
finite-matrix multiplicity checks are numerical companions; independent audit required
**Primary runner:** `scripts/frontier_planck_primitive_clifford_substrate_descent_obstruction.py`
**Helper runner:** `scripts/frontier_planck_primitive_clifford_majorana_edge_derivation.py`

```yaml
claim_type_author_hint: no_go
claim_scope: >-
  Exact obstruction, on the explicitly supplied event-cell exterior action,
  to deriving the displayed irreducible Cl_4(C) / two-mode CAR action on
  P_A H_cell. Even granting P_A = Lambda^1 W, the supplied spatial module is
  1+3 whereas an irreducible Cl_4(C) module restricts to two spin-half
  doublets; the simultaneous intertwiner space is exactly zero. The canonical
  wedge-plus-contraction action gives a second exact grade-leakage witness on
  the full cell. Numerical finite-matrix companion checks expose multiplicity
  on the full exterior and retained native cubic taste representations. The
  older explicit C^4 matrices remain a correct conditional consistency
  construction, not an event-cell descent.
actual_current_surface_status: no-go
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: >-
  The positive implication is false on the supplied event-cell representation
  surface; native-taste multiplicity checks are companion evidence only.
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Question

The earlier version of this note constructed four Hermitian gamma matrices on
an abstract `C^4`, checked the `Cl_4(C)` relations and two-mode CAR pairing,
and then identified that module with

```text
P_A H_cell,      H_cell = Lambda^* W,      W = span(t,x,y,z),
P_A = P_1,       rank(P_A) = 4.
```

Two independent audits correctly classified the load-bearing step as a
renaming. Equal dimension does not derive an action. The missing question is
sharper:

```text
Does the action already carried by P_A H_cell intertwine with the spatial
bivector action of an irreducible Cl_4(C) module, and do substrate-native
coframe operators restrict to P_A?
```

The answer is no on the explicitly supplied event-cell exterior
representation. A second numerical finite-matrix calculation on the retained
cubic taste representation finds underdetermination rather than a unique
rank-four descent. Thus a better `P_A` selector alone cannot repair the old
positive chain on that exterior-action surface.

## Allowed Premises And Forbidden Imports

The decisive no-go grants more than the current minimal axioms provide:

1. a four-axis complex event cell `H_cell = Lambda^* W`;
2. the distinguished time line and standard spatial rotation of
   `W = C t + span(x,y,z)`;
3. the active packet `P_A = Lambda^1 W` itself;
4. the retained native cubic `Cl(3)` matrices on `C^8` when testing the
   independent taste-space route;
5. complex linearity.

The proof does not import an observed value, fit, selected unitary basis,
link-local source map, reflection-positive vacuum sector, gravitational
boundary density, or coefficient match. In particular, it forbids the step

```text
dim(P_A H_cell) = dim(S_Cl4) = 4  therefore  P_A H_cell = S_Cl4.
```

The current `ANOMALY_FORCES_TIME_THEOREM.md` is a bounded conditional count
theorem. Its declared B-AXIS premise supplies one clock/transfer axis and its
conclusion supplies `d_t=1` under named premises. It does not construct a
specific endomorphism `Gamma_t` on either `P_A H_cell` or the cubic taste
space. No such operator is imported here.

## Exact Obstruction Theorem On The Supplied Exterior Action

Let the supplied spatial `SU(2)` action on

```text
P_A H_cell = Lambda^1 W = C t + span(x,y,z)
```

be the exterior action induced by rotations of the three spatial axes while
fixing `t`. Let `J_1,J_2,J_3` be its Hermitian generators in standard
normalization:

```text
[J_i,J_j] = i epsilon_ijk J_k.
```

Let `S` be an irreducible complex `Cl_4(C)` module with Hermitian Clifford
generators `Gamma_t,Gamma_x,Gamma_y,Gamma_z`, and let

```text
T_1 = -(i/2) Gamma_y Gamma_z,
T_2 = -(i/2) Gamma_z Gamma_x,
T_3 = -(i/2) Gamma_x Gamma_y
```

be the spatial bivector generators on `S`.

Then:

1. `P_A H_cell` is the `SU(2)` module `1 + 3`, with quadratic Casimir
   spectrum `{0,2,2,2}`.
2. `S` restricts to the spatial `SU(2)` as `2 + 2`, with quadratic Casimir
   `(3/4) I_4`.
3. Therefore

   ```text
   Hom_SU(2)(P_A H_cell, S) = {0}.
   ```

   In particular, there is no invertible map `U` satisfying

   ```text
   J_i U = U T_i      for i=1,2,3.
   ```

4. Consequently no irreducible `Cl_4(C)` action on `P_A H_cell` can be an
   induced extension of this supplied exterior spatial action. Any displayed
   `C^4` gamma matrices replace the `1+3` action by a `2+2` action; they do not
   descend from it.

This conclusion is basis-independent because the Casimir spectra and
intertwiner dimension are representation invariants.

## Proof

### The event-cell packet is scalar plus vector

The one-form packet has basis `(t,x,y,z)`. Spatial rotations fix `t` and act
in the defining three-vector representation on `(x,y,z)`. Hence

```text
P_A H_cell |_SU(2) = V_0 + V_1,
```

where `V_j` denotes spin `j`. The quadratic Casimir `sum_i J_i^2` is zero on
`V_0` and `j(j+1)=2` on `V_1`, giving

```text
spec(sum_i J_i^2) = {0,2,2,2}.
```

This is the same exterior one-particle action used by the clean
`SUBSTRATE_TO_P_A_FORCING_THEOREM_NOTE_2026-04-30.md` counterexample runner.

### An irreducible complex Cl_4 module is two spatial doublets

Complex `Cl_4(C)` is `M_4(C)`, so its irreducible module has dimension four.
The spatial bivectors satisfy `su(2)` and obey

```text
sum_i T_i^2 = (3/4) I_4.
```

Thus every irreducible summand has spin `1/2`. Dimension four gives two such
summands:

```text
S |_SU(2) = V_1/2 + V_1/2.
```

There is no common irreducible constituent between `V_0+V_1` and two copies
of `V_1/2`. Schur's lemma gives a zero intertwiner space. The runner also
forms the exact `48 x 16` simultaneous-intertwiner system and finds rank 16,
nullity 0.

### Why this directly blocks the old construction

If gamma matrices on `P_A H_cell` were induced from the supplied event-cell
action, their spatial bivectors would agree with that action up to an
invertible change of basis. Such a change of basis would be an invertible
intertwiner, contradicting the exact nullity result. The old runner checks
only the Clifford relations after the new action has already been assigned.

## Independent Full-Cell Clifford Attack

A natural attempt bypasses packet selection and constructs Clifford operators
directly on the full exterior cell. Let `epsilon_a` be exterior multiplication
by the coframe vector `e_a` and `iota_a` its adjoint contraction. Then

```text
C_a = epsilon_a + iota_a,
{C_a,C_b} = 2 delta_ab I_16.
```

This is a genuine canonical `Cl_4(C)` representation on `H_cell`. It does not
repair the target:

```text
C_a Lambda^1 W subset Lambda^0 W + Lambda^2 W,
P_A C_a P_A = 0,
[P_A,C_a] != 0.
```

So `P_A` is not invariant. The full module is reducible:

```text
Lambda^* W ~= S tensor C^4,
dim Comm_Cl4(H_cell) = 16.
```

There are four equivalent irreducible Clifford copies. Selecting one is a
primitive-idempotent or multiplicity-line choice, not a consequence of the
Clifford relations.

As a numerical finite-matrix companion, require the natural exterior spatial
action simultaneously. Subtracting the Clifford spin action from the
exterior rotation action produces a commuting right-spin action `R_i` with

```text
[R_i,C_a]=0,
sum_i R_i^2 = (3/4) I_16.
```

The runner finds that the jointly generated algebra has complex dimension 64,
center dimension one, and commutant dimension four, the finite-representation
signature of `M_8(C)` with multiplicity two. The smallest joint
Clifford-plus-exterior-spin block is therefore eight-dimensional. This is a
numerical companion with large singular-value gaps; the exact load-bearing
no-go remains the Casimir/intertwiner theorem above.

## Independent Retained Cubic-Taste Attack

The retained native `Cl(3)` authority acts on the cubic taste space `C^8`
using

```text
gamma_1 = sigma_x tensor I tensor I,
gamma_2 = sigma_y tensor sigma_x tensor I,
gamma_3 = sigma_y tensor sigma_y tensor sigma_x.
```

This companion route has the desired spin-half Casimir, but it still does not
derive the claimed packet. The displayed candidate nonuniqueness is exact;
the algebra and commutant ranks are reproducible numerical finite-matrix
checks:

1. the generated complex `Cl_3` algebra has dimension eight while its
   commutant on `C^8` has dimension eight, so multiplicities remain;
2. a temporal axis label does not specify an endomorphism anticommuting with
   the three spatial matrices;
3. already within the three-qubit Pauli strings there are eight Hermitian
   involutions that anticommute with all three spatial gamma matrices:

   ```text
   YYY, YYZ, YZI, YZX, ZII, ZIX, ZXY, ZXZ;
   ```

4. each choice extends the spatial matrices to a `Cl_4(C)` algebra acting on
   `C^8`, but the commutant has dimension four: it is a two-copy module;
5. obtaining a single `C^4` carrier requires an additional rank-four
   multiplicity projector and a bridge identifying it with `P_A H_cell`.

Thus the retained taste route does not itself supply a unique descent. The
audited scope of the graph-first `SU(3)` surface supplies a selected-axis
fiber/base decomposition and a `gl(4)` commutant on the base; it does not
include a coframe-to-gamma map or an irreducible Clifford-copy selector.

## What Survives From The Earlier Note

The helper runner still correctly verifies the following conditional
statement:

```text
GIVEN an abstract four-dimensional complex carrier K and GIVEN the displayed
gamma matrices on K, they generate M_4(C), pair into the two-mode CAR algebra,
and give K ~= F(C^2).
```

That is an algebraic consistency construction. It is not evidence that
`K = P_A H_cell`, that `P_A` is invariant, or that the gamma matrices are
induced by the event-cell or cubic-taste action. The coefficient equality
`c_Widom=c_cell=1/4` is likewise a cross-check after the rank-four carrier has
been assigned; it cannot select or derive that carrier.

## Exact Claim Boundary

Proved here:

```text
supplied exterior event-cell action + granted P_A
  -/-> equivariant irreducible Cl_4(C) action on P_A;

canonical exterior Cl_4(C) action on H_cell
  -/-> invariant four-dimensional P_A block;

retained native cubic Cl(3) action + temporal-axis label
  -/-> a supplied unique temporal gamma operator or unique irreducible C^4 copy
       within the tested finite-matrix realization [numerical companion].
```

Not proved here: a universal no-go against every enlarged framework. A
positive construction can be made after adding new structure. It must supply,
at minimum:

1. a spinorial packet whose spatial representation is `2+2`, or a theorem
   replacing the exterior `1+3` action by that spinorial action;
2. a temporal Clifford endomorphism, not only a temporal dimension/axis label;
3. a canonical multiplicity selector on the `C^8` or `C^16` carrier;
4. a physical bridge identifying the selected spinor packet with the active
   boundary response.

Those are changed or added premises. They are not derivable from rank four,
`P_A` selection, or the cited coefficient match.

## No-Go Discipline Gate

### N1 Alternative route enumeration

- **ATTEMPTED:** symmetry-only `P_A` uniqueness was rerun in this cycle using
  `SUBSTRATE_TO_P_A_FORCING_THEOREM_NOTE_2026-04-30.md:21-22,214` and its
  runner; the `P_3` witness still passes all eight blocks.
- **ATTEMPTED:** Hodge/oriented-incidence selection was rerun using
  `FIRST_ORDER_COFRAME_UNCONDITIONALITY_NO_GO_THEOREM_NOTE_2026-04-30.md:32-42`
  and its runner; the `P_1`/`P_3` Hodge witness still passes all eight blocks.
- **ATTEMPTED:** the link-local first-variation route can select `P_1` only on
  its added source surface per
  `LINK_LOCAL_FIRST_VARIATION_SELECTOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-10.md:49-66,100-112`;
  its runner was rerun, and granting its conclusion does not change the
  `1+3` versus `2+2` representation mismatch computed here.
- **ATTEMPTED:** the representation-intertwiner route on granted `P_A` has
  exact nullity zero.
- **ATTEMPTED:** the canonical full-cell exterior Clifford action exists, but
  it does not preserve `P_A` and has fourfold multiplicity.
- **ATTEMPTED:** the retained cubic-taste extension leaves both the temporal
  operator and irreducible copy unselected after reconstructing the matrices
  in `NATIVE_GAUGE_CLOSURE_NOTE.md:46-66`; its runner was rerun in this cycle.
- **ATTEMPTED:** the graph-first fiber/base route supplies a `gl(4)` commutant,
  which permits arbitrary base endomorphisms but selects no Clifford coframe
  vector map within the audited scope of
  `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md:35-112`; its runner was rerun in this
  cycle.

Scope boundary, not counted as an N1 route: a new spinor packet or explicit
approved representation bridge changes the premise surface and is not
foreclosed by this no-go.

### N2 Wall independence

The old wall was substrate-to-`P_A` selection. This result exposes a second
wall: even after `P_A` is granted, its stated spatial representation is not
the restriction of an irreducible `Cl_4(C)` module. They are independent:

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| packet selector / representation descent | no; the proof grants `P_A` and the descent still fails | no; changing to a spinor action does not select `P_A` among substrate packets | yes |

For the alternative native-taste route, the narrower obligations are also
pairwise independent. Here “physical bridge” means only the semantic
identification after the operator and copy have already been supplied; it is
not defined broadly enough to contain them.

| Native-taste pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| temporal gamma / rank-four copy | no; a `Cl_4` action on `C^8` remains two-copy | no; a rank-four projector does not construct an anticommuting temporal generator | yes |
| temporal gamma / physical bridge | no; an operator has no boundary semantics by itself | no; semantics does not supply the operator | yes |
| rank-four copy / physical bridge | no; a projector has no boundary semantics by itself | no; an identification of an already-selected copy does not select it | yes |

These are route-specific obligations, not additional walls in the exact
exterior-action theorem.

### N3 Hidden-wall scan

The proof text was scanned for `assume`, `by construction`, `standard`,
`framework provides`, `bridge context`, `background`, `naturally`,
`obviously`, `registered`, and `canonical`.

| Hit | Classification | Disposition |
|---|---|---|
| “standard spatial rotation” in the allowed-premise list | explicit strengthening grant | kept as supplied model input, not framework authority |
| “standard normalization” for `su(2)` generators | non-load-bearing convention | fixes `[J_i,J_j]=i epsilon_ijk J_k`; both Casimirs use the same normalization |
| “canonical wedge-plus-contraction” | displayed exact construction | reconstructed by the runner; no admission |
| “canonical full-cell action” | same displayed construction | non-load-bearing alternative route |
| “canonical multiplicity selector” | absent object needed by a future positive | open repair obligation, not assumed |
| “registered primitives” in N6 | primitive-registry check | explicitly states those primitives do not supply the bridge |

No target coefficient, fitted selector, observed value, action source,
reflection-positive state, unit convention, or hand-picked unitary is used.
The event-cell calculation grants `P_A`; failure therefore cannot be blamed on
the old selector no-go.

### N4 Residual matching

Residual matching is deliberately narrow:

| Cited witness and locator | Residual it attacks | Current residual | Match as proof witness? |
|---|---|---|---|
| `SUBSTRATE_TO_P_A_FORCING_THEOREM_NOTE_2026-04-30.md:21-22,214` | packet uniqueness | induced Clifford action after granting `P_A` | no; route history only |
| `FIRST_ORDER_COFRAME_UNCONDITIONALITY_NO_GO_THEOREM_NOTE_2026-04-30.md:32-42` | `P_1` versus `P_3` | `1+3` versus `2+2` action | no; route history only |
| `LINK_LOCAL_FIRST_VARIATION_SELECTOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-10.md:49-66,100-112` | source-support selection of `P_1` | induced Clifford action | no; granting it is a control |
| `NATIVE_GAUGE_CLOSURE_NOTE.md:46-66` | displayed cubic `C^8` matrices | native-taste extension multiplicity companion | yes for input matching; ranks remain numerical companions |
| `ANOMALY_FORCES_TIME_THEOREM.md:20-25,146-155` | conditional time count/axis | absence of a supplied temporal gamma endomorphism | yes for scope comparison, not as negative algebra evidence |

The proof witness for the new residual is the new runner, not the earlier
selector no-gos. It matches the auditor's quoted blocker by sharpening “no
induced action was proved” to “no equivariant induced action exists on the
stated exterior `P_A` representation.”

### N5 Proven surface

| Resolution | Tested? | Supported negative statement |
|---|---|---|
| per generator / mode | yes | each displayed exterior Clifford generator leaks from degree one; each spatial generator enters the exact intertwiner system |
| per four-dimensional block | yes | the full `P_A` intertwiner space is zero |
| per 16-dimensional event cell | yes | the displayed wedge-plus-contraction action does not preserve `P_A`; multiplicity ranks are numerical companions |
| per native `C^8` taste cell | yes, companion | displayed Pauli candidates and numerical algebra/commutant ranks |
| per lattice / dynamical theory | no | no lattice-wide or dynamical no-go is claimed |

Only the
enumeration of temporal extensions is Pauli-string-resolved; the text says
“already within the Pauli strings” and does not claim an exhaustive
classification of all endomorphisms. No per-site result is promoted to a
lattice-wide dynamical no-go. The exact claim is limited to the displayed
event-cell exterior action. The retained native cubic matrices provide a
numerical companion, not a second exact no-go. This note does not
forbid a future theory with a new spinor packet, changed representation
bridge, or approved multiplicity selector.

### N6 Partial closure

The requested positive theorem is not recovered. A bounded conditional route
may explicitly admit a spinor packet, temporal gamma operator, multiplicity
selector, and physical boundary-response bridge, then seek later import
retirement. None of the registered scale, kinetic-isotropy, or realized-state
primitives supplies those objects, and no convention-only reframe changes the
Casimir spectrum. The exact negative result closes only the current-surface
repair route and isolates the premise change needed for a later positive
attempt; it does not call that change a new axiom.

The partial-closure scan found one strong adjacent algebra theorem,
`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md` (named as
non-load-bearing scope context rather than a citation-graph dependency). It
classifies the two abstract one-generator real-Clifford sign extensions. Its
own scope explicitly does not close Wick rotation, spacetime, dynamics, or a
carrier realization; its current audit state is in progress. It therefore
does not supply the event-cell intertwiner or copy selector. The current
minimal-axiom and Tier-A registries contain no carrier premise, and the
controlled vocabulary contains no convention whose ratification changes an
`SU(2)` representation type. The 2026-07-10 open-PR scan found PR #5135,
which registers a different one-site P-QBIT carrier premise and does not close
this `Cl_4`/`P_A` event-cell residual; it found no in-flight repair of this
intertwiner. The existing link-local selector closes only support selection on
its bounded source surface, not representation descent.

### N7 Steelman

A hostile reviewer can combine the graph-selected factorization
`C^8 = C^2_fiber tensor C^4_base` with a chirality or commutant projector,
place `Cl_4(C)` on the four-dimensional base, and then declare that base to be
the physical boundary packet. This is the strongest live escape because it
combines the retained native matrices in `NATIVE_GAUGE_CLOSURE_NOTE.md`, the
retained selected-axis factorization in `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`,
the bounded `P_1` support selector in
`LINK_LOCAL_FIRST_VARIATION_SELECTOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-10.md`,
and the audit-in-progress abstract sign-extension theorem named in N6. These
are named as non-load-bearing steelman context, not proof dependencies. It
therefore has the right dimension and serious algebraic support. It does not
refute the stated no-go: the `gl(4)` commutant permits every base endomorphism
and selects no Clifford vector map, a fiber/base quotient is not the exterior
one-form packet, and identifying it with the boundary response is precisely a
new representation/physical bridge. Likewise, simply placing irreducible
gamma matrices on the four one-form labels changes the spatial representation
from `1+3` to `2+2`; the zero intertwiner result is why that is an assignment,
not a descent.

### N8 Cross-cycle echo

Earlier selector walls were partially bypassed by admitting a link-local
source domain or a reflection-positive vacuum sector. The same mechanism can
produce a future conditional positive here: explicitly admit the spinor
representation and multiplicity selector, then audit whether those imports
can be retired. That possibility is preserved. What cannot be reused is the
claim that a valid object on an isomorphic vector space establishes identity
of actions. Here the discriminant is representation type rather than projector
rank.

The repo search found these concrete echoes:

| Prior surface | Later status/mechanism | Applicability here |
|---|---|---|
| `AXIOM_STACK_MINIMALITY_CL4C_NO_GO_THEOREM_NOTE_2026-04-29.md` | historical broad exhaustion language; not current minimal-axiom authority | cautionary: do not repeat its universal “unique minimal extension” claim |
| `.claude/science/physics-loops/planck-pa-retention-20260430/NO_GO_LEDGER.md` | symmetry/Hodge selector wall partially bypassed by an explicit link-source premise | applicable as a conditional-premise route, not a derivation on the old surface |
| `.claude/science/physics-loops/hubble-c1-absolute-scale-gate-20260428/NO_GO_LEDGER.md` | records repeated isomorphic-carrier/semantic-bridge gaps | applicable discipline: distinguish algebra existence from physical carrier identity |
| `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md` | abstract extension route now in independent audit; physical realization excluded by its scope | may retire the abstract extension subproblem, but not the event-cell intertwiner or multiplicity bridge |

No prior retirement mechanism found in this scan changes the exact `SU(2)`
Casimir mismatch without changing the supplied representation premise.

## Verification

Run the discriminating substrate runner:

```bash
python3 scripts/frontier_planck_primitive_clifford_substrate_descent_obstruction.py
```

Expected close:

```text
Summary: PASS=10  FAIL=0
Exact verdict: OBSTRUCTION ON THE GRANTED EVENT-CELL SURFACE.
```

The older helper may still be run to reproduce the conditional construction:

```bash
python3 scripts/frontier_planck_primitive_clifford_majorana_edge_derivation.py
```

Its `PASS=8 FAIL=0` means only that the assigned abstract `C^4` matrices are
internally consistent.

## Referenced Route Context

The files below are route provenance and steelman context, not load-bearing
dependencies of the self-contained exact intertwiner theorem. They are kept as
code-formatted paths deliberately so the citation graph does not turn route
history into proof imports.

- `MINIMAL_AXIOMS_2026-06-29.md` — framework-boundary context only; none of
  Lattice, Qubit, Admissibility, or Record is a proof input to this
  granted-representation theorem.
- `NATIVE_GAUGE_CLOSURE_NOTE.md` — retained
  cubic `Cl(3)` matrices and bivector `su(2)` on `C^8`.
- `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`
  — selected-axis fiber/base and structural commutant surface; tested as an
  alternative route, not used in the exact intertwiner proof.
- `ANOMALY_FORCES_TIME_THEOREM.md` — non-load-bearing scope context. Its
  present bounded statement is a conditional temporal-dimension count and
  does not supply `Gamma_t`; it is deliberately not a citation-graph
  dependency of this no-go.
- Complex linearity is an explicit strengthening grant in this note. The
  `I3_ZERO_EXACT_THEOREM_NOTE.md` result assumes complex amplitudes for its own
  interference theorem and is not used here to derive complex structure.
- `SUBSTRATE_TO_P_A_FORCING_THEOREM_NOTE_2026-04-30.md`
  — clean symmetry-only selector no-go and event-cell exterior action.
- `FIRST_ORDER_COFRAME_UNCONDITIONALITY_NO_GO_THEOREM_NOTE_2026-04-30.md`
  — clean Hodge `P_1`/`P_3` degeneracy.
- `LINK_LOCAL_FIRST_VARIATION_SELECTOR_BRIDGE_NARROW_THEOREM_NOTE_2026-05-10.md`
  — bounded conditional support selector; it does not derive the Clifford
  action tested here.
