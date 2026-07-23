# Physical root-label-blind face-pump compiler — Cycle 651

Status: **PASS — exact reversible supplied-syndrome circuit and covariant orbit-selector comparator; autonomous physical pump remains open**
Authority: **none**
Audit: **unset**
Accepted: **false**
Constitutional effect: **none**

## Exact target

The target is a bounded-neighborhood physical-M2 compiler for Cycle 648's
root-label-blind face-syndrome pump.  It must cover periodic L3, L6, and held
L7; exhaust even and odd syndrome controls; use elementary support at most two
after literal fine-nearest-neighbor lowering; commute with ordinary
translations, all 24 proper-cubic frames, and their 576 products; and expose
inverse, deletion, leakage, lawful-domain, environment, and pinned
mass/contact/seam controls.  It may not query a named root, coordinate-zero
sheet, host path service, preferred frame, or global parity bit.

A circuit driven by a supplied syndrome rail, an unplaced orbit field, a
family of shortest paths without collision control, or a Kraus formula without
local projectors does not complete the target.

Every executable premise is byte-pinned to immutable commit
`4f2b07fd39cc83a3f6c21bd9559f948b615bd05c`.  The runner imports only the
pinned Cycle-642 and Cycle-648 executables.  Cycle 649 is not on this shore;
its observed working-tree paths are neither read nor imported and remain the
named interface `UNCONSUMED_NOT_ON_IMMUTABLE_SHORE`.

## Strongest result

For a tree with vertex-syndrome bits `s_v`, blank work bits `w_v`, and blank
edge-history bits `h_e`, the directionless leaf circuit uses

```text
CNOT(s_v -> w_v)
CNOT(w_leaf -> h_edge), CNOT(h_edge -> w_parent)
CNOT(h_edge -> physical logical-edge correction)
reverse the leaf CNOTs
CNOT(s_v -> w_v)
```

The input syndrome rail is retained.  All work and history return blank.  Each
elementary logical gate touches two M2 registers, no vertex-name query occurs,
and exhaustive L3/L6/L7 tests send every even syndrome to zero and every odd
syndrome to one structural-center defect.  The complete circuit uses
`69/132/153` two-M2 logical gates across the three axes.

The decisive physical-copy audit then separates a fixed selector from an
orbit selector.  Choosing the sorted first member of each Cycle-642 physical
fiber gives `171/342/387` all24 failures.  Exhaustive enumeration of every odd
X subset in every size-4 or size-8 role fiber finds zero subsets invariant
under that role's proper-cubic stabilizer.  This narrowly falsifies a fixed
frame-invariant Pauli copy selector on the Cycle-642 repetition-fiber
encoding; it is not a general controller no-go.

There is an exact algebraic repair.  Carry the uniform selector over the full
fiber.  Proper-cubic frames permute that selector orbit, and any two
single-copy X branches differ by an existing pairwise `XX` equality check.
They therefore act identically on the declared equality-code space, so the
uniform selector disentangles and returns there.  All branch-equivalence and
all24 orbit residuals are zero on L3/L6/L7.

This is the strongest constructive result, but not yet a physical compiler.
The immutable shore places the Cycle-642 data/correction fibers, while it
places zero of Cycle 651's declared syndrome, work, history, or selector
roles.  Their exact unplaced controller counts are `33/60/69`.  The inherited
fine-NN route families have maximum path lengths `136/344/345`, but no
collision-safe controller chooses or traverses them autonomously.
The declared controller counts per coarse cell are
`1.2223/0.2778/0.2012`; their finite-size accounting is constant, while
bounded physical neighborhoods remain unproved because the roles are unplaced.

## Route A — reversible local message passing

Disposition:
`EXACT_REVERSIBLE_SUPPLIED_SYNDROME_COMPILER__PHYSICAL_EXTRACTION_SELECTOR_AND_NN_PLACEMENT_OPEN`.

The active tree is stripped by current degree, with all current leaves handled
in parallel.  No operation tests whether a vertex has the textual value
`root`.  A leaf copies its work syndrome to its edge history and that history
toggles the surviving neighbor.  The selected history bits control the
logical-edge X corrections, after which every compute step is reversed.

| size | syndromes/axis | two-M2 gates, 3 axes | work/inverse failures | all24/all576 failures | unplaced controller roles | fixed-copy all24 failures |
|---|---:|---:|---:|---:|---:|---:|
| L3 | 16 | 69 | 0 | 0/0 | 33 | 171 |
| L6 | 128 | 132 | 0 | 0/0 | 60 | 342 |
| L7 held | 256 | 153 | 0 | 0/0 | 69 | 387 |

Deleting one selected correction on every applicable even input leaves
exactly its two endpoint syndromes.  Flipping any one face bit of every even
input produces the one-defect odd control.  Applying the retained-input
correction twice returns the data correction bits to zero.

The logical circuit is reversible because it keeps `s_v`.  It does not
extract `s_v` from unknown physical data.  The new controller roles have no
placement on the immutable shore, so a two-M2 logical gate is not credited as
a fine-NN physical gate.

## Route B — translation/frame-orbit virtual defect field

Disposition:
`EXACT_VIRTUAL_TRANSLATION_ORBIT_AND_UNIFORM_COPY_SELECTOR__PHYSICAL_FIELD_PLACEMENT_AND_ODD_ABSORBER_OPEN`.

The fixed Cycle-642 tree `T0` is reflection invariant and frame covariant, but
it is not ordinarily translation invariant on L6 or L7.  Translating its
numeric vertices gives these exact edge-set symmetric differences:

| size | differences for shifts `0..L-1` | distinct translated trees | extra logical edges for the full orbit |
|---|---|---:|---:|
| L3 | `0,0,0` | 1 | 0 |
| L6 | `0,8,6,4,6,8` | 6 | 90 |
| L7 held | `0,6,10,8,8,10,6` | 7 | 126 |

The complete family `{T_t}` closes exactly: translation sends `T_t` to
`T_(t+a)`, frame reflection sends `t` to `-t`, and axis rotations permute the
three axis families.  Exhaustive syndrome decoding commutes with every
translation; family and label checks return zero all24 and all576 failures.
The local handoff remains the two-CNOT leaf tile and maximum tree degree is
four.

The orbit-uniform physical-copy selector repairs the fixed-copy covariance
failure on the equality-code space.  However, the extra translated-tree
edges and every selector M2 have physical-placement count zero.  No orbit-label
state is prepared.  Thus this is a covariant virtual field comparator, not a
physical translation-covariant controller.

Odd input requires no global parity query: local handoffs simply leave one
defect at the structural center.  The lawful pumping domain is even face
syndrome, equivalent to the already-fixed Wilson-plus dependency.  No odd
absorber or sector-changing service is introduced.

## Route C — dissipative/Stinespring comparator

Disposition:
`EXACT_STINESPRING_SYNDROME_RESET_COMPARATOR__ENVIRONMENT_RETAINED_AND_PHYSICAL_PROJECTORS_UNPLACED`.

For each even syndrome `s`, let `P_s` be its orthogonal face-syndrome projector
and let `j(s)` be the exact leaf-decoder edge current.  The comparator is

```text
K_s = X(j(s)) P_s,
V |psi_s> = |s_numeric>_environment X(j(s)) |psi_s>.
```

The numeric-vertex syndrome contains `L` independent bits per axis on the
even domain.  The projectors are disjoint and exhaust that domain, so the
Kraus family is trace preserving there.  Exhaustive even and odd labels give
no Stinespring image collisions.  The uniform physical-copy selector returns
on the equality-code space and adds no selector label to the retained
environment.

Composing the exhaustive decoder action, translated-tree family, and uniform
selector gives zero all24/all576 Stinespring covariance residuals.  This is
still algebraic composition: the orbit field and physical projector
controller are unplaced.

| size | even Kraus sectors/axis | syndrome-environment M2/axis | collisions after deleting one environment coordinate | maximum face-projector support |
|---|---:|---:|---:|---:|
| L3 | 8 | 3 | 4 | 17 |
| L6 | 64 | 6 | 32 | 24 |
| L7 held | 128 | 7 | 64 | 17 |

Deleting one independent environment coordinate merges exactly
`4/32/64` pairs of even syndrome sectors after reset.  A one-face leakage
flip always exits to the explicit odd residual.  The environment is retained;
it is neither returned blank nor assigned Record or occurrence semantics.
The high-support physical projectors and their crossing-safe routed
measurements remain unplaced.

## Held-size, covariance, inverse, deletion, leakage, and lawful-domain controls

- Every syndrome word is exhausted per axis: `16/128/256` total and
  `8/64/128` even at L3/L6/L7.
- Route A returns all work/history, preserves its input rail, checks double
  application, correction deletion, and one-face leakage.
- Route A's decoder and leaf layers have zero all24/all576 residuals, while
  its fixed physical copy selector is separately falsified.
- Route B exhausts translation covariance of every syndrome on the complete
  tree orbit and checks the frame/translation label action.
- Route C explicitly retains its syndrome environment and tests coordinate
  deletion and even-to-odd leakage.
- Cycle 642 target-times-gauge rows and the Cycle-219 mass, Cycle-230 contact
  deletion, and Cycle-230 seam fixtures remain pinned.

## N1-N8 discipline

The freshness check fetched origin main.  Cycle 651 follows the current
no-go-discipline body with SHA-256
`7d1aea8243ddd972331b935e2e836657e72115da3efe259f828fe862469d68b7`
and proof-search governance with SHA-256
`be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258`.

N1 records the three executed families above.  Five materially different
routes remain open and are not counted as failures: a verified sidecar
placement, static subsystem wires, an asynchronous quantum-walk router, a
virtual-bond tree tensor, and a mobile odd-defect pair.  The observed Cycle
649 working-tree interface is explicitly unconsumed.

N2 keeps five scoped interfaces: syndrome extraction, collision-safe routing,
ordinary-translation origin removal, odd-defect treatment, and environment
return.  All 20 ordered directions are explicit with
`closure_implied=false`; independence beyond the executed interfaces is not
asserted.  N3 inventories every retained rail, blank rail, tree, fiber,
selector, orbit label, lawful domain, environment bit, and inherited path
family.

N4 matches Cycle 648's physical-routing and odd-defect residuals and Cycle
642's crossing-enforcement residual.  Cycle 643's global tableau residual is
dropped as a nonmatch.  N5 audits five negative phrases at element, site,
mode, block, and lattice resolutions.  N6 lists five partial-closure paths,
including Cycle 649 only as an unconsumed interface.

N7's strongest counter-route combines a verified sidecar orbit, the exact
uniform selector, and state-carried collision arbitration.  N8 records the
origin-retirement, route, tableau, and leaf-decoder mechanisms from Cycles
629, 642, 643, and 648 with exact immutable references.

```text
broad negative gate: FAIL / DO NOT SHIP
minimum-content gate: FAIL / DO NOT SHIP
shared-obstruction gate: FAIL / DO NOT SHIP
axiom-pressure gate: FAIL / DO NOT SHIP
```

All four shipped flags are false.  No impossibility, minimum-content,
shared-obstruction, or axiom-pressure claim is shipped.  The exact fixed-copy
falsifier is scoped only to a fixed stabilizer-invariant odd-X subset on the
immutable Cycle-642 fibers.  The orbit-uniform repair keeps broader routes
open.

## Supplied structure

- immutable Cycle-642/Cycle-648 shore `4f2b07fd39`;
- finite L3/L6/L7 sizes and the Cycle-642 tree topology;
- a retained local syndrome input rail;
- blank work and edge-history rails;
- Cycle-642 orbit fibers and complete pairwise `XX` equality checks;
- a virtual uniform selector for every logical correction edge;
- the complete translated-tree family;
- the even lawful domain and explicit odd residual;
- syndrome-labelled Stinespring environment bits;
- Cycle-642 shortest-path families without collision arbitration;
- pinned target-times-gauge, mass, contact, and seam comparators.

Not supplied are physical controller, selector, or translated-tree-orbit
placements; autonomous data-to-syndrome projectors; collision control;
orbit-label preparation; an odd absorber; returned dissipative exhaust;
physical time; energy; a rate; a Record; an occurrence; source stress;
gravity; or a Born law.

## Prior-art and novelty boundary

Reversible Boolean circuits, stabilizer recovery, syndrome-projector Kraus
maps, Stinespring dilation, tree peeling, and group averaging are established
methods.  Cycle 651 claims no invention of those general methods.

The new repository-local result is their exact application to the Cycle-642
orbit fibers: the `171/342/387` fixed-selector frame failure, the exhaustive
absence of a stabilizer-invariant odd-X subset, the equality-code proof that
the orbit-uniform selector returns, the `69/132/153` two-M2 reversible
supplied-syndrome circuits, and the full translated-tree family with exact
ordinary-translation/all24/all576 covariance.

Thirring is not used.

## Dependency ledger

| wall | Cycle-651 movement | exact residual |
|---|---|---|
| `C_ref` | advanced algebraically | fixed-copy selection is replaced by a uniform fiber orbit and full translated-tree family; physical selector/orbit-label genesis remains |
| `C_num` | advanced locally | exhaustive environment-label and deletion-collision counts; no empirical or Born normalization |
| `C_wrap` | advanced | reversible even/odd message compilation and exact one-defect odd boundary; no odd absorber or full physical reset |
| `C_int` | pinned | Cycle-642 quotient and Cycle-219/Cycle-230 fixtures only; no new `E G = G E` intertwiner |
| `C_local` | advanced abstractly | every controller gate has support two and work returns from a retained syndrome rail; extraction, placement, and collision-safe NN lowering remain |
| `C_source` | unchanged | no energy, rate, source, stress, gravity, Record, occurrence, or autonomous environment renewal |

Cycle 651 does not independently rebase campaign lane coordinates.

## Scope firewall

- A retained syndrome input rail is not autonomous syndrome extraction.
- A two-M2 logical gate is not fine-NN without placed endpoints and routes.
- A uniform virtual selector is not a prepared physical selector.
- A translation-orbit family is not preparation of its orbit-label state.
- A Stinespring environment is not returned merely because it is explicit.
- The environment is not a Record or occurrence.
- One odd residual is not odd-sector genesis.
- A compiler layer is not physical time.
- A phase is not energy; a generator is not a rate.
- No source, gravity, or Born claim is present.

## Optimal next campaign

Use no uncommitted placement premise.  Independently place one all24 orbit of
syndrome, work, history, and uniform-selector sidecars.  Compile one
Cycle-642 face projector and one logical-edge correction through a
collision-safe state-carried fine-NN router, including inverse, deletion,
leakage, ordinary translations, and environment accounting.  Scale to all
faces only after that literal one-check controller passes.
