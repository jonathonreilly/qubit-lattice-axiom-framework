# Finite switch geometry and a piece-additive charge on supplied least-cost cuttings — Cycle 735

Date: 2026-08-05

Claim type: bounded_theorem

Status: unaudited source note

Audit authority: none; audit status belongs to the independent audit lane.

## Supplied model and result

The supplied object is the unit four-cube `{0,1}^4`, with three columns labelled
spatial and one labelled tick.  Allowed pieces are normalized-volume-one five-corner
simplices.  The supplied cost of a piece counts vertex pairs whose L1 separation in all
four coordinates exceeds one.  A cutting is an exact 24-piece cover.

This four-coordinate cost is not framework nearest-neighbour adjacency.  The framework
does not select this cell, piece class, cost, cutting, or physical tick.  The direct
scientific predecessor is
[`PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md`](PHYSICAL_LEAST_COST_CUTTING_FLIP_AND_MOVE_LADDER_CYCLE734_NOTE_2026-08-04.md),
which supplies the exact least-cost population and move/region structure.  The runner
binds Cycle 734's generated receipt and independently reconstructs its inputs.

Within this finite model:

- 15,800 cost-144 cuttings use 192 of the 400 cost-6 pieces;
- replacing four pieces gives 46,128 edges labelled by 120 two-way regions;
- the four-piece move graph has 349 connected components, but also contains embedded
  families of six mutually commuting region switches;
- an exact GF(2) weight on the 192 pieces induces a symmetry-fixed two-sided partition
  of the cuttings, of sizes 7,704 and 8,096.  Every four-piece move reverses it and every
  six-piece move keeps it.

## The correction found by review

The submitted note claimed that independent switch behaviour stopped at dimension two.
That was false.  Its gate classified only connected components that were globally cube
graphs.  It did not search for cube subgraphs inside larger components.

The repaired primary and independent checker exhaustively extend labelled commuting
switch cubes.  A new region label is admitted only if its involution exists at every old
vertex, reaches a disjoint copy of the old cube, and commutes with every earlier label on
every vertex.  Sorted extension makes the enumeration complete.  The maximum dimension
is six: there are 160 distinct labelled dimension-six cubes, each containing 64
cuttings, and none in dimension seven.

The original whole-component result survives in its proper scope.  The 349 components
have size census

`1:144, 2:96, 4:36, 7:48, 236:24, 9320:1`.

Exactly 276 entire components are cubes, covering 480 cuttings, and their dimensions are
zero, one, or two.  No other entire component even has power-of-two size.  Thus global
component factorization stops at dimension two while embedded independent switch
families reach dimension six.

The smallest non-cube component has seven cuttings, four region labels, eight edges, and
degree pattern one 4 plus six 2s.  Across all cuttings, 273,936 unordered pairs of
available switches occur; 54,912 pairs share a piece.  The largest component contains
9,320 cuttings and 33,216 edges, with eccentricity 16 from its fixed first vertex.

## Exact piece-additive GF(2) charge

Let a piece weight be a vector in `GF(2)^192`, and label a cutting by the sum of its 24
piece weights.  Requiring every four-piece region flip to reverse the label gives 120
rows of rank 86.  The system is consistent, with a 106-dimensional weight kernel; its
induced labels on the 15,800 cuttings span dimension two.

Adding the requirement that every six-piece move keep the label raises the rank to 87.
The 105-dimensional weight kernel induces only one free sign on the cutting population.
The two solutions differ on every cutting and therefore name one unordered split of
sizes 7,704 and 8,096.  The primary's representative uses 56 pieces and separates all
120 region pairs; removing any selected piece breaks at least one row.

Every one of the 46,128 four-piece moves reverses the charge; none of the 31,968
six-piece moves does.  The undemanded sizes are mixed: 26,880 of 60,096 seven-piece
moves and 28,608 of 151,704 eight-piece moves reverse it.

No single region row carries the rank: deleting any one retains rank 86.  The 120 rows
form five carried families.  Deleting a whole family of size 12, 12, 24, 24, or 48
leaves rank 84, 84, 75, 83, or 64 respectively.

The 48 cuttings with no cost-keeping move replacing eight pieces or fewer form one orbit
of the 48-element carried action.  All lie on the smaller side of the charge.

## Ansatz-bounded negatives and No-Go Discipline

Two negative conclusions are finite and explicit:

1. No embedded labelled switch cube has dimension seven in this exact 15,800-vertex,
   120-label graph.
2. The fixed 192-piece additive GF(2) system is inconsistent if both four-piece and
   six-piece moves are required to reverse.

Neither conclusion rules out another supplied model, another move definition, a
non-piece-additive labelling, a different coefficient field, or a physical construction.

- N1 — Alternative routes: whole-component classification, exhaustive embedded-cube
  closure, primary bit-mask elimination, independent dense-array elimination, and direct
  graph colouring were compared.  Other label languages and models remain open.
- N2 — Wall independence: the dimension-seven wall is graph-theoretic; the reversed
  six-move wall is confined to the fixed piece-additive GF(2) matrix.  Neither depends on
  physical selection, multi-cell gluing, dynamics, or a continuum limit.
- N3 — Hidden walls: `no`, `cannot`, `impossible`, `independent`, `must`, and `all` were
  scanned.  Every surviving negative names its finite graph or algebraic ansatz.
- N4 — Residual matching: Cycle 734 supplies only exact finite floor/move/region data.
  No physical interpretation or universality is inherited.
- N5 — Resolution: per element, all 192 used pieces and 120 region rows; per site, one
  supplied 16-corner cell; per mode, no field/spectral/momentum mode; per block, all
  15,800 cuttings, 124,812,100 pairs, move graphs, and embedded cubes; lattice-wide, no
  multi-cell, arbitrary-L, thermodynamic, boundary, or continuum operation.
- N6 — Partial closure: higher-dimensional cubes may occur in other move graphs, and a
  non-additive or non-GF(2) charge may meet other reversal rules.
- N7 — Steelman: the submitted dimension-two claim confused global connected-component
  factorization with local commuting subgraphs.  The repaired theorem accepts that
  objection and reports the exact dimension-six counterstructure.
- N8 — Cross-cycle echo: Cycle 734 is direct because its floor/move/region data are
  consumed.  Cycle 733 is ordering/context only; none of its parity certificates or
  support/refill claims supplies a Cycle 735 step.

No-Go status for these two bounded finite negatives: PASS.

## Independent reconstruction and hostile tests

The independent checker does not import or execute the primary.  It uses an opposite
exact-cover pivot, reconstructs all 15,800 covers, verifies all 15,168 co-occurring
piece pairs with 2,928 primitive normals, and recomputes all 124,812,100 cutting pairs by
packed XOR/popcount rather than the primary's Gram product.  It rebuilds the 120 region
labels, whole-component and embedded-cube censuses, and GF(2) systems using dense array
elimination.  It also reconstructs the five region families and the 48-cutting orbit.

Hostile controls flip a region target, demand reversal at six pieces, remove a selected
charge piece, and duplicate a cover piece.  The affected gates fail closed.

## Claim boundary

What is proved is exact finite combinatorics for the supplied one-cell model: its
least-cost population, labelled move graph, embedded/whole cube structure, one
piece-additive GF(2) charge split, and stated move/isolation counts.

What is not proved:

- physical selection of the cell, tick, simplex class, cost, moves, or charge;
- that the label is a conserved or observable physical quantity;
- uniqueness among all label languages or coefficient systems;
- a result for another cost, piece class, cell extent, repeated domain, arbitrary L,
  boundary limit, thermodynamic limit, continuum, gravity, Record, or Born rule.

## Artifacts

- Primary runner:
  `scripts/physical_least_cost_cutting_piece_charge_cycle735_2026_08_05.py`
- Independent checker:
  `scripts/physical_least_cost_cutting_piece_charge_cycle735_independent_check_2026_08_05.py`
- Primary cache:
  `logs/runner-cache/physical_least_cost_cutting_piece_charge_cycle735_2026_08_05.txt`
- Independent cache:
  `logs/runner-cache/physical_least_cost_cutting_piece_charge_cycle735_independent_check_2026_08_05.txt`
- Generated receipt:
  `outputs/physical_least_cost_cutting_piece_charge_cycle735_2026_08_05_receipt_2026-08-05.json`

## Review-loop record

On 2026-08-12 the review loop independently refuted the submitted dimension-two ceiling,
repaired it to the exact global-versus-embedded distinction, and retained the verified
charge and finite graph results.  It also demoted the construction to supplied data;
made Cycle 734 a direct input-bound dependency; narrowed negative claims; added an
independent checker, hostile controls, canonical caches, generated receipt, fail-closed
exits, and the N1-N8/N5 packet above.  This is source-review provenance, not an audit
verdict.
