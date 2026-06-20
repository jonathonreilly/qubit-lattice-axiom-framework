# Block05 Section — Ray P-ABJ χ≠0 (A_min-native curvature)

**Edge:** P-ABJ / P1 of keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
(fanout 1105). The internal-route open ray re-targeted by retained
`ABJ_RESIDUAL_GW_NOT_NECESSARY` and listed STILL OPEN in the grounding map
(`routes_still_to_attempt[3]`): "exhibit a framework-internal `χ≠0` / `Q≠0`
background on which the taste-singlet index is nonzero."

**Ray:** Does ANY A_min-NATIVE mechanism give `χ≠0` (or `Q≠0`) **without** admitting
external curved geometry? Block02 PR-D proved the taste-singlet Kähler–Dirac index
tracks `χ` (+2 on a curved closed S²), but every A_min-native closed complex it tested
is a flat cubical **product** torus with `χ=0` → the wall was re-localized onto the
flat-cubic Lattice axiom. This ray attacks the three fronts the prior runners did NOT
build: (A) the Z_τ-extended complex / nontrivial cycles; (B) realized-state **induced
holonomy**; (C) lattice **defects / disclinations** reachable from the cubic adjacency.

**Runner:** `scripts/frontier_abj_chi_native_curvature_routes_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_chi_native_curvature_routes_2026_06_20.txt`
**Result: TOTAL: PASS=23 FAIL=0.**

**Posture:** honest frontier work (`trace_class = negative_route_pruning`). Outcome is
a **sharper no-go** — no A_min-native `χ≠0` crack — plus a precise **registered-data**
classification of the induced-holonomy curvature. No crack is sold as closure.

## Scope and absorbed authority (cited by path + PASS; recomputed/contrasted in-tree)

A_min = Lattice (cubic `Z³` nearest-neighbor adjacency) + Quantum + Record, plus the
four approved primitives: `kinetic_isotropy_primitive` (emergent time edge on the SAME
footing as the spatial cubic edge ⇒ a cubical `Z³×Z_τ` complex), `scale_reference_primitive`
(units only), `realized_state_primitive` (pointwise evaluation at the supplied
law-admissible realized state), `minimal_axioms`. None supplies a gauge field, a boundary,
a non-cubic cell, a curved geometry, or a topological-sector selector.

Absorbed (NOT rebuilt) — cited by path + PASS, recomputed/contrasted in-tree:
- `scripts/frontier_abj_pabj_kd_index_chi_tracking_2026_06_20.py` — **PASS=45**
  (KD index = χ; +2 on S²; product cubical tori all χ=0). The anchor this ray extends.
- `scripts/frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.py` — **PASS=34**
  (square-block ε-index = 0; `Q=0` on closed single-valued links; injected twist needed
  for `Q≠0`). The R-C honesty discipline this ray preserves.
- `scripts/frontier_induced_holonomy_matter_state_functional_derived_curvature_2026_06_10.py`
  — **PASS=12** (the curvature scalar `C = 1 − |tr Hol|/3`; sea/sea-orbit flat `C=0`,
  off-sea `C>0`). Recomputed in-tree in Part B.
- `scripts/anomaly_abj_obstruction_unified_2026_06_20.py` (PART D KD=χ cubical control).

**Method (in-tree, citation-free verdict).** A CW complex with integer boundary maps;
combinatorial Hodge Laplacian `L_k = ∂ₖᵀ∂ₖ + ∂_{k+1}∂_{k+1}ᵀ`; Betti `b_k = dim ker L_k`;
the graded Kähler–Dirac kernel index of `D_KD = d + d†` with grading `Γ = (−1)^k` equals
`Σ_k (−1)^k b_k = Σ_k (−1)^k f_k = χ` (Hodge). This is the **taste-singlet** (Dirac–Kähler)
object — recomputed here in-tree, exactly as in PR-D; the load-bearing verdict rests on
the in-tree recomputation, not the Catterall–Butt citation. `χ=+2` on S² is rebuilt as the
live non-vacuity anchor (A0).

## What this ray found — three prongs

### PRONG A — Z_τ / nontrivial cycles: a twisted time-gluing CANNOT move χ (A1–A3, S1)

The kinetic-isotropy emergent time circle gives a product `Z³×Z_τ` (a product of circles),
`χ(S¹)^n = 0`. PR-D's control only did **product** cubical tori. This ray adds the
**non-product** family reachable from the cubic adjacency by re-identifying boundary
edges — a **twisted time-gluing** (Klein bottle: the `y`-flip on wrapping `x`) — and
asks whether a twist creates `χ`.

- **A2:** Klein bottles on `3×4`, `4×4`, `4×6` square blocks: `χ=0`, KD index `=0`.
  A genuinely non-product closed surface, yet `χ` is **unmoved**.
- **A3 (sharper no-go):** the torus and the Klein bottle on the **same** `4×4` square
  block have **identical f-vectors** `[16,32,16]` ⇒ **identical χ=0**. Because
  `χ = Σ(−1)^k f_k` is a **cell count**, gluing/twisting the Z_τ circle changes
  orientability/homology but **never** the Euler characteristic. Nontrivial cycles do
  not generate `χ`.

**Residual surfaced and fixed mid-cycle (A1a — load-bearing-residuals discipline).** The
runner FAILED my first `χ=0` torus checks at edge length 2: an *embedded* cubical torus is
faithful only when **every edge length ≥ 3** — at length 2 the two parallel plaquette edges
in that direction coincide (`f=[4,4,4]`, `χ=4` is a degenerate artifact, not a torus). The
faithful family is `L≥3`; the PR-D algebraic cubical-set convention keeps `L=2` distinct and
gives `χ=0` either way. Documented as an explicit check (A1a), not hidden.

### PRONG B — induced holonomy: state-dependent LOCAL curvature; REGISTERED DATA (B1–B4, S2)

Per `INDUCED_HOLONOMY_..._2026-06-10.md`, the derived SU(3) curvature scalar
`C = 1 − |tr Hol|/3` is flat (`C=0`) on the closed-shell sea and its orbit, but
state-dependently NON-flat (`C>0`) off the sea. This ray recomputes that in-tree (B1:
`C_sea=0` exactly; off-sea mean `C≈0.73`) and then asks the **index/topology** questions
the holonomy note did not.

- **B2 — no native topological charge `Q` (decisive, sharper-than-expected).** A single
  realized state carries ONE induced holonomy (one SU(3) element, one det-phase mod 2π),
  hence **winding 0**. A *nonzero* winding appears ONLY when the state is transported
  around a **non-contractible loop through OTHER states** (a genuinely closed loop,
  `U(2π)=I` verified), and the value is a property of the **chosen path**, not of any
  realized state — it varies erratically with the loop generator (`{rank 1,2,4,5}` →
  windings `{1,−1,−1,0}`; rank-dependence is not even monotone). So any nonzero `Q` is
  **realized-PATH / choice data** — an *even weaker* basis than realized-state data — not
  a state invariant and not an A_min derivation.
- **B3 — REGISTERED-DATA verdict on `C` (counterfactual clause).** `C` is **not**
  invariant over the law-admissible realized-state family: it is `0` on the sea and `>0`
  off it (spread `≈0.93`). The LAW (A_min) admits **both** flat and curved states; the
  value is fixed by **which** state is realized, not by the law ⇒ the off-sea curvature is
  **registered data** (`realized_state_primitive`, counterfactual clause), exactly as the
  honesty/registered-data guards require — **not** an A_min-native derivation.
- **B4 — wrong KIND of object for `χ`.** `C` (and the det-phase) is a **local** connection
  invariant, not a quantized topological index: continuously perturbing the off-sea state
  moves `C` **continuously** (no quantized jumps; `dC` grows smoothly with the perturbation
  size). A native `χ`/`Q` would be integer-valued and locally constant — `C` is neither.

**Residuals surfaced and fixed mid-cycle.** The runner first reported a spurious winding
`Q≈4.77` because a random Hermitian loop generator does **not** close (`exp(2πiA)≠I`);
switching to an integer-spectrum generator closed the loop and exposed the real,
path-dependent finding above. A tautological `≥0.0` check at B4 was replaced by the genuine
continuity probe.

### PRONG C — lattice disclination: a SQUARE-celled χ≠0 surface, but ADMITTED curvature (C1–C4, S3)

A **disclination** keeps square cells and locally-cubic vertex links but inserts an
**angular deficit** (a vertex whose link has ≠ 4 squares) — the combinatorial Gauss–Bonnet
curvature concentrated at points. This is the sharpest new prong: it stays square-celled
yet is NOT a product torus.

- **C1 — the witness.** The **cube surface** (boundary of a 3-cube: 8 vertices, 12 edges,
  6 **square** faces; every vertex link = 3 squares = an angular deficit, a disclination at
  all 8 corners) has `χ = 8−12+6 = 2`, KD index `= +2`, Betti `[1,0,1]`. This is a
  **second** genuine `χ≠0` mechanism, distinct from PR-D's tetra-S² (squares, not triangles).
- **C2 — combinatorial Gauss–Bonnet (in-tree).** `Σ_v (1 − faces_at_v/4) = χ`: the cube
  surface gives `8 × (1 − 3/4) = 2 = χ`. So `χ≠0` here is **exactly** concentrated
  disclination curvature — a genuine geometric-curvature mechanism, computed in-tree.
- **C3 — HONESTY GUARD (decisive).** A_min's Lattice axiom is the **infinite / periodic,
  translation-invariant** `Z³` adjacency: every vertex link = 4 squares, zero deficit,
  flat-cubic. A disclination is a vertex with ≠ 4 face-links ⇒ it **breaks translation
  invariance** ⇒ it is exactly the **admitted angular deficit (curvature)**, categorically
  OUTSIDE the flat-cubic Lattice axiom. Verified: the flat cubical torus has **every**
  vertex link = 4 (and `χ=0`); the cube surface has links of size 3.
- **C4 — enumeration.** All 16 faithful flat-cubic A_min tori (edge lengths 3..6): EVERY
  one has `χ=0` AND every vertex link = 4 squares (zero deficit). `χ≠0` is **unreachable**
  inside the translation-invariant flat-cubic family. (Mirrors PR-D's 28-tori enumeration,
  now with the per-vertex angular-deficit certificate.)

**Residual fixed mid-cycle (C4).** The enumeration first included degenerate `L=2` tori
(the A1a artifact); restricting to faithful edge lengths 3..6 fixed it.

## The wall — sharpened and re-localized (the deliverable)

PR-D re-localized the P-ABJ internal wall onto "A_min's flat-cubic Lattice axiom; the
consumer must ADMIT a curved (`χ≠0`) geometry." This ray **sharpens and broadens** that on
three independent new fronts, and adds the precise registered-data classification of the
induced-holonomy route:

> Across ALL THREE A_min-native fronts the ray names, `χ≠0` / `Q≠0` is either
> **UNREACHABLE** (the Z_τ time circle and any twisted Klein/Möbius gluing leave `χ=0` —
> `χ` is a cell count, gluing-invariant; and the faithful flat-cubic torus family is
> enumerated all-`χ=0`), or **REGISTERED DATA** (induced holonomy supplies a
> state-dependent **local** curvature `C`, not law-invariant, with **no** native
> topological charge — any winding is realized-path / choice data), or **ADMITTED
> curvature** (a disclined square complex genuinely has `χ=+2`, but a disclination breaks
> the **translation-invariant** flat-cubic Lattice axiom). The internal route is **not
> cracked**; the wall is re-confirmed and sharpened to a **single named geometric
> admission — the flat-cubic + translation-invariant Lattice axiom** — and the
> induced-holonomy curvature is precisely classified as **realized-state registered data,
> not an A_min derivation**.

Why this is sharper than PR-D:
1. **Disclination witness (square cells).** PR-D's `χ≠0` witness was the triangulated S²
   (an injected non-cubic triangulation). The cube surface is a **square-celled** `χ=+2`
   complex with locally-cubic links — closing the steelman "maybe a square/cubic-adjacency
   curved complex is native." It is not: it requires breaking translation invariance. The
   wall now reads explicitly as **translation-invariance**, not merely "non-cubic cell."
2. **Z_τ / twisted-gluing closure.** PR-D only did product tori. The Klein-bottle family
   shows that **any** identification/twist of the time circle leaves `χ` fixed (same
   f-vector ⇒ same `χ`), closing the "maybe a nontrivial cycle / twisted time gluing
   helps" gap with the structural reason (`χ` is a gluing-invariant cell count).
3. **Induced-holonomy registered-data classification (the registered-data guard, executed).**
   The induced curvature `C` is shown to be (i) a **local** connection invariant (continuous,
   non-quantized), (ii) carrying **no** native topological charge (single-state winding 0;
   any winding is path-choice data), and (iii) **not** law-admissible-invariant ⇒
   **registered data**, precisely as the ray's registered-data guard demanded. This converts
   the most tempting "matter-state-induced curvature might crack it" hope into a clean,
   correctly-classified non-derivation.

## Honest status

- **Internal route: SHARPER NO-GO (no native crack).** A genuine A_min-native `χ≠0` would
  have cracked the internal route — it does not exist. The two genuine `χ≠0` mechanisms
  (the cube-surface disclination; PR-D's S²) both require **admitted curvature** (broken
  translation invariance); the Z_τ time circle and its twisted gluings cannot move `χ`; the
  induced-holonomy curvature is **realized-state registered data** with no native charge.
- **Registered-data check (explicit).** Induced-holonomy `C` is realized-state-DEPENDENT
  (spread `0→0.93` over the law-admissible state family) ⇒ registered data per the
  counterfactual clause, **not** a derivation. Any induced topological winding `Q` is
  realized-PATH / choice data (weaker still). The flat-cubic enumeration and the
  gluing-invariance of `χ` are, by contrast, **law-admissible invariants** (true for the
  entire family) — and they say `χ=0`.
- **Honesty / firewall discipline (block02 R-C preserved).** Every `χ≠0` object is read off
  its **own** f-vector with **zero** gauge field — no injected triangulation, boundary
  twist, or transition function. `Q` is the winding of the **derived** induced holonomy with
  zero injected twist. No empirical/observed values imported. No new axiom or primitive.
- **External premise unchanged.** P-ABJ/P1 B2 (the Adler–Bell–Jackiw
  anomaly-to-inconsistency implication) remains a categorically external admission, not
  derivable from A_min by policy. This ray does not touch it; it works only the internal
  open ray.
- **Load-bearing residuals (the discipline working).** The runner caught **four** real
  residual errors mid-cycle — two cubical-torus degeneracies at `L=2`, a spurious det-phase
  winding from a non-closing loop, and a tautological check — and in fixing the winding
  probe surfaced the genuinely sharper finding that the induced winding is realized-path /
  choice data. Each is documented in-tree, not hidden.

## What this unlocks on the 1105 cone

No audit movement claimed (independent audit lane is sole authority; nothing under
`docs/audit/**` touched). Audit-relevant content for the consolidation note:

1. **Re-localize the P-ABJ internal-route wall** from "flat-cubic Lattice axiom" to the
   sharper, fuller **"flat-cubic + translation-invariant Lattice axiom"** — a single named
   geometric admission that now also fences (a) the Z_τ / twisted-gluing route (`χ` is a
   gluing-invariant cell count) and (b) the square-celled-disclination route (the cube
   surface is `χ=+2` but breaks translation invariance).
2. **Classify the induced-holonomy route as registered data, definitively.** The most
   tempting internal candidate (`INDUCED_HOLONOMY_...` derived curvature) gives a
   **local**, **state-dependent**, **non-quantized** `C` with **no** native topological
   charge — `realized_state` registered data, not a derivation. This closes the
   "matter-state-induced curvature might supply `χ`/`Q`" steelman with a precise
   registered-data verdict, ready for the audit lane to fence.
3. **Non-vacuity re-witnessed in two cell types.** `χ=+2` is exhibited on a **square-celled**
   complex (cube surface) in addition to PR-D's triangulated S², so the wall is
   demonstrably NOT vacuity in either cell convention — answered the same way: such
   complexes exist, none is A_min-native.

## Firewall / forbidden-surface attestation

New artifacts only: this section, the runner
`scripts/frontier_abj_chi_native_curvature_routes_2026_06_20.py`, and its cache
`logs/runner-cache/frontier_abj_chi_native_curvature_routes_2026_06_20.txt`. **No file under
`docs/audit/`, `docs/publication/`, AUDIT_LEDGER/QUEUE, MISSING_DERIVATION_PROMPTS was
edited.** `docs/audit/data/` was treated READ-ONLY. No row/effective status set; no audit
verdict asserted; no `Type:` / `Claim type:` / bare retained/promoted standing claimed. The
independent audit lane is the sole status authority before any effective-retained movement.
No `git checkout/commit/push/fetch` was run (orchestrator owns git). The keystone and parent
are NOT cited as authority for any load-bearing fact — every load-bearing claim (KD index = χ
on S²; gluing-invariance of χ; the Klein-bottle family; the cube-surface disclination χ=+2
and its Gauss–Bonnet certificate; the faithful flat-cubic enumeration; the induced-holonomy
two-pole dichotomy, registered-data spread, and path-dependent winding) is recomputed in-tree
with explicit residuals and a `TOTAL: PASS=23 FAIL=0` line.
