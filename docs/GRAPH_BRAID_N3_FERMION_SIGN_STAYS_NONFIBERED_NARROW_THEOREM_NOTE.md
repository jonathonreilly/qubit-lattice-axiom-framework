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

## No-Go Discipline Gate

This note ships a positive narrowing plus a negative answer to the
fibered-enrichment escape; the discipline check is recorded.

- **N1 alternative routes the escape could take:** (1) richer torsion at N = 3
  (`Z_3` / `Z_4` -> anyon/parastatistics) — refuted: torsion stays `Z_2`;
  (2) the exchange class becoming a base-edge link-sign (fibered) class at N = 3 —
  refuted: codim-1 non-fibered complement at N = 3 too; (3) a coarse-graph
  artifact — refuted by subdivision stability; (4) a feature of `K_5`/`K_{3,3}`
  not of `Z^3` — refuted on the genuine `Z^3`-cube `K_{3,3}` witness.
- **N2 wall independence:** the *exchange-sign-is-non-fibered* fact and the
  *boson-vs-fermion sign selection* are distinct. This note settles the former at
  N = 3; it does not select the sign.
- **N3 hidden-wall scan:** the only framework input is the `Z^3` site graph shape
  (and, for the surviving-statistics framing, the retained per-site dim-2 result,
  cited only contextually). Everything else is exact integral / `GF(2)` linear
  algebra and `networkx` graph algorithms.
- **N4 residual matching:** the FS no-go §7 asked whether a lattice-native
  `UD_N` graph-braid structure makes the exchange sign fibered/coupled. This note
  attacks the **N = 3** instance of that residual and shows the exchange stays a
  non-fibered codim-1 `Z_2`.
- **N5 rhetoric audit:** "stays non-fibered at N = 3" means "the exchange `Z_2`
  is not in the `GF(2)`-span of base-edge link-sign cochains for N in {2, 3} on
  the tested non-planar graphs including the `Z^3` witness." It does **not** claim
  fermions are derived, nor that every `N` or every second-quantized lift has been
  settled.
- **N6 partial-closure scan:** a graded-locality / fermion-parity-superselection
  principle, or a second-quantized field-theoretic bridge, could still supply the
  cross-site CAR sign by a different route; this note does not foreclose those.
- **N7 steelman:** a reviewer may expect the three-generation many-body sector to
  carry richer braid torsion (parastatistics) that fibers over the lattice. The
  steelman fails: the integral `H_1(UD_3)` torsion is computed to be a single
  `Z_2`, and the fibered subspace's codimension is computed to be exactly 1 — the
  same as N = 2 — including on a genuine subgraph of `Z^3`.
- **N8 cross-cycle echo:** consistent with the N = 2 dichotomy note (anyons
  excluded, `Z_2` exchange) and the FS no-go (exchange decoupled from single-edge
  data). This is the many-body (N = 3) extension confirming no fibered enrichment.

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
