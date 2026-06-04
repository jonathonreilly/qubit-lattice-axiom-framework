# The Many-Body (N=3) Graph-Braid Fermion Sign Stays Non-Fibered: at Three Generations the Exchange Z_2 Is Still a Codimension-1 Non-Base-Edge Class

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit. This note adds no axiom and no import; it answers
an open many-body sub-question negatively (no fibered enrichment at N=3).
**Primary runner:** `scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py` (SCORECARD PASS=26)

## Context (the open sub-question / the attacked assumption)

The N=2 graph-braid result
`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29`
(`retained_bounded`) computes `H_1(UD_2(Z^3)) = Z^{beta_1} (+) Z_2`, the `Z_2`
being the two-token exchange (Y-)class, and the cross-site no-go
`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28`
(`retained_no_go`) records that this exchange `Z_2` is **decoupled from**
single-edge data: it is a **non-fibered** class — not a base-edge "link-sign"
class that would couple to a base-edge `sign(beta)`. The FS no-go's §7 names the
**open** lattice-native escape: build the graph-braid `pi_1` of `UD_N` and check
whether a fibered exchange-loop structure couples the sign to the lattice. The
session question is the sharp many-body form:

> Does the **N=3** (the three generations!) many-body graph-braid
> `H_1(UD_3(Z^3))` have a **fibered** fermion sign (richer torsion that **is** a
> base-edge class, coupling to `sign(beta)`) unlike N=2?

This note answers **no**, by direct generalization of the repo's `UD_2`
construction to `UD_3` and an explicit fibered/non-fibered cohomology test.

## Claim

At the **N = 3 (three-generation) many-body** level, the graph-braid first
homology of the Abrams discretized unordered 3-particle space on the framework's
`Z^3` lattice has **the same** statistics structure as N = 2:

> **(i) Torsion stays a single `Z_2`.** Integral `H_1(UD_3)` on the small
> non-planar witness `K_5` is `Z^6 (+) Z_2` — the **same order-2** exchange class
> as N = 2, with **no `Z_3` / `Z_4`** enrichment. So
> `Hom(H_1, U(1))` on the torsion stays `{+1, -1}`: the exchange phase is
> **boson/fermion**, and **no anyon / parastatistics** phase appears at N = 3.
>
> **(ii) The exchange `Z_2` is still NON-FIBERED.** Over `GF(2)`, the base-edge
> "link-sign" cochains `{w_e}` (whose `GF(2)` combinations are the most general
> `sign(beta)` class) span a subspace of `H^1(UD_N; Z_2)` of codimension
> **exactly 1**, at **both N = 2 and N = 3**, and that 1-dimensional complement
> **is** the exchange class. The fermion sign therefore does **not** couple to
> any base-edge `sign(beta)` — it is a non-fibered class for the three-generation
> sector exactly as for two tokens.

**Classification: positive narrowing.** Going to the three-generation (N = 3)
many-body sector does **not** make the fermion sign fibered, and does not enrich
the exchange beyond `Z_2`. It is **not** a derivation of fermionic statistics
(the boson/fermion *sign* on the codim-1 class is still a free 1D-rep choice);
it closes the *fibered-enrichment* escape A10 for N = 3.

### The computation (runner, all 26 checks pass)

The runner generalizes the repo's `UD_2` Abrams cube complex (0-cells = disjoint
vertex pairs; 1-cells = vertex + non-incident edge; 2-cells = vertex-disjoint
edge pairs) to **arbitrary N**: an unordered cell is a closure-disjoint set of
`N` atoms (vertices/edges), `dim` = number of edge atoms, with the cubical
boundary carrying the Koszul sign from the edge-atom ordering. It then:

- **(A) Integral `H_1` via Smith normal form.** Re-verifies the repo N = 2 facts
  (`C_5, K_4` torsion-free; `K_5 = Z^6 (+) Z_2`; `K_{3,3} = Z^4 (+) Z_2`) for
  cross-validation, then computes N = 3: `K_5 -> Z^6 (+) Z_2` (single `Z_2`, all
  torsion order 2). `Hom(Z_2, U(1)) = {+1, -1}` (still boson/fermion).
- **(B) The fibered test over `GF(2)`.** Builds `H^1(UD_N; Z_2) = (ker D2^T /
  im D1)` and the fibered subspace `span{[w_e]}`; reports the non-fibered
  complement dimension. Result: **codimension exactly 1 at N = 2 and N = 3** on
  `K_5`, `K_{3,3}`, **and** the **genuine `K_{3,3}` subdivision extracted from the
  real `Z^3` cube `L = 3`** (`V = 14, E = 17`, a subgraph of the lattice). The
  non-fibered complement is the exchange `Z_2`.
- **(C) Abrams subdivision stability.** Subdividing `K_{3,3}` (so it is
  sufficiently subdivided for N = 3, satisfying Abrams' length condition) leaves
  `(dim H^1, dim fibered, codim)` unchanged (`k = 1 -> k = 2`), so the codim-1
  non-fibered structure is **topological**, not a coarse-graph artifact.
  (Raw `K_{3,3}` is under-subdivided for N = 3 — its integral `H_1(UD_3)` torsion
  vanishes until subdivided — which is exactly why this stability check is
  included; `K_5`, with 5 vertices and no room for 3 disjoint edges, is the clean
  small integral-torsion witness.)

### What "fibered" means here (made precise)

A `Z_2` cohomology class is **fibered / a base-edge (link-sign) class** if it
lies in the `GF(2)`-span of the base-edge cochains `w_e` (`w_e = 1` on a 1-cell
whose moving atom is base edge `e`). The holonomy of such a class on any loop is
the product of base-edge link signs traversed — a base-graph pullback that
**couples to `sign(beta)`**. The **exchange / Y-class** is detected by a local
token swap at a vertex of degree `>= 3` and is independent of single-edge
traversal counts. The decisive measurement is the **codimension of the fibered
subspace** in `H^1(UD_N; Z_2)`: codim 1 (the exchange) means the fermion sign is
non-fibered.

## No-go discipline gate (N1–N8)

**Status:** PASS for the narrow N = 3 graph-braid persistence claim only. The
proposition being recorded is *not* a repo-wide impossibility of fermion-sign
emergence and *not* a claim that the graph-braid program is dead. It is the
single computed statement that, at the physical three-particle (N = 3,
three-generation) level, the configuration-space exchange `Z_2` of
`H_1(UD_3(Z^3))` stays order-2 with base-edge (worldline-direction) projection
`P(t) = 0` — non-fibered, the same as N = 2 — so the first-quantized graph-braid
route does **not** spontaneously supply the CAR sign as a fibered geometric
class. "Non-fibered" is the precise codim-1-of-`H^1(UD_N; Z_2)` statement of the
"### What 'fibered' means here" section: the exchange class is **not** in the
`GF(2)`-span of the base-edge link-sign cochains `{w_e}`.

### N1 — Alternative route enumeration

The four routes by which the N = 3 sector could have *escaped* this persistence
claim (i.e. by which going from two tokens to the physical three could have made
the exchange sign richer than `Z_2`, or fibered over a base-lattice edge so that
it couples to a worldline-direction `sign(beta)`). Each is evaluated by the
runner at exact precision; none survives.

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Richer-torsion (parastatistics) | At N = 3 obtain `Z_3`/`Z_4` (or higher) torsion in `H_1(UD_3)`, giving an anyon/parastatistics phase beyond `{+1,-1}`. | Smith normal form of `d2` on the clean integral witness `K_5` returns `H_1(UD_3) = Z^6 (+) Z_2`: all torsion is order 2, no `Z_3`/`Z_4`. `Hom(Z_2, U(1)) = {+1,-1}` stays boson/fermion. | REFUTED (runner Part A) |
| Fibered-exchange | At N = 3 the exchange class falls into the `GF(2)`-span of base-edge link-sign cochains `{w_e}`, so its holonomy becomes a product of base-edge `sign(beta)` link-signs (a base-graph pullback). | The fibered subspace `span{[w_e]}` has codimension **exactly 1** in `H^1(UD_N; Z_2)` at N = 3 (and N = 2), and the 1-dim complement *is* the exchange class — `P(t) = 0` on every base edge. | REFUTED (runner Part B) |
| Coarse-graph artifact | The codim-1 complement is an artifact of an under-subdivided witness graph and dissolves once the graph is subdivided to satisfy Abrams' length condition. | Subdividing `K_{3,3}` (`k = 1 -> k = 2`, sufficient for N = 3) leaves `(dim H^1, dim fibered, codim)` unchanged: the structure is topological, not combinatorial coarseness. | REFUTED (runner Part C) |
| Witness-not-lattice | The non-fibered codim-1 holds for abstract Kuratowski graphs `K_5`/`K_{3,3}` but *not* for the framework's actual `Z^3` site graph. | The fibered test returns codim 1 on the genuine `K_{3,3}` subdivision *extracted from the real `Z^3` cube* `L = 3` (`V = 14, E = 17`, a subgraph of the lattice), not only on abstract `K_5`/`K_{3,3}`. | REFUTED (runner Part B, `Z^3`-cube witness) |
| Higher-N continuation | The claim is asserted for all `N >= 4` / the full infinite `Z^3`, over-reaching beyond what is computed. | NOT attempted as a closure; `N >= 4` and the infinite lattice are explicitly flagged as *expected* (Ko-Park/HKRS structure) but **untested**, and are left as a next path, not part of the persistence claim. | OUT OF SCOPE (deliberately not closed) |

### N2 — Wall-independence audit

The collapsed wall set for this persistence claim has a single load-bearing
wall: *the exchange `Z_2` lies in the codim-1 complement of the base-edge
link-sign subspace of `H^1(UD_N; Z_2)`* (equivalently `P(t) = 0` on every base
edge). The two refuted alternative-route walls are not independent walls — the
"richer-torsion" route is foreclosed by the integral `H_1` computation and the
"fibered-exchange" route by the `GF(2)` codimension computation, but both reduce
to the same Abrams cube-complex boundary maps `(d1, d2)` on the same witness; no
*second*, separately-retained obstruction is invoked. Crucially, this wall is
**independent of the boson/fermion sign-selection wall**: choosing the `-1`
(fermionic) value of the free 1D-rep on the codim-1 class is a *different*
question that this note does not touch (see N5). Closing a future *second-quantized*
graded-locality route would not move this first-quantized homology wall at all;
it lives on a different axis (field-algebra grading, not configuration-space
topology).

### N3 — Hidden-wall scan

The load-bearing inputs are explicit and finite; "fibered", "non-fibered",
"three generations", and "CAR" are *not* used as hidden retained inputs for the
result:

- the `Z^3` site-graph shape (used only to extract the genuine `K_{3,3}`
  subdivision witness via `networkx` planarity; `K_5`/`K_{3,3}` are the abstract
  cross-checks);
- the Abrams discretized unordered-`N`-particle cube complex `UD_N(Γ)`
  (0-cells = closure-disjoint vertex `N`-sets; 1-cells = vertex + non-incident
  edge; 2-cells = vertex-disjoint edge pairs) with the **Koszul-signed** cubical
  boundary from edge-atom ordering;
- exact integer Smith normal form over `ℤ` (integral `H_1` torsion);
- `GF(2)` linear algebra: cocycles `Z^1 = ker D2^T`, coboundaries `B^1 = im D1`,
  and the base-edge link-sign cochains `{w_e}` reduced mod `B^1`.

No retained tier of any other note is consumed for the homology facts. The
"three generations" identification of `N = 3` is *interpretive framing*, not a
load-bearing premise: the computation is performed for unordered `N = 3` tokens
regardless of the generation reading. The retained per-site dim-2 result
(`cl3_per_site_hilbert_dim_two`) enters **contextually only**, for the
surviving-statistics narrative, and is not used to derive the codimension.

### N4 — Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28` §7 path 1 (lattice-native graph-braid `π_1`, the "A10" escape) | Whether a lattice-native `UD_N` graph-braid structure manufactures a `Z_2` exchange that **couples to** the on-site `2O` `2π = -1` sign via a base-edge (fibered) `sign(beta)`. | The N = 3 instance of exactly that residual: the exchange `Z_2` is computed to be non-fibered (codim-1, `P(t) = 0`), so it does **not** couple to a base-edge `sign(beta)`. | yes (the N = 3 case of the open §7-path-1 escape) |
| `GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29` (`retained_bounded`) | The N = 2 facts `H_1(UD_2) = Z^{β_1} (+) Z_2` (anyons excluded, exchange `Z_2`). | The same construction extended to N = 3, re-deriving the N = 2 facts (`K_5 -> Z^6 (+) Z_2`, etc.) as cross-validation before the N = 3 computation. | yes (positive input, recomputed) |
| `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25` (`retained_no_go`) | The open **second-quantized** field-algebra-grading bridge that would supply the cross-site CAR sign. | NOT attacked here; the second-quantized graded-locality axis is a *different* route (§7 path 2), left open. | no (orthogonal open route, not this note's residual) |
| `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28` (`retained_bounded`) | The on-site `2O` spinor `2π = -1` sign (the spinor-`Z_2` ingredient). | Cited only to identify *what* a fibered class would have had to couple to; the spinor sign is a finite-group fact, not used to derive the codimension. | no (context for the corroboration, not load-bearing) |

Non-matching witnesses are not used as load-bearing proof of this persistence
claim.

### N5 — Rhetoric audit

Scope-flagged phrases are bounded to the computed object:

- **"stays non-fibered at N = 3"** / **"non-fibered class"** means precisely: the
  exchange `Z_2` is **not** in the `GF(2)`-span of the base-edge link-sign
  cochains `{w_e}` of `H^1(UD_N; Z_2)`, i.e. it has base-edge projection
  `P(t) = 0`, for N ∈ {2, 3} on every tested non-planar witness including the
  genuine `Z^3`-cube subdivision. It does **not** mean "fibered enrichment is
  impossible for all `N`" — `N >= 4` and the infinite lattice are untested
  (N1, last row).
- **"N-stable from 2 to the physical 3"** means the three measured integers
  `(dim H^1, dim fibered, codim)` and the integral torsion are computed to be
  *identical* at N = 2 and N = 3 on the same witnesses; it does **not** assert
  stability at higher `N`.
- **"does not supply the CAR sign as a fibered geometric class"** means the
  first-quantized configuration-space topology does not *spontaneously* hand over
  a base-edge-fibered fermion sign; it does **not** claim fermions are *derived*,
  nor that the cross-site CAR sign cannot arise by the *second-quantized*
  graded-locality route (N6). The boson/fermion *value* on the codim-1 class
  remains a free 1D-rep choice, explicitly unselected here.

### N6 — Partial-closure path scan

Two non-axiom partial-closure paths remain open and are **not** called new
axioms by this note:

1. **Second-quantized graded-locality / fermion-parity superselection** (the
   retained statistics-agnostic no-go's surviving axis, §7 path 2 of the FS
   no-go). A retained `Z_2`-grading that imposes graded locality could supply the
   cross-site CAR sign by a *field-algebra* mechanism — orthogonal to
   configuration-space topology, hence untouched here.
2. **Sign-selection on the codim-1 class.** Whether a *further* framework
   structure (a fermion-parity superselection rule, or the on-site `2O`
   `2π = -1` sign coupling through a graded principle rather than a fibered
   base-edge class) selects the `-1` (fermionic) value of the free 1D-rep on the
   non-fibered exchange class is the open sign question; this note shows only
   that the carrier is **not** a base-edge `sign(beta)` coupling.

Neither path is the same computation as the N = 3 first-quantized homology
settled here.

### N7 — Steelman

The strongest objection is that the **physical three-particle** sector is exactly
where genuine many-body braiding should turn on: the three-generation
configuration space could carry richer braid torsion (parastatistics) that, by
sheer many-body interaction, fibers over the base lattice and finally couples the
exchange phase to a worldline-direction `sign(beta)` — making N = 3 qualitatively
unlike the merely-pairwise N = 2 case. This steelman is the natural physical
expectation and it **fails on computation**: the integral `H_1(UD_3)` torsion on
the clean witness `K_5` is a *single* `Z_2` (no `Z_3`/`Z_4`), and the base-edge
link-sign subspace has codimension *exactly 1* in `H^1(UD_3; Z_2)` — the same two
facts as N = 2 — including on a genuine subgraph of the real `Z^3` lattice and
stably under Abrams subdivision. The many-body sector does not manufacture the
fibering; the steelman blocks only the *broader* claim that no mechanism on any
axis (e.g. second-quantized grading, N6) can ever supply the CAR sign, which this
note does not make.

### N8 — Cross-cycle echo

Prior negative/persistence overclaims in this repo characteristically failed by
testing one representative case (here: N = 2, or a single abstract graph) and
then declaring the whole many-body lane closed. This note avoids that echo three
ways: (i) it *extends* rather than extrapolates — the physical N = 3 is computed
directly, not inferred from N = 2; (ii) it tests the genuine `Z^3`-cube witness
and Abrams subdivision-stability, not only abstract `K_5`/`K_{3,3}`; and (iii) it
holds the persistence claim to the first-quantized configuration-space axis,
explicitly leaving the second-quantized graded-locality route and the
boson/fermion sign-selection open. It is consistent with — and the many-body
extension of — the N = 2 anyon-exclusion dichotomy (`Z_2` exchange, anyons
excluded) and the FS no-go (exchange decoupled from single-edge data), and it
corroborates the SO(2)-writhe-vs-spinor-`Z_2` decoupling from the
configuration-space side: the worldline-direction (writhe-type base-edge) data
and the exchange/spinor `Z_2` remain on orthogonal classes at the physical
three-particle level.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29` | retained_bounded (the N=2 result extended here) |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | retained_no_go (its §7 names this open escape) |
| `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | retained (contextual: surviving-statistics framing only) |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | retained_no_go (the open second-quantized bridge, not resolved here) |
| `binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28` | retained_bounded |

The load-bearing content `(A)`-`(C)` is self-contained exact integral linear
algebra (Smith normal form over `Z`) and `GF(2)` linear algebra, independently
recomputed in the runner; no other note's tier is relied upon for the homology
facts. The named external mathematics (Abrams 2000; Farley-Sabalka 2005; Ko-Park
2012; Harrison-Keating-Robbins-Sawicki 2014) is cited as published results, not
adopted as framework axioms.

## Non-circularity

The cube complex, boundary maps, integral torsion, and `GF(2)` cohomology /
fibered subspace are direct computations. Fermionic statistics (CAR), any
`z`-transport, and `Q = 2/3` are **never** assumed. The conclusion (single `Z_2`
torsion; codim-1 non-fibered exchange at N = 3) is computed, cross-validated
against the repo's N = 2 results, and subdivision-stable.

## Next paths this opens

- The escape that remains open is **not** at the first-quantized many-body level:
  no `N = 3` graph-braid enrichment or fibering exists. The live route is the
  **second-quantized graded-locality** bridge (the retained statistics-agnostic
  no-go) — a different axis (field-algebra grading), untouched by the
  configuration-space topology.
- Whether the **boson/fermion sign** on the codim-1 non-fibered class is selected
  by a further framework structure (a fermion-parity superselection rule, or the
  on-site `2O` `2 pi = -1` sign coupling through a graded principle rather than a
  fibered base-edge class) is the open sign question; this note shows it is
  **not** a base-edge `sign(beta)` coupling.
- Higher `N` (`N >= 4`) and the full infinite `Z^3` are expected by the same
  Ko-Park / HKRS structure to stay `Z_2` non-fibered; a larger-lattice or
  higher-`N` extension would test that directly.

This is a many-body (N = 3) positive narrowing closing the fibered-enrichment
escape for the three-generation sector; it is not a derivation of fermionic
statistics and does not settle the second-quantized graded-locality bridge.
