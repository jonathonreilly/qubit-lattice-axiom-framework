# The N=3 Graph-Braid Exchange Class Stays Non-Fibered on Finite Lattice Witnesses

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Review provenance:** source theorem candidate; post-landing audit decides the
ledger grade. This note adds no axiom and no import; it answers a finite
many-body witness sub-question negatively (no base-edge fibered enrichment at
N=3 on the tested graph-braid witnesses).
**Primary runner:** `scripts/frontier_graph_braid_n3_fermion_sign_nonfibered.py` (SCORECARD PASS=26)
**Cached runner output:** [`logs/runner-cache/frontier_graph_braid_n3_fermion_sign_nonfibered.txt`](../logs/runner-cache/frontier_graph_braid_n3_fermion_sign_nonfibered.txt)
(`SCORECARD: PASS=26 FAIL=0`; dependency-free finite graph helper)

## Context (the open sub-question / the attacked assumption)

The N=2 graph-braid result
`GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29`
computes the finite-witness `UD_2` exchange class, the `Z_2` being the two-token
exchange (Y-)class, and the cross-site no-go
`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28`
records that this exchange `Z_2` is **decoupled from** single-edge data: it is a
**non-fibered** class -- not a base-edge "link-sign" class that would couple to a
base-edge `sign(beta)`. That note's §7 names the **open** lattice-native escape:
build the graph-braid `pi_1` of `UD_N` and check whether a fibered exchange-loop
structure couples the sign to the lattice. The session question is the sharp
finite N=3 form:

> Do the tested **N=3** graph-braid witnesses have a **fibered** exchange sign
> (richer exchange torsion, or an exchange class that is a base-edge class
> coupling to `sign(beta)`) unlike N=2?

This note answers **no**, by direct generalization of the repo's `UD_2`
construction to `UD_3` and an explicit fibered/non-fibered cohomology test.

## Claim

At the **N = 3 finite-witness** level, the graph-braid first homology and
mod-2 cohomology tests show the same exchange-class obstruction as N = 2:

> **(i) Torsion stays a single `Z_2`.** Integral `H_1(UD_3)` on the small
> non-planar witness `K_5` is `Z^6 (+) Z_2` — the **same order-2** exchange class
> as N = 2, with **no `Z_3` / `Z_4`** enrichment. So
> `Hom(Z_2, U(1))` on the exchange torsion stays `{+1, -1}`: the exchange
> torsion gives only the boson/fermion sign choices, with no torsion-based
> anyon or parastatistics enrichment at N = 3. Free `H_1` summands are not being
> identified with the exchange sign here.
>
> **(ii) The exchange `Z_2` is still NON-FIBERED.** Over `GF(2)`, the base-edge
> "link-sign" cochains `{w_e}` (whose `GF(2)` combinations are the most general
> `sign(beta)` class) span a subspace of `H^1(UD_N; Z_2)` of codimension
> **exactly 1**, at **both N = 2 and N = 3**, and that 1-dimensional complement
> **is** the exchange class. The fermion sign therefore does **not** couple to
> any base-edge `sign(beta)` on the tested witnesses -- it is a non-fibered class
> at N = 3 exactly as for two tokens.

**Classification: positive narrowing.** Going to the tested N = 3 many-body
witnesses does **not** make the exchange class fibered, and does not enrich the
exchange torsion beyond `Z_2`. It is **not** a derivation of fermionic statistics
(the boson/fermion *sign* on the codim-1 class is still a free 1D-rep choice);
it closes the finite N=3 version of the graph-braid fibered-enrichment escape.

### The computation (runner, all 26 checks pass)

The runner generalizes the repo's `UD_2` Abrams cube complex (0-cells = disjoint
vertex pairs; 1-cells = vertex + non-incident edge; 2-cells = vertex-disjoint
edge pairs) to **arbitrary N**: an unordered cell is a closure-disjoint set of
`N` atoms (vertices/edges), `dim` = number of edge atoms, with the cubical
boundary carrying the Koszul sign from the edge-atom ordering. It then:

- **(A) Integral `H_1` via Smith normal form.** Re-verifies the repo N = 2 facts
  (`C_5, K_4` torsion-free; `K_5 = Z^6 (+) Z_2`; `K_{3,3} = Z^4 (+) Z_2`) for
  cross-validation, then computes N = 3: `K_5 -> Z^6 (+) Z_2` (single exchange
  `Z_2`, all torsion order 2). `Hom(Z_2, U(1)) = {+1, -1}` on that torsion class.
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

Current cache certificate:

```text
SCORECARD: PASS=26 FAIL=0
```

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

**Gate result:** PASS for the narrow N = 3 graph-braid persistence claim only. The
proposition being recorded is *not* a repo-wide impossibility of fermion-sign
emergence and *not* a claim that the graph-braid program is dead. It is the
computed statement that, on the tested finite N = 3 graph-braid witnesses, the
configuration-space exchange `Z_2` stays order-2 with base-edge
(worldline-direction) projection `P(t) = 0` -- non-fibered, the same as N = 2 --
so this first-quantized graph-braid route does **not** spontaneously supply the
CAR sign as a fibered geometric class. "Non-fibered" is the precise
codim-1-of-`H^1(UD_N; Z_2)` statement of the
"### What 'fibered' means here" section: the exchange class is **not** in the
`GF(2)`-span of the base-edge link-sign cochains `{w_e}`.

### N1 — Alternative route enumeration

The five routes by which the N = 3 witness sector could have *escaped* this
persistence claim (i.e. by which going from two tokens to three tokens could have
made the exchange sign richer than `Z_2`, or fibered over a base-lattice edge so
that it couples to a worldline-direction `sign(beta)`). Each route is evaluated
by the runner or by the same finite chain-complex boundary maps; none survives
inside this scoped claim.

| route | what it would attempt | why it fails for this scoped claim | marker |
|---|---|---|---|
| Richer exchange torsion | At N = 3 obtain `Z_3`/`Z_4` (or higher) torsion in the exchange sector of `H_1(UD_3)`, giving a torsion-based exchange phase beyond `{+1,-1}`. | Smith normal form on the clean integral witness `K_5` returns `H_1(UD_3) = Z^6 (+) Z_2`: the exchange torsion is order 2, with no `Z_3`/`Z_4` torsion enrichment. Free `Z` summands are not the exchange torsion class. | ATTEMPTED (runner Part A) |
| Fibered exchange class | At N = 3 the exchange class falls into the `GF(2)`-span of base-edge link-sign cochains `{w_e}`, so its holonomy becomes a product of base-edge `sign(beta)` link signs (a base-graph pullback). | The fibered subspace `span{[w_e]}` has codimension **exactly 1** in `H^1(UD_N; Z_2)` at N = 3 (and N = 2), and the 1-dim complement is the exchange class -- `P(t) = 0` on every base edge. | ATTEMPTED (runner Part B) |
| Coboundary rescue | The exchange class is not visibly base-edge at the cochain level, but becomes base-edge after adding a coboundary / gauge redefinition in `H^1`. | The runner computes the fibered span **in cohomology**, reducing by `im D1`; the codim-1 complement remains after quotienting by coboundaries. | ATTEMPTED (runner Part B) |
| Coarse-graph artifact | The codim-1 complement is an artifact of an under-subdivided witness graph and dissolves once the graph is subdivided to satisfy Abrams' length condition. | Subdividing `K_{3,3}` (`k = 1 -> k = 2`, sufficient for N = 3) leaves `(dim H^1, dim fibered, codim)` unchanged: the structure is topological, not combinatorial coarseness. | ATTEMPTED (runner Part C) |
| Witness-not-lattice | The non-fibered codim-1 holds for abstract Kuratowski graphs `K_5`/`K_{3,3}` but *not* for the framework's actual `Z^3` site graph. | The fibered test returns codim 1 on the genuine `K_{3,3}` subdivision *extracted from the real `Z^3` cube* `L = 3` (`V = 14, E = 17`, a subgraph of the lattice), not only on abstract `K_5`/`K_{3,3}`. | ATTEMPTED (runner Part B, `Z^3`-cube witness) |

The higher-N / infinite-lattice continuation is deliberately not in this wall
set: `N >= 4` and the infinite lattice are untested next paths, not closed
consequences of this note.

### N2 — Wall-independence audit

The collapsed wall set for this persistence claim has a single load-bearing
wall: *the exchange `Z_2` lies in the codim-1 complement of the base-edge
link-sign subspace of `H^1(UD_N; Z_2)`* (equivalently `P(t) = 0` on every base
edge). The two refuted alternative-route walls are not independent walls — the
"richer-torsion" route is foreclosed by the integral `H_1` computation and the
"fibered-exchange" route by the `GF(2)` codimension computation, but both reduce
to the same Abrams cube-complex boundary maps `(d1, d2)` on the same witness; no
*second*, separately imported obstruction is invoked. Crucially, this wall is
**independent of the boson/fermion sign-selection wall**: choosing the `-1`
(fermionic) value of the free 1D-rep on the codim-1 class is a *different*
question that this note does not touch (see N5). Closing a future *second-quantized*
graded-locality route would not move this first-quantized homology wall at all;
it lives on a different axis (field-algebra grading, not configuration-space
topology).

### N3 — Hidden-wall scan

The load-bearing inputs are explicit and finite; "fibered", "non-fibered",
"three-token sector", and "CAR" are *not* used as hidden inputs for the result:

- the `Z^3` site-graph shape (used only through an explicit finite unit-edge
  `K_{3,3}` subdivision witness in the `L=3` cube; `K_5`/`K_{3,3}` are the
  abstract cross-checks);
- the Abrams discretized unordered-`N`-particle cube complex `UD_N(Γ)`
  (0-cells = closure-disjoint vertex `N`-sets; 1-cells = vertex + non-incident
  edge; 2-cells = vertex-disjoint edge pairs) with the **Koszul-signed** cubical
  boundary from edge-atom ordering;
- exact integer Smith normal form over `ℤ` (integral `H_1` torsion);
- `GF(2)` linear algebra: cocycles `Z^1 = ker D2^T`, coboundaries `B^1 = im D1`,
  and the base-edge link-sign cochains `{w_e}` reduced mod `B^1`.

No audit grade of any other note is consumed for the homology facts. Any
generation reading of `N = 3` is interpretive framing, not a load-bearing
premise: the computation is performed for unordered `N = 3` tokens regardless of
that reading. The per-site dim-2 row `cl3_per_site_hilbert_dim_two` enters
**contextually only**, for the surviving-statistics narrative, and is not used to
derive the codimension.

### N4 — Residual matching

| cited witness | residual attacked | residual here | match? |
|---|---|---|---|
| `FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28` §7 path 1 (lattice-native graph-braid `pi_1`, the graph-braid fibered-enrichment escape) | Whether a lattice-native `UD_N` graph-braid structure manufactures a `Z_2` exchange that **couples to** the on-site `2O` `2pi = -1` sign via a base-edge (fibered) `sign(beta)`. | The N = 3 finite-witness instance of exactly that residual: the exchange `Z_2` is computed to be non-fibered (codim-1, `P(t) = 0`), so it does **not** couple to a base-edge `sign(beta)`. | yes (the tested N = 3 case of the open §7-path-1 escape) |
| `GRAPH_BRAID_Z3_ANYON_EXCLUSION_DICHOTOMY_NARROW_THEOREM_NOTE_2026-05-29` | The N = 2 witness facts `H_1(UD_2) = Z^{beta_1} (+) Z_2` (torsion exchange `Z_2`, no richer torsion exchange). | The same construction extended to N = 3, re-deriving the N = 2 facts (`K_5 -> Z^6 (+) Z_2`, etc.) as cross-validation before the N = 3 computation. | yes (positive input, recomputed) |
| `STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25` | The open **second-quantized** field-algebra-grading bridge that would supply the cross-site CAR sign. | NOT attacked here; the second-quantized graded-locality axis is a *different* route (§7 path 2), left open. | no (orthogonal open route, not this note's residual) |
| `BINARY_OCTAHEDRAL_DISCRETE_SPINOR_SIGN_NARROW_THEOREM_NOTE_2026-05-28` | The on-site `2O` spinor `2pi = -1` sign (the spinor-`Z_2` ingredient). | Cited only to identify *what* a fibered class would have had to couple to; the spinor sign is a finite-group fact, not used to derive the codimension. | no (context for the corroboration, not load-bearing) |

Non-matching witnesses are not used as load-bearing proof of this persistence
claim.

### N5 — Rhetoric audit

Scope-flagged phrases are bounded to the computed object:

- **"stays non-fibered at N = 3"** / **"non-fibered class"** means precisely: the
  exchange `Z_2` is **not** in the `GF(2)`-span of the base-edge link-sign
  cochains `{w_e}` of `H^1(UD_N; Z_2)`, i.e. it has base-edge projection
  `P(t) = 0`, for N in {2, 3} on every tested non-planar witness including the
  genuine `Z^3`-cube subdivision. It does **not** mean "fibered enrichment is
  impossible for all `N`" — `N >= 4` and the infinite lattice are untested
  (N1).
- **"N-stable from 2 to 3"** means the three measured integers
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
   statistics-agnostic no-go's surviving axis, §7 path 2 of the FS no-go). A
   `Z_2`-grading that imposes graded locality could supply the cross-site CAR
   sign by a *field-algebra* mechanism — orthogonal to
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

The strongest objection is that the **three-particle** sector is exactly where
genuine many-body braiding should turn on: the N = 3 configuration space could
carry richer braid torsion (parastatistics) that, by
sheer many-body interaction, fibers over the base lattice and finally couples the
exchange phase to a worldline-direction `sign(beta)` — making N = 3 qualitatively
unlike the merely-pairwise N = 2 case. This steelman is the natural physical
expectation and it **fails on computation**: the integral `H_1(UD_3)` torsion on
the clean witness `K_5` is a *single* `Z_2` (no `Z_3`/`Z_4` exchange-torsion
enrichment), and the base-edge link-sign subspace has codimension *exactly 1* in `H^1(UD_3; Z_2)` — the same two
facts as N = 2 — including on a genuine subgraph of the real `Z^3` lattice and
stably under Abrams subdivision. The many-body sector does not manufacture the
fibering; the steelman blocks only the *broader* claim that no mechanism on any
axis (e.g. second-quantized grading, N6) can ever supply the CAR sign, which this
note does not make.

### N8 — Cross-cycle echo

Prior negative/persistence overclaims in this repo characteristically failed by
testing one representative case (here: N = 2, or a single abstract graph) and
then declaring the whole many-body lane closed. This note avoids that echo three
ways: (i) it *extends* rather than extrapolates — N = 3 is computed
directly, not inferred from N = 2; (ii) it tests the genuine `Z^3`-cube witness
and Abrams subdivision-stability, not only abstract `K_5`/`K_{3,3}`; and (iii) it
holds the persistence claim to the first-quantized configuration-space axis,
explicitly leaving the second-quantized graded-locality route and the
boson/fermion sign-selection open. It is consistent with — and the many-body
extension of — the N = 2 graph-braid dichotomy (`Z_2` exchange torsion, no richer
exchange torsion) and the FS no-go (exchange decoupled from single-edge data), and it
corroborates the SO(2)-writhe-vs-spinor-`Z_2` decoupling from the
configuration-space side: the worldline-direction (writhe-type base-edge) data
and the exchange/spinor `Z_2` remain on orthogonal classes at the tested
three-particle level.

## Upstream Rows Consulted

| claim_id | use in this note |
|---|---|
| `graph_braid_z3_anyon_exclusion_dichotomy_narrow_theorem_note_2026-05-29` | N=2 construction extended and recomputed here |
| `fs_rotation_exchange_discrete_insufficiency_narrow_no_go_note_2026-05-28` | names the graph-braid fibered-enrichment escape |
| `cl3_per_site_hilbert_dim_two_theorem_note_2026-05-02` | contextual surviving-statistics framing only |
| `staggered_dirac_substep1_statistics_agnostic_no_forcing_note_2026-05-25` | open second-quantized bridge, not resolved here |
| `binary_octahedral_discrete_spinor_sign_narrow_theorem_note_2026-05-28` | contextual spinor-sign target only |

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
  no tested `N = 3` graph-braid exchange-torsion enrichment or base-edge fibering
  exists. The live route is the **second-quantized graded-locality** bridge — a
  different axis (field-algebra grading), untouched by the configuration-space
  topology.
- Whether the **boson/fermion sign** on the codim-1 non-fibered class is selected
  by a further framework structure (a fermion-parity superselection rule, or the
  on-site `2O` `2 pi = -1` sign coupling through a graded principle rather than a
  fibered base-edge class) is the open sign question; this note shows it is
  **not** a base-edge `sign(beta)` coupling.
- Higher `N` (`N >= 4`) and larger finite-to-infinite lattice continuations
  remain next tests; this note does not infer them from the N = 3 witnesses.

This is a many-body (N = 3) positive narrowing closing the fibered-enrichment
escape for the tested three-token sector; it is not a derivation of fermionic
statistics and does not settle the second-quantized graded-locality bridge.
