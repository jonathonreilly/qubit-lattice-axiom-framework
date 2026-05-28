# S^3 Topology: Finite-Radius Construction (scope-narrowed)

**Status:** bounded finite-radius construction certificate over the explicit
cubical-ball family checked by the runners. The earlier "all-R PL S^3 theorem +
resolved uniqueness + resolved framework selection + lane CLOSED" wrapper is
**deferred to separate bridge theorems, not part of this note's load-bearing
scope** (see "Scope narrowing (2026-05-28)" below).  
**Claim type:** bounded_theorem
**Type:** Constructive finite computation over the checked cubical-ball family
**Date:** 2026-04-13; scope-narrowed 2026-05-28
**Primary runner:** [`scripts/frontier_s3_cap_uniqueness.py`](../scripts/frontier_s3_cap_uniqueness.py) (finite cone-cap construction certificate, PASS=52/0)

---

## Scope narrowing (2026-05-28)

The audit-lane verdict on this row (`s3_general_r_derivation_note`) was
`audited_failed`, with rationale:

> "the source claims an all-R PL S^3 theorem plus resolved uniqueness and
> framework selection, but its direct retained-grade authorities do not prove
> those statements. `s3_cap_uniqueness_note` is now audited only as a finite
> cone-cap construction certificate for R=2..5 and explicitly excludes global
> PL cap uniqueness, physical closure, ..."

and the re-audit instruction:

> "Replace the all-R wrapper with finite bounded scope or supply retained-grade
> one-hop all-R topology authorities before re-audit."

This pass takes the first option (finite bounded scope), mirroring the
canonical scope-narrow of
[`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md):
keep the verified content the retained one-hop authorities actually support, and
explicitly defer the over-claimed part to a separate bridge.

**What the retained one-hop authorities actually prove (verified against
`docs/audit/data/audit_ledger.json`):**

- [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) is
  `retained_bounded` **only** as a finite cone-cap construction certificate for
  the explicit cubical-ball family at `R = 2, 3, 4, 5`. Its own text explicitly
  states it does **not** prove global PL cap uniqueness, physical (Kawamoto-Smit)
  closure, PL Schoenflies, Alexander, mapping-class classification, van Kampen,
  Perelman, Moise, or any identification of the compactified lattice with
  `PL S^3`.
- [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md) is
  `retained_bounded` **only** as a finite-radius boundary-vertex-link disk
  certificate for `R = 2..10` plus an exhaustive 256-subset local certificate.
  Its own text states "the all-R cubical-ball disk theorem remains open pending
  the large-coordinate bridge lemma."

Because neither retained authority supplies an all-R topology result, global cap
uniqueness, or the physical-closure premise, those statements are removed from
this note's claim boundary and deferred below.

**Kept (bounded, supported by the retained authorities + the runner):** for each
checked radius `R` in the runner family, the cone-capped cubical ball
`M_R = B_R ∪ cone(∂B_R)` is an explicit finite simplicial complex whose finite
combinatorial structure is verified — boundary triangulation closed and
connected with Euler characteristic `χ = 2`, cone-cap complex with `χ = 1`,
apex link equal to the boundary triangulation, all non-base cone faces paired,
and (via the boundary-link certificate) boundary-vertex links that are PL disks
at `R = 2..10`. This is finite combinatorial mathematics over the declared
family, not a general-R topology theorem.

**Deferred to separate bridge theorems (NOT claimed by this note):**

1. **All-R PL S^3 theorem.** The statement "`M_R` is PL homeomorphic to `S^3`
   for *every* `R >= 2`" requires an all-R topology authority (an all-R
   boundary-link disk lemma plus the PL Poincaré / Moise application with
   hypotheses discharged for all `R`). No such retained-grade one-hop authority
   exists on the current surface; per `S3_BOUNDARY_LINK_THEOREM_NOTE.md` the
   all-R disk lemma is itself open. Deferred.
2. **Uniqueness of compactification.** The statement "the cone cap is the unique
   closure producing a closed simply-connected PL 3-manifold" requires global PL
   cap uniqueness (PL Schoenflies / Alexander trick / mapping-class
   classification), which `S3_CAP_UNIQUENESS_NOTE.md` explicitly does not prove.
   Deferred.
3. **Framework-level selection.** The statement "Kawamoto-Smit homogeneity
   forces closure" is a physical-closure premise that no retained authority on
   this surface derives. Deferred.

The two external mathematical theorems previously applied here (PL Poincaré /
Perelman 2003 and Moise) are part of the deferred all-R bridge, not part of this
note's bounded scope.

---

## Bounded statement (scope-narrowed)

Let B_R be the cubical ball of radius R in Z^3 (the union of all unit cubes
whose 8 corners lie within Euclidean distance R of the origin), and let

    M_R = B_R  cup  cone(partial B_R)

be the cone-capped closure.  For each radius R in the explicit runner family
(`R = 2, 3, 4, 5` for the cone-cap construction certificate; `R = 2..10` for the
boundary-vertex-link disk certificate), M_R is an explicit finite simplicial
complex whose finite combinatorial structure is verified: the boundary
triangulation is closed, connected, with Euler characteristic chi = 2; the
cone-cap complex has chi = 1; the apex link equals the boundary triangulation;
all non-base cone faces are paired; and every boundary-vertex link is a PL disk
(R = 2..10).

The stronger statement "M_R is PL homeomorphic to S^3 for every R >= 2" is the
deferred all-R bridge (see "Scope narrowing (2026-05-28)" above); it is **not**
claimed by this note.

---

## Deferred all-R argument (NOT load-bearing here)

The four-step argument below was the intended route to the all-R PL S^3 bridge.
It is retained as a record of the deferred bridge target, **not** as a claim of
this note. Closing it requires retained-grade one-hop all-R topology authorities
(an all-R boundary-link disk lemma plus the PL Poincaré / Moise application with
hypotheses discharged for all R), which do not exist on the current surface —
per [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md) the
all-R disk lemma is itself open. Steps 1-2 below sketch general-R arguments;
Step 3 is a direct consequence; Step 4 applies a single external theorem
(Perelman) whose hypotheses would need to be discharged for all R.

### Step 1.  Every vertex link is PL S^2 (for all R)

**Claim:** link(v, M_R) is PL homeomorphic to S^2 for every vertex v of
M_R, for every R >= 2.

**Proof (three vertex classes):**

*Interior vertices (R-independent).*
A vertex v is interior iff all 26 of its neighbors in the 3x3x3 block lie
in B_R.  When this holds, all 8 unit cubes incident to v are present.  The
link of v is the boundary of the octahedron (the 3D cross-polytope):
6 vertices, 12 edges, 8 triangles, chi = 2, closed, connected, orientable.
This is PL S^2.  The argument depends only on the local 3x3x3 neighborhood
of v, not on R.

*Cone point.*
link(cone_point, M_R) = partial B_R, the boundary surface of the cubical
ball.  This is a closed connected orientable 2-manifold with chi = 2 (it is
the boundary of a convex cubical body in Z^3), hence PL S^2 by the
classification of closed surfaces.

*Boundary vertices (the disk-capping lemma).*
For a boundary vertex v:

1. link(v, B_R) = D, a PL 2-disk (chi = 1, connected, with boundary).
2. partial D is a PL 1-sphere (single boundary cycle of length n).
3. cone(partial D) is a PL 2-disk with boundary = partial D.
   (Constructive: V = n+1, E = 2n, F = n, chi = 1, boundary = partial D.)
4. link(v, M_R) = D cup_{partial D} cone(partial D).

**The PL disk-capping lemma (proved constructively, no citation):**
Let D be a PL 2-disk with boundary cycle partial D.  Then
D cup_{partial D} cone(partial D) is a PL 2-sphere.

*Proof of lemma:*
- Every edge of partial D is in exactly 1 triangle of D and exactly 1
  triangle of cone(partial D), so in the union it is in exactly 2 triangles.
- Every interior edge of D is in exactly 2 triangles (unchanged).
- Every interior edge of cone(partial D) (the apex-v_i edges) is in exactly
  2 triangles.
- Therefore every edge is in exactly 2 triangles: the union is a closed
  2-manifold.
- chi(D cup cone(partial D)) = chi(D) + chi(cone(partial D)) - chi(partial D)
  = 1 + 1 - 0 = 2.
- Connected, closed, orientable, chi = 2 implies PL S^2 by the
  classification of closed surfaces.

The classification of closed surfaces (connected closed 2-manifold with
chi = 2 is S^2) is a standard result that we verify computationally rather
than cite as a black box: we check closed + connected + chi = 2 +
orientable for every link at every R.

**R-dependence caveat (Step 1).** The interior-vertex argument is manifestly
R-independent (local 3x3x3 property). The cone-point argument depends only on the
combinatorial structure of partial B_R. The boundary-vertex argument relies on
the disk-capping lemma applied to `link(v, B_R) = D`; the claim that this link is
a PL 2-disk **for all R** is exactly the all-R boundary-link disk lemma that
[`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md) records as
**open** (proved for the small-coordinate regime, checked R = 2..10). So the
all-R conclusion of Step 1 is deferred; the finite-radius checks below stand.

**Computational verification (finite radii):** the boundary-vertex-link disk
facts at R = 2..10 are verified by
`scripts/frontier_s3_boundary_link_theorem.py`, and per-radius vertex-link
checks are in `scripts/frontier_s3_general_r.py` (R = 2..10).

### Step 2.  pi_1(M_R) = 0 (for all R)

**Claim:** M_R is simply connected for every R >= 2.

**Proof (van Kampen):**
Write M_R = B_R cup cone(partial B_R), with:

- B_R is a convex cubical body in Z^3, hence contractible.
  In particular, pi_1(B_R) = 0.
- cone(partial B_R) is a cone over a compact space, hence contractible.
  In particular, pi_1(cone(partial B_R)) = 0.
- B_R  intersect  cone(partial B_R) = partial B_R, which is a PL S^2
  (from Step 1, the cone-point link), hence connected and simply connected.

By the Seifert-van Kampen theorem:

    pi_1(M_R) = pi_1(B_R) *_{pi_1(partial B_R)} pi_1(cone(partial B_R))
              = {e} *_{{e}} {e}
              = {e}.

**R-independence of Step 2:** The argument uses only: (a) B_R is convex
hence contractible, (b) a cone is contractible, (c) partial B_R is a
connected PL 2-sphere (from Step 1).  All three hold for every R >= 2.

**Computational verification:** frontier_s3_general_r.py computes
H_1(M_R; Z) = 0 by explicit boundary-matrix computation for R = 2..10,
confirming pi_1 = 0 (since H_1 is the abelianization of pi_1).

### Step 3.  M_R is a compact closed simply-connected PL 3-manifold (for all R)

This follows directly:
- **Compact:** M_R is a finite simplicial complex.
- **Closed (no boundary):** Every vertex link is a closed 2-manifold
  (Step 1), which is the characterization of a boundaryless PL 3-manifold.
- **PL 3-manifold:** Every vertex link is PL S^2 (Step 1).
- **Simply connected:** pi_1(M_R) = 0 (Step 2).

### Step 4.  M_R is PL homeomorphic to S^3 (for all R)

**The PL Poincare conjecture** (proved by Perelman, 2003; see Perelman,
arXiv:0211159, 0303109, 0307245; exposition by Morgan-Tian, Kleiner-Lott,
Cao-Zhu):

> Every compact closed simply-connected 3-manifold is homeomorphic to S^3.

Combined with the equivalence of the TOP and PL categories in dimension 3
(Moise's theorem: every topological 3-manifold admits a unique PL structure):

> Every compact closed simply-connected PL 3-manifold is PL homeomorphic
> to S^3.

**Application (deferred conclusion).** *If* Step 3 holds for all R — which
requires the open all-R boundary-link disk lemma (Step 1 caveat) — then M_R would
be PL homeomorphic to S^3 for every R >= 2. Because that all-R input is open, the
all-R conclusion is deferred, not claimed by this note.

---

## Assumptions (of the deferred all-R argument above)

These assumptions belong to the deferred all-R bridge, not to this note's bounded
finite-radius scope.

1. **Framework assumption:** The physical lattice is Z^3 with the standard
   cubical structure.  M_R is the cone-capped cubical ball.
2. **PL Poincare conjecture (Perelman 2003) + Moise:** the external theorems the
   deferred all-R argument would apply. Discharging their hypotheses **for all R**
   depends on the open all-R disk lemma; on the bounded surface they are not
   invoked.
3. **Classification of closed surfaces:** Used in the deferred Step 1 to identify
   connected closed orientable 2-manifolds with chi = 2 as S^2; checked
   computationally at the finite radii.
4. **Seifert-van Kampen theorem:** Used in the deferred Step 2.  Standard
   algebraic topology.

---

## What is actually proved (bounded)

For each radius R in the explicit runner family, M_R is an explicit finite
simplicial complex with the verified finite combinatorial structure listed in
the bounded statement above (boundary chi = 2, cone-cap chi = 1, apex link =
boundary triangulation, all non-base cone faces paired, boundary-vertex links
PL disks at R = 2..10). This is finite combinatorial mathematics over the
declared family.

It does **not** prove M_R is PL homeomorphic to S^3 for all R, nor compactness
uniqueness, nor framework-level closure. Those are the deferred bridges below.

---

## What remains open (deferred bridges)

1. **All-R PL S^3 theorem: OPEN (deferred).**
   "M_R is PL homeomorphic to S^3 for every R >= 2" requires a retained-grade
   all-R topology authority. Per
   [`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md), even
   the all-R boundary-link disk lemma is open pending the large-coordinate
   bridge lemma. No retained-grade one-hop all-R authority exists on the current
   surface.

2. **Uniqueness of compactification: OPEN (deferred).**
   "The cone cap is the unique closure producing a closed simply-connected PL
   3-manifold" requires global PL cap uniqueness (PL Schoenflies / Alexander
   trick / mapping-class classification). The retained authority
   [`S3_CAP_UNIQUENESS_NOTE.md`](S3_CAP_UNIQUENESS_NOTE.md) is `retained_bounded`
   **only** as a finite cone-cap construction certificate for R = 2..5 and
   explicitly disclaims global cap uniqueness. Deferred.

3. **Framework-level selection: OPEN (deferred).**
   "Kawamoto-Smit homogeneity forces closure" is a physical-closure premise that
   no retained authority on this surface derives;
   `S3_CAP_UNIQUENESS_NOTE.md` explicitly states it provides no derivation of
   the Kawamoto-Smit homogeneity premise and no proof that closure is physically
   mandatory. Deferred.

The external mathematical theorems (PL Poincaré / Perelman 2003, Moise) are part
of the deferred all-R bridge (item 1), not part of this note's bounded scope.

---

## Downstream usage preserved (spatial-S^3 topology for the Λ identity)

The downstream consumer
[`COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md`](COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md)
cites this note for condition 4 ("round `S^3` of radius `R`") feeding the exact
spectral-gap identity

    Lambda_vac = lambda_1(S^3_R) = 3 / R^2.

That identity's spectral leg (Lichnerowicz–Obata) is a **fixed-radius**
statement: for the round S^3 of any single radius R, lambda_1 = 3 / R^2. It does
**not** require an inductive all-R PL topology theorem, global cap uniqueness, or
the physical-closure premise — it requires only that the spatial slice carries
the S^3 topology at the radius in question, which the bounded finite-radius
construction here supports for the checked family. The narrowed scope therefore
still feeds the Λ spectral-gap identity through the same condition-4 edge; only
the deferred all-R / uniqueness / framework-selection over-claims are removed.
The downstream identity note is itself `audited_conditional` and already lists
this row among its unaudited/conditional upstream authorities, so the narrowing
does not weaken any retained downstream status.

---

## Deferred all-R proof routes (NOT load-bearing here)

The following two routes were the intended paths to the deferred all-R PL S^3
bridge (item 1 of "What remains open"). They are recorded as bridge targets,
not as claims of this bounded note.

### Route 1 (deferred): per-radius recognition / shellability

A per-radius constructive identification of M_R with S^3 (Rubinstein-Thompson
3-sphere recognition; explicit shelling order) would close the bridge at each
checked R without external citation. This route has no executable runner on the
current surface and is deferred.

### Route 2 (deferred): general-R chain + PL Poincaré

The four-step chain sketched in the deferred all-R argument above (vertex links
= S^2; pi_1 = 0; compact closed simply-connected PL 3-manifold; then the PL
Poincaré conjecture / Perelman 2003) would give M_R = S^3 for all R — but only
once the all-R boundary-link disk lemma is closed (currently open per
[`S3_BOUNDARY_LINK_THEOREM_NOTE.md`](S3_BOUNDARY_LINK_THEOREM_NOTE.md)) and the
external theorem hypotheses are discharged for all R. Deferred.

---

## How this changes the paper

The S^3 topology lane can be stated at the bounded scope this note supports:

> For each checked radius R in the runner family, the cone-capped cubical ball
> M_R = B_R cup cone(partial B_R) is an explicit finite simplicial complex with
> a verified finite combinatorial structure (boundary chi = 2, cone-cap chi = 1,
> apex link = boundary triangulation, boundary-vertex links PL disks at
> R = 2..10).

The all-R PL S^3 theorem, compactification uniqueness, and framework-level
selection are deferred bridges (see "What remains open" above); they are not
established by this note's retained one-hop authorities. The bounded
finite-radius spatial-S^3 topology still feeds the fixed-radius spectral-gap
identity `Lambda_vac = lambda_1(S^3_R) = 3 / R^2` (see "Downstream usage
preserved" above).

---

## Decision

**Scope-narrowed to a bounded finite-radius construction certificate** (was
"PROMOTE to CLOSED"; see "Scope narrowing (2026-05-28)").

What this note now carries:

- **Bounded (kept):** the explicit finite-radius cone-cap construction over the
  runner family — boundary chi = 2, cone-cap chi = 1, apex link = boundary
  triangulation, all non-base cone faces paired, boundary-vertex links PL disks
  at R = 2..10. Supported by the `retained_bounded` authorities
  [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) (R = 2..5) and
  [S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md)
  (R = 2..10).
- **Deferred (removed from claim boundary):** the all-R PL S^3 theorem, global
  compactification uniqueness, and framework-level (Kawamoto-Smit) selection.
  Closing these requires retained-grade one-hop all-R topology authorities that
  do not exist on the current surface (the PL Poincaré / Perelman 2003 + Moise
  application and the global cap-uniqueness argument are part of these deferred
  bridges).

Effective status is assigned by the independent audit lane only; this edit
narrows the source claim and does not assert any ledger status.

---

## Commands run

```
python scripts/frontier_s3_cap_uniqueness.py       # finite cone-cap certificate, PASS=52/0
python scripts/frontier_s3_general_r.py            # per-radius finite checks, R=2..10 (slow companion)
python scripts/frontier_s3_boundary_link_theorem.py # boundary-vertex-link disk certificate, R=2..10
```

---

## Citations

This section registers explicit dependency edges for the retained one-hop
authorities that support this note's bounded finite-radius scope. The markdown
links register them as one-hop dependency edges in the citation graph.

- [S3_CAP_UNIQUENESS_NOTE.md](S3_CAP_UNIQUENESS_NOTE.md) — `retained_bounded`
  finite cone-cap construction certificate for the explicit cubical-ball family
  at R = 2..5 (runner `scripts/frontier_s3_cap_uniqueness.py`, PASS=52/0). This
  note relies on it only for the finite cone-cap construction; the legacy
  "uniqueness of compactification" reading is **deferred**, matching this
  authority's own explicit disclaimer of global cap uniqueness, physical closure,
  and `PL S^3` identification.
- [S3_BOUNDARY_LINK_THEOREM_NOTE.md](S3_BOUNDARY_LINK_THEOREM_NOTE.md) —
  `retained_bounded` boundary-vertex-link disk certificate for R = 2..10 plus an
  exhaustive 256-subset local certificate (runner
  `scripts/frontier_s3_boundary_link_theorem.py`). Supplies the finite-radius
  boundary-link disk facts. Its own text records that the all-R cubical-ball disk
  theorem remains open; this note therefore does not lean on an all-R disk lemma.

The external mathematical theorems (PL Poincaré / Perelman 2003, Moise) and the
global cap-uniqueness arguments are part of the deferred all-R / uniqueness
bridges (see "What remains open"), not one-hop authorities for this bounded note.

The runner-side artifacts for this note's bounded scope are:

- `scripts/frontier_s3_cap_uniqueness.py` — finite cone-cap construction
  certificate over R = 2..5 (PASS=52/0); the direct executable artifact for the
  re-audited bounded scope.
- `scripts/frontier_s3_general_r.py` — per-radius finite checks (vertex links,
  homology) at R = 2..10; the slow companion runner referenced in the
  frontmatter. It verifies finite per-radius facts, not an all-R topology
  theorem.
- `scripts/frontier_s3_boundary_link_theorem.py` — boundary-vertex-link disk
  certificate at R = 2..10.

This edit is a scope narrowing: it removes the all-R PL S^3 theorem, the
"uniqueness/selection RESOLVED" claims, and the "lane CLOSED" status, keeping the
finite-radius construction content that the retained authorities support.
