# Physical covariant protected-link shadow — Cycle 528

Date: 2026-07-21
Authority: none
Audit: unset
Constitutional effect: none

Companion runner:

`scripts/physical_covariant_protected_link_shadow_cycle528_2026_07_21.py`

## Question and bounded answer

This cycle asks whether a protected edge/link carrier can stay live through
Cycle 523's remaining B layer and remove its norm-2 direct-stream residual,
while preserving bounded support and overhead, local constraints and
preparation, proper-cubic covariance, the one-particle mass fixture, contact
and the Cycle-230 seam block, and the exact 100-call/cell Cycle-523 schedule.

The strongest constructive result is an exact local one-link comparator.  A
fixed local phase change turns Cycle 236's oriented auxiliary-Majorana state

\[
 K_e=(|10\rangle-i|01\rangle)/\sqrt2
\]

into the endpoint-swap-symmetric Bell state

\[
 |\psi_+\rangle=(|10\rangle+|01\rangle)/\sqrt2 .
\]

The resulting auxiliary state is the unique local state selected by the
newly declared commuting constraints

\[
 YY=+1,\qquad -ZZ=+1.
\]

A locally controlled four-M2 link update then satisfies

\[
 U_{e,\mathrm{dress}}E_e=E_e\,\mathrm{FSWAP}_e
\]

to numerical precision, with zero terminal code leakage, an exact inverse,
three fixed one-/two-M2 preparation calls per link, and no unpreparation
during B.  Cycle 236's dressed update and this comparator induce the same
one-link FSWAP, but their full four-M2 code projectors differ by norm 2: the
local phase change does not remove Cycle 236's interleaved JW matter factor.
This is a comparison and a new local code, not a claimed localization of the
entire Cycle-236 sector.  The new carrier is nevertheless genuinely live
rather than a blank tag.

That local success does **not** close the simultaneous B matching.  The
product of the locally prepared Bell-link sectors induces exactly the product
of endpoint FSWAPs on the matter code.  The complete L5 and held-L6
two-particle censuses retain respectively 60,600 of 280,875 and 154,800 of
839,160 wrong exchange signs, with operator-norm residual 2.  Vacuum and all
one-particle states remain exact.  This falsifies this product-prepared
one-link construction; it is not a general local-gauge no-go.

## Declared code, preparation, update, and placement

Each coarse cell carries the seven Cycle-523 sites—six private face-centre
occupation M2 sites and one centre parity tag—plus six auxiliary endpoint M2
sites, one for every directed face.  Every undirected positive-axis B link
uses the matching pair of auxiliary endpoints.  Thus there are 13 active M2
sites per cell and three Bell links per cell.

The local link preparation is fixed:

1. apply `X` to the right auxiliary endpoint;
2. apply `H` to the left endpoint;
3. apply `CNOT(left -> right)`.

This prepares `psi+` from `|00>`.  The two local stabilizers above enforce
the auxiliary state.  The four-M2 dressed block acts on the two matter ports
and the two auxiliary endpoints and preserves both constraints.  Deleting
the update, perturbing its angle, deleting preparation, and reversing the
update all have explicit controls in the runner.

For the geometric certificate, coarse centres are separated by eight
physical lattice steps; the occupation ports sit at offsets `-D_a`, the
auxiliary ports at `3 D_a`, and the tag at the centre.  A canonical link block
therefore occupies the four collinear positions 1, 3, 5, and 7 and has
diameter six.  This is bounded independently of L.  The 13-site offset set,
the symmetric constraint pair, and the dressed block close under all 24
proper-cubic frames; the direction action closes on all 576 frame products.
The period-eight origin is supplied structure, not derived translation
selection.

The four-M2 dressed block is an explicit finite unitary but this cycle does
not synthesize its decomposition into the framework's one-/two-M2 primitive
library.  Accordingly the result is a bounded-neighbourhood compiler module,
not full primitive closure.  Cycle 523's already exact 100-call/cell onsite,
reverse, B-slot, contact, and parity schedule is retained as the matter-side
fixture.  Its three endpoint-FSWAP B calls per cell are replaced one-for-one
by three dressed blocks, leaving 100 bounded-block calls per cell if each
four-M2 block is counted as one call.  That 100 is not claimed as a bare
one-/two-M2 gate count after the replacement.

## Complete L5 and held-L6 sign census

For each size the runner compares two actions on every vacuum, one-particle,
and two-particle occupation basis state:

- `Gamma(P_B)`, the intrinsic exterior action of the complete Cycle-230 B
  permutation;
- the physical product of disjoint dressed Bell-link blocks, whose code
  action is the endpoint-FSWAP product.

| size | modes | one-particle failures | two-particle pairs | wrong signs |
|---:|---:|---:|---:|---:|
| L5 | 750 | 0 | 280,875 | 60,600 |
| L6 held out | 1,296 | 0 | 839,160 | 154,800 |

The two actions always agree on the output occupation.  A wrong sign is
therefore an exact basis-vector residual 2, proving operator-norm residual 2.
The onsite coin/contact factors common to both sides cannot reduce that norm.

## Larger endpoint-link response solve

The Bell state itself could have been too restrictive, so the runner tests a
strictly larger diagonal product class.  For every canonical positive-axis
link `e=(x,a)` introduce an arbitrary response bit

\[
 f_a(q_x,q_{x+\hat a})\in\mathbb F_2,
\]

where each endpoint word is an unrestricted six-bit M64 occupation word.
Axis dependence is allowed.  Proper-cubic covariance is deliberately **not**
imposed, making the search more permissive than the required compiler.  The
candidate correction on occupation `n` is

\[
 (-1)^{\sum_e f_{a(e)}(q_{x(e)},q_{y(e)})}.
\]

Every vacuum, one-particle, and two-particle state supplies one GF(2)
equation

\[
 A_n f=r(n),
\]

where `r(n)` is the exact exterior sign XOR the endpoint-FSWAP sign.  The
runner scans the complete L5 and L6 equation sets, retains all arbitrary
endpoint-word unknowns encountered, and looks first for a one-row and then a
two-row contradiction.

L5 has a minimum two-row inconsistent certificate and no one-row
contradiction: the vacuum row and the two-particle configuration occupying
direction 0 at cells `(0,0,0)` and `(1,0,1)` have the same three-unknown row
but require residual bits 0 and 1.  At even L6, that same two-particle shape
already has an all-zero response row and required residual bit 1, giving a
minimum one-row certificate.  XORing the L5 pair, or reading the L6 row
directly, gives

\[
 0\cdot f=1.
\]

This rules out translation-equivariant products of arbitrary endpoint-cell
diagonal link responses.  It does **not** test correlated link-sector
preparation, non-diagonal/stateful link-gauge transitions, a higher-form
code, or a link response with a larger bounded neighborhood.

## Constant-depth reformulation of Cycle 260

The constructive comparison introduces one prefix-shadow M2 `s_i` beside
each position of a length-`2L` alternating A/B cycle and declares

\[
 s_0=0,\qquad s_{i+1}=s_i\oplus n_i.
\]

All checks except the anchor are nearest-neighbor constraints.  Once this
code has been prepared, Cycle 260's order-change phase is the radius-one,
three-M2 seam expression

\[
 (-1)^{n_0(s_{2L-1}\oplus n_0\oplus n_{2L-1})}.
\]

It is exact on every one of the `2^(2L)` cycle words at L5 and held-L6.  This
is a real runtime localization: the exact phase no longer needs a moving
accumulator at runtime while the prefix code is valid.

Preparation and recode are separate.  The explicit prefix ladder has depths
`2L-1`, namely 9 and 11.  For radius-one gates, the final prefix bit depends
on an input at cyclic distance L, giving preparation and recode lightcone
lower bounds 5 and 6 on the tested sizes.  Keeping the old prefix field after
B violates local constraints on named basis states, so the code must be
updated.  The recode lower bound includes the old lawful shadow: vacuum and a
single occupation at position `2L-1` have identical old prefix words, and
their radius-`L-1` input neighborhoods about output `s_(L-1)` agree, but after
B the required output bits are 0 and 1.  A remote-pickup deletion gives exact
state-vector residual 2.  The selected seam/anchor remains supplied.  These
facts block a constant-depth
preparation/recode claim for this prefix encoding; they do not establish a
runtime impossibility and do not exclude a different distributed gauge code.

## Preserved fixtures and supplied structure

The runner re-executes the Cycle-523 onsite compiler and the Cycle-230 seam
fixture.  It requires:

- the full local M64 onsite intertwiner, inverse, and terminal leakage bounds;
- the beta `-0.3` one-particle mass fixture;
- all 15 contact phases at `g=0.37` and their deletion control;
- the Cycle-230 L3 seam block and its two retained singular values;
- exact 100-call/cell Cycle-523 protected-shadow schedules at L5 and L6;
- all 24 proper-cubic frames and all 576 frame products.

Supplied rather than derived are the Cycle-219 coin coefficients, Cycle-230
contact coupling and factor order, Cycle-523 compile-time QR schedule, the
period-eight supercell origin, and the Cycle-260 seam anchor.  No physical
duration, energy, Record, source law, global Jordan-Wigner service, nonlocal
parity service, or runtime host choice is inferred.

## Dependency and six-wall disposition

- `C_ref`: unchanged.  The CAR exterior action remains the declared coarse
  reference, not a derived physical encoding.
- `C_num`: unchanged.  This cycle adds exact finite algebra and censuses but
  no continuum or precision theorem.
- `C_wrap`: unchanged.  Wrapped phases are not called physical energy or
  time.
- `C_int`: locally preserved.  The `g=0.37` contact and seam block survive;
  no new interaction law is derived.
- `C_local`: narrowed.  One protected link, its local constraints,
  preparation, inverse, leakage, covariance, and live B update close.  The
  product of such links and the larger endpoint-diagonal product-response
  class fail globally.  Correlated/stateful gauge constructions remain open.
- `C_source`: unchanged.  No gravity/resource/source claim is made.

The overall physical M2 compiler remains open, so there is no shared
substrate obstruction and no axiom pressure.

## No-go discipline N1–N8

Broad no-go gate status: **FAIL / DO NOT SHIP**.  The artifact is demoted to
`partial-attempt-with-named-untested-routes`.  The exact GF(2) inconsistency
is retained only for its explicitly quantified endpoint-diagonal product
class.  It is not promoted to a general compiler obstruction.

The proof-search target contract is:

| field | contract |
|---|---|
| Target | compile the simultaneous intrinsic B matching with a bounded covariant protected link sector |
| Quantifiers/domain | all lawful code states; complete vacuum/N=1/N=2 censuses at L5 and held-L6 |
| Allowed premises | Cycle-219/230 coarse update, physical M2 sites, bounded local constraints and fixed schedules |
| Forbidden weakenings | global order/parity service, selected runtime branch, supplied nonlocal preparation, or dropping cubic frames |
| Required edge cases | vacuum, odd parity, periodic seams, endpoint reversal, deletion, leakage, inverse, and held size |
| Completion witness | an explicit `E` and `G_physical` with zero global intertwiner residual on the declared code |
| Not closure | an exact one-link action, a runtime-local phase with growing preparation, or a route-specific counterexample |

### N1 — alternative-route normalization

Families are normalized by `(object, mechanism, terminal obligation)`, not by
artifact or wording:

| family | normalized mechanism and terminal obligation | honesty/status |
|---|---|---|
| Cycle-236/Bell one-link | fermionic Majorana reference versus a product Bell stabilizer; exact local FSWAP intertwiner | **ATTEMPTED** — local closure, global product retains norm 2 |
| endpoint-diagonal product | arbitrary axis-dependent `f_a(q_x,q_y)`; solve every N<=2 sign equation | **ATTEMPTED** — exact L5/L6 inconsistent certificates |
| distributed prefix | local prefix constraints and seam phase; constant-depth lawful recode is terminal | **ATTEMPTED** — runtime phase exact, this preparation/recode scales |
| correlated link stabilizer/gauge | entangled link sector and local Gauss constraints; recurrent-patch isometry is terminal | **OPEN — NOT CLOSED** |
| non-diagonal stateful gauge | auxiliary state changes coherently during simultaneous B; constraint-preserving inverse is terminal | **OPEN — NOT CLOSED** |
| higher-form/topological | plaquette/face code with dynamical holonomy; all-sector local preparation and B intertwiner are terminal | **OPEN — NOT CLOSED** |

Because three materially distinct families remain open, N1 forbids a broad
no-go.  This is the reason for the explicit demotion above.

### N2 — wall-independence audit

The raw Bell mismatch is a special case of the larger endpoint-diagonal
product wall and is collapsed into `W_endpoint`; it is not double-counted.
The remaining wall-independence table is:

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---|---|---|
| `W_endpoint`, `W_prefix-prep/recode` | no | no | yes |
| `W_endpoint`, `W_four-M2-primitive` | no | no | yes |
| `W_prefix-prep/recode`, `W_four-M2-primitive` | no | no | yes |

The exact local comparator result is independent of the global matching
failure.  The prefix runtime phase is independent of its preparation and
recode depth.  None of the collapsed walls is substituted for another.

### N3 — hidden-wall scan

The hidden-condition phrase scan gives:

| phrase/hit | classification |
|---|---|
| “declared code/constraints” | explicit candidate definition, load-bearing and tested |
| “canonical positive-axis link” | response-family indexing convention; axis dependence is allowed and covariance is relaxed |
| “supplied structure” | explicit inventory: site-major reference basis, period-eight origin, coefficients, factor order, seam anchor |
| “by construction” / “standard QFT” / “obviously” | absent from the proof claims |

The site-major exterior basis is used only for the reference census;
translation equivalence is an explicit hypothesis of the GF(2) response
family.  The physical Bell candidate itself uses neither a global order nor a
parity service.  No hidden hit adds an uncounted wall.

### N4 — residual matching

| cited witness | witness residual | Cycle-528 residual | match? |
|---|---|---|---|
| Cycle 236 note/runner | one-link dressed FSWAP versus JW constraint locality/preparation | one-link action comparison only | yes for local action; **no** for full code projector, so not cited as global closure |
| Cycle 260 note/runner | exact order-change phase versus growing shuttle/marker preparation | exact prefix phase versus prefix preparation/recode | yes, at the preparation/runtime separation |
| Cycle 523 note/runner | endpoint B product versus intrinsic full B exterior action | same complete L5/L6 sign residual | yes |

The exact 60,600/154,800 counts, the L5 minimum two-row certificate, and the
L6 minimum one-row certificate identify `W_endpoint`.  Prefix deletions are
compared with the phase-indexed ordering change, not with an unrelated target.

### N5 — rhetoric audit

| resolution | tested result |
|---|---|
| one link | exact local comparator intertwiner, inverse, constraints, leakage, deletion |
| one endpoint-cell product response | included in the arbitrary local response variables |
| complete L5/L6 matching on N<=2 | exact mismatch census and GF(2) certificate |
| full Fock at L5/L6 | not tested because the required N<=2 widening gate failed |
| correlated/stateful gauge code | not tested and explicitly open |

The result is called a one-link closure and a route-class falsification.  It
is not called a physical-site compiler, a general local-gauge obstruction,
an impossibility theorem, or constitutional evidence.  A compiler factor
order is not called causal time; no phase is called physical energy.

### N6 — partial-closure path

Useful retained content is the covariant Bell comparator, exact local
constraints and preparation, live dressed update, all-frame layout, complete
sign census, minimal endpoint-response certificate, and exact localized
prefix runtime phase.  The unsynthesized four-M2 decomposition is a bounded
primitive-compilation task, not evidence for new physics.  A correlated link
code could reuse the placement and onsite fixture while replacing only the B
sector.  These are import-retirement/partial-closure paths, not axiom
proposals, and remain reusable even though full B closure fails.

### N7 — hostile steelman

The strongest surviving alternative is a correlated link code whose local
Gauss/stabilizer constraints make the auxiliary sector change coherently with
the simultaneous B matching.  Its next decisive test is an actual two-cell
and recurrent-patch isometry with a non-diagonal link transition, followed by
the same full L5/L6 sign census.  Cycle 236's exact dressed action is evidence
that auxiliary state can cancel a matter string conditionally, while Cycle
260's exact algebraic phase is evidence that a distributed carrier has the
right sign information; neither supplies the missing lawful recurrent
transition.  A second actionable alternative is a
distributed prefix/gauge field whose recode is a fixed constant-depth local
automorphism without a selected seam.  Neither has been tested here.

### N8 — cross-cycle echo

| prior echo | later disposition/mechanism | applicable here? |
|---|---|---|
| Cycle 236 exact dressed update / nonlocal JW constraints | not retired globally; Bell comparator retires only the one-link local-action question | yes, but insufficient for correlated preparation |
| Cycle 260 exact phase / growing shuttle | prefix field retires the runtime phase support, not preparation/recode | yes; motivates the open local-automorphism route |
| Cycle 523 onsite closure / norm-2 B wall | onsite wall retired by explicit bare schedule; B wall remains | yes; retain the onsite schedule and isolate B |

Cycle 528 therefore sharpens rather than repeats these walls.  The echoes are
consistent but do not establish a route-independent obstruction.

## Optimal next campaign

Build the N7 steelman rather than another endpoint phase ansatz: a correlated
link/stabilizer code with an explicit non-diagonal stateful B transition.
Start on the smallest two-cell/full-Fock patch, require local constraint
preservation and inverse/leakage controls, then widen immediately to a
recurrent patch and complete L5/held-L6 one-/two-particle census.  Keep the
Cycle-523 onsite schedule unchanged so the experiment isolates only the B
compiler wall.
