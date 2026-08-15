# Finite orbit-table ranks on the rebuilt unit four-cube — Cycle 763

Date: 2026-08-09

Authority: none; self-contained finite construction proposed for independent audit.

Status: proposed_retained

Claim type: bounded_theorem

Primary runner:

- [finite orbit-table rank runner](../scripts/physical_cell_cutting_finite_orbit_ranks_cycle763_2026_08_09.py)

Direct scientific dependencies: none.

## Trace and status fields

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: physical_cell_cutting_finite_orbit_ranks_cycle763_bounded_theorem_note_2026-08-09
target_blocker_text: "classify invariant binary incidence tables on the explicitly rebuilt finite cell object"
source_of_blocker_text: frontier_question
reachability_to_target: "direct finite exhaustive construction"
artifact_role: "bounded finite incidence theorem candidate"
next_trace_action: "independent audit of the landed source and runner evidence"
conditional_surface_status: "the target domain is the declared finite incidence object"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact existence theorem for two same-shape invariant matrices on one declared finite object"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact target

On the finite object defined below, there exist two binary `192` by `192`
matrices that are constant on the cover-piece orbits of the full `384`-element
coordinate-relabeling action and have row sum `8` and column sum `8`. The
reconstructed cover table has exact integer rank `105`. The explicit union of
orbit labels `(6, 11, 28, 39)` has exact integer rank `144`.

The theorem's domain is the labelled finite incidence object in this note.
Its interpretation class is finite combinatorics; physical and multicell
interpretations belong to separate targets with additional definitions.

## Declared object

Start with the sixteen binary corners of the unit four-cube. A candidate piece
is a five-corner simplex whose four edge vectors from its first corner have
determinant of absolute value one. Keep the candidates at the minimum declared
adjacency cost. A cutting is a set of kept pieces with pairwise disjoint
interiors that fills the cell. A cover is an eight-piece set that meets every
cutting once.

The runner rebuilds this object from its definitions. It obtains `2,672`
unit-determinant candidates, adjacency-cost floor `6`, and `400` candidates at
that floor. Its `5^4 = 625` rational grid avoids every facet plane of every
kept piece. The exact-cover search returns `15,800` cuttings, each with `24`
pieces of volume `1/24`; the exact facet/intersection checks certify all
co-occurring pairs. Exactly `192` pieces occur, and the runner reconstructs
exactly `192` eight-piece covers.

Let `A` be the cutting-by-piece table and `B` the cover-by-piece table. Exact
rational elimination gives

| table | rank | kernel dimension | row sum | column sum |
| --- | ---: | ---: | ---: | ---: |
| `A` | 88 | 104 | 24 | 1,975 |
| `B` | 105 | 87 | 8 | 8 |

The two row spaces span all `192` coordinates and meet in the constant line.
Gate D10 separately recomputes the rank of `B` by fraction-free integer
elimination.

## Coordinate action and orbit tables

Permuting the four coordinates and independently flipping them gives `384`
distinct maps. Gate G4 checks all `147,456` products for closure. The action is
transitive on the supported pieces and on the covers, and every map preserves
both incidence tables.

The action has `104` orbits on ordered piece pairs, `120` orbits on ordered
cover pairs, and `96` orbits on cover-piece cells. Each cover-piece orbit has
size `384`. Consequently, each orbit indicator has exactly two ones in every
cover row and exactly two ones in every piece column.

Read one orbit indicator as a bipartite graph on the covers and pieces. Every
vertex has degree two, so the graph is a disjoint union of cycles. For every
one of the `96` orbits, the runner finds `48` cycles, each visiting four covers
and four pieces. A cycle visiting `k` vertices on each side has matrix rank
`k - 1` for even `k` and rank `k` for odd `k`: after cyclic ordering its
determinant rule is `1 + (-1)^(k+1)`. Thus every individual orbit indicator
has exact rank `48 * 3 = 144`. The independently computed mod-`1,000,003`
ranks agree.

## Two exact same-shape matrices

Each invariant binary matrix with row sum eight that is expressed as a union
of cover-piece orbits uses four orbit indicators. Gate G39 reconstructs `B`
as exactly such a four-orbit union. The modular ranks of its four prefixes are
`[144, 93, 114, 105]`; this list is labelled modular, while D10 supplies the
exact endpoint rank `105`.

Gate G41 constructs a second declared union using orbit labels
`(6, 11, 28, 39)`. It checks every row sum and column sum against `8`, then
computes exact integer rank `144`. Hence the target is discharged by two
explicit, invariant, same-shape binary matrices with exact ranks `105` and
`144`.

This is a positive existence witness inside the declared finite protocol. The
runner performs a full exact check of both advertised ranks rather than using
a sampled rank distribution.

## Stabilizer and orbital-basis diagnostics

The stabilizer of a piece has order two. Its non-identity element has plus and
minus eigenspace dimensions `104` and `88`. The cutting row space splits as
`50 + 38`, and the cover row space splits as `55 + 50`. All twelve order-two
elements fixing a piece produce the same six dimensions
`[104, 88, 50, 38, 55, 50]` by separate exact ranks.

The `104` ordered-pair orbit indicators form the canonical orbital basis for
matrices commuting with the piece action. Gates G12 and G13 report that
exactly two basis matrices individually preserve the cutting row space and
exactly two individually preserve the cover row space. These statements count
individual members of that basis. The dimension of the preserving subspace of
arbitrary linear combinations is outside the target.

Four determinant-one coordinate subgroups of order `24` are also constructed
and checked for closure. They provide finite group-action diagnostics only.

## Inputs, imports, and primitive-registry result

| input | class and provenance | role and sensitivity |
| --- | --- | --- |
| labelled unit four-cube, determinant-one simplex rule, adjacency cost, cutting and cover definitions | declared finite-model data in this note and runner | define the theorem's object; changing one defines another object |
| `5^4` rational test grid | declared enumeration device | exact genericity and intersection gates bind completeness for this construction |
| coordinate permutations and flips | declared finite action | defines the orbit partition used by the theorem |
| orbit labels `(6, 11, 28, 39)` | declared constructive witness in the runner's deterministic labelling | exact row, column, invariance-by-orbit, and rank gates bind the witness |
| prime `1,000,003` | computational diagnostic | used only after agreement with exact cutting and cover ranks; the advertised witness ranks use integer elimination |
| Python integer/rational arithmetic and NumPy integer arrays | implementation substrate | hostile controls and independent review recomputation cover the load-bearing operations |

The primitive-registry check defined by
`docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` returns an empty
premise dependency set for this target. The current axiom and approved
primitive registry contributes zero numerical or structural inputs. The
runner declares no `AUDIT_INPUT_PATHS` because it reads no data file; its own
source bytes are bound by the runner-cache execution identity.

## Proof-obligation graph

The exact target closes through this acyclic graph:

1. the declared corner, determinant, cost, cutting, and cover definitions
   determine the finite search domain;
2. G0-G3 reconstruct the pieces, certify the generic grid and exact cuttings,
   and construct `A` and `B`;
3. G4-G7 and G26-G33 construct the group actions, prove incidence invariance,
   and enumerate the ordered-pair and cover-piece orbits;
4. G36 and G38 certify the `48` four-cycle decomposition of every cover-piece
   orbit, and the displayed cycle lemma gives exact rank `144` for each orbit
   indicator;
5. G39 reconstructs `B` from four orbit indicators, while D10 computes its
   exact integer rank `105`;
6. G41 constructs the declared four-orbit witness, checks its binary
   row-and-column shape, and computes exact integer rank `144`;
7. the two matrices from steps 5 and 6 discharge the positive existence
   target.

The subgroup, stabilizer, orbital-basis, and modular-prefix measurements are
diagnostics. They are leaves with no load-bearing edge into step 7.

## Controls and execution contract

The runner declares `AUDIT_TIMEOUT_SEC = 600` and
`MEMORY_LIMIT_MB = 2500`, uses a monotonic clock, and converts `ru_maxrss` by
platform convention. Synthetic values immediately below and above the memory
limit exercise both the Linux KiB and Darwin byte conversions.

The rank controls include an exact `192` by `192` identity, a duplicated cover
table, and agreement between exact and modular ranks for both primary tables.
The cyclic-shift control lies outside the coordinate action and changes the
cutting table. Every gate failure contributes to the final `FAIL` count and
causes a nonzero process exit after output accounting.

## Review record

The first combined review round reproduced the finite enumeration and exact
rank core, then required a narrower target. This revision:

- replaces the broad physical-boundary framing with the finite exact target;
- removes the fixed-seed sample and its promoted one-prime statistics;
- adds an exact same-shape orbit-union witness;
- narrows the commutant statement to individual canonical basis matrices;
- inventories every finite and computational input after the primitive check;
- exposes the proof-obligation graph and keeps physical interpretation outside
  the target; and
- makes timeout, resource accounting, and failed-gate exit behavior
  fail-closed.
