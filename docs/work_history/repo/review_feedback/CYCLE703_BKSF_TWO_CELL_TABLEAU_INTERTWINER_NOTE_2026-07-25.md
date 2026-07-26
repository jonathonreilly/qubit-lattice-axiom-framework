# Cycle 703 two-cell BKSF tableau intertwiner — review note

**Date:** 2026-07-25

**Type:** meta

**Authority:** none

**Audit:** unset

Terminology boundary: “physical” inside the stabilizer/tableau calculation
means the BKSF graph-edge-qubit layer as opposed to its logical matter
subsystem.  This note does not compose that layer with the Cycle-232 `Z^3`
site placement/repetition isometry and therefore does not close a strict
physical-site-M2 compiler.

**Reviewed object:** an explicit edge-qubit stabilizer-Clifford isometry for
the smallest connected two-complete-cell local-Gauss graph, with a fixed +1
loop character

**Status:** finite two-cell BKSF common-E and even-update intertwiner positive;
scalable locality-preserving preparation and periodic Wilson genesis open

## Verdict

The finite physical state-encoding seam isolated by the preceding Cycle-703
review is closed on the smallest connected patch containing two complete
six-matter-plus-reference cells.  The graph has 14 fermionic vertices and 38
edge qubits: each cell contributes 12 octahedral matter edges and six
matter-reference spokes, and the cells share one directed matter-stream edge
plus one parallel reference edge.

A deterministic spanning tree gives 25 independent fundamental-loop
constraints, exactly `38 - 14 + 1`.  Fixing those loop observables to the +1
character and fixing one independent local-D constraint leaves

```text
38 edge qubits - 25 loops - 1 independent D = 12 logical matter qubits.
```

For this open patch there is no noncontractible Wilson generator.  “Fixed
loop/Wilson character” therefore means the fixed +1 loop character here; a
periodic extension must additionally declare its three Wilson characters.
No periodic-Wilson preparation claim is smuggled into the open-patch result.

The companion constructs a phase-aware 76-row canonical Pauli tableau.  Its
first 12 commuting `W` rows are the physical `B(m)` representatives of the 12
matter `Z` operators.  The next 26 are the 25 loop stabilizers and one local-D
stabilizer.  The first 12 conjugate `V` rows are not arbitrary symplectic
partners: for matter mode `i` within either cell they are

```text
X_i^(BKSF) = -i [product_(k=i)^5 B(m_k)] A_(m_i,r).
```

An independent seven-mode Jordan-Wigner action verifies all 384 local columns
and fixes the phase so this operator flips matter bit `i`, flips the reference
parity bit, and has amplitude +1.  The remaining 26 `V` rows are obtained by
deterministic GF(2) symplectic completion.  The complete set is Hermitian,
rank 76, obeys the canonical commutator matrix, and round-trips exactly through
its inverse coordinates.  It therefore specifies a Clifford `C` and the
isometry

```text
E_BKSF |n_0 ... n_11> = C (|n_0 ... n_11> tensor |0>^26),
```

up to one irrelevant common phase.  This is an explicit stabilizer-tableau
state isometry, not a dimension-only existence argument and not a dense
`2^38` state construction.

The 24 logical `X/Z` rows have rank 24 modulo the 26 stabilizers.  The combined
rank is 50, and deleting any one of those 24 logical rows lowers it to 49.
Thus neither the stated logical count nor its orientation rests only on
commutator inspection.

This phase orientation is stronger than canonical commutators alone.  The
also-valid local prefix representative

```text
A_(m_i,r) product_(k<i) B(m_k)
```

has the same canonical `XX/XZ` algebra but decodes in this computational basis
as `-i X_i product_(k=0)^5 Z_k`.  A scalar phase cannot remove that
occupation-dependent cell-parity factor.  The exhaustive 64-state local phase
decoder per mode is why the suffix representative, rather than the raw prefix
representative, is used in `E_BKSF`.

The directed stream from left-cell matter mode 1 to right-cell matter mode 0
uses the physical words

```text
P = product_(k=1)^5 B(m_(right,k))
K = A_(m_left,1; m_right,0) A_(r_left,r_right)
H = [- P K + P B_u B_v K] / 2
FSWAP = [B_u + B_v - P K + P B_u B_v K] / 2.
```

Every Pauli summand commutes with all 26 selected stabilizers, so code leakage
is exactly zero by algebra rather than numerical tolerance.  Conjugating the
summands through the tableau gives the expected 12-mode CAR hop and fermionic
mode transposition on every one of the 4,096 logical occupation columns.
Thus, for the tested dressed hop and FSWAP,

```text
E_BKSF U_matter = U_phys E_BKSF
```

is certified without forming any dense edge-qubit matrix.  All 12 onsite `B`
operators and all 30 within-cell `B_i B_j` contact operators also decode to
the corresponding matter `Z_i` and `Z_i Z_j`, preserve the code, and
round-trip through the inverse tableau.

The companion additionally executes every one of the 24 octahedral onsite
coin edges.  For an ordered intracell graph edge `u<v`, it splits

```text
H_uv^(coin) = -i B_u (1-B_u B_v) A_uv / 2
            = [-i B_u A_uv + i B_v A_uv] / 2
```

into two Hermitian edge-qubit Pauli words, conjugates both through the tableau,
and compares their sum with an independently constructed 12-mode CAR hop on
all 4,096 logical columns.  All `24 * 4,096` actions, stabilizer commutators,
and inverse-tableau checks pass.  “Onsite generator coverage” here means the
12 occupations, 30 within-cell diagonal contacts, and all 24 available
octahedral coin edges; the three opposite-port pairs per cell are not graph
edges and are not silently counted.

This result closes the finite two-cell BKSF edge-qubit common-E objection.  It does
not prove bounded-depth or bounded-range preparation on a growing graph.  The
implemented symplectic completion solves equations against all tableau rows;
it is global Gaussian elimination.  On a graph family, a literal circuit
compiler for that completion is allowed to use two-qubit gates spanning the
patch diameter and a serial depth that grows with the number of edge qubits.
No geometry-local synthesis was run, and no lower bound ruling one out was
proved.  The exact statement is therefore: finite Clifford existence and
intertwining are positive; scalable local preparation depth/range are open,
and this particular global-elimination construction does not supply a
uniform bounded-depth/range encoder.

No axiom conclusion or route-independent no-go follows.

## Rank, phase, and character checks

The selected stabilizer set has rank 26 and no inconsistent phase relation.
All 25 fundamental loops are individually active: deleting any one lowers
the rank to 25 and releases one logical bit.  Deleting the selected
independent `D_left` row also lowers the rank to 25.  The graph identity

```text
D_left D_right = identity
```

is checked with phase, so the alternative presentation containing both local
`D` rows has rank 26 and either single-D deletion leaves its rank unchanged.
This separates “the chosen independent row is active” from the false claim
that every row in the redundant all-cell presentation is independently
active.

The +1 character is encoded in the signed loop Pauli rows themselves.  This
open graph has no noncontractible cycle left after the full fundamental-cycle
fix, hence Wilson rank zero.  The result neither deletes nor silently averages
over a Wilson sector.

## Tableau conjugation and inverse

Write the canonical rows as `W_i,V_i`, with
`[V_i,W_j]_s = delta_ij`.  Any physical Pauli `Q` has exact binary
coordinates

```text
beta_i = [Q,W_i]_s,
alpha_i = [Q,V_i]_s,
Q = i^q product_i V_i^beta_i product_i W_i^alpha_i.
```

For a code-preserving word, all `beta_i` belonging to the 26 stabilizer
partners vanish.  Its restriction is consequently the 12-qubit logical Pauli
formed from the first 12 coordinates; remaining `W` factors act as +1 on the
fixed code.  The companion checks the exact phase and binary round trip for
all 76 tableau generators and for every stream-hop, FSWAP, onsite-coin,
onsite-`B`, and contact summand.  This is both the forward conjugation and
inverse test requested by the state-isometry seam.

The 4,096-column comparison is then performed only in the 12-logical-qubit
occupation basis.  The physical side is never expanded into `2^38` rows.
This is an exact consequence of stabilizer code preservation plus canonical
tableau coordinates, not a sampled residual.

## Leakage and local support

Leakage is tested at the correct layer.  Each physical Pauli summand commutes
with every selected loop and local-D stabilizer.  Because the code projector
is their common +1 eigenspace, this commutation proves that both linear
combinations `H` and `FSWAP` preserve the code exactly.

The companion separately reports physical support weights for loops, the
selected `D`, logical `X/Z`, and the hop/FSWAP summands.  Every update word is
contained in this two-cell patch.  The arbitrary stabilizer destabilizers may
have wider support because they complete a global tableau; their support is
not credited as local update support or as a bounded preparation circuit.

The measured weights are:

| Object | Maximum Pauli weight |
| --- | ---: |
| fundamental-loop row | 27 |
| selected local `D` | 2 |
| logical `X` | 15 |
| logical `Z` | 6 |
| stream/coin update summand | 13 |
| globally completed stabilizer destabilizer | 12 |

These are held-patch measurements, not asymptotic bounds.  In particular, the
fundamental loops come from one deterministic spanning tree and need not be a
minimum-weight cycle basis.

## Circuit depth and range boundary

For the held 38-qubit instance the canonical tableau determines some finite
Clifford circuit.  The runner deliberately stops at that exact tableau: it
does not attach a hardware geometry and does not synthesize gates.  Across a
growing graph family, its linear systems contain every physical edge qubit
and every stabilizer row.  A direct Gaussian-elimination realization is
therefore nonuniform in size: its gate count/depth can grow with the edge
count, and its gate range can reach the graph diameter.

These are properties and permissions of the present construction, not a
topological lower-bound theorem.  Constant-depth local preparation could
still arise from a different loop basis, measurement and feed-forward,
pre-supplied entangled ancillas, code deformation, or another Clifford
synthesis.  Conversely, a fixed periodic Wilson character may itself require
a nonlocal resource.  Neither direction is decided by tableau rank.

The exact next size/geometry tasks are bounded.  Rebuild and invert the state
tableau on the open `L=2` cubic graph (eight cells, 168 edge qubits), then on
periodic `L=3` (27 cells, 648 edge qubits) after adding three explicit Wilson
rows.  If planar held patches are useful for gate routing, run open `2 x 2`
and `3 x 3` cell slabs as separate geometries rather than identifying them
with the three-dimensional `L=2,3` cubes.  For each held size: synthesize gates
on the declared edge-qubit adjacency, record depth and maximum routed range,
repeat the common-E hop/coin/contact conjugations without enumerating dense
physical states, and rebuild the encoding after translations/proper-cubic
frames.  None of those larger-size, periodic-character, or transformed-E
tasks is credited here.

## No-Go Discipline

**Gate result: FAIL for a broad preparation or compiler no-go.  Ship the
finite tableau positive and the named scalable-preparation boundary only.**

- **N1 — Alternative routes.** Materially distinct completion routes include
  a geometry-aware local Clifford synthesis of this tableau, a tree-grown
  open-boundary encoder, stabilizer measurement with feed-forward, a
  pre-prepared fixed-Wilson resource, code deformation with ancillas, and an
  exact nonconstant-depth encoder.  The present finite tableau already closes
  the state-isometry and even-update seams at two cells, so none of these can
  be collapsed into a broad impossibility claim.
- **N2 — Condition independence.** Finite code dimension, tableau phases,
  code preservation, logical operator intertwining, update support,
  preparation depth, preparation range, periodic Wilson selection, and
  transformed-E covariance are independent obligations.  Closing the first
  four does not close the latter four; failure to synthesize one circuit does
  not refute the finite isometry.
- **N3 — Hidden-condition scan.** The graph is open, connected, fixed-even,
  and exactly two complete cells.  All fundamental-loop eigenvalues are +1;
  one independent local-D row is selected; the other is redundant.  Matter
  bit order, reference placement, stream orientation, spectator parity,
  incidence order, and the absence of an open-patch Wilson generator are
  explicit.  Only parity-even updates are claimed.
- **N4 — Residual matching.** Stabilizer commutation matches physical leakage;
  canonical coordinates match edge-Pauli conjugation; 4,096 logical actions
  match the common-E intertwiner; deletion rank matches constraint activity.
  None of these residuals is relabeled as a local gate-synthesis or periodic
  Wilson-preparation result.
- **N5 — Resolution audit.** All logical columns are checked for the one
  displayed stream, all 76 generator inverses are checked, and every onsite
  `B`, within-cell contact, and all 24 octahedral coin edges are checked.  Other
  intercell port pairs follow the same formula but are not re-enumerated in
  this runner.  Larger sizes, periodic encoders, geometric circuit depth,
  translations, and proper-cubic transformed encodings are unexecuted.
- **N6 — Partial-closure and primitive scan.** The next constructive path is
  to synthesize this tableau with a declared edge-qubit geometry, measure
  depth/range on open `2 x 2`, `3 x 3`, and cubic `L=2` held patches, add the
  three periodic Wilson rows at `L=3`, and compare rebuilt encodings under
  translations and cubic frames.  This is a local research task; no new
  primitive, import, or axiom edit is justified by the finite result.
- **N7 — Steelman.** A strong positive compiler can take a fixed loop/Wilson
  stabilizer resource as admitted input, use the now explicit logical
  `X/Z` orientation, and compile the already bounded update Pauli words.  The
  exact two-cell result makes that route more credible even if preparation
  from product ancillas ultimately has growing depth.
- **N8 — Cross-cycle echo.** The prior Cycle-703 note correctly left the BKSF
  common-E tableau open; this runner closes that finite seam.  The surviving
  Wilson/genesis concern must not be echoed backward as a failure of the
  tableau, while the tableau must not be echoed forward as proof of bounded
  preparation or transformed-E covariance.

## Reproduction

```bash
PYTHONPATH=scripts python3 \
  scripts/frontier_cycle703_bksf_two_cell_tableau_intertwiner_2026_07_25.py
```

The companion should terminate with
`TWO_CELL_BKSF_TABLEAU_INTERTWINER_POSITIVE_SCALABLE_LOCAL_PREPARATION_OPEN`.
